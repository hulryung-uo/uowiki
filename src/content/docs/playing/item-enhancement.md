---
title: Item Enhancement
description: Enhance a crafted weapon or armor with a special material to add that material's bonuses — at the risk of failing or destroying the item. Plus Powder of Fortifying for durability.
status: source-verified
sources:
  - "servuo: Scripts/Services/Craft/Core/Enhance.cs (EnhanceResult Success/Failure/Broken, success-chance check)"
  - "servuo: Scripts/Services/BulkOrders/Items/PowderOfFortKeg.cs (Powder of Fortifying)"
last_verified: 2026-06-17
generated: false
---

**Enhancement** lets a crafter take an already-made **weapon or armor** and **re-forge it with
a special material** — a colored ingot or special leather — so the finished item gains *that
material's* bonuses (extra resists, damage, or properties) on top of what it already has. It's
how you turn a plain exceptional piece into a colored, boosted one — but it's a **gamble**.

## How it works

From the crafting tool's menu, choose **Enhance**, target your item, and supply the
**resource** (`Enhance.Invoke` in `Enhance.cs`): for example enhance a plate piece with
**valorite ingots**, or leather armor with **barbed leather**, to add that material's bonus.

Your **success chance** is the craft-skill success chance for making that item in that
material — so a high-skill crafter enhancing a piece they could easily craft has good odds,
while enhancing a high-end item in a rare material is risky.

## The three outcomes

The roll (`Enhance.CheckResult`) lands on one of:

| Result | What happens |
|---|---|
| **Success** | The item gains the material's bonuses. |
| **Failure** | Enhancement fails — the item is unchanged, but the **resources are consumed**. |
| **Broken** | The worst case — the **item is destroyed** (`item.Delete()`). |

So only enhance gear you can afford to lose, and prefer **exceptional** items and a maxed
crafter to tilt the odds toward Success. (Some items are flagged so they **can't** be enhanced
at all.)

## Powder of Fortifying

A related crafter consumable: **Powder of Fortifying** (a [Bulk Order Deed](/mechanics/bulk-order-deeds/)
reward) **raises an item's maximum durability** back up. Since [repairing](/items/weapons/#durability-and-repair)
slowly lowers an item's max durability over its life, powder of fortifying is how you keep a
valuable enhanced piece from wearing out — apply it before the max gets too low.

## See also

- [Weapons](/items/weapons/) and [Armor](/items/armor/) — quality, materials, and durability
- [Crafting](/playing/crafting/) · [Blacksmithy](/skills/blacksmithy/) · [Tailoring](/skills/tailoring/)
- [Items: resources](/items/resources/) — the ores and leathers you enhance with
- [Bulk Order Deeds](/mechanics/bulk-order-deeds/) — where Powder of Fortifying comes from
