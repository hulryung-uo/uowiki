#!/usr/bin/env python3
"""Extract weapon stats from ServUO into data/weapons.json.

Parses Scripts/Items/Equipment/Weapons/*.cs for each concrete weapon class and
captures the AOS-era stats our shard (EJ) uses: damage range, swing speed, the
governing combat skill (from the base class), one- vs two-handed layer, strength
requirement, and the primary/secondary special move (WeaponAbility).

Sources:
  - servuo: Scripts/Items/Equipment/Weapons/*.cs   (stats, abilities, base chain)
  - uo-resource/tiledata.mul                         (default Layer / hands)
  - uowiki/data/items.json                           (item_id, png icon)
  - anima/data/cliloc.json                           (display names)

Stdlib only. Run: python3 tools/extract_weapons.py
"""

import json
import os
import re
import struct
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(HERE)
ROOT = os.path.dirname(WIKI)

WEAPON_DIR = os.path.join(ROOT, "servuo", "Scripts", "Items", "Equipment", "Weapons")
TILEDATA = os.path.join(ROOT, "uo-resource", "tiledata.mul")
ITEMS_JSON = os.path.join(WIKI, "data", "items.json")
CLILOC_JSON = os.path.join(ROOT, "anima", "data", "cliloc.json")
OUT_JSON = os.path.join(WIKI, "data", "weapons.json")

# ---------------------------------------------------------------------------
# Base class -> combat skill. Derived from the DefSkill override in each
# Base*.cs (verified by reading the source). BaseThrown inherits Archery in the
# C# Skill getter, but throwing weapons are governed in practice by the Throwing
# skill (parry/swing math and the OPL "skill required: throwing"), so we map the
# whole thrown line to Throwing for documentation purposes.
# ---------------------------------------------------------------------------
SKILL_BY_BASE = {
    "BaseSword": "Swordsmanship",
    "BaseAxe": "Swordsmanship",
    "BasePoleArm": "Swordsmanship",
    "BaseBashing": "Mace Fighting",
    "BaseStaff": "Mace Fighting",
    "BaseWand": "Mace Fighting",
    "BaseKnife": "Fencing",
    "BaseSpear": "Fencing",
    "BaseRanged": "Archery",
    "BaseThrown": "Throwing",
}

# SkillName enum value -> friendly skill name used on the wiki. Some concrete
# weapons override DefSkill so their structural base class (which drives family)
# does not match the skill they train -- e.g. Kryss/Lance are BaseSword but
# train Fencing; WarAxe is a BaseAxe but trains Mace Fighting.
SKILLNAME_FRIENDLY = {
    "Swords": "Swordsmanship",
    "Macing": "Mace Fighting",
    "Fencing": "Fencing",
    "Archery": "Archery",
    "Throwing": "Throwing",
    "Wrestling": "Wrestling",
}

# Family grouping for the wiki page. Each concrete weapon is placed by walking
# its base chain to the first base that has a family here.
FAMILY_BY_BASE = {
    "BaseSword": "Swords",
    "BaseAxe": "Axes",
    "BaseBashing": "Maces & Hammers",
    "BaseStaff": "Staves",
    "BaseWand": "Wands",
    "BaseKnife": "Daggers & Knives",
    "BaseSpear": "Spears & Forks",
    "BasePoleArm": "Polearms",
    "BaseRanged": "Bows & Crossbows",
    "BaseThrown": "Thrown",
}

FAMILY_ORDER = [
    "Swords", "Axes", "Maces & Hammers", "Staves", "Daggers & Knives",
    "Spears & Forks", "Polearms", "Bows & Crossbows", "Thrown", "Wands",
]

# WeaponAbility -> human label + cliloc (from Scripts/Abilities/WeaponAbility.cs
# and the in-game special-move menu). Cliloc kept for cross-checking only.
ABILITY_LABEL = {
    "ArmorIgnore": "Armor Ignore",
    "BleedAttack": "Bleed Attack",
    "ConcussionBlow": "Concussion Blow",
    "CrushingBlow": "Crushing Blow",
    "Disarm": "Disarm",
    "Dismount": "Dismount",
    "DoubleStrike": "Double Strike",
    "InfectiousStrike": "Infectious Strike",
    "MortalStrike": "Mortal Strike",
    "MovingShot": "Moving Shot",
    "ParalyzingBlow": "Paralyzing Blow",
    "ShadowStrike": "Shadow Strike",
    "WhirlwindAttack": "Whirlwind Attack",
    "RidingSwipe": "Riding Swipe",
    "FrenziedWhirlwind": "Frenzied Whirlwind",
    "Block": "Block",
    "DefenseMastery": "Defense Mastery",
    "NerveStrike": "Nerve Strike",
    "TalonStrike": "Talon Strike",
    "Feint": "Feint",
    "DualWield": "Dual Wield",
    "DoubleShot": "Double Shot",
    "ArmorPierce": "Armor Pierce",
    "Bladeweave": "Bladeweave",
    "ForceArrow": "Force Arrow",
    "LightningArrow": "Lightning Arrow",
    "PsychicAttack": "Psychic Attack",
    "SerpentArrow": "Serpent Arrow",
    "ForceOfNature": "Force of Nature",
    "InfusedThrow": "Infused Throw",
    "MysticArc": "Mystic Arc",
    "Disrobe": "Disrobe",
    "ColdWind": "Cold Wind",
}

