---
title: Animal Lore
description: Inspect a creature's stats, loyalty, and abilities.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 2, Animal Lore)"
  - "servuo: Scripts/Skills/AnimalLore.cs"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/2.gif" alt="Animal Lore skill banner" width="160" />

Animal Lore appraises creatures and is core support for tamers. The stats table and the
skill-gated lore rules below are source-verified against ServUO; the general training advice
is community guidance pending field verification.

## What it does

Animal Lore opens a detailed window on a creature: hit points, stats, resistances, damage,
control slots, loyalty (for a pet), and whether it can be tamed and how hard. Tamers use it
to evaluate wild creatures before a tame, to read a pet's loyalty so it does not go wild,
and to plan training. See [taming & pets](/playing/taming-and-pets/).

## How to use it

Activate the skill and target a creature. The lore gump appears with its full stat block
(hits/stats, resistances, damage, combat skills, preferred foods, and loyalty). On your own
pet it shows current loyalty and condition; reading **wild** creatures requires higher skill
(see the gating below).

## How to train it

**Quick start:** an NPC Animal Trainer/Rancher/Veterinarian teaches Animal Lore up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`), so buy to ~30–42 first.

Animal Lore is an active **"read"** skill — target a creature and Use it; each read rolls a
gain check.

- **Below 100** — you can **only lore tamed (controlled) creatures** (the code blocks loring
  wild animals until 100), so train on a **pet** — your own or a friend's. Loring your own
  pets is always available and always rolls a gain check.
- **100–109.9** — you can also lore **wild tameable** creatures (chickens, sheep, cats, and
  up — see the [animals bestiary](/bestiary/animals/)).
- **110+** — you can lore **anything**, including wild untameable monsters; harder targets
  keep you inside the gain window longer.

Just keep loring something and GGS carries the slow late points. See
[skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Naturalist |
| Mastery skill | No |
| Gain notes | skill-ups can raise Int +1 (per-use stat gain weights) |

In `Scripts/Skills/AnimalLore.cs` the check is a target-skill roll against the creature
(`CheckTargetSkill(AnimalLore, c, min, 120.0)` — the useful range tops out at 120). What you
can lore depends on your skill:

- **Below 100** — you can only lore **already-tamed (controlled)** creatures; wild ones give
  "you can only lore tamed creatures."
- **100–109.9** — tamed creatures (no roll) **or tameable** wild ones (rolled against `min =
  80`).
- **110+** — also **non-tameable** creatures (rolled against `min = 100`).

So reading wild, untameable monsters requires 110+ Animal Lore.

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
