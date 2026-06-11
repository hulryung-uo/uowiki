#!/usr/bin/env python3
"""Extract crafting recipes from ServUO craft system definitions.

Parses Scripts/Services/Craft/Def*.cs AddCraft(...) calls (plus the
AddRes/AddSkill follow-ups that attach to the returned index) and resolves
cliloc numbers via anima/data/cliloc.json. Writes data/recipes.json.

The shard expansion is EJ (servuo/Config/Expansion.cfg), so every
`Core.X` conditional gate in the Def files is true: all recipes are
included, and `Core.X ? typeof(A) : typeof(B)` ternaries resolve to A.

DefInscription adds most of its recipes through private helpers
(AddSpell / AddNecroSpell / AddMysticSpell); those helpers' semantics are
mirrored here so spell scrolls are extracted too.

Usage: python3 tools/extract_crafting.py
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRAFT_DIR = os.path.normpath(os.path.join(ROOT, "..", "servuo", "Scripts", "Services", "Craft"))
CLILOC_PATH = os.path.normpath(os.path.join(ROOT, "..", "anima", "data", "cliloc.json"))
OUT_PATH = os.path.join(ROOT, "data", "recipes.json")

DEF_FILES = [
    "DefAlchemy.cs",
    "DefBlacksmithy.cs",
    "DefBowFletching.cs",
    "DefCarpentry.cs",
    "DefCartography.cs",
    "DefCooking.cs",
    "DefGlassblowing.cs",
    "DefInscription.cs",
    "DefMasonry.cs",
    "DefTailoring.cs",
    "DefTinkering.cs",
]

# ---------------------------------------------------------------- cliloc ----

with open(CLILOC_PATH, encoding="utf-8") as f:
    CLILOC = json.load(f)

unresolved_clilocs = set()


def resolve_cliloc(num):
    s = CLILOC.get(str(num))
    if s is None:
        unresolved_clilocs.add(num)
        return "cliloc:%d" % num
    return s.strip()


# ------------------------------------------------------------- C# parsing ---

def strip_comments(text):
    """Remove // and /* */ comments, respecting string/char literals."""
    out = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            out.append(text[i:j + 1])
            i = j + 1
        elif c == "'":
            j = i + 1
            while j < n and text[j] != "'":
                j += 2 if text[j] == "\\" else 1
            out.append(text[i:j + 1])
            i = j + 1
        elif text.startswith("//", i):
            j = text.find("\n", i)
            i = n if j == -1 else j
        elif text.startswith("/*", i):
            j = text.find("*/", i + 2)
            i = n if j == -1 else j + 2
        else:
            out.append(c)
            i += 1
    return "".join(out)


def method_body(text, signature_re):
    """Return the balanced-brace body of the first method matching signature_re."""
    m = re.search(signature_re, text)
    if not m:
        return None
    i = text.index("{", m.end())
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1:j]
    return None


def balanced_args(text, open_paren):
    """Given index of '(' return (raw_args_string, index_after_close)."""
    depth = 0
    in_str = False
    for j in range(open_paren, len(text)):
        c = text[j]
        if in_str:
            if c == "\\":
                continue
            if c == '"':
                in_str = False
        elif c == '"':
            in_str = True
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return text[open_paren + 1:j], j + 1
    return None, len(text)


def split_args(s):
    args, depth, in_str, cur = [], 0, False, []
    for c in s:
        if in_str:
            cur.append(c)
            if c == '"':
                in_str = False
        elif c == '"':
            in_str = True
            cur.append(c)
        elif c in "(<[":
            depth += 1
            cur.append(c)
        elif c in ")>]":
            depth -= 1
            cur.append(c)
        elif c == "," and depth == 0:
            args.append("".join(cur).strip())
            cur = []
        else:
            cur.append(c)
    if cur:
        args.append("".join(cur).strip())
    return args


def parse_typeof(arg):
    """typeof(X) or `Core.X ? typeof(A) : typeof(B)` -> simple type name."""
    m = re.search(r"typeof\s*\(\s*([\w.]+)\s*\)", arg)
    if not m:
        return None
    return m.group(1).split(".")[-1]


