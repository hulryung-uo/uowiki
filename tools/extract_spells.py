#!/usr/bin/env python3
"""Extract the 64 Magery spells from ServUO source into data/spells.json.

Reads:
  ../servuo/Scripts/Spells/{First..Eighth}/*.cs   — SpellInfo registrations
  ../servuo/Scripts/Spells/Base/MagerySpell.cs    — per-circle mana table and
                                                    cast-skill formula (GetCastSkills)

Mana per circle comes from MagerySpell.m_ManaTable. Cast skill comes from
GetCastSkills(): avg = ChanceLength * circleIndex; min = avg - ChanceOffset
(0% success below this), max = avg + ChanceOffset (100% success at/above).

Effect descriptions are one-sentence summaries curated in this file (DESCRIPTIONS),
written from reading each spell's OnCast/Target implementation. If a spell is
added/renamed in ServUO without a description here, extraction fails loudly.

Scope: Magery only (Necromancy/Chivalry/etc. are ignored).

Usage: python3 tools/extract_spells.py
Stdlib only.
"""

import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
SERVUO_ROOT = WIKI_ROOT.parent / "servuo"
SPELLS_DIR = SERVUO_ROOT / "Scripts" / "Spells"
OUT_PATH = WIKI_ROOT / "data" / "spells.json"

CIRCLE_DIRS = [
    (1, "First"), (2, "Second"), (3, "Third"), (4, "Fourth"),
    (5, "Fifth"), (6, "Sixth"), (7, "Seventh"), (8, "Eighth"),
]

# Reagent.* token -> display name
REAGENT_NAMES = {
    "BlackPearl": "Black Pearl",
    "Bloodmoss": "Bloodmoss",
    "Garlic": "Garlic",
    "Ginseng": "Ginseng",
    "MandrakeRoot": "Mandrake Root",
    "Nightshade": "Nightshade",
    "SpidersSilk": "Spiders' Silk",
    "SulfurousAsh": "Sulfurous Ash",
}

