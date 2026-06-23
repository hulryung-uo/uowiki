---
title: Wind
description: The hidden city of mages, sealed beneath the mountains and reached through a concealed mountain passage.
status: source-verified
sources:
  - "anima: data/map_pois.json (city: Wind)"
  - "anima: data/world_knowledge.yaml (cities.wind)"
  - "servuo: Data/Regions.xml (TownRegion \"Wind\", go 5223,190, rects x~5132-5366 y~3-204; present on both Felucca and Trammel facets)"
  - "servuo: Scripts/Regions/TownRegion.cs (TownRegion : GuardedRegion — Wind is a guarded town region, not a dungeon region)"
  - "servuo: Scripts/Items/Functional/PublicMoongate.cs (no Wind public-gate entry)"
  - "servuo: Data/teleporters.csv (Wind passage teleporter 5191,152 <-> surface 1367,891 on Felucca & Trammel — a plain Teleporter, no skill column / no Magery gate)"
  - "servuo: Scripts/Commands/GenTeleporter.cs (no SkillTeleporter placement for Wind)"
  - "reference: uo.com cities & towns (classic Magery-70 entry — OSI lore, not implemented on our shard)"
last_verified: 2026-06-22
generated: false
---

Wind is Britannia's best-kept secret — a hidden city of mages, sealed away beneath the
mountains. There is no road in; the only way through is a concealed **teleporter** in the
mountain passage. In classic UO lore that teleporter turned away anyone whose
[Magery](/skills/magery/) was not high enough (traditionally **70.0 or above**), making the
city a sanctuary for spellcasters — but **on our shard the passage teleporter has no skill
requirement** (it is a plain teleporter; see below). Inside, Wind is hushed and arcane: a place
of mage shops and libraries with none of the bustle of the surface towns. To most adventurers
it is a rumor; to those who know the way, a private retreat few outsiders will ever see.

[Open the Wind area in the interactive map →](https://uomap.vercel.app/?facet=felucca&x=1367&y=891&z=0)

## Getting there

- **Surface entrance (verified):** the passage teleporter drops you on the surface at
  **(1367, 891)** in the mountains of north-central Britannia, on both Felucca and Trammel
  (`Data/teleporters.csv`). (Classic OSI lore cites ≈(1361, 895) — essentially the same spot.)
- **City region location (verified):** the Wind town region itself sits in the Lost Lands /
  dungeon coordinate block of the map, roughly (5132–5366, 3–204), with its region travel point
  at (5223, 190). On our shard Wind is a **guarded `TownRegion`** (not a dungeon region) and
  exists on both the Felucca and Trammel facets (`Data/Regions.xml`). The in-city end of the
  passage teleporter is at (5191, 152).
- **No public moongate.** Wind has no public-moongate destination
  (`Scripts/Items/Functional/PublicMoongate.cs`). Access is by the passage teleporter.
- **No Magery gate on our shard.** The passage teleporter (5191,152 ↔ 1367,891) is a **plain
  `Teleporter`** — `Data/teleporters.csv` has no skill column and `Scripts/Commands/GenTeleporter.cs`
  places **no `SkillTeleporter`** for Wind. The classic **Magery ≈70.0** entry requirement is
  **OSI lore and is not implemented here** — anyone can walk through. See [Magery](/skills/magery/).

:::note[What is verified vs. lore]
**Verified from ServUO source:** Wind is a guarded `TownRegion` (not a dungeon region) on both
Felucca and Trammel, located in the Lost Lands coordinate block around (5132–5366, 3–204); it
has no public moongate; and it is reached by a **plain** passage teleporter linking (5191, 152)
inside to **(1367, 891)** on the surface — with **no skill requirement**. **Lore only:** the
classic **70.0 Magery** entry gate — that requirement is not present in our shard's data.
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

- [Mage](/professions/mage/) · [Magery](/skills/magery/) — the city's theme (no longer an entry gate on our shard)
- [Town services legend](/world/town-services/) · [Items: reagents](/items/reagents/)
- [World overview](/world/) · [Moongates and shrines](/world/moongates-and-shrines/)
