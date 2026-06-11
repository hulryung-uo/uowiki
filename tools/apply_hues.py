# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow"]
# ///
"""Bake UO hues into colored-variant resource sprites.

Many items share one grayscale sprite and differ only by a UO *hue* — e.g. all
nine ingot colors use art 0x1BF2, tinted by the metal's hue (Valorite 0x8AB,
Agapite 0x979, ...). UO hues are not a flat tint: each remaps the sprite's gray
ramp through a 32-color gradient in hues.mul, so CSS filters can't reproduce
them. This reads the CraftResource→hue table from ServUO and the gradients from
hues.mul, then writes a properly tinted PNG per hued resource class and points
data/items.json at it.

    python3 tools/apply_hues.py    # run after extract_items.py + trim_item_art.py
"""

from __future__ import annotations

import json
import re
import struct
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SERVUO = ROOT.parent / "servuo"
RESOURCE_INFO = SERVUO / "Scripts" / "Misc" / "ResourceInfo.cs"
HUES_MUL = ROOT.parent / "uo-resource" / "hues.mul"
ITEMS_JSON = ROOT / "data" / "items.json"
IMG = ROOT / "public" / "img" / "items"


def parse_class_hues() -> dict[str, int]:
    """class name -> game hue, from CraftResourceInfo(hue, ..., typeof(X), ...).
    First occurrence wins (the leather table lists each type once with its item hue)."""
    out: dict[str, int] = {}
    for line in RESOURCE_INFO.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.search(r"new\s+CraftResourceInfo\(\s*(0x[0-9A-Fa-f]+|\d+)\s*,", line)
        if not m:
            continue
        hue = int(m.group(1), 0)
        for t in re.findall(r"typeof\(\s*(\w+)\s*\)", line):
            out.setdefault(t, hue)  # first table that lists a type wins
    return out


def load_hues() -> list[list[tuple[int, int, int]]]:
    """hues.mul -> list indexed by file hue index, each a 32-entry RGB table."""
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
                r = ((c >> 10) & 0x1F); g5 = ((c >> 5) & 0x1F); b = c & 0x1F
                table.append(((r << 3) | (r >> 2), (g5 << 3) | (g5 >> 2), (b << 3) | (b >> 2)))
            hues.append(table)
    return hues


def apply_hue(src: Path, dst: Path, table: list[tuple[int, int, int]]) -> None:
    im = Image.open(src).convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            nr, ng, nb = table[r >> 3]  # gray sprite: R holds the 5-bit ramp index
            px[x, y] = (nr, ng, nb, a)
    im.save(dst)


def main() -> None:
    class_hues = parse_class_hues()
    hues = load_hues()
    doc = json.load(open(ITEMS_JSON))
    made = 0
    for it in doc["items"]:
        hue = class_hues.get(it["class"])
        if not hue:  # unknown class or hue 0 (Iron / Normal) -> keep base sprite
            continue
        idx = (hue & 0x3FFF) - 1
        if not (0 <= idx < len(hues)):
            continue
        base = IMG / f"{it['item_id']}.png"  # always the untinted sprite (idempotent)
        if not base.exists():
            continue
        out_name = f"{it['item_id']}-h{hue:04X}.png"
        apply_hue(base, IMG / out_name, hues[idx])
        it["png"] = f"/img/items/{out_name}"
        it["hue"] = f"0x{hue:04X}"
        made += 1
    json.dump(doc, open(ITEMS_JSON, "w"), ensure_ascii=False, indent=1)
    print(f"baked {made} hued sprites; {len(class_hues)} classes have a craft hue")


if __name__ == "__main__":
    main()
