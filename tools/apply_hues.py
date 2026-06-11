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


def grayscale_fraction(src: Path) -> float:
    """Fraction of opaque pixels whose channel spread max-min <= 16.

    Near-gray art (meant to be hued) scores ~1.0; already-colored art (potions,
    pre-tinted sprites) scores low. Returns 0.0 if there are no opaque pixels.
    """
    im = Image.open(src).convert("RGBA")
    px = im.load()
    opaque = 0
    gray = 0
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            opaque += 1
            if max(r, g, b) - min(r, g, b) <= 16:
                gray += 1
    if opaque == 0:
        return 0.0
    return gray / opaque


GRAY_THRESHOLD = 0.85  # >= this fraction of near-gray pixels => safe to bake


def main() -> None:
    class_hues = parse_class_hues()
    hues = load_hues()
    doc = json.load(open(ITEMS_JSON))
    made = 0            # newly baked or reused hued sprites pointed at this run
    craft_seen = 0      # items whose hue came from the CraftResource table
    literal_seen = 0    # items whose hue came from item_hue (a literal in source)
    craft_baked = 0     # of those, baked (art was grayscale)
    literal_baked = 0
    skipped_color = 0   # had a hue but art was already colored -> left untinted
    skipped_idx = 0     # hue index out of range / no art
    gray_cache: dict[str, float] = {}  # item_id -> grayscale fraction (cache)
    for it in doc["items"]:
        # Prefer the CraftResource hue (metals/leather/scales); otherwise fall
        # back to the item's own literal Hue assignment.
        craft_hue = class_hues.get(it["class"])
        if craft_hue:
            hue = craft_hue
            from_craft = True
        else:
            ih = it.get("item_hue")
            hue = int(ih, 0) if ih else None
            from_craft = False
        if not hue:  # no craft hue and no literal item_hue -> keep base sprite
            continue
        idx = (hue & 0x3FFF) - 1
        if not (0 <= idx < len(hues)):
            skipped_idx += 1
            continue
        base = IMG / f"{it['item_id']}.png"  # always the untinted sprite (idempotent)
        if not base.exists():
            skipped_idx += 1
            continue

        if from_craft:
            craft_seen += 1
        else:
            literal_seen += 1

        # Grayscale guard: only tint art that is (almost) entirely gray, so we
        # never double-tint art that already carries its color (potions, dyed
        # sprites). This applies ONLY to the literal item_hue fallback path.
        #
        # CraftResource sprites (metals/leather/logs/ore/scales) are EXEMPT:
        # several of those base sprites are not strictly gray (e.g. iron ingot
        # art 0x1BF2 is a bluish-gray), yet UO tints them by remapping the R
        # channel through the hue ramp — that is the long-standing, correct
        # resource-coloring behavior these PNGs depend on. Guarding them would
        # drop the 48 existing resource hues (Valorite ingots, etc.).
        if not from_craft:
            frac = gray_cache.get(it["item_id"])
            if frac is None:
                frac = grayscale_fraction(base)
                gray_cache[it["item_id"]] = frac
            if frac < GRAY_THRESHOLD:
                skipped_color += 1
                continue

        out_name = f"{it['item_id']}-h{hue:04X}.png"
        out_path = IMG / out_name
        if not out_path.exists():  # same sprite+hue dedupes across items
            apply_hue(base, out_path, hues[idx])
        it["png"] = f"/img/items/{out_name}"
        it["hue"] = f"0x{hue:04X}"
        made += 1
        if from_craft:
            craft_baked += 1
        else:
            literal_baked += 1
    json.dump(doc, open(ITEMS_JSON, "w"), ensure_ascii=False, indent=1)
    print(f"{len(class_hues)} classes have a craft hue")
    print(f"items with a literal item_hue : "
          f"{sum(1 for it in doc['items'] if it.get('item_hue'))}")
    print(f"  craft-hued items seen       : {craft_seen}")
    print(f"  literal-hued items seen     : {literal_seen}")
    print(f"baked/pointed (gray art)      : {made} "
          f"(craft={craft_baked}, literal={literal_baked})")
    print(f"skipped (already colored art) : {skipped_color}")
    print(f"skipped (no art / bad hue idx): {skipped_idx}")
    total_hued_pngs = len(list(IMG.glob("*-h*.png")))
    print(f"total hued PNGs on disk       : {total_hued_pngs}")


if __name__ == "__main__":
    main()
