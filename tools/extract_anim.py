# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Extract animated GIFs for bestiary creatures from the legacy UO anim MULs.

Ports ClassicUO's AnimationsLoader logic (src/ClassicUO.Assets/AnimationsLoader.cs):
  - mobtypes.txt   -> body type (monster/sea_monster/animal/human) + flags
  - Bodyconv.def   -> remaps a body into anim2/3/4/5 with a converted body id
  - index slot     -> CalculateLow/High/PeopleGroupOffset (5 stored dirs / group)
  - frame format   -> 256x ARGB1555 palette, frame offset table, row-run encoding

Reads  : /Users/dkkang/dev/uo/uowiki/data/creatures.json (body ids)
Writes : public/img/creatures/<body>.gif, data/creature_anim.json

Usage:
  uv run --script tools/extract_anim.py            # full extraction
  uv run --script tools/extract_anim.py --bodies 12 200 --dir 1 --out /tmp/spot
"""

from __future__ import annotations

import argparse
import json
import os
import struct
import sys
from datetime import date

from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCE_DIR = os.path.normpath(os.path.join(REPO_ROOT, "..", "uo-resource"))
CREATURES_JSON = os.path.join(REPO_ROOT, "data", "creatures.json")
OUT_GIF_DIR = os.path.join(REPO_ROOT, "public", "img", "creatures")
OUT_JSON = os.path.join(REPO_ROOT, "data", "creature_anim.json")

FRAME_DURATION_MS = 130

# AnimationGroupsType
MONSTER, SEA_MONSTER, ANIMAL, HUMAN, EQUIPMENT = 0, 1, 2, 3, 4
TYPE_NAMES = {"monster": MONSTER, "sea_monster": SEA_MONSTER, "animal": ANIMAL,
              "human": HUMAN, "equipment": EQUIPMENT}

# AnimationFlags
AF_CALC_OFFSET_LOW_GROUP_EXTENDED = 0x00020
AF_CALC_OFFSET_BY_LOW_GROUP = 0x00040
AF_CALC_OFFSET_BY_PEOPLE_GROUP = 0x00400

# offset groups
G_LOW, G_HIGH, G_PEOPLE = 1, 2, 3
GROUP_COUNT = {G_LOW: 13, G_HIGH: 22, G_PEOPLE: 35}

ANIM_FILE_NAMES = ["anim", "anim2", "anim3", "anim4", "anim5"]
IDX_ENTRY = struct.Struct("<III")  # Position, Size, Unknown


# ---------------------------------------------------------------- mul access

class AnimFiles:
    def __init__(self, resource_dir: str):
        self.idx: list[bytes | None] = [None] * 5
        self.mul: list = [None] * 5
        self.mul_len: list[int] = [0] * 5
        for i, name in enumerate(ANIM_FILE_NAMES):
            idx_path = os.path.join(resource_dir, f"{name}.idx")
            mul_path = os.path.join(resource_dir, f"{name}.mul")
            if os.path.exists(idx_path) and os.path.exists(mul_path):
                with open(idx_path, "rb") as f:
                    self.idx[i] = f.read()
                self.mul[i] = open(mul_path, "rb")
                self.mul_len[i] = os.path.getsize(mul_path)

    def read_slot(self, file_index: int, slot: int):
        """Return (pos, size) for an idx slot, or None if invalid/missing."""
        idx = self.idx[file_index]
        if idx is None:
            return None
        off = slot * IDX_ENTRY.size
        if off + IDX_ENTRY.size > len(idx):
            return None
        pos, size, _ = IDX_ENTRY.unpack_from(idx, off)
        if pos in (0, 0xFFFFFFFF) and size == 0:
            return None
        if pos == 0xFFFFFFFF or size in (0, 0xFFFFFFFF):
            return None
        if pos + size > self.mul_len[file_index]:
            return None
        return pos, size

    def read_data(self, file_index: int, pos: int, size: int) -> bytes:
        f = self.mul[file_index]
        f.seek(pos)
        return f.read(size)


# ---------------------------------------------------------------- def parsing

def _def_lines(path: str):
    """Yield whitespace-split token lists for non-comment def lines."""
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or not line[0].isdigit():
                continue
            # strip trailing comments
            for marker in ("#", "//"):
                p = line.find(marker)
                if p > 0:
                    line = line[:p]
            yield line.split()


def parse_mobtypes(path: str) -> dict[int, tuple[int, int]]:
    """body -> (type, flags)  [AnimationsLoader mobtypes.txt parsing]"""
    out: dict[int, tuple[int, int]] = {}
    if not os.path.exists(path):
        return out
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for raw in f:
            line = raw.strip()
            if not line or line[0] == "#" or not line[0].isdigit():
                continue
            parts = line.split()
            if len(parts) < 3:
                continue
            try:
                body = int(parts[0])
                typ = TYPE_NAMES.get(parts[1].lower())
                flagstr = parts[2]
                ci = flagstr.find("#")
                if ci == 0:
                    continue
                if ci > 0:
                    flagstr = flagstr[:ci]
                flags = int(flagstr, 16)
            except ValueError:
                continue
            if typ is not None:
                out[body] = (typ, flags)
    return out


def parse_bodyconv(path: str) -> dict[int, tuple[int, int]]:
    """body -> (file_index 1..4, converted_body)  [ProcessBodyConvDef]"""
    out: dict[int, tuple[int, int]] = {}
    if not os.path.exists(path):
        return out
    for parts in _def_lines(path):
        if len(parts) < 2:
            continue
        try:
            index = int(parts[0])
            vals = [int(p) for p in parts[1:5]]
        except ValueError:
            continue
        for i, body in enumerate(vals, start=1):
            if body < 0:
                continue
            out[index] = (i, body)  # last valid column wins (matches client loop)
    return out


def parse_body_def(path: str) -> dict[int, int]:
    """body -> replacement body  [ProcessBodyDef; {group} syntax]"""
    out: dict[int, int] = {}
    if not os.path.exists(path):
        return out
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or not line[0].isdigit():
                continue
            p = line.find("#")
            if p > 0:
                line = line[:p]
            # format: <index> {a, b, c} <hue>   or   <index> <a> <hue>
            try:
                lb = line.index("{")
                rb = line.index("}")
            except ValueError:
                parts = line.split()
                if len(parts) < 2:
                    continue
                try:
                    idx, group = int(parts[0]), [int(parts[1])]
                except ValueError:
                    continue
            else:
                try:
                    idx = int(line[:lb].split()[0])
                    group = [int(t) for t in line[lb + 1:rb].replace(",", " ").split()]
                except (ValueError, IndexError):
                    continue
            if not group:
                continue
            if idx in out:
                continue
            check = group[2] if len(group) >= 3 else group[0]
            out[idx] = check
    return out


# ---------------------------------------------------------------- offsets

def calc_type_by_graphic(graphic: int, file_index: int) -> int:
    if file_index == 1:  # anim2
        return MONSTER if graphic < 200 else ANIMAL
    if file_index == 2:  # anim3
        return ANIMAL if graphic < 300 else (MONSTER if graphic < 400 else HUMAN)
    return MONSTER if graphic < 200 else (ANIMAL if graphic < 400 else HUMAN)


def calc_offset(graphic: int, anim_type: int, flags: int) -> tuple[int, int, int]:
    """Return (byte_offset_into_idx, group_count, offset_group)."""
    group = None
    if anim_type == MONSTER:
        if flags & AF_CALC_OFFSET_BY_PEOPLE_GROUP:
            group = G_PEOPLE
        elif flags & AF_CALC_OFFSET_BY_LOW_GROUP:
            group = G_LOW
        else:
            group = G_HIGH
    elif anim_type == SEA_MONSTER:
        return graphic * 110 * IDX_ENTRY.size, GROUP_COUNT[G_LOW], G_HIGH
    elif anim_type == ANIMAL:
        if flags & AF_CALC_OFFSET_LOW_GROUP_EXTENDED:
            if flags & AF_CALC_OFFSET_BY_PEOPLE_GROUP:
                group = G_PEOPLE
            elif flags & AF_CALC_OFFSET_BY_LOW_GROUP:
                group = G_LOW
            else:
                group = G_HIGH
        else:
            group = G_LOW
    else:
        group = G_PEOPLE

    if group == G_LOW:
        return ((graphic - 200) * 65 + 22000) * IDX_ENTRY.size, GROUP_COUNT[G_LOW], G_LOW
    if group == G_HIGH:
        return graphic * 110 * IDX_ENTRY.size, GROUP_COUNT[G_HIGH], G_HIGH
    return ((graphic - 400) * 175 + 35000) * IDX_ENTRY.size, GROUP_COUNT[G_PEOPLE], G_PEOPLE


# walk / fallback action groups per offset group layout
PREFERRED_GROUPS = {
    G_LOW: [(0, "walk"), (2, "stand"), (9, "fidget")],
    G_HIGH: [(0, "walk"), (1, "stand"), (17, "fidget")],
    G_PEOPLE: [(0, "walk"), (4, "stand"), (5, "fidget")],
}


# ---------------------------------------------------------------- frame decode

def decode_frames(data: bytes):
    """Decode one (body, group, dir) blob -> (palette[256] of (r,g,b), frames).

    Each frame: dict(cx, cy, w, h, pixels)  where pixels is a bytearray of
    palette indices and 0xFF padding... we use a parallel coverage mask:
    pixels[i] == 256 means transparent. Stored as list[int] w*h.
    """
    if len(data) < 512 + 4:
        return None, []
    palette = [struct.unpack_from("<H", data, i * 2)[0] for i in range(256)]
    pal_rgb = []
    for c in palette:
        r = (c >> 10) & 0x1F
        g = (c >> 5) & 0x1F
        b = c & 0x1F
        pal_rgb.append(((r << 3) | (r >> 2), (g << 3) | (g >> 2), (b << 3) | (b >> 2)))

    base = 512
    (frame_count,) = struct.unpack_from("<I", data, base)
    if frame_count == 0 or frame_count > 1024:
        return pal_rgb, []
    if base + 4 + frame_count * 4 > len(data):
        return pal_rgb, []
    offsets = struct.unpack_from(f"<{frame_count}I", data, base + 4)

    frames = []
    for off in offsets:
        p = base + off
        if p + 8 > len(data):
            frames.append(None)
            continue
        cx, cy, w, h = struct.unpack_from("<hhhh", data, p)
        p += 8
        if w <= 0 or h <= 0:
            frames.append(None)
            continue
        pixels = [256] * (w * h)  # 256 == transparent
        ok = True
        while True:
            if p + 4 > len(data):
                ok = False
                break
            (header,) = struct.unpack_from("<I", data, p)
            p += 4
            if header == 0x7FFF7FFF:
                break
            run = header & 0x0FFF
            x = (header >> 22) & 0x3FF
            if x & 0x200:
                x -= 0x400
            y = (header >> 12) & 0x3FF
            if y & 0x200:
                y -= 0x400
            x += cx
            y += cy + h
            if p + run > len(data):
                ok = False
                break
            if 0 <= y < h and 0 <= x and x + run <= w:
                block = y * w + x
                for k in range(run):
                    pixels[block + k] = data[p + k]
            # out-of-bounds runs are clipped silently (matches buffer bounds)
            elif 0 <= y < h:
                block = y * w + x
                for k in range(run):
                    xx = x + k
                    if 0 <= xx < w:
                        pixels[block + k] = data[p + k]
            p += run
        if not ok:
            frames.append(None)
            continue
        frames.append({"cx": cx, "cy": cy, "w": w, "h": h, "pixels": pixels})
    return pal_rgb, frames


# ---------------------------------------------------------------- gif compose

def compose_gif(pal_rgb, frames, out_path: str) -> int:
    """Build an animated GIF from decoded frames. Returns frame count."""
    frames = [f for f in frames if f is not None]
    if not frames:
        return 0

    # union bounding box; anchor of each frame is at image pixel (cx, cy+h),
    # i.e. frame top-left sits at (-cx, -(cy+h)) relative to the anchor.
    left = min(-f["cx"] for f in frames)
    top = min(-(f["cy"] + f["h"]) for f in frames)
    right = max(-f["cx"] + f["w"] for f in frames)
    bottom = max(-(f["cy"] + f["h"]) + f["h"] for f in frames)
    cw, ch = right - left, bottom - top
    if cw <= 0 or ch <= 0 or cw > 1024 or ch > 1024:
        return 0

    # build gif palette: index 0 = transparent, then used colors
    used = set()
    for f in frames:
        used.update(i for i in f["pixels"] if i != 256)
    color_to_idx: dict[tuple[int, int, int], int] = {}
    for src_idx in sorted(used):
        rgb = pal_rgb[src_idx]
        if rgb not in color_to_idx:
            color_to_idx[rgb] = 0  # placeholder
    # assign indices 1..255; merge overflow to nearest existing color
    palette_list = [(0, 0, 0)]  # index 0: transparent (color irrelevant)
    assigned = {}
    for rgb in color_to_idx:
        if len(palette_list) < 256:
            assigned[rgb] = len(palette_list)
            palette_list.append(rgb)
        else:
            best = min(
                range(1, len(palette_list)),
                key=lambda i: sum((a - b) ** 2 for a, b in zip(palette_list[i], rgb)),
            )
            assigned[rgb] = best
    src_to_gif = {src: assigned[pal_rgb[src]] for src in used}

    flat_pal = []
    for rgb in palette_list:
        flat_pal.extend(rgb)
    flat_pal.extend([0] * (768 - len(flat_pal)))

    images = []
    for f in frames:
        buf = bytearray(cw * ch)  # 0 = transparent
        fx = -f["cx"] - left
        fy = -(f["cy"] + f["h"]) - top
        w, px = f["w"], f["pixels"]
        for row in range(f["h"]):
            dst = (fy + row) * cw + fx
            src = row * w
            for col in range(w):
                v = px[src + col]
                if v != 256:
                    buf[dst + col] = src_to_gif[v]
        img = Image.frombytes("P", (cw, ch), bytes(buf))
        img.putpalette(flat_pal)
        images.append(img)

    images[0].save(
        out_path,
        save_all=True,
        append_images=images[1:],
        duration=FRAME_DURATION_MS,
        loop=0,
        transparency=0,
        disposal=2,
        optimize=False,
    )
    return len(images)


# ---------------------------------------------------------------- extraction

class Extractor:
    def __init__(self):
        self.files = AnimFiles(RESOURCE_DIR)
        self.mobtypes = parse_mobtypes(os.path.join(RESOURCE_DIR, "mobtypes.txt"))
        self.bodyconv = parse_bodyconv(os.path.join(RESOURCE_DIR, "Bodyconv.def"))
        self.body_def = parse_body_def(os.path.join(RESOURCE_DIR, "Body.def"))

    def resolve(self, body: int, use_bodyconv: bool = True):
        """-> (file_index, conv_body, idx_byte_offset, group_count, offset_group)"""
        mob = self.mobtypes.get(body)
        flags = mob[1] if mob else 0
        file_index, conv_body = 0, body
        if use_bodyconv and body in self.bodyconv:
            file_index, conv_body = self.bodyconv[body]
            if self.files.idx[file_index] is None:
                file_index, conv_body = 0, body
        if mob and mob[0] != 5:
            anim_type = mob[0]
        else:
            anim_type = calc_type_by_graphic(conv_body, file_index)
        off, group_count, offset_group = calc_offset(conv_body, anim_type, flags)
        return file_index, conv_body, off, group_count, offset_group

    def try_decode(self, body: int, direction: int):
        """Try the preferred action groups; return (pal, frames, meta) or err str.

        No fallback to the un-converted anim.mul slot when the bodyconv target is
        empty: those legacy slots hold unrelated equipment art for UOP-era bodies.
        """
        file_index, conv_body, base_off, group_count, offset_group = self.resolve(body)
        base_slot = base_off // IDX_ENTRY.size
        errors = []
        for group_id, group_name in PREFERRED_GROUPS[offset_group]:
            if group_id >= group_count:
                continue
            slot = base_slot + group_id * 5 + direction
            loc = self.files.read_slot(file_index, slot)
            if loc is None:
                errors.append(f"{group_name}: empty idx slot")
                continue
            data = self.files.read_data(file_index, *loc)
            pal, frames = decode_frames(data)
            live = [f for f in frames if f is not None]
            if not live:
                errors.append(f"{group_name}: no decodable frames")
                continue
            meta = {
                "group": group_name,
                "anim_file": ANIM_FILE_NAMES[file_index] + ".mul",
                "conv_body": conv_body,
                "file_index": file_index,
            }
            return pal, live, meta
        return None, None, "; ".join(errors) if errors else "no valid slot"

    def extract_body(self, body: int, direction: int, out_dir: str):
        """Returns (meta dict) or raises ExtractError-as-string via tuple."""
        pal, frames, meta_or_err = self.try_decode(body, direction)
        used_body = body
        if pal is None and body in self.body_def and self.body_def[body] != body:
            # Body.def fallback replacement (client does this at draw time)
            repl = self.body_def[body]
            pal, frames, meta2 = self.try_decode(repl, direction)
            if pal is not None:
                meta2["via_body_def"] = repl
                meta_or_err = meta2
                used_body = repl
        if pal is None:
            return None, meta_or_err
        out_path = os.path.join(out_dir, f"{body}.gif")
        n = compose_gif(pal, frames, out_path)
        if n == 0:
            return None, "gif compose produced 0 frames"
        meta = meta_or_err
        meta["frames"] = n
        meta["used_body"] = used_body
        return meta, None


def load_creature_bodies():
    with open(CREATURES_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    creature_body: dict[str, int] = {}
    for c in data["creatures"]:
        b = c.get("body")
        if isinstance(b, list):
            b = next((x for x in b if isinstance(x, int) and x > 0), None)
        if isinstance(b, int) and b > 0:
            creature_body[c["class"]] = b
    return creature_body


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bodies", nargs="*", type=int, help="extract only these bodies")
    ap.add_argument("--dir", type=int, default=1, help="stored direction 0-4 (default 1)")
    ap.add_argument("--out", default=OUT_GIF_DIR, help="gif output dir")
    ap.add_argument("--no-json", action="store_true", help="skip writing creature_anim.json")
    args = ap.parse_args()

    ex = Extractor()
    creature_body = load_creature_bodies()
    if args.bodies:
        bodies = sorted(set(args.bodies))
        write_json = False
    else:
        bodies = sorted(set(creature_body.values()))
        write_json = not args.no_json

    os.makedirs(args.out, exist_ok=True)

    bodies_out = {}
    failures = []
    for body in bodies:
        try:
            meta, err = ex.extract_body(body, args.dir, args.out)
        except Exception as e:  # noqa: BLE001
            meta, err = None, f"exception: {e}"
        if meta is None:
            failures.append((body, err))
            print(f"FAIL body {body}: {err}")
            continue
        bodies_out[str(body)] = {
            "gif": f"/img/creatures/{body}.gif",
            "frames": meta["frames"],
            "group": meta["group"],
            "anim_file": meta["anim_file"],
        }
        if meta.get("via_body_def"):
            bodies_out[str(body)]["via_body_def"] = meta["via_body_def"]
        print(f"ok   body {body}: {meta['frames']} frames "
              f"({meta['group']}, {meta['anim_file']}"
              + (f", via Body.def -> {meta['via_body_def']}" if meta.get("via_body_def") else "")
              + ")")

    if write_json:
        out = {
            "_schema": {
                "bodies": "body id -> {gif path, frame count, action group, source anim file}",
                "creatures": "creature class -> body id used for its gif",
            },
            "_meta": {
                "generator": "tools/extract_anim.py",
                "extracted": date.today().isoformat(),
                "direction": args.dir,
                "frame_duration_ms": FRAME_DURATION_MS,
                "bodies_total": len(bodies),
                "bodies_ok": len(bodies_out),
                "failures": [{"body": b, "reason": r} for b, r in failures],
            },
            "bodies": bodies_out,
            "creatures": {
                cls: b for cls, b in sorted(creature_body.items())
                if str(b) in bodies_out
            },
        }
        with open(OUT_JSON, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
            f.write("\n")
        print(f"\nwrote {OUT_JSON}")

    print(f"\n{len(bodies_out)}/{len(bodies)} bodies extracted, {len(failures)} failures")
    if failures:
        print("failures:")
        for b, r in failures:
            print(f"  {b}: {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
