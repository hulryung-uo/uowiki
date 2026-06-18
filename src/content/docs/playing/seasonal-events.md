---
title: Seasonal Events
description: The rotating event framework — Treasures of Tokuno, Treasures of Doom/Khaldun/Kotl/Sorcerer's Dungeon, Krampus, Rising Tide, and more, toggled active/inactive over time for limited-time artifact rewards.
status: source-verified
sources:
  - "servuo: Scripts/Services/Seasonal Events/SeasonalEventSystem.cs (EventType list, Active/Inactive rotation)"
  - "servuo: Scripts/Services/Seasonal Events/TreasuresOfTokuno/TreasuresOfTokuno.cs (drop-era / reward-era artifacts)"
last_verified: 2026-06-18
generated: false
---

The shard runs a **rotating seasonal-event system** (`SeasonalEventSystem`): a roster of
limited-time events that are switched **Active or Inactive** over time. While an event is
active, hunting the right creatures or content drops that event's **exclusive artifacts and
collectibles** — so it pays to know what's running.

## The event roster

Events tracked by the system (`EventType`), each toggled on its own schedule:

- **Treasures of Tokuno** — kill Tokuno-themed creatures for a chance at **lesser Tokuno
  artifacts**, which you can trade up for **greater Tokuno artifacts** and dye **pigments**.
- **Treasures of Doom / Khaldun / Kotl City / Sorcerer's Dungeon** — each turns a specific
  dungeon into a limited-time artifact farm with its own drop table.
- **Virtue Artifacts** — virtue-themed artifact rewards.
- **Krampus Encounter** — a holiday-season boss event with festive rewards.
- **Rising Tide** — a High-Seas pirate event.
- **Forsaken Foes** — an undead-themed event.

## How they work

- An event is either **Active** or **Inactive** (`EventStatus`); only active events drop their
  rewards. Some run on a **scheduled window** (start/duration), so they come and go.
- During a **Treasures of …** event, the targeted creatures/dungeon gain a **drop chance** for
  that event's artifacts (a "drop era" of items), and you can often **turn lesser pieces up**
  into the better "reward era" items.
- Because rewards are **time-limited**, an active event is the window to farm items you can't
  get otherwise.

## Tips

- **Check what's active** before planning a farm — the rewards only drop while the event runs.
- Treasures-of-a-dungeon events stack with that dungeon's normal loot (and any
  [champion spawn](/playing/champion-spawns/)), making the dungeon doubly worth running while
  it's live.

## See also

- [Dungeons](/world/dungeons/) — the dungeons that "Treasures of …" events light up
- [Champion Spawns](/playing/champion-spawns/) · [Doom — The Gauntlet](/playing/doom-gauntlet/) — overlapping artifact sources
- [Daily Rares](/playing/daily-rares/) · [Community Collections](/playing/community-collections/) — other limited/collectible loops
