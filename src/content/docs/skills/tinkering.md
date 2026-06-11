---
title: Tinkering
description: Make tools, locks, traps, jewelry, and clockwork.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 37)"
  - "servuo: Scripts/Services/Craft/DefTinkering.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/37.gif" alt="Tinkering skill banner" width="160" />

Tinkering is the versatile small-goods [crafting skill](/playing/crafting/). The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Tinkering makes a huge range of small items from ingots, wood, and parts: crafting **tools**
(including the tools other crafts need), keys and **locks**, **trapped containers**, clocks,
sextants, scissors, jewelry, golems, and clockwork assemblies. It is the support craft that
keeps every other crafter supplied and provides the locked/trapped boxes used to train
[Lockpicking](/skills/lockpicking/) and [Remove Trap](/skills/remove-trap/).

## How to use it

Carry tinker's tools and the materials (ingots, boards, gems), then use the tools to open the
crafting menu and build the item. See [crafting](/playing/crafting/).

## How to train it

**Quick start:** an NPC Tinker teaches up to **one-third of its own skill, capped at 42.0**
(`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then make the hardest part
that still has a workable success %, stepping up as skill climbs:

- **Low skill** — craft simple tools and parts; cheap and fast (and the wire/ingot ones are
  the classic cheap grind — smelt or vendor the output and repeat).
- **Mid/high skill** — work up to jewelry, traps, and clockwork for the steadiest gains.

Keep a **bulk ingot supply** so a session runs uninterrupted; GGS pays out the slow late
points as long as you keep crafting. Recipe thresholds live in
`Scripts/Services/Craft/DefTinkering.cs`. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Tinker |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.5, Dex +0.2, Int +0.3 (per-use stat gain weights) |

Tinkering is a pure crafting skill — no active target. It is unique in being able to make
**trapped lockable boxes**, the standard rig for training rogue skills.

## Related skills & synergies

- **[Lockpicking](/skills/lockpicking/) + [Remove Trap](/skills/remove-trap/)** — Tinker-made
  locked/trapped boxes are how those skills are trained.
- **[Blacksmithy](/skills/blacksmithy/)** — shares the ingot supply and makes tinkers a handy
  second craft for a smith.

## See also

- [Crafting (how to play)](/playing/crafting/) · [Tinkering crafting](/crafting/tinkering/)
- [Tools catalog](/items/catalog/tools/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
