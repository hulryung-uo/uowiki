---
title: Server Rules & Rates
description: Gameplay-relevant server configuration — housing, loot generation, treasure maps, NPC vendors, and save/restart schedule.
status: source-verified
sources:
  - "servuo: Config/Housing.cfg"
  - "servuo: Config/Loot.cfg"
  - "servuo: Config/TreasureMaps.cfg"
  - "servuo: Config/Vendors.cfg"
  - "servuo: Config/AutoSave.cfg"
  - "servuo: Config/AutoRestart.cfg"
last_verified: 2026-06-11
generated: false
---

The laws of the land, as written in the server's own configuration files. All values below are
read from `Config/*.cfg`.

## Housing (`Config/Housing.cfg`)

| Setting | Value | What it means |
|---------|-------|---------------|
| Houses per account | **1** (`AccountHouseLimit=1`) | One house per account; only the most recently placed house auto-refreshes. |

## Loot generation (`Config/Loot.cfg`)

Loot on this shard uses the modern budget system: each corpse gets a property "budget" that the
generator spends on magic item properties.

| Setting | Value |
|---------|-------|
| Felucca luck bonus | **+1000** (`FeluccaLuckBonus=1000`) |
| Felucca budget bonus | **+100** (`FeluccaBudgetBonus=100`) |
| Base budget range | **150–700** (`MinBaseBudget`/`MaxBaseBudget`) |
| Adjusted budget range | **150–1450** (`MinAdjustedBudget`/`MaxAdjustedBudget`) |
| Max properties per item | **11** (`MaxProps=11`) |
| Powder of Fortifying on jewelry | **Not allowed** (`CanPOFJewelry=False`) |

The practical takeaway: hunting in Felucca yields meaningfully better loot (luck and budget
bonuses) at the cost of open PvP.

## Treasure maps (`Config/TreasureMaps.cfg`)

| Setting | Value |
|---------|-------|
| Randomized dig locations | **Enabled** (`Enabled=True`) — chests are not at the classic fixed spots. |
| Chance for a creature to carry a map | **1%** base (`LootChance=.01`; individual creatures can override this). |
| Map location reset time | **30.0** (`ResetTime=30.0`; the config does not state the unit — see source `Scripts/` treasure map system before relying on it). |

## NPC vendors (`Config/Vendors.cfg`)

| Setting | Value |
|---------|-------|
| Restock interval | **60 minutes** (`RestockDelay=60`) |
| Max items sold to a vendor at once | **500** (`MaxSell=500`) |
| Economy: purchases to raise a price | 1000 (`BuyItemChange=1000`) |
| Economy: sales to lower a price | 1000 (`SellItemChange=1000`) |
| Stocked amount of economy items | 500 (`EconomyStockAmount=500`) |
| Bribe multiplier decay | 25–30 days (`BribeDecayMinTime`/`BribeDecayMaxTime`) |

The publish-21 vendor economy is active: heavy buying inflates prices, heavy selling deflates
them, per item type. Find physical vendor locations on the
[interactive map](https://uomap.vercel.app) (295 NPC vendors are plotted).

## Saves and restarts

| Setting | Value | Source |
|---------|-------|--------|
| World auto-save | **Every 15 minutes**, 15-second warning (`Frequency=00:00:15:00`, `WarningTime=00:00:00:15`) | `Config/AutoSave.cfg` |
| Save archives | Disabled (`ArchivesEnabled=False`) | `Config/AutoSave.cfg` |
| Daily auto-restart | **Disabled** (`Enabled=False`) | `Config/AutoRestart.cfg` |

A brief world-save pause every 15 minutes is normal; the shard does not schedule daily restarts.

## Related

- [Shard identity card](/shard/) — expansion and caps
- [Skill gain mechanics](/mechanics/skill-gain/)
