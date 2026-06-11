#!/usr/bin/env python3
"""Extract the ServUO plant (gardening) system into data/plants.json.

Reads ../servuo/Scripts/Services/Plants/:
  - PlantItem.cs       enum PlantStatus     -> growth stages
  - PlantType.cs       enum PlantType + PlantTypeInfo[] m_Table -> growable plants
                       (itemID, flowery, crossable, reproduces, category)
  - PlantHue.cs        enum PlantHue + PlantHueInfo m_Table -> colours
                       (display hue, gump hue, name cliloc, bright/crossable/reproduces)
  - PlantResources.cs  PlantResourceInfo[] m_ResourceList -> what plants yield

Plant-type display names are computed the way ServUO does it
(PlantTypeInfo.Name): for art tile id < 0x4000 the cliloc is 1020000 + itemID,
otherwise 1078872 + itemID. Hue/category/status names come straight from their
LabelNumber clilocs. All cliloc text is resolved via ../anima/data/cliloc.json.

Output: data/plants.json
  { stages: [...], plant_types: [...], plant_hues: [...], resources: [...] }

Usage: python3 tools/extract_plants.py
Stdlib only.
"""

import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
SERVUO = WIKI_ROOT.parent / "servuo"
PLANTS_DIR = SERVUO / "Scripts" / "Services" / "Plants"
CLILOC_PATH = WIKI_ROOT.parent / "anima" / "data" / "cliloc.json"
ITEMS_PATH = WIKI_ROOT / "data" / "items.json"
OUT_PATH = WIKI_ROOT / "data" / "plants.json"


def load_cliloc():
    if not CLILOC_PATH.exists():
        return {}
    raw = json.load(CLILOC_PATH.open(encoding="utf-8"))
    # keys are strings like "1060813"
    return {int(k): v for k, v in raw.items()}


def cliloc(table, num):
    if num is None or num < 0:
        return None
    return table.get(num)


def load_item_names():
    """Map item_id int -> display name, from data/items.json (for resources)."""
    out = {}
    if not ITEMS_PATH.exists():
        return out
    data = json.load(ITEMS_PATH.open(encoding="utf-8"))
    for it in data.get("items", []):
        cls = it.get("class")
        if cls:
            out.setdefault(cls, {"item_id": it.get("item_id"), "name": it.get("name")})
    return out


def parse_int(tok):
    tok = tok.strip()
    if tok.startswith("0x") or tok.startswith("0X"):
        return int(tok, 16)
    return int(tok)


# ---------------------------------------------------------------------------
# PlantStatus (growth stages)
# ---------------------------------------------------------------------------
def parse_stages(text):
    """The named, gameplay-meaningful PlantStatus values (skip the StageN aliases)."""
    # only the descriptive block before the StageN aliases
    block = text.split("enum PlantStatus", 1)[1].split("}", 1)[0]
    named = {}
    for m in re.finditer(r"(\w+)\s*=\s*(\d+)", block):
        name, val = m.group(1), int(m.group(2))
        named.setdefault(val, name)
    # The descriptive labels the client uses (PlantItem.GetLocalizedPlantStatus
    # / OnSingleClick): dirt -> seed -> sapling -> plant -> full grown -> decorative.
    order = [
        ("BowlOfDirt", 0, "An empty plant bowl filled with dirt. Soften it with water, then plant a seed."),
        ("Seed", 1, "A seed has been planted. Keep the water level steady and it will sprout."),
        ("Sapling", 2, "A young sapling (stages 2-3). It keeps growing on each daily check."),
        ("Plant", 4, "A recognisable plant (stages 4-6). The bowl turns green."),
        ("FullGrownPlant", 7, "Fully grown (stages 7-9). It now shows its type and colour, can be pollinated, and yields seeds/resources."),
        ("DecorativePlant", 10, "Set to decorative: a finished houseplant that no longer needs watering and can be placed for decoration."),
        ("DeadTwigs", 11, "Dead twigs. The plant was neglected or killed; only twigs remain."),
    ]
    stages = []
    for name, val, desc in order:
        stages.append({"name": name, "value": val, "description": desc})
    return stages


