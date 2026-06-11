#!/usr/bin/env python3
"""Extract creature data from ServUO mobile scripts into data/creatures.json.

Walks ../servuo/Scripts/Mobiles recursively, finds non-abstract classes that
(transitively) extend BaseCreature, and regex-parses their [Constructable]
constructors for combat stats, resistances, skills, taming info, and loot.

Usage: python3 tools/extract_creatures.py
Stdlib only (Python 3.8+).
"""

import json
import os
import re
import sys
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVUO_ROOT = os.path.normpath(os.path.join(REPO_ROOT, "..", "servuo"))
MOBILES_DIR = os.path.join(SERVUO_ROOT, "Scripts", "Mobiles")
SCRIPTS_DIR = os.path.join(SERVUO_ROOT, "Scripts")
OUT_PATH = os.path.join(REPO_ROOT, "data", "creatures.json")

CLASS_DECL_RE = re.compile(
    r"^\s*(?:public\s+|internal\s+|sealed\s+)*(?P<abstract>abstract\s+)?"
    r"(?:public\s+|internal\s+|sealed\s+|partial\s+)*class\s+(?P<name>\w+)\s*"
    r"(?::\s*(?P<bases>[\w.,<>\s]+?))?\s*(?:where\s+[\w\s:,.]+)?\{",
    re.MULTILINE,
)

# NPC-ish subtrees we never want in a bestiary even though they extend BaseCreature.
DENY_BASES = {
    "BaseVendor", "BaseQuester", "BaseEscortable", "BaseConvo", "BaseHire",
    "BaseGuard", "BaseShieldGuard", "BaseFactionGuard", "BaseFactionVendor",
    "PlayerMobile", "BaseHealer", "BaseGuildmaster",
}

NUM_RE = r"(-?(?:0x[0-9A-Fa-f]+|\d+(?:\.\d+)?))"


def to_num(tok):
    tok = tok.strip()
    if tok.lower().startswith("0x") or tok.lower().startswith("-0x"):
        return int(tok, 16)
    return float(tok) if "." in tok else int(tok)


def num_or_range(m1, m2):
    a = to_num(m1)
    if m2 is None:
        return a
    return [a, to_num(m2)]


def find_block(text, open_brace_idx):
    """Return the substring inside the braces starting at open_brace_idx ('{')."""
    depth = 0
    i = open_brace_idx
    n = len(text)
    while i < n:
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[open_brace_idx + 1:i]
        i += 1
    return None  # unbalanced