def parse_textdef(arg):
    """TextDefinition arg -> (display_string, ok). Handles cliloc ints,
    int+int arithmetic, and string literals."""
    arg = arg.strip()
    m = re.fullmatch(r'"((?:[^"\\]|\\.)*)"', arg)
    if m:
        return m.group(1), True
    if re.fullmatch(r"\d+", arg):
        return resolve_cliloc(int(arg)), True
    if re.fullmatch(r"\d+(\s*\+\s*\d+)+", arg):
        return resolve_cliloc(sum(int(x) for x in re.findall(r"\d+", arg))), True
    return arg, False


def resolve_ternary(arg):
    """`Core.X ? a : b` -> a (expansion is EJ, so all Core.X are true)."""
    m = re.fullmatch(r"Core\.\w+\s*\?\s*(.+?)\s*:\s*(.+)", arg.strip())
    return m.group(1) if m else arg.strip()


def parse_num(arg):
    try:
        return float(resolve_ternary(arg))
    except ValueError:
        return None


def parse_int(arg):
    try:
        return int(resolve_ternary(arg))
    except ValueError:
        return None


# --------------------------------------------------- inscription helpers ----

REG_ENUM = [
    "BlackPearl", "Bloodmoss", "Garlic", "Ginseng", "MandrakeRoot",
    "Nightshade", "SulfurousAsh", "SpidersSilk", "BatWing", "GraveDust",
    "DaemonBlood", "NoxCrystal", "PigIron", "Bone", "DragonBlood",
    "FertileDirt", "DaemonBone",
]

# GetRegLocalization() in DefInscription.cs
NECRO_REG_CLILOC = {
    "BatWing": 1023960, "GraveDust": 1023983, "DaemonBlood": 1023965,
    "NoxCrystal": 1023982, "PigIron": 1023978, "Bone": 1023966,
    "DragonBlood": 1023970, "FertileDirt": 1023969, "DaemonBone": 1023968,
}

# ------------------------------------------------------ tinkering helper ----

# GemType enum (Scripts/Items/Equipment/Jewelry/BaseJewel.cs); None = 0
GEM_TYPE = ["None", "StarSapphire", "Emerald", "Sapphire", "Ruby", "Citrine",
            "Amethyst", "Tourmaline", "Amber", "Diamond"]

# DefTinkering.AddJewelrySet(): (item class, name cliloc base, ingot amount)
JEWELRY_SET = [
    ("GoldRing", 1044176, 2),
    ("SilverBeadNecklace", 1044185, 2),
    ("GoldNecklace", 1044194, 2),
    ("GoldEarrings", 1044203, 2),
    ("GoldBeadNecklace", 1044212, 2),
    ("GoldBracelet", 1044221, 2),
]

# AddSpell() switch(m_Circle): (minSkill, maxSkill, group cliloc)
SPELL_CIRCLE = {
    0: (-25.0, 25.0, 1111691), 1: (-10.8, 39.2, 1111691),
    2: (3.5, 53.5, 1111692), 3: (17.8, 67.8, 1111692),
    4: (32.1, 82.1, 1111693), 5: (46.4, 96.4, 1111693),
    6: (60.7, 110.7, 1111694), 7: (75.0, 125.0, 1111694),
}


def reg_resource(reg_name, necro_loc=False):
    idx = REG_ENUM.index(reg_name)
    if necro_loc:
        cliloc = NECRO_REG_CLILOC.get(reg_name, 1044353 + idx)
    else:
        cliloc = 1044353 + idx
    return {"type": reg_name, "name": resolve_cliloc(cliloc), "amount": 1}


def parse_regs(args):
    regs = []
    for a in args:
        m = re.fullmatch(r"Reg\.(\w+)", a.strip())
        if m:
            regs.append(m.group(1))
    return regs


# ----------------------------------------------------------- extraction -----

CALL_RE = re.compile(
    r"\b(AddCraft|AddRes|AddSkill|AddSpell|AddNecroSpell|AddMysticSpell"
    r"|AddJewelrySet)\s*\("
)
CIRCLE_RE = re.compile(r"m_Circle\s*=\s*(\d+)\s*;")


