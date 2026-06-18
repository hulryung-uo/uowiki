---
title: Armor Refinement
description: Refine crafted armor for extra resistance using refinement components — reinforcing for more defense, deflecting for resist, assembled and applied through the armor refiner.
status: source-verified
sources:
  - "servuo: Scripts/Services/Armor Refinement/Items.cs (RefinementType Reinforcing/Deflecting, craft types, ModType)"
  - "servuo: Scripts/Services/Armor Refinement/ArmorRefiner.cs"
last_verified: 2026-06-18
generated: false
---

**Armor refinement** is an end-game crafting layer that adds **extra resistance** to armor
beyond what materials and [enhancement](/playing/item-enhancement/) provide. You collect
**refinement components**, combine them, and apply the result to a piece with the **Armor
Refiner**.

## Refinement components

Refinements come as **components** (`RefinementComponent`) of a few kinds (`Items.cs`):

- **Type** — **Reinforcing** or **Deflecting** (the two flavors of the resist bonus).
- **Craft type** — tied to the armor's craft: **Blacksmith**, **Tailor**, or **Carpentry**
  components match metal, leather/cloth, and wood armor respectively.
- **Mod type** — what stat the refinement boosts (e.g. **Defense**).

Components drop/are obtained at various **intensities**; you assemble matching components into a
usable refinement through the refiner's gump.

## Applying a refinement

Use the **Armor Refiner** on the assembled refinement and target an armor piece whose **craft
type matches** (blacksmith refinement on metal armor, etc.). A successful application adds the
refinement's **resistance bonus** to that piece — letting a finished suit push its resists
higher than crafting alone allows.

## Notes

- Refinements stack on top of base material resists, **exceptional** quality, and the crafter's
  [Arms Lore](/skills/arms-lore/) bonus — it's a min-maxer's tool for squeezing armor toward the
  **70% resist cap** (see [Armor](/items/armor/)).
- Match the **craft type** to the armor, or the refinement won't apply.

## See also

- [Armor](/items/armor/) — base resists, materials, and the 70% cap
- [Item Enhancement](/playing/item-enhancement/) — the other way to boost a finished piece
- [Crafting](/playing/crafting/) — making the armor you'll refine
