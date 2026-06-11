---
title: Tactics
description: The universal melee damage skill — the exact damage bonus formula and how it trains itself.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (tacticsBonus, ScaleDamageOld)"
  - "servuo: Server/Skills.cs (SkillInfo 27)"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/27.gif" alt="Tactics skill banner" width="160" />

Knowing *how* to fight matters as much as knowing how to swing. Tactics is the damage
multiplier behind every weapon skill — no warrior build skips it.

**Stats:** Strength (primary), Dexterity (secondary) · **Title:** Tactician

## What it does

Tactics adds directly to your melee damage. In `BaseWeapon.cs`, the damage bonus stack is:

```
tacticsBonus  = Tactics × 0.625%   (+6.25% extra at 100.0)
anatomyBonus  = Anatomy × 0.5%     (+5% extra at 100.0)
strengthBonus = Str × 0.3%         (+5% extra at 100 Str)
lumberBonus   = Lumberjacking × 0.2% (+10% at 100.0; axes only)
```

At grandmaster, Tactics alone contributes **+68.75% damage** — the largest single physical
bonus in the formula. A fighter without Tactics hits like a polite suggestion.

Tactics has no active use; it is purely passive. It also gates some weapon **special moves**,
which require minimum Tactics values (per the AOS weapon ability system — exact thresholds
vary by move; unverified here pending a dedicated combat page).

## Training

Tactics gains **passively whenever you deal weapon damage** — `ScaleDamageOld` performs a
Tactics skill check on each damage calculation. In practice:

- Fight anything that fights back. Tactics rises alongside your weapon skill
  ([Swordsmanship](/skills/swordsmanship/), Mace Fighting, Fencing, Archery, Wrestling).
- Early levels fly (everything below 10.0 gains per use); later levels follow the standard
  [gain curve](/mechanics/skill-gain/) with GGS as a safety net.
- Strength is the primary stat, so hitting things also makes you stronger — Britannia's
  fitness program.

## Related skills

- [Swordsmanship](/skills/swordsmanship/) and the other weapon skills — your to-hit
- **Anatomy** — the companion damage bonus, and a prerequisite for good [Healing](/skills/healing/)
- [Lumberjacking](/skills/lumberjacking/) — the axe-only damage bonus
