---
title: Imbuing
description: Add magical properties to items.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 56)"
  - "servuo: Scripts/Services/LootGeneration/Imbuing/"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/56.gif" alt="Imbuing skill banner" width="160" />

Imbuing is an expansion-era (Stygian Abyss) crafting skill that adds magical properties to
items. The prose is community-derived from ServUO and general UO mechanics (no
uorenaissance.com entry) pending field verification; the stats table is source-verified
against ServUO. Behavior is expansion-specific — see [crafting](/playing/crafting/).

## What it does

Imbuing lets a crafter infuse a weapon, armor piece, or jewelry with chosen magical
properties — resistances, hit-chance, mana/stamina bonuses, slayer, and more — up to per-item
intensity and property-count caps. It is how players build gear to an exact specification
rather than relying on lucky loot. It works hand-in-hand with **unraveling** (via
[Item Identification](/skills/item-identification/)) to break magic loot into the residues
imbuing consumes.

## How to use it

Work at a **soulforge**. Gather the ingredients each property needs — magical residue,
enchanted essence, relic fragments, plus special resources and gems — then imbue the chosen
property onto the item. Higher skill allows stronger property values and more total
intensity. See [crafting](/playing/crafting/).

## How to train it

**Quick start:** an SA Imbuing trainer NPC (in the gargoyle city of Ter Mur) teaches Imbuing
up to **one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first if you can reach
one (few NPCs have it).

Imbuing rises from **imbuing properties onto items at the Soul Forge** — work the hardest
intensity that still has a workable success %, stepping up as skill climbs:

- **Low/mid skill** — imbue cheap, low-intensity properties onto disposable rings/bracelets.
- **High skill** — imbue higher-intensity properties; the highest tiers hold the gain window
  late, and GGS pays out the slow late points. Keep a **bulk supply of imbuing ingredients**
  so a session never stops. Some specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Artificer |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Imbuing data and definitions live under `Scripts/Services/LootGeneration/Imbuing/`. Intensity
and property caps are expansion-specific; exact per-property values are **unverified** here.

## Related skills & synergies

- **[Item Identification](/skills/item-identification/)** — unravels magic loot into the
  residue/essence/relic ingredients imbuing consumes.
- **[Mysticism](/skills/mysticism/)** — Imbuing is a valid secondary skill supporting
  Mysticism's effectiveness.
- **[Blacksmithy](/skills/blacksmithy/) / [Tailoring](/skills/tailoring/)** — supply the
  exceptional base items imbuers enhance.

## See also

- [Crafting (how to play)](/playing/crafting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
