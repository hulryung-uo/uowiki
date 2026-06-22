---
title: Meditation
description: Recover mana faster, actively and passively.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 46: Int primary / Str secondary, Stoic, no stat gain, not mastery)"
  - "servuo: Scripts/Skills/Meditation.cs (OnUse: chance = (50 + (skill - missingMana)*2)/100; CheckSkill 0-100; armor blocks via RegenRates.GetArmorOffset > 0, msg 500135)"
  - "servuo: Scripts/Misc/RegenRates.cs (GetArmorOffset / medable-armor rule)"
  - "servuo: Scripts/Mobiles/NPCs/Mage.cs (Meditation trainer); Scripts/Mobiles/Normal/BaseCreature.cs (baseToSet = BaseFixedPoint/3, capped 42.0)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/46.gif" alt="Meditation skill banner" width="160" />

Meditation speeds mana regeneration. The prose is community-derived (paraphrased from the
uorenaissance.com skill list plus ServUO behavior) pending field verification; the stats
table and active-check formula below are source-verified against ServUO.

## What it does

Meditation refills your mana faster — **actively**, by entering a meditative trance for a
burst of regen, and **passively**, by raising your background mana regen at all times. It is
near-mandatory on any [Magery](/skills/magery/)-based caster who wants to keep casting. See
[meditation & mana](/playing/meditation-and-mana/).

## How to use it

- **Active** — use the skill to enter meditation. While meditating, mana regenerates quickly;
  taking damage or acting breaks it.
- **Passive** — once trained, it boosts regen automatically, **but only while wearing
  little/no non-medable (metal) armor** — the "medable armor" rule. Non-medable armor blocks
  the mana-regen bonus, and trying to *actively* meditate in it is refused outright
  ("Regenative forces cannot penetrate your armor!" — the in-game string is misspelled).

## How to train it

**Quick start:** an NPC Mage teaches Meditation up to **one-third of its own skill, capped at
42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

The active-meditation skill check fires on each Use (`Scripts/Skills/Meditation.cs`,
`CheckSkill(Meditation, 0.0, 100.0)`), so the loop is **drain mana, then meditate it back**:

- **Low/mid skill** — cast spells to spend mana, then Use Meditation to recover it, over and
  over. Meditating with the most empty mana pool gives the best check.
- **High skill** — keep the spend-then-meditate loop going; GGS guarantees the slow late
  points as long as you keep meditating.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Stoic |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

From `Scripts/Skills/Meditation.cs`: the active-meditation success chance is
`(50 + (skill − missingMana) × 2) / 100` — so a higher skill (and less mana missing) is more
likely to enter the trance. Metal armor blocks the regen entirely. The skill check runs
`CheckSkill(Meditation, 0.0, 100.0)`.

## Related skills & synergies

- **[Magery](/skills/magery/) + [Evaluating Intelligence](/skills/evaluating-intelligence/)**
  — the caster core; Meditation refunds the mana. See the Pure Mage build on
  [seven-GM templates](/templates/seven-gm/) and the [Mage template](/templates/mage/).
- **[Focus](/skills/focus/)** — stacks with Meditation and keeps regenerating in metal armor.

## See also

- [Meditation & mana (how to play)](/playing/meditation-and-mana/) · [Spellcasting](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
