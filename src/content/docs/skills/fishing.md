---
title: Fishing
description: Pull fish, sea serpents, and treasure from the water.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Services/Harvest/Fishing.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/18.gif" alt="Fishing skill banner" width="160" />

Fishing is a [gathering skill](/playing/gathering-resources/) worked from any water tile. The
prose is community-derived (paraphrased from the uorenaissance.com skill list plus ServUO
behavior) pending field verification; the stats table is source-verified against ServUO.

## What it does

Fishing casts a pole into water to land fish, the staple food supply for
[Cooking](/skills/cooking/). At higher skill it also pulls up message-in-a-bottle treasure,
special big fish, shipwreck loot, and — sometimes — a sea serpent or other water monster that
must be fought. It is a relaxed, low-stakes gathering loop with occasional excitement.

## How to use it

Equip a fishing pole, use it, and target a water tile within reach (from shore or, better,
from a boat). Each cast rolls for a catch. See
[gathering resources](/playing/gathering-resources/) and
[movement & travel](/playing/movement-and-travel/) (boats).

## How to train it

- **Low/mid skill** — fish from any shoreline or dock; catches and gains come steadily.
- **High skill** — fish from a boat in deep water for the better hauls (special fish, MIBs,
  treasure) and to keep gaining.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Intelligence |
| Title | Fisherman |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.5, Int +0.5 (per-use stat gain weights) |

Implementation lives in `Scripts/Services/Harvest/Fishing.cs`. Deep-water and high-skill catches
(serpents, big fish, treasure) become available as skill rises; exact catch tables are
**unverified** here.

## Related skills & synergies

- **[Cooking](/skills/cooking/)** — turns the catch into food.
- **[Cartography](/skills/cartography/)** — MIB and shipwreck content overlaps with sea/
  treasure hunting.
- Sea monsters you may hook are in the [sea bestiary](/bestiary/sea/).

## See also

- [Gathering resources](/playing/gathering-resources/)
- [Movement & travel](/playing/movement-and-travel/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
