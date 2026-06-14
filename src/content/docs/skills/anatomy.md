---
title: Anatomy
description: Knowledge of bodies that boosts melee damage and bandage healing.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (anatomyBonus GetBonus(Anatomy,0.5,100,5) = +55% at GM)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-15
generated: false
---

<img src="/img/skill-flags/1.gif" alt="Anatomy skill banner" width="160" />

Anatomy is a passive support skill that raises melee damage and improves bandage
[healing](/skills/healing/). The prose is community-derived (paraphrased from the
uorenaissance.com skill list plus ServUO behavior) pending field verification; the stats
table and the damage-bonus note are source-verified against ServUO.

## What it does

Studying a creature's physiology lets you strike its weak points harder and tend wounds more
effectively. Anatomy adds a percentage bonus to melee damage and increases how much a
bandage restores, so it sits on nearly every warrior and bandage-medic build. It is purely
support: it has no attack or cast of its own.

## How to use it

Anatomy works two ways:

- **Passive** — once trained, the bonus applies automatically whenever you swing a melee
  weapon (see [combat basics](/playing/combat-basics/)) or apply a bandage with
  [Healing](/skills/healing/).
- **Active (training)** — use the skill and target a living creature to read its physical
  condition. This is mainly a way to grind the skill.

## How to train it

**Quick start:** buy up from an NPC Healer/Warrior trainer — a trainer teaches up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`), so pay one to ~30–42 first.

Anatomy is an active **"read"** skill — each Use targets a creature and rolls a gain check
whether you learn anything new or not:

- **Low/mid skill** — target yourself or any nearby creature and Use repeatedly; the read
  trains it cheaply without combat. Just keep clicking fresh targets.
- **Alternative / high skill** — let it climb passively while you fight with a melee weapon
  and heal between fights; it gains alongside [Tactics](/skills/tactics/) and
  [Healing](/skills/healing/). GGS guarantees the slow high-end points if you keep using it.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Biologist |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.15, Dex +0.15, Int +0.7 (per-use stat gain weights) |

In `Scripts/Items/Equipment/Weapons/BaseWeapon.cs` the melee damage bonus is computed as
`GetBonus(Anatomy, 0.500, 100.0, 5.00)` = `(Anatomy × 0.5 + 5) ÷ 100` at grandmaster — i.e.
**+55% bonus damage at 100 skill** (`Anatomy × 0.5%`, plus a flat **+5%** at the GM tier), the
companion to [Tactics](/skills/tactics/)'s +68.75%. The full melee damage stack is laid out in
[Advanced combat → Damage components](/playing/combat-advanced/#damage-components). Anatomy
also factors into bandage healing alongside [Healing](/skills/healing/).

## Related skills & synergies

- **[Tactics](/skills/tactics/) + Anatomy** — the two damage multipliers every melee build
  pairs with a weapon skill.
- **[Healing](/skills/healing/) + Anatomy** — high in both enables faster cures and
  self-resurrection with bandages.
- Featured in the Sword Dexxer and Tank Mage builds on [seven-GM templates](/templates/seven-gm/).

## See also

- [Combat basics](/playing/combat-basics/)
- [Healing](/skills/healing/) · [Tactics](/skills/tactics/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
