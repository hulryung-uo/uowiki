---
title: Taste Identification
description: Detect poison in food and drink.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 36)"
  - "servuo: Scripts/Skills/TasteID.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/36.gif" alt="Taste Identification skill banner" width="160" />

Taste Identification (Taste ID) samples consumables to detect poison. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and skill-check note below are source-verified
against ServUO.

## What it does

Taste ID lets you sample food, drink, or a potion to find out whether it is **poisoned**
before you consume it — a safety check against [Poisoning](/skills/poisoning/) traps on food.
It is a niche skill with limited use outside that specific defensive scenario.

## How to use it

Activate the skill and target the food or drink. A successful roll reports whether it carries
poison (and roughly how strong). See [poison & status](/playing/poison-and-status/).

## How to train it

**Quick start:** an NPC Cook/Baker/Alchemist teaches Taste ID up to **one-third of its own
skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

The method: **Use it on a consumable, over and over:**

- **Low/high skill** — taste food or drink repeatedly; any consumable works as a target, so
  keep a stack of bread or a pitcher handy and spam it. GGS guarantees the slow late points as
  long as you keep tasting.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Praegustator |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.2, Int +0.8 (per-use stat gain weights) |

From `Scripts/Skills/TasteID.cs`: the check is `CheckTargetSkill(TasteID, food, 0, 100)`; on
success it reads `food.Poison` and reports the poison (if any).

## Related skills & synergies

- **[Poisoning](/skills/poisoning/)** — the threat Taste ID defends against (poisoned food).
- **[Cooking](/skills/cooking/) / [Alchemy](/skills/alchemy/)** — the consumables you might
  want to verify.

## See also

- [Poison & status (how to play)](/playing/poison-and-status/)
- [Food & drink catalog](/items/catalog/food-drink/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
