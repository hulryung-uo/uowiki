---
title: How to Play — Gathering Resources
description: How to harvest raw materials — mining ore into ingots, lumberjacking logs into boards, fishing, skinning corpses for leather, the cloth chain, and cartography/treasure gathering. Tool, action, yield, location, and skill gate for each.
status: unverified
sources:
  - "servuo: Scripts/Services/Harvest/* (mining, lumberjacking, fishing harvest systems)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (corpse hide/wool/fur/meat carving yields)"
  - "servuo: Scripts/Services/Craft/Core/Resmelt.cs (smelting ore to ingots at a forge)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This guide covers **gathering** — harvesting the raw materials that feed
[crafting](/playing/crafting/). For each resource type it lists the **tool**, the
**action**, the **yield**, **where** to do it, and the **skill gate**. The exact skill
numbers and the colored/tiered resource tables live on the
[resources reference](/items/resources/) — link there rather than restating numbers, which
vary by tier and shard config.

**Definitions used on this page:**
- **Harvest action** — using a gathering tool on a valid target tile (a mountain wall, a
  tree, water) to pull resources.
- **Yield** — what you get per successful harvest (raw ore, logs, fish, etc.).
- **Refining** — converting a raw yield into a usable crafting material (ore → ingots,
  logs → boards, raw fiber → cloth).
- **Skill gate** — the minimum skill that lets you harvest a resource at all; higher tiers
  need more skill.

## Mining (ore → ingots)

[Mining](/skills/mining/) harvests metal ore from the ground and turns it into the
**ingots** smiths need.

- **Tool:** a **pickaxe** or **shovel** (from a blacksmith/tinker or the
  [tools catalog](/items/catalog/tools/)).
- **Action:** double-click the tool and target a **mountainside, cave wall, or rock**
  (or, with a shovel, certain ground tiles). Your character digs and, on success, **ore**
  drops into your pack.
- **Refine:** carry the ore to a **forge** and use it there to **smelt** it into
  **ingots** (the smelt step is part of the smithing/craft system — see
  [Resmelt.cs] in source and the [Blacksmithy](/skills/blacksmithy/) page). Ingots are the
  actual crafting material.
- **Where:** mountains, caves, and dungeons. Deeper/dungeon spots and certain tiles yield
  the higher tiers.
- **Skill gate:** plain **iron** ore needs minimal skill; **colored ore tiers** (the more
  valuable metals) each require progressively higher [Mining](/skills/mining/) and let
  smiths craft stronger, colored gear. The full ore tier list and skill numbers are on the
  [resources reference](/items/resources/).

Mining is also the entry to **stone** for [Masonry](/crafting/masonry/) and **sand** for
[Glassblowing](/crafting/glassblowing/) where those are enabled.

## Lumberjacking (logs → boards)

[Lumberjacking](/skills/lumberjacking/) harvests wood for carpenters and fletchers.

- **Tool:** a **hatchet** or **axe** (any axe-type weapon works; from a smith or the
  [tools catalog](/items/catalog/tools/)).
- **Action:** double-click the tool and target a **tree**. On success you get **logs**.
- **Refine:** use the tool (or a saw) to turn **logs into boards**, the material
  [Carpentry](/skills/carpentry/) and [Bowcraft/Fletching](/skills/bowcraft-fletching/)
  consume.
- **Where:** forests and wooded areas everywhere. Different regions hold the higher
  **wood tiers**.
- **Skill gate:** ordinary wood needs little skill; **colored/special wood tiers** each
  need more [Lumberjacking](/skills/lumberjacking/) and produce better crafted items. See
  the [resources reference](/items/resources/) for the wood tier list and numbers.

Note: an axe in hand also serves as a weapon, so a lumberjack can fight off wildlife while
harvesting (see [Combat Basics](/playing/combat-basics/)).

## Fishing (pole → fish and more)

[Fishing](/skills/fishing/) harvests from water.

- **Tool:** a **fishing pole** (from provisioners or the [tools catalog](/items/catalog/tools/)).
- **Action:** double-click the pole and target a **water tile** (or fish from a boat). On
  success you reel in **fish**, which [Cooking](/skills/cooking/) turns into food.
- **Beyond fish:** higher fishing skill and the right spots can land **big fish**, pull up
  **message-in-a-bottle SOS** quests (leading to sunken treasure), and **treasure/booty**
  from deep water. These are the fishing endgame.
