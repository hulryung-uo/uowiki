---
title: Stealth
description: Move while staying hidden.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 47)"
  - "servuo: Scripts/Skills/Stealth.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/47.gif" alt="Stealth skill banner" width="160" />

Stealth lets you walk while staying [hidden](/skills/hiding/). The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table, the step formula, and the armor cap below are source-verified
against ServUO.

## What it does

Stealth turns Hiding from a stationary trick into mobility: while hidden, you can take a
number of careful steps without being revealed, instead of popping into view the moment you
move. It is the foundation of scouts, thieves, and stealth archers. See
[hiding & stealth](/playing/hiding-and-stealth/).

## How to use it

[Hide](/skills/hiding/) first, then move — each step rolls Stealth. Succeed and you stay
hidden for that step; the number of guaranteed stealthy steps you bank scales with skill.
Wearing too much non-medable (metal) armor stops you stealthing entirely.

## How to train it

You must be **[Hidden](/skills/hiding/) first** — Stealth only rolls while you walk hidden, and
each success banks steps equal to **`Stealth / 5`** (`Scripts/Skills/Stealth.cs`; ~20 steps at
GM). An NPC Ranger/Thief will teach Stealth, but only once your Hiding meets the requirement
(`BaseCreature.CheckTeach` blocks teaching Stealth below `Stealth.HidingRequirement`), and it
caps at the usual **one-third of the NPC's skill, max 42.0**.

The method: **Hide, then walk in stealth until revealed, re-hide, repeat.**

- **Low skill** — hide, then step carefully; it's slow at first because failed steps reveal
  you. Keep [Hiding](/skills/hiding/) high so you can re-hide instantly and resume walking.
- **High skill** — keep moving while hidden; reliable steps come once skill is high. Watch
  your armor — too much non-medable armor blocks stealth entirely. GGS carries the late points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Rogue |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

From `Scripts/Skills/Stealth.cs`: the allowed stealthy steps are **`skill / 5`** (AOS era;
**`skill / 10`** pre-AOS) — so about **20 steps at GM** on this expansion. Too much armor
blocks it: an armor rating ≥ **42** (AOS; **26** pre-AOS) means "You could not hope to move
quietly wearing this much armor." `MageArmor`-flagged pieces do not count toward that rating.

## Related skills & synergies

- **[Hiding](/skills/hiding/)** — Stealth requires you to be hidden first; the two are
  inseparable.
- **[Stealing](/skills/stealing/) + [Snooping](/skills/snooping/)** — the thief core, or
  pair with [Archery](/skills/archery/) for the Stealth Archer build on
  [seven-GM templates](/templates/seven-gm/).

## See also

- [Hiding & stealth (how to play)](/playing/hiding-and-stealth/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
