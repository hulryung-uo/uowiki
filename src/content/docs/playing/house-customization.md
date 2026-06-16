---
title: Customizing Your House
description: How house customization works on this shard — entering design mode on a foundation, the design tools (walls, floors, stairs, roofs, doors, teleporters), multiple stories, the commit/backup/revert workflow, and the gold cost charged from your bank.
status: source-verified
sources:
  - "servuo: Scripts/Multis/HouseFoundation.cs (BeginCustomize, Designer_* commands, MaxLevels, commit cost, fixtures)"
  - "servuo: Scripts/Multis/BaseHouse.cs (MovingCrate, RelocateEntities/RestoreRelocatedEntities)"
last_verified: 2026-06-16
generated: false
---

A **customizable house** lets you design the whole interior — walls, floors, stairs,
roofs, doors, and teleporters — yourself, tile by tile, instead of living in a fixed shell.
This page is the full walkthrough of the design system. For the house shells themselves and
how to get one, see [House Types](/playing/house-types/); for the day-to-day mechanics
(lockdowns, decay, vendors), see [Housing](/playing/housing/).

## What can be customized

Only a **customizable foundation** can be redesigned. When you place a *foundation* deed you
pick the footprint (an empty platform), then build the structure on top. **Classic
pre-built houses** (the cottage, tower, keep, castle shells) are placed as-is and **cannot**
be freely redesigned — choose a foundation if you want to design your own layout. See the
two paths on [House Types](/playing/house-types/).

## Entering design (customize) mode

Stand in your house, open the **house sign**, and choose **"Customize This House."** Only the
**owner** can do this, and not while in combat (*"Wouldst thou flee during the heat of
battle??"*). Entering design mode (`HouseFoundation.BeginCustomize`):

- **Clears the house for editing** — your locked-down items are set aside, and any other
  players and pets inside are moved out to the sign. Stewards/mannequins are re-deeded.
- Drops you into a private **design view** where only you see the work-in-progress; visitors
  outside still see the old house until you commit.

Your belongings are restored when you commit (see [below](#committing-backing-up-and-reverting)).

## The design tools

In design mode the client shows the **House Design Tool** palette. The building actions
(`Designer_*` packet handlers in `HouseFoundation.cs`) are:

| Tool | What it does |
|---|---|
| **Walls** | place wall, window, and archway pieces around the footprint |
| **Floors / tiles** | lay floor tiles (and the various floor materials) |
| **Stairs** | place stairs that connect one story to the next |
| **Roofs** | place roofing pieces (Samurai-Empire roof system: pitch and height per piece) |
| **Doors** | place house doors — tracked as **fixtures** (see below) |
| **Teleporters** | place paired teleporters — also **fixtures**, used to link floors |
| **Eraser / Delete** | remove the piece under the cursor |
| **Level** | switch which **story** you are editing (see below) |
| **Synchronize** | re-sync the design view with the server if it drifts |

Doors and teleporters are **fixtures**: the foundation tracks them as a set and rebuilds
them around your walls, so you place them with the door/teleporter tools rather than as loose
items.

## Stories (levels)

A foundation supports multiple **stories**, set by its footprint (`HouseFoundation.MaxLevels`):

- **3 stories** for normal foundations, **4 stories** if the plot is **14 tiles or larger**
  in either dimension.
- Each level sits **20 z apart** (`GetLevelZ`), and you switch between them with the
  **Level** control while designing.
- Use **stairs** to walk between adjacent floors, or **teleporters** to jump between any two
  (handy for towers and split layouts). A **roof** tops the structure.

## Committing, backing up, and reverting

Designing is non-destructive until you **commit**. The design tool gives you:

- **Backup** — save a checkpoint of the current design.
- **Restore** — roll the design back to your last backup.
- **Revert** — discard all changes and return to the last committed house.
- **Clear** — wipe back to the empty foundation to start over.
- **Commit** — finalize the design, rebuild the real house, and **restore your items**.

When you **commit**, items that were set aside come back; anything that no longer fits the new
layout is dropped into a **moving crate** inside the house (`BaseHouse.MovingCrate`) for you
to re-place. Because moving a wall can shift where a decoration lands, expect to **re-place
some locked-down décor** after a big redesign — see [Decorating](/playing/decorating/).

## What it costs

- **Activating customize mode is free** on this shard (`CustomizationCost` is `0` under AOS;
  it was a flat 10,000 gold only on pre-AOS rules).
- **Committing a design charges gold from your bank** equal to the **price of the new design
  minus the price of the old one** (`HouseFoundation` commit logic). A bigger or more
  elaborate layout (more walls, floors, fixtures) costs more; if you **simplify** a design,
  the difference is **refunded** to your bank instead
  (*"~1_AMOUNT~ gold has been withdrawn from / deposited into your bank box."*).
- You therefore need the gold **in your bank** to commit an upgrade — if you can't afford the
  difference, the commit won't go through.

## A practical workflow

1. **Empty the house first** (or accept that loose décor lands in the moving crate). Bank
   anything you don't want disturbed.
2. House sign → **Customize This House**.
3. Build **floor by floor**: lay floors, raise walls, add doors, then place **stairs** (or
   teleporters) to connect levels, and finish with a **roof**. Use the **Level** control to
   move between stories.
4. **Backup** often so a misstep is one **Restore** away.
5. When happy, **Commit** (pay the difference) — or **Revert** to throw it all away.
6. Re-place décor from the **moving crate** and [decorate](/playing/decorating/) with the
   [Interior Decorator](/playing/decorating/#the-interior-decorator-tool).

## See also

- [House Types](/playing/house-types/) — foundations vs. classic shells, sizes, and storage
- [Housing](/playing/housing/) — placing, lockdowns/secures, decay, vendors
- [Decorating](/playing/decorating/) — furnishing the interior once it's built
