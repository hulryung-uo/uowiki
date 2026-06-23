---
title: Decorating
description: A practical guide to decorating your UO house — the in-house decorator tool (turn, raise, lower items), stacking and placement tricks, the lockdown-then-decorate workflow, add-on deeds, dyeing furniture, theme ideas (tavern, library, mage tower, museum), and where to find inspiration.
status: source-verified
sources:
  - "servuo: Scripts/Items/Tools/InteriorDecorator.cs (DecorateCommand Turn/Up/Down + GetHue; CheckUse requires IsCoOwner; Up caps at floorZ+15; works on locked-down/secured items)"
  - "servuo: Scripts/Items/Tools/DyeTub.cs, FurnitureDyeTub.cs (dyeing cloth/furniture)"
  - "servuo: Scripts/Items/Addons/BaseAddonDeed.cs (add-on deeds place multi-tile fixtures)"
  - "servuo: Scripts/Mobiles/NPCs/Mannequin/Mannequin.cs, Scripts/Services/CleanUpBritannia/Items/Steward.cs (both BaseCreature, Blessed/invulnerable, redeedable, CUB rewards)"
  - "general UO decorating practice and community technique knowledge, pending in-game field verification"
  - "wiki: /playing/housing/ (lockdowns/secures), /playing/house-types/ (house shells)"
  - "wiki: /reference/hues/ (dye colors)"
last_verified: 2026-06-23
generated: false
---

A house is a shell; **decorating** is what turns it into a tavern, a wizard's tower, or a
museum of your adventures. This guide covers the tools and tricks players use to place
furniture exactly where they want it, the workflow that keeps your work safe, and a few
themed build ideas. It is **community technique knowledge** (not yet field-verified on this
shard); the underlying mechanics — lockdowns, secures, storage limits — are documented and
sourced on [Housing](/playing/housing/).

Before decorating, you need a house: see [House Types](/playing/house-types/) for the
shells you start from (a fixed classic house, or a customizable foundation you design
first). Everything below assumes you are the **owner or co-owner** of the house.

## The Interior Decorator tool

The **Interior Decorator** is the heart of interior design — the "interior kit" that nudges
furniture into place. It is an item (buy one from an Architect/Carpenter NPC, or craft it)
that you place inside your house and **double-click** to open its menu
(`Scripts/Items/Tools/InteriorDecorator.cs`, `DecorateCommand` = `Turn` / `Up` / `Down`,
plus a `GetHue` color-picker mode that only appears when you are *not* standing in a house).
Pick a mode, then target a **locked-down** item to nudge it without picking it up:

- **Turn** — rotate the item to its next available facing. Many items (chairs, tables, some
  decorations) have several orientations; cycle until it faces the way you want.
- **Up** — lift the item upward by a small z-increment. Use this to set books on a shelf,
  mugs on a table, or stack one decoration on another.
- **Down** — drop the item back toward the floor.

