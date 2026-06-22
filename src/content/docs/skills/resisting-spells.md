---
title: Resisting Spells
description: Shrug off hostile magic and reduce its effects.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 26 — Resisting Spells: Str/Dex, gain Str 0.25/Dex 0.25/Int 0.5, title Warder, mastery=false)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (GetMinResistance: MagicResist raises minimum elemental resistances; min 40 at GM)"
  - "servuo: Scripts/Spells/Base/SpellHelper.cs (GetOffsetScalar / GetOffset: MagicResist reduces stat-curse magnitude; CheckSkill(MagicResist) fires on curse target)"
  - "servuo: Scripts/Spells/Base/Spell.cs (GetDamageScalar: pre-AOS, MagicResist reduces spell damage vs EvalInt; GetResistSkill)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/26.gif" alt="Resisting Spells skill banner" width="160" />

Resisting Spells (Magic Resistance) lowers the impact of hostile magic. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and the damage-reduction note below are
source-verified against ServUO.

## What it does

Resisting Spells gives you a chance to resist harmful spells and reduces the severity of
effects like paralyze, poison, and stat debuffs. It also raises your minimum elemental
resistances. (On older pre-AOS rule sets it additionally scaled down direct spell damage;
under our AOS+ shard that damage scalar is off — see the numbers below.) It is a defensive
staple for anyone who fights casters, especially in PvP. See
[spellcasting](/playing/spellcasting/).

## How to use it

Resisting Spells is **passive** — it applies automatically whenever a hostile spell targets
you. There is no activation; you simply benefit from having the skill when magic hits.

## How to train it

**Train by being hit by spells.** Resisting Spells is conventionally not stocked on NPC teach
lists, so in practice there is no buy-up shortcut — you train it by **being targeted by
hostile magic**. The skill check fires on the *target* of a spell
(`Scripts/Spells/Base/MagerySpell.cs`: `CheckResisted` →
`target.CheckSkill(SkillName.MagicResist, ...)`; curses also check it via `SpellHelper.cs`),
and only while your resist is below the spell's window.

- **Low/high skill** — have a training partner cast harmless/weak spells *at you*, or fight
  spellcasting monsters (see the [bestiary](/bestiary/)) and let them blast you. Each hostile
  spell that lands on you rolls a gain. GGS guarantees the slow late points as long as the
  spells keep coming.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Strength |
| Secondary stat | Dexterity |
| Title | Warder |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.25, Dex +0.25, Int +0.5 (per-use stat gain weights) |

On our shard (ServUO, AOS+), Resisting Spells works three ways:

- **Chance to resist effect spells.** `MagerySpell.CheckResisted` rolls a resist chance from
  your MagicResist skill (`GetResistPercent`) against the spell's circle. A successful roll
  reduces or negates effects like paralyze, poison, and stat curses. The skill-gain check
  fires on the *target* only while your resist is below the spell's window
  (`MagerySpell.cs`: `target.CheckSkill(SkillName.MagicResist, …)`).
- **Raises minimum elemental resistances.** `PlayerMobile.GetMinResistance` floors your
  Physical/Fire/Cold/Poison/Energy resistances based on Magic Resistance: at **GM (100)** the
  minimum is **40**, climbing further above GM.
- **Reduces stat-curse magnitude.** For Clumsy/Feeblemind/Weaken/Curse, higher MagicResist
  shrinks the stat penalty (`SpellHelper.GetOffsetScalar`).

Note: in pre-AOS rule sets MagicResist *also* directly scaled down incoming spell damage
(`Spell.GetDamageScalar`, EvalInt vs. resist), but that damage scalar is disabled under AOS+
(`if (!Core.AOS)`). The `1 − ((MagicResist × 0.5 + 10) / 100)` formula sometimes quoted from
`AOS.cs` applies only to Blood Oath damage **reflected back vs. creatures**, not to general
incoming spell damage — do not treat it as a flat 60% spell-damage cut.

## Related skills & synergies

- Appears on nearly every PvP-aware template — the Sword Dexxer, Tank Mage, Pure Mage, and
  Stealth builds on [seven-GM templates](/templates/seven-gm/) all carry it.
- **[Meditation](/skills/meditation/) / [Magery](/skills/magery/)** — the caster core it
  protects.

## See also

- [Spellcasting (how to play)](/playing/spellcasting/) · [Notoriety & PvP](/playing/notoriety-and-pvp/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
