---
title: Necromancy
description: Dark spells fueled by special reagents.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 49: Int primary / Str secondary, Necromancer, mastery)"
  - "servuo: Scripts/Spells/Necromancy/NecromancerSpell.cs (CastSkill=Necromancy, DamageSkill=SpiritSpeak)"
  - "servuo: Scripts/Spells/Necromancy/ (CurseWeapon, CorpseSkin, PainSpike, BloodOathSpell, WraithForm, LichForm, VampiricEmbrace, HorrificBeast, SummonFamiliar, AnimateDeadSpell, PoisonStrike, Strangle, Wither, Exorcism — reagents BatWing/GraveDust/DaemonBlood/NoxCrystal/PigIron)"
  - "servuo: Scripts/Mobiles/NPCs/Mulcivikh.cs (Umbra Necromancy trainer); Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeach AOS-only; baseToSet = BaseFixedPoint/3, capped 42.0)"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/49.gif" alt="Necromancy skill banner" width="160" />

Necromancy is an expansion-era (Age of Shadows) dark-magic school. The prose is
community-derived from ServUO and general UO mechanics (no uorenaissance.com entry) pending
field verification; the stats table is source-verified against ServUO. Behavior is
expansion-specific — see [magic schools](/playing/magic-schools/).

## What it does

Necromancy casts curses, summons, transformations, and damage: Curse Weapon, Corpse Skin,
Pain Spike, Blood Oath, Wraith/Lich/Vampiric/Horrific transformation forms, Summon Familiar,
Animate Dead, Poison Strike, Strangle, Wither, and Exorcism. It uses **necromantic
reagents** — bat wing, grave dust, daemon blood, nox crystal, pig iron — rather than the
standard eight. On this shard several effects are boosted by
[Spirit Speak](/skills/spirit-speak/).

## How to use it

Cast from the necromancer spellbook with the necro reagents and mana. The wraith/lich/etc.
**transformation forms** change your character and grant passive bonuses while active. See
[spellcasting](/playing/spellcasting/), [reagents](/items/reagents/), and
[magic schools](/playing/magic-schools/).

## How to train it

**Quick start:** the Umbra necromancer trainer (Mulcivikh) teaches Necromancy up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`; teachable on this EJ shard) — buy to
~30–42 first.

Necromancy rises from **casting its spells**, which consume reagents — keep a stock of nox
crystals, grave dust, bat wings, etc.:

- **Low skill** — cast the cheap spells (Curse Weapon, Corpse Skin) over and over; they're
  mana-light and train fast.
- **Mid/high skill** — cast steadily in combat; the higher spells and forms (e.g. Wraith Form,
  Vampiric Embrace) hold the gain window, and GGS pays out the slow late points. Some
  specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Necromancer |
| Mastery skill | Yes |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Spell implementations live under `Scripts/Spells/Necromancy/`. Several spells' magnitude and
the transformation forms' bonuses scale with Necromancy and [Spirit Speak](/skills/spirit-speak/);
exact numbers are expansion-specific and **unverified** here.

## Related skills & synergies

- **[Spirit Speak](/skills/spirit-speak/)** — boosts many necro effects and is the standard
  companion skill.
- **[Magery](/skills/magery/) + [Meditation](/skills/meditation/)** — the Necro-Mage build on
  [seven-GM templates](/templates/seven-gm/).
- **[Chivalry](/skills/chivalry/)** — thematic opposite; its anti-undead spells counter necro
  play.

## See also

- [Magic schools](/playing/magic-schools/) · [Spellcasting](/playing/spellcasting/)
- [Reagents](/items/reagents/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
