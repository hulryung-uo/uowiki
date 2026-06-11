---
title: Herding
description: Direct animals to move where you point.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Items/Equipment/Weapons/ShepherdsCrook.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/20.gif" alt="Herding skill banner" width="160" />

Herding directs animals to walk to a chosen spot using a shepherd's crook. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and difficulty formula below are source-verified
against ServUO.

## What it does

Herding lets you point a creature to a location and have it move there, useful for relocating
livestock, repositioning a creature, or nudging a wild animal where you want it (for example,
into a pen or away from danger). It is a minor utility skill with occasional practical use for
ranchers and tamers.

## How to use it

Equip a shepherd's crook, use it, target the creature, then target the destination. The roll
is harder for tougher creatures. See [taming & pets](/playing/taming-and-pets/).

## How to train it

- **Low skill** — herd weak, easily-tamed animals (sheep, chickens — see the
  [animals bestiary](/bestiary/animals/)).
- **Mid/high skill** — herd progressively tougher creatures whose taming difficulty puts you
  in the gain window.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Shepherd |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +1.625, Dex +0.625, Int +0.25 (per-use stat gain weights) |

From `Scripts/Items/Equipment/Weapons/ShepherdsCrook.cs`, the herd attempt rolls
`CheckTargetSkill(Herding, creature, min, max)` where **min = creature's tame skill − 30** and
**max = tame skill + 30 + random(10)** — so a creature's herding difficulty tracks its
[taming](/skills/animal-taming/) difficulty. If your Herding already exceeds the max, the
creature taunts ("That wasn't even challenging").

## Related skills & synergies

- **[Animal Taming](/skills/animal-taming/) + [Animal Lore](/skills/animal-lore/)** — herding
  difficulty derives from tame difficulty, and tamers occasionally use it to position
  creatures.

## See also

- [Taming & pets (how to play)](/playing/taming-and-pets/)
- [Animals bestiary](/bestiary/animals/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
