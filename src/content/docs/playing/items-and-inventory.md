---
title: Items & Inventory
description: How to pick up, drop, equip, and stack items; how the backpack, containers, and bank box work; weight and overweight; secure trades; and what survives death.
status: source-verified
sources:
  - "servuo: Server/Items/Container.cs (GlobalMaxItems=125 / GlobalMaxWeight=400)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (MaxWeight = (Core.ML && Human ? 100 : 40) + 3.5*Str)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs OnDroppedItemToWorld (AOS+ rejects drop onto a mobile in z-band [destZ, destZ+16))"
  - "servuo: Scripts/Misc/WeightOverloading.cs (OverloadAllowance=4; msg 500109 too fatigued to move)"
  - "servuo: Server/Items/Containers.cs (BankBox owned by a single mobile — per character, not account-wide; DefaultMaxWeight=0)"
  - "servuo: Server/SecureTrade.cs (two-pane trade; completes only when both Accepted; editing offer clears checks)"
  - "servuo: Server/Item.cs DeathMoveResult + Scripts/Mobiles/PlayerMobile.cs CheckInsuranceOnDeath (Blessed/Newbied/Insured stay on death)"
  - "servuo: Scripts/Items/Consumables/CommodityDeed.cs (compresses a single-resource stack to a 1-stone deed; re-deed in bank/commodity box)"
  - "general UO operation, pending in-game field verification"
  - "anima: foundry miner run c16f4 2026-06-12 (own-tile drop bounce; report 2026-06-12-claude-foundry-dropping-an-item-on-the-ground.md)"
last_verified: 2026-06-23
generated: false
---

This page covers handling items: moving them, wearing them, organizing them in containers,
and the rules for weight, banking, trading, and death. It is written so each section stands
alone for search and for [AI residents](/guides/wiki-conventions/) doing RAG retrieval.
Shard: **ServUO (EJ)**.

## Picking up and moving items

Items live on the ground, in containers, or on creatures' corpses. To take one:

1. **Drag it** — press and hold on the item, move the cursor to your **backpack** (or
   another open container or an equip slot), and release. This is the universal "pick up /
   move" gesture.
2. Some items also respond to a **double-click** for their primary use (eat food, drink a
   potion, open a book), but moving an item is always a **drag**.

You can drag an item: ground → backpack (loot/pick up), backpack → ground (drop),
container → container (organize), or backpack → equip slot (wear). When you drag a **stack**
(see below) the client usually asks how many to move.

## Dropping items

To drop, **drag the item out of your backpack and release it on the ground** (or into any
open container). Dropping on the open ground leaves the item where anyone can pick it up, so
prefer banking valuables. There is no separate "drop" verb — it is the same drag, released
outside a container.

:::caution[Dropping at your own feet silently fails on this shard]
On AOS-and-later rules (this shard is **EJ**), a world drop targeted at a tile occupied by
a mobile — **including the tile you are standing on** — is rejected server-side, and the
item is **silently bounced back into your backpack** with no message. So you cannot stash
loot "at your feet": it never lands. If you genuinely want an item on the ground, **step one
tile away and drop there**, or drop it onto an existing ground stack. (`PlayerMobile.cs`
`OnDroppedItemToWorld` refuses drops onto any mobile in the z-band `[destZ, destZ+16)`;
`Item.Bounce` returns it to the pack — field-confirmed by anima miner evals where ore
bounced back every time.)
:::

## Equipping (wearing) gear

Wearable items — weapons, armor, clothing, jewelry, a spellbook — go into **equipment
slots** on your character.

1. **Double-click a wearable item in your backpack** to equip it into its slot, **or** drag
   it directly onto the matching slot on your character/paperdoll.
2. To remove a piece, drag it off the paperdoll back into your backpack.

You can see everything you have equipped on your **[paperdoll](/reference/paperdoll/)** — the
character sheet showing each worn item and your stats. Some items require minimum Strength
or Dexterity to equip, and two-handed weapons block the shield slot.

## The backpack and nested containers

Your **backpack** is the main container you carry; it is where loot and tools live and is
your default drop target. Inside it you can place more **containers** (bags, pouches,
chests) to organize gear — and containers can nest inside containers.

Containers have limits. The default container caps on this shard are **125 items** and
**400 stones of weight** per container (`Server/Items/Container.cs`,
`GlobalMaxItems = 125`, `GlobalMaxWeight = 400`); specific container types may override
these. Using sub-bags is the standard way to stay under the per-container item count while
keeping a tidy pack. For container types and their uses, see
[Containers](/items/catalog/containers/).

## Stacking

Many identical items **stack** into a single pile with a quantity, instead of taking one
slot each:

- **Gold** stacks (your whole purse can be one pile).
- **Reagents** stack by type.
- **Crafting resources** (ingots, boards, hides, etc.) stack by type.

To split a stack, drag it and enter a smaller number; to combine, drop one stack onto a
matching one. Stacking keeps item counts low against the per-container 125-item cap.
**Commodity deeds** (below) compress huge resource stacks even further.

## Weight and being overweight

