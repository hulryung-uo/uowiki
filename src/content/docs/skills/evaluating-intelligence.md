---
title: Evaluating Intelligence
description: Scale offensive spell damage and read targets' Int.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo id 16)"
  - "servuo: Scripts/Skills/EvalInt.cs"
  - "servuo: Scripts/Spells/Base/Spell.cs (GetNewAosDamage, GetDamageFixed, DamageSkill)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills)"
  - "servuo: Scripts/Misc/SkillCheck.cs (TryStatGain, ML stat-gain path)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
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

Eval Int is an active **"read"** skill (`Scripts/Skills/EvalInt.cs`). You can target anything,
but only a Mobile (creature/player) gives a usable reading — the active skill check is
`CheckTargetSkill(EvalInt, target, 0.0, 120.0)`, so any living creature in range (8 tiles)
trains it. Accuracy improves with skill: the reading's margin of error is
`max(0, 20 − EvalInt/5)`, and the target's **mana** reading only appears once your Eval Int
**base is 76.0 or higher**.

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
| Gain notes | on a skill-up, the standard ML stat-gain roll favors **Int** (primary) then **Str** (secondary) |

On our EJ shard (`Core.ML`), a skill-up rolls the standard stat-gain mechanic
(`Scripts/Misc/SkillCheck.cs`, `TryStatGain`): a flat ~5% chance, then the **primary** stat
(Int) is favored ~3:1 over the **secondary** (Str). The per-skill gain weights in
`Server/Skills.cs` only applied on the pre-ML mechanic.

Eval Int is the magery analogue of [Anatomy](/skills/anatomy/)/[Tactics](/skills/tactics/)
for melee: it is the primary multiplier on spell damage. On our AOS/EJ shard the scaling is in
`Scripts/Spells/Base/Spell.cs` (`GetNewAosDamage`): base spell damage is multiplied by
`evalScale = 30 + (9 × EvalInt) / 100` percent — i.e. **30%** with no Eval Int up to **120%**
at GM (100.0). So GM Eval Int roughly **quadruples** the base damage versus an untrained caster.
A separate flat **damage bonus** is then added from `Caster.Int/10`, Inscription
(`scribeBonus`), and Spell Damage Increase. Eval Int is the `DamageSkill` for Magery spells
(`GetDamageFixed` reads `Skills[EvalInt]`).

## Related skills & synergies

- **[Magery](/skills/magery/) + Eval Int** — the inseparable mage damage core.
- **[Meditation](/skills/meditation/) + [Inscription](/skills/inscription/) +
  [Resisting Spells](/skills/resisting-spells/)** — round out the Pure Mage on
  [seven-GM templates](/templates/seven-gm/) and the [Mage template](/templates/mage/).

## See also

- [Spellcasting (how to play)](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
