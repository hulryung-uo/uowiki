# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render DRESSED animated GIFs for humanoid bestiary mobs.

A dressed mobile is drawn exactly as ClassicUO does
(src/ClassicUO.Client/Game/GameObjects/Views/MobileView.cs +
 src/ClassicUO.Assets/AnimationsLoader.cs):

  1. The BODY animation (creature body graphic) for an action group + direction.
  2. For each equipped item, in paperdoll layer order, that item's EQUIPMENT
     animation for the SAME action group + direction, composited over the body
     per-frame, tinted by the item's hue.

An item's equipment animation is indexed in the anim MULs by the item's AnimID
(from tiledata.mul, the same id used for paperdoll gumps). Equipment is anim
type Equipment, which — like Human — uses the People group offset. So we decode
an equipment AnimID with the *same* MUL/index/frame codec the body uses (we reuse
tools/extract_anim.py wholesale and just force the Human/People offset path).

Equipconv.def remaps some (body, AnimID) -> (newGraphic, gump, color); we parse
and apply it (mostly gender/race substitutions, e.g. body 401 = female).

Tinting:
  - Body frames keep their native palette (UO body anims are already skin/hair
    toned in the MUL; the client applies no partial hue to the bare body here).
  - Equipment art is grayscale; we tint it via the hues.mul ramp (partial hue ==
    full hue for grayscale), exactly like tools/apply_hues / extract_paperdoll.
    Hue: the item's baked hue, else neutral clothing hue 1854 for random-dyed.

Reads : data/mob_appearance.json, data/creature_anim.json, data/creatures.json,
        uo-resource/{anim*.mul,tiledata.mul,hues.mul,Equipconv.def}
Writes: public/img/creatures/dressed-<class-slug>.gif (+ .png first frame),
        data/creature_dressed.json

Usage:
  uv run --script tools/extract_anim_dressed.py
  uv run --script tools/extract_anim_dressed.py --only Gypsy Brigand --dir 1
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import struct
import sys
from datetime import date

from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCE_DIR = os.path.normpath(os.path.join(REPO_ROOT, "..", "uo-resource"))
TILEDATA = os.path.join(RESOURCE_DIR, "tiledata.mul")
HUES_MUL = os.path.join(RESOURCE_DIR, "hues.mul")
EQUIPCONV = os.path.join(RESOURCE_DIR, "Equipconv.def")

APPEARANCE_JSON = os.path.join(REPO_ROOT, "data", "mob_appearance.json")
ANIM_JSON = os.path.join(REPO_ROOT, "data", "creature_anim.json")
OUT_GIF_DIR = os.path.join(REPO_ROOT, "public", "img", "creatures")
OUT_JSON = os.path.join(REPO_ROOT, "data", "creature_dressed.json")

# Reuse the verified MUL/index/frame codec from extract_anim.py without editing it.
_spec = importlib.util.spec_from_file_location(
    "extract_anim", os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract_anim.py")
)
ea = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ea)

IDX = ea.IDX_ENTRY.size
FRAME_DURATION_MS = ea.FRAME_DURATION_MS

# Skin / neutral clothing hues (match extract_paperdoll.py).
SKIN_HUE = 1024
NEUTRAL_CLOTHING_HUE = 1854

# Paperdoll layer draw order (back to front) — same list extract_paperdoll uses,
# from ClassicUO PaperDollInteractable._layerOrder.
LAYER_ORDER = [
    "Cloak", "Shirt", "Pants", "Shoes", "Legs", "Arms", "Torso", "Tunic",
    "Ring", "Bracelet", "Face", "Gloves", "Skirt", "Robe", "Waist",
    "Necklace", "Hair", "Beard", "Earrings", "Helmet", "OneHanded",
    "TwoHanded", "Talisman",
]
LAYER_RANK = {name: i for i, name in enumerate(LAYER_ORDER)}


# --------------------------------------------------------------------------- #
# tiledata.mul ItemID -> AnimID  (copied from extract_paperdoll.parse_tiledata)
# --------------------------------------------------------------------------- #
def parse_tiledata_animid(path: str) -> dict[int, int]:
    data = open(path, "rb").read()
    land_entry = 8 + 2 + 20
    land_group = 4 + 32 * land_entry
    static_entry = 8 + 1 + 1 + 4 + 2 + 2 + 2 + 1 + 20
    static_group = 4 + 32 * static_entry
    pos = 512 * land_group
    animid: dict[int, int] = {}
    group = 0
    while pos + static_group <= len(data):
        pos += 4
        for j in range(32):
            aid = struct.unpack_from("<H", data, pos + 14)[0]
            animid[group * 32 + j] = aid
            pos += static_entry
        group += 1
    return animid


