---
title: Animal Taming
description: Befriending the beasts of Britannia — the taming difficulty formula, example creatures, and the long road to dragons.
status: source-verified
sources:
  - "servuo: Scripts/Skills/AnimalTaming.cs (success check; ScaleSkills first-tame 0.90/0.86/0.72)"
  - "servuo: Scripts/Mobiles/Normal/*.cs (MinTameSkill values)"
  - "servuo: Server/Skills.cs (SkillInfo 35)"
last_verified: 2026-06-15
generated: false
---

<img src="/img/skill-flags/35.gif" alt="Animal Taming skill banner" width="160" />

Some adventurers carry swords; tamers carry an entourage. Animal Taming turns wild creatures
into loyal companions — eventually including ones that breathe fire.

**Stats:** Strength (primary), Intelligence (secondary) · **Title:** Tamer

## How it works

Use the skill, target a creature, and talk it down while standing close. Per
`Scripts/Skills/AnimalTaming.cs`, the success check is:

```
minSkill = creature.CurrentTameSkill + (previousOwners × 6.0) + 24.9
check: AnimalTaming between (minSkill − 25.0) and (minSkill + 25.0)
```

In plain terms: at exactly a creature's tame skill you have roughly a coin-flip; the chance
scales linearly across a ±25-point window. **Each previous owner adds 6.0 effective
difficulty**, so a much-traded pet becomes nearly untameable. Taming attempts also passively
exercise Animal Lore (checked 0–120).

## Example difficulties

`MinTameSkill` values from the creature scripts (`Scripts/Mobiles/Normal/`):

| Creature | Min tame skill |
|----------|----------------|
| Rabbit | −18.9 (anyone) |
| Cow | 11.1 |
| Horse | 29.1 |
| Dragon | 93.9 |
| Nightmare | 95.1 |
| White Wyrm | 96.3 |

(A full creature table belongs to the [Bestiary](/bestiary/).)

## First-tame skill penalty

A freshly-tamed pet does **not** keep its wild skills at full value — `AnimalTaming.cs`
scales them down on the first tame:

| Situation | Skills retained | Notes |
|---|---|---|
| Normal first tame | **90%** | the pet's skills are set to 90% of their wild values |
| Paralyzed during the tame | **86%** | tamed while held by a paralyze effect |
| Greater Dragon (first tame) | **72%** | plus skill **cap reduced to 90%**; Magery capped at tame |

This matters when choosing a high-end pet: a Greater Dragon starts well below its wild
sheet and is permanently capped lower, which is the main trade-off versus an ordinary
[Dragon](/bestiary/). Skills then train back up through use, up to the (possibly reduced) cap.

## Training

- **0–30:** buy initial skill from an NPC Animal Trainer — a trainer teaches up to **one-third
  of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
  `baseToSet = ourSkill.BaseFixedPoint / 3`). Then tame everything in a farm field — rabbits,
  birds, sheep, cows. Release and re-tame; a fresh target is needed for each attempt.
- **30–60:** horses (29.1) are the classic mid-range target — tame, release, repeat. The
  [Skara Brae](/world/skara-brae/) fields and Britain's farmland both work.
- **60–90:** progress through tougher wilderness spawn — the rule of thumb from the formula:
  pick creatures whose tame skill is near your current skill for the best gain band
  (see [skill gain](/mechanics/skill-gain/)).
- **90–100+:** dragons (Destard) and nightmares (Fire Dungeon) — bring protection or a
  very good escape plan, since difficult tames fail often and the subjects object violently.

The universal rule is **tame up the difficulty ladder**, always on a creature whose tame skill
is near yours. Anti-macro is off on this shard, and GGS guarantees the painful late points
eventually land. See [using & training skills](/playing/using-and-training-skills/).

## Related skills

- **Animal Lore** — inspect before you tame; trains passively alongside
- **Veterinary** — bandage-heal and resurrect your pets ([Healing](/skills/healing/)'s animal cousin)
- [Pet Training](/playing/pet-training/) — grow the pet after you tame it (stats, skills, abilities)
- [Skara Brae](/world/skara-brae/) — the tamer's town
