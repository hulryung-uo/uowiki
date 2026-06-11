---
title: Remove Trap
description: Disarm trapped containers.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 48)"
  - "servuo: Scripts/Skills/RemoveTrap.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/48.gif" alt="Remove Trap skill banner" width="160" />

Remove Trap detects and disables traps on containers. The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table and timing notes below are source-verified against ServUO.

## What it does

Remove Trap lets you disarm the traps on chests and containers — explosion, dart, and poison
traps on dungeon and treasure chests — so you can loot them safely instead of eating the
blast. It is the companion to [Lockpicking](/skills/lockpicking/) and
[Detecting Hidden](/skills/detecting-hidden/) on a treasure hunter.

## How to use it

Stand next to the trapped container (you must be in range), use the skill, and target it. A
successful roll clears the trap. On treasure chests the work takes longer the higher the
chest tier. See [gathering resources](/playing/gathering-resources/).

## How to train it

- **Low/mid skill** — disarm boxes trapped by a [Tinker](/skills/tinkering/) at a chosen
  difficulty (the standard training rig).
- **High skill** — disarm real dungeon and treasure-map chests.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Trap Specialist |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

From `Scripts/Skills/RemoveTrap.cs`: there is a **10-second** reuse delay, you must be within
**3 tiles** of the container, and on success the chest's `TrapLevel` is set to 0. Treasure
chests take longer to disarm by tier — roughly **20 / 60 / 180 / 420 / 540 seconds** for
Stash / Supply / Cache / Hoard / Trove.

## Related skills & synergies

- **[Lockpicking](/skills/lockpicking/) + [Detecting Hidden](/skills/detecting-hidden/) +
  [Cartography](/skills/cartography/) + [Mining](/skills/mining/)** — the treasure-hunter
  toolkit.
- **[Tinkering](/skills/tinkering/)** — crafts the trapped boxes used to train.

## See also

- [Gathering resources](/playing/gathering-resources/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
