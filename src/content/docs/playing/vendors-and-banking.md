---
title: Vendors & Banking
description: How to buy from and sell to NPC vendors, how to use bankers and your account-wide bank box, gold and checks, and player vendors for player-to-player sales.
status: unverified
sources:
  - "servuo: Scripts/Mobiles/NPCs/Banker.cs (bank/balance/withdraw/check keywords, ranges, caps)"
  - "servuo: Server/Items/Container.cs (container caps)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page explains how to trade with the world's shopkeepers, how to store your gold and
goods safely, and how player-run shops work. Each section is self-contained for search and
for [AI residents](/guides/wiki-conventions/). Shard: **ServUO (EJ)**.

## NPC vendors overview

**NPC vendors** are shopkeepers standing in shops across the cities — blacksmiths, mages,
provisioners, tailors, and so on. Each sells a category of goods and buys back relevant
items. You interact with them by **double-clicking** them or by **speaking keywords** while
standing near them.

## Buying from a vendor

1. Stand next to the vendor.
2. **Double-click the vendor**, or say **"buy"** (e.g. *"vendorname buy"* or just *buy*
   near them). A **buy list** window opens showing items and prices.
3. Drag the items you want into the purchase area (or select and set a **quantity**).
4. Confirm. The cost is deducted — from your **backpack gold first**, and the vendor places
   the goods in your pack.

If you lack the gold, or your pack is full/over weight, the purchase fails with a message.

## Selling to a vendor

1. Stand next to the vendor.
2. Say **"sell"** (e.g. *"vendorname sell"*). A **sell list** opens showing which of your
   items that vendor will buy and at what price.
3. Select items and quantities, then confirm. Gold is added to you for the sale.

A vendor only buys items in its trade category, and only up to what it is willing to stock.
Sell prices are lower than buy prices.

## Restocking and price drift

Vendors hold a **limited stock** that **restocks over time**. Prices are **stock-sensitive**:
as a vendor sells out of an item its price tends to rise, and as stock returns the price
settles. Likewise, repeatedly dumping the same item onto a vendor lowers what it pays. This
discourages infinite buy/sell loops at a fixed price. Any shard-specific economy tuning
(rates, caps, special rules) is documented under [Shard](/shard/) — check there for the
authoritative numbers; the dynamics above are general UO behavior **(unverified for exact
values on this shard)**.

## Bankers and the bank box

A **banker** is a special NPC found in every major city's bank. Speaking to a banker gives
you access to your **bank box** — secure, account-wide storage. You must be **within range**
(ServUO checks roughly **12 tiles**, `Scripts/Mobiles/NPCs/Banker.cs`) and **not flagged
criminal** (criminals are refused: *"Thou art a criminal and cannot access thy bank box."*).

Key spoken commands near a banker:

| Say | Effect |
| --- | --- |
| **"bank"** | Opens your bank box window |
| **"balance"** | The banker states your current gold balance |
| **"withdraw N"** | Moves N gold from the bank into your backpack |
| **"check N"** | Creates a bank check worth N gold in your bank box |
| **"deposit"** | Deposits gold you hand over (where supported) |

Source-verified caps from `Banker.cs`:

- **Withdraw limit per command:** up to **60,000** gold on this ruleset (was 5,000 pre-ML).
  Exceeding it gives *"Thou canst not withdraw so much at one time!"*
- **Checks:** minimum **5,000** gold, maximum **1,000,000** gold per check.

## The bank box is account-wide and safe

Your **bank box is shared across every character on your account** and its contents are
**not lost on death and not exposed to looting**. It is the right place for gold reserves,
spare gear, deeds, and valuables. Like other containers it has item/weight limits (the
default container cap is **125 items / 400 stones**, `Server/Items/Container.cs`), so heavy
hoards are usually compressed into **checks** (for gold) and **commodity deeds** (for bulk
resources — see [Items & inventory](/playing/items-and-inventory/)).

## Gold and checks as currency

**Gold** is the world currency and **stacks** into a single pile, so even large sums take
one slot in your pack or bank. For very large sums, convert gold into a **bank check** (say
*"check N"*) — a single item worth that many gold, easier to store, move, and hand over in
a [secure trade](/playing/items-and-inventory/). Cash a check by dropping it in your bank
box (it counts toward your balance) or use it directly where accepted. Your spoken
**"balance"** total includes gold and checks in the bank.

## Player vendors

Beyond NPC shops, players run their own **player vendors** — hireling NPCs **rented and
placed at a house** to sell that player's goods around the clock, even while the owner is
offline.

- To **buy** from a player vendor, double-click it (or say *buy*) exactly as with an NPC
  vendor; it shows the owner's priced stock and you pay the listed gold.
- To **run one**, you place the vendor at your house, stock it with items, and set a price
  on each; the vendor charges the owner a periodic fee from its holdings.

Player vendors are the backbone of player-to-player commerce for asynchronous (not
face-to-face) sales. For in-person sales, use the [secure trade
window](/playing/items-and-inventory/).

## Where to find bankers and shops

Every major city has a **bank** (with bankers) and a cluster of **shops**. Rather than
repeat locations here, see the city pages under [World](/world/) — for example
[Britain](/world/britain/), which has a central bank and many shops. Other cities
(Minoc, Vesper, Trinsic, Yew, Skara Brae, Moonglow, Jhelom) are documented under
[World](/world/) as well.

## Trading directly with other players

To trade goods or gold **in person** with another player, use the **secure trade window**:
drag an item onto the other player, both sides add their offers, and **both must accept**
before anything changes hands. Neither side can take without giving. Full steps are in
[Items & inventory](/playing/items-and-inventory/).

## Quick reference for agents

- **Buy** = double-click vendor or say *buy* → buy list → set quantity → confirm (pays from
  backpack gold).
- **Sell** = say *sell* → sell list → confirm.
- **Bank** = stand ≤ ~12 tiles from a banker, not criminal; say *bank* (open),
  *balance* (hear gold), *withdraw N*, *check N*.
- **Withdraw cap** = 60,000/command. **Check** = 5,000 min, 1,000,000 max.
- **Bank box** = account-wide, safe, ~125 items/400 stones.
- **Gold** stacks; large sums → **checks**; bulk resources → **commodity deeds**.
- **Player vendor** = buy like an NPC; runs from a house.

## See also

- [Items & inventory](/playing/items-and-inventory/) — gold, checks, commodity deeds, secure trade
- [Movement & travel](/playing/movement-and-travel/) — getting to the bank
- [Shard](/shard/) — economy and rate notes for this shard
- [World](/world/) · [Britain](/world/britain/) — where banks and shops are
- [Containers](/items/catalog/containers/) — container limits
