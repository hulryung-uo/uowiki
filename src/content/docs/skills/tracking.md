---
title: Tracking
description: Locate nearby creatures and players by their tracks.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 38 — Ranger, Int/Dex, dexGain 1.25 / intGain 1.25)"
  - "servuo: Scripts/Skills/Tracking.cs"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills — teach cap)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/38.gif" alt="Tracking skill banner" width="160" />

Tracking locates nearby mobiles and points you toward them. The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table, the range formula, and the reveal-chance formula below are
source-verified against ServUO.

## What it does

Tracking detects nearby creatures, animals, humans, or players within a range that grows with
skill, then plants a quest-arrow guiding you to the chosen target. It is the hunter's and
scout's locator — useful for finding prey, lost pets, or a fleeing player, and it can even
help reveal hidden targets. See [movement & travel](/playing/movement-and-travel/).

## How to use it

Activate the skill and pick a category (Animals / Monsters / Human NPCs / Players). It lists
the mobiles of that type in range; choose one and a quest-arrow points to it until you arrive
(or it leaves range). See [targeting](/playing/targeting/).

## How to train it

**Quick start:** an NPC Ranger teaches Tracking up to **one-third of its own skill, capped at
42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

The trick: **Use Tracking over and over with targets in range** — each attempt rolls a gain.

- **Low/high skill** — track repeatedly across the four categories wherever the relevant
  mobiles exist. Busy areas keep targets available: **stand in a town for humans/animals**, or
  in the wilds/a dungeon for monsters, and just keep tracking. GGS guarantees the slow late
  points as long as you keep using it.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Ranger |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +1.25, Int +1.25 (per-use stat gain weights) |

From `Scripts/Skills/Tracking.cs`: detection range is **`10 + Tracking / 10`** tiles — so
**18 tiles at GM**. The chance to track (and reveal) a hidden target on the modern (SE) ruleset
is `50 × (Tracking × 2 + DetectHidden) / divisor`, where the divisor depends on the target's
Hiding/Stealth — so [Detecting Hidden](/skills/detecting-hidden/) improves Tracking's reveal
odds.

## Related skills & synergies

- **[Detecting Hidden](/skills/detecting-hidden/)** — factors into Tracking's chance to find
  hidden targets.
- **[Cartography](/skills/cartography/) + [Camping](/skills/camping/)** — the explorer/
  treasure-hunter kit.

## See also

- [Movement & travel](/playing/movement-and-travel/) · [Hiding & stealth](/playing/hiding-and-stealth/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
