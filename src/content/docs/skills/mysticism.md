---
title: Mysticism
description: Gargoyle-era mysticism spells.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 55)"
  - "servuo: Scripts/Spells/Mysticism/"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/55.gif" alt="Mysticism skill banner" width="160" />

Mysticism is an expansion-era (Stygian Abyss) spell school. The prose is community-derived
from ServUO and general UO mechanics (no uorenaissance.com entry) pending field verification;
the stats table is source-verified against ServUO. Behavior is expansion-specific — see
[magic schools](/playing/magic-schools/).

## What it does

Mysticism is a versatile spell school covering healing (Healing Stone, Cleansing Winds),
direct damage (Nether Bolt, Eagle Strike, Hail Storm, Nether Cyclone), summons (Animated
Weapon, Rising Colossus), and debuffs/utility (Sleep, Mass Sleep, Enchant, Stone Form,
Spell Trigger). Its spell effectiveness is **supported by a secondary skill** — either
[Focus](/skills/focus/) or [Imbuing](/skills/imbuing/) — whichever is higher contributes.

## How to use it

Cast from the Book of Mysticism using reagents and mana. Spell power scales with Mysticism
plus the higher of your Focus or Imbuing. See [spellcasting](/playing/spellcasting/) and
[magic schools](/playing/magic-schools/).

## How to train it

- **Low skill** — cast the cheap spells (Nether Bolt, Healing Stone) repeatedly.
- **Mid/high skill** — cast steadily in combat; the stronger spells hold the gain window
  late. Specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Intelligence |
| Title | Mystic |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Note the **Strength-primary** stat (unusual for a caster school). Spell implementations live
under `Scripts/Spells/Mysticism/`. The Focus-or-Imbuing support and exact damage numbers are
expansion-specific and **unverified** here.

## Related skills & synergies

- **[Focus](/skills/focus/) or [Imbuing](/skills/imbuing/)** — the supporting secondary skill
  that boosts Mysticism's effectiveness (whichever is higher).
- **[Magery](/skills/magery/) + [Meditation](/skills/meditation/)** — common hybrid pairing
  on a "mystic-mage"; see the Necro-Mage/Spellweaver/Mystic note on
  [seven-GM templates](/templates/seven-gm/).

## See also

- [Magic schools](/playing/magic-schools/) · [Spellcasting](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
