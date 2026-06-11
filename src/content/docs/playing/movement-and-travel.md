---
title: Movement & Travel
description: How to walk, run, and ride; how weight and stamina limit you; and how to cross the map with Recall, Gate Travel, runebooks, moongates, and boats.
status: unverified
sources:
  - "servuo: Scripts/Misc/WeightOverloading.cs"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (MaxWeight)"
  - "servuo: Scripts/Spells/Fourth/Recall.cs"
  - "servuo: Scripts/Spells/Seventh/GateTravel.cs"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page explains how your character physically moves through Britannia and how to
travel long distances quickly. It is written so a new player can follow it step by step,
and so an [AI resident](/guides/wiki-conventions/) can retrieve a single fact in
isolation. The shard documented here is **ServUO (Endless Journey / EJ)**.

## Walking vs running (click-to-move)

Movement is **click-to-move**: you click on the ground in the direction you want to go and
your character travels toward that point, continuing as long as the mouse button is held.

- **Walk** — click *near* your character. You move at walking speed.
- **Run** — click *farther* from your character. You move at running speed, which is faster
  but drains **stamina** (see below).

The two-tier rule is "close = walk, far = run." Hold the button and steer by moving the
cursor; release to stop. (Most clients also support keyboard/arrow or WASD-style movement
that follows the same walk/run distinction.)

**For AI agents:** there is no waypoint pathfinder you invoke — movement is a continuous
"face this direction and step" loop. To reach a destination you issue directional steps (or
repeated move-toward-point commands) and re-evaluate after each step. Obstacles are not
auto-routed around; you must detect a blocked step and choose a new direction yourself.

## Stamina and fatigue

**Stamina** (Stam) is the pool that running and exertion consume. When stamina is high you
run freely; as it falls you slow, and at **0 stamina you cannot move at all** until it
regenerates (ServUO sends *"You are too fatigued to move."* and blocks the step —
`Scripts/Misc/WeightOverloading.cs`).

Stamina drains faster when you are **running** than walking, and faster still when you are
**overweight** (see next section). It regenerates over time while you rest. Being mounted
sharply reduces the stamina drain from carried weight.

## Weight and being overweight

Everything you carry has a **weight in stones**. Your maximum carry weight is set by your
**Strength**:

- **Max carry weight = base + (3.5 × Strength)**, where base is **100** stones for a Human
  on this ruleset (or 40 otherwise) — `Scripts/Mobiles/PlayerMobile.cs`.
- You may exceed it by a small **overload allowance of 4 stones** before fatigue kicks in
  (`OverloadAllowance = 4`, `Scripts/Misc/WeightOverloading.cs`).

When you go past that allowance, **every step drains extra stamina**, scaling with how far
over you are; running doubles the drain and being mounted divides it by three
(`GetStamLoss`). If the overload empties your stamina, the step is **blocked** with
*"You are too fatigued to move, because you are carrying too much weight!"* — in practice,
**too heavy = you can't move.**

To fix overweight: drop or bank items, raise Strength, or load excess onto a [pack
animal](/playing/taming-and-pets/). For how items and their weights work, see
[Items & inventory](/playing/items-and-inventory/). For Strength and stats, see
[Character & stats](/playing/character-and-stats/).

## Riding a mount

A **mount** (horse, llama, or other rideable creature) moves faster than running on foot
and greatly reduces the stamina cost of carried weight. To ride:

1. Acquire and (if it is a wild creature) **tame** the animal — see
   [Taming & pets](/playing/taming-and-pets/).
