---
title: Poisoning
description: Coat blades and food with poison.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 30)"
  - "servuo: Scripts/Skills/Poisoning.cs"
  - "servuo: Scripts/Items/Consumables/*PoisonPotion.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/30.gif" alt="Poisoning skill banner" width="160" />

Poisoning applies poison to weapons (and, classically, food). The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table, potion skill ranges, and charge formula below are
source-verified against ServUO.

## What it does

Poisoning lets you coat a bladed or piercing weapon — or food/drink — with poison from a
poison potion, so that creatures struck (or fed) take poison damage over time. Higher skill
lets you apply **stronger** poisons more reliably. It is a Mastery skill favored by assassins
and a nasty addition to a [Fencer's](/skills/fencing/) infectious-strike blade.

## How to use it

Have a poison potion in your pack, use the Poisoning skill, then target a bladed/piercing
weapon (or food). The skill check decides whether the poison takes. See
[poison & status](/playing/poison-and-status/) and [combat basics](/playing/combat-basics/).

## How to train it

- **Low skill (0–60)** — apply **lesser** poison potions; matched to skill 0.0–60.0.
- **Mid skill (30–70 / 60–100)** — **regular** then **greater** poison potions.
- **High skill (80–100)** — **deadly** poison potions for the steadiest late gains.

See [skill gain](/mechanics/skill-gain/) and [alchemy](/skills/alchemy/) (which brews the
potions).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Assassin |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Dex +0.4, Int +1.6 (per-use stat gain weights) |

Verified from ServUO. Per-potion skill ranges (`MinPoisoningSkill`/`MaxPoisoningSkill` on each
`*PoisonPotion.cs`): **Lesser 0–60**, **Regular 30–70**, **Greater 60–100**, **Deadly 80–100**.
The check is `CheckTargetSkill(Poisoning, target, min, max)` (`Scripts/Skills/Poisoning.cs`).
A successful application gives a weapon **`18 − (level × 2)` charges** (so a weaker poison
yields more charges). On **failure** there is a **5% chance to poison yourself**.

## Related skills & synergies

- **[Fencing](/skills/fencing/) / a weapon skill** — poisoned blades + infectious strike.
- **[Alchemy](/skills/alchemy/)** — brews the poison potions you apply.
- **[Healing](/skills/healing/) / [Taste Identification](/skills/taste-identification/)** —
  cure poison / detect poisoned food.

## See also

- [Poison & status (how to play)](/playing/poison-and-status/)
- [Potions catalog](/items/catalog/potions/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
