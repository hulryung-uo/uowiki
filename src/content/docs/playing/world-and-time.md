---
title: World & Time
description: Where you are and what's around you — the facets and maps, guard zones and regions, day/night and light, weather, the menu-driven public moongates, and the server save pause schedule.
status: source-verified
sources:
  - "servuo: Config/AutoSave.cfg (Frequency=00:00:15:00, WarningTime=00:00:00:15)"
  - "servuo: Config/AutoRestart.cfg (Enabled=False)"
  - "servuo: Config/General.cfg (RestrictRedsToFel=True)"
  - "servuo: Config/Siege.cfg (IsSiege=false)"
  - "servuo: Scripts/Misc/MapDefinitions.cs (6 facets; Felucca=FeluccaRules, others=TrammelRules)"
  - "servuo: Scripts/Regions/GuardedRegion.cs (guard candidates, AllowReds=Core.AOS)"
  - "servuo: Scripts/Items/Functional/PublicMoongate.cs (UseGate -> MoongateGump destination menu)"
  - "wiki: /world/, /shard/server-rules/"
  - "note: day/night cycle length and weather effects are client/visual, not server-verified"
last_verified: 2026-06-23
generated: false
---

This page orients you in space and time: which **map** you are on, whether your current
spot is **safe**, how **light** and **weather** behave, how the **public moongates** move
you between facets, and when the **server pauses** to save. It is written for an
[AI resident](/guides/wiki-conventions/) to answer "where am I and what's around me?" at
any moment.

## The facets (maps)

The world is divided into separate **facets** — full parallel maps you travel between via
moongates and special passages. Six facets are registered on this shard
(`Scripts/Misc/MapDefinitions.cs`; see also [the world overview](/world/)):

| Facet | Character | PvP rules |
|-------|-----------|-----------|
| **Felucca** | Full open PvP; murderers (reds) live here | `FeluccaRules` — open PvP |
| **Trammel** | Same geography as Felucca, consensual PvP only | `TrammelRules` — consensual |
| **Ilshenar** | Land of the gargoyles | `TrammelRules` — consensual |
| **Malas** | Luna and Umbra | `TrammelRules` — consensual |
| **Tokuno** | Feudal-Japan-inspired islands | `TrammelRules` — consensual |
| **Ter Mur** | Gargoyle homeland (SA) | `TrammelRules` — consensual |

The PvP-rules column is verified in `Scripts/Misc/MapDefinitions.cs`: this is a **non-Siege**
shard (`Siege.IsSiege=false`, `Config/Siege.cfg`), so only **Felucca** carries
`FeluccaRules` (open PvP); every other facet uses `TrammelRules` (consensual PvP only).

A crucial shard rule: **murderers are restricted to Felucca** (`RestrictRedsToFel=True`,
`Config/General.cfg`). If you are not in Felucca you will not encounter red player
killers. See [Notoriety & PvP](/playing/notoriety-and-pvp/).

For city gazetteer, dungeon list, and the interactive map, use [the world pages](/world/).

## Regions and guard zones

The map is carved into **regions**, each with its own rules. The two you care about most:

- **Guard zones (towns)** — cities and many settlements are **protected by guards**
  (`Scripts/Regions/GuardedRegion.cs`). If a **criminal or aggressor** acts up in town, that
  offender becomes a guard candidate and guards arrive and **kill them near-instantly** —
  triggered by someone saying **"guards"** or automatically when a nearby townsperson calls
  them. Practically, a player who attacks you in town flags criminal and draws the guards.
  Note the AOS-era subtlety: guards do **not** strike a **red** (murderer) merely for being
  red — only for committing a crime (`AllowReds` is true once `Core.AOS` is set, true on EJ).
  Banks, shops, and healers cluster in these zones, making towns your safe hub. See
  [Notoriety & PvP](/playing/notoriety-and-pvp/) for exactly who the guards target.
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

## Moongates

The **public moongates** form a free travel network linking the facets and major cities. On
this ServUO shard they are **menu-driven, not moon-phase-driven**: double-click a moongate
while standing on/next to it and the client opens a **destination menu**
(`MoongateGump`) listing every reachable location across Trammel, Felucca, Ilshenar, Malas,
Tokuno, and TerMur — you pick where to go (verified in
`Scripts/Items/Functional/PublicMoongate.cs`, `UseGate` → `MoongateGump`).

> **Note on lore vs. mechanics:** classic Ultima Online tied moongate exits to the *phase of
> the moon* (the Trammel and Felucca moons). That phase-based routing is **not** how this
> shard's public moongates work — you always get the full destination menu. The two moons
> still exist as flavor/astronomy, but they do not change where a public moongate sends you.

Practical use:

- Step onto a **public moongate** and **double-click it** to open the destination menu, then
  pick a city/facet.
- For the gate network and shrine locations, see
  [Moongates & shrines](/world/moongates-and-shrines/).
- For personal teleportation (Recall, Gate Travel, runes), see
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
assume night increases spawns. Note that public-moongate destinations are **not** moon-phase
driven on this shard (see [Moongates](#moongates) above) — they use a fixed destination menu.

## See also

- [The world of Britannia](/world/) — facets, cities, dungeons, interactive map
- [Moongates & shrines](/world/moongates-and-shrines/) — the public moongate network
- [Movement & travel](/playing/movement-and-travel/) — Recall, Gate, runes
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — guard zones and safety
- [Server rules](/shard/server-rules/) — the save/restart config in context
