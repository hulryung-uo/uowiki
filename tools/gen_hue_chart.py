# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow"]
# ///
"""Generate the Hue Reference page art: a full-palette chart, labeled swatches
for notable craft-resource hues, and "same sprite, different hue" demo ingots.

A UO *hue* is a 1-based index into hues.mul; each hue is a 32-shade gradient
(ARGB1555) that remaps a grayscale sprite's shadow->highlight ramp. This script
reuses the exact hues.mul parsing from tools/apply_hues.py (HueGroup = 4-byte
header + 8 * 88-byte entries; 32 uint16 colors per entry; game hue N -> file
index N-1) and the CraftResource hue table from ServUO for naming.

    uv run --script tools/gen_hue_chart.py

Outputs (all under public/img/hues/, plus data/hue_notable.json):
  chart.png            full palette grid (mid-tone of every hue)
  h-<HUE>.png          labeled 32-shade ramp swatch per notable hue
  demo-<HUE>.png       ingot art 0x1BF2 tinted by each notable metal hue
"""

from __future__ import annotations

import json
import struct
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
HUES_MUL = ROOT.parent / "uo-resource" / "hues.mul"
INGOT_SRC = ROOT / "public" / "img" / "items" / "0x1BF2.png"
OUT = ROOT / "public" / "img" / "hues"
NOTABLE_JSON = ROOT / "data" / "hue_notable.json"

# ARGB1555 ramp has 32 shades 0..31 (shadow -> highlight). Pick a representative
# mid/upper-mid tone for the palette grid and single-swatch previews.
MID_INDEX = 24

# Notable hues, sourced from servuo Scripts/Misc/ResourceInfo.cs CraftResourceInfo
# tables. (kind, name, game hue). Metals first so the demo row reads Iron + 8.
NOTABLE = [
    ("metal", "Iron", 0x000),
    ("metal", "Dull Copper", 0x973),
    ("metal", "Shadow Iron", 0x966),
    ("metal", "Copper", 0x96D),
    ("metal", "Bronze", 0x972),
    ("metal", "Gold", 0x8A5),
    ("metal", "Agapite", 0x979),
    ("metal", "Verite", 0x89F),
    ("metal", "Valorite", 0x8AB),
    ("leather", "Spined", 0x283),
    ("leather", "Horned", 0x227),
    ("leather", "Barbed", 0x1C1),
    ("scale", "Red Scales", 0x66D),
    ("scale", "Yellow Scales", 0x8A8),
    ("scale", "Black Scales", 0x455),
    ("scale", "Green Scales", 0x851),
    ("scale", "White Scales", 0x8FD),
    ("scale", "Blue Scales", 0x8B0),
    ("wood", "Oak", 0x7DA),
    ("wood", "Ash", 0x4A7),
    ("wood", "Yew", 0x4A8),
    ("wood", "Heartwood", 0x4A9),
    ("wood", "Bloodwood", 0x4AA),
    ("wood", "Frostwood", 0x47F),
]


