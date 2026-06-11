---
title: Discordance
description: Weaken a target's stats and skills with discordant music.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Skills/Discordance.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/15.gif" alt="Discordance skill banner" width="160" />

Discordance is a bard skill that debuffs a creature with jarring music. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and effect formula below are source-verified
against ServUO.

## What it does

Discordance plays disharmonious music at a target to lower its stats and combat/resistance
skills for a time, making a tough foe noticeably easier to fight or tame. It is one of the
three bard skills, and arguably the most valuable for PvM because the debuff applies to
nearly anything.

## How to use it

Equip an instrument and use Discordance, then target the creature. The attempt rolls against
the creature's difficulty (modified by [Musicianship](/skills/musicianship/)); on success the
debuff is applied for a duration. See [combat basics](/playing/combat-basics/).

## How to train it

**Train [Musicianship](/skills/musicianship/) first** — every Discord attempt rolls against
it, so it just fails until Music is high. An NPC Bard teaches Discordance up to **one-third of
its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then the universal method:
**discord the toughest target you still succeed on, repeatedly** — barding difficulty scales
with the target.

- **Low skill** — discord weak creatures with a quality instrument.
- **Mid/high skill** — discord progressively tougher creatures; harder targets keep you in the
  gain window. GGS pays out the slow late points as long as you keep using it.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Demoralizer |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Dex +0.25, Int +0.25 (per-use stat gain weights) |

From `Scripts/Skills/Discordance.cs`: the debuff magnitude is
`effect = max(-28, Discordance / -4)` — i.e. up to **−28%** to the target's stats and skills
at GM (scaling as skill/4). In PvP the effect is **halved**. [Musicianship](/skills/musicianship/)
above 100 reduces the difficulty (`diff -= (music - 100) * 0.5`), and there is roughly an
**8-second** reuse delay reduced by the mastery bonus.

## Related skills & synergies

- **[Musicianship](/skills/musicianship/) — required** for every attempt to succeed.
- **[Provocation](/skills/provocation/) + [Peacemaking](/skills/peacemaking/)** — the full
  bard trio; see the Bard build on [seven-GM templates](/templates/seven-gm/).
- **[Animal Taming](/skills/animal-taming/)** — discording a tough creature before taming
  lowers its effective difficulty.

## See also

- [Combat basics](/playing/combat-basics/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
