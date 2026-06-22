---
title: Veterinary
description: Bandage-heal and resurrect pets.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 39, Veterinary)"
  - "servuo: Scripts/Items/Resource/Bandage.cs"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/39.gif" alt="Veterinary skill banner" width="160" />

Veterinary is the pet-healing skill — the [Healing](/skills/healing/) of the animal world.
The stats table and the healing/cure/resurrect formulas below are source-verified against
ServUO; the general training advice is community guidance pending field verification.

## What it does

Veterinary applies bandages to **heal and cure animals**, and at high skill **resurrect** a
dead pet. It is core support for tamers — a tamed pet is only as good as the vet keeping it
alive. It works with [Animal Lore](/skills/animal-lore/) the way [Healing](/skills/healing/)
works with [Anatomy](/skills/anatomy/): Lore raises the amount Vet restores. See
[taming & pets](/playing/taming-and-pets/).

## How to use it

Carry bandages, use them, and target your pet (or another animal). The bandage heals over a
short delay; higher Vet (plus Lore) heals more and faster, cures poison, and — at high
skill — brings a dead pet back. See [healing (how to play)](/playing/healing/).

## How to train it

**Quick start:** an NPC Veterinarian/Animal Trainer teaches Veterinary up to **one-third of
its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. The method is simple:
**bandage a wounded pet, repeatedly.**

- **Low/mid skill** — vet a pet that has taken light damage (let it fight something weak, then
  bandage it) over and over; keep a stack of bandages on hand.
- **High skill** — keep healing a pet through tougher fights; curing poison and resurrecting a
  dead pet hold the gain window late. GGS pays out the slow late points.

Veterinary reads both itself and [Animal Lore](/skills/animal-lore/) — keep Lore up alongside.
See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Veterinarian |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.8, Dex +0.4, Int +0.8 (per-use stat gain weights) |

All of it runs through the bandage code in `Scripts/Items/Resource/Bandage.cs`. When the
patient is a non-player animal/monster, **Veterinary is the primary skill and
[Animal Lore](/skills/animal-lore/) the secondary** (`GetPrimarySkill` / `GetSecondarySkill`),
exactly mirroring Healing + Anatomy for players:

- **Heal amount (AOS):** `min = Lore/8 + Vet/5 + 4`, `max = Lore/6 + Vet/2.5 + 4`, with a small
  **`+HitsMax/100`** bonus when healing a creature. So both Vet and Lore raise the amount
  restored.
- **Bandage delay:** healing another creature with Veterinary is a flat **2 seconds** (AOS),
  much faster than healing a player.
- **Cure poison:** requires **Vet ≥ 60 and Lore ≥ 60**; cure chance scales with skill and the
  poison level.
- **Resurrect a dead pet:** requires **Vet ≥ 80 and Lore ≥ 80**; success chance is
  `(Vet − 68) / 50`. A resurrected pet loses **0.1 from every skill**.

## Related skills & synergies

- **[Animal Taming](/skills/animal-taming/) + [Animal Lore](/skills/animal-lore/) + Veterinary**
  — the tamer trio; see the Animal Tamer build on [seven-GM templates](/templates/seven-gm/)
  and the [Animal Tamer template](/templates/animal-tamer/).

## See also

- [Taming & pets (how to play)](/playing/taming-and-pets/) · [Healing](/playing/healing/)
- [Animals bestiary](/bestiary/animals/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
