---
title: Monster Stealing
description: Use the Stealing skill on certain creatures to lift special consumables and ingredients from them — a thief's alternative to picking pockets.
status: source-verified
sources:
  - "servuo: Scripts/Services/Monster Stealing/Core/StealingHandler.cs (HandleSteal, once-per-creature)"
  - "servuo: Scripts/Services/Monster Stealing/Core/BaseThieveConsumable.cs (stealable balms, lotions, ingredients)"
last_verified: 2026-06-18
generated: false
---

**Monster stealing** lets a thief turn the [Stealing](/skills/stealing/) skill on **creatures**
(not just players and containers) to lift **special items** off them — a niche but rewarding use
of an otherwise PvP/utility skill.

## How it works

Target a stealable creature with Stealing (`StealingHandler.HandleSteal`):

- A successful steal pulls a **special consumable or ingredient** from the creature — things
  like **balms and lotions** (`BaseThieveConsumable`) and other thief-only materials.
- Each creature can be **stolen from only once** — once emptied you get *"That creature has
  already been stolen from. There is nothing left to steal."*
- It's risky: failing (or stealing from a live, dangerous creature) can turn the fight against
  you, so thieves pick their moment.

## Why do it

The items you can only get this way (thief consumables and ingredients) give a dedicated
**[Stealing](/skills/stealing/)** character a reason to hunt beyond pickpocketing — a supply of
materials that don't drop any other way.

## See also

- [Stealing](/skills/stealing/) · [Snooping](/skills/snooping/) — the thief's core skills
- [Hiding & stealth](/playing/hiding-and-stealth/) — staying unseen while you work
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — the risks of a thief's life
