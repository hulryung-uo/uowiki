---
title: Focus
description: Passive stamina and mana regeneration.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 50 — Focus: Dex/Int, no stat gain, title Driven, mastery=false)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = ourSkill.BaseFixedPoint / 3, capped 420 = 42.0)"
  - "servuo: Scripts/Misc/RegenRates.cs (Focus boosts stam regen by Focus*0.1; mana regen via focusBonus = Focus/200 (ML) / Focus*0.05 (AOS), added independently of the armor penalty that zeroes meditation)"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-22
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
  recover**: cast or sprint to drain, then let it tick back, repeatedly. The skill check
  fires inside the stamina and mana regen ticks (`RegenRates.CheckBonusSkill` for
  `SkillName.Focus`), so it climbs in the background whenever your stamina or mana is below
  max and regenerating; GGS guarantees the slow late points as long as you keep acting.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Driven |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

The Focus skill's regeneration is implemented in `Scripts/Misc/RegenRates.cs` (not
`Scripts/Abilities/Focus.cs`, which is an unrelated weapon "Rage Focusing" buff). Focus adds
`Focus.Value × 0.1` points to the stamina-regen rate, and contributes to mana regen as
`focusBonus = Focus / 200` (Mondain's Legacy) or `Focus × 0.05` (AOS). Crucially, Focus's
mana bonus is added **independently** of the armor penalty that zeroes the
[Meditation](/skills/meditation/) bonus — so unlike Meditation, Focus's mana regen is **not**
blocked by wearing metal armor, which is its main appeal on armored hybrids.

## Related skills & synergies

- **[Meditation](/skills/meditation/)** — the two stack on casters who want maximum mana
  regen (and Focus keeps working in heavy armor).
- **[Mysticism](/skills/mysticism/)** — Focus is a valid secondary skill that supports
  Mysticism's effectiveness.

## See also

- [Meditation & mana](/playing/meditation-and-mana/) · [Magic schools](/playing/magic-schools/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
