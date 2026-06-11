---
title: Animal Lore
description: Inspect a creature's stats, loyalty, and abilities.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Skills/AnimalLore.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/2.gif" alt="Animal Lore skill banner" width="160" />

Animal Lore appraises creatures and is core support for tamers. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and skill-check note are source-verified against
ServUO.

## What it does

Animal Lore opens a detailed window on a creature: hit points, stats, resistances, damage,
control slots, loyalty (for a pet), and whether it can be tamed and how hard. Tamers use it
to evaluate wild creatures before a tame, to read a pet's loyalty so it does not go wild,
and to plan training. See [taming & pets](/playing/taming-and-pets/).

## How to use it

Activate the skill and target a creature. The lore gump appears with its full stat block. On
a creature you have not yet tamed it shows tameability and difficulty; on your own pet it
shows current loyalty and condition.

## How to train it

**Quick start:** an NPC Animal Trainer/Rancher/Veterinarian teaches Animal Lore up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`), so buy to ~30–42 first.

Animal Lore is an active **"read"** skill — target a creature and Use it; each read rolls a
gain check.

- **Low skill** — lore weak, common animals around town and farms (chickens, sheep, cats,
  see the [animals bestiary](/bestiary/animals/)).
- **Mid/high skill** — lore tougher creatures; harder targets keep you inside the gain
  window longer. If you have a tamer, **lore your own pets** repeatedly — always available,
  always fresh.

Just keep loring something new and GGS carries the slow late points. See
[skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Naturalist |
| Mastery skill | No |
| Gain notes | skill-ups can raise Int +1 (per-use stat gain weights) |

In `Scripts/Skills/AnimalLore.cs` the check is run as a target-skill roll against the
creature (`CheckTargetSkill(AnimalLore, c, min, 120.0)`) — the skill caps its useful range
at 120 for reading the toughest creatures, with the minimum difficulty scaling to the
target.

## Related skills & synergies

- **[Animal Taming](/skills/animal-taming/) + Animal Lore + [Veterinary](/skills/veterinary/)**
  — the classic tamer trio: tame the pet, lore it, vet it.
- Featured in the Animal Tamer build on [seven-GM templates](/templates/seven-gm/) and the
  [Animal Tamer template](/templates/animal-tamer/).

## See also

- [Taming & pets (how to play)](/playing/taming-and-pets/)
- [Animals bestiary](/bestiary/animals/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
