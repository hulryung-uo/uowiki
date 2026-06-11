---
title: Provocation
description: Goad monsters into fighting each other.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 22)"
  - "servuo: Scripts/Skills/Provocation.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
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

- **Low skill** — provoke pairs of weak creatures against each other.
- **Mid/high skill** — provoke progressively tougher pairs; the combined difficulty of the
  two targets sets the gain window. High [Musicianship](/skills/musicianship/) is mandatory.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Rouser |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Dex +0.45, Int +0.05 (per-use stat gain weights) |

From `Scripts/Skills/Provocation.cs`: the difficulty is the **average of both creatures'**
instrument difficulty, minus 5 — `diff = ((diff(A) + diff(B)) × 0.5) − 5` — and the check is
`CheckTargetSkill(Provocation, target, diff − 25, diff + 25)`. [Musicianship](/skills/musicianship/)
above 100 subtracts `(music − 100) × 0.5` from the difficulty. The reuse delay is about
**10 seconds** (reduced by the mastery bonus).

## Related skills & synergies

- **[Musicianship](/skills/musicianship/) — required** for every attempt.
- **[Peacemaking](/skills/peacemaking/) + [Discordance](/skills/discordance/)** — the full
  bard trio; see the Bard build on [seven-GM templates](/templates/seven-gm/).

## See also

- [Combat basics](/playing/combat-basics/)
- [Instruments catalog](/items/catalog/instruments/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
