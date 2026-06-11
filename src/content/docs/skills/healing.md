---
title: Healing
description: Bandage healing — heal amounts, cure and resurrection thresholds, bandage timing, and training.
status: source-verified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (BandageContext)"
  - "servuo: Server/Skills.cs (SkillInfo 17)"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/17.gif" alt="Healing skill banner" width="160" />

A warrior's best weapon is the strip of cloth in their off-hand. Healing turns bandages into
hit points, antidotes, and — at the high end — second chances.

**Stats:** Intelligence (primary), Dexterity (secondary) · **Title:** Healer

## How it works

Apply a **bandage** (cut cloth) to yourself, another player, or a humanoid. All numbers below
are from `Scripts/Items/Resource/Bandage.cs`. Healing always works with **Anatomy** as its
companion skill; for animals, the same system uses Veterinary + Animal Lore.

### Heal amount (AOS rules, active here)

```
chance to succeed = (Healing + 10) / 100 − 0.02 × slips
heal amount: between  Anatomy/8 + Healing/5 + 4
             and      Anatomy/6 + Healing/2.5 + 4
```

"Slips" are the times you took damage mid-bandage — each costs 2% success and reduces the
amount healed. At GM Healing/Anatomy a clean bandage restores roughly 36–61 HP.

### Cure poison

Requires **Healing ≥ 60 and Anatomy ≥ 60**:

```
cure chance = (Healing − 30)/50 − 0.1 × poisonLevel − 0.02 × slips
```

### Resurrection

Requires **Healing ≥ 80 and Anatomy ≥ 80** (and 5 extra seconds on the bandage):

```
res chance = (Healing − 68)/50 − 0.02 × slips
```

— about 64% at GM with no slips.

### Bandage timing (AOS)

| Target | Seconds |
|--------|---------|
| Yourself | `ceil(11 − Dex/20)`, clamped 4–8 (4s at 140+ Dex) |
| Someone else | `ceil(4 − Dex/60)`, minimum 2 |
| A pet (Veterinary) | flat 2 |

Dexterity is the bandage stat — another reason warriors love it.

## Training

- **0–60:** buy from an NPC healer, then bandage yourself after taking modest damage.
  Sparring with a partner (or a weak monster you out-armor) provides steady wounds.
- **60–80:** add cure practice — lesser poison from training or wandering snakes.
- **80–100:** resurrection attempts give the best checks; ghosts are rarely in short supply
  outside a dungeon entrance. Standard [gain rules](/mechanics/skill-gain/) and GGS apply.

Keep **Anatomy training in lockstep** — every formula above reads both skills, and the 60/80
thresholds check both.

## Related skills

- **Anatomy** — non-negotiable companion
- **Veterinary** — the same mechanics for pets ([Animal Taming](/skills/animal-taming/) builds)
- [Swordsmanship](/skills/swordsmanship/) / [Tactics](/skills/tactics/) — who do you think is bleeding?
