---
title: Housing
description: How to place a house from a deed, customize it, lock down and secure items, manage keys and co-owners/friends, keep the house from decaying, set up a player vendor, and the shard's one-house-per-account rule.
status: unverified
sources:
  - "servuo: Config/Housing.cfg (AccountHouseLimit=1)"
  - "servuo: Config/General.cfg"
  - "wiki: /shard/server-rules/ (housing config)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

A house is your private, persistent space in the world — storage, a base of operations,
and a shopfront. This page walks through placing one, locking your belongings down so
they are safe, granting access to others, keeping the house alive, and selling goods from
a [player vendor](/playing/vendors-and-banking/).

The single most important shard rule up front: **one house per account**
(`AccountHouseLimit=1`, from `Config/Housing.cfg`; see [server rules](/shard/server-rules/)).

## Placing a house

You place a house from a **house deed** onto a valid, open plot of land.

**To place a house:**

1. **Obtain a house deed** (bought from an architect/real-estate NPC or another player).
   The deed corresponds to a specific house size/style.
2. **Find an open plot** — flat, unobstructed ground large enough for the house's
   footprint, not overlapping roads, other houses, spawn points, or no-build regions.
   Towns and many special regions do not allow placement.
3. **Double-click the deed.** A translucent **footprint preview** appears under your
   cursor showing exactly where the house will sit.
4. **Position the footprint** until it shows as a valid (placeable) location, then
   **confirm** placement.
5. The deed is consumed and the house appears, with you as its **owner**. You receive the
   **house key**.

If placement is blocked, the client tells you why (obstruction, too close to another
house, invalid region). Move and try again.

**Which house to place?** See [House Types](/playing/house-types/) for the full catalogue —
every classic (pre-built) house and customizable foundation, with footprint, storage, cost,
and an exterior render of each. Once it's standing, [Decorating](/playing/decorating/) walks
through furnishing the interior.

## Customization

Many house styles are **customizable**: you enter a design/customization mode (via the
house sign or a command menu) and edit walls, floors, doors, stairs, and roofing within
the plot's footprint and a storage/fixture budget. Pre-built (classic) houses are placed
as-is and are not freely redesignable. Exact customization limits are **unverified** —
open the house sign menu to see the options your house supports.

## Lockdowns and secures

By default, items you drop inside a house are loose — they can **decay** and, in PvP
rules, may be vulnerable. To keep belongings safe you **lock them down** or **secure** a
container.

- **Lockdown** — pins an item in place so it does not decay and cannot be casually moved
  or stolen by visitors. Lock down decorations, crafting tools, and display pieces.
  **To lock down:** open the house menu (house sign or context menu), choose **Lock Down**,
  and target the item.
- **Secure** — designates a **container** as secured storage. Items inside a secured
  container are protected and only accessible to the access levels you allow. **To secure:**
  choose **Secure** from the house menu and target a container; you then set who may access
  it (owner only, co-owners, friends, or anyone).
- **Release** — the inverse (Release / Unsecure) returns an item or container to loose
  status so you can pick it up or move it.

Both lockdowns and secures count against your house's **storage limits** (below).

## Keys, co-owners, and friends

Houses use a tiered **access system**. From most to least privileged:

| Level | Can do |
|-------|--------|
| **Owner** | Everything: place/demolish, customize, set all access, lock down/secure, ban. |
| **Co-owner** | Most owner powers except demolishing/transferring: access secures, lock down, add friends. |
| **Friend** | Enter freely, open doors, use friend-accessible secures; cannot change the house. |
| **Anyone (public)** | If the house is set **public**, anyone may enter; private houses bar non-friends. |

Manage these from the **house sign** menu: **Add Co-owner**, **Add Friend**, **Remove**,
and **Ban** target a player to set their level.

**Keys:** the owner holds the **house key**, which locks/unlocks the doors. You can make
duplicate keys for trusted players or rekey the house if a key is lost or compromised.
Co-owners and friends can typically open doors without a physical key by virtue of their
access level.

## House decay and refreshing

Houses **decay** over time if neglected. To keep a house alive you must **refresh** it,
which on this shard happens by **the owner (or an account member) visiting / being present
at the house** periodically; visiting resets the decay timer. A house left unrefreshed
degrades through decay stages and eventually collapses, dropping its contents.

Shard-specific note: with **one house per account** and only the *most recently placed*
house auto-refreshing (`Config/Housing.cfg`), keep your single house current and do not
expect an old, replaced house to maintain itself. The exact decay timer values on this
shard are **unverified** — check the house sign, which reports the house's current
condition. Visit regularly to be safe.

## Placing a player vendor

A **player vendor** is an NPC you hire to stand in your house (or on your plot) and sell
your goods to passers-by while you are offline.

**To set up a player vendor:**

1. Acquire a **vendor contract / vendor deed**.
2. Stand where you want the vendor and **use the deed**; name the vendor when prompted.
3. **Stock the vendor**: drag items onto it, and **price** each item. The vendor charges
   you a small ongoing fee from its held gold based on inventory value.
4. Customers **double-click the vendor**, **"buy"** the priced items, and the gold
   accrues to the vendor for you to collect.

Full buying/selling mechanics, fees, and how customers interact are on
[Vendors & banking](/playing/vendors-and-banking/). Keep the vendor funded so it is not
dismissed for unpaid fees.

## Storage limits

Each house has a finite **storage capacity** — a combined budget of **lockdowns** and
**secures** it can hold, scaled by house size (bigger houses store more). When you hit the
limit you cannot lock down or secure anything new until you release something. The exact
per-house numbers on this shard are **unverified**; the house sign menu reports your
current lockdown/secure usage versus the maximum.

## Shard housing rules (summary)

From `Config/Housing.cfg` and [server rules](/shard/server-rules/):

| Rule | Value | Source |
|------|-------|--------|
| **Houses per account** | **1** | `AccountHouseLimit=1` |
| Auto-refresh | Only the **most recently placed** house auto-refreshes | `Config/Housing.cfg` note |

Plan accordingly: choose your one plot deliberately, and refreshing your current house is
what keeps it standing.

## See also

- [House Types](/playing/house-types/) — every house and foundation, with size, storage, and cost
- [Decorating](/playing/decorating/) — furnishing your house with the decorator tool
- [Vendors & banking](/playing/vendors-and-banking/) — player vendors, buying and selling
- [Items & inventory](/playing/items-and-inventory/) — what you store
- [Server rules](/shard/server-rules/) — the housing config in context
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — house access and theft flagging
- [Movement & travel](/playing/movement-and-travel/) — marking a rune to recall home
