---
title: Magery
description: The eight circles of classic spellcasting — cast chance per circle, mana costs, reagents, and how to train.
status: source-verified
sources:
  - "servuo: Scripts/Spells/Base/MagerySpell.cs (GetCastSkills, GetMana)"
  - "servuo: Server/Skills.cs (SkillInfo 25)"
  - "servuo: Scripts/Misc/SkillCheck.cs"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/25.gif" alt="Magery skill banner" width="160" />

*Kal Ort Por* — and you are somewhere else. Magery is the realm's most versatile skill: damage,
travel, defense, and utility across eight circles of spells.

**Stats:** Intelligence (primary), Strength (secondary) · **Title:** Mage

## How casting works

Each spell belongs to a **circle** (1–8). Per `MagerySpell.cs` (`GetCastSkills`), your chance
to successfully cast is a standard skill check across a window centered on
`(100/7) × (circle − 1)`, ±20 skill:

| Circle | Skill window (min–max) | 50% cast at | Mana |
|--------|------------------------|-------------|------|
| 1st | −20.0 – 20.0 | 0.0 | 4 |
| 2nd | −5.7 – 34.3 | 14.3 | 6 |
| 3rd | 8.6 – 48.6 | 28.6 | 9 |
| 4th | 22.9 – 62.9 | 42.9 | 11 |
| 5th | 37.1 – 77.1 | 57.1 | 14 |
| 6th | 51.4 – 91.4 | 71.4 | 20 |
| 7th | 65.7 – 105.7 | 85.7 | 40 |
| 8th | 80.0 – 120.0 | 100.0 | 50 |

Casting **from a scroll** counts as two circles lower (`circle -= 2` when `Scroll != null`),
so scrolls are both a convenience and a training tool. Base cast time grows with circle:
`(4 + circleIndex) × 0.25s`, where `circleIndex` runs **0–7** (the `SpellCircle` enum is
zero-based). So a **1st-circle** spell takes **1.0s** and an **8th-circle** spell **2.75s**
before any Faster Casting reductions (`MagerySpell.cs`, `CastDelaySecondsPerTick = 0.25`).

Every cast consumes [reagents](/items/reagents/); spell-by-spell recipes live in the
[Magic section](/magic/).

## Training

Cast spells whose window brackets your skill — too easy gains nothing, too hard can't be cast
(see [skill gain](/mechanics/skill-gain/)). A classic ladder:

- **0–30:** buy initial skill from an NPC Mage — a trainer teaches up to **one-third of its
  own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
  `baseToSet = ourSkill.BaseFixedPoint / 3`). Then cast 1st–2nd circle (Magic Arrow, Cure).
- **30–55:** 3rd–4th circle — Fireball, Lightning, Recall (Recall everywhere; it's useful *and* trains).
- **55–75:** 5th–6th circle — Energy Bolt, Invisibility, Mark.
- **75–100:** 7th–8th circle — Flamestrike, Gate Travel, summons. The 8th circle reaches
  "no challenge" only at 120, so it trains to the cap.

The universal method is the **spell ladder**: keep casting the offensive spell whose window
brackets your skill (Fireball → Lightning → Energy Bolt → Flamestrike), stepping up each
circle as the lower one stops gaining, and **mind your reagent supply** so a session never
stops. Intelligence (primary stat) and Meditation determine how long you can keep casting;
Eval Int scales the damage. GGS guarantees the slow last points eventually arrive. See
[using & training skills](/playing/using-and-training-skills/).

## Related skills

- **Evaluating Intelligence** — damage scaling; **Meditation** — mana recovery;
  **Resisting Spells** — defense; **Inscription** — scrolls that train you and pay you
- [Moonglow](/world/moonglow/) — the mage city, with reagent vendors at the bank's doorstep
- [Items: reagents](/items/reagents/) — the shopping list
