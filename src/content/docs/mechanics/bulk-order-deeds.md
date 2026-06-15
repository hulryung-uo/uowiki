---
title: Bulk Order Deeds (BODs)
description: How Bulk Order Deeds work on this shard — the point-based reward system, how to obtain small and large BODs, skill gates, and the smith/tailor reward catalogs with point costs.
status: source-verified
sources:
  - "servuo: Scripts/Services/BulkOrders/BulkOrderSystem.cs (NewSystemEnabled = Core.TOL, 6h delay, 2 cached, point banking)"
  - "servuo: Scripts/Services/BulkOrders/SmallBODs/SmallSmithBOD.cs (amount/material/exceptional gating)"
  - "servuo: Scripts/Services/BulkOrders/LargeBODs/LargeSmithBOD.cs (large-BOD sets)"
  - "servuo: Scripts/Services/BulkOrders/Rewards/Rewards.cs (reward collections + point costs)"
  - "servuo: Scripts/Mobiles/NPCs/BaseVendor.cs (context-menu offer flow)"
last_verified: 2026-06-15
generated: false
---

**Bulk Order Deeds (BODs)** are crafting contracts handed out by NPC crafters: make a set
quantity of an item to a required quality, turn the filled deed back in, and earn rewards —
the long-game income and gear pipeline for every crafter. This shard runs the **modern,
point-based BOD system** (`BulkOrderSystem.NewSystemEnabled = Core.TOL`, and our expansion is
**EJ**, which is past TOL). Turning in BODs banks **points** per craft type that you spend
from a reward menu — you are not locked into whatever single reward a deed rolled.

This page documents the rules from `Scripts/Services/BulkOrders/`. For the recipes themselves
see [Crafting](/crafting/); for the skills, [Blacksmithy](/skills/blacksmithy/) and
[Tailoring](/skills/tailoring/).

## Which NPCs give which BODs

Talk to (open the **context menu** on) the matching crafting NPC and choose the bulk-order
option. Each craft type has its own deeds and its own point bank:

| Craft type | NPCs that offer it |
|---|---|
| **Smith** | Blacksmith, Weaponsmith, Armorer, Blacksmith Guildmaster |
| **Tailor** | Tailor, Weaver |
| **Tinkering** | Tinker |
| **Inscription** | Scribe |
| **Alchemy** | Alchemist |
| **Cooking** | Cook |
| **Fletching** | Bowyer |
| **Carpentry** | Carpenter |

## Getting a deed: the 6-hour timer

- A new deed becomes available **every 6 hours** per craft type
  (`BulkOrderSystem.Delay = 6`).
- The system **caches up to 2** unclaimed deeds, with a third "in the pipe" if your last one
  was more than 6 hours ago (`MaxCachedDeeds = 2`) — so you can let a couple bank up rather
  than logging in exactly on the timer.
- Timers are **per craft type**: a smith who also tailors runs an independent Smith timer and
  Tailor timer.

## Small BODs

A **small BOD** asks for a quantity of **one** item. Three things define it:

- **Amount:** **10, 15, or 20** of the item (`AmountMax`). Higher skill skews the roll toward
  larger amounts.
- **Exceptional:** the deed may require every item be **exceptional** quality. For smithing
  this only happens at skill **≥ 70.1**, where the chance is `(skill + 80) / 200` — about
  **90% at GM** (100 skill).
- **Material:** the deed may demand a specific **colored material** (Dull Copper → Valorite
  for smithing; Spined / Horned / Barbed leather for tailoring). Material BODs only roll at
  skill **≥ 70.1**, and the rarer the material the rarer the deed — the weighting runs from
  ~25% Dull Copper down to ~0.2% Valorite (`m_BlacksmithMaterialChances`).

Higher amount + exceptional + a rare material = far more points (and a far harder fill).

## Large BODs

A **large BOD** bundles a themed **set** of small BODs into one contract for a bigger payout.
For smithing the sets are (`LargeSmithBOD.cs`): **Ring**mail, **Plate**, **Chain**mail,
**Axes**, **Fencing**, **Maces**, **Pole**arms, and **Swords**. To build one:

1. Obtain (or buy from other players) the **small BODs** that match a set, all with the
   **same amount and the same material/exceptional requirement**.
2. Drop each matching small BOD onto the **large BOD deed** to fill its slots.
3. When every slot is filled and crafted, turn the large BOD in for its (larger) reward.

This is why crafters trade small BODs: assembling a matched set into a large deed is worth
much more than the smalls individually.

## Rewards: banking and spending points

When you hand a completed deed back to the NPC, its value is **added to your point bank** for
that craft type (`BankedPoints`). Point value scales with the **amount**, whether it was
**exceptional**, the **material** rarity, and (for large BODs) the number of items in the set.
The accompanying **gold and fame** scale roughly as `(points / 50)²`, so a big exceptional
material deed pays out steeply more gold than a plain 10-count.

You then spend banked points from the **reward menu**. Selected smith rewards and their point
costs (`SmithRewardCalculator`):

| Reward | Point cost |
|---|---|
| Sturdy shovel / smith hammer | 10 |
| Sturdy pickaxe · smith title | 25 |
| Leather mining gloves · prospector's tool · gargoyle's pickaxe | 100–200 |
| Powder of temperament · ringmail mining gloves | 450 |
| **Runic hammer — Dull Copper** | **500** |
| Runic hammer — Shadow Iron | 550 |
| Runic hammer — Copper | 650 |
| Runic hammer — Bronze | 700 |
| Runic hammer — Gold | 950 |
| Runic hammer — Agapite | 1050 |
| Runic hammer — Verite | 1150 |
| **Runic hammer — Valorite** | **1200** |
| Colored anvil · Blacksmithy power scrolls (+5 / +10 / +15 / +20) | (group rewards) |

Runic hammers carry **`55 − 5×tier` charges** — a Dull Copper hammer has 50 charges, a
Valorite hammer only 15 — so the rarest runics are also the most rationed.

Selected tailor rewards (`TailorRewardCalculator`):

| Reward | Point cost |
|---|---|
| Sewing kit · cloth · tailor title | 10 |
| Colored sandals | 150 |
| **Runic sewing kit — Spined** | **350** |
| Tapestry · Tailoring +5 power scroll | 400 |
| Bear rug | 450 |
| Tailoring +10 power scroll | 500 |
| Clothing bless deed | 550 |
| **Runic sewing kit — Horned** | **600** |
| Tailoring +20 power scroll | 650 |
| **Runic sewing kit — Barbed** | **700** |

## Crafter takeaways

- Visit your crafting NPC every few hours and **let deeds bank** (up to 2–3) — they cost
  nothing to hold.
- Push your craft skill to **70.1+** to unlock exceptional and material deeds; **GM** maximizes
  the exceptional rate and point value.
- **Trade and collect matching small BODs** to assemble large BODs — the point math rewards it.
- Bank toward the **runic tool** you want: runic hammers/kits are the gear pipeline (high-resist
  armor and high-property weapons) that makes a crafter's vendor worth visiting.

## See also

- [Blacksmithy](/skills/blacksmithy/) · [Tailoring](/skills/tailoring/) — the two biggest BOD crafts
- [Crafting](/crafting/) — the recipe tables (with item stats)
- [Items: resources](/items/resources/) — the ingots, leather, and materials BODs consume
- [Blacksmith profession](/professions/blacksmith/) — the smith's long game
