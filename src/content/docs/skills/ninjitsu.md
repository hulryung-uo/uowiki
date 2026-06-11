---
title: Ninjitsu
description: Ninja techniques, forms, and stealth attacks.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 53)"
  - "servuo: Scripts/Spells/Ninjitsu/"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/53.gif" alt="Ninjitsu skill banner" width="160" />

Ninjitsu is the expansion-era (Samurai Empire) ninja skill. The prose is community-derived
from ServUO and general UO mechanics (no uorenaissance.com entry) pending field verification;
the stats table is source-verified against ServUO. Behavior is expansion-specific — see
[magic schools](/playing/magic-schools/).

## What it does

Ninjitsu grants a toolkit of stealthy combat and mobility tricks: **Animal Form** (turn into
a creature for speed or disguise), **Mirror Image** (decoy clones), **Focus Attack**, **Death
Strike** and **Surprise Attack** (hit-from-hiding bonuses), **Backstab**, and **Smoke Bomb**
(instant hide). It rewards a hit-and-vanish playstyle and leans heavily on
[Hiding](/skills/hiding/)/[Stealth](/skills/stealth/).

## How to use it

Activate abilities from the Book of Ninjitsu (most cost mana). Several stealth attacks require
you to strike from [hiding](/skills/hiding/); Animal Form and Smoke Bomb support the sneak
playstyle. See [hiding & stealth](/playing/hiding-and-stealth/) and
[advanced combat](/playing/combat-advanced/).

## How to train it

- **Low skill** — use Animal Form and the cheap abilities repeatedly.
- **Mid/high skill** — weave stealth attacks and forms into combat; gains come from use.
  Specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Ninja |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Ability implementations live under `Scripts/Spells/Ninjitsu/` (e.g. `FocusAttack.cs`,
`AnimalForm.cs`). Exact ability numbers are expansion-specific and **unverified** here.

## Related skills & synergies

- **[Hiding](/skills/hiding/) + [Stealth](/skills/stealth/)** — required for the
  strike-from-hiding attacks; the core ninja synergy.
- **A weapon skill + [Tactics](/skills/tactics/)** — Ninjitsu layers onto a melee fighter.
- **[Bushido](/skills/bushido/)** — the common samurai/ninja hybrid.

## See also

- [Hiding & stealth](/playing/hiding-and-stealth/) · [Advanced combat](/playing/combat-advanced/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
