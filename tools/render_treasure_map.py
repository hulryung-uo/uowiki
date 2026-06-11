# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow", "numpy"]
# ///
"""Render treasure-hunting images for the UO wiki.

Outputs:
  public/img/treasure/locations.png    -- 193 classic dig sites plotted on Felucca
  public/img/treasure/example-map.png  -- the decoded treasure-map gump, drawn the way
                                          the real client shows it: hand-drawn ink
                                          line-art (coastline outlines + hatch ticks)
                                          on a cream parchment scroll, with the client's
                                          "Plot Course" title, compass rose and a
                                          numbered pin at the dig spot.

Reuses:
  - gen_maps.py's base image + 1px==1 UO unit coordinate mapping
  - render_ui.py / uoplib gump decoder for the real client map-gump art

Sources (read-only):
  - Base map:  /Users/dkkang/dev/uo/uomap/images/map_felucca.png (7170x4098, 1px/UO unit)
  - Sites:     data/treasure.json (from tools/extract_treasure.py)
  - Client gump art: /Users/dkkang/dev/uo/uo-resource/gumpartLegacyMUL.uop
      0x1432  parchment scroll frame (ResizePic 9-slice; wooden-rod end + edge)
      0x1398  "Plot Course" title graphic (top centre)
      0x139D  compass rose with "N" (bottom-right)
    Gump IDs verified against ClassicUO MapGump.cs.

Run:  uv run --script tools/render_treasure_map.py
"""

import json
import os
import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

WIKI = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI / "tools"))
import uoplib  # noqa: E402

MAP_PNG = Path("/Users/dkkang/dev/uo/uomap/images/map_felucca.png")
TREASURE_JSON = WIKI / "data" / "treasure.json"
OUT_DIR = WIKI / "public" / "img" / "treasure"

UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
GUMP_UOP = os.path.join(UO_DIR, "gumpartLegacyMUL.uop")
GUMP_PATTERN = "build/gumpartlegacymul/%08d.tga"

# Real client map-gump art (verified against ClassicUO MapGump.cs).
FRAME_GUMP = 0x1432    # parchment scroll frame (ResizePic 9-slice)
TITLE_GUMP = 0x1398    # "Plot Course" title graphic
COMPASS_GUMP = 0x139D  # compass rose with "N"

UO_W, UO_H = 7170, 4098  # felucca image == UO coordinate space (gen_maps.py)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
UO_FONT = str(WIKI / "public" / "fonts" / "uo-ascii.ttf")

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


# --------------------------------------------------------------- parchment scroll

def make_parchment(w: int, h: int, seed: int = 7) -> Image.Image:
    """A cream parchment canvas with subtle mottling, ready for ink line-art."""
    rng = np.random.default_rng(seed)
    base_col = np.array([0xec, 0xdf, 0xbe], dtype=np.float32)
    noise = rng.normal(0, 6, (h, w, 1))
    blob = Image.fromarray((rng.normal(0, 1, (h, w)) * 255).astype(np.uint8))
    mott = np.asarray(blob.filter(ImageFilter.GaussianBlur(10)), dtype=np.float32)
    mott -= mott.mean()
    canvas = base_col[None, None, :] + noise + mott[..., None] * 0.6
    arr = np.clip(canvas, 150, 240).astype(np.uint8)
    return Image.fromarray(arr).convert("RGBA")


