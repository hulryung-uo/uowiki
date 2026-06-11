---
title: How to Play — Treasure Hunting
description: The treasure-hunter playstyle on our shard — find or buy a treasure map, decode it with Cartography, dig the chest with Mining, fight the guardians, and pick the trapped chest for gold, gems, magic gear, power scrolls and special scrolls. Covers the five Forgotten-Treasures map levels (Stash, Supply, Cache, Hoard, Trove), the five loot packages, the skills involved, and where the chests are buried.
status: source-verified
sources:
  - "servuo: Scripts/Services/TreasureMaps/TreasureMap.cs (decode, dig, dig range, guardians, spawn tables, location randomization)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapInfo.cs (levels, packages, decode difficulty, chest skills, loot tables)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapChest.cs (chest, trap, artifacts)"
  - "servuo: Scripts/Items/Tools/MapItem.cs (decoded-map gump 0x139D)"
  - "servuo: Config/TreasureMaps.cfg (Enabled=True, LootChance=.01, ResetTime=30.0)"
  - "servuo: Config/Expansion.cfg (CurrentExpansion=EJ -> modern system live)"
  - "servuo: Data/treasure.cfg (193 classic dig sites)"
  - "client art: gumpartLegacyMUL.uop gump 0x139D (map-window parchment)"
last_verified: 2026-06-11
generated: false
---

**Treasure hunting** is the explorer's profession: you obtain a treasure map, decode it
to reveal where a chest is buried, travel to that spot, dig it up, fight the monsters that
erupt from the ground, then unlock and disarm the chest for its loot. It rewards a
well-rounded character and pays out in gold, gems, magic gear, and — at the top tiers —
power scrolls and special skill scrolls.

> **Which system runs here.** Our shard runs expansion **EJ**
> (`Config/Expansion.cfg` → `CurrentExpansion=EJ`), so `TreasureMapInfo.NewSystem` is
> **true** and the modern **Forgotten Treasures** treasure-map system is live. Maps have
> the five levels **Stash, Supply, Cache, Hoard, Trove** and a loot **package**, not the
> older "level 1–7" numbering. The numbers and tables on this page are source-verified
> against the EJ code paths.

## What is treasure hunting

The full loop, in order:

1. **Get a map.** Treasure maps drop from monsters (see below) or are bought/traded from
   other players.
2. **Decode it.** Double-click the map; a [Cartography](/skills/cartography/) skill check
   decodes it and marks the dig spot with a red pin
   (`TreasureMap.Decode`, `DisplayTo`).
3. **Travel to the spot.** The decoded map shows a small regional view; you sail or ride
   to that real-world location.
4. **Dig.** Stand near the pin with a digging tool (a [Mining](/skills/mining/) tool) and
   dig. Your skill sets how close you must be (`DigTarget`).
5. **Fight the guardians.** Finishing the dig spawns four monsters scaled to the map level
   (`DigTimer`). Survive them.
6. **Open the chest.** The chest is **locked and trapped** — pick the lock with
   [Lockpicking](/skills/lockpicking/) and disarm it with [Remove Trap](/skills/remove-trap/)
   (or risk the explosion), then loot it.

People treasure-hunt for the payout: tens of thousands of gold per chest, bags of gems,
randomly-magic weapons/armor/jewelry, and — at higher tiers — **power scrolls**,
**scrolls of transcendence** and **scrolls of alacrity**.

## The treasure map item

Every map has a **level** and a **package**. The level sets the difficulty and the loot
budget; the package themes the gear and scrolls toward a playstyle.

**Levels** (enum `TreasureLevel`), easiest to hardest:

| Level | Decode difficulty | Chest required skill | Magic items | Gold range |
|---|---|---|---|---|
| **Stash** | 100 | 5 | 6 | 10,000–40,000 |
| **Supply** | 200 | 45 | 8 | 20,000–50,000 |
| **Cache** | 300 | 75 | 12 (24 for Assassin) | 30,000–60,000 |
| **Hoard** | 400 | 80 | 18 | 40,000–70,000 |
| **Trove** | 500 | 80 | 36 | 50,000–70,000 |