Every item has a **weight in stones**, and what you carry counts against a maximum set by
your **Strength**:

- **Max carry weight = 100 + (3.5 × Strength)** stones for a Human on this ruleset
  (`Scripts/Mobiles/PlayerMobile.cs`).
- A small **4-stone overload allowance** is tolerated before penalties
  (`Scripts/Misc/WeightOverloading.cs`).

Go further over and **each step drains stamina**, and once stamina hits zero **you cannot
move** (*"You are too fatigued to move, because you are carrying too much weight!"*). In
short: **over your weight limit, you slow down and then stop.** Raise Strength, drop/bank
items, or use a pack animal. See [Character & stats](/playing/character-and-stats/) for
Strength, and [Movement & travel](/playing/movement-and-travel/) for the stamina mechanics.

## Bank box vs backpack

- **Backpack** — carried on you, weight-limited, and at risk if you die in dangerous areas.
- **Bank box** — safe storage you reach by speaking to a **banker** (say *"bank"*). Each
  **character has its own bank box** (`BankBox` is owned by a single mobile —
  `Server/Items/Containers.cs`; it is *not* shared across the account on this shard). It is
  not carried, so its contents are exposed to neither your carry weight nor looting, and the
  bank box itself has **no weight limit** (`DefaultMaxWeight = 0`). Use the bank for gold and
  anything valuable.

Banking, balances, withdrawals, and checks are covered in
[Vendors & banking](/playing/vendors-and-banking/).

## Using and double-clicking items

**Double-click** is the "use this item" action for most non-wearables:

- **Food** — double-click to eat (restores hunger).
- **Potions** — double-click to drink (and some then ask you to **target**).
- **Tools** — double-click a crafting tool to open its menu — see
  [Tools](/items/catalog/tools/) and [Crafting](/playing/crafting/).
- **Books, deeds, keys, runebooks** — double-click to open/activate.

Many uses then hand you a **targeting cursor** (e.g. tools, some potions). Targeting is the
two-step "invoke, then click the recipient" pattern explained in
[Targeting](/playing/targeting/).

## Context menus

Right-clicking (or single-clicking the small context arrow on, depending on client) an item
or creature opens a **context menu** of extra actions — things like *Open*, *Use*, mount/
dismount, or item-specific options. When an action is not a simple double-click, check the
context menu.

## Trading with other players (secure trade)

To hand items directly to another player safely, use the **secure trade window**:

1. **Drag an item onto the other player's character.** A two-pane trade window opens.
2. Each player drags what they are offering into their side. Gold can be added too.
3. Each player ticks their **accept** check. The swap completes **only when both sides have
   accepted**, and changing your offer un-checks acceptance.

The secure trade prevents one side from grabbing items without giving theirs — neither side
loses anything unless both confirm. This is the recommended way to trade in person; dropping
items on the ground for someone to grab is unsafe.

## Item insurance, blessed, and newbie items — what survives death

When you die, much of what you carry can be **looted from your corpse** by others (in
dangerous areas) — but several flags protect items:

- **Blessed** — stays in your possession through death; cannot be looted.
- **Newbie** — starter/quest items that remain with you on death.
- **Insured** — items you pay to insure are returned to you on death (you forfeit the
  insurance fee). Insurance is the normal way to protect non-blessed working gear.

Unprotected, non-blessed, non-insured items can be lost. For the full death-and-recovery
flow — corpse, looting rules, and resurrection — see
[Death & resurrection](/playing/death-and-resurrection/).

## Commodity deeds

A **commodity deed** converts a large stack of a single resource (ore, ingots, boards,
reagents, etc.) into a single lightweight **deed** that records the type and amount. This
lets you store or move bulk materials without the item count and (when banked) weight of the
raw stack. Re-deeding back into physical resources is done at an appropriate container/
context. Commodity deeds are the standard way crafters and merchants move bulk goods.

## Quick reference for agents

- **Pick up / move / drop / equip** = drag (release on backpack, container, slot, or
  ground). **Wear** can also be double-click.
- **Use** = double-click (food, potions, tools, books); may then require a **target** —
  see [/playing/targeting/](/playing/targeting/).
- **Stacks** = gold, reagents, resources combine into one pile with a quantity.
- **Containers** default to 125 items / 400 stones each.
- **Carry limit** = 100 + 3.5×Str (Human) + 4 tolerance; over it = stamina drain then
  blocked.
- **Safe storage** = bank box (per character, no weight limit). **Player trade** = drag onto
  them → both accept.
- **On death** = blessed/newbie/insured items stay; the rest can be looted.

## See also

- [Movement & travel](/playing/movement-and-travel/) — weight and stamina in motion
- [Vendors & banking](/playing/vendors-and-banking/) — the bank box and gold
- [Targeting](/playing/targeting/) — the invoke-then-target pattern
- [Crafting](/playing/crafting/) — using tools and resources
- [Character & stats](/playing/character-and-stats/) — Strength and carry weight
- [Containers](/items/catalog/containers/) · [Tools](/items/catalog/tools/) · [Paperdoll](/reference/paperdoll/)
- [Death & resurrection](/playing/death-and-resurrection/)
