---
title: Spirit Speak
description: Channel the dead; underpins necromancy and ghost-hearing.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 32: Int primary / Str secondary, Medium, IntGain 1.0, UseWhileCasting=true, not mastery)"
  - "servuo: Scripts/Skills/SpiritSpeak.cs (AOS: BeginSpiritSpeak; corpse channel heals RandomMinMax(min,max), min=1+skill*0.25; 0 mana with corpse, 10 mana without; CheckSkill 0-120; blocks if Spell.IsCasting)"
  - "servuo: Scripts/Spells/Necromancy/NecromancerSpell.cs (DamageSkill = SpiritSpeak — boosts necro spells)"
  - "servuo: Scripts/Mobiles/NPCs/Healer.cs (CheckTeach restricts to Forensics/Healing/SpiritSpeak/Swords)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/32.gif" alt="Spirit Speak skill banner" width="160" />

Spirit Speak channels spiritual energy and underpins necromancy. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and skill-check note below are source-verified
against ServUO.

## What it does

Spirit Speak lets you understand the speech of **ghosts** (dead players, who otherwise sound
like "oOOoo") and **channel energy from nearby corpses to heal yourself**. On this shard it
also boosts many [Necromancy](/skills/necromancy/) effects, so it is the standard companion
skill for a necromancer. See [death & resurrection](/playing/death-and-resurrection/).

## How to use it

Activate the skill. If a fresh corpse is within 3 tiles it is channeled (marked consumed) and
heals you for **free**; with no corpse nearby you channel your own energy for **10 mana**. The
skill is flagged usable while a spell is queued (`UseWhileCasting`), but the handler refuses if
you are **actively casting** ("You are already casting a spell."). Ghosts become intelligible
to you while your Spirit Speak is high enough. See [spellcasting](/playing/spellcasting/).

## How to train it

**No town trainer.** Spirit Speak is taught only by Healer-type NPCs (their `CheckTeach`
allows just Forensics, Healing, Spirit Speak, and Swordsmanship), not ordinary town vendors —
for most players there is effectively no trainer, so train it by use. On this AOS-era (EJ)
shard the skill check fires when you channel — `CheckSkill(SpiritSpeak, 0.0, 120.0)` in
`Scripts/Skills/SpiritSpeak.cs` — so it keeps gaining past GM. (The legacy
`CheckSkill(SpiritSpeak, 0, 100)` path only runs on a non-AOS server.)

- **Low/high skill** — Use the skill repeatedly, ideally **next to a fresh corpse** so the
  channel-heal fires (channeling both heals you and trains). Fighting and killing creatures
  produces a steady supply of corpses; just kill, channel, repeat. GGS guarantees the slow
  late points as long as you keep using it.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Medium |
| Mastery skill | No |
| Gain notes | skill-ups can raise Int +1 (per-use stat gain weights) |

From `Scripts/Skills/SpiritSpeak.cs` (AOS path): each channel rolls
`CheckSkill(SpiritSpeak, 0.0, 120.0)`, so it stays useful past GM. The heal is
`RandomMinMax(min, max)` where `min = 1 + (SpiritSpeak.Value × 0.25)` and `max = min + 4` —
i.e. ~26–30 at 100 skill — and the success roll is `SpiritSpeak.Value / 100`. Channeling a
nearby corpse costs **0 mana** and marks the corpse consumed (hued); with no corpse it costs
**10 mana**. The skill is flagged `UseWhileCasting`, but the handler still rejects use mid-cast.
(The legacy `CheckSkill(SpiritSpeak, 0, 100)` is the non-AOS branch.)

## Related skills & synergies

- **[Necromancy](/skills/necromancy/)** — Spirit Speak boosts many necro effects; the
  inseparable pairing. See the Necro-Mage build on [seven-GM templates](/templates/seven-gm/).
- **[Magery](/skills/magery/) + [Meditation](/skills/meditation/)** — the caster core a
  necro-mage layers it onto.

## See also

- [Death & resurrection](/playing/death-and-resurrection/) · [Spellcasting](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
