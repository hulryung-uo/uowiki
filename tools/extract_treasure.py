# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Extract treasure-hunting facts from ServUO into data/treasure.json.

This wiki documents OUR shard, which runs expansion EJ (Config/Expansion.cfg
=> CurrentExpansion=EJ). Because TreasureMapInfo.NewSystem == Core.EJ, the
modern "Forgotten Treasures" treasure-map system is LIVE here: maps have the
five levels Stash/Supply/Cache/Hoard/Trove and one of five loot packages
(Artisan/Assassin/Mage/Ranger/Warrior).

Sources (read-only, paths relative to ../servuo):
  - Scripts/Services/TreasureMaps/TreasureMap.cs       (decode/dig/spawn/locations)
  - Scripts/Services/TreasureMaps/TreasureMapInfo.cs   (levels, packages, loot, chest)
  - Scripts/Services/TreasureMaps/TreasureMapChest.cs  (chest skills, artifacts)
  - Config/TreasureMaps.cfg                            (Enabled/LootChance/ResetTime)
  - Config/Expansion.cfg                               (CurrentExpansion=EJ)
  - Data/treasure.cfg                                  (192 classic dig sites)

Output:
  data/treasure.json

Run:  uv run --script tools/extract_treasure.py
"""

import json
import re
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
SERVUO = Path("/Users/dkkang/dev/uo/servuo")
TREASURE_CFG = SERVUO / "Data" / "treasure.cfg"
MAPS_CFG = SERVUO / "Config" / "TreasureMaps.cfg"
EXPANSION_CFG = SERVUO / "Config" / "Expansion.cfg"
OUT = WIKI / "data" / "treasure.json"

# Felucca/Trammel coordinate space upper bound (TreasureMap.cs m_FelTramWrap).
UO_W, UO_H = 5120, 4096


def parse_locations() -> list[dict]:
    """Parse Data/treasure.cfg: one 'X Y' per line -> [{x, y}, ...]."""
    pts = []
    for line in TREASURE_CFG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            pts.append({"x": int(parts[0]), "y": int(parts[1])})
        except ValueError:
            continue
    return pts


def cfg_value(text: str, key: str) -> str | None:
    m = re.search(rf"^\s*{re.escape(key)}\s*=\s*(.+?)\s*$", text, re.MULTILINE)
    return m.group(1) if m else None


def main():
    locations = parse_locations()

    maps_cfg_text = MAPS_CFG.read_text(encoding="utf-8")
    expansion_text = EXPANSION_CFG.read_text(encoding="utf-8")

    config = {
        "expansion": cfg_value(expansion_text, "CurrentExpansion"),
        "new_system_live": cfg_value(expansion_text, "CurrentExpansion") == "EJ",
        "randomized_locations_enabled": cfg_value(maps_cfg_text, "Enabled") == "True",
        "loot_chance": float(cfg_value(maps_cfg_text, "LootChance") or 0.0),
        "reset_time_days": float(cfg_value(maps_cfg_text, "ResetTime") or 0.0),
    }

    # --- Modern (Forgotten Treasures, EJ) facts, from TreasureMapInfo.cs ---
    levels = ["Stash", "Supply", "Cache", "Hoard", "Trove"]
    packages = ["Artisan", "Assassin", "Mage", "Ranger", "Warrior"]

    # AssignChestQuality(): dif per level; Utility.Random(dif) <= Cartography skill.
    decode_difficulty = {
        "Stash": 100,
        "Supply": 200,
        "Cache": 300,
        "Hoard": 400,
        "Trove": 500,
    }

    # TreasureMapInfo.Fill(): chest skill scaling keyed by (int)level 0..4.
    # LockLevel = RequiredSkill - 10; MaxLockLevel = RequiredSkill + 40.
    chest_skills = {
        "Stash": {"required_skill": 5, "lock_level": -5, "max_lock_level": 45,
                  "trap_power": 25, "trap_level": 1},
        "Supply": {"required_skill": 45, "lock_level": 35, "max_lock_level": 85,
                   "trap_power": 75, "trap_level": 3},
        "Cache": {"required_skill": 75, "lock_level": 65, "max_lock_level": 115,
                  "trap_power": 125, "trap_level": 5},
        "Hoard": {"required_skill": 80, "lock_level": 70, "max_lock_level": 120,
                  "trap_power": 150, "trap_level": 6},
        "Trove": {"required_skill": 80, "lock_level": 70, "max_lock_level": 120,
                  "trap_power": 170, "trap_level": 7},
    }
    trap_type = "ExplosionTrap"

    # Gold per level, GetGoldCount() in TreasureMapInfo.cs.
    gold = {
        "Stash": [10000, 40000],
        "Supply": [20000, 50000],
        "Cache": [30000, 60000],
        "Hoard": [40000, 70000],
        "Trove": [50000, 70000],
    }

    # Magic equipment count, GetEquipmentAmount().
    equipment_amount = {
        "Stash": 6, "Supply": 8, "Cache": 12, "Hoard": 18, "Trove": 36,
    }  # Cache+Assassin is 24 (special-cased in source)

    # Dig range from Cartography (NewSystem path uses Cartography, not Mining),
    # DigTarget.OnTarget: >=100 -> 4, >=81 -> 3, >=51 -> 2, else 1 tile.
    dig_range = [
        {"skill_at_least": 100.0, "tiles": 4},
        {"skill_at_least": 81.0, "tiles": 3},
        {"skill_at_least": 51.0, "tiles": 2},
        {"skill_at_least": 0.0, "tiles": 1},
    ]

    # Guardians: DigTimer spawns 4 mobs (level>=2). NewSystem: each has a 70%
    # chance to be a tagged "(Guardian)". Spawn tables by facet/level.
    guardians = {
        "count": 4,
        "guardian_chance": 0.70,  # Utility.RandomDouble() >= 0.3
        "felucca_trammel_by_level": {
            # GetSpawnList maps NewSystem level -> classic table rows.
            "Stash": ["Mongbat", "Ratman", "HeadlessOne", "Skeleton", "Zombie"],
            "Supply": ["OrcishMage", "Gargoyle", "Gazer", "HellHound", "EarthElemental"],
            "Cache": ["Lich", "OgreLord", "DreadSpider", "AirElemental", "FireElemental",
                      "LichLord", "Daemon", "ElderGazer"],
            "Hoard": ["AncientWyrm", "Balron", "BloodElemental", "PoisonElemental", "Titan"],
            "Trove": ["BloodElemental", "ColdDrake", "FrostDragon", "FrostDrake",
                      "GreaterDragon", "PoisonElemental"],
        },
    }

    # High-level special loot rules (TreasureMapInfo.cs).
    special_loot = {
        "power_scrolls": {
            "facet": "Felucca only",
            "min_level": "Cache",
            "value": 110.0,
            "note": "GetPowerScrollList: Felucca + level >= Cache; PowerScroll(skill, 110.0).",
        },
        "scrolls_of_transcendence": {
            "excluded_levels": ["Supply", "Cache"],
            "note": "GetTranscendenceList: not on Supply/Cache; amount per (int)level+1.",
        },
        "scrolls_of_alacrity": {
            "excluded": "Stash (all); Cache on Felucca",
            "note": "GetAlacrityList.",
        },
        "reagents": {
            "only": "Stash + Mage package",
            "amount_by_quality": {"Rusty": 20, "Standard": 40, "Gold": 60},
            "note": "GetReagentList / GetRegAmount.",
        },
        "gems": {
            "note": "GetGemCount: base 7/9/11 by chest quality + level*5, one bag of gems.",
        },
    }

    chest_quality = {
        "values": ["Rusty", "Standard", "Gold"],
        "note": "AssignChestQuality: Cartography vs Utility.Random(decode_difficulty); "
                "higher skill -> Gold; affects gem/reg/material counts and chest art.",
    }

    facet_regions = {
        "note": "When TreasureMaps.Enabled (NewChestLocations) is True, the chest "
                "spot is randomized within per-facet diggable rectangles "
                "(TreasureMap.cs), then ValidateLocation() rejects towns, houses, "
                "dungeons, champ spawns, roads and non-walkable/non-natural tiles. "
                "Felucca and Trammel use the whole map.",
        "felucca_trammel": [[0, 0, 5119, 4095]],
        "rect_counts": {
            "tokuno": 32, "malas": 4, "ilshenar": 8, "termur": 8, "eodon": 11,
        },
    }

    classic_note = (
        "Data/treasure.cfg holds 192 fixed classic dig sites (Britannia/"
        "Felucca-Trammel coords). These are used by GetRandomClassicLocation() "
        "when NewChestLocations is False; on our shard NewChestLocations is True, "
        "so live maps randomize within the facet regions above. The 192 sites are "
        "the traditional, well-known treasure spots players think of as 'the dig "
        "locations' and are what is plotted on the wiki map."
    )

    data = {
        "system": "Forgotten Treasures (modern EJ system)",
        "config": config,
        "levels": levels,
        "packages": packages,
        "decode_difficulty": decode_difficulty,
        "decode_note": "Decode: Cartography skill check; AssignChestQuality compares "
                       "Cartography against Utility.Random(decode_difficulty). "
                       "decode_difficulty is the classic level/100 table.",
        "chest_skills": chest_skills,
        "trap_type": trap_type,
        "chest_quality": chest_quality,
        "gold": gold,
        "equipment_amount": equipment_amount,
        "dig_range": dig_range,
        "guardians": guardians,
        "special_loot": special_loot,
        "facet_regions": facet_regions,
        "classic_locations_note": classic_note,
        "coord_space": {"width": UO_W, "height": UO_H},
        "location_count": len(locations),
        "locations": locations,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"expansion: {config['expansion']}  new_system_live: {config['new_system_live']}")
    print(f"randomized locations enabled: {config['randomized_locations_enabled']}")
    print(f"loot_chance: {config['loot_chance']}  reset_time_days: {config['reset_time_days']}")
    print(f"levels: {levels}")
    print(f"packages: {packages}")
    print(f"classic dig locations parsed: {len(locations)}")
    xs = [p["x"] for p in locations]
    ys = [p["y"] for p in locations]
    print(f"x range: {min(xs)}..{max(xs)}   y range: {min(ys)}..{max(ys)}")
    print(f"wrote {OUT.relative_to(WIKI)}")


if __name__ == "__main__":
    main()
