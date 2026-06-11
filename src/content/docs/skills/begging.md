---
title: Begging
description: Ask NPCs for spare coin and small goods.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Skills/Begging.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/6.gif" alt="Begging skill banner" width="160" />

Begging solicits gold or trinkets from NPCs. The prose is community-derived (paraphrased from
the uorenaissance.com skill list plus ServUO behavior) pending field verification; the
amounts and skill check below are source-verified against ServUO.

## What it does

Begging is a minor, flavorful social skill: you plead with a townsperson or merchant NPC for
a handout. The payoff is small — a few coins, or occasionally a trinket reward — so it is
played more for roleplay and completionism than profit.

## How to use it

Activate the skill and target an NPC. If the roll succeeds and they pity you, they hand over
a little gold (or, rarely, a small reward item). See
[vendors & banking](/playing/vendors-and-banking/) and
[communication & social](/playing/communication-and-social/).

## How to train it

- **Low/high skill** — beg from town NPCs repeatedly. There is a per-use cooldown, so
  Begging is slow to raise; just keep targeting fresh NPCs around a busy town.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Beggar |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

From `Scripts/Skills/Begging.cs`:

- The check is `CheckTargetSkill(Begging, target, 0.0, 100.0)` — useful from 0 to GM.
- A successful beg takes roughly **one tenth** of the NPC's carried gold
  (`theirPack.GetAmount(Gold) / 10`), clamped to a **maximum of 10–14 gold** per attempt.
- There is a **10-second** cooldown after a beg (`NextSkillTime + 10000`).

## Related skills & synergies

Begging stands largely on its own. It overlaps thematically with other social/rogue play but
has no mechanical synergy with combat or crafting skills.

## See also

- [Vendors & banking](/playing/vendors-and-banking/)
- [Communication & social](/playing/communication-and-social/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
