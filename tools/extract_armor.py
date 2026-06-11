# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Extract the armor reference from ServUO into data/armor.json.

Parses every concrete armor class under
  ../servuo/Scripts/Items/Equipment/Armor/*.cs
together with the shared logic in BaseArmor.cs / ArmorEnums.cs.

For each concrete BaseArmor (and BaseShield) subclass we resolve, walking
the in-file parent chain so subclasses inherit values they don't override:

  - class / source file
  - material        (ArmorMaterialType override; BaseShield defaults Plate)
  - slot            (body position, derived from the class-name keyword and
                     the BaseArmor.BodyPosition Layer->ArmorBodyType map)
  - base resists    (BasePhysical/Fire/Cold/Poison/EnergyResistance getters)
  - str req         (AosStrReq for AOS/EJ; OldStrReq for the pre-AOS era)
  - armor base       (ArmorBase = pre-AOS Armor Rating contribution)
  - medable          (DefMedAllowance: All / Half / None — default None)

Layer itself is assigned at runtime from client tiledata
(BaseArmor ctor: `Layer = (Layer)ItemData.Quality;`) and is not present in
the C# source, so the body slot is derived from the class-name keyword,
which is unambiguous for the standard equipment pieces. Pieces whose slot
cannot be inferred are tagged slot="unknown" and reported.

Per-material summary rows are aggregated from the parsed chest/standard
pieces (and reconciled against the per-piece list) so the wiki can show a
"cloth -> dragon" base-resist / str-req / medable table.

Cross-references data/items.json for item_id + png and the cliloc display
name (already resolved into items.json by extract_items.py).

Output: data/armor.json  (per-material summary + per-piece list).

Usage: python3 tools/extract_armor.py
"""

import json
import os
import re
import sys
from collections import OrderedDict, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVUO = "/Users/dkkang/dev/uo/servuo"
ARMOR_DIR = os.path.join(SERVUO, "Scripts", "Items", "Equipment", "Armor")
ITEMS_PATH = os.path.join(ROOT, "data", "items.json")
OUT_PATH = os.path.join(ROOT, "data", "armor.json")

# ArmorMaterialType.Plate is the BaseShield default (BaseShield.cs).
SHIELD_DEFAULT_MATERIAL = "Plate"

# class-name keyword -> body slot. Order matters (longest/most specific
# first). Mirrors BaseArmor.BodyPosition (Layer -> ArmorBodyType).
SLOT_KEYWORDS = [
    ("Shield", "shield"),
    ("Buckler", "shield"),
    # neck / gorget
    ("Gorget", "gorget"),
    ("Collar", "gorget"),
    ("Mempo", "gorget"),     # face guard, worn in neck slot
    # head
    ("Helm", "helm"), ("Helmet", "helm"), ("Cap", "helm"),
    ("Hood", "helm"), ("Cowl", "helm"), ("Circlet", "helm"),
    ("Kabuto", "helm"), ("Jingasa", "helm"), ("Hatsuburi", "helm"),
    ("Bascinet", "helm"), ("Coif", "helm"),
    # hands
    ("Gloves", "gloves"), ("Mitts", "gloves"),
    # arms
    ("Arms", "arms"), ("Sode", "arms"), ("Pauldrons", "arms"),
    ("WingArmor", "arms"), ("Sleeves", "arms"),
    # legs
    ("Legs", "legs"), ("Kilt", "legs"), ("Skirt", "legs"),
    ("Pants", "legs"), ("Haidate", "legs"), ("Suneate", "legs"),
    ("Shorts", "legs"), ("Tonlet", "legs"), ("Do", "legs"),
    # torso
    ("Chest", "chest"), ("Bustier", "chest"), ("Tunic", "chest"),
    ("Jacket", "chest"), ("ArmsArmor", "arms"),
]

# A friendlier ordering for materials cloth -> dragon/exotic.
MATERIAL_ORDER = [
    "Cloth", "Leather", "Spined", "Horned", "Barbed", "Studded",
    "Bone", "Ringmail", "Chainmail", "Plate", "Dragon", "Wood", "Stone",
]

INT_GETTER_NAMES = {
    "BasePhysicalResistance": "phys",
    "BaseFireResistance": "fire",
    "BaseColdResistance": "cold",
    "BasePoisonResistance": "poison",
    "BaseEnergyResistance": "energy",
    "AosStrReq": "aos_str_req",
    "OldStrReq": "old_str_req",
    "ArmorBase": "armor_base",
    "InitMinHits": "init_min_hits",
    "InitMaxHits": "init_max_hits",
}


def find_classes(src, path):
    """Yield (class_name, parent_name, body_text) for every class in a file."""
    out = []
    # match: public ... class Name : Parent[, IFoo] {  ... balanced ... }
    for m in re.finditer(
        r"public\s+(?:sealed\s+|abstract\s+)?class\s+(\w+)\s*:\s*([\w]+)",
        src,
    ):
        name = m.group(1)
        parent = m.group(2)
        # find the opening brace after the match, then balance braces
        i = src.find("{", m.end())
        if i < 0:
            continue
        depth = 0
        j = i
        while j < len(src):
            c = src[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        body = src[i + 1 : j]
        out.append((name, parent, body))
    return out


def parse_int_getter(body, prop):
    """Return int value of `public override int <prop> { get { return N; } }`.

    Handles both single-line and multi-line block forms. Only matches a
    literal integer return; computed values are skipped (None)."""
    # single-line: { get { return 5; } }
    pat = (
        r"public\s+override\s+int\s+" + re.escape(prop)
        + r"\s*\{\s*get\s*\{\s*return\s+(-?\d+)\s*;\s*\}\s*\}"
    )
    m = re.search(pat, body)
    if m:
        return int(m.group(1))
    # multi-line block form
    pat2 = (
        r"public\s+override\s+int\s+" + re.escape(prop)
        + r"\s*\{\s*get\s*\{\s*return\s+(-?\d+)\s*;"
    )
    m = re.search(pat2, body)
    if m:
        return int(m.group(1))
    return None


def parse_material(body):
    m = re.search(
        r"ArmorMaterialType\s+MaterialType\s*\{[^}]*?ArmorMaterialType\.(\w+)",
        body,
        re.S,
    )
    if m:
        return m.group(1)
    # single-line { get { return ArmorMaterialType.X; } }
    m = re.search(r"MaterialType\s*\{[^}]*?ArmorMaterialType\.(\w+)", body, re.S)
    if m:
        return m.group(1)
    return None


def parse_medable(body):
    m = re.search(
        r"DefMedAllowance\s*\{[^}]*?ArmorMeditationAllowance\.(\w+)", body, re.S
    )
    if m:
        return m.group(1)
    return None


def slot_for(name):
    for kw, slot in SLOT_KEYWORDS:
        if kw in name:
            return slot
    return "unknown"


def main():
    files = sorted(
        f for f in os.listdir(ARMOR_DIR) if f.endswith(".cs")
    )

    # First pass: parse every class in every file into a record.
    records = {}  # class_name -> dict
    for fn in files:
        path = os.path.join(ARMOR_DIR, fn)
        with open(path, encoding="utf-8", errors="replace") as fh:
            src = fh.read()
        for name, parent, body in find_classes(src, path):
            rec = {
                "class": name,
                "parent": parent,
                "source": os.path.relpath(path, SERVUO),
                "_fields": {},
                "material": parse_material(body),
                "medable_raw": parse_medable(body),
            }
            for prop, key in INT_GETTER_NAMES.items():
                v = parse_int_getter(body, prop)
                if v is not None:
                    rec["_fields"][key] = v
            records[name] = rec

    def resolve(name, key, seen=None):
        """Walk the parent chain to resolve an inherited field value."""
        if seen is None:
            seen = set()
        if name in seen or name not in records:
            return None
        seen.add(name)
        rec = records[name]
        if key in rec["_fields"]:
            return rec["_fields"][key]
        return resolve(rec["parent"], key, seen)

    def resolve_material(name, seen=None):
        if seen is None:
            seen = set()
        if name in seen or name not in records:
            return None
        seen.add(name)
        rec = records[name]
        if rec["material"]:
            return rec["material"]
        # shields: BaseShield default is Plate
        if rec["parent"] == "BaseShield":
            return SHIELD_DEFAULT_MATERIAL
        return resolve_material(rec["parent"], seen)

    def resolve_medable(name, seen=None):
        if seen is None:
            seen = set()
        if name in seen or name not in records:
            return None
        seen.add(name)
        rec = records[name]
        if rec["medable_raw"]:
            return rec["medable_raw"]
        return resolve_medable(rec["parent"], seen)

    def is_shield(name, seen=None):
        if seen is None:
            seen = set()
        if name in seen or name not in records:
            return name in ("BaseShield",)
        seen.add(name)
        rec = records[name]
        if rec["parent"] == "BaseShield":
            return True
        return is_shield(rec["parent"], seen)

    # Only concrete pieces: skip the abstract Base* classes.
    ABSTRACT = {"BaseArmor", "BaseShield"}

    def derives_from_armor(name, seen=None):
        """True iff the class chain reaches BaseArmor/BaseShield. Excludes
        BaseHat/belt items (AssassinsCowl, MagesHood, Crimson*Belt) that
        merely live in the Armor directory."""
        if seen is None:
            seen = set()
        if name in ("BaseArmor", "BaseShield"):
            return True
        if name in seen or name not in records:
            return False
        seen.add(name)
        return derives_from_armor(records[name]["parent"], seen)

    # Cross-reference items.json for id/png/name.
    with open(ITEMS_PATH, encoding="utf-8") as fh:
        items = json.load(fh)["items"]
    by_class = {}
    for it in items:
        by_class.setdefault(it["class"], it)

    pieces = []
    unknown_slot = []
    missing_item = []
    for name in sorted(records):
        if name in ABSTRACT:
            continue
        if not derives_from_armor(name):
            continue
        rec = records[name]
        material = resolve_material(name)
        shield = is_shield(name)
        slot = "shield" if shield else slot_for(name)
        if slot == "unknown":
            unknown_slot.append(name)
        med = resolve_medable(name) or "None"
        aos_str = resolve(name, "aos_str_req")
        old_str = resolve(name, "old_str_req")
        resists = {
            k: resolve(name, k)
            for k in ("phys", "fire", "cold", "poison", "energy")
        }
        it = by_class.get(name)
        if not it:
            missing_item.append(name)
        piece = OrderedDict()
        piece["class"] = name
        piece["name"] = it["name"] if it else None
        piece["item_id"] = it["item_id"] if it else None
        piece["png"] = it["png"] if it else None
        piece["material"] = material
        piece["slot"] = slot
        piece["is_shield"] = shield
        piece["base_resist"] = resists
        piece["str_req_aos"] = aos_str
        piece["str_req_old"] = old_str
        piece["armor_base"] = resolve(name, "armor_base")
        piece["medable"] = med
        piece["source"] = rec["source"]
        pieces.append(piece)

    # ---- per-material summary ----------------------------------------
    # Aggregate base-resist / str-req / medable per material. We report the
    # range across pieces (min..max) and the representative chest piece
    # (the canonical "armor rating" reference for that material).
    mat_groups = defaultdict(list)
    for p in pieces:
        if p["material"]:
            mat_groups[p["material"]].append(p)

    summary = []
    ordered_mats = [m for m in MATERIAL_ORDER if m in mat_groups]
    ordered_mats += [m for m in mat_groups if m not in MATERIAL_ORDER]
    for mat in ordered_mats:
        group = mat_groups[mat]
        non_shield = [p for p in group if not p["is_shield"]]
        ref_pool = non_shield or group
        # canonical chest reference: prefer the plain "<Material>Chest"
        # piece over Female/Gargish/Hide/exotic variants so the summary
        # row reflects the baseline material, not a reskin.
        VARIANT = (
            "Female", "Gargish", "Hide", "Tiger", "Leaf",
            "DragonTurtle", "Ninja",
        )
        chests = [p for p in ref_pool if p["slot"] == "chest"]
        plain_chests = [
            p for p in chests if not any(v in p["class"] for v in VARIANT)
        ]
        chest = (plain_chests or chests or [None])[0]
        rep = chest or ref_pool[0]

        def rng(key):
            vals = [
                p["base_resist"][key]
                for p in ref_pool
                if p["base_resist"][key] is not None
            ]
            if not vals:
                return None
            return [min(vals), max(vals)]

        def srng(field):
            vals = [p[field] for p in ref_pool if p[field] is not None]
            if not vals:
                return None
            return [min(vals), max(vals)]

        meds = sorted({p["medable"] for p in ref_pool})
        row = OrderedDict()
        row["material"] = mat
        row["piece_count"] = len(group)
        row["chest_resist"] = chest["base_resist"] if chest else None
        row["chest_str_req_aos"] = chest["str_req_aos"] if chest else None
        row["chest_armor_base"] = chest["armor_base"] if chest else None
        row["resist_range"] = {
            k: rng(k) for k in ("phys", "fire", "cold", "poison", "energy")
        }
        row["str_req_aos_range"] = srng("str_req_aos")
        row["armor_base_range"] = srng("armor_base")
        row["medable"] = meds[0] if len(meds) == 1 else meds
        row["representative_piece"] = rep["class"]
        summary.append(row)

    out = OrderedDict()
    out["_schema"] = (
        "Armor reference extracted from ServUO "
        "Scripts/Items/Equipment/Armor. 'materials' is a per-ArmorMaterialType "
        "summary (base resist range, chest reference, str req, medable). "
        "'pieces' is one row per concrete armor/shield class with base "
        "Physical/Fire/Cold/Poison/Energy resistances (AOS/EJ), AOS and "
        "pre-AOS Strength requirement, ArmorBase (pre-AOS Armor Rating), the "
        "body slot, material, and meditation allowance (All/Half/None). "
        "item_id/png/name cross-referenced from items.json. Resists/str-req "
        "are the AOS-era values defined per class in source; runtime values "
        "add resource (ore/leather) and quality bonuses."
    )
    out["_meta"] = {
        "piece_count": len(pieces),
        "shield_count": sum(1 for p in pieces if p["is_shield"]),
        "material_count": len(summary),
        "unknown_slot_count": len(unknown_slot),
        "unknown_slot": sorted(unknown_slot),
        "missing_item_xref_count": len(missing_item),
        "missing_item_xref": sorted(missing_item),
        "armor_scalars": [0.07, 0.07, 0.14, 0.15, 0.22, 0.35],
        "armor_scalar_order": "Gorget, Gloves, Helmet, Arms, Legs, Chest",
        "source": "servuo Scripts/Items/Equipment/Armor",
    }
    out["materials"] = summary
    out["pieces"] = pieces

    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
        fh.write("\n")

    # ---- coverage report ---------------------------------------------
    print("armor.json written:", os.path.relpath(OUT_PATH, ROOT))
    print("  pieces:", len(pieces), "  shields:", out["_meta"]["shield_count"])
    print("  materials:", len(summary))
    for row in summary:
        cr = row["chest_resist"]
        crs = (
            "p{phys} f{fire} c{cold} po{poison} e{energy}".format(**cr)
            if cr
            else "(no chest piece)"
        )
        print(
            "    {:9s} n={:<3d} chest[{}] str={} ar={} med={}".format(
                row["material"],
                row["piece_count"],
                crs,
                row["chest_str_req_aos"],
                row["chest_armor_base"],
                row["medable"],
            )
        )
    if unknown_slot:
        print("  unknown slot ({}):".format(len(unknown_slot)), ", ".join(sorted(unknown_slot)))
    if missing_item:
        print(
            "  no items.json xref ({}):".format(len(missing_item)),
            ", ".join(sorted(missing_item)),
        )


if __name__ == "__main__":
    main()
