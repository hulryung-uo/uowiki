# /// script
# requires-python = ">=3.9"
# dependencies = ["fonttools", "pillow"]
# ///
"""Build a real TrueType web font from the UO client's own bitmap font (fonts.mul).

The UO ASCII font is a pixel/bitmap font. We parse fonts.mul into per-font,
per-char bitmaps, pick the most characterful ornate font index, then synthesize
a TTF where each "on" pixel becomes a filled unit square. The result is a
copyright-clean web font extracted from our own client files, used to render
spell power-words ("In Lor", "Kal Ort Por") in the authentic UO typeface.

Format (verified against classicuo FontsLoader.cs):
  fonts.mul = sequence of FONTS. Each font = 1 header byte + 224 CHARACTERS.
  Each character = width(u8), height(u8), unknown(u8), then width*height pixels,
  each a 16-bit little-endian ARGB1555. A pixel is "on" if value != 0.
  Char index j (0..223) -> ASCII 0x20 + j.

Usage:
  uv run --script tools/extract_uo_font.py            # full build + verify
  uv run --script tools/extract_uo_font.py --preview  # only render index previews
"""

import argparse
import struct
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

WIKI_ROOT = Path(__file__).resolve().parent.parent
FONTS_MUL = Path("/Users/dkkang/dev/uo/uo-resource/fonts.mul")
OUT_TTF = WIKI_ROOT / "public" / "fonts" / "uo-ascii.ttf"
PREVIEW_DIR = WIKI_ROOT / "tools" / "_uo_font_preview"

NUM_CHARS = 224
ASCII_BASE = 0x20  # char index 0 -> space

# Chosen after rendering previews of all 10 ASCII fonts (tools/_uo_font_preview/).
# Index 4 is an upright gothic/blackletter-flavored serif: characterful ornate
# capitals (distinctive A, B, K, P, R) with the authentic UO spellbook look,
# while staying clearly legible. Index 0/3 are heavy/blobby ("fat" font), index
# 2 is clean but plainer, index 5 is the most ornate but italic and less legible
# at small sizes. Index 4 best balances character and readability for power-words.
CHOSEN_FONT_INDEX = 4


class Char:
    __slots__ = ("ascii", "w", "h", "on")

    def __init__(self, ascii_code, w, h, on):
        self.ascii = ascii_code  # ASCII code point
        self.w = w
        self.h = h
        self.on = on  # set of (x, y) "on" pixel coords, y=0 is TOP row


