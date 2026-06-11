# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow", "pyyaml"]
# ///
"""Generate static PNG maps with POI markers for the UO wiki.

Sources (read-only):
  - Base map:  /Users/dkkang/dev/uo/uomap/images/map_felucca.png (7170x4098, 1 px per UO unit)
  - POIs:      /Users/dkkang/dev/uo/uomap/js/data.js  (POI_DATA.felucca + NPC_VENDORS)
  - Bounds:    /Users/dkkang/dev/uo/anima/data/world_knowledge.yaml (cities.<name>.bounds)

Outputs:
  - data/map_pois.json
  - public/img/maps/felucca-cities.png
  - public/img/maps/felucca-dungeons.png
  - public/img/maps/felucca-moongates-shrines.png
  - public/img/maps/city-<slug>.png  (8 cities)
  - public/img/maps/dungeon-<slug>.png  (one per felucca dungeon)

Run:  uv run --script tools/gen_maps.py
"""

import json
import re
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

WIKI = Path(__file__).resolve().parent.parent
MAP_PNG = Path("/Users/dkkang/dev/uo/uomap/images/map_felucca.png")
DATA_JS = Path("/Users/dkkang/dev/uo/uomap/js/data.js")
WORLD_YAML = Path("/Users/dkkang/dev/uo/anima/data/world_knowledge.yaml")
OUT_DIR = WIKI / "public" / "img" / "maps"
POIS_JSON = WIKI / "data" / "map_pois.json"

UO_W, UO_H = 7170, 4098  # UO Felucca coordinate space (matches uomap UO_MAPS)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

OVERVIEW_WIDTH = 1500
CITY_MAX_SIDE = 1600
CITY_PAD = 0.10
CITY_MAX_LABELS = 25

DUNGEON_WINDOW = 1100   # UO units, full crop side (~550 each direction from center)
DUNGEON_MAX_WIDTH = 520  # downscaled output width for table thumbnails

COLORS = {
    "city": ("#22c55e", "#ffffff"),       # fill, outline
    "dungeon": ("#ef4444", "#ffffff"),
    "moongate": ("#a855f7", "#ffffff"),
    "shrine": ("#f59e0b", "#ffffff"),
    "npc_vendor": ("#84cc16", "#ffffff"),
}

# Wiki cities: slug -> world_knowledge.yaml key
WIKI_CITIES = {
    "britain": "britain",
    "minoc": "minoc",
    "yew": "yew",
    "vesper": "vesper",
    "trinsic": "trinsic",
    "jhelom": "jhelom",
    "moonglow": "moonglow",
    "skara-brae": "skara_brae",
}

# Vendor label priority on city crops (lower = more important)
VENDOR_PRIORITY = [
    "Banker", "Blacksmith", "Healer", "Provisioner", "Mage", "Innkeeper",
    "Armorer", "Weaponsmith", "Tailor", "Alchemist", "Carpenter", "Tinker",
    "Bowyer", "Scribe", "Jeweler", "Baker", "Butcher", "Stable", "Animal Trainer",
]


# ---------------------------------------------------------------- data parsing

def _parse_entries(block: str, with_desc: bool = True):
    """Parse JS object-literal entries: { name: 'X', x: 1, y: 2, desc: '...' }."""
    entries = []
    # Match each { ... } object (no nested braces in this data)
    for obj in re.finditer(r"\{([^{}]*)\}", block):
        body = obj.group(1)
        name = _js_string(body, "name")
        x = _js_number(body, "x")
        y = _js_number(body, "y")
        if name is None or x is None or y is None:
            continue
        e = {"name": name, "x": x, "y": y}
        if with_desc:
            desc = _js_string(body, "desc")
            if desc is not None:
                e["desc"] = desc
        entries.append(e)
    return entries


def _js_string(body: str, key: str):
    m = re.search(rf"\b{key}\s*:\s*'((?:[^'\\]|\\.)*)'", body)
    if not m:
        m = re.search(rf'\b{key}\s*:\s*"((?:[^"\\]|\\.)*)"', body)
    if not m:
        return None
    return m.group(1).replace("\\'", "'").replace('\\"', '"')


def _js_number(body: str, key: str):
    m = re.search(rf"\b{key}\s*:\s*(-?\d+(?:\.\d+)?)", body)
    return float(m.group(1)) if m else None


def _extract_array(src: str, start_idx: int) -> str:
    """Return text of the [...] array starting at the first '[' at/after start_idx."""
    i = src.index("[", start_idx)
    depth = 0
    for j in range(i, len(src)):
        c = src[j]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return src[i : j + 1]
    raise ValueError("unbalanced brackets")


