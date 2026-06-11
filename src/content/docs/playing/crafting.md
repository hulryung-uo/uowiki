---
title: How to Play — Crafting
description: The universal crafting loop — tool to menu to category to item to make — plus per-trade entry points, materials, exceptional quality and maker's marks, failure and material loss, repairing, runic tools, enhancing and Bulk Order Deeds.
status: unverified
sources:
  - "servuo: Scripts/Services/Craft/Core/CraftGump.cs, CraftItem.cs (craft menu flow, exceptional chance, maker's mark)"
  - "servuo: Scripts/Services/Craft/Core/QueryMakersMarkGump.cs, Repair.cs, Enhance.cs, Resmelt.cs (mark/repair/enhance/smelt features)"
  - "servuo: Scripts/Services/Craft/Def*.cs (per-trade craft definitions: Blacksmithy, Tailoring, Tinkering, Carpentry, BowFletching, Inscription, Cooking, Alchemy, Cartography, Masonry, Glassblowing)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This guide explains how **crafting** works in general — the loop that every trade skill
shares — and then points you to the right tool, skill page, and recipe list for each
trade. Crafting turns raw materials (gathered or bought) into finished goods: weapons,
armor, clothing, furniture, tools, food, scrolls, potions, and more. For where the raw
materials come from, see [Gathering resources](/playing/gathering-resources/) and the
[resources reference](/items/resources/). For a worked starting build, see the
[Blacksmith template](/templates/blacksmith/).

