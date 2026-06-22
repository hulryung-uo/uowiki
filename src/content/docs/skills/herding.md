---
title: Herding
description: Direct animals to move where you point.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 20, Herding)"
  - "servuo: Scripts/Items/Equipment/Weapons/ShepherdsCrook.cs"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/20.gif" alt="Herding skill banner" width="160" />

Herding directs animals to walk to a chosen spot using a shepherd's crook. The stats table,
herdable-target rules, and difficulty formula below are source-verified against ServUO; the
general training advice is community guidance pending field verification.

## What it does

Herding lets you point a creature to a location and have it move there, useful for relocating
livestock, repositioning a creature, or nudging a wild animal where you want it (for example,
into a pen or away from danger). It is a minor utility skill with occasional practical use for
ranchers and tamers.

## How to use it

Equip a shepherd's crook, use it, target the creature, then target the destination. The roll
is harder for tougher creatures. See [taming & pets](/playing/taming-and-pets/).

## How to train it

**Quick start:** an NPC Ranger or Rancher teaches Herding up to **one-third of its own skill,
capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

The method: **target a creature, then a destination tile, and drive it there — repeatedly.**

- **Low skill** — herd weak, easily-driven animals (sheep, chickens — see the
  [animals bestiary](/bestiary/animals/)) back and forth in a loop.
- **Mid/high skill** — herd progressively tougher creatures whose difficulty puts you in the
  gain window. GGS guarantees the slow late points as long as you keep herding.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Shepherd |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +1.625, Dex +0.625, Int +0.25 (per-use stat gain weights) |

From `Scripts/Items/Equipment/Weapons/ShepherdsCrook.cs`, only **tameable** creatures are
herdable (plus a fixed list of champ-spawn monsters); **paragons cannot be herded**, and a
creature that is already **controlled** ("That animal looks tame already") cannot. The herd
attempt rolls `CheckTargetSkill(Herding, creature, min, max)` where **min = creature's
CurrentTameSkill − 30** and **max = CurrentTameSkill + 30 + random(10)** — so a creature's
herding difficulty tracks its [taming](/skills/animal-taming/) difficulty. If your Herding
already meets or exceeds the max, the creature taunts ("That wasn't even challenging").

## Related skills & synergies

- **[Animal Taming](/skills/animal-taming/) + [Animal Lore](/skills/animal-lore/)** — herding
  difficulty derives from tame difficulty, and tamers occasionally use it to position
  creatures.

## See also

- [Taming & pets (how to play)](/playing/taming-and-pets/)
- [Animals bestiary](/bestiary/animals/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