Notes verified from the source: the decorator only works while you are standing **in a
house you own or co-own** (`CheckUse` requires `IsCoOwner`; otherwise *"You must be in your
house to do this."*), and only on items that are **locked down or secured** (loose items
can't be finely positioned and risk decaying). **Up** stops once an item reaches roughly 15
units above the floor (*"You cannot raise it up any higher."*), so you can't push a piece
out through the roof. Add-on components (multi-tile furniture) can be turned. This is why
the golden rule is **lock down first, then decorate**.

## The lockdown-then-decorate workflow

1. **Drop the item** roughly where you want it inside the house.
2. **Lock it down** from the house menu (target the item). It is now fixed and safe from
   decay and casual theft.
3. **Use the decorator tool** to *turn*, *raise*, and *lower* it into its final position.
4. **Repeat**, building up from the floor: rugs and carpets first, then furniture, then the
   small items that sit *on* the furniture (raise those onto the surface).

Every locked-down decoration counts against your house's **lockdown limit**, and secured
containers against your **secure count** — both detailed (with per-house numbers) on
[House Types](/playing/house-types/) and [Housing](/playing/housing/). Decorating and
storage compete for the same budget, so plan: a heavily themed house has less room for
loot, and vice versa.

## Placement tricks

- **Stacking and layering.** Raise an item enough and you can rest a second item on top of
  it — books stacked on a desk, a candle on a mantel, plates on a table. Build vertically
  with repeated *raise* clicks.
- **Raising onto surfaces.** Tables, shelves, and counters have a height; place the small
  item on the floor beside the furniture, lock it down, then *raise* it until it visually
  sits on the surface.
- **Hiding the edges.** Tuck rugs partly under furniture, or use large items to mask the
  seam where a wall meets the floor, for a finished look.
- **Add-on deeds.** Many decorative fixtures — forges, looms, training dummies, fountains,
  large furniture sets, mounted trophies — come as **add-on deeds**. Double-click the deed
  inside your house and target a spot; the add-on builds in place and is owned by the house
  (re-deedable later via the house menu). Add-ons are the easiest way to place big,
  multi-tile pieces.
- **Carpets and floor tiles** lay flat and are a quick way to define rooms or zones inside
  an open customizable foundation.

## Dyeing and recoloring

Color ties a room together. Many furniture pieces and cloth items can be **dyed**:

- **Dye tubs** recolor cloth, clothing, and some furniture. Apply a dye tub to a furniture
  dye tub or a clothing item, then target the piece to apply the tub's current hue.
- **Furniture dye tubs** specifically recolor wooden furniture to match a palette.
- Pick hues deliberately — see the [hue reference](/reference/hues/) for the shard's color
  values, including the notable and rare hues, so your tavern's chairs or your library's
  rugs share a consistent palette.

Recoloring is one of the cheapest, highest-impact decorating moves: a matched hue across
furniture, rugs, and banners reads as intentional design.

## Theme ideas

A theme gives a house coherence. A few classics to build toward:

- **Tavern.** Long tables and benches, kegs and bottles raised onto a bar counter, a
  cooking hearth or BBQ add-on, lanterns for warmth, and a chalkboard "menu." Leave open
  floor for gatherings.
- **Library.** Bookshelves (add-on or locked-down books raised onto shelves), reading desks
  with quills and open tomes, globes and maps, a few comfortable chairs, muted rug hues.
- **Mage tower.** Best in a [Tower or Small Stone Tower](/playing/house-types/): a runic
  study with spellbooks, crystal balls, candelabra, alchemy stations, and an observatory
  feel up top. Vertical themes suit the multi-floor tower shells.
- **Museum / trophy hall.** Mounted creature trophies, display cases (secured containers)
  of rare loot, statues, banners of your guild, and good sightlines so visitors can tour.

Match the [house shell](/playing/house-types/) to the theme — a thatched cottage makes a
cozy home, a keep or castle makes a guild hall or museum, a customizable foundation lets
you design the exact floor plan a theme needs.

## Mannequins & house servants

Two special **house NPCs** are decoration in their own right (both `BaseCreature`, invulnerable,
placed in your house and renamable):

- **Mannequin** — a posable dummy you **dress in gear** to **display a suit** in your house.
  Equip it from your pack (it allows the owner to equip/lift), name it, and it shows off a full
  outfit — perfect for a trophy room, a "for sale" display by a vendor, or just showing off a
  rare set. (`Scripts/Mobiles/NPCs/Mannequin/Mannequin.cs`.)
- **Steward** — a house servant NPC you can place, rename, and keep around the house as flavor
  (and light utility); like the mannequin it's invulnerable and redeedable.
  (`Scripts/Services/CleanUpBritannia/Items/Steward.cs`.)

Both are obtained as rewards (e.g. through [Clean Up Britannia](/playing/cleanup-britannia/))
and count as house décor — a living centerpiece rather than a static statue.

## Storage vs. decoration balance

Every decoration is a lockdown you can't spend on stored goods. Decide your house's
**purpose** first:

- A **crafting / storage** house wants most of its budget in secures (containers of
  resources) and minimal decoration.
- A **showpiece** house spends lavishly on locked-down decorations and accepts limited
  storage.
- Most players land in between — a tidy, themed main room plus a back room of secured
  containers for materials.

Bigger houses (see [House Types](/playing/house-types/)) simply give you more of both
budgets, which is the real argument for upgrading your one plot.

## Galleries & inspiration

Do not copy others' screenshots into your own builds blind — but these well-known community
resources are full of ideas, techniques, and tours worth studying. (External links;
descriptions are ours.)

- **[UO Stratics — Housing & Decorating](https://uo.stratics.com/)** — the long-running UO
  fan encyclopedia; its housing and decorating sections cover deco item lists, placement
  guides, and classic technique write-ups.
- **[r/ultimaonline (Reddit)](https://www.reddit.com/r/ultimaonline/)** — the main UO
  subreddit, where players regularly post house tours and "rate my deco" threads with
  candid feedback and how-they-did-it comments.
- **[UOGuide](https://www.uoguide.com/)** — community wiki with articles on housing
  customization, add-ons, and decorating items and their hues.
- **YouTube "UO house tour" / "UO decorating" searches** — many creators post walkthrough
  videos of finished houses; watching the camera pan reveals stacking and raising tricks
  that are hard to convey in text.
- **Official UO / Stratics Discord communities** — active housing and decorating channels
  where decorators trade techniques, share dye hues, and answer placement questions in real
  time.

When a technique you see externally contradicts what this wiki says about *mechanics*
(limits, lockdowns, decay), trust the [Housing](/playing/housing/) page — it is sourced
from this shard's server config — and file a discrepancy report if the wiki is wrong.

## See also

- [Housing](/playing/housing/) — lockdowns, secures, decay, access, the one-house rule
- [House Types](/playing/house-types/) — the shells you decorate, with storage budgets
- [Hue reference](/reference/hues/) — dye colors and notable hues
- [Items & inventory](/playing/items-and-inventory/) — what goes on your shelves
- [Crafting](/playing/crafting/) — making furniture and decorations yourself