def load_hues() -> list[list[tuple[int, int, int]]]:
    """hues.mul -> list indexed by file hue index, each a 32-entry RGB table.

    Mirrors tools/apply_hues.py exactly: HueGroup = 4-byte header + 8 entries of
    88 bytes; each entry is 32 little-endian uint16 ARGB1555 colors.
    """
    data = HUES_MUL.read_bytes()
    GROUP = 708  # 4-byte header + 8 * 88-byte entries
    hues: list[list[tuple[int, int, int]]] = []
    for g in range(len(data) // GROUP):
        base = g * GROUP + 4
        for e in range(8):
            off = base + e * 88
            colors = struct.unpack_from("<32H", data, off)
            table = []
            for c in colors:
                r = (c >> 10) & 0x1F
                g5 = (c >> 5) & 0x1F
                b = c & 0x1F
                table.append(((r << 3) | (r >> 2), (g5 << 3) | (g5 >> 2), (b << 3) | (b >> 2)))
            hues.append(table)
    return hues


def hue_table(hues, game_hue: int) -> list[tuple[int, int, int]] | None:
    """game hue N -> file index N-1; hue 0 has no gradient (means 'unhued')."""
    idx = (game_hue & 0x3FFF) - 1
    if 0 <= idx < len(hues):
        return hues[idx]
    return None


def gen_chart(hues) -> tuple[int, int, int]:
    """Full palette grid: one MID_INDEX swatch per game hue 1..N.

    Returns (hue_count, width, height).
    """
    cell = 14
    cols = 40
    n = len(hues)
    rows = (n + cols - 1) // cols
    pad = 1  # outer border
    w = cols * cell + 2 * pad
    h = rows * cell + 2 * pad
    img = Image.new("RGB", (w, h), (24, 24, 28))
    px = img.load()
    grid = (60, 60, 68)
    for i in range(n):
        col = i % cols
        row = i // cols
        x0 = pad + col * cell
        y0 = pad + row * cell
        r, g, b = hues[i][MID_INDEX]
        for y in range(y0, y0 + cell):
            for x in range(x0, x0 + cell):
                px[x, y] = (r, g, b)
    # thin gridlines every 8 columns / rows for orientation
    for col in range(0, cols + 1, 8):
        x = min(pad + col * cell, w - 1)
        for y in range(h):
            px[x, y] = grid
    for row in range(0, rows + 1, 8):
        y = min(pad + row * cell, h - 1)
        for x in range(w):
            px[x, y] = grid
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / "chart.png")
    return n, w, h


def gen_swatch(table, game_hue: int) -> None:
    """48x48 swatch showing the full 32-shade ramp as horizontal strips."""
    size = 48
    img = Image.new("RGB", (size, size), (0, 0, 0))
    px = img.load()
    for y in range(size):
        # map row -> ramp index 0..31 (shadow at top, highlight at bottom)
        idx = min(31, y * 32 // size)
        r, g, b = table[idx]
        for x in range(size):
            px[x, y] = (r, g, b)
    img.save(OUT / f"h-0x{game_hue:04X}.png")


def gen_demo(table, game_hue: int) -> None:
    """Tint the ingot sprite 0x1BF2 by remapping its R channel through the ramp,
    same technique as apply_hues.apply_hue."""
    im = Image.open(INGOT_SRC).convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            nr, ng, nb = table[r >> 3]
            px[x, y] = (nr, ng, nb, a)
    im.save(OUT / f"demo-0x{game_hue:04X}.png")


def main() -> None:
    hues = load_hues()
    OUT.mkdir(parents=True, exist_ok=True)

    n, w, h = gen_chart(hues)
    print(f"chart.png: {n} hues, {w}x{h}px")

    notable_out = []
    demos = 0
    for kind, name, game_hue in NOTABLE:
        table = hue_table(hues, game_hue)
        if table is None:
            print(f"  WARN no gradient for {name} 0x{game_hue:04X}; skipping")
            continue
        gen_swatch(table, game_hue)
        entry = {
            "kind": kind,
            "name": name,
            "hue": f"0x{game_hue:04X}",
            "hue_dec": game_hue,
            "swatch": f"/img/hues/h-0x{game_hue:04X}.png",
        }
        # demo ingot only makes sense for metals (the ingot sprite)
        if kind == "metal":
            gen_demo(table, game_hue)
            entry["demo"] = f"/img/hues/demo-0x{game_hue:04X}.png"
            demos += 1
        notable_out.append(entry)

    NOTABLE_JSON.parent.mkdir(parents=True, exist_ok=True)
    json.dump(
        {"hue_count": n, "notable": notable_out},
        open(NOTABLE_JSON, "w"),
        ensure_ascii=False,
        indent=1,
    )
    print(f"notable swatches: {len(notable_out)} ({demos} metal demos)")
    print(f"wrote {NOTABLE_JSON.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
