# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render UO "gump" (UI window) reference images for the wiki.

We do NOT run the ClassicUO client (no display / server / session). Instead we
build authentic UI images straight from the client's own GUMP ART
(gumpartLegacyMUL.uop) — the same copyright-clean source the rest of the wiki
uses — and overlay plausible example values (stats, name, gold, ...) using the
extracted UO ASCII font so the windows aren't empty.

Gump ids (verified in classicuo/src/ClassicUO.Client/Game/UI/Gumps/):
  0x0802  player status bar background   (StatusGump.cs, StatusGumpOld)
  0x0803  compact self health bar bg     (HealthBarGump.cs, BACKGROUND_NORMAL)
  0x0805  red bar line (depleted track)  (HealthBarGump.cs, LINE_RED)
  0x0806  blue bar line (filled HP/St/Mn)(HealthBarGump.cs, LINE_BLUE)
  0x003C  default backpack container     (ContainerGump.cs, Default Backpack)
  0x08AC  magery spellbook (closed/open) (SpellbookGump.cs, Magery bookGraphic)
  0x1F40..0x1F43  skill-list parchment scroll parts
          (ExpandableScroll.cs: top, right-edge, middle-tile, bottom)
  0x0834  skill-scroll title plate       (StandardSkillsGump.cs, TitleGumpID)

Field x/y positions for the status bar come straight from StatusGumpOld's
Label{X=,Y=} declarations so the example numbers land in their real slots.

Outputs (public/img/ui/):
  status-bar.png  health-bar.png  backpack.png  spellbook.png  skills.png

