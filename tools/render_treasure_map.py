# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render treasure-hunting images for the UO wiki.

Outputs:
  public/img/treasure/locations.png    -- 193 classic dig sites plotted on Felucca
  public/img/treasure/example-map.png  -- an example decoded treasure-map gump

Reuses:
  - gen_maps.py's base image + 1px==1 UO unit coordinate mapping
  - render_ui.py / uoplib gump decoder for the client parchment art (gump 0x139D)

Sources (read-only):
  - Base map:  /Users/dkkang/dev/uo/uomap/images/map_felucca.png (7170x4098, 1px/UO unit)
  - Sites:     data/treasure.json (from tools/extract_treasure.py)
  - Parchment: /Users/dkkang/dev/uo/uo-resource/gumpartLegacyMUL.uop, gump 0x139D
               (the map-window background tile the client uses for decoded maps;
               ServUO MapItem.cs sends 0x139D as the map background)

Run:  uv run --script tools/render_treasure_map.py
"""

import json
import os
import struct
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIKI = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI / "tools"))
import uoplib  # noqa: E402

MAP_PNG = Path("/Users/dkkang/dev/uo/uomap/images/map_felucca.png")
TREASURE_JSON = WIKI / "data" / "treasure.json"
OUT_DIR = WIKI / "public" / "img" / "treasure"

UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
GUMP_UOP = os.path.join(UO_DIR, "gumpartLegacyMUL.uop")
GUMP_PATTERN = "build/gumpartlegacymul/%08d.tga"
PARCHMENT_GUMP = 0x139D  # map-window background tile (MapItem.cs)

UO_W, UO_H = 7170, 4098  # felucca image == UO coordinate space (gen_maps.py)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# Britannia (Felucca/Trammel) coordinate bounds: 0..5119 x 0..4095.
BRIT_W, BRIT_H = 5120, 4096

# Overview output width (downscaled from the 5120-wide Britannia crop).
OVERVIEW_WIDTH = 1500

# Example decoded map: ~600 UO-unit regional crop (TreasureMap.GetWidthAndHeight
# uses width=height=600 for Trammel/Felucca).
EXAMPLE_WINDOW = 600


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD, size)


# --------------------------------------------------------------- gump decoder
# (same RLE decoder as render_ui.py / extract_spell_icons.py)

def decode_gump(uop: uoplib.UopFile, gump_id: int) -> Image.Image:
    entry = uop.get_by_name(GUMP_PATTERN % gump_id)
    if entry is None:
        raise KeyError(f"gump 0x{gump_id:04X} not present")
    payload = uop.read(entry)
    if entry.flag == uoplib.FLAG_NONE:
        w, h = entry.extra1, entry.extra2
    else:
        w, h = struct.unpack_from("<II", payload, 0)
        payload = payload[8:]
    row_lookup = struct.unpack_from("<%di" % h, payload, 0)
    total_words = len(payload) // 4
    tbl = uoplib.COLOR_TABLE_5TO8
    out = bytearray(w * h * 4)
    for y in range(h):
        pos = row_lookup[y] * 4
        gsize = (row_lookup[y + 1] if y < h - 1 else total_words) - row_lookup[y]
        x = 0
        for _ in range(gsize):
            value, run = struct.unpack_from("<HH", payload, pos)
            pos += 4
            if value != 0:
                r = tbl[(value >> 10) & 0x1F]
                g = tbl[(value >> 5) & 0x1F]
                b = tbl[value & 0x1F]
                px = struct.pack("<4B", r, g, b, 255)
                base = (y * w + x) * 4
                out[base:base + run * 4] = px * run
            x += run
    return Image.frombytes("RGBA", (w, h), bytes(out))


def tile_parchment(uop: uoplib.UopFile, w: int, h: int) -> Image.Image:
    """Tile the client map-window parchment art (0x139D) to fill w x h."""
    tile = decode_gump(uop, PARCHMENT_GUMP).convert("RGBA")
    out = Image.new("RGBA", (w, h))
    for ty in range(0, h, tile.height):
        for tx in range(0, w, tile.width):
            out.alpha_composite(tile, (tx, ty))
    return out


# --------------------------------------------------------------- markers

def draw_x(draw, px, py, r, fill, outline="#ffffff", width=2):
    """Draw an X treasure marker centered at (px, py)."""
    draw.line((px - r, py - r, px + r, py + r), fill=outline, width=width + 2)
    draw.line((px - r, py + r, px + r, py - r), fill=outline, width=width + 2)
    draw.line((px - r, py - r, px + r, py + r), fill=fill, width=width)
    draw.line((px - r, py + r, px + r, py - r), fill=fill, width=width)


def draw_legend(draw, items, font, x=14, y=14):
    pad, row_h, sw = 12, 26, 16
    tw = max(draw.textbbox((0, 0), lab, font=font)[2] for _, lab in items)
    w = pad * 2 + sw + 10 + tw
    h = pad * 2 + row_h * len(items) - 8
    draw.rectangle((x, y, x + w, y + h), fill=(15, 15, 20, 220), outline="#cccccc")
    for i, (color, lab) in enumerate(items):
        cy = y + pad + i * row_h + 8
        draw_x(draw, x + pad + sw // 2, cy, 7, color)
        draw.text((x + pad + sw + 10, cy - 9), lab, font=font, fill="#ffffff",
                  stroke_width=1, stroke_fill="#111111")


# --------------------------------------------------------------- locations.png

def render_locations(base: Image.Image, locations: list[dict], out_path: Path):
    """Crop to Britannia bounds, plot all classic dig sites as X markers."""
    crop = base.crop((0, 0, BRIT_W, BRIT_H))  # 1px==1 UO unit
    scale = OVERVIEW_WIDTH / crop.width
    img = crop.resize((OVERVIEW_WIDTH, round(crop.height * scale)), Image.LANCZOS)
    img = img.convert("RGBA")
    draw = ImageDraw.Draw(img, "RGBA")

    on_map = 0
    for e in locations:
        ux, uy = e["x"], e["y"]
        if not (0 <= ux < BRIT_W and 0 <= uy < BRIT_H):
            continue
        px, py = ux * scale, uy * scale
        draw_x(draw, px, py, 5, "#facc15")  # gold X
        on_map += 1

    title_font = load_font(26)
    draw.text((OVERVIEW_WIDTH - 470, img.height - 40),
              f"{on_map} classic treasure dig sites",
              font=title_font, fill="#ffffff", stroke_width=2, stroke_fill="#111111")
    draw_legend(draw, [("#facc15", "Classic dig site")], load_font(18))

    img.convert("RGB").save(out_path, optimize=True)
    print(f"wrote {out_path.relative_to(WIKI)}  ({on_map} sites plotted)")
    return on_map


# --------------------------------------------------------------- example-map.png

def render_example(base: Image.Image, uop: uoplib.UopFile, spot: dict, out_path: Path):
    """Crop a ~EXAMPLE_WINDOW regional view around `spot`, frame it with the
    client parchment art, draw a red pin at the dig spot."""
    ux, uy = spot["x"], spot["y"]
    # The game offsets the dig spot within the window rather than centering it
    # (TreasureMap.cs: x1 = ChestLocation.X - RandomMinMax(width/4, 3*width/4)),
    # so the pin sits off-centre and you must read the surrounding terrain to
    # pinpoint it. Reproduce that with a fixed off-centre placement.
    off_x = int(EXAMPLE_WINDOW * 0.38)
    off_y = int(EXAMPLE_WINDOW * 0.60)
    cx1 = max(0, min(ux - off_x, BRIT_W - EXAMPLE_WINDOW))
    cy1 = max(0, min(uy - off_y, BRIT_H - EXAMPLE_WINDOW))
    cx2 = cx1 + EXAMPLE_WINDOW
    cy2 = cy1 + EXAMPLE_WINDOW

    region = base.crop((cx1, cy1, cx2, cy2)).convert("RGBA")
    # Upscale the regional view for legibility.
    view_scale = 1.0
    if region.width < 520:
        view_scale = 520 / region.width
        region = region.resize(
            (round(region.width * view_scale), round(region.height * view_scale)),
            Image.LANCZOS)

    # Parchment frame: a border of tiled map-window art around the region.
    border = 46
    fw = region.width + border * 2
    fh = region.height + border * 2
    frame = tile_parchment(uop, fw, fh)

    # Inset shadow + the regional map.
    draw = ImageDraw.Draw(frame, "RGBA")
    draw.rectangle((border - 3, border - 3, border + region.width + 2,
                    border + region.height + 2), outline=(60, 40, 20, 255), width=3)
    frame.alpha_composite(region, (border, border))

    # Red pin at the dig spot, in framed coordinates.
    draw = ImageDraw.Draw(frame, "RGBA")
    pin_x = border + (ux - cx1) * view_scale
    pin_y = border + (uy - cy1) * view_scale
    r = 9
    draw.line((pin_x - r, pin_y - r, pin_x + r, pin_y + r), fill="#ffffff", width=6)
    draw.line((pin_x - r, pin_y + r, pin_x + r, pin_y - r), fill="#ffffff", width=6)
    draw.line((pin_x - r, pin_y - r, pin_x + r, pin_y + r), fill="#dc2626", width=4)
    draw.line((pin_x - r, pin_y + r, pin_x + r, pin_y - r), fill="#dc2626", width=4)
    draw.ellipse((pin_x - 3, pin_y - 3, pin_x + 3, pin_y + 3),
                 fill="#dc2626", outline="#ffffff", width=1)

    # Caption inside the lower parchment border.
    cap_font = load_font(18)
    cap = f"Decoded treasure map - dig near ({ux}, {uy}) on Felucca"
    bb = draw.textbbox((0, 0), cap, font=cap_font)
    cap_x = (fw - (bb[2] - bb[0])) // 2
    draw.text((cap_x, border + region.height + 12), cap, font=cap_font,
              fill="#2b1d0e", stroke_width=1, stroke_fill="#d8c08a")

    frame.convert("RGB").save(out_path, optimize=True)
    print(f"wrote {out_path.relative_to(WIKI)}  (spot {ux},{uy}; {fw}x{fh})")


# --------------------------------------------------------------- main

def pick_example(locations: list[dict]) -> dict:
    """Pick a recognizable inland Britannia site (near Britain/Cove area)."""
    # Prefer a spot comfortably inside the landmass and away from edges.
    target = (1450, 1600)  # central Britannia plains, inland
    best = min(
        (e for e in locations
         if 300 < e["x"] < BRIT_W - 300 and 300 < e["y"] < BRIT_H - 300),
        key=lambda e: (e["x"] - target[0]) ** 2 + (e["y"] - target[1]) ** 2,
    )
    return best


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(TREASURE_JSON.read_text(encoding="utf-8"))
    locations = data["locations"]

    base = Image.open(MAP_PNG).convert("RGB")
    print(f"base map: {base.width}x{base.height}  ({len(locations)} dig sites)")

    render_locations(base, locations, OUT_DIR / "locations.png")

    uop = uoplib.UopFile(GUMP_UOP, has_extra=True)
    spot = pick_example(locations)
    render_example(base, uop, spot, OUT_DIR / "example-map.png")


if __name__ == "__main__":
    main()
