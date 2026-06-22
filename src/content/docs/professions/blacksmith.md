---
title: Blacksmith
description: Mine ore, smelt ingots, and forge the arms and armor a shard runs on. Skills, the build, the smithing loop, what you make, and how it pays.
status: source-verified
sources:
  - "servuo: Scripts/Services/Craft/DefBlacksmithy.cs (MainSkill = Blacksmith)"
  - "servuo: Scripts/Services/Craft/Core/CraftItem.cs (success & exceptional chance from main skill only; Arms Lore not referenced)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs OnCraft (exceptional weapon: +35 DI, +ArmsLore/20 DI)"
  - "servuo: Scripts/Items/Equipment/Armor/BaseArmor.cs DistributeExceptionalBonuses (exceptional armor: +ArmsLore/20 random resist)"
  - "servuo: Scripts/Skills/ArmsLore.cs (active skill is item identification only)"
  - "servuo: Scripts/Mobiles/NPCs/Blacksmith.cs (BODType.Smith; SupportsBulkOrders needs Blacksmith skill > 0)"
  - "servuo: Scripts/Services/BulkOrders/ (BulkOrderSystem.cs banked points; Rewards/ runic hammers, ancient smithy hammers, power scrolls)"
  - "servuo: Config/Expansion.cfg (EJ)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The blacksmith turns rock into weapons and armor. You dig ore out of mountainsides, smelt
it into ingots, and pound those ingots into swords, shields, and full suits of plate at a
forge and anvil. It is the backbone craft of any fighting community — every warrior and
archer needs gear, and the smith is who makes and repairs it. Smithing pairs gathering
(Mining) with crafting (Blacksmithy) into one self-sufficient supply chain.

## Core skills

- [Mining](/skills/mining/) — dig ore from rock and mountainsides; the raw-material end of the chain.
- [Blacksmithy](/skills/blacksmithy/) — smelt ore into ingots and forge them into arms and armor; the headline skill.
- [Tinkering](/skills/tinkering/) — lets you craft your own smith hammers and tongs (and a forge/anvil deed), so you never have to buy tools.
- [Arms Lore](/skills/arms-lore/) — does **not** change how often you make **exceptional** pieces (the craft engine never checks it), but on this shard it adds bonus properties to items that come out exceptional: weapons get **+Arms Lore/20 Damage Increase** (+5% DI at GM, on top of the +35% an exceptional weapon already grants) and armor gets **+Arms Lore/20 extra resist points** (+5 at GM). A genuine, modest upgrade to every exceptional piece.

## The build

Follow the [Blacksmith Template](/templates/blacksmith/) for the stat spread (heavy
Strength for carrying ore and ingots), the skill order, and where to mine and smith at each
stage. The classic loadout is Mining + Blacksmithy + Tinkering + Arms Lore plus combat or
travel skills to round it out. For fitting seven grandmaster skills under the 700-point cap,
see [7x GM Templates](/templates/seven-gm/).

## How to craft

Read [Crafting](/playing/crafting/) for the craft menu and exceptional/quality mechanics,
and [Gathering Resources](/playing/gathering-resources/) for the mining loop. The
[Blacksmithy crafting](/crafting/blacksmithy/) page lists the full recipe catalog and
ingot requirements.

The loop: equip a [smith's hammer or tongs](/items/tools/), find an ore vein, and mine
until your pack is heavy with ore. Return to a forge, smelt the ore into ingots, then stand
at an anvil and forge weapons and armor from the craft menu. Higher Blacksmithy is what
raises your chance at exceptional items; Arms Lore then sweetens each exceptional piece with
extra damage (weapons) or resist (armor). Mining lower mountains gives
common iron; deeper or special veins yield colored ores (shadow, bronze, and up) that make
stronger, pricier gear.

## What you make / tools

- [Tools](/items/tools/) — a **smith's hammer** and **tongs** to work the forge; a tinker can make these for you.
- [Resources](/items/resources/) — **ore and ingots**, the iron-to-colored-ore chain that feeds every recipe.
- [Weapons](/items/weapons/) and the [weapon catalog](/items/catalog/weapons/) — swords, maces, and axes for fighters.
- [Armor](/items/armor/) and the [armor catalog](/items/catalog/armor/) and [shields](/items/catalog/shields/) — chain, ring, and plate suits.

**Bulk Order Deeds (BODs):** NPC smiths hand out deeds asking for a quantity of a given
item; filling them banks reward points you spend on rare tools and runic hammers. Working
BODs is a steady long-term income and gear source for a smith — see
[Bulk Order Deeds](/mechanics/bulk-order-deeds/) for the full point-and-reward system.

## Making a living

Smiths earn several ways: sell **bulk ingots** to other crafters, turn out **exceptional
weapons and armor** for player vendors and adventurers, and **repair** worn gear for a fee.
The biggest long game is **BOD rewards** — runic hammers from filled bulk orders let you
craft magical, high-resist gear that sells for serious gold. Move stock through
[Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Blacksmith Template](/templates/blacksmith/) — the full build and progression
- [Tinker](/professions/tinker/) — makes the tools a smith uses; a common companion craft
- [Warrior](/professions/warrior/) · [Archer](/professions/archer/) — your customers
- [Mining](/skills/mining/) · [Blacksmithy](/skills/blacksmithy/) · [Blacksmithy crafting](/crafting/blacksmithy/)
