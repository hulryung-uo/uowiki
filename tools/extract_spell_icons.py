# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Extract the 64 Magery spell icons from gumpartLegacyMUL.uop.

Gump ID mapping (confirmed in ClassicUO src/ClassicUO.Client/Game/Data/
SpellsMagery.cs + SpellDefinition.cs): magery spell id 1..64 has large
gump icon 0x1B58 + (id-1) and small icon = large - 0x1298, i.e. gump
0x8C0..0x8FF (2240..2303), 44x44. We use the SMALL icon.

Gump format (ClassicUO GumpsLoader.GetGump):
  UOP entry has_extra: extra1 = width, extra2 = height (flag 0 entries).
  payload: int32 rowLookup[height] (offsets in 4-byte words from payload
  start), then per row a sequence of (u16 color, u16 run) RLE pairs.
  Row y pair count = rowLookup[y+1] - rowLookup[y] (last row:
  len(payload)//4 - rowLookup[y]). color 0 = transparent, else ARGB1555.

Output:
  public/img/spells/<spell-id>.png   (1..64)
  data/spell_icons.json
"""

import json
import os
import struct
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
GUMP_PATTERN = "build/gumpartlegacymul/%08d.tga"
LARGE_ICON_BASE = 0x1B58
SMALL_ICON_DELTA = 0x1298  # small = large - delta (gump 2240..2303)

# Canonical magery spell order, ids 1..64 (ClassicUO SpellsMagery.cs).
SPELL_NAMES = [
    # 1st circle
    "Clumsy", "Create Food", "Feeblemind", "Heal",
    "Magic Arrow", "Night Sight", "Reactive Armor", "Weaken",
    # 2nd
    "Agility", "Cunning", "Cure", "Harm",
    "Magic Trap", "Magic Untrap", "Protection", "Strength",
    # 3rd
    "Bless", "Fireball", "Magic Lock", "Poison",
    "Telekinesis", "Teleport", "Unlock", "Wall of Stone",
    # 4th
    "Arch Cure", "Arch Protection", "Curse", "Fire Field",
    "Greater Heal", "Lightning", "Mana Drain", "Recall",
    # 5th
    "Blade Spirits", "Dispel Field", "Incognito", "Magic Reflection",
    "Mind Blast", "Paralyze", "Poison Field", "Summon Creature",
    # 6th
    "Dispel", "Energy Bolt", "Explosion", "Invisibility",
    "Mark", "Mass Curse", "Paralyze Field", "Reveal",
    # 7th
    "Chain Lightning", "Energy Field", "Flamestrike", "Gate Travel",
    "Mana Vampire", "Mass Dispel", "Meteor Swarm", "Polymorph",
    # 8th
    "Earthquake", "Energy Vortex", "Resurrection", "Air Elemental",
    "Summon Daemon", "Earth Elemental", "Fire Elemental", "Water Elemental",
]


# ClassicUO name -> ServUO name (as found in data/spells.json)
NAME_ALIASES = {
    "Magic Untrap": "Remove Trap",
    "Unlock": "Unlock Spell",
    "Flamestrike": "Flame Strike",
}


def decode_gump(uop: uoplib.UopFile, entry: uoplib.UopEntry) -> Image.Image:
    payload = uop.read(entry)
    if entry.flag == uoplib.FLAG_NONE:
        w, h = entry.extra1, entry.extra2
    else:
        # compressed entries carry width/height in the decompressed payload
        w, h = struct.unpack_from("<II", payload, 0)
        payload = payload[8:]
    if w <= 0 or h <= 0:
        raise ValueError("bad gump dimensions")

    row_lookup = struct.unpack_from("<%di" % h, payload, 0)
    total_words = len(payload) // 4
    tbl = uoplib.COLOR_TABLE_5TO8

    out = bytearray(w * h * 4)  # RGBA, transparent
    for y in range(h):
        pos = row_lookup[y] * 4
        gsize = (row_lookup[y + 1] if y < h - 1 else total_words) - row_lookup[y]
        x = 0
        for _ in range(gsize):
            value, run = struct.unpack_from("<HH", payload, pos)
            pos += 4
            if value != 0:
                r = tbl[(value >> 10) & 0x1F]
                g = tbl[(value >> 5) & 0x1F]
                b = tbl[value & 0x1F]
                px = struct.pack("<4B", r, g, b, 255)
                base = (y * w + x) * 4
                out[base:base + run * 4] = px * run
            x += run

    return Image.frombytes("RGBA", (w, h), bytes(out))


def main() -> int:
    spells_meta = json.load(open(os.path.join(ROOT, "data", "spells.json")))
    slug_by_name = {s["name"]: s["slug"] for s in spells_meta["spells"]}

    out_dir = os.path.join(ROOT, "public", "img", "spells")
    os.makedirs(out_dir, exist_ok=True)

    uop = uoplib.UopFile(os.path.join(UO_DIR, "gumpartLegacyMUL.uop"), has_extra=True)

    icons = {}
    extracted = 0
    for spell_id, name in enumerate(SPELL_NAMES, start=1):
        large_id = LARGE_ICON_BASE + spell_id - 1
        gump_id = large_id - SMALL_ICON_DELTA
        used = "small"
        entry = uop.get_by_name(GUMP_PATTERN % gump_id)
        if entry is None:  # fall back to the large icon
            gump_id, used = large_id, "large"
            entry = uop.get_by_name(GUMP_PATTERN % gump_id)
        if entry is None:
            print(f"  MISSING gump for spell {spell_id} {name}")
            continue

        img = decode_gump(uop, entry)
        png_path = os.path.join(out_dir, f"{spell_id}.png")
        img.save(png_path)
        extracted += 1

        wiki_name = NAME_ALIASES.get(name, name)
        slug = slug_by_name.get(wiki_name)
        if slug is None:
            print(f"  WARNING: no slug in spells.json for '{wiki_name}'")
        icons[str(spell_id)] = {
            "name": wiki_name,
            "slug": slug,
            "gump_id": f"0x{gump_id:X}",
            "icon": used,
            "png": f"/img/spells/{spell_id}.png",
            "size": [img.width, img.height],
        }

    doc = {
        "_schema": {
            "description": "Magery spell icon PNGs extracted from gumpartLegacyMUL.uop "
                           "(small spellbook icons, gump 0x8C0..0x8FF). Keyed by magery "
                           "spell id 1..64; slug matches data/spells.json.",
            "extracted_by": "tools/extract_spell_icons.py",
            "source": "uo-resource/gumpartLegacyMUL.uop",
        },
        "icons": icons,
    }
    with open(os.path.join(ROOT, "data", "spell_icons.json"), "w") as f:
        json.dump(doc, f, indent=2)
        f.write("\n")

    print(f"extracted {extracted}/64 spell icons -> {out_dir}")
    return 0 if extracted == 64 else 1


if __name__ == "__main__":
    sys.exit(main())
