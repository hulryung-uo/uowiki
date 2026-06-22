---
title: Cooking
description: Turn raw ingredients into food and feasts.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 13 — Int/Dex, gain Dex 2.0/Int 3.0)"
  - "servuo: Scripts/Services/Craft/DefCooking.cs (InitCraftList: dough, bread, cooked bird, fish steaks, cakes, pies, cookies, muffins)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = BaseFixedPoint/3, capped 420)"
  - "servuo: Scripts/Misc/SkillCheck.cs (GGSActive / CheckGGS)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/13.gif" alt="Cooking skill banner" width="160" />

Cooking is the food-preparation [crafting skill](/playing/crafting/). The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Cooking prepares raw fish, meat, and dough into edible food and finer dishes at an oven,
stove, or campfire, keeping you and your pets fed and supporting other crafts (baking bread,
making pies). Higher skill reduces burnt results and unlocks better dishes.

## How to use it

Gather ingredients (fish from [fishing](/skills/fishing/), meat and hides from kills, dough
from flour and water), then cook at a heat source. Use the cooking process to combine raw
ingredients and bake the result. See [crafting](/playing/crafting/) and
[food & drink catalog](/items/catalog/food-drink/).

## How to train it

**Quick start:** an NPC Cook/Baker teaches up to **one-third of its own skill, capped at
42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then make the hardest dish
that still has a workable success %, stepping up as skill climbs:

- **Low skill** — bake bread and cook simple meats; cheap, repeatable.
- **Mid/high skill** — work up to the more complex dishes; success rate climbs and burns drop.

Keep a **bulk supply of flour, water, and raw food** so a session runs uninterrupted; GGS
pays out the slow late points as long as you keep cooking. Recipe thresholds live in
`Scripts/Services/Craft/DefCooking.cs`. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Chef |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +2, Int +3 (per-use stat gain weights) |

Cooking is a pure crafting skill — no active target. Note: poison-detection on consumables is
handled by [Taste Identification](/skills/taste-identification/), not Cooking.

## Related skills & synergies

- **[Fishing](/skills/fishing/)** — primary food supply for a cook.
- **[Alchemy](/skills/alchemy/) / [Inscription](/skills/inscription/)** — companion
  consumable crafts.
- **[Taste Identification](/skills/taste-identification/)** — spots poison in the food you
  make or buy.

## See also

- [Crafting (how to play)](/playing/crafting/) · [Cooking crafting](/crafting/cooking/)
- [Food & drink catalog](/items/catalog/food-drink/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
