---
title: Tactics
description: The universal melee damage skill — the exact damage bonus formula and how it trains itself.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (tacticsBonus in ScaleDamageAOS, passive Tactics CheckSkill)"
  - "servuo: Scripts/Abilities/WeaponAbility.cs (special-move skill/Tactics requirements; TOL branch)"
  - "servuo: Server/Skills.cs (SkillInfo 27)"
last_verified: 2026-06-17
generated: false
---

<img src="/img/skill-flags/27.gif" alt="Tactics skill banner" width="160" />

Knowing *how* to fight matters as much as knowing how to swing. Tactics is the damage
multiplier behind every weapon skill — no warrior build skips it.

**Stats:** Strength (primary), Dexterity (secondary) · **Title:** Tactician

Tactics affects your damage in **two** ways: it is a large flat **damage multiplier**, and it
**unlocks weapon special moves**.

### 1. The damage bonus

When a hit lands, `ScaleDamageAOS` (the active path on this AOS/EJ shard) scales the weapon's
base damage by a stack of additive bonuses — Tactics is the biggest one:

```
tacticsBonus  = Tactics × 0.625%   (+6.25% extra at 100.0)   → +68.75% at GM
anatomyBonus  = Anatomy × 0.5%     (+5% extra at 100.0)      → +55% at GM
strengthBonus = Str × 0.3%         (+5% extra at 100 Str)    → +35% at 100 Str
lumberBonus   = Lumberjacking × 0.2% (+10% at 100.0; axes only) → +30% at GM
```

These are **added together**, then multiply the weapon's base damage:
`damage = base × (1 + Tactics% + Anatomy% + Str% + …)`. So **Tactics scales linearly** —
roughly **+0.625% damage per point**, plus a **+6.25% jump at exactly 100.0**. At grandmaster
it contributes **+68.75%**, the single largest physical bonus in the formula; a fighter
without Tactics hits like a polite suggestion.

*Worked example:* a weapon with **15** base damage, wielded at GM Tactics + GM Anatomy + 100
Str, is scaled by `1 + 0.6875 + 0.55 + 0.35 = 2.5875` → about **39** before item Damage
Increase, slayers, and resists. Drop Tactics and that same swing falls to ~29 — a ~25% loss.
The full stack lives in [Advanced combat → Damage components](/playing/combat-advanced/#damage-components).

### 2. It unlocks special moves

Tactics is the **secondary requirement** for weapon [special moves](/playing/combat-advanced/#special-moves-primary-and-secondary)
(`WeaponAbility.cs`). On this shard (TOL+ rules) you need, in addition to the weapon-skill
requirement (70 primary / 90 secondary):

- **30.0 Tactics** to use a weapon's **primary** special move,
- **60.0 Tactics** to use its **secondary** special move.

Below those values the move simply won't fire (*"You need … weapon skill to perform that
attack"*). So Tactics isn't just damage — it's the gate to disarms, bleeds, armor-ignoring
hits, and the rest of your weapon's toolkit.

Tactics has **no active use** of its own; both effects are passive.

## Training

Tactics gains **passively whenever you deal weapon damage** — `ScaleDamageAOS` performs a
Tactics skill check on each damage calculation. In practice:

- Fight anything that fights back. Tactics rises alongside your weapon skill
  ([Swordsmanship](/skills/swordsmanship/), Mace Fighting, Fencing, Archery, Wrestling).
- Early levels fly (everything below 10.0 gains per use); later levels follow the standard
  [gain curve](/mechanics/skill-gain/) with GGS as a safety net.
- Strength is the primary stat, so hitting things also makes you stronger — Britannia's
  fitness program.
- **Quick start:** an NPC weapon trainer also teaches Tactics up to **one-third of its own
  skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
  `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42, then it rides up with every
  fight. Train it with your weapon skill and [Anatomy](/skills/anatomy/) on the same monsters.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Related skills

- [Swordsmanship](/skills/swordsmanship/) and the other weapon skills — your to-hit
- **Anatomy** — the companion damage bonus, and a prerequisite for good [Healing](/skills/healing/)
- [Lumberjacking](/skills/lumberjacking/) — the axe-only damage bonus
