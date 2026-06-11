# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render isometric house exterior PNGs from client multi + static art.

A "multi" is a list of static tiles {itemID, x, y, z, flags}. We read the
multi table (multi.mul + multi.idx), then draw each tile's STATIC art (the
same item art used elsewhere, decoded by tools/extract_art.decode_static_art)
at its isometric screen position, painter-sorted so nearer tiles overdraw
farther ones. The result is cropped to content and written to
public/img/houses/<multi_id-hex>.png.

Multi format (confirmed against ClassicUO src/ClassicUO.Assets/MultiLoader.cs):
  multi.idx: 12-byte entries {i32 lookup/offset, i32 length, i32 extra}.
  multi.mul: for each multi, `length / record_size` records. Modern clients
    (CV_7090+, which these MUL files are — 16-byte records) store each record
    as: u16 ID, i16 X, i16 Y, i16 Z, u16 Flags, u32 Unknown (16 bytes total).
    The loader reads the first 12 bytes as {ID,X,Y,Z,Flags(u32)} then skips the
    remainder. Flags != 0 means visible (old format); 0 / 0x100 visible (new).
  Static art is at art index itemID + 0x4000.

Isometric projection (standard UO 44x44 tile, half = 22):
  screenX = (x - y) * 22
  screenY = (x + y) * 22 - z * 4
Tiles are drawn from far (low x+y, low z) to near (high x+y, high z) so the
near ones paint over the far ones. Static art is anchored by its lower edge:
each art image of size (w, h) is blitted at (screenX - w/2, screenY - h + 44)
relative to the tile's ground point, matching how the client seats statics.
"""

import os
import struct
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib
from extract_art import decode_static_art

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
ART_PATTERN = "build/artlegacymul/%08d.tga"
STATIC_OFFSET = 0x4000

TILE_HALF = 22   # half of the 44px iso tile diamond
Z_STEP = 4       # screen pixels per z unit


def read_multi(idx: bytes, mul: bytes, multi_id: int):
    """Return list of (itemID, x, y, z, visible) for a multi, or None."""
    off_pos = multi_id * 12
    if off_pos + 12 > len(idx):
        return None
    offset, length, _extra = struct.unpack_from("<iii", idx, off_pos)
    if offset < 0 or length <= 0 or offset + length > len(mul):
        return None
    # detect record size: these MUL files use 16-byte records (new format).
    rec = 16 if length % 16 == 0 else 12
    count = length // rec
    tiles = []
    for i in range(count):
        base = offset + i * rec
        item_id, x, y, z, flags = struct.unpack_from("<Hhhhi", mul, base)
        # itemID 0/1 are the "no draw" foundation/placeholder tiles — always
        # skip. For real tiles we draw regardless of the flag word (these MUL
        # files mix flags 0 and 1 on visible structural tiles, e.g. doors are
        # flagged 0); the flag here is not a reliable visibility gate.
        if item_id <= 1:
            continue
        tiles.append((item_id, x, y, z, True))
    return tiles


def render_multi(tiles, uop, art_cache):
    """Composite tiles into a cropped RGBA image, or None if nothing drew."""
    placed = []  # (sort_key, screenX, screenY, img)
    for item_id, x, y, z, visible in tiles:
        if not visible:
            continue
        key = item_id + STATIC_OFFSET
        if key in art_cache:
            img = art_cache[key]
        else:
            entry = uop.get_by_name(ART_PATTERN % key)
            img = decode_static_art(uop.read(entry)) if entry else None
            art_cache[key] = img
        if img is None:
            continue
        sx = (x - y) * TILE_HALF
        sy = (x + y) * TILE_HALF - z * Z_STEP
        # painter order: back-to-front by (x+y), then z, then itemID
        placed.append(((x + y, z, item_id), sx, sy, img))

    if not placed:
        return None

    placed.sort(key=lambda p: p[0])

    # compute bounds. Art is anchored with its bottom at the tile's south
    # corner: blit top-left at (sx - w/2, sy - h + TILE_HALF*2).
    minx = miny = 10**9
    maxx = maxy = -10**9
    boxes = []
    for _k, sx, sy, img in placed:
        w, h = img.size
        # seat each static: horizontally centered on the tile's screen point,
        # bottom edge resting on it (statics grow upward from the floor).
        bx = sx - w // 2
        by = sy - h
        boxes.append((bx, by, img))
        minx = min(minx, bx); miny = min(miny, by)
        maxx = max(maxx, bx + w); maxy = max(maxy, by + h)

    W, H = maxx - minx, maxy - miny
    if W <= 0 or H <= 0 or W > 6000 or H > 6000:
        return None
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for bx, by, img in boxes:
        canvas.alpha_composite(img, (bx - minx, by - miny))

    # crop to non-transparent content
    bbox = canvas.getbbox()
    if bbox:
        canvas = canvas.crop(bbox)
    return canvas


def main(argv):
    # which multis to render: passed as hex args, else the classic house set
    if len(argv) > 1:
        ids = [int(a, 16) for a in argv[1:]]
    else:
        # classic house multi IDs from data/houses.json
        import json
        d = json.load(open(os.path.join(ROOT, "data", "houses.json")))
        ids = [int(r["multi_id"], 16) for r in d["classic"]
               if r.get("multi_id")]

    idx = open(os.path.join(UO_DIR, "multi.idx"), "rb").read()
    mul = open(os.path.join(UO_DIR, "multi.mul"), "rb").read()
    uop = uoplib.UopFile(os.path.join(UO_DIR, "artLegacyMUL.uop"))

    out_dir = os.path.join(ROOT, "public", "img", "houses")
    os.makedirs(out_dir, exist_ok=True)

    art_cache = {}
    written = []
    failed = []
    for mid in ids:
        tiles = read_multi(idx, mul, mid)
        if not tiles:
            failed.append((mid, "no multi record"))
            continue
        img = render_multi(tiles, uop, art_cache)
        if img is None:
            failed.append((mid, "nothing rendered"))
            continue
        name = f"0x{mid:X}.png"
        img.save(os.path.join(out_dir, name))
        written.append((mid, img.size, len(tiles)))

    for mid, size, ntiles in written:
        print(f"0x{mid:X}: {ntiles} tiles -> {size[0]}x{size[1]} px")
    for mid, why in failed:
        print(f"0x{mid:X}: FAILED ({why})")
    print(f"\nrendered {len(written)}/{len(ids)} multis")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