# --------------------------------------------------------------------------- #
# hues.mul ramp  (copied from extract_paperdoll.load_hues)
# --------------------------------------------------------------------------- #
def load_hues(path: str) -> list[list[tuple[int, int, int]]]:
    data = open(path, "rb").read()
    GROUP = 708
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
                table.append((
                    (r << 3) | (r >> 2),
                    (g5 << 3) | (g5 >> 2),
                    (b << 3) | (b >> 2),
                ))
            hues.append(table)
    return hues


# --------------------------------------------------------------------------- #
# Equipconv.def  ->  {body: {animID: (newGraphic, gump, color)}}
# (per ProcessEquipConvDef, AnimationsLoader.cs ~465)
# --------------------------------------------------------------------------- #
def parse_equipconv(path: str) -> dict[int, dict[int, tuple[int, int, int]]]:
    out: dict[int, dict[int, tuple[int, int, int]]] = {}
    if not os.path.exists(path):
        return out
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for raw in f:
            line = raw.strip()
            if not line or not line[0].isdigit():
                continue
            p = line.find("#")
            if p >= 0:
                line = line[:p]
            parts = line.split()
            if len(parts) < 5:
                continue
            try:
                body = int(parts[0])
                graphic = int(parts[1])
                new_graphic = int(parts[2])
                gump = int(parts[3])
                color = int(parts[4])
            except ValueError:
                continue
            out.setdefault(body, {})[graphic] = (new_graphic, gump, color)
    return out


def hue_to_table(hues, hue_int: int):
    """hue_int is a 1-based hue index; partial-hue flag ignored for grayscale."""
    idx = (hue_int & 0x3FFF) - 1
    if 0 <= idx < len(hues):
        return hues[idx]
    return None


# --------------------------------------------------------------------------- #
# Equipment-frame decode (reusing extract_anim's codec) with optional hue tint.
# Returns a list of frames (dict cx,cy,w,h,rgba) where rgba is a flat bytearray
# of length w*h*4 (already tinted / coloured); transparent pixels alpha 0.
# --------------------------------------------------------------------------- #
def decode_layer_rgba(ex, graphic: int, group_id: int, direction: int,
                      hue_table):
    """Decode a body/equipment graphic at the People offset; return rgba frames.

    hue_table None -> use the frame's native palette (body). Otherwise tint each
    opaque pixel by ramping its grey value (palette R 0..255 -> table[R>>3])."""
    off, _gc, _og = ea.calc_offset(graphic, ea.HUMAN, 0)
    base_slot = off // IDX
    slot = base_slot + group_id * 5 + direction
    loc = ex.files.read_slot(0, slot)
    if loc is None:
        return None
    data = ex.files.read_data(0, *loc)
    pal_rgb, frames = ea.decode_frames(data)
    if pal_rgb is None:
        return None
    live = [f for f in frames if f is not None]
    if not live:
        return None

    out = []
    for f in frames:  # keep None placeholders so indices line up if needed
        if f is None:
            out.append(None)
            continue
        w, h, px = f["w"], f["h"], f["pixels"]
        rgba = bytearray(w * h * 4)
        for i, v in enumerate(px):
            if v == 256:
                continue
            r, g, b = pal_rgb[v]
            if hue_table is not None:
                # grayscale art: ramp by luminance (R == G == B for grays).
                tr, tg, tb = hue_table[r >> 3]
                r, g, b = tr, tg, tb
            o = i * 4
            rgba[o] = r
            rgba[o + 1] = g
            rgba[o + 2] = b
            rgba[o + 3] = 255
        out.append({"cx": f["cx"], "cy": f["cy"], "w": w, "h": h, "rgba": rgba})
    return out


# --------------------------------------------------------------------------- #
# Compose dressed frames -> GIF + first-frame PNG.
# Each layer is a list of rgba frames; we union all bounding boxes (using each
# frame's own center offset, matching extract_anim's anchor math) and alpha-
# composite body-then-equipment per frame.
# --------------------------------------------------------------------------- #
def _frame_box(f):
    return (-f["cx"], -(f["cy"] + f["h"]), -f["cx"] + f["w"], -(f["cy"] + f["h"]) + f["h"])


