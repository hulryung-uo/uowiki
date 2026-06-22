---
title: Stealing
description: Take what isn't nailed down.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 33 — Pickpocket, Dex/Int, dexGain 1.0)"
  - "servuo: Scripts/Skills/Stealing.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/33.gif" alt="Stealing skill banner" width="160" />

Stealing lifts items from packs, creatures, and the ground. The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table and weight/skill formula below are source-verified against
ServUO.

## What it does

Stealing is the thief's payoff skill: the snatch that follows a [Snooping](/skills/snooping/)
recon. You can lift items from NPCs, monsters (steal special loot off tough creatures), and
other players' packs. Success depends on the item's **weight** versus your skill, and a failed
or noticed steal from a player flags you **criminal**. See [notoriety & PvP](/playing/notoriety-and-pvp/).

## How to use it

Activate the skill and target the item in a pack or on a creature (both hands must be free;
you must be in the Thieves' Guild to steal from players). Light items are far easier than
heavy ones. See [items & inventory](/playing/items-and-inventory/).

## How to train it

**No regular town trainer.** Stealing is a thief skill — no ordinary vendor teaches it (only a
wandering Gypsy/Thief NPC carries it), so for most players you train it by use from the start.

The trick: **steal a light item off an NPC, a training partner, or your own placed container,
repeatedly.** Difficulty scales with the item's weight (`Scripts/Skills/Stealing.cs`: items
over **10 stones can't be lifted at all** — `w > 10` — and the check window is built from
`pileWeight` × the stack), so stay with light items to keep succeeding:

- **Low skill** — steal **light** items (≤ a few stones) over and over; a partner's stocked
  pack or a controlled setup is standard.
- **High skill** — heavier (but still ≤10-stone) items and special monster loot give the late
  gains. GGS guarantees the slow late points as long as you keep stealing.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Pickpocket |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +1 (per-use stat gain weights) |

From `Scripts/Skills/Stealing.cs`: the difficulty scales with item weight — the check uses a
window of roughly `pileWeight × 10 ± 22.5/27.5`, so heavier piles are exponentially harder.
The max amount you can grab from a stack is `(Stealing / 10) / itemWeight` (at least 1). The
faction sigil uses a special high-skill check (`80.0` / `100.0–120.0`).

## Related skills & synergies

- **[Snooping](/skills/snooping/) + [Hiding](/skills/hiding/) + [Stealth](/skills/stealth/)**
  — the thief core: hide, stealth in, snoop, steal; see the Thief/Rogue build on
  [seven-GM templates](/templates/seven-gm/).

## See also

- [Notoriety & PvP](/playing/notoriety-and-pvp/) · [Items & inventory](/playing/items-and-inventory/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
