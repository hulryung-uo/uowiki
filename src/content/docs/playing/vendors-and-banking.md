---
title: Vendors & Banking
description: How to buy from and sell to NPC vendors, how to use bankers and your account-wide bank box, gold and checks, and player vendors for player-to-player sales.
status: source-verified
sources:
  - "servuo: Scripts/Mobiles/NPCs/Banker.cs (bank/balance/withdraw/check keywords, InRange 12, withdraw cap 60000 Core.ML, criminal refusal, account-gold balance & check-service-disabled)"
  - "servuo: Scripts/Misc/CurrentExpansion.cs (AccountGold.Enabled = Core.TOL, ConvertOnBank = true)"
  - "servuo: Server/Items/Container.cs (GlobalMaxItems=125, GlobalMaxWeight=400)"
  - "servuo: Server/Items/Containers.cs (BankBox.DefaultMaxWeight = 0)"
  - "servuo: Scripts/Mobiles/NPCs/BaseVendor.cs (buy pays backpack gold first, then bank/account, then bank box)"
  - "note: vendor restock/price drift and player-vendor fee specifics not deep-verified here"
last_verified: 2026-06-23
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
4. Confirm. The cost is deducted from your **backpack gold first**; if your pack lacks enough,
   the vendor automatically draws the rest from your **bank / account gold** (verified in
   `Scripts/Mobiles/NPCs/BaseVendor.cs`: backpack → `Banker.Withdraw` / account currency →
   bank box). The goods are placed in your pack.

If you lack the gold everywhere, or your pack is full/over weight, the purchase fails with a
message.

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

Key spoken commands near a banker (verified in `Scripts/Mobiles/NPCs/Banker.cs`):

| Say | Effect |
| --- | --- |
| **"bank"** | Opens your bank box window |
| **"balance"** | The banker states your balance (see note below) |
| **"withdraw N"** | Moves N gold from your account into your backpack |
| **"check N"** | Would create a bank check — **disabled on this shard** (see below) |
| **"deposit"** | Deposits gold you hand over (where supported) |

Source-verified details from `Banker.cs`:

- **Withdraw limit per command:** up to **60,000** gold on this ruleset (was 5,000 pre-ML;
  the code branches `Core.ML ? 60000 : 5000`). Exceeding it gives *"Thou canst not withdraw so
  much at one time!"*
- **Account-wide currency is enabled** on this shard: `AccountGold.Enabled = Core.TOL` and
  EJ ≥ TOL, so it is **true** (`Scripts/Misc/CurrentExpansion.cs`). With it on:
  - Gold dropped into the bank is **converted to account-wide virtual gold**
    (`AccountGold.ConvertOnBank = true`), pooled across all characters on the account.
  - **"balance"** reports your account totals — **Platinum and Gold** (plus any secure-account
    amount) — not a single physical pile (`Banker.cs`, message `1155855`/`1155848`).
  - **The "check" service is turned off.** Saying *check N* makes the banker reply
    *"We no longer offer a checking service."* (`Banker.cs`: `if (AccountGold.Enabled && ...)`).
    The 5,000-min / 1,000,000-max check limits still exist in code but are unreachable while
    account gold is enabled. To move large sums, use the account-wide bank balance itself or a
    [secure trade](/playing/items-and-inventory/).
- A **criminal cannot use the banker** at all — *bank*, *balance*, *withdraw*, and *check* are
  refused (*"Thou art a criminal and cannot access thy bank box."* / *"I will not do business
  with a criminal!"*).

## The bank box is account-wide and safe

Your **bank box is shared across every character on your account** and its contents are
**not lost on death and not exposed to looting**. It is the right place for gold reserves,
spare gear, deeds, and valuables.

The default container cap is **125 items / 400 stones**
(`m_GlobalMaxItems = 125`, `m_GlobalMaxWeight = 400` in `Server/Items/Container.cs`), but the
**bank box specifically has no weight limit** — `BankBox.DefaultMaxWeight` returns **0**
(`Server/Items/Containers.cs`), so the practical bank-box constraint is the **125-item cap**,
not weight. To stay under 125 items, compress bulk resources into **commodity deeds** (see
[Items & inventory](/playing/items-and-inventory/)); gold itself is account-wide and does not
occupy a bank-box slot on this shard (see banker note above).

## Gold and checks as currency

**Gold** is the world currency and **stacks** into a single pile, so even large sums take
one slot in your pack. In the **bank**, gold goes further: on this shard gold is **account-wide
virtual currency** — dropping it in the bank converts it into a pooled balance shared by all
your characters (`AccountGold.ConvertOnBank = true`, `Scripts/Misc/CurrentExpansion.cs`), and
once a sum is large enough the bank tracks it as **Platinum** as well as Gold. Your spoken
**"balance"** reports those account totals.

**Bank checks** are a legacy feature for storing very large gold sums as a single item.
Because account-wide gold is enabled here, the banker's **"check" service is disabled** — it
replies *"We no longer offer a checking service."* You therefore do not need checks for
storage on this shard; the account balance handles large sums. (Existing checks can still be
deposited and count toward your balance.)

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
- **Bank** = stand ≤ 12 tiles from a banker, not criminal; say *bank* (open),
  *balance* (hear account totals), *withdraw N*.
- **Withdraw cap** = 60,000/command (Core.ML; was 5,000 pre-ML).
- **Checks disabled** here — account-wide gold is on; *check N* → "We no longer offer a
  checking service."
- **Bank box** = account-wide, safe; **125-item cap, no weight limit** (DefaultMaxWeight=0).
- **Gold** = account-wide virtual balance (Platinum + Gold); bulk resources → **commodity deeds**.
- **Player vendor** = buy like an NPC; runs from a house.

## See also

- [Items & inventory](/playing/items-and-inventory/) — gold, checks, commodity deeds, secure trade
- [Movement & travel](/playing/movement-and-travel/) — getting to the bank
- [Shard](/shard/) — economy and rate notes for this shard
- [World](/world/) · [Britain](/world/britain/) — where banks and shops are
- [Containers](/items/catalog/containers/) — container limits