def compose_dressed(layers, out_gif: str, out_png: str):
    """layers: ordered list of (label, frames). frames[i] aligned by index.

    Returns (frame_count, (w, h)) or (0, None) on failure."""
    # body is layers[0]; its live frame count drives the animation length.
    body_frames = [f for f in layers[0][1] if f is not None]
    n = len(body_frames)
    if n == 0:
        return 0, None

    # Union bbox over every frame of every layer (clamped/cycled to n frames).
    all_frames = []
    for _label, frames in layers:
        live = [f for f in frames if f is not None]
        if not live:
            continue
        all_frames.extend(live)
    left = min(_frame_box(f)[0] for f in all_frames)
    top = min(_frame_box(f)[1] for f in all_frames)
    right = max(_frame_box(f)[2] for f in all_frames)
    bottom = max(_frame_box(f)[3] for f in all_frames)
    cw, ch = right - left, bottom - top
    if cw <= 0 or ch <= 0 or cw > 1024 or ch > 1024:
        return 0, None

    def layer_frame(frames, i):
        live = [f for f in frames if f is not None]
        if not live:
            return None
        if i < len(live):
            return live[i]
        return live[i % len(live)]  # cycle short equipment layers

    images = []
    for i in range(n):
        canvas = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        for _label, frames in layers:
            f = layer_frame(frames, i)
            if f is None:
                continue
            fx = -f["cx"] - left
            fy = -(f["cy"] + f["h"]) - top
            sub = Image.frombytes("RGBA", (f["w"], f["h"]), bytes(f["rgba"]))
            canvas.alpha_composite(sub, (fx, fy))
        images.append(canvas)

    # First-frame PNG.
    images[0].save(out_png)

    # Quantize to a shared adaptive palette with a transparent index for GIF.
    pal_frames = []
    # Build one global palette from the union of frames for stable colors.
    union = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    for im in images:
        union.alpha_composite(im)
    base_p = union.convert("RGB").quantize(colors=255, method=Image.MEDIANCUT)
    palette = base_p.getpalette()

    for im in images:
        alpha = im.getchannel("A")
        rgb = im.convert("RGB")
        q = rgb.quantize(palette=base_p, dither=Image.NONE)
        # reserve palette index 255 for transparency
        q = q.copy()
        qpx = q.load()
        apx = alpha.load()
        for y in range(ch):
            for x in range(cw):
                if apx[x, y] == 0:
                    qpx[x, y] = 255
        q.putpalette(palette[:765] + [0, 0, 0])
        pal_frames.append(q)

    pal_frames[0].save(
        out_gif,
        save_all=True,
        append_images=pal_frames[1:],
        duration=FRAME_DURATION_MS,
        loop=0,
        transparency=255,
        disposal=2,
        optimize=False,
    )
    return n, (cw, ch)


# --------------------------------------------------------------------------- #
def class_slug(cls: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "-", cls).lower()