LAYER_NAME = {1: "One-handed", 2: "Two-handed"}

# Abstract bases / non-equippable helpers to skip.
SKIP_CLASSES = {
    "NinjaWeapon", "WandTarget", "LoadEntry", "UnloadEntry",
}


# ---------------------------------------------------------------------------
def load_tiledata_layers():
    """Return {item_id_int: layer_int} from tiledata.mul (new/HS format).

    Static block: 4-byte header + 32 entries of 41 bytes.
    Entry: flags(8) weight(1) quality(1=layer) ...  -> byte 9 is the layer.
    """
    with open(TILEDATA, "rb") as f:
        data = f.read()
    land_size = 512 * (4 + 32 * 30)
    static_entry = 41
    static_block = 4 + 32 * static_entry
    layers = {}

    def layer_of(tid):
        block = tid // 32
        idx = tid % 32
        off = land_size + block * static_block + 4 + idx * static_entry
        if off + static_entry > len(data):
            return None
        return data[off + 9]

    return layer_of


def load_items_index():
    with open(ITEMS_JSON) as f:
        items = json.load(f)["items"]
    by_class = {}
    for it in items:
        by_class[it["class"]] = it
    return by_class


def load_cliloc():
    with open(CLILOC_JSON) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
def list_class_decls(text):
    """Yield (class_name, base_name) for class declarations in a file."""
    for m in re.finditer(
        r"public\s+(?:sealed\s+|abstract\s+)?class\s+(\w+)\s*:\s*(\w+)", text):
        yield m.group(1), m.group(2)


def find_int_override(text, name):
    """public override int <name> { get { ... return <int>; } }
    Return first integer-ish literal (decimal or 0x), else None."""
    m = re.search(
        r"public\s+override\s+int\s+" + re.escape(name) +
        r"\b[^{]*\{(.*?)\}\s*\}", text, re.DOTALL)
    if not m:
        # single-line getter form: => or get { return X; }
        m = re.search(
            r"public\s+override\s+int\s+" + re.escape(name) +
            r"\b[^=;{]*=>\s*([^;]+);", text)
        if not m:
            return None
        body = m.group(1)
    else:
        body = m.group(1)
    return parse_int_from_body(body)


def parse_int_from_body(body):
    # Prefer a Core.ML ternary (our shard runs ML/EJ): pick the ML-true branch.
    tern = re.search(r"Core\.ML\s*\?\s*([^:]+):\s*([^;]+)", body)
    if tern:
        ml_val = first_number(tern.group(1))
        if ml_val is not None:
            return ml_val
    return first_number(body)


def first_number(s):
    m = re.search(r"return\s+(0x[0-9A-Fa-f]+|\d+)", s)
    if not m:
        m = re.search(r"(0x[0-9A-Fa-f]+|\d+)", s)
    if not m:
        return None
    tok = m.group(1)
    try:
        return int(tok, 16) if tok.lower().startswith("0x") else int(tok)
    except ValueError:
        return None


def find_float_override(text, name):
    m = re.search(
        r"public\s+override\s+float\s+" + re.escape(name) +
        r"\b.*?return\s+([0-9.]+)f?", text, re.DOTALL)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def find_ability(text, name):
    """<name> getter -> WeaponAbility.<X>; returns 'X' or None."""
    m = re.search(
        r"public\s+override\s+WeaponAbility\s+" + re.escape(name) +
        r"\b.*?WeaponAbility\.(\w+)", text, re.DOTALL)
    return m.group(1) if m else None


def find_explicit_layer(text, class_name):
    """Layer override set inside the constructor: Layer = Layer.TwoHanded;"""
    # Look only at the body of the parameterless [Constructable] ctor.
    m = re.search(
        r"\[Constructable\][^{]*public\s+" + re.escape(class_name) +
        r"\s*\([^)]*\)[^{]*\{(.*?)\}", text, re.DOTALL)
    region = m.group(1) if m else text
    lm = re.search(r"Layer\s*=\s*Layer\.(OneHanded|TwoHanded)", region)
    if lm:
        return 1 if lm.group(1) == "OneHanded" else 2
    return None