def build_scroll(uop: uoplib.UopFile, body: Image.Image) -> Image.Image:
    """Wrap `body` (the parchment line-art map) in the client scroll frame.

    Gump 0x1432 is the ResizePic top-left corner: a wooden rod with a turned
    finial on the left and the parchment top edge to the right. We slice it into
    the rod band + finial and tile/mirror those to form top & bottom wooden rods
    with end caps, leaving the parchment body between them.
    """
    corner = decode_gump(uop, FRAME_GUMP).convert("RGBA")  # 38x38
    # The wooden rod occupies the upper band; the turned finial is the left ~14px.
    rod_h = 22
    finial_w = 14
    rod_band = corner.crop((0, 0, corner.width, rod_h))
    finial = corner.crop((0, 0, finial_w, rod_h))           # left turned cap
    # A clean rod tile from the edge region (right of the finial), to repeat.
    rod_tile = corner.crop((finial_w + 6, 0, corner.width, rod_h))

    bw, bh = body.width, body.height
    pad = 10  # parchment margin around the map
    inner_w = bw + pad * 2
    rod_overhang = 8  # rods stick out past the parchment a touch

    full_w = inner_w + rod_overhang * 2
    full_h = bh + pad * 2 + rod_h * 2
    out = Image.new("RGBA", (full_w, full_h), (0, 0, 0, 0))

    # Parchment body panel (slightly larger than the map, map centred on it).
    panel = make_parchment(inner_w, bh + pad * 2, seed=11)
    out.alpha_composite(panel, (rod_overhang, rod_h))
    out.alpha_composite(body, (rod_overhang + pad, rod_h + pad))

    def lay_rod(y_top: int, flip_v: bool):
        rod = rod_tile
        cap = finial
        if flip_v:
            rod = rod.transpose(Image.FLIP_TOP_BOTTOM)
            cap = cap.transpose(Image.FLIP_TOP_BOTTOM)
        # Tile the plain rod across the full width.
        x = 0
        while x < full_w:
            out.alpha_composite(rod, (x, y_top))
            x += rod.width
        # End-cap finials (left as-is, right mirrored).
        out.alpha_composite(cap, (0, y_top))
        out.alpha_composite(cap.transpose(Image.FLIP_LEFT_RIGHT),
                            (full_w - cap.width, y_top))

    lay_rod(0, flip_v=False)               # top rod
    lay_rod(full_h - rod_h, flip_v=True)   # bottom rod (mirrored)
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

INK = (52, 34, 20, 255)  # dark sepia ink


def land_water_mask(crop_rgb: Image.Image) -> np.ndarray:
    """Classify each pixel land vs water on the Felucca base map.

    Ocean is blue (B clearly above R and G, fairly dark); land is green/brown/
    grey. A simple per-channel threshold splits them cleanly (the B-R histogram
    on a regional crop is strongly bimodal). We then median-filter the mask so
    coastlines come out smooth rather than pixel-noisy.
    """
    arr = np.asarray(crop_rgb).astype(np.int16)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    water = (b > r + 10) & (b > g + 5)
    land = ~water
    lm = Image.fromarray((land * 255).astype(np.uint8))
    lm = lm.filter(ImageFilter.MedianFilter(7)).filter(ImageFilter.MedianFilter(5))
    return np.asarray(lm) > 128


def _mask_boundary(mask: np.ndarray) -> np.ndarray:
    """Land pixels that touch water in a 4-neighbourhood (the coastline)."""
    m = mask.astype(np.uint8)
    up = np.zeros_like(m); up[1:, :] = m[:-1, :]
    dn = np.zeros_like(m); dn[:-1, :] = m[1:, :]
    lf = np.zeros_like(m); lf[:, 1:] = m[:, :-1]
    rt = np.zeros_like(m); rt[:, :-1] = m[:, 1:]
    return (m == 1) & (up + dn + lf + rt < 4)


