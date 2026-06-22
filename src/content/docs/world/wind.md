---
title: Wind
description: The hidden city of mages, sealed beneath the mountains and open only to those skilled in Magery.
status: source-verified
sources:
  - "anima: data/map_pois.json (city: Wind)"
  - "anima: data/world_knowledge.yaml (cities.wind)"
  - "servuo: Data/Regions.xml (TownRegion \"Wind\", go 5223,190, rects x~5132-5366 y~3-204; present on both Felucca and Trammel facets)"
  - "servuo: Scripts/Regions/TownRegion.cs (TownRegion : GuardedRegion — Wind is a guarded town region, not a dungeon region)"
  - "servuo: Scripts/Items/Functional/PublicMoongate.cs (no Wind public-gate entry)"
  - "reference: uo.com cities & towns"
last_verified: 2026-06-22
generated: false
---

Wind is Britannia's best-kept secret — a hidden city of mages, sealed away beneath the
mountains and barred to all but the magically gifted. There is no road in. The only entrance is
a **teleporter** that turns away anyone whose [Magery](/skills/magery/) is not high enough
(traditionally **70.0 or above**), so the city is, by design, a sanctuary for spellcasters and
scholars. Inside, Wind is hushed and arcane: a place of mage shops and libraries with none of
the bustle of the surface towns. To most adventurers it is a rumor; to a trained mage, it is a
private retreat few outsiders will ever see.

[Open the Wind area in the interactive map →](https://uomap.vercel.app/?facet=felucca&x=1361&y=895&z=2)

## Getting there

- **Surface entrance (lore):** the hidden entrance is traditionally placed in the mountains of
  north-central Britannia, near (1361, 895). This entrance coordinate is OSI lore and is **not**
  confirmed against our shard's source.
- **City region location (verified):** the Wind town region itself sits in the Lost Lands /
  dungeon coordinate block of the map, roughly (5132–5366, 3–204), with its region travel point
  at (5223, 190). On our shard Wind is a **guarded `TownRegion`** (not a dungeon region) and
  exists on both the Felucca and Trammel facets (`Data/Regions.xml`).
- **No public moongate.** Wind has no public-moongate destination
  (`Scripts/Items/Functional/PublicMoongate.cs`). Access is by the hidden teleporter described
  below.
- **Magery-gated teleporter (lore).** Classic UO requires finding a hidden teleporter that
  enforces a **Magery requirement** (about 70.0 skill). The teleporter location and exact
  threshold are **not** confirmed against our shard's source. See [Magery](/skills/magery/).

:::note[What is verified vs. lore]
**Verified from ServUO source:** Wind is a guarded `TownRegion` (not a dungeon region) on both
Felucca and Trammel, located in the Lost Lands coordinate block around (5132–5366, 3–204), and
it has no public moongate. **Still lore / unverified:** the surface-entrance coordinate
(1361, 895) and the 70.0 Magery entry requirement — the hidden teleporter is placed via
decoration/teleporter data and was not located in source during this pass, so treat the
threshold and entrance as a guideline until confirmed in-game.
:::

## Services

Wind has no mainstream marketplace; its trades serve the magical arts. Per lore
([what the icons mean](/world/town-services/)):

<img src="/img/services/mage.gif" alt="Mage shop" width="28" /> Mage shop ·
<img src="/img/services/eye.gif" alt="Scribe / library" width="28" /> Scribe / library ·
<img src="/img/services/reagents.gif" alt="Reagents" width="28" /> Reagents

No NPC vendor spawns are recorded at Wind's surface coordinates in our map data, since the
inhabited city sits behind the teleporter — so this list is described from lore rather than
matched to spawn data, and is **unverified** for our shard.

## Nearby

- The **mountains** that conceal Wind also riddle the surrounding area with
  [mining](/skills/mining/) spots and cave systems.
- The hidden, members-only nature of the city is its defining feature — there is little to
  "pass through" here, only a destination for those who qualify.

## Related

- [Mage](/professions/mage/) · [Magery](/skills/magery/) — the skill that unlocks the door
- [Town services legend](/world/town-services/) · [Items: reagents](/items/reagents/)
- [World overview](/world/) · [Moongates and shrines](/world/moongates-and-shrines/)