def find_defskill(text):
    """public override SkillName DefSkill { get { return SkillName.X; } }"""
    m = re.search(
        r"public\s+override\s+SkillName\s+DefSkill\b.*?SkillName\.(\w+)",
        text, re.DOTALL)
    if m:
        return SKILLNAME_FRIENDLY.get(m.group(1), m.group(1))
    return None


def find_required_race(text):
    m = re.search(r"RequiredRace\s*\{?\s*get\s*\{?\s*return\s+Race\.(\w+)", text)
    if not m:
        m = re.search(r"RequiredRace\s*=>\s*Race\.(\w+)", text)
    return m.group(1) if m else None


def resolve_base_attr(class_to_base, file_text_by_class, leaf, getter):
    """Walk base chain collecting first non-None getter(text)."""
    cur = leaf
    seen = set()
    while cur and cur not in seen:
        seen.add(cur)
        txt = file_text_by_class.get(cur)
        if txt is not None:
            val = getter(txt)
            if val is not None:
                return val
        cur = class_to_base.get(cur)
    return None


def walk_chain(class_to_base, leaf, mapping):
    cur = leaf
    seen = set()
    while cur and cur not in seen:
        seen.add(cur)
        if cur in mapping:
            return mapping[cur], cur
        cur = class_to_base.get(cur)
    return None, None


