---
title: Throwing
description: Gargoyle ranged combat with thrown weapons.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 57 — Throwing: Dex/Str, no stat gain, title Bladeweaver, mastery=true)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = ourSkill.BaseFixedPoint / 3, capped 420 = 42.0)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseThrown.cs (MinThrowRange/MaxThrowRange, Str-scaled range capped ~11 tiles)"
  - "servuo: Scripts/Items/Equipment/Weapons/Cyclone.cs & SoulGlaive.cs (RequiredRace = Gargoyle; MinThrowRange 6 / 8)"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/57.gif" alt="Throwing skill banner" width="160" />

Throwing is the gargoyle ranged-combat skill, introduced with the Stygian Abyss expansion.
The prose is community-derived from ServUO and general UO mechanics (no uorenaissance.com
entry) pending field verification; the stats table is source-verified against ServUO.
Throwing is **gargoyle-only** — see [magic schools](/playing/magic-schools/) and
[character & stats](/playing/character-and-stats/).

## What it does

Throwing governs accuracy and damage with the gargoyle thrown weapons — the **cyclone** and
**soul glaive** — boomerang-like weapons that fly out and return. Each thrown weapon has a
**minimum throw range** (cyclone 6 tiles, soul glaive 8 tiles per `Cyclone.cs`/`SoulGlaive.cs`)
and a maximum range that grows with Strength, capped around 11 tiles (`BaseThrown.cs`), so
there is an effective-distance band: standing too close to the target reduces the throw.
Throwing weapons also carry weapon special moves (the cyclone's Moving Shot and Infused
Throw). It is the gargoyle answer to [Archery](/skills/archery/) and a Mastery skill.

## How to use it

Only a **gargoyle** character can use thrown weapons. Equip a cyclone or soul glaive and
attack a target at range; mind the optimal distance. Damage scales with the weapon,
[Tactics](/skills/tactics/), and [Anatomy](/skills/anatomy/). See
[combat basics](/playing/combat-basics/) and [advanced combat](/playing/combat-advanced/).

## How to train it

**Quick start (gargoyle skill):** the SA trainer NPC who knows Throwing teaches up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first if you can find
one (Throwing is a Stygian Abyss skill with few trainers).

The universal method: **fight monsters slightly tougher than you can faceroll** so each throw
sits in your gain window, and train **Throwing + [Tactics](/skills/tactics/) +
[Anatomy](/skills/anatomy/) together**.

- **Low skill** — throw at weak creatures from range.
- **Mid/high skill** — fight tougher monsters at the weapon's effective range (stay outside
  the minimum throw range); gains come from combat, and GGS covers the slow late points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Strength |
| Title | Bladeweaver |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Throwing-weapon implementations live under `Scripts/Items/Equipment/Weapons/` (`BaseThrown.cs`,
`Cyclone.cs`, `SoulGlaive.cs`). Both throwing weapons set `RequiredRace = Race.Gargoyle`, so
they are gargoyle-only. Max range scales with Strength: `Range = BaseRange + ((Str −
StrReq) / ((140 − StrReq) / 3))`, capped at 11 tiles (`BaseThrown.cs`).

## Related skills & synergies

- **[Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/)** — the damage core for any
  ranged gargoyle warrior.
- **[Bushido](/skills/bushido/) / [Chivalry](/skills/chivalry/)** — Mastery schools that
  layer onto a throwing gargoyle.

## See also

- [Combat basics](/playing/combat-basics/) · [Character & stats](/playing/character-and-stats/)
- [Weapons catalog](/items/catalog/weapons/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
