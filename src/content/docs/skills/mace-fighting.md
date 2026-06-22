---
title: Mace Fighting
description: Hit things with maces, mauls, and staves.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 41 — Mace Fighting: Str/Dex, gain Str 0.9/Dex 0.1, title Armsman, mastery=true)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = ourSkill.BaseFixedPoint / 3, capped 420 = 42.0)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseBashing.cs (OnHit drains 3-5 stamina); WarMace.cs (CrushingBlow), Maul.cs (ConcussionBlow)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/41.gif" alt="Mace Fighting skill banner" width="160" />

Mace Fighting is the blunt-weapon melee skill. The prose is community-derived (paraphrased
from the uorenaissance.com skill list plus ServUO behavior) pending field verification; the
stats table is source-verified against ServUO.

## What it does

Mace Fighting governs accuracy and damage with blunt weapons — maces, war maces, mauls,
hammers, and staves. On every hit a mace-class weapon drains **3-5 points of an opponent's
stamina** (`BaseBashing.OnHit`), and several carry strong special moves (the War Mace's
crushing blow, the Maul's concussion blow), making them a punishing PvP weapon class. It is
a Mastery skill.

## How to use it

Equip a mace-class weapon and attack. Damage scales with the weapon,
[Tactics](/skills/tactics/), and [Anatomy](/skills/anatomy/); staves can be wielded with
two hands or paired with a [shield](/skills/parrying/) depending on the weapon. See
[combat basics](/playing/combat-basics/) and [advanced combat](/playing/combat-advanced/).

## How to train it

**Quick start:** an NPC trainer who knows Mace Fighting (a Ninja or weapon vendor) teaches up
to **one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

The universal method: **fight monsters slightly tougher than you can faceroll** so each swing
sits in your gain window, and train **Mace Fighting + [Tactics](/skills/tactics/) +
[Anatomy](/skills/anatomy/) together** from the same fights.

- **Low skill** — fight weak creatures with a fast mace.
- **Mid/high skill** — work up to tougher monsters; the per-hit stamina drain makes maces
  good for shutting down a target's swing speed. GGS covers the slow late points as long as
  you keep swinging.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Dexterity |
| Title | Armsman |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Str +0.9, Dex +0.1 (per-use stat gain weights) |

Mace Fighting is one of the four weapon skills (with
[Swordsmanship](/skills/swordsmanship/), [Fencing](/skills/fencing/), and
[Archery](/skills/archery/)). As a Mastery skill, high Mace Fighting unlocks weapon mastery
abilities.

## Related skills & synergies

- **Mace Fighting + [Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/)** — the damage
  core.
- **[Parrying](/skills/parrying/) + [Healing](/skills/healing/) +
  [Resisting Spells](/skills/resisting-spells/)** — sword-and-board dexxer; swap Mace Fighting
  in for Swordsmanship on [seven-GM templates](/templates/seven-gm/).

## See also

- [Combat basics](/playing/combat-basics/) · [Advanced combat](/playing/combat-advanced/)
- [Weapons catalog](/items/catalog/weapons/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
