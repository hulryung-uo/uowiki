---
title: Reagents
description: A buyer's overview of the eight magery reagents — what each fuels, which circles consume them most, and where to shop.
status: source-verified
sources:
  - "servuo: Scripts/Spells/First..Eighth (reagent usage counts, surveyed 2026-06-11)"
  - "anima: data/world_knowledge.yaml (mage_shop city features)"
last_verified: 2026-06-11
generated: false
---

A mage's power lives in a shoulder bag of weeds, ash, and spider parts. This is the shopping
guide; per-spell recipes live in the [Magic section](/magic/).

## The eight reagents

Usage counts are how many of the 64 magery spells consume each reagent, surveyed from the
spell sources (`Scripts/Spells/First` through `Eighth`):

| | Reagent | Spells using it | Heaviest circles | Signature spells |
|---|---------|-----------------|------------------|------------------|
| <img src="/img/items/0x0F86.png" class="uo-sprite" alt="" width="56" /> | Mandrake Root | 35 | 4th, 7th, 8th | Recall, Greater Heal, Gate Travel |
| <img src="/img/items/0x0F7B.png" class="uo-sprite" alt="" width="56" /> | Bloodmoss | 27 | 3rd, 8th | Recall, Teleport, the 8th-circle summons |
| <img src="/img/items/0x0F8C.png" class="uo-sprite" alt="" width="56" /> | Sulfurous Ash | 25 | 7th, 4th | Flamestrike, Gate Travel, Fireball line |
| <img src="/img/items/0x0F8D.png" class="uo-sprite" alt="" width="56" /> | Spider's Silk | 22 | 7th, 8th | Heal, Greater Heal, Flamestrike, summons |
| <img src="/img/items/0x0F84.png" class="uo-sprite" alt="" width="56" /> | Garlic | 20 | 4th, 1st–3rd | Heal, Greater Heal, Cure, protection line |
| <img src="/img/items/0x0F7A.png" class="uo-sprite" alt="" width="56" /> | Black Pearl | 17 | 7th, 5th | Recall, Energy Bolt, Gate Travel |
| <img src="/img/items/0x0F88.png" class="uo-sprite" alt="" width="56" /> | Nightshade | 16 | 5th, 2nd | Energy Bolt, curse/poison line |
| <img src="/img/items/0x0F85.png" class="uo-sprite" alt="" width="56" /> | Ginseng | 11 | 1st, 4th | Heal, Greater Heal, Cure |

Buying advice that falls out of the table:

- **Mandrake, bloodmoss, black pearl** — travel magic (Recall/Gate) burns these constantly;
  every mage hoards them.
- **Garlic, ginseng, spider's silk** — the healing set. Support mages empty these first.
- **Sulfurous ash, spider's silk, black pearl, nightshade** — the combat set
  (Flamestrike and Energy Bolt are the workhorse damage spells).

## Where to buy

Mage shops stock all eight. Cities with a mage shop per `world_knowledge.yaml`:

- **[Moonglow](/world/moonglow/)** — the mage city; reagent fields on the island itself
- **[Britain](/world/britain/)** — several mage vendors near the center
- **Nujel'm** — mage shop in the palace city
- **Papua** — the Lost Lands stop for reagents
- **Wind** — mages-only hidden city (you can already cast if you can enter)

Find exact vendor doorsteps on the [interactive map](https://uomap.vercel.app) (toggle NPC
Vendors and search "Mage"). Vendor stock refreshes every 60 minutes and prices respond to
bulk buying (`Config/Vendors.cfg` — see [server rules](/shard/server-rules/)), so reagent
runs across two or three cities beat hammering one vendor.

## Notes

- Necromancy uses a separate reagent set (bat wings, grave dust, etc.) — documented with the
  [Magic](/magic/) section.
- Reagent costs per spell rise with circle; an 8th-circle summon can eat four reagent types
  in one cast. Stock in hundreds, not dozens.

## Related

- [Magery](/skills/magery/) — circles, cast chances, mana
- [Magic](/magic/) — per-spell reagent recipes
