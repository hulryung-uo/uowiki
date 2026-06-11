# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Extract a comprehensive item catalog from ServUO Scripts/Items/.

Walks Scripts/Items/ recursively. For every CONCRETE item class (extends
Item or one of the known Base*Item / BaseWeapon / BaseArmor / BaseJewel /
BaseClothing / BaseHat / BaseShoes / Food / BasePotion etc. families) it
resolves:

  - ItemID    (via the same constructor/base-chain heuristics as
               tools/extract_art.py — reused by import)
  - name      (string literal in base("...")/Name="..." ; else a
               LabelNumber / cliloc int resolved via cliloc.json ; else a
               humanized class name, marked name_source="class")
  - weight    (a literal Weight = N, else null)
  - category    (top-level subdir under Scripts/Items/)
  - subcategory (next path segment, if any)

Abstract classes, Base* classes, and anything under Internal/, Corpses/,
Damageable/ are skipped. Classes whose ItemID cannot be statically
resolved (computed from random/array) are counted as skipped.

For every unique resolved item id it extracts the static art PNG into
public/img/items/<0xITEMID>.png (shared with crafting icons — keyed by id
so they dedupe).

Output: data/items.json.

Usage: uv run --script tools/extract_items.py
"""

import json
import os
import re
import sys
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib
# Reuse the working decoder + heuristics from extract_art (untouched).
import extract_art

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
SERVUO = "/Users/dkkang/dev/uo/servuo"
ITEMS_DIR = os.path.join(SERVUO, "Scripts", "Items")
CLILOC_PATH = "/Users/dkkang/dev/uo/anima/data/cliloc.json"
ART_PATTERN = extract_art.ART_PATTERN
STATIC_OFFSET = extract_art.STATIC_OFFSET

# Directories under Scripts/Items/ we never catalog.
SKIP_DIRS = {"Internal", "Corpses", "Damageable"}

# Base families: a class is an "item" if its base-chain reaches one of
# these (or "Item"). Used to filter out non-item classes that happen to
# live under Scripts/Items/ (attributes, helpers, components, etc.).
ITEM_BASE_HINTS = (
    "Item", "BaseWeapon", "BaseArmor", "BaseJewel", "BaseClothing",
    "BaseHat", "BaseShoes", "BaseShield", "BaseRanged", "BaseMeleeWeapon",
    "BaseStaff", "BaseSword", "BaseAxe", "BaseBashing", "BaseSpear",
    "BasePoleArm", "BaseKnife", "BaseWand", "BaseBook", "BaseContainer",
    "BasePotion", "BaseFood", "Food", "BeverageBottle", "BaseBeverage",
    "BaseReagent", "BaseTool", "BaseHarvestTool", "BaseRunicTool",
    "BaseInstrument", "BaseLight", "BaseAddon", "BaseAddonContainer",
    "BaseTalisman", "BaseQuiver", "BaseSpellbook", "Spellbook",
    "BaseGranite", "BaseIngot", "BaseOre", "BaseLog", "BaseLeather",
    "BaseHides", "BaseScales", "BaseClothMaterial", "BaseGem",
    "BaseRuneStone", "BaseDoor", "BaseHouseDoor", "BaseTrap", "BaseGate",
    "BaseMagicFish", "Fish", "BaseFish", "BaseCraftableArtifact",
    "BaseStatuette", "BaseAttachableEffect", "BaseLevelGem",
    "BaseEpaulettes", "BaseEarrings", "BaseRing", "BaseBracelet",
    "BaseNecklace", "BaseSandals", "BaseBoots", "BaseGloves",
    "BaseHelm", "BaseSuit", "BaseClothItem", "BaseOuterTorso",
    "BaseMiddleTorso", "BaseInnerTorso", "BaseInnerLegs", "BaseOuterLegs",
    "BaseWaist", "BasePants", "BaseShirt", "BaseCloak", "BaseMagicStaff",
)

# Don't catalog these abstract/utility base names even if concrete-looking.
SKIP_CLASS_PREFIXES = ("Base",)
SKIP_CLASS_NAMES = {
    "Item", "Food", "Spellbook", "Fish", "AddonComponent",
    "AddonContainerComponent", "LockableContainer", "Container",
}

NAME_ASSIGN_RE = re.compile(r'\bName\s*=\s*"((?:[^"\\]|\\.)*)"')
BASE_STR_RE = re.compile(r':\s*(?:base|this)\s*\(\s*"((?:[^"\\]|\\.)*)"')
LABELNUMBER_RE = re.compile(r"\bLabelNumber\s*=>?\s*(\d{4,7})\b")
LABELNUMBER_RET_RE = re.compile(
    r"public\s+override\s+int\s+LabelNumber\b[^{]*\{[^}]*?return\s+(\d{4,7})", re.S)
WEIGHT_RE = re.compile(r"\bWeight\s*=\s*(\d+(?:\.\d+)?)\b")


def is_concrete_class(name, body):
    """A class declaration is concrete if not marked `abstract`."""
    # find the declaration line for this class name
    m = re.search(
        r"(?:public|internal|protected|private)?\s*"
        r"((?:abstract\s+|sealed\s+|partial\s+|static\s+)*)class\s+" + re.escape(name) + r"\b",
        body)
    if m:
        return "abstract" not in m.group(1)
    return True


def reaches_item_base(classes, name, depth=0, seen=None):
    """True if name's base-chain reaches Item or a known item base family."""
    if seen is None:
        seen = set()
    if depth > 12 or name in seen:
        return False
    seen.add(name)
    if name in ITEM_BASE_HINTS:
        return True
    entry = classes.get(name)
    if entry is None:
        return False
    base = entry[0]
    if not base:
        return False
    base = base.split(".")[-1]
    if base in ITEM_BASE_HINTS:
        return True
    return reaches_item_base(classes, base, depth + 1, seen)


