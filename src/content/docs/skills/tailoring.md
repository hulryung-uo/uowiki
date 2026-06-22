---
title: Tailoring
description: Sew cloth and leather into clothing and armor.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 34 — Dex/Int, gain Str 0.38/Dex 1.63/Int 0.5)"
  - "servuo: Scripts/Services/Craft/DefTailoring.cs (InitCraftList: clothing, leather/studded/bone armor; GetChanceAtMin = 0.5)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = BaseFixedPoint/3, capped 420)"
  - "servuo: Scripts/Misc/SkillCheck.cs (GGSActive / CheckGGS)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/34.gif" alt="Tailoring skill banner" width="160" />

Tailoring is the cloth-and-leather [crafting skill](/playing/crafting/). The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Tailoring sews cloth and leather into clothing, bandages, and leather/studded/bone armor with
a sewing kit. Higher skill unlocks heavier armor types and better quality (exceptional pieces
carry bonus armor and can take a maker's mark). It is one of the two pillar crafter skills
(with [Blacksmithy](/skills/blacksmithy/)) and supplies the cloth and leather armor casters
and rogues favor.

## How to use it

Stock cloth (from bolts/cotton) and leather (tan hides from kills), then use a sewing kit to
open the crafting menu. Exceptional results need high skill and good tools. See
[crafting](/playing/crafting/).

## How to train it

**Quick start:** an NPC Tailor/Weaver teaches up to **one-third of its own skill, capped at
42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first. Then make the hardest piece
that still has a workable success %, stepping up as skill climbs:

- **Low skill** — sew simple cloth items and bandages; cheap and fast.
- **Mid skill** — basic leather armor.
- **High skill** — studded/bone armor and the hardest pieces for the steadiest gains and
  exceptional output.

Keep a **bulk supply of cloth/leather** so a session runs uninterrupted; GGS pays out the slow
late points as long as you keep sewing. Recipe thresholds live in
`Scripts/Services/Craft/DefTailoring.cs`. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Tailor |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +0.38, Dex +1.63, Int +0.5 (per-use stat gain weights) |

Tailoring is a pure crafting skill — no active target. Higher-grade leathers (from special
creatures) raise difficulty and reward.

## Related skills & synergies

- **[Blacksmithy](/skills/blacksmithy/)** — the partner pillar craft; see the Crafter build
  on [seven-GM templates](/templates/seven-gm/) and the [Blacksmith template](/templates/blacksmith/).
- **[Imbuing](/skills/imbuing/)** — enhances the exceptional armor a tailor makes.

## See also

- [Crafting (how to play)](/playing/crafting/) · [Tailoring crafting](/crafting/tailoring/)
- [Armor](/items/catalog/armor/) · [Clothing](/items/catalog/clothing/)
- [Bulk Order Deeds](/mechanics/bulk-order-deeds/) — runic sewing kits and the point-reward system
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
