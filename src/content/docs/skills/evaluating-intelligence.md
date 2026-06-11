---
title: Evaluating Intelligence
description: Scale offensive spell damage and read targets' Int.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Skills/EvalInt.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/16.gif" alt="Evaluating Intelligence skill banner" width="160" />

Evaluating Intelligence (Eval Int) is the mage's offensive damage skill. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Eval Int raises the damage of your offensive [Magery](/skills/magery/) spells — the higher it
is, the harder your fireballs, energy bolts, and explosions hit. It can also read a target's
Intelligence and mana. It is a near-mandatory support skill on any battle mage. See
[spellcasting](/playing/spellcasting/).

## How to use it

- **Passive** — the damage bonus applies automatically whenever you cast a damaging Magery
  spell.
- **Active (training)** — use the skill and target a creature to gauge its Int/mana.

## How to train it

**Quick start:** an NPC Mage teaches Eval Int up to **one-third of its own skill, capped at
42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

Eval Int is an active **"read"** skill, but note it only targets things you *could cast on* —
a living creature, not an item.

- **Low/mid skill** — Use it on creatures to read their Int repeatedly; a tethered or weak
  monster is an endless target. Or simply cast damage spells in combat, where it climbs
  alongside Magery (it scales your spell damage).
- **High skill** — let it ride in combat; harder fights keep both Magery and Eval Int gaining,
  and GGS pays out the slow late points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Scholar |
| Mastery skill | No |
| Gain notes | skill-ups can raise Int +1 (per-use stat gain weights) |

Eval Int is the magery analogue of [Anatomy](/skills/anatomy/)/[Tactics](/skills/tactics/)
for melee: it is the primary multiplier on spell damage. Implementation in
`Scripts/Skills/EvalInt.cs`; the damage scaling is applied in the spell/`SpellHelper` damage
math.

## Related skills & synergies

- **[Magery](/skills/magery/) + Eval Int** — the inseparable mage damage core.
- **[Meditation](/skills/meditation/) + [Inscription](/skills/inscription/) +
  [Resisting Spells](/skills/resisting-spells/)** — round out the Pure Mage on
  [seven-GM templates](/templates/seven-gm/) and the [Mage template](/templates/mage/).

## See also

- [Spellcasting (how to play)](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