*Decode difficulty* is the `AssignChestQuality`/decode table (`Utility.Random(difficulty)`
compared against your Cartography). *Chest required skill*, *magic item count* and *gold
range* are from `TreasureMapInfo.Fill`, `GetEquipmentAmount` and `GetGoldCount`.

**Packages** (enum `TreasurePackage`) — the loot theme:

- **Artisan** — crafting tools/resources, recipes, mapmaker/crafter goodies.
- **Assassin** — daggers, light armor, stealth/poison-flavored loot (and more magic items at Cache).
- **Mage** — staves, robes/leather, reagents (on Stash), caster scrolls.
- **Ranger** — bows, hide/studded armor, archery/taming flavor.
- **Warrior** — heavy weapons, plate armor and shields, melee scrolls.

**Where maps come from.** Maps drop as monster loot at a base chance of
**`LootChance = .01`** (1%), overridable per creature
(`Config/TreasureMaps.cfg`, `TreasureMap.LootChance`). A dug chest can itself contain the
next map up: at levels below Trove there is a 10% chance the chest drops a map one level
higher (`TreasureMapInfo.Fill`). Decoded maps become **blessed** so they stay on you.

## The skills of a treasure hunter

Treasure hunting is the canonical reason to build a broad character — it touches several
skills end-to-end, which is why it pairs naturally with a
[seven-GM template](/templates/seven-gm/).

- **[Cartography](/skills/cartography/)** — **decode** the map. The higher the level, the
  more Cartography you need (the decode difficulty table above). On this modern system
  Cartography *also* governs dig range (below) and the chest's quality roll
  (`AssignChestQuality`).
- **[Mining](/skills/mining/)** — you must carry a **digging tool** (any Mining harvest
  tool, e.g. a shovel or pickaxe) to dig the chest up (`TreasureMap.HasDiggingTool`).
- **[Lockpicking](/skills/lockpicking/)** — the chest is locked; its lock level is the
  chest's *required skill − 10* and its max lock level is *required skill + 40*
  (`TreasureMapInfo.Fill`).
- **[Remove Trap](/skills/remove-trap/)** — every chest is fitted with an
  **explosion trap** (`TrapType.ExplosionTrap`); disarm it before it detonates.
- **Combat / [Magery](/magic/) / [Taming](/playing/taming-and-pets/)** — to handle
  the guardians that spawn on the dig. See [combat basics](/playing/combat-basics/).

### Dig range

How close you must target to the pin to dig depends on your **Cartography** (the modern
system uses Cartography, not Mining, for range — `DigTarget.OnTarget`):

| Cartography | Max dig range |
|---|---|
| 100+ | 4 tiles |
| 81–99 | 3 tiles |
| 51–80 | 2 tiles |
| below 51 | 1 tile |

If you target too far away the map tells you which direction to move; within 8 tiles it
says you are "very close."

## Reading the map (the gump)

When you decode a map it opens as a small parchment window showing a **regional view** of
the area around the buried chest, with a **red pin** marking the exact spot. You read the
surrounding terrain (coastline, roads, landmarks), travel to that real-world location, and
dig within range of the pin.

![Example of a decoded treasure map: a regional parchment view with a red pin at the dig spot](/img/treasure/example-map.png)

*An example decoded map (rendered from the Felucca world map framed with the client's
map-window parchment art, gump `0x139D`; red X marks the dig spot).* The in-client gump is
the same idea: terrain inside a parchment frame with the dig location pinned.

## The dig locations

There are two ways a chest's spot can be chosen, and it matters for where you end up
digging:

- **Classic fixed sites (the traditional "dig spots").** `Data/treasure.cfg` lists
  **193 hard-coded** Britannia (Felucca/Trammel) coordinates — the well-known treasure
  spots players think of as *the* dig locations. These are used by
  `GetRandomClassicLocation()` when randomized locations are **off**.
