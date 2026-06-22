---
title: Musicianship
description: The base instrument skill behind all barding.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo id 29)"
  - "servuo: Scripts/Items/Equipment/Instruments/BaseInstrument.cs (CheckMusicianship, GetDifficultyFor, GetBardRange, UsesRemaining)"
  - "servuo: Scripts/Skills/Discordance.cs / Peacemaking.cs / Provocation.cs (music-difficulty reduction)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills)"
  - "servuo: Scripts/Misc/SkillCheck.cs (TryStatGain, ML stat-gain path)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
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

**Quick start:** an NPC Bard teaches Musicianship up to **one-third of its own skill, capped
at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

- **Low/high skill** — simply **play an instrument** (Use it, no target needed) over and over.
  It trains with no target, so **most bards GM Musicianship first** — every active bard skill
  ([Discordance](/skills/discordance/), [Peacemaking](/skills/peacemaking/),
  [Provocation](/skills/provocation/)) rolls against it, so they fail until it's high. GGS
  pays out the slow late points as long as you keep playing.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Bard |
| Mastery skill | No |
| Gain notes | on a skill-up, the standard ML stat-gain roll favors **Dex** (primary) then **Int** (secondary) |

Each play is a `CheckMusicianship` roll (`BaseInstrument.cs`): the chance to play well is simply
`Musicianship.Value / 100`, so at GM you essentially always succeed and a bard skill never
fails on the music step. On a skill-up, the standard ML stat-gain mechanic
(`Scripts/Misc/SkillCheck.cs`, `TryStatGain`) gives a flat ~5% chance, then favors the
**primary** stat (Dex) ~3:1 over the **secondary** (Int); the per-skill `DexGain`/`IntGain`
weights only mattered on the pre-ML mechanic.

Instrument quality and a Musicianship value above 100 lower the effective difficulty of the
bard skills — in `Scripts/Skills/Discordance.cs`, `Peacemaking.cs`, and `Provocation.cs`,
music above 100 subtracts `(music − 100) × 0.5` from the difficulty, and an Exceptional or
matching-slayer instrument lowers it further (`GetDifficultyFor`). Bard range also scales with
the bard skill: `8 + skill/15` tiles (`GetBardRange`). Instruments carry limited
charges/uses that are consumed per attempt (`UsesRemaining` / `ConsumeUse` in
`BaseInstrument.cs`).

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
