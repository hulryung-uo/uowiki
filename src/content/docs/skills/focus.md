---
title: Focus
description: Passive stamina and mana regeneration.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Abilities/Focus.cs"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/50.gif" alt="Focus skill banner" width="160" />

Focus is an expansion-era (Age of Shadows) passive regeneration skill. The prose is
community-derived from ServUO and general UO mechanics (no uorenaissance.com entry) pending
field verification; the stats table is source-verified against ServUO. Behavior is
expansion-specific — see [magic schools](/playing/magic-schools/) and
[meditation & mana](/playing/meditation-and-mana/).

## What it does

Focus passively increases your stamina and mana regeneration rates. It is a low-maintenance
support skill that asks nothing of you in play — it just makes your bars refill faster, which
is why it is often slotted onto hybrid templates that want extra sustain without the armor
restrictions of [Meditation](/skills/meditation/).

## How to use it

Focus is entirely passive — there is no target or activation. Once you have the skill, the
regeneration bonus applies at all times. It also serves as the secondary skill that supports
[Mysticism](/skills/mysticism/). See [meditation & mana](/playing/meditation-and-mana/).

## How to train it

**Quick start:** Focus is a common NPC skill (many warrior and mage NPCs have it), so a
trainer can teach it up to **one-third of its own skill, capped at 42.0**
(`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

- Focus gains as you regenerate mana/stamina, so the practical method is to **spend and
  recover**: cast or sprint to drain, then let it tick back, repeatedly. There is no targeted
  grind — it climbs in the background while you play, and GGS guarantees the slow late points
  as long as you keep acting. Specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Driven |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Focus implementation is in `Scripts/Abilities/Focus.cs`. Unlike [Meditation](/skills/meditation/),
Focus's mana regen is **not** blocked by wearing metal armor, which is its main appeal on
armored hybrids. Exact regen-per-skill numbers are expansion-specific and **unverified**
here.

## Related skills & synergies

- **[Meditation](/skills/meditation/)** — the two stack on casters who want maximum mana
  regen (and Focus keeps working in heavy armor).
- **[Mysticism](/skills/mysticism/)** — Focus is a valid secondary skill that supports
  Mysticism's effectiveness.

## See also

- [Meditation & mana](/playing/meditation-and-mana/) · [Magic schools](/playing/magic-schools/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
