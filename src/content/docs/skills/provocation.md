---
title: Provocation
description: Goad monsters into fighting each other.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo id 22)"
  - "servuo: Scripts/Skills/Provocation.cs"
  - "servuo: Scripts/Items/Equipment/Instruments/BaseInstrument.cs (CheckMusicianship, GetDifficultyFor, GetBardRange)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills, Unprovokable)"
  - "servuo: Scripts/Misc/SkillCheck.cs (TryStatGain, ML stat-gain path)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/22.gif" alt="Provocation skill banner" width="160" />

Provocation is a bard skill that turns monsters against each other. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and difficulty/cooldown notes below are
source-verified against ServUO.

## What it does

Provocation plays music to enrage one creature into attacking another. A skilled bard can
walk into a dungeon and make the monsters kill each other, taking no risk and earning the
loot. It is the most powerful PvM bard skill and a Mastery skill. See
[combat basics](/playing/combat-basics/).

## How to use it

Equip an instrument and use Provocation. Target the creature you want to enrage, then target
the creature you want it to attack. A successful [Musicianship](/skills/musicianship/) play is
required, then the Provocation roll decides whether it works. The two creatures must be
hostile-able to each other.

## How to train it

**Train [Musicianship](/skills/musicianship/) first** — every Provoke attempt rolls against
it, so it just fails until Music is high. An NPC Bard teaches Provocation up to **one-third of
its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then the universal method:
**provoke the toughest pair you still succeed on, repeatedly** — barding difficulty scales
with the targets.

- **Low skill** — provoke pairs of weak creatures against each other.
- **Mid/high skill** — provoke progressively tougher pairs; the combined difficulty of the two
  targets sets the gain window. GGS pays out the slow late points as long as you keep using it.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Rouser |
| Mastery skill | Yes |
| Gain notes | on a skill-up, the standard ML stat-gain roll favors **Int** (primary) then **Dex** (secondary) |

On our EJ shard (`Core.ML`), a skill-up rolls the standard stat-gain mechanic
(`Scripts/Misc/SkillCheck.cs`, `TryStatGain`): a flat ~5% chance, then the **primary** stat
(Int) is favored ~3:1 over the **secondary** (Dex). Provocation's `DexGain`/`IntGain` weights
in `Server/Skills.cs` (4.5 / 0.5) only applied on the *pre-ML* mechanic and do not govern
gains on this shard.

From `Scripts/Skills/Provocation.cs`: the difficulty is the **average of both creatures'**
instrument difficulty, minus 5 — `diff = ((GetDifficultyFor(A) + GetDifficultyFor(B)) × 0.5) − 5`
— and the check is `CheckTargetSkill(Provocation, target, diff − 25, diff + 25)`.
[Musicianship](/skills/musicianship/) above 100 subtracts `(music − 100) × 0.5` from the
difficulty, and the mastery bonus reduces it further. Both targets must be within bard range
(`8 + Provocation/15` tiles) of each other. The reuse delay is **10 seconds** (reduced by the
mastery bonus). Controlled pets, `Unprovokable` creatures, and paragons of base difficulty
≥ 160 cannot be provoked.

## Related skills & synergies

- **[Musicianship](/skills/musicianship/) — required** for every attempt.
- **[Peacemaking](/skills/peacemaking/) + [Discordance](/skills/discordance/)** — the full
  bard trio; see the Bard build on [seven-GM templates](/templates/seven-gm/).

## See also

- [Combat basics](/playing/combat-basics/)
- [Instruments catalog](/items/catalog/instruments/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
