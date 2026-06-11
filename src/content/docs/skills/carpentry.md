---
title: Carpentry
description: Build furniture, instruments, and woodcraft from boards.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Services/Craft/DefCarpentry.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/11.gif" alt="Carpentry skill banner" width="160" />

Carpentry is the woodworking [crafting skill](/playing/crafting/). The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Carpentry turns boards into furniture, containers, musical instruments, staves and bows
(some shared with [Fletching](/skills/bowcraft-fletching/)), training dummies, and house
add-ons. It is the backbone craft for furnishing a [house](/playing/housing/) and supplying
bards with instruments.

## How to use it

Stock boards (from [lumberjacking](/skills/lumberjacking/)), then use carpentry tools (a saw)
to open the crafting menu and build a piece. Higher skill unlocks more complex items and
raises success and the chance of an exceptional result. See
[crafting](/playing/crafting/) and [housing](/playing/housing/).

## How to train it

- **Low skill** — craft simple items (shafts, basic furniture, instruments) for fast gains.
- **Mid/high skill** — step up to harder furniture and add-ons; exceptional pieces become
  more frequent and more valuable.

Recipe thresholds live in `Scripts/Services/Craft/DefCarpentry.cs`. See
[skill gain](/mechanics/skill-gain/).

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
