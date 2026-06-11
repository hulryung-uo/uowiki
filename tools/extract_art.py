# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Extract item (static) art PNGs from artLegacyMUL.uop.

Which items: every item class referenced by data/recipes.json (recipe
outputs `item_type` + resource `type` fields) plus a curated list of
reagents / raw resources / common tools. ItemIDs are resolved by parsing
ServUO item scripts: `: base(0x1BF2)` / `: this(0x...)` constructor
chains and `ItemID = 0x...` assignments, following base classes when a
class has no literal of its own (e.g. IronIngot -> BaseIngot).

Static art format (confirmed in ClassicUO ArtLoader.LoadArt):
  UOP entry name "build/artlegacymul/%08d.tga" where the file index is
  item_id + 0x4000 (indices < 0x4000 are land tiles, raw 44x44).
  Entry payload (flag 0 = uncompressed in this uop):
    u32 flags, i16 width, i16 height,
    u16 lineoffsets[height]   (in u16 words, relative to end of this table)
    rows of RLE runs: (u16 xoffset, u16 run) then `run` u16 ARGB1555
    pixels; xoffset+run == 0 ends the row; xoffset+run >= 2048 ends image.
    color 0 = transparent.

Output:
  public/img/items/<0xITEMID>.png
  data/item_art.json   (class name -> item_id/png/name)
