---
title: Begging
description: Ask NPCs for spare coin and small goods.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 6 — Beggar, Dex/Int, no stat gain)"
  - "servuo: Scripts/Skills/Begging.cs"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills — teach cap)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
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

**Trainer is rare.** Only a wandering Gypsy NPC teaches Begging — no fixed town vendor — but
where you find one it teaches up to **one-third of its own skill, capped at 42.0**
(`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`).

The method is just **Use it on town NPCs in a loop:**

- **Low/high skill** — beg from town NPCs repeatedly. There is a notable per-use cooldown
  (`Scripts/Skills/Begging.cs` returns a long re-use delay), so Begging is slow to raise; just
  keep targeting fresh NPCs around a busy town and let GGS carry the slow points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

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