def category_of(path):
    """(category, subcategory) from a path under Scripts/Items/."""
    rel = os.path.relpath(path, ITEMS_DIR)
    parts = rel.split(os.sep)
    category = parts[0] if len(parts) > 1 else "Misc"
    subcategory = parts[1] if len(parts) > 2 else None
    return category, subcategory


def resolve_name(classes, cliloc, name, depth=0, seen=None):
    """Return (display_name, name_source) for a class.

    name_source in {"literal", "cliloc", "class"}.
    """
    if seen is None:
        seen = set()
    if depth > 10 or name in seen:
        return None, None
    seen.add(name)
    entry = classes.get(name)
    if entry is None:
        return None, None
    base, body, _path = entry

    # literal string in base("...") / this("...")
    m = BASE_STR_RE.search(body)
    if m and m.group(1).strip():
        return m.group(1).strip(), "literal"
    # Name = "..."
    m = NAME_ASSIGN_RE.search(body)
    if m and m.group(1).strip():
        return m.group(1).strip(), "literal"
    # LabelNumber => 1234567  or  return 1234567 in LabelNumber override
    for rx in (LABELNUMBER_RE, LABELNUMBER_RET_RE):
        m = rx.search(body)
        if m:
            cid = m.group(1)
            txt = cliloc.get(cid)
            if txt:
                return txt, "cliloc"
    # recurse base
    if base:
        bn = base.split(".")[-1]
        if bn not in ("Item", "object", ""):
            r, src = resolve_name(classes, cliloc, bn, depth + 1, seen)
            if r:
                return r, src
    return None, None


def resolve_weight(classes, name, depth=0, seen=None):
    if seen is None:
        seen = set()
    if depth > 8 or name in seen:
        return None
    seen.add(name)
    entry = classes.get(name)
    if entry is None:
        return None
    base, body, _path = entry
    m = WEIGHT_RE.search(body)
    if m:
        v = float(m.group(1))
        return int(v) if v == int(v) else v
    if base:
        bn = base.split(".")[-1]
        if bn not in ("Item", "object", ""):
            return resolve_weight(classes, bn, depth + 1, seen)
    return None