def _extract_braced(src: str, start_idx: int) -> str:
    """Return text of the {...} block starting at the first '{' at/after start_idx."""
    i = src.index("{", start_idx)
    depth = 0
    for j in range(i, len(src)):
        c = src[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return src[i : j + 1]
    raise ValueError("unbalanced braces")


def parse_data_js() -> dict:
    src = DATA_JS.read_text(encoding="utf-8")

    # POI_DATA.felucca block
    m = re.search(r"const POI_DATA\s*=\s*\{\s*felucca\s*:", src)
    if not m:
        raise SystemExit("POI_DATA.felucca not found in data.js")
    fel_block = _extract_braced(src, src.index("{", m.end() - 1))

    pois = {}
    for cat in re.finditer(r"(\w+)\s*:\s*\[", fel_block):
        cat_name = cat.group(1)
        arr = _extract_array(fel_block, cat.end() - 1)
        pois[cat_name] = _parse_entries(arr, with_desc=True)

    # NPC vendors: felucca aliases trammel
    m = re.search(r"const NPC_VENDORS\s*=\s*\{\s*trammel\s*:", src)
    if m:
        arr = _extract_array(src, m.end() - 1)
        pois["npc_vendor"] = _parse_entries(arr, with_desc=False)

    return pois


def load_city_bounds() -> dict:
    data = yaml.safe_load(WORLD_YAML.read_text(encoding="utf-8"))
    out = {}
    for key, info in data.get("cities", {}).items():
        out[key] = {
            "name": info.get("name", key.title()),
            "center": info.get("center"),
            "bounds": info.get("bounds"),
        }
    return out


# ---------------------------------------------------------------- drawing

def load_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def boxes_overlap(a, b, pad: int = 2) -> bool:
    return not (
        a[2] + pad < b[0] or b[2] + pad < a[0] or a[3] + pad < b[1] or b[3] + pad < a[1]
    )


def place_label(draw, taken, px, py, r, text, font, fill="#ffffff", stroke="#111111"):
    """Draw text near marker, choosing the first candidate spot that avoids
    already-placed label boxes. Returns the placed bbox."""
    bb = draw.textbbox((0, 0), text, font=font, stroke_width=2)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    gap = r + 3
    cands = [
        (px + gap, py - th / 2),            # right
        (px - gap - tw, py - th / 2),       # left
        (px - tw / 2, py - gap - th),       # above
        (px - tw / 2, py + gap),            # below
        (px + gap, py - gap - th),          # upper-right
        (px + gap, py + gap),               # lower-right
        (px - gap - tw, py - gap - th),     # upper-left
        (px - gap - tw, py + gap),          # lower-left
        (px + gap + 12, py - th / 2),       # far right
        (px - tw / 2, py + gap + 12),       # far below
    ]
    W, H = draw.im.size
    best = None
    for cx, cy in cands:
        box = (cx, cy, cx + tw, cy + th)
        if box[0] < 1 or box[1] < 1 or box[2] > W - 1 or box[3] > H - 1:
            continue
        if any(boxes_overlap(box, t) for t in taken):
            continue
        best = (cx, cy, box)
        break
    if best is None:  # fall back: clamp right-side position into the image
        cx = min(max(px + gap, 1), W - tw - 1)
        cy = min(max(py - th / 2, 1), H - th - 1)
        best = (cx, cy, (cx, cy, cx + tw, cy + th))
    cx, cy, box = best
    draw.text(
        (cx - bb[0], cy - bb[1]), text, font=font,
        fill=fill, stroke_width=2, stroke_fill=stroke,
    )
    taken.append(box)
    return box


def draw_marker(draw, px, py, r, fill, outline="#ffffff"):
    draw.ellipse((px - r, py - r, px + r, py + r), fill=fill, outline=outline, width=2)


def draw_legend(draw, items, font, x=12, y=12):
    """items: list of (color, label). Draws a semi-opaque box in the corner."""
    pad, row_h, sw = 10, 22, 12
    tw = max(draw.textbbox((0, 0), lab, font=font)[2] for _, lab in items)
    w = pad * 2 + sw + 8 + tw
    h = pad * 2 + row_h * len(items) - 6
    draw.rectangle((x, y, x + w, y + h), fill=(15, 15, 20, 215), outline="#cccccc")
    for i, (color, lab) in enumerate(items):
        cy = y + pad + i * row_h + 6
        draw.ellipse((x + pad, cy - sw // 2, x + pad + sw, cy + sw // 2),
                     fill=color, outline="#ffffff")
        draw.text((x + pad + sw + 8, cy - 8), lab, font=font, fill="#ffffff",
                  stroke_width=1, stroke_fill="#111111")


def make_overview(base: Image.Image, layers, out_path: Path, legend=None):
    """layers: list of (entries, color, label_key) drawn in order."""
    scale = OVERVIEW_WIDTH / base.width
    img = base.resize((OVERVIEW_WIDTH, round(base.height * scale)), Image.LANCZOS)
    img = img.convert("RGBA")
    draw = ImageDraw.Draw(img, "RGBA")
    font = load_font(15)
    px_per_uo = base.width / UO_W * scale

    taken = []
    # First pass: markers (so labels can route around each other, markers stay put)
    for entries, color, _ in layers:
        for e in entries:
            px, py = e["x"] * px_per_uo, e["y"] * px_per_uo
            draw_marker(draw, px, py, 5, color)
            taken.append((px - 5, py - 5, px + 5, py + 5))
    for entries, color, _ in layers:
        for e in entries:
            px, py = e["x"] * px_per_uo, e["y"] * px_per_uo
            place_label(draw, taken, px, py, 5, e["name"], font)
    if legend:
        draw_legend(draw, legend, load_font(14))
    img.convert("RGB").save(out_path, optimize=True)


def vendor_priority(name: str) -> int:
    parts = [p.strip() for p in name.split(",")]
    best = len(VENDOR_PRIORITY)
    for p in parts:
        for i, key in enumerate(VENDOR_PRIORITY):
            if key.lower() in p.lower():
                best = min(best, i)
    return best


def make_city_map(base: Image.Image, city_name, bounds, pois, out_path: Path):
    x1, y1, x2, y2 = bounds
    bw, bh = x2 - x1, y2 - y1
    pad_x, pad_y = bw * CITY_PAD, bh * CITY_PAD
    px_per_uo = base.width / UO_W  # 1.0 for the felucca image

    cx1 = max(0, round((x1 - pad_x) * px_per_uo))
    cy1 = max(0, round((y1 - pad_y) * px_per_uo))
    cx2 = min(base.width, round((x2 + pad_x) * px_per_uo))
    cy2 = min(base.height, round((y2 + pad_y) * px_per_uo))

    img = base.crop((cx1, cy1, cx2, cy2)).convert("RGBA")
    scale = 1.0
    if max(img.width, img.height) > CITY_MAX_SIDE:
        scale = CITY_MAX_SIDE / max(img.width, img.height)
        img = img.resize((round(img.width * scale), round(img.height * scale)),
                         Image.LANCZOS)
    # Small crops produce unreadably tiny maps; upscale to a usable size.
    if max(img.width, img.height) < 600:
        scale = 600 / max(img.width, img.height)
        img = img.resize((round(img.width * scale), round(img.height * scale)),
                         Image.LANCZOS)

    draw = ImageDraw.Draw(img, "RGBA")
    font = load_font(14)
    title_font = load_font(20)

    def to_px(ux, uy):
        return ((ux * px_per_uo - cx1) * scale, (uy * px_per_uo - cy1) * scale)

    def inside(ux, uy):
        px, py = to_px(ux, uy)
        return 0 <= px < img.width and 0 <= py < img.height

    taken = []

    # Vendors inside the crop, prioritized
    vendors = [v for v in pois.get("npc_vendor", []) if inside(v["x"], v["y"])]
    vendors.sort(key=lambda v: (vendor_priority(v["name"]), v["name"]))
    labeled = vendors[:CITY_MAX_LABELS - 1]  # leave one slot for the city label
    unlabeled = vendors[CITY_MAX_LABELS - 1:]

    vcolor = COLORS["npc_vendor"][0]
    for v in vendors:
        px, py = to_px(v["x"], v["y"])
        draw_marker(draw, px, py, 5, vcolor)
        taken.append((px - 5, py - 5, px + 5, py + 5))

    # City marker
    city_poi = next((c for c in pois.get("city", [])
                     if c["name"].lower() == city_name.lower() and inside(c["x"], c["y"])),
                    None)
    if city_poi:
        px, py = to_px(city_poi["x"], city_poi["y"])
        draw_marker(draw, px, py, 8, COLORS["city"][0])
        taken.append((px - 8, py - 8, px + 8, py + 8))
        place_label(draw, taken, px, py, 8, city_poi["name"], title_font)

    for v in labeled:
        px, py = to_px(v["x"], v["y"])
        place_label(draw, taken, px, py, 5, v["name"], font)
    if unlabeled:
        note = f"+{len(unlabeled)} more vendors"
        draw.text((10, img.height - 26), note, font=font, fill="#ffffff",
                  stroke_width=2, stroke_fill="#111111")

    img.convert("RGB").save(out_path, optimize=True)


def dungeon_slug(name: str) -> str:
    """Slug for a dungeon image: lowercased, spaces->hyphens, apostrophes removed."""
    s = name.lower().replace("'", "").replace("’", "")
    s = re.sub(r"\s+", "-", s.strip())
    return s


def make_dungeon_map(base: Image.Image, dungeon, out_path: Path):
    """Crop a ~DUNGEON_WINDOW square around the dungeon, mark it, label it,
    downscale to DUNGEON_MAX_WIDTH. Reuses to_px/draw_marker/place_label."""
    px_per_uo = base.width / UO_W  # 1.0 for the felucca image
    half = DUNGEON_WINDOW / 2.0
    ux, uy = dungeon["x"], dungeon["y"]

    cx1 = max(0, round((ux - half) * px_per_uo))
    cy1 = max(0, round((uy - half) * px_per_uo))
    cx2 = min(base.width, round((ux + half) * px_per_uo))
    cy2 = min(base.height, round((uy + half) * px_per_uo))

    img = base.crop((cx1, cy1, cx2, cy2)).convert("RGBA")
    scale = 1.0
    if img.width > DUNGEON_MAX_WIDTH:
        scale = DUNGEON_MAX_WIDTH / img.width
        img = img.resize((round(img.width * scale), round(img.height * scale)),
                         Image.LANCZOS)

    draw = ImageDraw.Draw(img, "RGBA")
    font = load_font(16)

    def to_px(px_x, px_y):
        return ((px_x * px_per_uo - cx1) * scale, (px_y * px_per_uo - cy1) * scale)

    mx, my = to_px(ux, uy)
    taken = [(mx - 7, my - 7, mx + 7, my + 7)]
    draw_marker(draw, mx, my, 7, COLORS["dungeon"][0])
    place_label(draw, taken, mx, my, 7, dungeon["name"], font)

    img.convert("RGB").save(out_path, optimize=True)


# ---------------------------------------------------------------- main

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    POIS_JSON.parent.mkdir(parents=True, exist_ok=True)

    pois = parse_data_js()
    POIS_JSON.write_text(json.dumps(pois, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    for cat, entries in pois.items():
        print(f"parsed {cat}: {len(entries)}")

    base = Image.open(MAP_PNG).convert("RGB")
    print(f"base map: {base.width}x{base.height} "
          f"({base.width / UO_W:.4f} px per UO unit)")

    make_overview(base, [(pois["city"], COLORS["city"][0], "city")],
                  OUT_DIR / "felucca-cities.png")
    print("wrote felucca-cities.png")

    make_overview(base, [(pois["dungeon"], COLORS["dungeon"][0], "dungeon")],
                  OUT_DIR / "felucca-dungeons.png")
    print("wrote felucca-dungeons.png")

    make_overview(
        base,
        [(pois["moongate"], COLORS["moongate"][0], "moongate"),
         (pois["shrine"], COLORS["shrine"][0], "shrine")],
        OUT_DIR / "felucca-moongates-shrines.png",
        legend=[(COLORS["moongate"][0], "Moongate"), (COLORS["shrine"][0], "Shrine")],
    )
    print("wrote felucca-moongates-shrines.png")

    cities = load_city_bounds()
    for slug, key in WIKI_CITIES.items():
        info = cities.get(key)
        if not info or not info.get("bounds"):
            print(f"WARNING: no bounds for {key}, skipping")
            continue
        out = OUT_DIR / f"city-{slug}.png"
        make_city_map(base, info["name"], info["bounds"], pois, out)
        print(f"wrote {out.name}")

    seen_slugs = {}
    for d in pois.get("dungeon", []):
        slug = dungeon_slug(d["name"])
        # Resolve name collisions deterministically: -2, -3, ...
        n = seen_slugs.get(slug, 0) + 1
        seen_slugs[slug] = n
        if n > 1:
            slug = f"{slug}-{n}"
        out = OUT_DIR / f"dungeon-{slug}.png"
        make_dungeon_map(base, d, out)
        print(f"wrote {out.name}")


if __name__ == "__main__":
    main()