"""

import json
import os
import re
import struct
import sys
from collections import OrderedDict

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
SERVUO = "/Users/dkkang/dev/uo/servuo"
ART_PATTERN = "build/artlegacymul/%08d.tga"
STATIC_OFFSET = 0x4000

# --- curated always-include list -------------------------------------------

REAGENTS = [
    "BlackPearl", "Bloodmoss", "Garlic", "Ginseng",
    "MandrakeRoot", "Nightshade", "SpidersSilk", "SulfurousAsh",
]

TOOL_CANDIDATES = [
    "Pickaxe", "Shovel", "Hatchet", "Tongs", "SewingKit", "TinkerTools",
    "TinkersTools", "MortarPestle", "ScribesPen", "Saw", "SmithHammer",
    "SmithyHammer", "SmithsHammer", "FletcherTools", "DovetailSaw",
    "MapmakersPen", "FlourSifter", "Skillet", "RollingPin", "Scorp",
]

MISC_CURATED = [
    "Bandage", "Spellbook", "Runebook", "RuneBook", "RecallRune",
    "Bow", "Crossbow", "HeavyCrossbow", "Katana",
]

# resource classes are enumerated from Scripts/Items/Resource/ by suffix
RESOURCE_SUFFIXES = ("Ingot", "Ore", "Log", "Board", "Leather", "Hides")
RESOURCE_EXACT = {"Log", "Board", "Cloth", "UncutCloth", "BoltOfCloth",
                  "Leather", "Hides", "Bandage"}

# --- ServUO class parsing ---------------------------------------------------

CLASS_RE = re.compile(
    r"^\s*(?:public|internal)?\s*(?:abstract\s+|sealed\s+|partial\s+)*class\s+"
    r"(\w+)\s*(?::\s*([\w.]+))?", re.M)
CTOR_CHAIN_RE = re.compile(r":\s*(?:base|this)\s*\(([^)]*)\)")
FIRST_ARG_RE = re.compile(r"^\s*(0x[0-9A-Fa-f]+|\d+)\s*(?:,|$)")
HEX_RE = re.compile(r"0x[0-9A-Fa-f]+")
ITEMID_RE = re.compile(r"\bItemID\s*=\s*(0x[0-9A-Fa-f]+|\d+)\b")
RETURN_HEX_RE = re.compile(r"\breturn\s+(0x[0-9A-Fa-f]+)\b")

MIN_ITEM_ID = 0x100  # filters out hue/amount literals like this(0)
MAX_ITEM_ID = 0xFFFF


def _plausible(v: int) -> bool:
    return MIN_ITEM_ID <= v <= MAX_ITEM_ID


def index_classes():
    """name -> (base_name, body, path). Scripts/Items wins on duplicates."""
    classes = {}
    scan_roots = [
        os.path.join(SERVUO, "Scripts", "Items"),
        os.path.join(SERVUO, "Scripts", "Services"),
        os.path.join(SERVUO, "Scripts"),
    ]
    seen_files = set()
    for root in scan_roots:
        for dirpath, _dirs, files in os.walk(root):
            for fn in files:
                if not fn.endswith(".cs"):
                    continue
                path = os.path.join(dirpath, fn)
                if path in seen_files:
                    continue
                seen_files.add(path)
                try:
                    text = open(path, encoding="utf-8-sig", errors="replace").read()
                except OSError:
                    continue
                matches = list(CLASS_RE.finditer(text))
                for i, m in enumerate(matches):
                    name, base = m.group(1), m.group(2)
                    body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
                    if name not in classes:
                        classes[name] = (base, text[m.start():body_end], path)
    return classes


def resolve_item_id(classes, name, depth=0):
    """Return (item_id, via_class) or (None, reason).

    Candidate tiers, first plausible literal wins:
      1. literal first argument of a `: base(...)` / `: this(...)` chain
         (e.g. `: base(0x13FF)`, `: base(0xF7A, amount)`)
      2. hex default value of a constructor parameter
         (e.g. `public Runebook(int maxCharges, int id = 0x22C5)`)
      3. any hex literal inside a base/this chain argument list
         (e.g. `: this(content, 0xEFA)`, `: base(Core.AOS ? id : 0xEFA)`)
      4. `ItemID = 0x...` assignment
      5. `return 0x...` (ComputeItemID-style classes, e.g. beverages)
      6. recurse into the base class (e.g. IronIngot -> BaseIngot)
    """
    if depth > 10:
        return None, "base-chain too deep"
    entry = classes.get(name)
    if entry is None:
        return None, "class not found"
    base, body, _path = entry

    chains = [m.group(1) for m in CTOR_CHAIN_RE.finditer(body)]

    # tier 1: literal first chain argument
    for args in chains:
        m = FIRST_ARG_RE.match(args)
        if m and _plausible(int(m.group(1), 0)):
            return int(m.group(1), 0), name
    # tier 2: ctor parameter defaults
    for m in re.finditer(r"public\s+%s\s*\(([^)]*)\)" % re.escape(name), body):
        for h in HEX_RE.findall(m.group(1)):
            if _plausible(int(h, 0)):
                return int(h, 0), name
    # tier 3: any hex literal in chain args
    for args in chains:
        for h in HEX_RE.findall(args):
            if _plausible(int(h, 0)):
                return int(h, 0), name
    # tier 3b: decimal literals >= 0x1000 in chain args (e.g. Cannonball
    # `: this(amount, 16932)`; amounts/hues are never that large)
    for args in chains:
        for d in re.findall(r"\b(\d{4,6})\b", args):
            if 0x1000 <= int(d) <= MAX_ITEM_ID:
                return int(d), name
    # tier 4: ItemID assignment
    for m in ITEMID_RE.finditer(body):
        if _plausible(int(m.group(1), 0)):
            return int(m.group(1), 0), name
    # tier 5: hex return values (ComputeItemID etc.)
    for m in RETURN_HEX_RE.finditer(body):
        if _plausible(int(m.group(1), 0)):
            return int(m.group(1), 0), name
    # tier 6: follow base class
    if base and base not in ("Item", "object"):
        return resolve_item_id(classes, base.split(".")[-1], depth + 1)
    return None, f"no itemID literal (base={base})"


# --- art decoding ------------------------------------------------------------

def decode_static_art(payload: bytes) -> Image.Image | None:
    if len(payload) < 8:
        return None
    _flags, w, h = struct.unpack_from("<Ihh", payload, 0)
    if w <= 0 or h <= 0 or w > 1024 or h > 1024:
        return None
    buf = payload[8:]
    lineoffsets = struct.unpack_from("<%dH" % h, buf, 0)
    datastart = h * 2
    tbl = uoplib.COLOR_TABLE_5TO8

    out = bytearray(w * h * 4)
    y = 0
    x = 0
    ptr = datastart + lineoffsets[0] * 2
    while y < h:
        if ptr + 4 > len(buf):
            break
        xoffs, run = struct.unpack_from("<HH", buf, ptr)
        ptr += 4
        if xoffs + run >= 2048:
            break
        if xoffs + run != 0:
            x += xoffs
            pixels = struct.unpack_from("<%dH" % run, buf, ptr)
            ptr += run * 2
            base = (y * w + x) * 4
            for val in pixels:
                if val != 0:
                    out[base] = tbl[(val >> 10) & 0x1F]
                    out[base + 1] = tbl[(val >> 5) & 0x1F]
                    out[base + 2] = tbl[val & 0x1F]
                    out[base + 3] = 255
                base += 4
            x += run
        else:
            x = 0
            y += 1
            if y < h:
                ptr = datastart + lineoffsets[y] * 2
    return Image.frombytes("RGBA", (w, h), bytes(out))


def class_display_name(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", " ", name).lower()


# --- main --------------------------------------------------------------------

def main() -> int:
    recipes = json.load(open(os.path.join(ROOT, "data", "recipes.json")))

    wanted = OrderedDict()  # class name -> display name (or None)
    def want(cls, disp=None):
        if cls not in wanted or (disp and not wanted[cls]):
            wanted[cls] = disp

    for key, system in recipes.items():
        if key == "_schema":
            continue
        for r in system.get("recipes", []):
            want(r["item_type"], r.get("name"))
            for res in r.get("resources", []):
                want(res["type"], res.get("name"))

    print("indexing ServUO classes ...")
    classes = index_classes()
    print(f"  {len(classes)} classes indexed")

    # curated: reagents + misc + existing tools
    for cls in REAGENTS + MISC_CURATED:
        if cls in classes:
            want(cls)
    tools_found = [c for c in TOOL_CANDIDATES if c in classes]
    for cls in tools_found:
        want(cls)

    # curated: all resource classes under Scripts/Items/Resource/
    resource_dir = os.path.join(SERVUO, "Scripts", "Items", "Resource")
    n_resource = 0
    for name, (_base, _body, path) in classes.items():
        if not path.startswith(resource_dir):
            continue
        if name.endswith(RESOURCE_SUFFIXES) or name in RESOURCE_EXACT:
            if not name.startswith("Base"):
                want(name)
                n_resource += 1

    print(f"target classes: {len(wanted)} "
          f"(recipes + {len(REAGENTS)} reagents, {len(tools_found)} tools, "
          f"{n_resource} resource classes)")

    # resolve item ids
    resolved = {}
    unresolved = {}
    for cls in wanted:
        item_id, via = resolve_item_id(classes, cls)
        if item_id is not None and 0 < item_id < 0x10000:
            resolved[cls] = item_id
        else:
            unresolved[cls] = via

    # extract art
    out_dir = os.path.join(ROOT, "public", "img", "items")
    os.makedirs(out_dir, exist_ok=True)
    uop = uoplib.UopFile(os.path.join(UO_DIR, "artLegacyMUL.uop"))

    items = {}
    no_art = {}
    written_pngs = set()
    for cls in sorted(resolved):
        item_id = resolved[cls]
        entry = uop.get_by_name(ART_PATTERN % (item_id + STATIC_OFFSET))
        if entry is None:
            no_art[cls] = f"0x{item_id:04X}: no art entry"
            continue
        img = decode_static_art(uop.read(entry))
        if img is None:
            no_art[cls] = f"0x{item_id:04X}: undecodable art"
            continue
        hexid = f"0x{item_id:04X}"
        png_rel = f"/img/items/{hexid}.png"
        if hexid not in written_pngs:
            img.save(os.path.join(out_dir, f"{hexid}.png"))
            written_pngs.add(hexid)
        items[cls] = {
            "item_id": hexid,
            "png": png_rel,
            "name": wanted.get(cls) or class_display_name(cls),
        }

    # drop stale PNGs from previous runs
    removed = 0
    for fn in os.listdir(out_dir):
        if fn.startswith("0x") and fn.endswith(".png") and fn[:-4] not in written_pngs:
            os.remove(os.path.join(out_dir, fn))
            removed += 1
    if removed:
        print(f"removed {removed} stale PNGs")

    doc = {
        "_schema": {
            "description": "Static item art PNGs extracted from artLegacyMUL.uop for "
                           "item classes used by data/recipes.json plus curated "
                           "reagents/resources/tools. Keyed by ServUO item class name. "
                           "item_id resolved from ServUO constructors.",
            "extracted_by": "tools/extract_art.py",
            "sources": ["uo-resource/artLegacyMUL.uop", "servuo: Scripts/Items/**"],
        },
        "items": items,
    }
    with open(os.path.join(ROOT, "data", "item_art.json"), "w") as f:
        json.dump(doc, f, indent=2, sort_keys=False)
        f.write("\n")

    print(f"\nresolved item ids : {len(resolved)}/{len(wanted)} classes")
    print(f"art extracted     : {len(items)} classes -> {len(written_pngs)} unique PNGs")
    if unresolved:
        print(f"unresolved ({len(unresolved)}):")
        for cls, why in sorted(unresolved.items()):
            print(f"  {cls}: {why}")
    if no_art:
        print(f"no art ({len(no_art)}):")
        for cls, why in sorted(no_art.items()):
            print(f"  {cls}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