# ---------------------------------------------------------------------------
# PlantType + PlantTypeInfo
# ---------------------------------------------------------------------------
RE_TYPEINFO = re.compile(
    r"new\s+PlantTypeInfo\(\s*"
    r"(?P<item>0x[0-9A-Fa-f]+|\d+)\s*,\s*"
    r"(?P<ox>-?\d+)\s*,\s*"
    r"(?P<oy>-?\d+)\s*,\s*"
    r"PlantType\.(?P<type>\w+)\s*,\s*"
    r"(?P<contains>true|false)\s*,\s*"
    r"(?P<flowery>true|false)\s*,\s*"
    r"(?P<crossable>true|false)\s*,\s*"
    r"(?P<reproduces>true|false)\s*,\s*"
    r"PlantCategory\.(?P<category>\w+)"
)


def plant_name_cliloc(item_id):
    return (1020000 + item_id) if item_id < 0x4000 else (1078872 + item_id)


def parse_plant_types(text, cl):
    rows = []
    for m in RE_TYPEINFO.finditer(text):
        item_id = parse_int(m.group("item"))
        name_cliloc = plant_name_cliloc(item_id)
        name = cliloc(cl, name_cliloc)
        rows.append({
            "type": m.group("type"),
            "name": name,
            "name_cliloc": name_cliloc,
            "item_id": f"0x{item_id:04X}",
            "category": m.group("category"),
            "flowery": m.group("flowery") == "true",
            "crossable": m.group("crossable") == "true",
            "reproduces": m.group("reproduces") == "true",
        })
    return rows


# ---------------------------------------------------------------------------
# PlantHue + PlantHueInfo
# ---------------------------------------------------------------------------
RE_HUEINFO = re.compile(
    r"m_Table\[PlantHue\.(?P<key>\w+)\]\s*=\s*new\s+PlantHueInfo\(\s*"
    r"(?P<hue>0x[0-9A-Fa-f]+|\d+)\s*,\s*"
    r"(?P<name>\d+)\s*,\s*"
    r"PlantHue\.(?P<phue>\w+)"
    r"(?:\s*,\s*(?P<gump>0x[0-9A-Fa-f]+|\d+))?"
)

# the [Flags] enum body, to learn which hues are Bright/Crossable/Reproduces
RE_HUE_DEF = re.compile(r"^\s*(\w+)\s*=\s*(.+?),?\s*$", re.MULTILINE)


def parse_hue_flags(text):
    """Resolve each named PlantHue to its bright/crossable/reproduces booleans."""
    block = text.split("enum PlantHue", 1)[1].split("}", 1)[0]
    BRIGHT, CROSS, REPRO = 0x8000000, 0x4000000, 0x2000000
    vals = {}
    # iteratively resolve symbolic expressions
    for _ in range(6):
        for m in RE_HUE_DEF.finditer(block):
            name, expr = m.group(1), m.group(2).strip()
            if name in vals:
                continue
            total = 0
            ok = True
            for part in expr.split("|"):
                part = part.strip()
                if not part:
                    ok = False
                    break
                if part.startswith("0x") or part.startswith("0X") or part.isdigit():
                    total |= parse_int(part)
                elif part in vals:
                    total |= vals[part]
                else:
                    ok = False
                    break
            if ok:
                vals[name] = total
    flags = {}
    for name, v in vals.items():
        flags[name] = {
            "bright": bool(v & BRIGHT),
            "crossable": bool(v & CROSS),
            "reproduces": bool(v & REPRO),
        }
    return flags


