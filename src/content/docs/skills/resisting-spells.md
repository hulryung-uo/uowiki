---
title: Resisting Spells
description: Shrug off hostile magic and reduce its effects.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 26)"
  - "servuo: Scripts/Misc/AOS.cs (MagicResist damage reduction)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/26.gif" alt="Resisting Spells skill banner" width="160" />

Resisting Spells (Magic Resistance) lowers the impact of hostile magic. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and the damage-reduction note below are
source-verified against ServUO.

## What it does

Resisting Spells reduces the chance and severity of harmful spells landing on you — direct
damage spells, and effects like paralyze, poison, and stat debuffs. It also raises your
minimum elemental resistances. It is a defensive staple for anyone who fights casters,
especially in PvP. See [spellcasting](/playing/spellcasting/).

## How to use it

Resisting Spells is **passive** — it applies automatically whenever a hostile spell targets
you. There is no activation; you simply benefit from having the skill when magic hits.

## How to train it

- **Low/high skill** — gains come from **being targeted by hostile magic**. A training
  partner casting harmless/weak spells at you, or fighting spellcasting monsters
  (see the [bestiary](/bestiary/)), raises it.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Dexterity |
| Title | Warder |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.25, Dex +0.25, Int +0.5 (per-use stat gain weights) |

From `Scripts/Misc/AOS.cs`, magic-damage taken is scaled by
`1 − ((MagicResist × 0.5 + 10) / 100)` — i.e. GM Magic Resistance cuts incoming spell damage
by roughly **60%** (`(100 × 0.5 + 10) = 60`). Resist also raises minimum resistances and
lowers the chance/severity of magical status effects.

## Related skills & synergies

- Appears on nearly every PvP-aware template — the Sword Dexxer, Tank Mage, Pure Mage, and
  Stealth builds on [seven-GM templates](/templates/seven-gm/) all carry it.
- **[Meditation](/skills/meditation/) / [Magery](/skills/magery/)** — the caster core it
  protects.

## See also

- [Spellcasting (how to play)](/playing/spellcasting/) · [Notoriety & PvP](/playing/notoriety-and-pvp/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
