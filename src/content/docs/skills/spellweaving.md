---
title: Spellweaving
description: Arcanist circle magic of the elves.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 54)"
  - "servuo: Scripts/Spells/Spellweaving/"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/54.gif" alt="Spellweaving skill banner" width="160" />

Spellweaving is the expansion-era (Mondain's Legacy) arcanist spell school. The prose is
community-derived from ServUO and general UO mechanics (no uorenaissance.com entry) pending
field verification; the stats table is source-verified against ServUO. Behavior is
expansion-specific — see [magic schools](/playing/magic-schools/).

## What it does

Spellweaving casts arcane spells — summons (Summon Fey/Fiend, Vortex, Nature's Fury), area
damage (Wildfire, Word of Death, Thunderstorm), buffs (Gift of Renewal, Attunement, Immolating
Weapon, Arcane Empowerment), and utility (Gift of Life, Etheral Voyage, Dryad Allure). Its
signature mechanic is the **focus circle**: when multiple arcanists stand together (or you
hold an **Arcane Focus**), spell power scales up.

## How to use it

Cast from the Spellweaving spellbook with mana. Casting inside a focus circle of fellow
arcanists, or carrying an Arcane Focus item, raises the effective casting "focus level" and
makes the spells stronger. See [spellcasting](/playing/spellcasting/) and
[magic schools](/playing/magic-schools/).

## How to train it

**No town trainer.** Spellweaving is an Elf school with no standard NPC vendor that teaches it
(only rare/boss mobiles carry the skill), so train it by use from the start — you also need to
complete the quest to learn the school before you can cast.

Spellweaving rises from **casting its spells** (no reagents, but most spells scale with how
many weavers share an Arcane Circle):

- **Low skill** — cast the cheap spells (Arcane Circle, Gift of Renewal) repeatedly.
- **Mid/high skill** — cast steadily in combat; the stronger spells hold the gain window, and
  GGS pays out the slow late points. Some specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Arcanist |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Spell implementations live under `Scripts/Spells/Spellweaving/` (including
`Items/ArcaneFocus.cs`). The focus-circle scaling and per-spell numbers are expansion-specific
and **unverified** here. Associated with the **elven** race.

## Related skills & synergies

- **[Magery](/skills/magery/) + [Meditation](/skills/meditation/)** — common hybrid; see the
  Necro-Mage/Spellweaver/Mystic note on [seven-GM templates](/templates/seven-gm/).
- **[Focus](/skills/focus/)** — extra mana regen for the casting-heavy arcanist.

## See also

- [Magic schools](/playing/magic-schools/) · [Spellcasting](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