def parse_fonts_mul(path: Path):
    """Return list[font] where each font is list[Char] of length 224.

    Mirrors FontsLoader.Load: walk to count fonts, then re-read fonts.
    """
    raw = path.read_bytes()
    n = len(raw)

    # First pass: count fonts exactly as the loader does.
    pos = 0
    font_count = 0
    while pos < n:
        exit_flag = False
        pos += 1  # font header byte
        for _ in range(NUM_CHARS):
            if pos + 3 >= n:
                break
            w = raw[pos]
            h = raw[pos + 1]
            pos += 3  # w, h, unknown
            bcount = w * h * 2
            if pos + bcount > n:
                exit_flag = True
                break
            pos += bcount
        if exit_flag:
            break
        font_count += 1

    # Second pass: read pixel data.
    fonts = []
    pos = 0
    for _ in range(font_count):
        pos += 1  # header byte
        chars = []
        for j in range(NUM_CHARS):
            if pos + 3 >= n:
                chars.append(Char(ASCII_BASE + j, 0, 0, set()))
                continue
            w = raw[pos]
            h = raw[pos + 1]
            pos += 3
            on = set()
            count = w * h
            # pixels are u16 LE, row-major, Data[y*w + x]
            if count:
                px = struct.unpack_from("<%dH" % count, raw, pos)
                pos += count * 2
                for idx, val in enumerate(px):
                    if val != 0:
                        on.add((idx % w, idx // w))
            chars.append(Char(ASCII_BASE + j, w, h, on))
        fonts.append(chars)
    return fonts


def char_for(font, ch):
    j = ord(ch) - ASCII_BASE
    if 0 <= j < len(font):
        return font[j]
    return None


def render_text_bitmap(font, text, scale=3, pad=4, gap=2):
    """Compose a PNG by blitting the raw UO bitmaps (for choosing an index)."""
    chars = [char_for(font, c) for c in text]
    max_h = max((c.h for c in chars if c), default=1)
    total_w = sum(((c.w if c else 4) + 1) for c in chars) + 2 * gap
    img = Image.new("RGB", (total_w * scale + 2 * pad, max_h * scale + 2 * pad), (24, 22, 30))
    px = img.load()
    cx = pad
    for c in chars:
        if c is None or c.w == 0:
            cx += 4 * scale
            continue
        # baseline align to bottom
        y_off = (max_h - c.h)
        for (x, y) in c.on:
            for sy in range(scale):
                for sx in range(scale):
                    X = cx + x * scale + sx
                    Y = pad + (y + y_off) * scale + sy
                    if 0 <= X < img.width and 0 <= Y < img.height:
                        px[X, Y] = (235, 220, 180)
        cx += (c.w + 1) * scale
    return img


def render_previews(fonts):
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    sample = "In Lor Kal Ort Por ABC abc"
    for i, font in enumerate(fonts):
        img = render_text_bitmap(font, sample, scale=3)
        img.save(PREVIEW_DIR / f"font_{i:02d}.png")
    print(f"Wrote {len(fonts)} previews to {PREVIEW_DIR}")


def build_ttf(font, font_index):
    """Synthesize a TTF where each 'on' pixel becomes a filled unit square.

    UO bitmaps are top-row-first (y=0 = top). Font/glyph coordinates are
    bottom-up (y increases upward, baseline at y=0). So we FLIP y:
    glyph_y = (max_ascent - 1 - bitmap_y).
    """
    upm = 2048

    # Determine a common pixel size. Use the tallest letter glyph so caps/
    # ascenders fit; descenders (g, p, q, y) drop below baseline.
    ascii_codes = list(range(0x20, 0x7F))

    # Cap height = height of 'A'..'Z'/digits; descent = how far some glyphs
    # extend below the alpha baseline. UO bitmaps already include their own
    # internal vertical placement via height; we sit every glyph's BOTTOM row
    # on the baseline, then add a small uniform descent for letters like 'g'.
    cap_h = 0
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        c = char_for(font, ch)
        if c and c.h:
            cap_h = max(cap_h, c.h)
    if cap_h == 0:
        cap_h = max((char_for(font, chr(cc)).h for cc in ascii_codes
                     if char_for(font, chr(cc)) and char_for(font, chr(cc)).h), default=16)

    # pixel size so cap glyph occupies most of the em above baseline.
    # Leave headroom: ascent region ~ 0.78 of em, descent ~ 0.22.
    ascent_px_budget = cap_h
    pixel = int(upm * 0.74 / max(ascent_px_budget, 1))

    descent_px = 0  # measured from how far glyphs hang below their cap region

    glyph_order = [".notdef"]
    cmap = {}
    advances = {}
    pen_glyphs = {}

    # Build .notdef (empty box)
    pen = TTGlyphPen(None)
    pen_glyphs[".notdef"] = pen.glyph()
    advances[".notdef"] = int(round((6) * pixel))

    for cc in ascii_codes:
        ch = chr(cc)
        c = char_for(font, ch)
        gname = f"uni{cc:04X}"
        glyph_order.append(gname)
        cmap[cc] = gname

        pen = TTGlyphPen(None)
        if c is None or c.w == 0 or c.h == 0:
            # space / empty: advance only
            adv = c.w if (c and c.w) else max(3, cap_h // 2)
            advances[gname] = int(round((adv + 1) * pixel))
            pen_glyphs[gname] = pen.glyph()
            continue

        # Sit the glyph's bottom row on the baseline. Flip y: bitmap y=0 (top)
        # -> highest glyph y. Bottom bitmap row (y=h-1) -> glyph y=0.
        for (x, y) in c.on:
            gx0 = x * pixel
            gx1 = (x + 1) * pixel
            gy_bottom = (c.h - 1 - y) * pixel
            gy_top = (c.h - y) * pixel
            # unit square contour (counter-clockwise filled)
            pen.moveTo((gx0, gy_bottom))
            pen.lineTo((gx1, gy_bottom))
            pen.lineTo((gx1, gy_top))
            pen.lineTo((gx0, gy_top))
            pen.closePath()
        pen_glyphs[gname] = pen.glyph()
        advances[gname] = int(round((c.w + 1) * pixel))

    ascent = int(round((cap_h + 2) * pixel))
    descent_px = max(descent_px, int(round(0.22 * cap_h)) + 2)
    descent = int(round(descent_px * pixel))

    fb = FontBuilder(upm, isTTF=True)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap(cmap)

    hmetrics = {g: (advances[g], 0) for g in glyph_order}
    fb.setupGlyf(pen_glyphs)
    fb.setupHorizontalMetrics(hmetrics)
    fb.setupHorizontalHeader(ascent=ascent, descent=-descent)

    family = "UO Ascii"
    name_strings = dict(
        familyName=family,
        styleName="Regular",
        uniqueFontIdentifier=f"UOAscii-fontidx{font_index};extract_uo_font",
        fullName=family,
        psName="UOAscii-Regular",
        version="1.0",
        copyright="Glyphs synthesized from Ultima Online client fonts.mul (own client files).",
    )
    fb.setupNameTable(name_strings)
    fb.setupOS2(sTypoAscender=ascent, sTypoDescender=-descent,
                usWinAscent=ascent, usWinDescent=descent,
                sCapHeight=int(round(cap_h * pixel)))
    fb.setupPost()

    OUT_TTF.parent.mkdir(parents=True, exist_ok=True)
    fb.save(str(OUT_TTF))
    return OUT_TTF


def verify(ttf_path):
    """Render sample strings with the BUILT TTF via PIL and save PNGs."""
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    samples = ["In Lor", "Kal Ort Por", "Greater Heal"]
    font = ImageFont.truetype(str(ttf_path), 28)
    out_paths = []
    for s in samples:
        # measure
        tmp = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(tmp)
        bbox = d.textbbox((0, 0), s, font=font)
        w = bbox[2] - bbox[0] + 16
        h = bbox[3] - bbox[1] + 16
        img = Image.new("RGB", (w, h), (24, 22, 30))
        d = ImageDraw.Draw(img)
        d.text((8 - bbox[0], 8 - bbox[1]), s, font=font, fill=(235, 220, 180))
        p = PREVIEW_DIR / ("verify_" + s.replace(" ", "_") + ".png")
        img.save(p)
        out_paths.append(p)
    # combined strip
    combo = Image.new("RGB", (max(Image.open(p).width for p in out_paths) + 8,
                              sum(Image.open(p).height for p in out_paths) + 8),
                      (24, 22, 30))
    y = 4
    for p in out_paths:
        im = Image.open(p)
        combo.paste(im, (4, y))
        y += im.height
    combo_path = PREVIEW_DIR / "verify_combined.png"
    combo.save(combo_path)
    print(f"Verify renders written to {PREVIEW_DIR}")
    return combo_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", action="store_true", help="render per-index previews and exit")
    ap.add_argument("--index", type=int, default=CHOSEN_FONT_INDEX)
    args = ap.parse_args()

    if not FONTS_MUL.exists():
        sys.exit(f"fonts.mul not found at {FONTS_MUL}")

    fonts = parse_fonts_mul(FONTS_MUL)
    print(f"Parsed {len(fonts)} ASCII fonts from {FONTS_MUL.name}")
    for i, f in enumerate(fonts):
        a = char_for(f, "A")
        print(f"  font {i}: 'A' = {a.w}x{a.h}" if a else f"  font {i}: no 'A'")

    if args.preview:
        render_previews(fonts)
        return

    render_previews(fonts)  # always emit previews for the record
    idx = args.index
    print(f"Building TTF from font index {idx}")
    ttf = build_ttf(fonts[idx], idx)
    size = ttf.stat().st_size
    print(f"Wrote {ttf} ({size} bytes)")
    verify(ttf)


if __name__ == "__main__":
    main()
