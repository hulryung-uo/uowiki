---
title: Imbuing
description: Add magical properties to items.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 56 — Int/Str, no stat gain on use)"
  - "servuo: Scripts/Services/LootGeneration/Imbuing/Core/Imbuing.cs (CheckSoulForge; GetMaxProps = 5; GetMaxWeight 450 base/+50 exc/+50 ranged/+100 two-handed/500 jewelry; UnravelItem uses SkillName.Imbuing → MagicalResidue/EnchantedEssence/RelicFragment)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeachSkills: baseToSet = BaseFixedPoint/3, capped 420)"
  - "note: no uorenaissance.com entry — expansion-era skill, prose derived from ServUO + UO mechanics"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/56.gif" alt="Imbuing skill banner" width="160" />

Imbuing is an expansion-era (Stygian Abyss) crafting skill that adds magical properties to
items. The prose is community-derived from ServUO and general UO mechanics (no
uorenaissance.com entry) pending field verification; the stats table is source-verified
against ServUO. Behavior is expansion-specific — see [crafting](/playing/crafting/).

## What it does

Imbuing lets a crafter infuse a weapon, armor piece, or jewelry with chosen magical
properties — resistances, hit-chance, mana/stamina bonuses, slayer, and more — up to **5
properties** per item (`GetMaxProps`) and a total intensity "weight" cap of **450** on most
items (rising to **500** on jewelry and exceptional pieces, +50 for ranged, +100 for
two-handed weapons; `GetMaxWeight`). It is how players build gear to an exact specification
rather than relying on lucky loot. It works hand-in-hand with **unraveling** — which also runs
on the **Imbuing skill itself** (not Item Identification) at a soulforge, breaking magic loot
into the residues imbuing consumes.

## How to use it

Work at a **soulforge** (`CheckSoulForge` is required for both imbuing and unraveling).
Gather the ingredients each property needs — magical residue, enchanted essence, relic
fragments, plus special resources and gems — then imbue the chosen property onto the item.
Higher skill allows stronger property values and more total intensity. Unraveling yields
residue tiered by the item's weight and your skill: **magical residue** at low weight,
**enchanted essence** at mid weight, and **relic fragments** from high-weight items (weight
≥480, which requires 95+ Imbuing). See [crafting](/playing/crafting/).

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
  so a session never stops.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Artificer |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

Imbuing data and definitions live under `Scripts/Services/LootGeneration/Imbuing/`
(`Core/Imbuing.cs`). Item caps: max **5** properties (`GetMaxProps`) and a total intensity
weight of **450** (base), **+50** for exceptional quality, **+50** for ranged weapons, **+100**
for two-handed weapons, and a flat **500** for jewelry (`GetMaxWeight`). Per-property maximum
intensities are defined in `ItemPropertyInfo`.

## Related skills & synergies

- **[Item Identification](/skills/item-identification/)** — useful to identify magic loot
  before deciding what to unravel; note that the **unravel action itself uses the Imbuing
  skill**, not Item ID.
- **[Mysticism](/skills/mysticism/)** — Imbuing is a valid secondary skill supporting
  Mysticism's effectiveness.
- **[Blacksmithy](/skills/blacksmithy/) / [Tailoring](/skills/tailoring/)** — supply the
  exceptional base items imbuers enhance.

## See also

- [Crafting (how to play)](/playing/crafting/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
