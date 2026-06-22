---
title: Alchemist
description: Grind reagents into potions — heal, cure, refresh, explosion, and more. Skills, the build, the brewing loop, what you make, and how it earns.
status: source-verified
sources:
  - "servuo: Scripts/Services/Craft/DefAlchemy.cs (MainSkill = Alchemy; potions consume reagents + 1 empty Bottle; output 1 per craft; standard potions need no Magery)"
  - "servuo: Scripts/Services/Craft/Core/CraftItem.cs (no skill-scaled batch yield for potions — UseAllRes not set)"
  - "servuo: Scripts/Items/Consumables/BasePotion.cs EnhancePotions (potion potency scales with the DRINKER's Alchemy, not the crafter's)"
  - "servuo: Scripts/Items/Consumables/BaseExplosionPotion.cs (explosion damage adds the thrower's Alchemy bonus)"
  - "servuo: Config/Expansion.cfg (EJ)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The alchemist brews potions. With a mortar and pestle and a pack full of reagents, you
distill the bottles every fighter, tamer, and adventurer relies on — heal, cure, and refresh
to stay alive, explosion and poison to deal damage. Potions are consumed constantly across a
shard, so a good alchemist never runs short of buyers. The craft is cheap to start and pairs
well with Magery, which shares the same reagent supply.

## Core skills

- [Alchemy](/skills/alchemy/) — the headline skill: combine reagents in a mortar and pestle to brew potions.
- [Magery](/skills/magery/) — optional but natural companion; it draws on the same [reagents](/items/reagents/) and lets you both brew and cast.

## The build

There is no dedicated alchemist template yet — Alchemy slots onto a caster or crafter
character, most often a mage (they share reagents) or a multi-craft build. Build it into a
multi-skill spread and see [7x GM Templates](/templates/seven-gm/) for fitting Alchemy under
the 700-point cap.

## How to craft

Read [Crafting](/playing/crafting/) for the craft menu and exceptional mechanics. The full
potion recipe catalog and reagent requirements live on the
[Alchemy crafting](/crafting/alchemy/) page.

The loop: stock the [reagents](/items/reagents/) each potion needs, hold a **mortar and
pestle**, and select a potion from the craft menu. Each brew consumes reagents plus one
**empty bottle** and yields a single potion (keep a stack of empty bottles on hand). Buy
reagents from NPC mages or grow/gather your own to cut costs.

Note on potency: in this ServUO, brewing a potion at higher Alchemy does **not** make it
stronger or produce extras — the recipe yields one bottle regardless of skill. A potion's
effect is set by the **drinker's** Alchemy when consumed (`BasePotion.EnhancePotions`), and
thrown explosion/conflagration potions add the **thrower's** Alchemy to their damage. So
Alchemy benefits whoever *uses* the potion; as a maker, your skill mainly governs the success
chance and unlocks the higher-tier recipes (greater heal, deadly poison, greater explosion).

## What you make / tools

- [Tools](/items/tools/) — a **mortar and pestle** is the alchemist's one essential tool; a tinker can make it.
- [Reagents](/items/reagents/) — the inputs: black pearl, nightshade, garlic, ginseng, and the rest; each potion has its own recipe.
- [Potions catalog](/items/catalog/potions/) — your output: **heal, cure, refresh, agility, strength, explosion, and poison** potions.
- **Kegs** (crafted by a [carpenter](/professions/carpenter-bowyer/)) store potions in bulk so you can pour many bottles into one container.

## Making a living

Alchemists earn by selling **bulk consumables** — stacks of heal, cure, and refresh potions
are perpetual demand from warriors, archers, and tamers who burn through them in every fight.
**Explosion and deadly poison** potions sell to PvPers and dungeon farmers for offense.
Pour stock into kegs for easy bulk sale and move it through
[Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [7x GM Templates](/templates/seven-gm/) — fitting alchemy onto a build
- [Mage](/professions/mage/) — shares the reagent supply; a common pairing
- [Carpenter & Bowyer](/professions/carpenter-bowyer/) — crafts the kegs alchemists store potions in
- [Alchemy](/skills/alchemy/) · [Alchemy crafting](/crafting/alchemy/) · [Reagents](/items/reagents/) · [Potions catalog](/items/catalog/potions/)
