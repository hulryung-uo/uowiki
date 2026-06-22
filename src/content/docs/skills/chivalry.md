---
title: Chivalry
description: Paladin spells fueled by tithed gold.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 51: Str primary / Int secondary, Paladin, mastery)"
  - "servuo: Scripts/Spells/Chivalry/PaladinSpell.cs (RequiredTithing, Caster.TithingPoints; ComputePowerValue uses Karma + Chivalry.Fixed)"
  - "servuo: Scripts/Items/Functional/Ankhs.cs (TitheEntry — tithe gold at an ankh/shrine)"
  - "servuo: Scripts/Spells/Chivalry/ (CloseWounds, CleanseByFire, RemoveCurse, ConsecrateWeapon, HolyLight, DivineFury, EnemyOfOne, SacredJourney, NobleSacrifice, DispelEvil)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeach: AOS-only for Chivalry; baseToSet = BaseFixedPoint/3, capped 42.0)"
  - "servuo: Scripts/Mobiles/NPCs/KeeperOfChivalry.cs (Chivalry trainer); Config/Expansion.cfg (EJ => Core.AOS)"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/51.gif" alt="Chivalry skill banner" width="160" />

Chivalry is the paladin spell school, an expansion-era (Age of Shadows) skill powered by
tithed gold instead of reagents. The prose is community-derived from ServUO and general UO
mechanics (no uorenaissance.com entry) pending field verification; the stats table is
source-verified against ServUO. Behavior is expansion-specific — see
[magic schools](/playing/magic-schools/).

## What it does

Chivalry grants holy-knight abilities: self-healing (Close Wounds), curing
(Cleanse by Fire/Remove Curse), smiting undead and demons harder (Consecrate Weapon, Holy
Light), combat blessings (Divine Fury, Enemy of One), and travel/utility (Sacred Journey,
Noble Sacrifice). Effects scale with Chivalry skill and positive **Karma**, so paladins keep
their Karma high.

## How to use it

Tithe gold at a shrine to build a tithing pool, then cast Chivalry abilities from the Book of
Chivalry, which draw on that pool (and mana) instead of reagents. See
[spellcasting](/playing/spellcasting/) and [magic schools](/playing/magic-schools/).

## How to train it

**Quick start:** a Paladin/Keeper of Chivalry NPC teaches Chivalry up to **one-third of its
own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`; on this EJ shard the post-AOS schools are
teachable) — buy to ~30–42 first.

Chivalry rises from **casting its spells**, which consume **tithing points** rather than
reagents — donate gold at a shrine/holy place to stock your tithe pool first:

- **Low skill** — cast the cheap, always-useful spells (Divine Fury, Consecrate Weapon)
  repeatedly in combat against weak foes.
- **Mid/high skill** — cast steadily while fighting undead/demons where the school shines.
  Keep the tithing pool topped up, and GGS pays out the slow late points. Some specifics are
  **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Intelligence |
| Title | Paladin |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Chivalry spell implementations live under `Scripts/Spells/Chivalry/`. Many effects scale with
both Chivalry and Karma; exact per-spell numbers are expansion-specific and **unverified**
here.

## Related skills & synergies

- **A weapon skill + [Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/)** — Chivalry
  buffs a melee core (the paladin dexxer).
- **[Bushido](/skills/bushido/)** — the samurai-paladin hybrid stacks both schools.
- **[Necromancy](/skills/necromancy/)** — thematically opposed; Chivalry's anti-undead/demon
  spells counter necro play.

## See also

- [Magic schools](/playing/magic-schools/) · [Spellcasting](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