def pick_worn(worn: list[dict]) -> list[dict]:
    """Select which items the mob actually wears for the render.

    Non-optional pieces always; for optional pieces keep one representative per
    layer (first listed). Weapons (OneHanded/TwoHanded) are usually a random
    pick from several optional candidates -> include the first one only."""
    chosen: list[dict] = []
    seen_layers: set[str] = set()
    # First pass: all non-optional pieces.
    for it in worn:
        if not it.get("optional"):
            chosen.append(it)
            seen_layers.add(it["layer"])
    # Second pass: optional pieces, one per layer not already filled.
    for it in worn:
        if it.get("optional") and it["layer"] not in seen_layers:
            chosen.append(it)
            seen_layers.add(it["layer"])
    return chosen


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", type=int, default=1, help="stored direction 0-4 (default 1)")
    ap.add_argument("--only", nargs="*", help="only these creature classes")
    ap.add_argument("--out", default=OUT_GIF_DIR)
    args = ap.parse_args()

    appearance = json.load(open(APPEARANCE_JSON))["creatures"]
    anim = json.load(open(ANIM_JSON))
    anim_creatures = anim["creatures"]
    anim_bodies = anim["bodies"]

    animid = parse_tiledata_animid(TILEDATA)
    hues = load_hues(HUES_MUL)
    equipconv = parse_equipconv(EQUIPCONV)
    ex = ea.Extractor()

    os.makedirs(args.out, exist_ok=True)

    results: dict[str, dict] = {}
    failures: list[tuple[str, str]] = []
    fallbacks: list[tuple[str, str]] = []

    classes = sorted(appearance.keys())
    if args.only:
        want = set(args.only)
        classes = [c for c in classes if c in want]

    for cls in classes:
        entry = appearance[cls]
        # Must be a humanoid paperdoll mob (got a paperdoll render) ...
        if not entry.get("paperdoll"):
            continue
        # ... and must have a bare-body GIF.
        if cls not in anim_creatures:
            continue
        body_id = anim_creatures[cls]
        body_meta = anim_bodies.get(str(body_id))
        if not body_meta:
            continue

        group_name = body_meta.get("group", "walk")
        # Map group name back to a People-group action id.
        people_groups = {g[1]: g[0] for g in ea.PREFERRED_GROUPS[ea.G_PEOPLE]}
        group_id = people_groups.get(group_name, 0)

        # Decode the body (native palette).
        body_rgba = decode_layer_rgba(ex, body_id, group_id, args.dir, None)
        if not body_rgba or not any(f for f in body_rgba):
            fallbacks.append((cls, f"body {body_id} did not decode"))
            continue

        worn = pick_worn(entry.get("worn", []))
        layer_records = []
        equip_layers = []  # (rank, label, frames)
        bad = None
        for it in worn:
            iid = int(it["item_id"], 0)
            aid = animid.get(iid)
            if not aid:
                continue  # no equipment art for this item; skip silently
            graphic = aid
            # Equipconv remap for this body graphic.
            conv = equipconv.get(body_id, {})
            if aid in conv:
                new_graphic, _gump, _color = conv[aid]
                if new_graphic > 0:
                    graphic = new_graphic
            # Hue: baked item hue, else neutral for random dye, else none.
            hue_int = None
            if it.get("hue"):
                hue_int = int(it["hue"], 0) & 0x3FFF
            elif it.get("hue_random"):
                hue_int = NEUTRAL_CLOTHING_HUE
            hue_table = hue_to_table(hues, hue_int) if hue_int else None

            frames = decode_layer_rgba(ex, graphic, group_id, args.dir, hue_table)
            if frames is None or not any(f for f in frames):
                bad = f"{it['class']} (AnimID {aid}, graphic {graphic}) no frames"
                break
            rank = LAYER_RANK.get(it["layer"], 99)
            equip_layers.append((rank, it["class"], frames))
            layer_records.append({
                "class": it["class"],
                "item_id": it["item_id"],
                "layer": it["layer"],
                "anim_id": aid,
                "graphic": graphic,
                "hue": f"0x{hue_int:04X}" if hue_int else None,
            })

        if bad is not None:
            fallbacks.append((cls, bad))
            continue
        if not equip_layers:
            fallbacks.append((cls, "no equipment layers decoded"))
            continue

        equip_layers.sort(key=lambda t: t[0])
        layers = [("body", body_rgba)] + [(lbl, fr) for _r, lbl, fr in equip_layers]

        slug = class_slug(cls)
        gif_path = os.path.join(args.out, f"dressed-{slug}.gif")
        png_path = os.path.join(args.out, f"dressed-{slug}.png")
        try:
            n, size = compose_dressed(layers, gif_path, png_path)
        except Exception as e:  # noqa: BLE001
            failures.append((cls, f"compose error: {e}"))
            continue
        if n == 0:
            fallbacks.append((cls, "compose produced 0 frames"))
            continue

        results[cls] = {
            "slug": slug,
            "body_id": body_id,
            "group": group_name,
            "direction": args.dir,
            "frames": n,
            "size": list(size),
            "gif": f"/img/creatures/dressed-{slug}.gif",
            "png": f"/img/creatures/dressed-{slug}.png",
            "layers": layer_records,
        }
        print(f"ok   {cls}: {n} frames, {len(layer_records)} layers -> dressed-{slug}.gif")

    doc = {
        "_schema": {
            "description": "Dressed walking GIFs for humanoid bestiary mobs: the "
                           "body animation with each worn item's equipment "
                           "animation composited per-frame in paperdoll layer "
                           "order, per ClassicUO MobileView. Equipment animation "
                           "is indexed by item AnimID (tiledata.mul) at the "
                           "People group offset, Equipconv.def applied, tinted by "
                           "item hue (or neutral 1854 for random dye) via "
                           "hues.mul. Body keeps its native MUL palette.",
            "extracted_by": "tools/extract_anim_dressed.py",
            "sources": [
                "data/mob_appearance.json", "data/creature_anim.json",
                "uo-resource/anim*.mul", "uo-resource/tiledata.mul",
                "uo-resource/hues.mul", "uo-resource/Equipconv.def",
            ],
            "frame_duration_ms": FRAME_DURATION_MS,
            "skin_hue": SKIN_HUE,
            "neutral_clothing_hue": NEUTRAL_CLOTHING_HUE,
        },
        "_meta": {
            "extracted": date.today().isoformat(),
            "direction": args.dir,
            "dressed_ok": len(results),
            "fallbacks": [{"class": c, "reason": r} for c, r in fallbacks],
            "failures": [{"class": c, "reason": r} for c, r in failures],
        },
        "creatures": results,
    }
    if not args.only:
        with open(OUT_JSON, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2)
            f.write("\n")
        print(f"\nwrote {OUT_JSON}")

    print(f"\n{len(results)} dressed, {len(fallbacks)} fell back to bare body, "
          f"{len(failures)} errors")
    for c, r in fallbacks:
        print(f"  fallback {c}: {r}")
    for c, r in failures:
        print(f"  ERROR    {c}: {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