- **Our shard's modern randomized maps.** Because `Config/TreasureMaps.cfg` has
  **`Enabled=True`** (`TreasureMap.NewChestLocations`), live maps instead **randomize the
  chest within each facet's diggable regions** (`TreasureMap.GetRandomLocation`). For
  Felucca and Trammel that region is the **whole map** (`0,0 → 5119,4095`); Tokuno, Malas,
  Ilshenar, Ter Mur and Eodon use specific rectangles. The picked tile is then validated
  by `ValidateLocation` — it rejects towns, houses, dungeons, champion-spawn regions,
  roads, and any non-walkable or non-natural tile (only dirt/grass/jungle/forest/snow are
  allowed), so chests always land in open wilderness.

The map below plots the **193 classic sites** on Felucca so you can see the traditional
spread across Britannia. On our shard, treat it as a guide to the *kind* of terrain
treasure favors rather than an exact list of where today's maps point.

![Map of Britannia with all 193 classic treasure dig sites plotted as gold X markers](/img/treasure/locations.png)

*All 193 classic dig sites from `Data/treasure.cfg`, plotted on the Felucca map.*

## The chest & loot

**Guardians.** Completing the dig spawns **4** monsters at the chest
(`DigTimer.OnTick`). On the modern system each spawn has a **70%** chance to be tagged a
`(Guardian)`. They scale to the map level and facet (`TreasureMap.Spawn` tables) — for
Felucca/Trammel, roughly:

- **Stash** — mongbats, ratmen, skeletons, zombies, headless ones.
- **Supply** — orcish mages, gargoyles, gazers, hell hounds, earth elementals.
- **Cache** — liches, ogre lords, dread spiders, elementals, lich lords, daemons, elder gazers.
- **Hoard** — ancient wyrms, balrons, blood/poison elementals, titans.
- **Trove** — blood/poison elementals, cold drakes, frost dragons/drakes, greater dragons.

**Opening it.** The chest is locked and carries an **explosion trap**; pick the lock with
[Lockpicking](/skills/lockpicking/) and disarm with [Remove Trap](/skills/remove-trap/).
Chest **quality** (Rusty / Standard / Gold) is rolled from your Cartography at dig time and
boosts the gem, reagent and material counts.

**Loot** (`TreasureMapInfo.Fill`), by what's inside:

- **Gold** — a bag of gold scaled to level (see the table above), plus a **bag of gems**
  whose count grows with chest quality and level.
- **Magic equipment** — randomly-magic weapons, armor and jewelry themed by the map's
  **package**, in the counts from the level table (6 → 36 items from Stash → Trove).
- **Reagents** — only on **Stash + Mage** maps (20/40/60 by chest quality).
- **Crafting resources & special materials** — on **Artisan** maps (ingots, boards,
  leather; imbuing ingredients on Ter Mur, etc.).
- **Special / minor-artifact loot & decorations** — increasing chance from Supply upward.
- **Power scrolls** — **Felucca only**, on **Cache and higher**, at **+110** in the
  package's skills (`GetPowerScrollList`).
- **Scrolls of Transcendence** — on most levels except Supply/Cache
  (`GetTranscendenceList`).
- **Scrolls of Alacrity** — on most levels except Stash (and not Cache on Felucca)
  (`GetAlacrityList`).

Magic gear and special items are themed by the package and built by
`RunicReforging.GenerateRandomItem` within a per-level budget. See the
[items reference](/items/) for what the individual drops are.

## See also

- [Cartography](/skills/cartography/) · [Mining](/skills/mining/) ·
  [Lockpicking](/skills/lockpicking/) · [Remove Trap](/skills/remove-trap/)
- [Seven-GM template](/templates/seven-gm/) · [Combat basics](/playing/combat-basics/) ·
  [Taming and pets](/playing/taming-and-pets/)
- [Gathering resources](/playing/gathering-resources/) · [Items reference](/items/)

Locations plotted from `Data/treasure.cfg`; map art and the decoded-map parchment are the
client's own copyright-clean assets.
