---
title: Alchemy
description: Brew potions and explosive concoctions from reagents.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Services/Craft/DefAlchemy.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/0.gif" alt="Alchemy skill banner" width="160" />

Alchemy is a [crafting skill](/playing/crafting/) that turns ground reagents and empty
bottles into potions. The prose here is community-derived (paraphrased from the
uorenaissance.com skill list plus ServUO behavior) pending field verification; the stats
table is source-verified against ServUO.

## What it does

Alchemy lets you brew consumable potions: cure, heal, and refresh; strength and agility
tonics; night sight; and the offensive explosion and conflagration potions thrown in PvP
and PvM. It is the supply line behind any character who leans on potions instead of (or
alongside) spells, and a steady gold earner because potions are always in demand.

## How to use it

Stock a mortar and pestle plus the reagents the recipe calls for and the empty bottles to
hold the result. Double-click the mortar and pestle to open the crafting menu, pick the
potion, and mix. Higher skill unlocks stronger potions, raises success chance, and can yield
more bottles per batch. See [crafting](/playing/crafting/) for the general crafting loop and
[reagents](/items/reagents/) for what each potion consumes.

## How to train it

**Quick start:** buy up from an NPC Alchemist — a town trainer teaches any skill it knows up
to **one-third of its own value, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`, hard-capped at 420). Pay an alchemist
up to ~30–42, then train by mixing.

Then train the way you train any [crafting skill](/playing/crafting/): repeatedly mix the most
difficult potion you can still attempt with a reasonable success rate, then step up as the
skill climbs.

- **Low skill** — mix refresh and lesser cure/heal potions; cheap reagents, frequent gains.
- **Mid skill** — graduate to greater cure/heal and the agility/strength tonics.
- **High skill** — deadly/greater potions and explosion potions give the steadiest late
  gains and the best resale value.

Keep a bulk reagent supply and empty bottles on hand so a session is not interrupted; drink or
vendor the output so you can keep mixing. GGS is active here, so even at high skill *keep
brewing the hardest potion you still succeed at* and the guaranteed-gain timer pays out the
slow late points. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Alchemist |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +0.5, Int +0.5 (per-use stat gain weights) |

Recipes and their skill requirements are defined in
`Scripts/Services/Craft/DefAlchemy.cs`. Alchemy is a pure crafting skill — there is no
active "use" target; all progress comes from the crafting menu.

## Related skills & synergies

- **[Cooking](/skills/cooking/)** and **[Inscription](/skills/inscription/)** — the other
  reagent/consumable crafts a potion-seller often carries.
- **[Magery](/skills/magery/)** and **[Taste Identification](/skills/taste-identification/)**
  — Magery casters lean on cure/heal/refresh potions; Taste ID spots poisoned consumables.
- **[Poisoning](/skills/poisoning/)** — alchemists brew the poison potions a poisoner then
  applies to blades.

## See also

- [Crafting (how to play)](/playing/crafting/)
- [Reagents](/items/reagents/) · [Potions catalog](/items/catalog/potions/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
