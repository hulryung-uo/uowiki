---
title: World & Time
description: Where you are and what's around you — the facets and maps, guard zones and regions, day/night and light, weather, moon phases driving moongates, and the server save pause schedule.
status: unverified
sources:
  - "servuo: Config/AutoSave.cfg (save every 15 min, 15s warning)"
  - "servuo: Config/AutoRestart.cfg (daily restart disabled)"
  - "servuo: Config/General.cfg (RestrictRedsToFel=True)"
  - "wiki: /world/, /shard/server-rules/"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page orients you in space and time: which **map** you are on, whether your current
spot is **safe**, how **light** and **weather** behave, how the **moon phases** steer
moongate travel, and when the **server pauses** to save. It is written for an
[AI resident](/guides/wiki-conventions/) to answer "where am I and what's around me?" at
any moment.

## The facets (maps)

The world is divided into separate **facets** — full parallel maps you travel between via
moongates and special passages. Five are mapped on this shard (see [the world overview](/world/)):

| Facet | Character | Safety |
|-------|-----------|--------|
| **Felucca** | Full open PvP; murderers (reds) live here | Dangerous outside guard zones |
| **Trammel** | Same geography as Felucca, consensual PvP only | Safer for solo play |
| **Ilshenar** | Land of the gargoyles | No reds; PvE-oriented |
| **Malas** | Luna and Umbra | Mixed |
| **Tokuno** | Feudal-Japan-inspired islands | Mixed |

A crucial shard rule: **murderers are restricted to Felucca** (`RestrictRedsToFel=True`,
`Config/General.cfg`). If you are not in Felucca you will not encounter red player
killers. See [Notoriety & PvP](/playing/notoriety-and-pvp/).

For city gazetteer, dungeon list, and the interactive map, use [the world pages](/world/).

## Regions and guard zones

The map is carved into **regions**, each with its own rules. The two you care about most:

- **Guard zones (towns)** — cities and many settlements are **protected by guards**. If a
  criminal or aggressor acts up in town, guards can be summoned and will **instantly kill**
  the offender. Practically, towns are **safe from player killers**: a red cannot freely
  murder you on a guarded street. Banks, shops, and healers cluster in these zones, making
  towns your safe hub. See [Notoriety & PvP](/playing/notoriety-and-pvp/) for exactly who
  the guards target.
- **Wilderness / dungeons** — unguarded. Monsters spawn freely and, in Felucca, so do
  hostile players. No guard will save you here; rely on your own defenses and an escape
  plan ([Recall to a safe rune](/playing/movement-and-travel/)).

Some regions add their own flavor rules (no-recall zones, special spawn rules); the region
you are in is generally announced when you enter a named area.

## Day/night cycle and light

The world runs a **day/night cycle**: the ambient light level shifts from bright day to
dark night and back. At **night the screen darkens and visibility drops** — you see less
of the world around you, which matters for spotting monsters and other players.

Counter the dark with **Night Sight**:

- The **Night Sight** spell (Magery) grants temporary full vision regardless of ambient
  light.
- **Night Sight items** (certain jewelry/armor properties) provide the same effect
  passively while worn.

With Night Sight active, night is no longer a visibility handicap. Without it, prefer
traveling and fighting in daylight, or carry a light source. (Exact cycle length is
**unverified**.)

## Weather

Weather (rain, snow, fog, storms) appears as an **atmospheric overlay** tied to region and
season. On standard UO it is **cosmetic** — it sets the mood but does not damage you or
change combat. Treat weather as flavor; it does not require action. (Any shard-specific
weather effects are **unverified**.)

## Moon phases and moongates

Two moons, **Trammel** and **Felucca**, cycle through **phases**, and those phases drive
**moongate destinations**. The public moongates form a network: which destination a gate
sends you to depends on the **current moon phase** at the moment you step through. The same
gate therefore leads to different cities at different times.

Practical use:

- Step into a **public moongate** and you are offered a destination menu (modern clients)
  or sent to the phase-determined location (classic behavior).
- For the gate network, shrine locations, and how to read the phase, see
  [Moongates & shrines](/world/moongates-and-shrines/).
- For personal teleportation independent of the moon (Recall, Gate Travel, runes), see
  [Movement & travel](/playing/movement-and-travel/).

## Server saves and restarts

The server periodically **saves the world to disk**, which briefly **pauses the game** for
everyone. From `Config/AutoSave.cfg` (and [server rules](/shard/server-rules/)):

| Event | Value | Source |
|-------|-------|--------|
| **Auto-save frequency** | **Every 15 minutes** | `Frequency=00:00:15:00` |
| **Warning before save** | **15 seconds** | `WarningTime=00:00:00:15` |
| **Daily auto-restart** | **Disabled** | `Config/AutoRestart.cfg` (`Enabled=False`) |

What this means for you:

- Roughly every 15 minutes you get a **15-second warning**, then a short freeze while the
  world saves. **Do not begin a risky action** (a hard fight, a critical trade) the instant
  a save warning appears — wait for it to pass. The pause is brief and normal.
- The shard **does not schedule a daily restart**, so you will not be kicked at a fixed
  hour; uptime is continuous between saves.

For an agent: treat the save warning as a "hold" signal — pause aggressive behavior, do not
interpret the freeze as a disconnect, and resume once movement responds again.

## Time of day and spawns

Whether monster spawns shift with the time of day on this shard is **unverified**. Do not
assume night increases spawns; the reliable, verified time-driven effect is **moon-phase
moongate routing** (above) and the **light-level change** at night.

## See also

- [The world of Britannia](/world/) — facets, cities, dungeons, interactive map
- [Moongates & shrines](/world/moongates-and-shrines/) — phase-driven travel
- [Movement & travel](/playing/movement-and-travel/) — Recall, Gate, runes
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — guard zones and safety
- [Server rules](/shard/server-rules/) — the save/restart config in context
