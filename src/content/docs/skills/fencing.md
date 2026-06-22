---
title: Fencing
description: Hit things with spears, daggers, and pointed weapons.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 42 — Fencing: Dex/Str, gain Str 0.45/Dex 0.55, title Fencer, mastery=true)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = ourSkill.BaseFixedPoint / 3, capped 420 = 42.0)"
  - "servuo: Scripts/Items/Equipment/Weapons/Kryss.cs (ArmorIgnore + InfectiousStrike), Spear.cs / Pike.cs (ArmorIgnore/ParalyzingBlow + InfectiousStrike)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/42.gif" alt="Fencing skill banner" width="160" />

Fencing is the piercing-weapon melee skill. The prose is community-derived (paraphrased from
the uorenaissance.com skill list plus ServUO behavior) pending field verification; the stats
table is source-verified against ServUO.

## What it does

Fencing governs accuracy and damage with piercing weapons — spears, kryss, daggers, war
forks, and short spears. Many fencing weapons are fast and several carry useful special moves
(armor ignore, paralyzing blow, infectious strike), making it a popular PvP weapon class. It
is a Mastery skill.

## How to use it

Equip a fencing weapon and attack a target. Damage scales with the weapon,
[Tactics](/skills/tactics/), and [Anatomy](/skills/anatomy/); special moves draw on
stamina/mana and your Mastery. See [combat basics](/playing/combat-basics/) and
[advanced combat](/playing/combat-advanced/).

## How to train it

**Quick start:** an NPC trainer who knows Fencing (a Ninja or weapon vendor) teaches up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

The universal method: **fight monsters slightly tougher than you can faceroll** so each swing
sits in your gain window, and train **Fencing + [Tactics](/skills/tactics/) +
[Anatomy](/skills/anatomy/) together** from the same fights.

- **Low skill** — fight weak creatures with a fast fencing weapon (a dagger or short spear).
- **Mid/high skill** — work up to tougher monsters; the fast swing speed of fencing weapons
  means many attempts per minute, which trains it quickly. GGS covers the slow late points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Strength |
| Title | Fencer |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Str +0.45, Dex +0.55 (per-use stat gain weights) |

Fencing is one of the four weapon skills (with [Swordsmanship](/skills/swordsmanship/),
[Mace Fighting](/skills/mace-fighting/), and [Archery](/skills/archery/)). As a Mastery skill,
high Fencing unlocks weapon mastery abilities.

## Related skills & synergies

- **Fencing + [Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/)** — the damage core.
- **[Poisoning](/skills/poisoning/)** — fencing weapons take poison well (infectious strike
  on poisoned blades is a classic combo).
- **[Healing](/skills/healing/) + [Resisting Spells](/skills/resisting-spells/)** — the
  Sword-Dexxer skeleton on [seven-GM templates](/templates/seven-gm/) (swap Fencing in for
  Swordsmanship).

## See also

- [Combat basics](/playing/combat-basics/) · [Advanced combat](/playing/combat-advanced/)
- [Weapons catalog](/items/catalog/weapons/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
