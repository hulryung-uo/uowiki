---
title: Wrestling
description: Unarmed attack and defense — a mage's best friend.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 43 — Wrestling: Str/Dex, gain Str 0.9/Dex 0.1, title Wrestler, mastery=true)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = ourSkill.BaseFixedPoint / 3, capped 420 = 42.0)"
  - "servuo: Scripts/Items/Equipment/Weapons/Fists.cs (PrimaryAbility = Disarm, SecondaryAbility = ParalyzingBlow)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/43.gif" alt="Wrestling skill banner" width="160" />

Wrestling is the unarmed combat skill — and a caster's defensive backbone. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Wrestling governs your hand-to-hand attack and, crucially, your **defensive chance to avoid
blows while empty-handed**. For a mage who carries no weapon, GM Wrestling is the shield that
keeps melee attackers from interrupting spellcasts, and it can land **disarm** and **paralyze**
special moves with bare fists. It is a Mastery skill.

## How to use it

Fight with both hands empty and you use Wrestling automatically. Damage is small, but the
defensive value (dodging hits) is the point for casters. Disarm/stun specials draw on
stamina/mana like other weapon moves. See [combat basics](/playing/combat-basics/).

## How to train it

**Quick start:** an NPC trainer who knows Wrestling teaches up to **one-third of its own
skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

Wrestling trains **unarmed** — and crucially, **while casting**: a mage keeps empty hands, so
Wrestling rises whenever you melee or are meleed, even mid-fight. The universal method:
**fight something slightly tougher than you can faceroll** so each swing is in the gain window.

- **Low skill** — punch weak creatures bare-handed; pair with [Tactics](/skills/tactics/) and
  [Anatomy](/skills/anatomy/) from the same fights.
- **High skill** — keep fighting unarmed; on a mage it climbs while you tank melee and cast,
  and fighting something that hits you trains the defensive side. GGS covers the late points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Dexterity |
| Title | Wrestler |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Str +0.9, Dex +0.1 (per-use stat gain weights) |

Wrestling is the fifth combat skill alongside the four weapon skills. Its main value is
defensive: high Wrestling reduces how often empty-handed casters get hit (and interrupted).

## Related skills & synergies

- **[Magery](/skills/magery/) + [Meditation](/skills/meditation/) +
  [Evaluating Intelligence](/skills/evaluating-intelligence/)** — Wrestling is the unarmed
  defense on the Pure Mage and Tank Mage builds; see [seven-GM templates](/templates/seven-gm/)
  and the [Mage template](/templates/mage/).
- **[Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/)** — a Tank Mage adds these to
  make its fists a real weapon.

## See also

- [Combat basics](/playing/combat-basics/) · [Advanced combat](/playing/combat-advanced/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
