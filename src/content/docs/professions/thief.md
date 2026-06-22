---
title: Thief
description: Take what isn't yours and vanish — stealing, snooping, hiding, and stealth. The rogue skills, how it works, the risks, and how thieves earn.
status: source-verified
sources:
  - "servuo: Scripts/Skills/Stealing.cs"
  - "servuo: Scripts/Skills/Snooping.cs"
  - "wiki cross-references; general UO play"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The thief lives by sleight of hand and a quick exit: lift valuables from packs, monsters, and
other players, then melt into the shadows before anyone reacts. It's the highest-risk,
highest-skill rogue path — a successful theft can net a rare artifact, a failed one can flag
you criminal and get you killed. A thief carries almost no gear because anything could be
lost in a getaway.

## Core skills

- [Stealing](/skills/stealing/) — the core skill: lift items from NPCs, players, and live monster packs. Your success roll is against the item's **weight** (the check is roughly weight×10 ±25 skill), and **nothing over 10 stones can be stolen at all** ("That is too heavy to steal"). Both hands must be free, and you must be in the **Thieves Guild** to steal from another player (`Scripts/Skills/Stealing.cs`).
- [Snooping](/skills/snooping/) — peek inside another's backpack before you steal, so you target the valuable item rather than grabbing blind. Snooping rolls your skill (and failing can reveal you); each snoop costs a little **karma** (−4) (`Scripts/Skills/Snooping.cs`).
- [Hiding](/skills/hiding/) — drop out of sight on the spot; your escape button after a lift.
- [Stealth](/skills/stealth/) — **move while hidden** so you can reposition and slip away instead of being pinned where you vanished.
- [Lockpicking](/skills/lockpicking/) — optional, to crack locked chests and containers you can then loot.
- [Detecting Hidden](/skills/detecting-hidden/) — optional, to spot rival hiders and traps.

## The build

There is **no dedicated thief template** in this wiki yet. Build it around Stealing +
Snooping + Hiding + Stealth as the four-skill rogue core, then add
[Lockpicking](/skills/lockpicking/), [Detecting Hidden](/skills/detecting-hidden/), and a
survival or escape skill such as [Magery](/skills/magery/) (for Recall). See
[7x GM Templates](/templates/seven-gm/) for fitting all seven under the 700-point cap.

## How to play it

Read [Hiding & Stealth](/playing/hiding-and-stealth/) — the mechanics of vanishing, moving
unseen, and being revealed. The core loop: [Hide](/skills/hiding/), approach a target under
[Stealth](/skills/stealth/), [Snoop](/skills/snooping/) the pack to find the prize,
[Steal](/skills/stealing/) it, then hide and stealth away before the reveal lands.

Getting **caught** lifting from an innocent person or their corpse calls `CriminalAction`,
which lets guards and victims attack you freely — and stealing from a player additionally
**requires Thieves Guild membership** in the first place (`Scripts/Skills/Stealing.cs`).
Understand the consequences in [Notoriety & PvP](/playing/notoriety-and-pvp/) before you lift
from a person. Stealing from live monster packs is lower-risk — the code never marks those
thefts as "caught" — and is where the rare drops are. A thief's whole craft is leaving before
the flag matters.

## Gear & tools

- Carry **almost nothing of value** — anything in your pack can be lost if you die mid-getaway.
- A lockpick for [Lockpicking](/skills/lockpicking/) targets — see [tools](/items/catalog/tools/).
- Light [armor](/items/armor/) for mobility; no shield, nothing that slows the escape.
- A spellbook and [reagents](/items/reagents/) only if you've taken Magery for Recall escapes.

## Making a living

Thieves earn by **stealing valuables** — gold, gems, reagents, and the occasional high-value
item lifted from NPCs and players. The safer and often more lucrative play is
**stealing from monster packs**, where powerful [bestiary](/bestiary/) creatures can yield
rare artifacts to a successful lift. Fence the proceeds via
[Vendors & Banking](/playing/vendors-and-banking/). Income is spiky — feast or nothing — but
a good theft beats hours of farming.

## See also

- [Treasure Hunter](/professions/treasure-hunter/) — the other rogue path, shares Lockpicking
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — the criminal flag and its consequences
- [Hiding & Stealth](/playing/hiding-and-stealth/) — the mechanics of vanishing
- [Stealing](/skills/stealing/) · [Snooping](/skills/snooping/) · [Hiding](/skills/hiding/) · [Stealth](/skills/stealth/) · [Lockpicking](/skills/lockpicking/)
