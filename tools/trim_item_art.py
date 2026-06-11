# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow"]
# ///
"""Trim transparent padding from item art PNGs.

UO static-art tiles place the graphic within a larger canvas with an in-world
draw offset, leaving big transparent margins (e.g. a skullcap's art is 11x15
inside a 49x32 canvas). For icon display we want the art to fill its frame, so
every PNG is cropped to its alpha bounding box. Idempotent — already-tight PNGs
are left alone. Run after extract_art.py / extract_items.py.

    python3 tools/trim_item_art.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ITEMS = Path(__file__).resolve().parent.parent / "public" / "img" / "items"
MARGIN = 1  # px of transparent breathing room kept around the art


def main() -> None:
    trimmed = skipped = blank = 0
    for png in sorted(ITEMS.glob("*.png")):
        im = Image.open(png).convert("RGBA")
        bbox = im.split()[-1].getbbox()  # bounds of non-transparent alpha
        if bbox is None:
            blank += 1
            continue
        l, t, r, b = bbox
        l = max(0, l - MARGIN); t = max(0, t - MARGIN)
        r = min(im.width, r + MARGIN); b = min(im.height, b + MARGIN)
        if (l, t, r, b) == (0, 0, im.width, im.height):
            skipped += 1
            continue
        im.crop((l, t, r, b)).save(png)
        trimmed += 1
    print(f"trimmed {trimmed}, already-tight {skipped}, fully-transparent {blank}")


if __name__ == "__main__":
    main()
