---
title: Clean Up Britannia
description: Turn unwanted items in for Clean Up Britannia points, bank them in the point exchange, and trade them for exclusive rewards — the shard's recycling-for-rewards program.
status: source-verified
sources:
  - "servuo: Scripts/Services/CleanUpBritannia/CleanUpBritanniaData.cs (Enabled, points system)"
  - "servuo: Scripts/Services/CleanUpBritannia/PointExchange.cs (deposit/withdraw points to account exchange)"
last_verified: 2026-06-18
generated: false
---

**Clean Up Britannia** is the shard's "recycle for rewards" program: hand in unwanted items
and earn **Clean Up points** you can spend on an exclusive reward catalog. It's enabled here
(`CleanUpBritanniaData.Enabled`) and is a tidy way to turn vendor-junk and surplus loot into
something worth keeping.

## Earning points

**Donate eligible items** to the Clean Up Britannia collection. Each item is worth a set number
of **points** based on how much the system wants it cleared from the world — common clutter is
worth a little, while specific targeted items are worth more. Your points accrue to your
character (`PointsSystem.CleanUpBritannia`).

## The point exchange

Points can be moved into a shared **point exchange** (`PointExchange`): you **deposit** points
into the exchange and **withdraw** them, and the exchange total is **account-wide** — so you can
pool points across characters and manage them in one place. The gump shows your current points
and how much you can withdraw.

## Spending points

Trade your points for the **Clean Up Britannia reward catalog** — exclusive decorative and
functional items only available through the program. The more you contribute, the better the
rewards you can afford.

## Why bother

- It gives **value to junk** — surplus crafted goods, low-end loot, and clutter become points.
- The rewards are **exclusive**, so it's the only source for certain décor and items.
- Cleaning items out also keeps the world tidy, which is the whole point of the program.

## See also

- [Community Collections](/playing/community-collections/) — the other donation-for-rewards track
- [Items & inventory](/playing/items-and-inventory/) — managing the stuff you'll clean up
- [Vendors & banking](/playing/vendors-and-banking/) — selling vs cleaning up