def main():
    cliloc = json.load(open(CLILOC_PATH))
    print("indexing ServUO classes ...")
    classes = extract_art.index_classes()
    print(f"  {len(classes)} classes indexed")

    # Walk only Scripts/Items/, collecting concrete item classes.
    candidates = OrderedDict()  # name -> path (only those under Items/)
    for name, (base, body, path) in classes.items():
        if not path.startswith(ITEMS_DIR):
            continue
        rel = os.path.relpath(path, ITEMS_DIR)
        top = rel.split(os.sep)[0]
        if top in SKIP_DIRS:
            continue
        if name in SKIP_CLASS_NAMES:
            continue
        if name.startswith(SKIP_CLASS_PREFIXES):
            continue
        if not is_concrete_class(name, body):
            continue
        if not reaches_item_base(classes, name):
            continue
        candidates[name] = path

    print(f"  {len(candidates)} concrete item-class candidates")

    # Resolve item ids.
    items = []
    skipped = []  # (class, reason)
    resolved_ids = {}  # name -> item_id
    for name in candidates:
        item_id, _via = extract_art.resolve_item_id(classes, name)
        if item_id is None or not (0 < item_id < 0x10000):
            skipped.append((name, "no static ItemID"))
            continue
        resolved_ids[name] = item_id

    # Extract art for unique ids.
    out_dir = os.path.join(ROOT, "public", "img", "items")
    os.makedirs(out_dir, exist_ok=True)
    uop = uoplib.UopFile(os.path.join(UO_DIR, "artLegacyMUL.uop"))

    existing_pngs = set(
        fn[:-4] for fn in os.listdir(out_dir)
        if fn.startswith("0x") and fn.endswith(".png"))
    written_new = set()
    png_for_id = {}  # item_id -> png path or None (no art)
    no_art = set()

    def ensure_png(item_id):
        hexid = f"0x{item_id:04X}"
        if hexid in png_for_id:
            return png_for_id[hexid]
        if item_id in no_art:
            return None
        png_rel = f"/img/items/{hexid}.png"
        if hexid in existing_pngs:
            png_for_id[hexid] = png_rel
            return png_rel
        entry = uop.get_by_name(ART_PATTERN % (item_id + STATIC_OFFSET))
        if entry is None:
            no_art.add(item_id)
            return None
        try:
            img = extract_art.decode_static_art(uop.read(entry))
        except Exception:
            img = None
        if img is None:
            no_art.add(item_id)
            return None
        img.save(os.path.join(out_dir, f"{hexid}.png"))
        written_new.add(hexid)
        existing_pngs.add(hexid)
        png_for_id[hexid] = png_rel
        return png_rel

    for name in candidates:
        if name not in resolved_ids:
            continue
        item_id = resolved_ids[name]
        path = candidates[name]
        category, subcategory = category_of(path)
        disp, name_source = resolve_name(classes, cliloc, name)
        if not disp:
            disp = extract_art.class_display_name(name)
            name_source = "class"
        weight = resolve_weight(classes, name)
        png = ensure_png(item_id)
        items.append({
            "class": name,
            "item_id": f"0x{item_id:04X}",
            "name": disp,
            "name_source": name_source,
            "weight": weight,
            "category": category,
            "subcategory": subcategory,
            "png": png,
            "source": "Scripts/Items/" + os.path.relpath(path, ITEMS_DIR).replace(os.sep, "/"),
        })

    # Sort by category, subcategory, name (case-insensitive).
    items.sort(key=lambda it: (
        it["category"].lower(),
        (it["subcategory"] or "").lower(),
        it["name"].lower(),
        it["class"].lower(),
    ))

    by_category = {}
    for it in items:
        by_category[it["category"]] = by_category.get(it["category"], 0) + 1

    doc = {
        "_schema": {
            "description": "Comprehensive item catalog extracted from ServUO "
                           "Scripts/Items/. One entry per concrete item class. "
                           "item_id resolved from constructors/base chains; name "
                           "from a base(\"...\")/Name literal, a LabelNumber cliloc, "
                           "or a humanized class name (see name_source). PNGs are "
                           "static art from artLegacyMUL.uop keyed by item id and "
                           "shared with crafting icons.",
            "extracted_by": "tools/extract_items.py",
            "sources": ["uo-resource/artLegacyMUL.uop", "servuo: Scripts/Items/**",
                        "anima/data/cliloc.json"],
            "fields": {
                "name_source": "literal | cliloc | class",
                "weight": "literal Weight or null",
                "png": "static art path, or null if no art entry exists",
            },
        },
        "_meta": {
            "item_count": len(items),
            "candidate_count": len(candidates),
            "skipped_count": len(skipped),
            "unique_pngs": len([p for p in png_for_id.values() if p]),
            "new_pngs_this_run": len(written_new),
            "no_art_count": len(no_art),
            "by_category": dict(sorted(by_category.items())),
            "skipped": [{"class": c, "reason": r} for c, r in sorted(skipped)],
        },
        "items": items,
    }
    with open(os.path.join(ROOT, "data", "items.json"), "w") as f:
        json.dump(doc, f, indent=2, sort_keys=False)
        f.write("\n")

    # Report.
    print(f"\nitems cataloged   : {len(items)}")
    print(f"candidates        : {len(candidates)}")
    print(f"skipped (no id)   : {len(skipped)}")
    print(f"items with no art : {len(no_art)}")
    print(f"unique PNGs used  : {len([p for p in png_for_id.values() if p])}")
    print(f"new PNGs this run : {len(written_new)}")
    print(f"total PNGs in dir : {len(existing_pngs)}")
    print("by category:")
    for cat, n in sorted(by_category.items()):
        print(f"  {cat:14s} {n}")
    # name source breakdown
    src_counts = {}
    for it in items:
        src_counts[it["name_source"]] = src_counts.get(it["name_source"], 0) + 1
    print("name sources:", dict(sorted(src_counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
