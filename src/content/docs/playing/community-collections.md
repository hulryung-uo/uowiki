---
title: Community Collections
description: Donate gold and items to Britannia's community collections — the Britannian Library, Vesper Museum, and Royal Zoo — to earn points, climb reward tiers, and unlock exclusive statues, artifacts, and titles.
status: source-verified
sources:
  - "servuo: Scripts/Services/CommunityCollections/ (CollectionsSystem, BaseCollectionItem tiers, CollectionDecayTimer)"
  - "servuo: Scripts/Services/CommunityCollections/{MuseumDonationBox,RoyalZooDonationBox}.cs; Scripts/Quests/FriendsOfTheLibrary.cs"
last_verified: 2026-06-17
generated: false
---

**Community collections** are shared, server-wide donation drives. You give gold, resources,
or specific items to a collection's **donation box**, which converts them into **points**; as
the collection's total climbs it unlocks **tiers of rewards** that any contributor can then
buy with their personal points. It's a cooperative, slow-burn way to earn exclusive décor,
gear, and titles.

## The collections

| Collection | Where | Theme |
|---|---|---|
| **Britannian Library** (Friends of the Library) | Britain | Books, knowledge, scholarly décor |
| **Vesper Museum** | Vesper | Rare weapons, jewelry, and replica artifacts |
| **Royal Zoo** | Moonglow | Animals and creature-themed rewards |

## How donating works

1. **Find the collection's donation box** (or the NPC that runs it) and open it.
2. **Donate** what the collection accepts — gold and the specific items that collection wants.
   Each donation is worth a number of **points** (`CollectionItem`).
3. Your contribution adds to the **collection's running total** *and* banks **personal points**
   for you to spend.
4. As the collection total crosses **tier thresholds** (`BaseCollectionItem`, `MaxTier`), new
   **reward items unlock** for everyone — you then spend your personal points to claim them.

## Rewards

Each collection offers its own catalog — typically **decorative statues and statuettes**,
**museum weapons and jewelry** (replica artifacts), library books and quote plaques, and
**special titles** you can wear (`SelectTitleGump`). The higher the tier the collection has
reached, the better the items on offer.

## Watch the decay

Collections **lose points over time** (`CollectionDecayTimer`) — they slowly drain back down,
so tiers aren't permanent and the community has to keep feeding a collection to hold a high
tier. If a reward you want is just above the current tier, a coordinated donation push (or your
own bulk donation) can tip it over before it decays.

## See also

- [Vendors & banking](/playing/vendors-and-banking/) — gold for donations
- [Veteran Rewards](/playing/veteran-rewards/) — the other long-term reward track
- [Decorating](/playing/decorating/) — where collection statues and trophies go
- [Vesper](/world/vesper/) · [Britain](/world/britain/) — collection home cities
