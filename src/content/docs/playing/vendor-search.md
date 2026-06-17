---
title: Vendor Search
description: Search every player vendor on the shard for the item you want, then get a map straight to it — the shard-wide shopping tool.
status: source-verified
sources:
  - "servuo: Scripts/Services/Vendor Searching/VendorSearch.cs (CanSearch, criteria matching)"
  - "servuo: Scripts/Services/Vendor Searching/{VendorSearchGump,VendorSearchMap,VendorSearchCriteria}.cs"
last_verified: 2026-06-17
generated: false
---

**Vendor Search** lets you scour **every player vendor on the shard** for an item from one
menu, instead of hopping between houses hoping to find it. It's the single biggest
quality-of-life tool for shopping.

## How to search

Open the **vendor search** menu (from the context menu / help options where the system makes
it available — you must be somewhere you can safely search, roughly at a **bank or secure
location**; `VendorSearch.CanSearch` blocks searching while you're in a logout-delay state).
Then set your **criteria** (`VendorSearchCriteria`):

- **Item name / type**, and
- filters like **price range**, item properties, and race restrictions (gargoyle/elf items).

The search returns matching items currently for sale on player vendors **across the shard**,
with their **prices and the vendor's location**.

## Getting there

Pick a result and you receive a **vendor search map** (`VendorSearchMap`) — a map item marked
with the vendor's location. Use it to travel to that vendor and buy the item directly. The map
becomes inactive once that item is no longer for sale.

## Notes

- It searches **player vendors only** — not NPC shops (for those, just visit the relevant
  NPC; see [Vendors & banking](/playing/vendors-and-banking/)).
- Great for hunting **specific crafted gear, rare décor, and runic-made items** that only
  players sell.

## See also

- [Vendors & banking](/playing/vendors-and-banking/) — buying, selling, and player vendors
- [Housing](/playing/housing/) — running your own player vendor
- [Movement & travel](/playing/movement-and-travel/) — getting to the vendor on the map
