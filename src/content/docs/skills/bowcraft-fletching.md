---
title: Bowcraft/Fletching
description: Craft bows, crossbows, and arrows from wood.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Services/Craft/DefBowFletching.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/8.gif" alt="Bowcraft/Fletching skill banner" width="160" />

Bowcraft/Fletching (Fletching) is the [crafting skill](/playing/crafting/) that supplies
archers with bows, crossbows, and ammunition. The prose is community-derived (paraphrased
from the uorenaissance.com skill list plus ServUO behavior) pending field verification; the
stats table is source-verified against ServUO.

## What it does

Fletching shapes boards and feathers into the full ranged arsenal: bows, crossbows, heavy
crossbows, arrows, and bolts. It is the support craft behind every [archer](/skills/archery/),
keeping a steady supply of weapons and the consumable ammunition combat eats through.

## How to use it

Stock boards (from [lumberjacking](/skills/lumberjacking/)) and, for arrows, feathers, then
use a fletching kit to open the crafting menu and build the item. Higher skill unlocks
heavier ranged weapons, improves success, and can yield exceptional-quality bows with bonus
damage. See [crafting](/playing/crafting/) and [gathering resources](/playing/gathering-resources/).

## How to train it

**Quick start:** an NPC trainer (a Bowyer or Ranger) teaches Fletching up to **one-third of
its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then make the hardest piece
that still has a workable success %, stepping up as skill climbs:

- **Low skill** — fletch arrows and shafts; cheap and fast.
- **Mid skill** — bows and crossbows.
- **High skill** — heavy crossbows and the hardest pieces give the steadiest late gains;
  exceptional results become more frequent.

Keep a **bulk supply of boards** so a session runs uninterrupted; GGS pays out the slow late
points as long as you keep crafting. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/). Recipe thresholds live in
`Scripts/Services/Craft/DefBowFletching.cs`.

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Strength |
| Title | Bowyer |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.6, Dex +1.6 (per-use stat gain weights) |

Fletching is a pure crafting skill — no active target; all progress comes from the crafting
menu, and special woods raise difficulty (and reward).

## Related skills & synergies

- **[Archery](/skills/archery/)** — the customer for everything you make.
- **[Lumberjacking](/skills/lumberjacking/) + [Carpentry](/skills/carpentry/)** — wood
  supply and the sister woodcraft skill.

## See also

- [Crafting (how to play)](/playing/crafting/) · [Bowfletching crafting](/crafting/bowfletching/)
- [Weapons catalog](/items/catalog/weapons/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
