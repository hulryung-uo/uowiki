---
title: Fishing
description: Pull fish, sea serpents, and treasure from the water.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 18, Fishing)"
  - "servuo: Scripts/Services/Harvest/Fishing.cs"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/18.gif" alt="Fishing skill banner" width="160" />

Fishing is a [gathering skill](/playing/gathering-resources/) worked from any water tile. The
stats table and the special-catch mechanics below are source-verified against ServUO; the
general training advice is community guidance pending field verification.

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

**Quick start:** an NPC Fisherman teaches Fishing up to **one-third of its own skill, capped
at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. After that it's a pure
resource loop: just keep casting and **GGS carries it**.

- **Low/mid skill** — fish from any shoreline or dock; catches and gains come steadily.
- **High skill** — fish from a boat in deep water for the better hauls (special fish, MIBs,
  treasure) and to keep gaining.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Strength |
| Title | Fisherman |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.5, Dex +0.5 (per-use stat gain weights) |

Implementation lives in `Scripts/Services/Harvest/Fishing.cs`. The special-catch table
(`MutateEntry`) gates the better hauls on **deep water** (Trammel/Felucca/Tokuno only) and on
your **base** Fishing skill:

- **Special fishing net** and **big fish** — require base Fishing **≥ 80**, deep water.
- **Message in a bottle (MIB)** — requires base Fishing **≥ 100**, deep water.

Reeling up a **treasure map, MIB, or special fishing net** also spawns a water monster next to
you — a **25% chance of a Deep Sea Serpent**, otherwise a regular **Sea Serpent**
(`Give()`). Fishing up an existing **SOS** message's location yields a shipwreck chest.

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