# ---------------------------------------------------------------------------
def main():
    layer_of = load_tiledata_layers()
    items_by_class = load_items_index()
    cliloc = load_cliloc()

    # Pass 1: read every file, record class declarations + per-class source text.
    class_to_base = {}
    file_text_by_class = {}
    class_to_file = {}

    for fn in sorted(os.listdir(WEAPON_DIR)):
        if not fn.endswith(".cs"):
            continue
        path = os.path.join(WEAPON_DIR, fn)
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        decls = list(list_class_decls(text))
        for cname, base in decls:
            class_to_base[cname] = base
            class_to_file[cname] = fn
            # Store the full file text for each class declared in it (most
            # weapon files declare exactly one class). Good enough for the
            # single-class-per-file weapon scripts here.
            file_text_by_class[cname] = text

    # Determine which classes are concrete equippable weapons:
    # they must chain (eventually) to a Base* in FAMILY_BY_BASE, not be a Base*
    # themselves, not be abstract helpers, and have an item_id in items.json.
    base_names = set(FAMILY_BY_BASE) | {
        "BaseWeapon", "BaseMeleeWeapon"}

    weapons = []
    unresolved = []

    for cname in sorted(class_to_base):
        if cname in SKIP_CLASSES:
            continue
        if cname in base_names:
            continue
        if cname.startswith("Base"):
            continue
        # Must resolve to a known family via base chain.
        family, fam_base = walk_chain(class_to_base, cname, FAMILY_BY_BASE)
        if family is None:
            continue
        # Skill: a per-class DefSkill override (walking the chain) wins over the
        # base-class default, so weapons like Kryss (BaseSword -> Fencing) are
        # tagged with the skill they actually train.
        skill = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                  find_defskill)
        skill_from_base, _ = walk_chain(class_to_base, cname, SKILL_BY_BASE)
        if skill is None:
            skill = skill_from_base
        skill_differs = (skill != skill_from_base)

        text = file_text_by_class[cname]
        item = items_by_class.get(cname)
        item_id = item["item_id"] if item else None
        png = item["png"] if item else None

        # Damage / speed / str (AOS-era, our shard). Walk base chain so a
        # subclass that doesn't override falls back to its base's value.
        min_dmg = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                    lambda t: find_int_override(t, "AosMinDamage"))
        max_dmg = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                    lambda t: find_int_override(t, "AosMaxDamage"))
        speed = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                  lambda t: find_int_override(t, "AosSpeed"))
        ml_speed = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                     lambda t: find_float_override(t, "MlSpeed"))
        str_req = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                    lambda t: find_int_override(t, "AosStrengthReq"))

        # Special moves: walk chain (BaseWand defaults Dismount/Disarm).
        prim = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                 lambda t: find_ability(t, "PrimaryAbility"))
        sec = resolve_base_attr(class_to_base, file_text_by_class, cname,
                                lambda t: find_ability(t, "SecondaryAbility"))

        # Layer: an explicit constructor override (this class or an inherited
        # ctor, e.g. OrcishBow : Bow gets Bow's TwoHanded) wins; else tiledata.
        layer = None
        cur = cname
        seen = set()
        while cur and cur not in seen:
            seen.add(cur)
            ctext = file_text_by_class.get(cur)
            if ctext is not None:
                layer = find_explicit_layer(ctext, cur)
                if layer is not None:
                    break
            cur = class_to_base.get(cur)
        layer_source = "override" if layer else None
        if layer is None and item_id:
            try:
                layer = layer_of(int(item_id, 16))
                layer_source = "tiledata"
            except (TypeError, ValueError):
                layer = None
        race = find_required_race(text)

        name = item["name"] if item else humanize(cname)

        wpn = OrderedDict([
            ("class", cname),
            ("name", name),
            ("family", family),
            ("skill", skill),
            ("skill_differs_from_family", skill_differs),
            ("base", class_to_base.get(cname)),
            ("item_id", item_id),
            ("png", png),
            ("min_damage", min_dmg),
            ("max_damage", max_dmg),
            ("speed", speed),
            ("ml_speed", ml_speed),
            ("str_req", str_req),
            ("hands", LAYER_NAME.get(layer)),
            ("layer", layer),
            ("layer_source", layer_source),
            ("primary", ABILITY_LABEL.get(prim, prim)),
            ("secondary", ABILITY_LABEL.get(sec, sec)),
            ("primary_raw", prim),
            ("secondary_raw", sec),
            ("required_race", race),
            ("source", "Scripts/Items/Equipment/Weapons/" + class_to_file[cname]),
        ])
        weapons.append(wpn)

        missing = [k for k in ("min_damage", "max_damage", "speed", "str_req",
                               "primary", "secondary", "item_id", "hands")
                   if wpn[k] is None]
        if missing:
            unresolved.append((cname, missing))

    weapons.sort(key=lambda w: (FAMILY_ORDER.index(w["family"]), w["name"].lower()))

    # Per-family grouping. The family's headline skill is the structural base's
    # skill (e.g. all Swords default to Swordsmanship) -- individual members may
    # override it (skill_differs_from_family flags those).
    fam_to_base_skill = {fam: SKILL_BY_BASE[base]
                         for base, fam in FAMILY_BY_BASE.items()}
    families = OrderedDict()
    for fam in FAMILY_ORDER:
        members = [w["class"] for w in weapons if w["family"] == fam]
        exceptions = [w["class"] for w in weapons
                      if w["family"] == fam and w["skill_differs_from_family"]]
        if members:
            families[fam] = OrderedDict([
                ("skill", fam_to_base_skill[fam]),
                ("count", len(members)),
                ("skill_exceptions", exceptions),
                ("members", members),
            ])

    out = OrderedDict([
        ("_schema", OrderedDict([
            ("description",
             "Weapon stats extracted from ServUO. AOS-era values (our shard runs "
             "EJ): min/max damage, swing speed (AosSpeed integer + ML float "
             "seconds), strength requirement, governing skill, one/two-handed "
             "layer, and primary/secondary special moves (WeaponAbility)."),
            ("extracted_by", "tools/extract_weapons.py"),
            ("sources", [
                "servuo: Scripts/Items/Equipment/Weapons/*.cs",
                "servuo: Scripts/Abilities/WeaponAbility.cs",
                "uo-resource/tiledata.mul",
                "uowiki/data/items.json",
                "anima/data/cliloc.json",
            ]),
            ("fields", OrderedDict([
                ("skill", "governing combat skill (from base class)"),
                ("min_damage/max_damage", "AOS base damage range"),
                ("speed", "AosSpeed integer (higher = faster, pre-ML)"),
                ("ml_speed", "ML swing speed in seconds (lower = faster)"),
                ("str_req", "AosStrengthReq strength requirement"),
                ("hands", "One-handed or Two-handed"),
                ("layer_source", "override (ctor Layer=) or tiledata (art quality)"),
                ("primary/secondary", "special moves; raw = C# WeaponAbility name"),
            ])),
        ])),
        ("_meta", OrderedDict([
            ("weapon_count", len(weapons)),
            ("family_count", len(families)),
        ])),
        ("families", families),
        ("weapons", weapons),
    ])

    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=1)
        f.write("\n")

    # Coverage report to stderr.
    print(f"Wrote {OUT_JSON}", file=sys.stderr)
    print(f"  weapons: {len(weapons)}  families: {len(families)}", file=sys.stderr)
    for fam, info in families.items():
        print(f"    {fam:18s} {info['count']:3d}  ({info['skill']})", file=sys.stderr)
    no_id = [w["class"] for w in weapons if not w["item_id"]]
    no_dmg = [w["class"] for w in weapons if w["min_damage"] is None]
    no_layer = [w["class"] for w in weapons if w["hands"] is None]
    print(f"  missing item_id: {len(no_id)} {no_id}", file=sys.stderr)
    print(f"  missing damage:  {len(no_dmg)} {no_dmg}", file=sys.stderr)
    print(f"  missing hands:   {len(no_layer)} {no_layer}", file=sys.stderr)
    if unresolved:
        print(f"  partial ({len(unresolved)}):", file=sys.stderr)
        for cname, miss in unresolved:
            print(f"    {cname}: {miss}", file=sys.stderr)


def humanize(cname):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", cname).lower()


if __name__ == "__main__":
    main()
