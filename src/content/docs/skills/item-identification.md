---
title: Item Identification
description: Appraise the type and value of items.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 3, Item Identification)"
  - "servuo: Scripts/Skills/ItemIdentification.cs"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/3.gif" alt="Item Identification skill banner" width="160" />

Item Identification (Item ID) appraises items and, on expansion content, drives
**unraveling** for [Imbuing](/skills/imbuing/). The stats table and the skill-check/unravel
mechanics below are source-verified against ServUO; the general training advice is community
guidance pending field verification.

## What it does

Item ID reveals an item's true nature and rough worth — useful for spotting what a weapon,
armor piece, or piece of loot actually is and what it might sell for. Its most important
modern role is telling you what magical residue/essence an item will **unravel** into, the
ingredient pipeline for [Imbuing](/skills/imbuing/).

## How to use it

Activate the skill and target the item (in your pack, equipped, or on a vendor). A successful
roll shows its identification and, for magic items, the unravel result. See
[items & inventory](/playing/items-and-inventory/) and
[vendors & banking](/playing/vendors-and-banking/).

## How to train it

**Quick start:** an NPC trainer who knows Item ID teaches up to **one-third of its own skill,
capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

Item ID is an active **"read"** skill — Use it on an item and it rolls a gain check each time:

- **Low/high skill** — keep a stack of crafted or looted gear and identify it over and over;
  any item works as a target, so this is one of the quickest skills to GM.

Just keep identifying and GGS pays out the slow late points. See
[skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Merchant |
| Mastery skill | No |
| Gain notes | skill-ups can raise Int +1 (per-use stat gain weights) |

From `Scripts/Skills/ItemIdentification.cs`, the check is `CheckTargetSkill(ItemID, o, 0, 100)`
— useful from 0 to GM. On a successful ID it names the item and **guesses its value**. For
weapons, armor, jewelry, and hats it also reports the [Imbuing](/skills/imbuing/) **unravel
ingredient**, keyed to the item's imbue weight:

- weight 1–200 → **Magical Residue**
- weight 200–480 → **Enchanted Essence** (you need **Imbuing ≥ 45** to be told which)
- weight ≥ 480 → **Relic Fragment** (you need **Imbuing ≥ 95** to be told which)

Items with little to no magic, or already-imbued items, report that they cannot be unraveled.

## Related skills & synergies

- **[Imbuing](/skills/imbuing/)** — Item ID's unravel result feeds the imbuing ingredient
  supply.
- **[Arms Lore](/skills/arms-lore/)** — the parallel weapon/armor appraisal skill.

## See also

- [Items & inventory](/playing/items-and-inventory/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
