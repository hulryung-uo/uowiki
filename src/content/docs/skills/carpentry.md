---
title: Carpentry
description: Build furniture, instruments, and woodcraft from boards.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 11 — Str/Dex, gain Str 2.0/Dex 0.5)"
  - "servuo: Scripts/Services/Craft/DefCarpentry.cs (InitCraftList: furniture, containers, instruments, staves, training dummies, add-ons — staves are carpentry's only weapons; bows are Fletching)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = BaseFixedPoint/3, capped 420)"
  - "servuo: Scripts/Misc/SkillCheck.cs (GGSActive / CheckGGS)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/11.gif" alt="Carpentry skill banner" width="160" />

Carpentry is the woodworking [crafting skill](/playing/crafting/). The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Carpentry turns boards into furniture, containers, musical instruments, staves (its only
weapon line — quarterstaff, gnarled staff, black staff and the wild staves; bows and
crossbows belong to [Fletching](/skills/bowcraft-fletching/)), training dummies, and house
add-ons. It is the backbone craft for furnishing a [house](/playing/housing/) and supplying
bards with instruments.

## How to use it

Stock boards (from [lumberjacking](/skills/lumberjacking/)), then use carpentry tools (a saw)
to open the crafting menu and build a piece. Higher skill unlocks more complex items and
raises success and the chance of an exceptional result. See
[crafting](/playing/crafting/) and [housing](/playing/housing/).

## How to train it

**Quick start:** an NPC Carpenter teaches up to **one-third of its own skill, capped at 42.0**
(`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then make the hardest item
that still has a workable success %, stepping up as skill climbs:

- **Low skill** — craft simple items (shafts, basic furniture, instruments) for fast gains.
- **Mid/high skill** — step up to harder furniture and add-ons; exceptional pieces become
  more frequent and more valuable.

Keep a **bulk supply of boards** so a session runs uninterrupted; GGS pays out the slow late
points as long as you keep crafting the hardest thing you still succeed at. Recipe thresholds
live in `Scripts/Services/Craft/DefCarpentry.cs`. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Dexterity |
| Title | Carpenter |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +2, Dex +0.5 (per-use stat gain weights) |

Carpentry is a pure crafting skill — no active target. It is unusual among crafts in being
Strength-primary.

## Related skills & synergies

- **[Lumberjacking](/skills/lumberjacking/)** — supplies the boards.
- **[Bowcraft/Fletching](/skills/bowcraft-fletching/) + [Tinkering](/skills/tinkering/)** —
  the common companion crafts (woodcraft and tool/parts making).
- **[Musicianship](/skills/musicianship/)** — carpenters supply bards' instruments.

## See also

- [Crafting (how to play)](/playing/crafting/) · [Carpentry crafting](/crafting/carpentry/)
- [Housing](/playing/housing/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