def parse_plant_hues(text, cl):
    flags = parse_hue_flags(text)
    rows = []
    for m in RE_HUEINFO.finditer(text):
        key = m.group("key")
        name_cliloc = int(m.group("name"))
        f = flags.get(key, {})
        rows.append({
            "hue_name": key,
            "name": cliloc(cl, name_cliloc),
            "name_cliloc": name_cliloc,
            "display_hue": f"0x{parse_int(m.group('hue')):X}",
            "gump_hue": f"0x{parse_int(m.group('gump')):X}" if m.group("gump") else f"0x{parse_int(m.group('hue')):X}",
            "bright": f.get("bright", False),
            "crossable": f.get("crossable", False),
            "reproduces": f.get("reproduces", False),
        })
    return rows


# ---------------------------------------------------------------------------
# PlantResources
# ---------------------------------------------------------------------------
RE_RESINFO = re.compile(
    r"new\s+PlantResourceInfo\(\s*"
    r"PlantType\.(?P<type>\w+)\s*,\s*"
    r"PlantHue\.(?P<hue>\w+)\s*,\s*"
    r"typeof\((?P<res>\w+)\)\s*\)"
)


def parse_resources(text, item_names):
    rows = []
    seen = set()
    for m in RE_RESINFO.finditer(text):
        key = (m.group("type"), m.group("hue"), m.group("res"))
        if key in seen:
            continue
        seen.add(key)
        info = item_names.get(m.group("res"), {})
        rows.append({
            "plant_type": m.group("type"),
            "required_hue": m.group("hue"),
            "resource_class": m.group("res"),
            "resource_name": info.get("name"),
            "resource_item_id": info.get("item_id"),
        })
    return rows


def main():
    cl = load_cliloc()
    item_names = load_item_names()

    status_text = (PLANTS_DIR / "PlantItem.cs").read_text(encoding="utf-8")
    type_text = (PLANTS_DIR / "PlantType.cs").read_text(encoding="utf-8")
    hue_text = (PLANTS_DIR / "PlantHue.cs").read_text(encoding="utf-8")
    res_text = (PLANTS_DIR / "PlantResources.cs").read_text(encoding="utf-8")

    stages = parse_stages(status_text)
    plant_types = parse_plant_types(type_text, cl)
    plant_hues = parse_plant_hues(hue_text, cl)
    resources = parse_resources(res_text, item_names)

    out = {
        "_meta": {
            "extracted_by": "tools/extract_plants.py",
            "sources": [
                "servuo: Scripts/Services/Plants/PlantItem.cs",
                "servuo: Scripts/Services/Plants/PlantType.cs",
                "servuo: Scripts/Services/Plants/PlantHue.cs",
                "servuo: Scripts/Services/Plants/PlantResources.cs",
                "servuo: Scripts/Services/Plants/PlantSystem.cs",
                "anima/data/cliloc.json",
                "uowiki/data/items.json",
            ],
            "notes": {
                "growth_check_delay_hours": 23.0,
                "ideal_water_level": 2,
                "water_range": "0-4",
                "malady_range": "0-2 each (infestation, fungus, poison, disease)",
                "plant_name_cliloc_rule": "itemID < 0x4000 ? 1020000+itemID : 1078872+itemID (PlantTypeInfo.Name)",
            },
        },
        "stages": stages,
        "plant_types": plant_types,
        "plant_hues": plant_hues,
        "resources": resources,
    }

    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    missing_type_names = [t["type"] for t in plant_types if not t["name"]]
    print(f"stages:       {len(stages)}")
    print(f"plant_types:  {len(plant_types)}")
    print(f"plant_hues:   {len(plant_hues)}")
    print(f"resources:    {len(resources)}")
    if missing_type_names:
        print(f"WARNING: {len(missing_type_names)} plant types had no cliloc name: {missing_type_names}", file=sys.stderr)
    print(f"-> {OUT_PATH.relative_to(WIKI_ROOT)}")


if __name__ == "__main__":
    main()