def strip_comments(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    text = re.sub(r"//[^\n]*", "", text)
    return text


def build_inheritance_map():
    """class name -> (first base name, is_abstract) over all of Scripts/."""
    inherit = {}
    parents = set()
    for dirpath, _dirs, files in os.walk(SCRIPTS_DIR):
        for fn in files:
            if not fn.endswith(".cs"):
                continue
            try:
                with open(os.path.join(dirpath, fn), encoding="utf-8", errors="replace") as f:
                    text = f.read()
            except OSError:
                continue
            for m in CLASS_DECL_RE.finditer(text):
                bases = m.group("bases")
                base = None
                if bases:
                    base = bases.split(",")[0].strip().split("<")[0].split(".")[-1]
                inherit.setdefault(m.group("name"), (base, bool(m.group("abstract"))))
                if base:
                    parents.add(base)
    return inherit, parents


def extends_base_creature(name, inherit, _seen=None):
    """True if class chain reaches BaseCreature without passing a denied base."""
    seen = set()
    cur = name
    while cur and cur not in seen:
        seen.add(cur)
        if cur in DENY_BASES:
            return False
        if cur == "BaseCreature":
            return True
        cur = inherit.get(cur, (None, False))[0]
    return False


def parse_constructors(class_name, body):
    """Yield (initializer_args_or_None, ctor_body) for non-Serial constructors."""
    pat = re.compile(
        r"(?:public|protected|internal)\s+" + re.escape(class_name) +
        r"\s*\((?P<params>[^)]*)\)\s*(?::\s*(?:base|this)\s*\((?P<init>[^{;]*)\))?\s*\{"
    )
    for m in pat.finditer(body):
        if "Serial" in m.group("params"):
            continue
        brace = body.index("{", m.end() - 1)
        cbody = find_block(body, brace)
        if cbody is None:
            continue
        yield m.group("init"), cbody


def extract_creature(class_name, file_text, class_body, rel_path):
    c = {"class": class_name, "source": rel_path}

    # CorpseName attribute appears before the class declaration.
    decl = re.search(r"class\s+" + re.escape(class_name) + r"\b", file_text)
    if decl:
        head = file_text[:decl.start()]
        cm = re.findall(r'\[CorpseName\(\s*"([^"]*)"\s*\)\]', head)
        if cm:
            c["corpse_name"] = cm[-1]

    ctors = list(parse_constructors(class_name, class_body))
    if not ctors:
        return None, "no parseable constructor"

    merged = "\n".join(cb for _init, cb in ctors)
    for init, _cb in ctors:
        if init and "AIType" in init:
            ai = re.search(r"AIType\.(\w+)", init)
            fm = re.search(r"FightMode\.(\w+)", init)
            if ai:
                c["ai_type"] = ai.group(1)
            if fm:
                c["fight_mode"] = fm.group(1)
            break

    nm = re.search(r'\bName\s*=\s*"([^"]*)"', merged)
    if nm:
        c["name"] = nm.group(1)
    else:
        rn = re.search(r'\bName\s*=\s*NameList\.RandomName\(\s*"([^"]+)"', merged)
        if rn:
            c["name"] = None
            c["name_list"] = rn.group(1)
        else:
            # BaseMount-style: name passed through base("a horse", ...)
            for init, _cb in ctors:
                if init:
                    sn = re.search(r'^\s*"([^"]*)"', init)
                    if sn:
                        c["name"] = sn.group(1)
                        break

    bm = re.search(r"\bBody\s*=\s*" + NUM_RE, merged)
    if bm:
        c["body"] = int(to_num(bm.group(1)))
    else:
        bl = re.search(r"\bBody\s*=\s*Utility\.RandomList\(([^)]*)\)", merged)
        if bl:
            try:
                c["body"] = [int(to_num(x)) for x in bl.group(1).split(",")]
            except ValueError:
                pass

    sm = re.search(r"\bBaseSoundID\s*=\s*" + NUM_RE, merged)
    if sm:
        c["base_sound_id"] = int(to_num(sm.group(1)))

    # Core stats: SetStr(x) or SetStr(min, max)
    for stat in ("Str", "Dex", "Int", "Hits", "Stam", "Mana"):
        m = re.search(r"\bSet" + stat + r"\(\s*" + NUM_RE + r"\s*(?:,\s*" + NUM_RE + r"\s*)?\)", merged)
        if m:
            c[stat.lower()] = num_or_range(m.group(1), m.group(2))

    m = re.search(r"\bSetDamage\(\s*" + NUM_RE + r"\s*(?:,\s*" + NUM_RE + r"\s*)?\)", merged)
    if m:
        c["damage"] = num_or_range(m.group(1), m.group(2))

    dts = {}
    for m in re.finditer(r"\bSetDamageType\(\s*ResistanceType\.(\w+)\s*,\s*(\d+)\s*\)", merged):
        dts[m.group(1)] = int(m.group(2))
    if dts:
        c["damage_types"] = dts

    res = {}
    for m in re.finditer(
            r"\bSetResistance\(\s*ResistanceType\.(\w+)\s*,\s*" + NUM_RE + r"\s*(?:,\s*" + NUM_RE + r"\s*)?\)",
            merged):
        res[m.group(1)] = num_or_range(m.group(2), m.group(3))
    if res:
        c["resistances"] = res

    skills = {}
    for m in re.finditer(
            r"\bSetSkill\(\s*SkillName\.(\w+)\s*,\s*" + NUM_RE + r"\s*(?:,\s*" + NUM_RE + r"\s*)?\)",
            merged):
        skills[m.group(1)] = num_or_range(m.group(2), m.group(3))
    if skills:
        c["skills"] = skills

    for field, key in (("Fame", "fame"), ("Karma", "karma"), ("VirtualArmor", "virtual_armor"),
                       ("ControlSlots", "control_slots")):
        m = re.search(r"\b" + field + r"\s*=\s*(-?\d+)\s*;", merged)
        if m:
            c[key] = int(m.group(1))

    if re.search(r"\bTamable\s*=\s*true", merged):
        c["tamable"] = True
        m = re.search(r"\bMinTameSkill\s*=\s*(-?[\d.]+)", merged)
        if m:
            c["min_tame_skill"] = float(m.group(1))

    # Loot
    loot = {}
    gl = re.search(r"override\s+void\s+GenerateLoot\s*\(\s*\)\s*\{", class_body)
    if gl:
        gbody = find_block(class_body, class_body.index("{", gl.end() - 1))
        if gbody:
            packs = []
            for m in re.finditer(r"\bAddLoot\(\s*LootPack\.(\w+)\s*(?:,\s*(\d+)\s*)?\)", gbody):
                packs.append({"pack": m.group(1), "count": int(m.group(2)) if m.group(2) else 1})
            if packs:
                loot["packs"] = packs
    pack_items = sorted(set(re.findall(r"\bPackItem\(\s*new\s+(\w+)\s*\(", merged)))
    if pack_items:
        loot["pack_items"] = pack_items
    pg = re.search(r"\bPackGold\(\s*(\d+)\s*(?:,\s*(\d+)\s*)?\)", merged)
    if pg:
        loot["pack_gold"] = num_or_range(pg.group(1), pg.group(2))
    if loot:
        c["loot"] = loot

    # Resource property overrides: int Meat/Hides/Feathers/Wool, HideType.
    # Matches both `=> 3;` and `{ get { return 3; } }` styles.
    for prop in ("Meat", "Hides", "Feathers", "Wool"):
        m = re.search(
            r"override\s+int\s+" + prop + r"\b(?:\s*=>\s*(\d+)|.{0,160}?return\s+(\d+)\s*;)",
            class_body, re.DOTALL)
        if m:
            c[prop.lower()] = int(m.group(1) or m.group(2))
    m = re.search(
        r"override\s+HideType\s+HideType\b(?:\s*=>\s*|.{0,160}?return\s+)HideType\.(\w+)",
        class_body, re.DOTALL)
    if m:
        c["hide_type"] = m.group(1)

    if not any(k in c for k in ("str", "hits", "damage", "skills")):
        return None, "no combat stats in constructor (likely NPC/special)"
    return c, None


SCHEMA = {
    "creatures": "list of creature objects; one per non-abstract class extending BaseCreature",
    "creature.class": "C# class name (unique key)",
    "creature.name": "display Name set in constructor; null when randomized (see name_list)",
    "creature.name_list": "NameList.RandomName() list id when the name is randomized",
    "creature.corpse_name": "from the [CorpseName] attribute",
    "creature.body": "body id (int) or list of possible ids (Utility.RandomList)",
    "creature.base_sound_id": "BaseSoundID (int)",
    "creature.ai_type / fight_mode": "from the base(AIType.X, FightMode.Y, ...) constructor call",
    "creature.str/dex/int/hits/stam/mana": "int, or [min, max] when SetX(min, max)",
    "creature.damage": "int or [min, max] from SetDamage",
    "creature.damage_types": "{ResistanceType: percent} from SetDamageType",
    "creature.resistances": "{ResistanceType: value or [min, max]} from SetResistance",
    "creature.skills": "{SkillName: value or [min, max]} from SetSkill",
    "creature.fame/karma/virtual_armor": "ints",
    "creature.tamable/min_tame_skill/control_slots": "taming info (tamable omitted when false)",
    "creature.loot.packs": "[{pack: LootPack name, count}] from AddLoot in GenerateLoot",
    "creature.loot.pack_items": "item class names from simple PackItem(new X()) calls",
    "creature.loot.pack_gold": "int or [min, max] from PackGold",
    "creature.meat/hides/feathers/wool/hide_type": "carve resource property overrides",
    "creature.source": "script path relative to the servuo root",
}


def main():
    if not os.path.isdir(MOBILES_DIR):
        sys.exit(f"ServUO mobiles dir not found: {MOBILES_DIR}")

    inherit, parents = build_inheritance_map()

    creatures = {}
    files_scanned = 0
    files_with_creatures = 0
    skipped = []           # (path, class, reason) — candidate classes that failed to parse
    skipped_base = 0       # abstract or used-as-base classes (intentionally excluded)

    for dirpath, _dirs, files in os.walk(MOBILES_DIR):
        for fn in sorted(files):
            if not fn.endswith(".cs"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, SERVUO_ROOT).replace(os.sep, "/")
            files_scanned += 1
            try:
                with open(path, encoding="utf-8", errors="replace") as f:
                    text = strip_comments(f.read())
            except OSError as e:
                skipped.append((rel, None, f"unreadable: {e}"))
                continue

            found_here = False
            for m in CLASS_DECL_RE.finditer(text):
                cname = m.group("name")
                if not extends_base_creature(cname, inherit):
                    continue
                # Skip abstract classes and Base* infrastructure classes used as
                # parents (concrete creatures like Orc that happen to be
                # subclassed are still real spawns and stay in).
                if m.group("abstract") or (cname in parents and (
                        cname.startswith("Base") or cname == "TalkingBaseCreature")):
                    skipped_base += 1
                    continue
                if cname in creatures:  # duplicate class name; keep first occurrence
                    continue
                body = find_block(text, text.index("{", m.end() - 1))
                if body is None:
                    skipped.append((rel, cname, "unbalanced braces"))
                    continue
                creature, err = extract_creature(cname, text, body, rel)
                if err:
                    skipped.append((rel, cname, err))
                    continue
                creatures[cname] = creature
                found_here = True
            if found_here:
                files_with_creatures += 1

    out = {
        "_schema": SCHEMA,
        "_meta": {
            "generator": "tools/extract_creatures.py",
            "extracted": date.today().isoformat(),
            "servuo_root": "../servuo",
            "mobiles_dir": "Scripts/Mobiles",
            "files_scanned": files_scanned,
            "files_with_creatures": files_with_creatures,
            "creature_count": len(creatures),
            "skipped_class_count": len(skipped),
            "skipped_base_or_abstract_count": skipped_base,
            "skipped": [{"source": s, "class": cls, "reason": r} for s, cls, r in skipped],
        },
        "creatures": sorted(creatures.values(), key=lambda c: c["class"]),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"scanned {files_scanned} files; extracted {len(creatures)} creatures "
          f"from {files_with_creatures} files")
    print(f"skipped {len(skipped)} candidate classes (parse/NPC), "
          f"{skipped_base} abstract/base classes")
    print(f"wrote {os.path.relpath(OUT_PATH, REPO_ROOT)}")


if __name__ == "__main__":
    main()
