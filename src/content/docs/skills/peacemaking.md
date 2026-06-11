---
title: Peacemaking
description: Calm aggression with music — yours or the whole area's.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 9)"
  - "servuo: Scripts/Skills/Peacemaking.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/9.gif" alt="Peacemaking skill banner" width="160" />

Peacemaking is a bard skill that soothes aggression with music. The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table and cooldown notes below are source-verified against ServUO.

## What it does

Peacemaking calms creatures so they stop attacking. In **targeted** mode it pacifies a single
creature; in **area** mode it quiets every eligible foe around you, interrupting their attacks
and buying breathing room. It is one of the three bard skills and a strong panic button and
crowd-control tool. See [combat basics](/playing/combat-basics/).

## How to use it

Equip an instrument and use Peacemaking. Choose to target one creature, or play an area peace
to calm the room. A successful [Musicianship](/skills/musicianship/) play is required first,
then the Peacemaking roll lands the effect.

## How to train it

**Train [Musicianship](/skills/musicianship/) first** — every Peace attempt rolls against it,
so it just fails until Music is high. An NPC Bard teaches Peacemaking up to **one-third of its
own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then the universal method:
**peace the toughest target you still succeed on, repeatedly** — barding difficulty scales
with the target.

- **Low skill** — peace weak creatures with a quality instrument.
- **Mid/high skill** — peace tougher creatures; harder targets keep you in the gain window.
  GGS pays out the slow late points as long as you keep using it.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Pacifier |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

From `Scripts/Skills/Peacemaking.cs`: the target check is
`CheckTargetSkill(Peacemaking, target, diff − 25, diff + 25)`. The reuse delay is roughly
**10 seconds** (reduced by the mastery bonus), and area peace has its own short cooldown.
Some creatures are flagged `AreaPeaceImmune` and cannot be area-pacified.

## Related skills & synergies

- **[Musicianship](/skills/musicianship/) — required** for every attempt.
- **[Provocation](/skills/provocation/) + [Discordance](/skills/discordance/)** — the full
  bard trio; see the Bard build on [seven-GM templates](/templates/seven-gm/).

## See also

- [Combat basics](/playing/combat-basics/)
- [Instruments catalog](/items/catalog/instruments/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