Run:  uv run --script tools/render_ui.py
"""

from __future__ import annotations

import os
import struct
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
GUMP_UOP = os.path.join(UO_DIR, "gumpartLegacyMUL.uop")
GUMP_PATTERN = "build/gumpartlegacymul/%08d.tga"
FONT_PATH = os.path.join(ROOT, "public", "fonts", "uo-ascii.ttf")
OUT_DIR = os.path.join(ROOT, "public", "img", "ui")

# UO label text in the status/health gumps is a pale near-white (hue 0x0386).
LABEL_RGB = (227, 227, 214)


def decode_gump(uop: uoplib.UopFile, gump_id: int) -> Image.Image:
    """Decode a gump by id -> RGBA Image (same RLE decoder as extract_spell_icons)."""
    entry = uop.get_by_name(GUMP_PATTERN % gump_id)
    if entry is None:
        raise KeyError(f"gump 0x{gump_id:04X} not present")
    payload = uop.read(entry)
    if entry.flag == uoplib.FLAG_NONE:
        w, h = entry.extra1, entry.extra2
    else:
        w, h = struct.unpack_from("<II", payload, 0)
        payload = payload[8:]
    if w <= 0 or h <= 0:
        raise ValueError(f"gump 0x{gump_id:04X}: bad dimensions {w}x{h}")

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


def _font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size)


def draw_label(draw: ImageDraw.ImageDraw, xy, text, font, *, center=False,
               fill=LABEL_RGB):
    """Draw UO-style text. The status gump labels are left-aligned at X,Y; the
    health-bar name is centered. A 1px dark drop shadow matches the client's
    outlined font look."""
    x, y = xy
    if center:
        bbox = font.getbbox(text)
        x -= (bbox[2] - bbox[0]) / 2
    draw.text((x + 1, y + 1), text, font=font, fill=(0, 0, 0, 180))
    draw.text((x, y), text, font=font, fill=fill)


# ---------------------------------------------------------------------------

def render_status_bar(uop: uoplib.UopFile) -> Image.Image:
    """Gump 0x0802 with the StatusGumpOld example values overlaid.

    Positions are the Label{X,Y} from StatusGumpOld. Left column at x=86:
    name(42), Str(62), Dex(74), Int(86), sex(98), AR(110). Right column at
    x=171: Hits(62), Mana(74), Stam(86), Gold(98), Weight(110).
    """
    img = decode_gump(uop, 0x0802).convert("RGBA")
    d = ImageDraw.Draw(img)
    f = _font(11)

    # left column
    draw_label(d, (86, 41), "Bjorn", f)        # MobileStats.Name
    draw_label(d, (86, 62), "80", f)           # Strength
    draw_label(d, (86, 74), "55", f)           # Dexterity
    draw_label(d, (86, 86), "25", f)           # Intelligence
    draw_label(d, (86, 98), "Male", f)         # Sex
    draw_label(d, (86, 110), "32", f)          # AR (physical resist)

    # right column
    draw_label(d, (171, 62), "78/80", f)       # Hits/HitsMax
    draw_label(d, (171, 74), "40/40", f)       # Mana/ManaMax
    draw_label(d, (171, 86), "62/65", f)       # Stamina/StaminaMax
    draw_label(d, (171, 98), "13280", f)       # Gold
    draw_label(d, (171, 110), "187/520", f)    # Weight/WeightMax
    return img


def render_health_bar(uop: uoplib.UopFile) -> Image.Image:
    """Gump 0x0803 (self bar). Three tracks at x=34, y=12/25/38. Red line
    0x0805 is the depleted track; blue line 0x0806 drawn on top to the filled
    width. Name is centered near the top of the frame."""
    bg = decode_gump(uop, 0x0803).convert("RGBA")
    red = decode_gump(uop, 0x0805).convert("RGBA")   # 109x11 depleted track
    blue = decode_gump(uop, 0x0806).convert("RGBA")  # 109x11 filled bar

    out = bg.copy()
    full = blue.width  # 109
    # (current, max) for HP, Stamina, Mana — matches the status-bar example.
    pools = [(78, 80), (62, 65), (40, 40)]
    ys = [12, 25, 38]
    for (cur, mx), y in zip(pools, ys):
        out.alpha_composite(red, (34, y))
        w = max(1, round(full * cur / mx))
        out.alpha_composite(blue.crop((0, 0, w, blue.height)), (34, y))

    d = ImageDraw.Draw(out)
    # The empty stone band across the top of 0x0803 is where the client puts the
    # name textbox; centre the example name there.
    draw_label(d, (out.width // 2, 2), "Bjorn", _font(10), center=True)
    return out


def render_backpack(uop: uoplib.UopFile) -> Image.Image:
    """Gump 0x003C — the default backpack/container frame (window chrome)."""
    return decode_gump(uop, 0x003C).convert("RGBA")


def render_spellbook(uop: uoplib.UopFile) -> Image.Image:
    """Gump 0x08AC — the magery spellbook (open book frame)."""
    return decode_gump(uop, 0x08AC).convert("RGBA")


def render_skills(uop: uoplib.UopFile) -> Image.Image:
    """Compose the skill-list parchment scroll from ExpandableScroll parts
    (0x1F40 top, 0x1F42 middle tiled, 0x1F43 bottom), overlay the 0x0834 title
    plate and a few example skill rows so it reads as the skill window."""
    top = decode_gump(uop, 0x1F40).convert("RGBA")
    mid = decode_gump(uop, 0x1F42).convert("RGBA")
    bot = decode_gump(uop, 0x1F43).convert("RGBA")
    title = decode_gump(uop, 0x0834).convert("RGBA")

    w = max(top.width, mid.width, bot.width)
    mid_repeat = 3  # enough body to list a handful of skills
    height = top.height + mid.height * mid_repeat + bot.height
    out = Image.new("RGBA", (w, height), (0, 0, 0, 0))

    y = 0
    out.alpha_composite(top, (0, y)); y += top.height
    for _ in range(mid_repeat):
        out.alpha_composite(mid, (0, y)); y += mid.height
    out.alpha_composite(bot, (0, y))

    # Title plate centered in the top scroll roll.
    out.alpha_composite(title, ((w - title.width) // 2, 8))

    d = ImageDraw.Draw(out)
    f = _font(11)
    # A few representative skills with example values, right-aligned values.
    rows = [
        ("Anatomy", "62.4"),
        ("Healing", "78.1"),
        ("Magery", "90.0"),
        ("Swordsmanship", "100.0"),
        ("Tactics", "85.7"),
        ("Wrestling", "44.3"),
    ]
    text_left = 55
    val_right = w - 60
    ry = top.height + 8
    for name, val in rows:
        draw_label(d, (text_left, ry), name, f, fill=(60, 40, 20))
        vb = f.getbbox(val)
        draw_label(d, (val_right - (vb[2] - vb[0]), ry), val, f, fill=(60, 40, 20))
        ry += 16
    return out


# ---------------------------------------------------------------------------

def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    uop = uoplib.UopFile(GUMP_UOP, has_extra=True)

    jobs = [
        ("status-bar.png", render_status_bar),
        ("health-bar.png", render_health_bar),
        ("backpack.png", render_backpack),
        ("spellbook.png", render_spellbook),
        ("skills.png", render_skills),
    ]

    rendered, skipped = [], []
    for fname, fn in jobs:
        try:
            img = fn(uop)
            img.save(os.path.join(OUT_DIR, fname))
            rendered.append((fname, img.width, img.height))
            print(f"  rendered {fname}  {img.width}x{img.height}")
        except Exception as e:  # noqa: BLE001 - report and continue
            skipped.append((fname, str(e)))
            print(f"  SKIPPED {fname}: {e}")

    print(f"\n{len(rendered)}/{len(jobs)} UI images rendered -> {OUT_DIR}")
    if skipped:
        for fname, why in skipped:
            print(f"  skipped {fname}: {why}")
    return 0 if not skipped else 1


if __name__ == "__main__":
    sys.exit(main())
