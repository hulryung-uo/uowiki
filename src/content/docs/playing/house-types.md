---
title: House Types
description: Every house you can place on this shard — the classic pre-built deeds (small stone house through castle) and the customizable foundation plots (7x7 up to 18x18, plus keep/castle), with footprint, lockdown and secure storage, and gold cost for each.
status: source-verified
sources:
  - "servuo: Scripts/Multis/Deeds.cs (deed classes, MultiID, LabelNumber, GetHouse)"
  - "servuo: Scripts/Multis/Houses.cs (BaseHouse subclass footprint + MaxSecure)"
  - "servuo: Scripts/Multis/HousePlacementTool.cs (HousePlacementEntry storage/lockdowns/cost)"
  - "servuo: Scripts/VendorInfo/SBHouseDeed.cs (NPC deed prices)"
  - "servuo: Config/Housing.cfg (AccountHouseLimit=1), Config/Expansion.cfg (EJ)"
  - "client: multi.mul / multi.idx (exterior renders, via tools/render_house.py)"
last_verified: 2026-06-11
generated: false
---

This is the catalogue of houses you can own on this shard: what each one looks like, how
big its plot is, how much it stores, and what it costs. Before you buy, read
[Housing](/playing/housing/) for *how* placement, lockdowns, decay, and access actually
work — this page is the **menu**, that page is the **manual**.

Shard rule that frames every choice below: **one house per account**
(`AccountHouseLimit=1`, `Config/Housing.cfg`; see [server rules](/shard/server-rules/)).
You get exactly one plot, so pick deliberately. Shard expansion is **EJ** (`Config/Expansion.cfg`).

## Two ways to get a house

There are two distinct families of house, chosen from two different sources:

- **Classic (pre-set) houses** — a fixed design baked into a single *multi* (walls, roof,
  doors all placed for you). You place them from a **house deed** bought from an
  architect / real-estate NPC, or via the **Classic Houses** tab of the
  [House Placement Tool](/playing/housing/#placing-a-house). What you see is what you get:
  the layout cannot be redesigned (though you can still decorate — see
  [Decorating](/playing/decorating/)).
- **Customizable foundations** — an empty multi-story foundation you place from the
  **2-Story** / **3-Story Customizable Houses** tab of the House Placement Tool, then
  **design yourself** in customization mode (walls, floors, doors, stairs, roofing). You
  pick the plot footprint up front; the interior is a blank slate.

### Storage numbers, explained

Two limits govern how much a house holds (both detailed on [Housing](/playing/housing/)):

- **Lockdowns** — individual items pinned in place.
- **Secures** — for classic houses this is the **number of secured containers** you may
  designate; for customizable foundations the placement tool instead quotes a total
  **secure-storage** budget (a much larger number, e.g. 425 for the smallest plot).

The base values are listed below **straight from the source**. In-game, totals are scaled
by `BaseHouse.GlobalBonusStorageScalar` — **×1.4 on this EJ shard** (`Core.SA`). The
number in parentheses is that scaled in-game figure, e.g. a small house's `212` lockdowns
becomes **296** in practice.

## Classic houses

Pre-built, fixed-layout houses. **Footprint** is the plot's bounding box in tiles;
**Lockdowns** and **Secures** show *base (×1.4 in-game)*; **Cost** is the gold withdrawn
on placement via the House Placement Tool; **Deed** is the NPC architect's sell price for
the equivalent deed (— = not sold individually by the deed vendor).

| Exterior | House | Footprint | Lockdowns | Secures | Cost (gp) | Deed (gp) |
|----------|-------|-----------|-----------|---------|-----------|-----------|
| ![Stone and plaster house](/img/houses/0x64.png) | Stone and plaster house | 7x7 | 212 (296) | 3 (4) | 36,750 | 43,800 |
| ![Field stone house](/img/houses/0x66.png) | Field stone house | 7x7 | 212 (296) | 3 (4) | 36,750 | 43,800 |
| ![Small brick house](/img/houses/0x68.png) | Small brick house | 7x7 | 212 (296) | 3 (4) | 36,500 | 43,800 |
| ![Wooden house](/img/houses/0x6A.png) | Wooden house | 7x7 | 212 (296) | 3 (4) | 35,000 | 43,800 |
| ![Wood and plaster house](/img/houses/0x6C.png) | Wood and plaster house | 7x7 | 212 (296) | 3 (4) | 36,500 | 43,800 |
| ![Thatched-roof cottage](/img/houses/0x6E.png) | Thatched-roof cottage | 7x7 | 212 (296) | 3 (4) | 36,500 | 43,800 |
| ![Small stone workshop](/img/houses/0xA0.png) | Small stone workshop | 7x7 | 212 (296) | 3 (4) | 50,250 | 60,600 |
| ![Small marble workshop](/img/houses/0xA2.png) | Small marble workshop | 7x7 | 212 (296) | 3 (4) | 52,250 | 63,000 |
| ![Small stone tower](/img/houses/0x98.png) | Small stone tower | 8x8 | 290 (406) | 4 (5) | 73,250 | 88,500 |
| ![Two-story villa](/img/houses/0x9E.png) | Two-story villa | 11x12 | 550 (770) | 8 (11) | 113,500 | 136,500 |
| ![Sandstone house with patio](/img/houses/0x9C.png) | Sandstone house with patio | 12x9 | 425 (595) | 6 (8) | 76,250 | 90,900 |
| ![Two-story log cabin](/img/houses/0x9A.png) | Two-story log cabin | 8x13 | 550 (770) | 8 (11) | 81,250 | 97,800 |
| ![Brick house](/img/houses/0x74.png) | Brick (guild) house | 14x14 | 685 (958) | 8 (11) | 131,250 | 144,500 |
| ![Two-story wood and plaster house](/img/houses/0x76.png) | Two-story wood and plaster house | 14x14 | 685 (958) | 10 (14) | 162,500 | 192,400 |
| ![Two-story stone and plaster house](/img/houses/0x78.png) | Two-story stone and plaster house | 14x14 | 685 (958) | 10 (14) | 162,750 | — |
| ![Large house with patio](/img/houses/0x8C.png) | Large house with patio | 15x14 | 685 (958) | 8 (11) | 129,000 | 152,800 |
| ![Marble house with patio](/img/houses/0x96.png) | Marble house with patio | 15x14 | 685 (958) | 10 (14) | 160,250 | 192,000 |
| ![Tower](/img/houses/0x7A.png) | Tower | 24x16 | 1,059 (1,482) | 15 (21) | 366,250 | 433,200 |
| ![Small stone keep](/img/houses/0x7C.png) | Small stone keep | 24x24 | 1,312 (1,836) | 18 (25) | 562,500 | 665,200 |
| ![Castle](/img/houses/0x7E.png) | Castle | 31x31 | 2,038 (2,853) | 28 (39) | 865,000 | 1,022,800 |

The six smallest houses (stone-and-plaster through thatched cottage) are mechanically
identical 7x7 cottages — only the **art** differs, so pick by looks and budget. Footprints
above are the structure's plot; the small houses also project a one-tile entry step, which
is why the placement preview reads slightly taller than 7x7.

## Customizable foundations

Empty foundations you design yourself — see **[Customizing Your House](/playing/house-customization/)**
for the full design-mode walkthrough (tools, stories, commit/revert, and the gold it costs).
You choose the footprint when you place it; the table is large (over 100 sizes), so the
ranges below summarise each category. Storage and lockdowns scale with plot size; **Cost** is
the placement gold. (As above, in-game lockdown/secure totals are **×1.4**.)

| Category | Plot sizes | Lockdowns (base) | Secure storage (base) | Cost range (gp) |
|----------|-----------|------------------|------------------------|-----------------|
| **2-Story Customizable** | 7x7 up to 13x13 (47 sizes) | 212 – 650 | 425 – 1,300 | 33,000 – 102,000 |
| **3-Story Customizable** | 9x14 up to 18x18 (55 sizes) | 575 – 1,059 | 1,150 – 2,119 | 77,000 – 187,000 |
| **Custom Keep / Castle** | 23x23 keep, 32x32 castle (2 sizes) | 1,312 / 2,038 | 2,625 / 4,076 | 525,000 each |

Representative footprints and their numbers:

| Foundation | Lockdowns | Secure storage | Cost (gp) |
|------------|-----------|----------------|-----------|
| 7x7 2-Story (smallest) | 212 | 425 | 33,000 |
| 10x10 2-Story | 425 | 850 | 63,000 |
| 13x13 2-Story | 650 | 1,300 | 102,000 |
| 14x14 3-Story | 685 | 1,370 | 117,000 |
| 18x18 3-Story (largest standard) | 1,059 | 2,119 | 187,000 |
| 23x23 Customizable Keep | 1,312 | 2,625 | 525,000 |
| 32x32 Customizable Castle | 2,038 | 4,076 | 525,000 |

The full 104-size table lives in `data/houses.json` (`foundations`); the placement tool
shows every size with its exact storage and cost when you open the 2-Story / 3-Story tabs.

## Choosing: the tradeoffs

- **Cheap and small vs. large and dear.** A 7x7 cottage is ~35,000 gp and stores ~296
  items; a castle is over a million gold and holds ~2,850 lockdowns plus dozens of secure
  containers. Storage scales roughly with price — you are buying *space*.
- **Classic (fixed) vs. customizable.** Classic houses give you a finished, characterful
  building (a real tower, a real keep) for slightly less gold and zero design effort, but
  the walls are where they are forever. Foundations cost a touch more and start as an empty
  shell, but you control **every wall, floor, door, and roof** — ideal if you want a
  specific layout, a shop floor, or a themed build (see [Decorating](/playing/decorating/)).
- **Footprint is the real constraint.** Open land for large plots is scarce. A modest
  customizable foundation you can actually *place* beats a castle you can never fit. Scout
  the [world](/playing/world-and-time/) for room before committing your one slot.
- **Secures vs. lockdowns.** Lockdowns hold loose items (decorations, tools); secures hold
  *containers* of items. Crafters and hoarders should weigh a house's secure capacity, not
  just its lockdown count.

## See also

- [Housing](/playing/housing/) — placement, customization, lockdowns/secures, decay, keys,
  co-owners, player vendors, and the one-house rule in full
- [Decorating](/playing/decorating/) — turning a house shell into a home
- [Vendors & banking](/playing/vendors-and-banking/) — funding the deed and running a shop
- [Server rules](/shard/server-rules/) — the housing config in context
- [World & time](/playing/world-and-time/) — where you can place a plot
