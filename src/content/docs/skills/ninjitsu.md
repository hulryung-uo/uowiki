---
title: Ninjitsu
description: Ninja techniques, forms, and stealth attacks.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 53: Dex primary / Int secondary, Ninja, mastery)"
  - "servuo: Scripts/Spells/Ninjitsu/NinjaSpell.cs (CastSkill=Ninjitsu, RequiredMana, ScaleMana)"
  - "servuo: Scripts/Spells/Ninjitsu/ (AnimalForm, MirrorImage, FocusAttack, DeathStrike, SurpriseAttack, Backstab); AnimalForm.cs RequiredSkill 0, RequiredMana 10 (ML)"
  - "servuo: Scripts/Spells/Ninjitsu/Backstab.cs + SurpriseAttack.cs (require Hidden && AllowedStealthSteps > 0)"
  - "servuo: Scripts/Mobiles/NPCs/Ninja.cs (Ninjitsu trainer); Scripts/Mobiles/Normal/BaseCreature.cs (baseToSet = BaseFixedPoint/3, capped 42.0)"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/53.gif" alt="Ninjitsu skill banner" width="160" />

Ninjitsu is the expansion-era (Samurai Empire) ninja skill. The prose is community-derived
from ServUO and general UO mechanics (no uorenaissance.com entry) pending field verification;
the stats table is source-verified against ServUO. Behavior is expansion-specific — see
[magic schools](/playing/magic-schools/).

## What it does

Ninjitsu grants a toolkit of stealthy combat and mobility tricks: **Animal Form** (turn into
a creature for speed or disguise), **Mirror Image** (decoy clones), **Death Strike**,
**Surprise Attack** and **Backstab** (hit-from-hiding bonuses), plus weapon specials like
**Focus Attack** and **Ki Attack**. Smoke Bombs (crafted consumables, not a spellbook ability)
give an instant hide and round out the kit. It rewards a hit-and-vanish playstyle and leans
heavily on [Hiding](/skills/hiding/)/[Stealth](/skills/stealth/).

## How to use it

Activate abilities from the Book of Ninjitsu (most cost mana). Surprise Attack and Backstab
require you to strike from [hiding](/skills/hiding/) (the code checks you are hidden with
stealth steps available); Animal Form and Smoke Bombs support the sneak playstyle. See
[hiding & stealth](/playing/hiding-and-stealth/) and [advanced combat](/playing/combat-advanced/).

## How to train it

**Quick start:** an NPC Ninja (or a Ninja trainer in the Tokuno towns) teaches Ninjitsu up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

Ninjitsu rises from **using its abilities** — the cheapest reliable trainer is **Animal Form**:

- **Low skill** — shift into Animal Form (and back) and use the cheap abilities repeatedly; it
  costs only mana, so it's an easy loop.
- **Mid/high skill** — weave stealth attacks and forms into combat; harder use holds the gain
  window, and GGS pays out the slow late points. Some specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

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