**Definitions used on this page:**
- **Trade tool** — the item you double-click to craft (a smith's hammer, sewing kit,
  tinker's tools, etc.). Each trade has its own tool.
- **Craft menu / craft gump** — the window that opens when you use a trade tool. It lists
  **categories** of items and the **items** within each.
- **Exceptional** — the highest quality result, giving better stats and the option to
  stamp your name on the item.
- **Resource / material** — the ingredients consumed when you craft (ingots, boards,
  leather, cloth, reagents, etc.).

## The universal crafting loop

Every trade follows the same five steps (verified against the craft system in
`Scripts/Services/Craft/Core/`):

1. **Have the tool and materials.** Put the trade tool and the required raw materials in
   your **backpack**. Some recipes also need you to be near a station (a **forge & anvil**
   for smithing, an **oven** for baking, a **loom** for cloth, etc.).
2. **Double-click the trade tool.** This opens the **craft menu** (the `CraftGump`).
3. **Pick a category.** The menu groups items into categories (for a smith: weapons,
   armor, shields…). Click the category to see its items.
4. **Pick an item.** Each item shows the **skill required** and the **materials it
   consumes**. Items you lack the skill or materials for are marked.
5. **Make it.** Click *Make Now* (or set a quantity to batch-craft). Your character works
   for a moment, then either **succeeds** (the item appears in your pack) or **fails**.

You can keep the menu open and craft repeatedly. Each attempt trains the governing skill
(see [Skill gain](/mechanics/skill-gain/)).

## Per-trade entry points

Each trade uses a different skill, tool, and menu. The skill ranges and full recipe lists
live on the linked pages — this table is just the **entry point**:

| Trade | Skill | Tool (double-click) | Recipes |
| --- | --- | --- | --- |
| Smithing | [Blacksmithy](/skills/blacksmithy/) | Smith's hammer (at a **forge & anvil**) | [/crafting/blacksmithy/](/crafting/blacksmithy/) |
| Tailoring | [Tailoring](/skills/tailoring/) | Sewing kit | [/crafting/tailoring/](/crafting/tailoring/) |
| Tinkering | [Tinkering](/skills/tinkering/) | Tinker's tools | [/crafting/tinkering/](/crafting/tinkering/) |
| Carpentry | [Carpentry](/skills/carpentry/) | Saw / dovetail saw | [/crafting/carpentry/](/crafting/carpentry/) |
| Fletching | [Bowcraft/Fletching](/skills/bowcraft-fletching/) | Fletcher's tools | [/crafting/bowfletching/](/crafting/bowfletching/) |
| Inscription | [Inscription](/skills/inscription/) | Scribe's pen | [/crafting/inscription/](/crafting/inscription/) |
| Cooking | [Cooking](/skills/cooking/) | Skillet / at an **oven** | [/crafting/cooking/](/crafting/cooking/) |
| Alchemy | Alchemy | Mortar & pestle | [/crafting/alchemy/](/crafting/alchemy/) |
| Cartography | Cartography | Mapmaker's pen | [/crafting/cartography/](/crafting/cartography/) |
| Masonry | (skill + tool) | Mallet & chisel | [/crafting/masonry/](/crafting/masonry/) |
| Glassblowing | (skill + tool) | Blowpipe (at a forge/furnace) | [/crafting/glassblowing/](/crafting/glassblowing/) |

Browse all trades from the [crafting overview](/crafting/). The tools themselves are in
the [tools catalog](/items/catalog/tools/).

## Materials and where to get them

Recipes consume **raw materials** that must be in your pack:

- **Ingots** for smithing — smelt mined ore at a forge. See [Mining](/skills/mining/) and
  [Gathering resources](/playing/gathering-resources/).
- **Boards** for carpentry and fletching — chop logs into boards. See
  [Lumberjacking](/skills/lumberjacking/).
- **Leather/hides** and **cloth** for tailoring — skin corpses for leather, or run the
  cloth chain. See [Gathering resources](/playing/gathering-resources/).
- **Reagents** for inscription/alchemy — bought from NPC mages/alchemists or gathered. See
  [reagents](/items/reagents/).
- **Food ingredients** for cooking — flour, raw fish/meat, etc.

Exact skill gates and the **colored ore / leather / wood tiers** (which require higher
skill and yield better items) are listed on the [resources reference](/items/resources/) —
link there rather than memorizing numbers.

## Success, exceptional quality and maker's marks

When you craft, the outcome is one of three things:

- **Failure** — you fail the attempt (see [Failure and material loss](#failure-and-material-loss)).
- **Normal success** — a standard-quality item.
- **Exceptional success** — the best quality, with bonus durability/stats and the option
  to **mark** it. The exceptional chance rises with skill above the recipe's requirement
  (computed by `GetExceptionalChance` in `CraftItem.cs`; some recipes can never be
  exceptional, and certain items/talismans add a bonus).

**Maker's mark:** when you craft an item exceptionally, you may be asked (via the
`QueryMakersMarkGump`) whether to **stamp your character's name** on it ("Crafted by
&lt;name&gt;"). Marked exceptional goods are prized and sell better. You typically set a
preference once and the menu remembers it.

Higher skill therefore matters twice: it lets you craft harder items at all, and it raises
the share of those items that come out exceptional.

## Failure and material loss

Crafting can fail, and **failure can consume some of your materials**. In general:

- A failed attempt may **destroy part of the resources** for that item (the craft system
  rolls this per attempt). Cheap, low-skill items rarely hurt; expensive colored-resource
  items can burn material on failure.
- Your **failure rate falls as your skill rises** above the recipe's requirement. Train on
  cheap items before risking rare materials.
- Exact loss amounts depend on the recipe and resource and are not restated here
  (unverified specifics) — practice on common materials first.

## Repairing items

Worn weapons, armor and tools lose **durability** and eventually break. You can **repair**
them with the matching trade skill (per `Repair.cs`):

1. Double-click the relevant **trade tool** (e.g. a smith's hammer for metal armor/weapons,
   a sewing kit for leather/cloth, a saw for wooden items).
2. Choose **Repair** in the craft menu (or use a **repair deed**).
3. Target the damaged item.

Success restores durability; a failed repair can **lower the item's maximum durability**,
so repair with high skill. Each trade repairs the item types it can make — smithing repairs
metal, tailoring repairs leather/cloth, carpentry/fletching repairs wood, and so on.

## Runic tools and enhancing (brief)

Two advanced features let high-end crafters make magic gear (mechanics are
expansion-dependent — treat the specifics as unverified):

- **Runic tools** — special, limited-use trade tools (runic hammers, sewing kits, etc.,
  often from [Bulk Order rewards](#bulk-order-deeds-bods)) that craft items with **random
  magic properties**. You craft as normal while holding the runic tool.
- **Enhancing** — taking a finished item and **re-forging it with a better resource**
  (per `Enhance.cs`) to add that resource's bonus. Enhancing can **destroy the item on
  failure**, so it is risky.

See the individual [/crafting/](/crafting/) trade pages for which runic tools and
enhancement options each trade supports.

## Resmelting (recovering metal)

Smiths can **resmelt** crafted or looted metal items back into a portion of their ingots at
a forge (per `Resmelt.cs`) — useful for recycling failed or unwanted metal goods. Use the
smith's menu's smelt option and target the item near a forge.

## Bulk Order Deeds (BODs)

**Bulk Order Deeds** are the crafting reward loop. An NPC shopkeeper for a trade (e.g. a
blacksmith or weaver) periodically offers a **BOD**: a deed asking for a quantity of a
specific item (optionally exceptional, and of a specific material).

To use a BOD:
1. Get the deed from the relevant NPC (ask for a bulk order / use the context menu).
2. **Craft the requested items** and drop each onto the deed to fill it.
3. **Turn in the completed deed** to an NPC for **rewards** — gold, rare materials, runic
   tools, recipes, and **large BODs** that combine several small ones for bigger prizes.

BODs are the main path to runic tools and other crafter-only rewards. Reward tables differ
by trade and shard configuration — check the trade's [/crafting/](/crafting/) page.

## See also

- [Crafting overview](/crafting/) and [Blacksmithy crafting](/crafting/blacksmithy/)
- [Blacksmith template](/templates/blacksmith/) — a full crafting build
- [Gathering resources](/playing/gathering-resources/) — where materials come from
- [Resources reference](/items/resources/) · [tools catalog](/items/catalog/tools/) ·
  [resources catalog](/items/catalog/resources/)
- Skill pages: [Blacksmithy](/skills/blacksmithy/) · [Tailoring](/skills/tailoring/) ·
  [Tinkering](/skills/tinkering/) · [Carpentry](/skills/carpentry/) ·
  [Bowcraft/Fletching](/skills/bowcraft-fletching/) · [Inscription](/skills/inscription/) ·
  [Cooking](/skills/cooking/)
- [Skill gain](/mechanics/skill-gain/) · [hue/color reference](/reference/hues/)
