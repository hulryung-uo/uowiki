---
title: Lockpicking
description: Open locked chests and doors without a key.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 24)"
  - "servuo: Scripts/Items/Consumables/LockPick.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/24.gif" alt="Lockpicking skill banner" width="160" />

Lockpicking opens locked containers and doors with picks. The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table and pick mechanics below are source-verified against ServUO.

## What it does

Lockpicking lets you open locked chests and doors without a key — dungeon chests, locked loot,
and, most lucratively, the chests dug up from [treasure maps](/skills/cartography/). Higher
locks demand more skill, and a trapped chest can spring on you if you have not dealt with the
trap.

## How to use it

Carry lockpicks, use one, and target the locked container or door. The roll compares your
skill to the lock's difficulty. Beware: picking a **trapped** chest can trigger it — clear it
first with [Remove Trap](/skills/remove-trap/). See [gathering resources](/playing/gathering-resources/).

## How to train it

- **Low/mid skill** — pick easy locks. [Tinkers](/skills/tinkering/) can craft locked boxes
  at a chosen difficulty, the classic training setup.
- **High skill** — pick harder dungeon and treasure chests; treasure-map chests scale their
  lock to map level.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Infiltrator |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +2 (per-use stat gain weights) |

From `Scripts/Items/Consumables/LockPick.cs`: you must have skill ≥ the lock's
**RequiredSkill** to attempt it; the check then rolls `CheckTargetSkill(Lockpicking,
container, LockLevel, MaxLockLevel)`. On **failure** there is a **25% chance the lockpick
breaks**. A lock level of 0 cannot be picked, and −255 means it is magically locked (needs a
spell, not a pick).

## Related skills & synergies

- **[Cartography](/skills/cartography/) + [Mining](/skills/mining/) +
  [Remove Trap](/skills/remove-trap/)** — the treasure-hunter kit: decode, dig, disarm, pick.
- **[Tinkering](/skills/tinkering/)** — crafts the locked boxes used to train (and the picks).

## See also

- [Gathering resources](/playing/gathering-resources/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
