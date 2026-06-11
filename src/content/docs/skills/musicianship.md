---
title: Musicianship
description: The base instrument skill behind all barding.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 29)"
  - "servuo: Scripts/Items/Equipment/Instruments/BaseInstrument.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/29.gif" alt="Musicianship skill banner" width="160" />

Musicianship is the base instrument skill that gates every bard ability. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Musicianship is how well you play an instrument — and it is the prerequisite check for all
three bard skills: [Peacemaking](/skills/peacemaking/), [Provocation](/skills/provocation/),
and [Discordance](/skills/discordance/). If the Musicianship check fails, the barding attempt
fails before its own roll even happens, so bards GM it first. High Musicianship (above 100,
on quality instruments) also reduces the difficulty of the bard skills themselves.

## How to use it

Equip an instrument and play it (use the instrument). Each play is a Musicianship check. In
combat, the bard skills automatically require a successful Musicianship play to land. See
[combat basics](/playing/combat-basics/).

## How to train it

- **Low/high skill** — simply play an instrument repeatedly. It needs no target and trains
  passively, so most bards max it before touching the active bard skills.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Bard |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +0.8, Int +0.2 (per-use stat gain weights) |

Instrument quality and a Musicianship value above 100 lower the effective difficulty of the
bard skills — e.g. in `Scripts/Skills/Discordance.cs` and `Provocation.cs`, music above 100
subtracts `(music − 100) × 0.5` from the difficulty. Instruments also have charges/condition
(`BaseInstrument.cs`).

## Related skills & synergies

- **The bard trio** — [Peacemaking](/skills/peacemaking/),
  [Provocation](/skills/provocation/), and [Discordance](/skills/discordance/) all depend on
  Musicianship; see the Bard build on [seven-GM templates](/templates/seven-gm/).
- **[Carpentry](/skills/carpentry/)** — crafts the instruments bards play.

## See also

- [Combat basics](/playing/combat-basics/)
- [Instruments catalog](/items/catalog/instruments/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
