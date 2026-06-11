---
title: Spirit Speak
description: Channel the dead; underpins necromancy and ghost-hearing.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 32)"
  - "servuo: Scripts/Skills/SpiritSpeak.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
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

Activate the skill. If a corpse is nearby it is consumed/channeled to heal you; the skill can
be used **while casting** other spells (it does not lock you out of magic). Ghosts become
intelligible to you while your Spirit Speak is high enough. See
[spellcasting](/playing/spellcasting/).

## How to train it

**No town trainer.** Spirit Speak is taught only by Healer-type NPCs, not ordinary town
vendors — for most players there is effectively no trainer, so train it by use. The check
fires on each Use (`Scripts/Skills/SpiritSpeak.cs`: `CheckSkill(SpiritSpeak, 0, 100)`, and a
second `CheckSkill(SpiritSpeak, 0.0, 120.0)` when you channel a corpse to heal).

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

From `Scripts/Skills/SpiritSpeak.cs`: the base check is `CheckSkill(SpiritSpeak, 0, 100)`,
and when channeling a nearby corpse the roll extends to 0.0–120.0 (so it stays useful past
GM). The amount healed scales with the skill; the corpse is marked channeled/consumed. Spirit
Speak is flagged usable while casting.

## Related skills & synergies

- **[Necromancy](/skills/necromancy/)** — Spirit Speak boosts many necro effects; the
  inseparable pairing. See the Necro-Mage build on [seven-GM templates](/templates/seven-gm/).
- **[Magery](/skills/magery/) + [Meditation](/skills/meditation/)** — the caster core a
  necro-mage layers it onto.

## See also

- [Death & resurrection](/playing/death-and-resurrection/) · [Spellcasting](/playing/spellcasting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