# One-sentence effect summaries, keyed by spell class name. Curated from
# reading OnCast/Target in each Scripts/Spells/<Circle>/<Spell>.cs.
DESCRIPTIONS = {
    # Circle 1
    "ClumsySpell": "Temporarily lowers the target's Dexterity, with potency and duration scaling on the caster's Evaluating Intelligence.",
    "CreateFoodSpell": "Conjures a random item of food directly into the caster's backpack.",
    "FeeblemindSpell": "Temporarily lowers the target's Intelligence, scaling on the caster's Evaluating Intelligence.",
    "HealSpell": "Instantly restores a small amount of hit points to the target, but fails on poisoned or mortally wounded targets.",
    "MagicArrowSpell": "Fires a magical bolt at the target dealing a small amount of pure fire damage.",
    "NightSightSpell": "Grants the target a magical light that lets them see in darkness for an extended duration.",
    "ReactiveArmorSpell": "Buffs the caster's physical resistance at the cost of the other elemental resistances (pre-AOS: reflects part of melee damage back at attackers).",
    "WeakenSpell": "Temporarily lowers the target's Strength, scaling on the caster's Evaluating Intelligence.",
    # Circle 2
    "AgilitySpell": "Temporarily raises the target's Dexterity, scaling on the caster's Evaluating Intelligence.",
    "CunningSpell": "Temporarily raises the target's Intelligence, scaling on the caster's Evaluating Intelligence.",
    "CureSpell": "Attempts to neutralize poison on the target, with success chance based on caster skill versus poison level.",
    "HarmSpell": "Deals cold damage to the target, hitting hardest at point-blank range and weakening with distance.",
    "MagicTrapSpell": "Places a magical explosive trap on a container that detonates on the next person to open it.",
    "ProtectionSpell": "Prevents the caster's spells from being interrupted, at the cost of physical resistance and Resisting Spells skill (pre-AOS: a timed armor buff).",
    "RemoveTrapSpell": "Removes a magical trap from a trapped container.",
    "StrengthSpell": "Temporarily raises the target's Strength, scaling on the caster's Evaluating Intelligence.",
    # Circle 3
    "BlessSpell": "Temporarily raises the target's Strength, Dexterity and Intelligence all at once.",
    "FireballSpell": "Hurls a ball of fire that deals moderate fire damage to the target.",
    "MagicLockSpell": "Magically locks an unlocked, untrapped chest (cannot be used on doors or secured containers).",
    "PoisonSpell": "Inflicts poison on the target, with poison level scaling on caster skill and proximity to the target.",
    "TelekinesisSpell": "Manipulates an item, lever or container from a distance, triggering or opening it remotely.",
    "TeleportSpell": "Instantly moves the caster to a visible nearby location in line of sight.",
    "UnlockSpell": "Magically unlocks chests with low-level locks (fails on door locks and strongly locked or trapped chests).",
    "WallOfStoneSpell": "Raises a temporary wall of stone that blocks movement across a short line of tiles.",
    # Circle 4
    "ArchCureSpell": "Cures poison on all valid targets in an area around the target point (single-target cure with a skill bonus when targeting one mobile).",
    "ArchProtectionSpell": "Casts Protection on the target (pre-AOS: on everyone in an area around the target point).",
    "CurseSpell": "Temporarily lowers the target's Strength, Dexterity and Intelligence, and under AOS also caps their resistances and blocks beneficial stat buffs.",
    "FireFieldSpell": "Creates a temporary line of fire on the ground that repeatedly burns anyone standing in it.",
    "GreaterHealSpell": "Restores a large amount of hit points to the target, but fails on poisoned or mortally wounded targets.",
    "LightningSpell": "Strikes the target with a bolt of lightning dealing energy damage.",
    "ManaDrainSpell": "Drains mana from the target if they fail to resist (under AOS the mana returns to them after a delay).",
    "RecallSpell": "Instantly transports the caster to the location stored in a marked rune (also works off ship keys to board a boat).",
    # Circle 5
    "BladeSpiritsSpell": "Summons an uncontrolled whirling blade spirit that attacks the nearest creatures, consuming follower slots.",
    "DispelFieldSpell": "Dispels a single field tile such as fire, poison, energy or paralyze fields, or a wall of stone.",
    "IncognitoSpell": "Disguises the caster with a random name, body and hair, concealing their identity for a duration.",
    "MagicReflectSpell": "Causes hostile spells to reflect back at their caster (under AOS instead trades physical resistance for boosts to the elemental resistances).",
    "MindBlastSpell": "Blasts the target with psychic cold damage, under AOS scaling on the caster's Intelligence (pre-AOS: based on the stat gap between caster and target).",
    "ParalyzeSpell": "Freezes the target in place for a duration based on caster skill, broken by damage.",
    "PoisonFieldSpell": "Creates a temporary wall of poisonous vapor that poisons anyone moving through it.",
    "SummonCreatureSpell": "Summons a random natural creature (such as a bear, wolf or panther) to fight for the caster, consuming follower slots.",
    # Circle 6
    "DispelSpell": "Attempts to banish a summoned creature outright, with success based on caster skill versus the summon's dispel difficulty.",
    "EnergyBoltSpell": "Fires a powerful bolt of pure energy damage at the target.",
    "ExplosionSpell": "Plants a delayed explosion on the target that detonates for heavy fire damage after a few seconds.",
    "InvisibilitySpell": "Renders the target invisible until the effect expires or they act.",
    "MarkSpell": "Binds the caster's current location into a blank recall rune for later Recall or Gate Travel.",
    "MassCurseSpell": "Lowers Strength, Dexterity and Intelligence of every valid target in an area around the target point.",
    "ParalyzeFieldSpell": "Creates a temporary field that paralyzes anyone who walks into it.",
    "RevealSpell": "Reveals hidden and invisible creatures and players in an area, with radius based on caster skill.",
    # Circle 7
    "ChainLightningSpell": "Calls down lightning on every valid target in an area, dealing energy damage (divided among targets pre-AOS).",
    "EnergyFieldSpell": "Creates a temporary impassable wall of energy that blocks movement entirely.",
    "FlameStrikeSpell": "Engulfs the target in a pillar of flame dealing heavy fire damage.",
    "GateTravelSpell": "Opens a pair of linked moongates between the caster and the location stored in a marked rune, usable by anyone.",
    "ManaVampireSpell": "Drains mana from the target and transfers it to the caster if the target fails to resist.",
    "MassDispelSpell": "Attempts to dispel every summoned creature in a large area around the target point.",
    "MeteorSwarmSpell": "Rains meteors on an area, dealing fire damage to every valid target (divided among targets pre-AOS).",
    "PolymorphSpell": "Transforms the caster's body into a chosen creature form, with combat stats to match, until cancelled.",
    # Circle 8
    "AirElementalSpell": "Summons an air elemental to fight for the caster, consuming two follower slots.",
    "EarthElementalSpell": "Summons an earth elemental to fight for the caster, consuming two follower slots.",
    "EarthquakeSpell": "Shakes the earth, dealing physical damage to every valid target nearby based on their current hit points.",
    "EnergyVortexSpell": "Summons an uncontrolled energy vortex that relentlessly attacks the nearest creature, consuming follower slots.",
    "FireElementalSpell": "Summons a fire elemental to fight for the caster, consuming two follower slots.",
    "ResurrectionSpell": "Returns a dead player's ghost to life where they stand.",
    "SummonDaemonSpell": "Summons a daemon to fight for the caster, consuming follower slots (and under AOS damaging the caster's karma).",
    "WaterElementalSpell": "Summons a water elemental to fight for the caster, consuming two follower slots.",
}