- **Where:** any water — rivers, lakes, coastlines, and the open sea from a boat (deep-sea
  content needs a boat; see [Movement & travel](/playing/movement-and-travel/)).
- **Skill gate:** basic fishing needs almost no skill; **big fish, SOS recovery and deep-sea
  hauls** gate behind higher [Fishing](/skills/fishing/). See the
  [resources reference](/items/resources/) for specifics.

## Skinning corpses (hides → leather)

Slain animals and monsters can be **carved** for crafting materials — the leather supply
for [Tailoring](/skills/tailoring/).

- **Tool:** any **bladed weapon or a skinning knife/dagger**.
- **Action:** double-click the blade and target a fresh **corpse**. Depending on the
  creature you get **hides**, **meat**, **wool/fur**, **feathers**, or **scales** (per the
  carve yields in `BaseCreature.cs`). Summoned, bonded-pet, or already-carved corpses give
  nothing.
- **Refine:** **tan hides into leather** (use the hides, or visit a tanner/leather-working
  station). Leather is the material tailors use for armor; raw **meat** is cooking fodder.
- **Where:** anywhere you hunt — the [bestiary](/bestiary/) pages note which creatures drop
  hides, wool, fur, scales, or feathers.
- **Skill gate:** carving a corpse needs no skill, but the **colored/exotic leather tiers**
  come from specific (often dangerous) creatures and require higher [Tailoring](/skills/tailoring/)
  to work. See the [resources reference](/items/resources/).

## The cloth chain (fiber → cloth)

Cloth for tailoring comes from a multi-step **cloth chain** rather than a single harvest:

1. **Gather raw fiber:**
   - **Cotton** — picked from **cotton plants** on farms.
   - **Flax** — harvested from **flax plants**.
   - **Wool** — **shear a sheep** (use scissors/shears on a live sheep) or carve wool/fur
     from certain creatures.
2. **Spin into thread/yarn:** use a **spinning wheel** on the raw cotton/flax (→ thread) or
   wool (→ yarn).
3. **Weave into cloth:** use a **loom** on the thread/yarn to produce a **bolt of cloth**.
4. **Cut into cloth:** use **scissors** on the bolt to get usable **cloth**, the
   tailoring material.

Spinning wheels and looms are found in tailor shops and player houses. The full chain and
any skill notes are on the [resources reference](/items/resources/).

## Cartography and treasure gathering (brief)

A few other "gathering" loops feed off skills rather than tiles:

- **Cartography** ([/crafting/cartography/](/crafting/cartography/)) — craft and **decode
  treasure maps**. A decoded map leads to a **buried treasure chest** you dig up (often
  needing Mining to dig and combat to clear the guardians). The chest yields gold, gems,
  reagents and rare crafting materials.
- **Fishing SOS / sunken treasure** (above) — the seafaring equivalent.
- **Looting and gem/reagent gathering** — monster corpses and dungeon spawns drop **gems,
  reagents and special materials** used in [crafting](/playing/crafting/); gather them as
  you hunt.

## Putting it together

The gathering-to-crafting pipeline, end to end:

1. **Harvest** the raw yield (ore, logs, fish, hides, fiber).
2. **Refine** it into a crafting material (ingots, boards, leather, cloth).
3. **Craft** finished goods from that material — see [Crafting](/playing/crafting/).

Higher gathering skill unlocks the **colored/tiered resources** that, in turn, let
crafters make better and colored items. Train the gathering skill on common resources
first, then chase the higher tiers as your skill climbs (see [Skill gain](/mechanics/skill-gain/)).

## See also

- Skill pages: [Mining](/skills/mining/) · [Lumberjacking](/skills/lumberjacking/) ·
  [Fishing](/skills/fishing/) · [Tailoring](/skills/tailoring/)
- [Resources reference](/items/resources/) — ore/wood/leather/cloth tiers and skill numbers
- [Crafting](/playing/crafting/) — turning materials into goods ·
  [resources catalog](/items/catalog/resources/) · [tools catalog](/items/catalog/tools/)
- [Movement & travel](/playing/movement-and-travel/) — boats for deep-sea fishing
- [Combat Basics](/playing/combat-basics/) — defending yourself while you gather
- [Skill gain](/mechanics/skill-gain/)