def render_lineart(land: np.ndarray, seed: int = 7) -> Image.Image:
    """Hand-drawn ink map: coastline outlines + outward hatch ticks + sparse
    stipple, all in sepia ink on a cream parchment canvas (no colour fill)."""
    h, w = land.shape
    coast = _mask_boundary(land)
    img = make_parchment(w, h, seed=seed)
    draw = ImageDraw.Draw(img, "RGBA")
    px = img.load()

    # Coastline: thicken the boundary by one pixel for a confident ink line.
    thick = np.asarray(
        Image.fromarray((coast * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(3))
    ) > 128
    for y, x in zip(*np.where(thick)):
        px[x, y] = INK

    # Outward normals (toward water) from a blurred land field, for the ticks.
    field = np.asarray(
        Image.fromarray((land * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2.5)),
        dtype=np.float32,
    ) / 255.0
    gy, gx = np.gradient(field)
    ys, xs = np.where(coast)
    for i in range(len(ys)):
        if i % 5:  # sample every 5th boundary pixel
            continue
        y, x = int(ys[i]), int(xs[i])
        nx, ny = -gx[y, x], -gy[y, x]  # decreasing land -> water side
        mag = (nx * nx + ny * ny) ** 0.5
        if mag < 1e-3:
            continue
        nx /= mag; ny /= mag
        draw.line((x + nx * 1.5, y + ny * 1.5, x + nx * 7, y + ny * 7),
                  fill=INK, width=1)

    # Very sparse stipple well inside large landmasses (the classic UO texture).
    rng = np.random.default_rng(seed)
    interior = np.asarray(
        Image.fromarray((land * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(11))
    ) > 128
    iy, ix = np.where(interior)
    if len(iy):
        sel = rng.choice(len(iy), size=min(len(iy) // 90, 400), replace=False)
        for k in sel:
            px[int(ix[k]), int(iy[k])] = INK

    return img


def draw_pin(draw: ImageDraw.ImageDraw, x: float, y: float):
    """A numbered dig-spot marker: a little stake with a blue '1' label box."""
    # Stake driven into the coast.
    draw.line((x, y, x, y - 16), fill=(40, 30, 18, 255), width=3)
    draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(40, 30, 18, 255))
    # Blue-outlined label box with "1".
    bw, bh = 18, 16
    bx, by = x - bw // 2, y - 16 - bh
    draw.rectangle((bx, by, bx + bw, by + bh), fill=(247, 243, 224, 255),
                   outline=(40, 78, 150, 255), width=2)
    try:
        font = ImageFont.truetype(UO_FONT, 13)
    except OSError:
        font = load_font(13)
    tb = draw.textbbox((0, 0), "1", font=font)
    tx = bx + (bw - (tb[2] - tb[0])) / 2 - tb[0]
    ty = by + (bh - (tb[3] - tb[1])) / 2 - tb[1]
    draw.text((tx, ty), "1", font=font, fill=(40, 78, 150, 255))


def render_example(base: Image.Image, uop: uoplib.UopFile, spot: dict, out_path: Path):
    """Draw the decoded map the way the real client does: ink line-art on a
    parchment scroll, with the "Plot Course" title, compass rose and a numbered
    pin at the dig spot."""
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

    crop = base.crop((cx1, cy1, cx2, cy2)).convert("RGB")
    land = land_water_mask(crop)

    # Ink line-art at native crop resolution, then upscale for display.
    art = render_lineart(land)
    target_w = 460
    view_scale = target_w / art.width
    art = art.resize((target_w, round(art.height * view_scale)), Image.LANCZOS)

    # A faint ink border framing the drawn map, like the real gump.
    bd = ImageDraw.Draw(art, "RGBA")
    bd.rectangle((1, 1, art.width - 2, art.height - 2),
                 outline=(90, 64, 38, 160), width=1)

    # Numbered pin at the dig spot, in line-art coordinates.
    draw = ImageDraw.Draw(art, "RGBA")
    pin_x = (ux - cx1) * view_scale
    pin_y = (uy - cy1) * view_scale
    draw_pin(draw, pin_x, pin_y)

    # Wrap the map in the client parchment scroll frame (0x1432).
    scroll = build_scroll(uop, art)

    # Title (0x1398) across the top, compass rose (0x139D) bottom-right.
    title = decode_gump(uop, TITLE_GUMP).convert("RGBA")
    compass = decode_gump(uop, COMPASS_GUMP).convert("RGBA")

    top_gap = 16
    side_gap = 12
    canvas_w = max(scroll.width, title.width + 8) + side_gap * 2
    canvas_h = top_gap + title.height + 10 + scroll.height + side_gap
    canvas = make_parchment(canvas_w, canvas_h, seed=3).convert("RGBA")
    # Tint the outer canvas a touch darker so the scroll reads as a panel on it.
    shade = Image.new("RGBA", (canvas_w, canvas_h), (120, 92, 52, 38))
    canvas.alpha_composite(shade)

    scroll_x = (canvas_w - scroll.width) // 2
    scroll_y = top_gap + title.height + 10
    canvas.alpha_composite(scroll, (scroll_x, scroll_y))

    title_x = (canvas_w - title.width) // 2
    canvas.alpha_composite(title, (title_x, top_gap))

    cmp_scale = 1.55
    compass = compass.resize(
        (round(compass.width * cmp_scale), round(compass.height * cmp_scale)),
        Image.LANCZOS)
    cmp_x = scroll_x + scroll.width - compass.width - 18
    cmp_y = scroll_y + scroll.height - compass.height - 18
    canvas.alpha_composite(compass, (cmp_x, cmp_y))

    canvas.convert("RGB").save(out_path, optimize=True)
    print(f"wrote {out_path.relative_to(WIKI)}  (spot {ux},{uy}; "
          f"{canvas_w}x{canvas_h})")


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
