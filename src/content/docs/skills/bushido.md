---
title: Bushido
description: Samurai stances and warrior techniques.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 52: Str primary / Int secondary, Samurai, mastery)"
  - "servuo: Scripts/Spells/Bushido/SamuraiSpell.cs (CastSkill=Bushido, RequiredSkill/RequiredMana, ScaleMana)"
  - "servuo: Scripts/Spells/Bushido/ (Confidence, CounterAttack, Evasion, HonorableExecution, LightningStrike, MomentumStrike)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = BaseFixedPoint/3, capped 42.0)"
  - "servuo: Scripts/Mobiles/NPCs/Hamato.cs + Samurai.cs (Bushido trainers)"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/52.gif" alt="Bushido skill banner" width="160" />

Bushido is the samurai combat school, an expansion-era (Samurai Empire) skill. The prose is
community-derived from ServUO and general UO mechanics (no uorenaissance.com entry) pending
field verification; the stats table is source-verified against ServUO. Some behavior is
expansion-specific — see [magic schools](/playing/magic-schools/).

## What it does

Bushido grants a set of melee combat abilities — defensive stances and counterattacks
(Confidence, Counter Attack, Evasion), and finishing strikes (Honorable Execution, Lightning
Strike, Momentum Strike) — that trigger or are activated during melee. Its effects scale with
your equipped weapon skill and the ability used, rewarding a disciplined, defensive fighting
style.

## How to use it

Bushido abilities are activated from the Bushido spellbook/abilities and consume mana, then
apply on your next swing or as a stance. You fight with a normal weapon
([Swordsmanship](/skills/swordsmanship/), [Fencing](/skills/fencing/), etc.) and weave the
abilities in. See [combat basics](/playing/combat-basics/),
[advanced combat](/playing/combat-advanced/), and [magic schools](/playing/magic-schools/).

## How to train it

**Quick start:** an NPC Samurai (Hamato, or a Samurai trainer in the Tokuno towns) teaches
Bushido up to **one-third of its own skill, capped at 42.0**
(`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

Bushido rises from **using its abilities in combat**, so an active samurai fighting style
trains it:

- **Low skill** — toggle the cheaper stances/abilities (Confidence, Evasion) and fight weak
  creatures so each ability fires.
- **Mid/high skill** — keep activating abilities every fight against tougher foes; harder
  fights hold the gain window, and GGS pays out the slow late points. Some specifics are
  **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Intelligence |
| Title | Samurai |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Bushido ability implementations live under `Scripts/Spells/Bushido/`. As a Mastery skill,
high Bushido also enables weapon mastery effects. Exact damage/stance numbers are
expansion-specific and **unverified** here.

## Related skills & synergies

- **A weapon skill + [Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/)** — Bushido is
  layered onto a normal melee core.
- **[Parrying](/skills/parrying/)** — pairs with Bushido's defensive stances (sword-and-board
  samurai).
- **[Chivalry](/skills/chivalry/)** — the classic paladin/samurai hybrid pairs both schools.

## See also

- [Magic schools](/playing/magic-schools/) · [Advanced combat](/playing/combat-advanced/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
