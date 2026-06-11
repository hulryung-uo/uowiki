---
title: Item Identification
description: Appraise the type and value of items.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 3)"
  - "servuo: Scripts/Skills/ItemIdentification.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/3.gif" alt="Item Identification skill banner" width="160" />

Item Identification (Item ID) appraises items and, on expansion content, drives
**unraveling** for [Imbuing](/skills/imbuing/). The prose is community-derived (paraphrased
from the uorenaissance.com skill list plus ServUO behavior) pending field verification; the
stats table and skill-check note below are source-verified against ServUO.

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
— useful from 0 to GM. On magic items it reports the unravel ingredient (magical residue,
enchanted essence, or a relic fragment) used by [Imbuing](/skills/imbuing/).

## Related skills & synergies

- **[Imbuing](/skills/imbuing/)** — Item ID's unravel result feeds the imbuing ingredient
  supply.
- **[Arms Lore](/skills/arms-lore/)** — the parallel weapon/armor appraisal skill.

## See also

- [Items & inventory](/playing/items-and-inventory/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