def extract_file(path):
    with open(path, encoding="utf-8") as f:
        text = strip_comments(f.read())

    msk = re.search(r"MainSkill[^;{]*\{[^}]*SkillName\.(\w+)", text)
    main_skill = msk.group(1) if msk else None

    body = method_body(text, r"public\s+override\s+void\s+InitCraftList\s*\(\s*\)")
    if body is None:
        return main_skill, [], [{"reason": "no InitCraftList body"}]

    recipes = []
    skipped = []
    current = None  # most recent successfully parsed recipe (AddRes target)
    spell_index = 0  # DefInscription m_Index
    circle = 0       # DefInscription m_Circle

    # interleave m_Circle assignments with calls, in source order
    events = []
    for m in CALL_RE.finditer(body):
        events.append((m.start(), "call", m))
    for m in CIRCLE_RE.finditer(body):
        events.append((m.start(), "circle", m))
    events.sort(key=lambda e: e[0])

    for _, kind, m in events:
        if kind == "circle":
            circle = int(m.group(1))
            continue

        name = m.group(1)
        raw, _end = balanced_args(body, m.end() - 1)
        if raw is None:
            skipped.append({"call": name, "reason": "unbalanced parens"})
            continue
        args = split_args(raw)
        line = body.count("\n", 0, m.start()) + 1  # body-relative, for reports

        if name == "AddCraft":
            item_type = parse_typeof(args[0])
            group, g_ok = parse_textdef(args[1])
            iname, n_ok = parse_textdef(args[2])
            if args[3].startswith("SkillName."):
                craft_skill = args[3].split(".")[1]
                rest = args[4:]
            else:
                craft_skill = None
                rest = args[3:]
            if item_type is None or len(rest) < 5:
                skipped.append({"call": name, "args": raw.strip()[:120],
                                "reason": "unparseable item type/arity"})
                current = None
                continue
            min_s, max_s = parse_num(rest[0]), parse_num(rest[1])
            res_type = parse_typeof(rest[2])
            res_name, _ = parse_textdef(rest[3])
            amount = parse_int(rest[4])
            if None in (min_s, max_s, res_type, amount) or not (g_ok and n_ok):
                skipped.append({"call": name, "args": raw.strip()[:120],
                                "reason": "non-literal arguments"})
                current = None
                continue
            current = {
                "item_type": item_type,
                "name": iname,
                "category": group,
                "min_skill": min_s,
                "max_skill": max_s,
                "resources": [
                    {"type": res_type, "name": res_name, "amount": amount}
                ],
                "skills": [],
            }
            if craft_skill:
                current["craft_skill"] = craft_skill
            recipes.append(current)

        elif name == "AddRes":
            if current is None:
                skipped.append({"call": name, "args": raw.strip()[:120],
                                "reason": "no preceding AddCraft"})
                continue
            res_type = parse_typeof(args[1])
            res_name, _ = parse_textdef(args[2])
            amount = parse_int(args[3])
            if res_type is None or amount is None:
                skipped.append({"call": name, "args": raw.strip()[:120],
                                "reason": "non-literal resource"})
                continue
            current["resources"].append(
                {"type": res_type, "name": res_name, "amount": amount})

        elif name == "AddSkill":
            if current is None:
                continue
            sk = re.search(r"SkillName\.(\w+)", args[1])
            lo, hi = parse_num(args[2]), parse_num(args[3])
            if sk and lo is not None and hi is not None:
                current["skills"].append(
                    {"skill": sk.group(1), "min": lo, "max": hi})

        elif name == "AddSpell":
            item_type = parse_typeof(args[0])
            regs = parse_regs(args[1:])
            lo, hi, group_cl = SPELL_CIRCLE[circle]
            current = {
                "item_type": item_type,
                "name": resolve_cliloc(1044381 + spell_index),
                "category": resolve_cliloc(group_cl),
                "min_skill": lo,
                "max_skill": hi,
                "resources": [reg_resource(r) for r in regs]
                + [{"type": "BlankScroll",
                    "name": resolve_cliloc(1044377), "amount": 1}],
                "skills": [],
            }
            spell_index += 1
            recipes.append(current)

        elif name == "AddJewelrySet":
            # DefTinkering helper: 6 jewelry pieces per gem type
            gm = re.search(r"GemType\.(\w+)", args[0])
            gem_item = parse_typeof(args[1])
            if not gm or gem_item is None or gm.group(1) not in GEM_TYPE:
                skipped.append({"call": name, "args": raw.strip()[:120],
                                "reason": "unparseable gem type"})
                continue
            offset = GEM_TYPE.index(gm.group(1)) - 1
            for cls, name_base, ingots in JEWELRY_SET:
                current = {
                    "item_type": cls,
                    "name": resolve_cliloc(name_base + offset),
                    "category": resolve_cliloc(1044049),
                    "min_skill": 40.0,
                    "max_skill": 90.0,
                    "resources": [
                        {"type": "IronIngot",
                         "name": resolve_cliloc(1044036), "amount": ingots},
                        {"type": gem_item,
                         "name": resolve_cliloc(1044231 + offset), "amount": 1},
                    ],
                    "skills": [],
                }
                recipes.append(current)

        elif name in ("AddNecroSpell", "AddMysticSpell"):
            item_type = parse_typeof(args[3])
            regs = parse_regs(args[4:])
            lo = parse_num(args[2])
            if name == "AddNecroSpell":
                spell_no = parse_int(args[0])
                iname = resolve_cliloc(1060509 + spell_no)
                group = resolve_cliloc(1061677)
            else:
                iname = resolve_cliloc(int(args[0]))
                group = resolve_cliloc(1111671)
            current = {
                "item_type": item_type,
                "name": iname,
                "category": group,
                "min_skill": lo,
                "max_skill": round(lo + 1.0, 1),
                "resources": [reg_resource(r, necro_loc=True) for r in regs]
                + [{"type": "BlankScroll",
                    "name": resolve_cliloc(1044377), "amount": 1}],
                "skills": [],
            }
            recipes.append(current)

    return main_skill, recipes, skipped


