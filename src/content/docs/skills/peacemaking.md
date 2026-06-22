---
title: Peacemaking
description: Calm aggression with music — yours or the whole area's.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo id 9)"
  - "servuo: Scripts/Skills/Peacemaking.cs"
  - "servuo: Scripts/Items/Equipment/Instruments/BaseInstrument.cs (CheckMusicianship, GetDifficultyFor, GetBardRange)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills, Uncalmable / AreaPeaceImmune)"
  - "servuo: Scripts/Misc/SkillCheck.cs (TryStatGain, ML stat-gain path)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
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
| Gain notes | on a skill-up, the standard ML stat-gain roll favors **Int** (primary) then **Dex** (secondary) |

On our EJ shard (`Core.ML`), a skill-up rolls the standard stat-gain mechanic
(`Scripts/Misc/SkillCheck.cs`, `TryStatGain`): a flat ~5% chance, then the **primary** stat
(Int) is favored ~3:1 over the **secondary** (Dex). Peacemaking's zero `DexGain`/`IntGain`
weights in `Server/Skills.cs` only suppressed gains on the *pre-ML* mechanic, so the earlier
"no stat gain" note does not apply on this shard.

From `Scripts/Skills/Peacemaking.cs`, there are two modes:

- **Targeted** (target another creature): rolls
  `CheckTargetSkill(Peacemaking, target, diff − 25, diff + 25)` where
  `diff = instrument.GetDifficultyFor(target) − 10`, further reduced by `(music − 100) × 0.5`
  above 100 Musicianship and by the mastery bonus. On success the creature is pacified for
  `seconds = clamp(100 − diff/1.5, 10, 120)`. Reuse delay **5s** on success, **10s** on a fail
  (each reduced by the mastery bonus). `Uncalmable` creatures can never be calmed.
- **Area** (target yourself): a single `CheckSkill(Peacemaking, 0, 120)` (no per-target
  difficulty) calms every eligible foe in bard range (`8 + Peacemaking/15` tiles) for ~1
  second. Reuse delay **5s** on success, **10s** on a fail. Creatures flagged
  `Uncalmable` or `AreaPeaceImmune` are skipped. A successful Musicianship play is required
  in both modes.

## Related skills & synergies

- **[Musicianship](/skills/musicianship/) — required** for every attempt.
- **[Provocation](/skills/provocation/) + [Discordance](/skills/discordance/)** — the full
  bard trio; see the Bard build on [seven-GM templates](/templates/seven-gm/).

## See also

- [Combat basics](/playing/combat-basics/)
- [Instruments catalog](/items/catalog/instruments/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
