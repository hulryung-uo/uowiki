---
title: Archery
description: Strike from range with bows and crossbows.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/31.gif" alt="Archery skill banner" width="160" />

Archery is the ranged weapon skill, governing accuracy and damage with bows and crossbows.
The prose is community-derived (paraphrased from the uorenaissance.com skill list plus ServUO
behavior) pending field verification; the stats table is source-verified against ServUO.

## What it does

Archery is the ranged counterpart to the melee weapon skills. It determines your chance to
hit and your damage with bows, crossbows, and heavy crossbows, letting you open fights from a
distance and kite faster-than-you enemies. It is a Mastery skill, so high Archery unlocks
weapon mastery abilities.

## How to use it

Equip a bow or crossbow and ammunition (arrows for bows, bolts for crossbows), then attack a
target. You need line of sight and you must stand still to fire effectively — moving
interrupts the shot. Damage scales with the weapon, [Tactics](/skills/tactics/), and
[Anatomy](/skills/anatomy/). See [combat basics](/playing/combat-basics/).

## How to train it

**Quick start:** an NPC trainer who knows Archery (a Ranger or weapon vendor) teaches up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

The universal method: **fight monsters slightly tougher than you can faceroll** so each shot
sits in your gain window, and train **Archery + [Tactics](/skills/tactics/) +
[Anatomy](/skills/anatomy/) together** — all three rise from the same fights.

- **Low skill** — shoot weak creatures (or train-dummy archery butts where available) from
  range, keeping ammo stocked.
- **Mid/high skill** — fight progressively tougher monsters; pair with a
  [Fletcher](/skills/bowcraft-fletching/) to keep your own ammunition and bows supplied. GGS
  covers the slow late points as long as you keep shooting.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Strength |
| Title | Archer |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Str +0.25, Dex +0.75 (per-use stat gain weights) |

As a Dexterity-primary skill, Archery benefits from high Dex (faster swing/recovery). It is
one of the four weapon skills (with [Swordsmanship](/skills/swordsmanship/),
[Mace Fighting](/skills/mace-fighting/), and [Fencing](/skills/fencing/)).

## Related skills & synergies

- **Archery + [Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/)** — the damage core
  for any ranged warrior.
- **[Bowcraft/Fletching](/skills/bowcraft-fletching/)** — self-supply bows and ammo.
- **[Hiding](/skills/hiding/) + [Stealth](/skills/stealth/)** — the Stealth Archer build on
  [seven-GM templates](/templates/seven-gm/) opens fights from concealment.

## See also

- [Combat basics](/playing/combat-basics/) · [Advanced combat](/playing/combat-advanced/)
- [Weapons catalog](/items/catalog/weapons/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