def main():
    out = {
        "_schema": {
            "description": "Crafting recipes extracted from ServUO craft "
                           "system Def*.cs files. Keyed by craft system slug.",
            "extracted_by": "tools/extract_crafting.py",
            "source_dir": "servuo: Scripts/Services/Craft/",
            "cliloc_source": "anima/data/cliloc.json",
            "expansion": "EJ (all Core.X gates enabled)",
            "system_fields": {
                "system": "display name",
                "main_skill": "ServUO SkillName of the craft system",
                "source": "servuo path of the Def file",
                "recipes": "list of recipe objects",
                "skipped": "AddCraft/AddRes calls that could not be parsed",
            },
            "recipe_fields": {
                "item_type": "C# item class name",
                "name": "resolved item display name",
                "category": "resolved craft gump category",
                "min_skill": "skill at 0% success chance (can be negative)",
                "max_skill": "skill at 100% success chance",
                "resources": "[{type, name, amount}] consumed materials",
                "skills": "[{skill, min, max}] extra skill requirements",
                "craft_skill": "(optional) overrides main_skill for this item",
            },
        }
    }

    total = 0
    for fn in DEF_FILES:
        path = os.path.join(CRAFT_DIR, fn)
        if not os.path.exists(path):
            print("missing: %s (skipping file)" % fn, file=sys.stderr)
            continue
        slug = fn[3:-3].lower()  # DefBowFletching.cs -> bowfletching
        main_skill, recipes, skipped = extract_file(path)
        out[slug] = {
            "system": re.sub(r"(?<=[a-z])(?=[A-Z])", " ", fn[3:-3]),
            "main_skill": main_skill,
            "source": "Scripts/Services/Craft/" + fn,
            "recipes": recipes,
            "skipped": skipped,
        }
        total += len(recipes)
        print("%-16s %4d recipes, %d skipped" % (slug, len(recipes), len(skipped)))

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print("\ntotal: %d recipes -> %s" % (total, os.path.relpath(OUT_PATH, ROOT)))
    if unresolved_clilocs:
        print("unresolved clilocs (%d): %s" % (
            len(unresolved_clilocs),
            ", ".join(str(c) for c in sorted(unresolved_clilocs))))
    else:
        print("unresolved clilocs: 0")


if __name__ == "__main__":
    main()