2. **Double-click the mount** while standing next to it to climb on; double-click again (or
   use the mount's context menu) to dismount.

A tamed mount that you do not own will not let you ride it. Mounts can also be blocked,
fatigued, or dismounted in combat depending on circumstances.

## What blocks movement

- **Walls, mountains, and impassable terrain** stop you — you cannot walk through solid
  objects.
- **Deep water** blocks land travel; crossing the sea needs a boat (below).
- **Closed doors** block the tile. **Double-click a door** to open it, then step through.
  (For AI agents: opening a door is a required, separate action — a closed door reads as a
  blocked step.)
- **Line of sight / reachability** matters for interacting with things you pass, and some
  travel spells refuse a destination they cannot resolve.

## Long-distance travel overview

Walking across the world is slow. The fast options, in roughly increasing convenience:

| Method | What it does | Needs |
| --- | --- | --- |
| **Recall** | Teleports *you* to a marked rune's spot | Magery/scroll, reagents, mana, a marked rune |
| **Gate Travel** | Opens a two-way portal others can also use | Higher Magery/scroll, more reagents+mana, a marked rune |
| **Runebook** | Holds many runes for quick Recall/Gate | A runebook filled with marked runes |
| **Moongates** | Public gate network between cities/facets | Walk into a moongate; pick a destination |
| **Boats** | Sea travel across water | A ship and its key/commands |

All magical travel consumes **reagents and mana** and can be blocked at certain
destinations (guarded zones, housing, dungeons with anti-recall rules). Reagent and mana
details live on the spell pages linked below.

## Recall

**Recall** instantly transports you to the location stored in a **marked rune**.

1. **Mark a rune** at the spot you want to save — cast **Mark** on a blank recall rune while
   standing there. The rune now remembers that exact location.
2. To travel, cast **Recall** and **target the marked rune** (or a runebook entry). You
   appear at the saved spot.

Recall moves only you (and what you carry / your following pets, per the rules). It needs
Magery (or a Recall scroll), reagents, and mana. See
[Recall](/magic/circle-4/recall/) for the exact reagents, mana cost, and skill thresholds,
and [Magery](/skills/magery/) for casting.

## Gate Travel

**Gate Travel** opens a **moongate-like portal** between your location and a marked rune's
location. Unlike Recall, the portal is a doorway **other players (and pets) can also walk
through**, making it the standard way to move a group.

1. Have a **marked rune** (or runebook entry) for the destination.
2. Cast **Gate Travel** and target the rune. A blue gate appears at your feet and another at
   the destination.
3. **Double-click / step into** the gate to cross.

Gate Travel is a higher-circle spell than Recall and costs more reagents and mana. See
[Gate Travel](/magic/circle-7/gate-travel/) for exact requirements.

## Runes and runebooks

A **recall rune** stores one location once it is marked. A **runebook** is a container that
holds many runes in labeled slots, so you can Recall or Gate to any of them without
carrying loose runes. Open the runebook, pick an entry, and choose **Recall** or **Gate**
from it. Runebooks make travel networks practical (banks, dungeons, your house, vendor
hubs).

## Moongates

**Moongates** are the **public, free gate network** linking the major cities and the game's
facets. You do not need spells or reagents to use them.

1. Walk to a city moongate.
2. Activate it (step into it / use its menu) and choose a destination from the gate list.

Which destination a moongate offers can depend on the **phase of the moon** in classic UO,
so the available exit cycles over time. The cities, dungeons, and the moongate layout for
this shard are documented under [World](/world/) — see
[Moongates & shrines](/world/moongates-and-shrines/) for the network, and individual city
pages such as [Britain](/world/britain/) for where each gate sits. Coordinates are not
repeated here; follow those links.

## Boats and sea travel

Open water blocks walking, so crossing the sea uses a **boat**. In brief:

- You obtain a ship (from a shipwright or a deed) and place it on water.
- You **double-click the ship's key** (or speak movement commands like *forward*, *back*,
  *turn*) to pilot it; the deck carries you and anything aboard.
- Recall and Gate can interact with boats via the ship's key in some cases (see
  [Recall](/magic/circle-4/recall/)).

This is a brief overview; detailed ship handling is out of scope for this page.

## Shrine and sacred travel

Britannia's **shrines** are fixed world locations (the Virtue shrines) tied to resurrection
and other rituals rather than a personal teleport network. See
[Moongates & shrines](/world/moongates-and-shrines/) for their locations and roles. Whether
any shrine offers direct travel on this shard is **(unverified)** and pending in-game
confirmation.

## Quick reference for agents

- **Move** = continuous click-to-move; near = walk, far = run.
- **Door** = double-click to open before stepping through.
- **Mount** = double-click to ride; faster + less weight fatigue.
- **Overweight** (> Str-based max + 4) = stamina drain, then blocked steps.
- **Cross the map** = Recall (self) or Gate (group) to a marked rune; both cost
  reagents+mana — see [/magic/](/magic/).
- **Public transit** = moongates, no cost — see [/world/moongates-and-shrines/](/world/moongates-and-shrines/).

## See also

- [Items & inventory](/playing/items-and-inventory/) — weight, backpack, dropping items
- [Taming & pets](/playing/taming-and-pets/) — getting and riding a mount
- [Character & stats](/playing/character-and-stats/) — Strength and carry weight
- [Recall](/magic/circle-4/recall/) · [Gate Travel](/magic/circle-7/gate-travel/) · [Magery](/skills/magery/)
- [World](/world/) · [Moongates & shrines](/world/moongates-and-shrines/) · [Britain](/world/britain/)
