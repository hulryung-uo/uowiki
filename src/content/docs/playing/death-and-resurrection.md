---
title: Death & Resurrection
description: What happens at 0 HP — becoming a ghost, your corpse and loot, getting resurrected, item insurance, and retrieving your body.
status: unverified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (bandage resurrection thresholds)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page explains dying and coming back. For preventing death see
[Healing](/playing/healing/); for getting res'd specifically by bandage see
[Healing → Resurrecting with a bandage](/playing/healing/#resurrecting-with-a-bandage);
for murderer/notoriety effects see [Notoriety & PvP](/playing/notoriety-and-pvp/).

## What happens at 0 HP

When your hit points reach **0**, you **die** and become a **ghost**:

- Your character turns into a **grey, translucent ghost** and can move freely.
- As a ghost you **cannot be easily heard** by the living — your speech comes out as
  "**Oooo**" sounds to other players unless they have [Spirit Speak](/skills/spirit-speak/)
  active (which lets them hear ghosts).
- You **cannot attack, cast, or interact** with most of the world while dead. You wander
  until you are resurrected.

## Your corpse and loot

When you die, a **corpse** is left at the spot you fell:

- It holds your **loot** — most items you were carrying and wearing drop to the corpse,
  unless they are **blessed**, **newbied**, or **insured** (see below).
- Other players (and, in dungeons, monsters/looters) can take from your corpse, depending
  on the area's ruleset and your notoriety. Recover your body quickly.
- Your corpse decays over time, so don't dawdle.

## What stays with you vs what drops

- **Blessed items** — never drop on death; they stay equipped/in your pack. Starting gear
  and many quest items are blessed.
- **Newbied items** — like blessed for newcomers; remain on you.
- **Insured items** — items you paid to **insure** stay with you on death (a fee is
  deducted on each death from your insurance funds). This is the modern way to protect
  valuable gear.
- **Everything else** — drops to your corpse and can be looted.

Exact insurance cost/mechanics are **shard-dependent and unverified here** — confirm on
[the shard config](/shard/). Manage and insure items via
[Vendors & banking](/playing/vendors-and-banking/) and
[Items & inventory](/playing/items-and-inventory/).

## Ghost movement

As a ghost you can **walk and run normally** to reach a place where you can be
resurrected. You pass freely and are not attacked. You generally cannot use doors,
mounts, or most items while dead. Head for the nearest healer, shrine, or living friend.

## Getting resurrected

Several methods bring a ghost back to life:

- **Wandering Healer NPCs** — roving healers in the wilderness will resurrect you on
  approach (double-click them). They are the classic "walk your ghost to a healer" option.
- **Town Healer NPCs** — healers stationed in towns and at healer buildings resurrect you.
  See [the world / towns](/world/). **Note:** town/NPC healers will **not** resurrect
  flagged **murderers** (red characters) — see
  [Notoriety & PvP](/playing/notoriety-and-pvp/).
- **Shrines** — moongate/virtue **shrines** can resurrect a ghost who reaches them; see
  [moongates & shrines](/world/moongates-and-shrines/).
- **A player's Resurrection spell** — a [Magery](/skills/magery/) caster (8th-circle
  Resurrection) can res you on the spot.
- **A player's bandage** — a healer with **Healing ≥ 80 and Anatomy ≥ 80** can resurrect
  you with a bandage (verified in `Bandage.cs`; full procedure in
  [Healing](/playing/healing/#resurrecting-with-a-bandage)).
- **Chivalry / other** — some systems (e.g. Chivalry's Resurrect) can also res
  (unverified availability).

**To accept a resurrection:** you are shown a **resurrect gump** — click to accept and you
return to life with low HP at that location.

## Resurrection penalty

On modern AOS-and-later rules the penalty for dying is **minimal** — typically you come
back at low HP/stat/mana and may take a short stat/skill dip that recovers, rather than the
heavy permanent loss of early eras. The **exact penalty is shard-dependent and unverified
here**; check [the shard rules](/shard/). (Resurrecting a **dead pet** does cost the pet a
small permanent skill loss, ~0.1 per skill, per `Bandage.cs`.)

## Retrieving your corpse and loot

After you are resurrected:

1. **Return to your corpse** (you respawned wherever you got res'd, which may be far away —
   you may need to travel back; see [Movement & travel](/playing/movement-and-travel/)).
2. **Loot your own corpse** — open it and drag your items back. Anything **insured/blessed**
   never left you, so you only need to reclaim the rest.
3. Re-equip your weapon and armor, re-bandage/heal up, and you're ready again.

If you cannot reach the body in time (it decayed or was looted), your dropped items are
gone — which is exactly why insurance and blessed gear matter for valuables.

## See also

- [Healing](/playing/healing/) — including bandage and spell resurrection
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — murderers can't be res'd by town healers
- [The world & towns](/world/), [moongates & shrines](/world/moongates-and-shrines/)
- [Items & inventory](/playing/items-and-inventory/), [Vendors & banking](/playing/vendors-and-banking/)
- [Spirit Speak](/skills/spirit-speak/) — hearing and aiding ghosts
- [The shard rules](/shard/) — insurance and penalty specifics
