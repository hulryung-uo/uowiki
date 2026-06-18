---
title: Daily Rares
description: Collectible rare items that respawn at fixed spots around the world each day — find them before someone else does.
status: source-verified
sources:
  - "servuo: Scripts/Services/DailyRares.cs (Enabled, DailyRaresSpawner — fixed-location daily spawns)"
last_verified: 2026-06-18
generated: false
---

**Daily rares** are collectible decorative items that **respawn once per day** at **fixed
locations** around Britannia (`DailyRaresSpawner`, enabled via `DailyRares.Enabled`). They're a
small treasure-hunt for collectors: learn the spots, make the rounds, and grab the day's rares
before another player beats you to them.

## How they work

- The system places a set of **rare item types** at specific map points — things like
  **daily rocks, jars, a broken chair**, and other oddball décor (`DailyRocks`, `DailyRock`,
  `DailyFullJars`, `DailyBrokenChair`, and more).
- Each location holds **one** of its rare at a time. Once a player **picks it up**, that spot is
  empty until the daily respawn refreshes it.
- Because they're **fixed-location and once-per-day**, they reward players who know the routes
  and check in regularly — first come, first served.

## Collecting them

- **Learn the locations** and run a circuit; the value is in the routine.
- These items are pure **collectibles / décor** — their worth is rarity and display value, not
  combat utility, so they're prized by [decorators](/playing/decorating/) and traders.

## See also

- [Decorating](/playing/decorating/) — where rare collectibles end up
- [Community Collections](/playing/community-collections/) · [Clean Up Britannia](/playing/cleanup-britannia/) — other collector tracks
- [Treasure hunting](/playing/treasure-hunting/) — the dig-for-loot cousin
