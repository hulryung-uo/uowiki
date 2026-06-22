---
title: Discordance
description: Weaken a target's stats and skills with discordant music.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo id 15)"
  - "servuo: Scripts/Skills/Discordance.cs"
  - "servuo: Scripts/Items/Equipment/Instruments/BaseInstrument.cs (CheckMusicianship, GetDifficultyFor, GetBaseDifficulty, GetBardRange)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills)"
  - "servuo: Scripts/Misc/SkillCheck.cs (TryStatGain, ML stat-gain path)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/15.gif" alt="Discordance skill banner" width="160" />

Discordance is a bard skill that debuffs a creature with jarring music. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and effect formula below are source-verified
against ServUO.

## What it does

Discordance plays disharmonious music at a target to lower its resistances and skills for a
time, making a tough foe noticeably easier to fight or tame. (On our AOS/EJ shard the debuff
is applied as resistance and skill penalties; the older pre-AOS version lowered raw Str/Dex/Int
instead — see `Scripts/Skills/Discordance.cs`.) It is one of the three bard skills, and
arguably the most valuable for PvM because the debuff applies to nearly anything that isn't
bard-immune.

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
| Gain notes | on a skill-up, the standard ML stat-gain roll favors **Dex** (primary) then **Int** (secondary) |

On our EJ shard (`Core.ML`), stat gain on a skill-up is the standard mechanic
(`Scripts/Misc/SkillCheck.cs`, `TryStatGain`): a flat ~5% chance, then the skill's **primary**
stat (Dex) is chosen ~3:1 over its **secondary** (Int) when both are set to rise. The
per-skill `StrGain`/`DexGain`/`IntGain` weights in `Server/Skills.cs` only matter on the
pre-ML mechanic and do not apply here.

From `Scripts/Skills/Discordance.cs` (AOS path): the debuff magnitude is
`effect = max(-28, Discordance / -4)` — i.e. up to **−28%** to the target's resistances and
skills at GM (scaling as skill/4). The effect is **halved against very tough creatures**
(base barding difficulty ≥ 160), not in PvP. [Musicianship](/skills/musicianship/) above 100
reduces the difficulty (`diff -= (music - 100) * 0.5`), the base difficulty already gets a flat
`-10`, and an Exceptional or matching-slayer instrument lowers it further
(`GetDifficultyFor`). The reuse delay is **8 seconds**, reduced by the Discordance mastery
bonus (`8000 - (masteryBonus/5)*1000` ms). The bard must stay alive, visible, and within
bard range (`8 + Discordance/15` tiles) or the discord ends after 15 seconds.

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