RE_CLASS = re.compile(r"class\s+(\w+)\s*:\s*MagerySpell")
RE_SPELLINFO = re.compile(r"new\s+SpellInfo\s*\((.*?)\);", re.DOTALL)
RE_STRINGS = re.compile(r'"((?:[^"\\]|\\.)*)"')
RE_REAGENT = re.compile(r"Reagent\.(\w+)")
RE_MANA_TABLE = re.compile(r"m_ManaTable\s*=\s*new\s+int\[\]\s*\{([^}]*)\}")
RE_CHANCE = re.compile(
    r"ChanceOffset\s*=\s*([\d.]+)\s*,\s*ChanceLength\s*=\s*([\d.]+)\s*/\s*([\d.]+)"
)


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def parse_circle_tables():
    """Parse mana table + cast-skill formula constants out of MagerySpell.cs."""
    src = read_source(SPELLS_DIR / "Base" / "MagerySpell.cs")

    m = RE_MANA_TABLE.search(src)
    if not m:
        sys.exit("ERROR: could not find m_ManaTable in MagerySpell.cs")
    mana = [int(x.strip()) for x in m.group(1).split(",") if x.strip()]
    if len(mana) != 8:
        sys.exit(f"ERROR: expected 8 mana entries, got {len(mana)}")

    c = RE_CHANCE.search(src)
    if not c:
        sys.exit("ERROR: could not find ChanceOffset/ChanceLength in MagerySpell.cs")
    offset = float(c.group(1))
    length = float(c.group(2)) / float(c.group(3))

    circles = {}
    for idx in range(8):
        avg = length * idx  # GetCastSkills: avg = ChanceLength * (int)Circle
        circles[str(idx + 1)] = {
            "mana": mana[idx],
            # below min_skill the cast always fails; at/above max_skill it never fizzles
            "min_skill": round(avg - offset, 1),
            "max_skill": round(avg + offset, 1),
        }
    return circles


def read_source(path: Path) -> str:
    """ServUO sources are mostly UTF-8 but a few files are cp1252."""
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252")


def parse_spell_file(path: Path, circle: int, circles: dict) -> dict:
    src = read_source(path)

    cls = RE_CLASS.search(src)
    if not cls:
        sys.exit(f"ERROR: no MagerySpell class found in {path}")
    class_name = cls.group(1)

    info = RE_SPELLINFO.search(src)
    if not info:
        sys.exit(f"ERROR: no SpellInfo registration found in {path}")
    args = info.group(1)

    strings = RE_STRINGS.findall(args)
    if len(strings) < 2:
        sys.exit(f"ERROR: could not parse name/mantra in {path}")
    name, mantra = strings[0], strings[1]

    reagents = []
    for token in RE_REAGENT.findall(args):
        if token not in REAGENT_NAMES:
            sys.exit(f"ERROR: unknown reagent Reagent.{token} in {path}")
        reagents.append(REAGENT_NAMES[token])

    if class_name not in DESCRIPTIONS:
        sys.exit(f"ERROR: no curated description for {class_name} ({path}); add one to DESCRIPTIONS")

    ct = circles[str(circle)]
    return {
        "class_name": class_name,
        "name": name,
        "slug": slugify(name),
        "mantra": mantra,
        "reagents": reagents,
        "circle": circle,
        "mana": ct["mana"],
        "min_skill": ct["min_skill"],
        "max_skill": ct["max_skill"],
        "description": DESCRIPTIONS[class_name],
        "source": str(path.relative_to(SERVUO_ROOT)).replace("\\", "/"),
    }


def main():
    circles = parse_circle_tables()

    spells = []
    for circle, dirname in CIRCLE_DIRS:
        files = sorted((SPELLS_DIR / dirname).glob("*.cs"))
        if len(files) != 8:
            sys.exit(f"ERROR: expected 8 spells in {dirname}/, found {len(files)}")
        for f in files:
            spells.append(parse_spell_file(f, circle, circles))

    if len(spells) != 64:
        sys.exit(f"ERROR: expected 64 spells, got {len(spells)}")

    out = {
        "_schema": {
            "description": "Magery spells extracted from ServUO source by tools/extract_spells.py. Do not hand-edit; re-run the extractor.",
            "extracted_from": "servuo: Scripts/Spells/First..Eighth + Scripts/Spells/Base/MagerySpell.cs",
            "circles": "map of circle number -> {mana, min_skill, max_skill}; min_skill = 0% cast chance threshold, max_skill = 100% (from MagerySpell.GetCastSkills)",
            "spells": "list of {class_name, name, slug, mantra, reagents, circle, mana, min_skill, max_skill, description, source}; description is a curated one-sentence summary of OnCast/Target behavior",
        },
        "circles": circles,
        "spells": spells,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(spells)} spells across {len(circles)} circles -> {OUT_PATH}")


if __name__ == "__main__":
    main()
