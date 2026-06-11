---
title: Dungeons
description: Every mapped dungeon with its location, features, and the monsters that actually spawn there on this shard.
status: source-verified
sources:
  - "servuo: Spawns/*.xml (felucca, trammel, ilshenar, malas, tokuno, termur — spawn lists)"
  - "uomap: js/data.js (dungeon POI coordinates)"
  - "client map art (per-dungeon crops)"
last_verified: 2026-06-12
generated: false
---

Where the loot is, the teeth are. The **location coordinates** below come from the
[interactive map's](https://uomap.vercel.app) POI data; the **monster lists** in each
section are extracted directly from this shard's spawn files
(`../servuo/Spawns/*.xml`, via `tools/extract_dungeon_spawns.py` →
[`data/dungeon_spawns.json`](https://github.com/)) — so they reflect what *actually*
spawns here, not era lore. Where this shard runs the revamped version of a classic
dungeon (Despise, Wrong), the spawn reflects that.

New to delving? Read [Combat Basics](/playing/combat-basics/) and
[Treasure Hunting](/playing/treasure-hunting/) first, and skim the
[Bestiary](/bestiary/) for what you're about to meet. Most dungeons exist on both
**Felucca** and **Trammel** with identical spawns — but in Felucca they're also
[open PvP zones with better loot](/shard/server-rules/).

![Map of Felucca dungeon locations](/img/maps/felucca-dungeons.png)

## Quick reference

### Felucca / Trammel

| Dungeon | Location (x, y) | Map | Danger summary |
|---------|-----------------|-----|----------------|
| [Despise](#despise) | [(1301, 1090)](https://uomap.vercel.app/?facet=felucca&x=1301&y=1090&z=2) | [<img src="/img/maps/dungeon-despise.png" alt="Despise location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=1301&y=1090&z=2) | A fair first dungeon, now revamped with a Good/Evil split. |
| [Orc Cave](#orc-cave) | [(1017, 1430)](https://uomap.vercel.app/?facet=felucca&x=1017&y=1430&z=2) | [<img src="/img/maps/dungeon-orc-cave.png" alt="Orc Cave location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=1017&y=1430&z=2) | Orc clans; manageable for new fighters. |
| [Covetous](#covetous) | [(2498, 921)](https://uomap.vercel.app/?facet=felucca&x=2498&y=921&z=2) | [<img src="/img/maps/dungeon-covetous.png" alt="Covetous location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=2498&y=921&z=2) | Multi-level: harpies and gazers up top, undead below. |
| [Deceit](#deceit) | [(4111, 434)](https://uomap.vercel.app/?facet=felucca&x=4111&y=434&z=2) | [<img src="/img/maps/dungeon-deceit.png" alt="Deceit location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=4111&y=434&z=2) | Undead-infested island dungeon — bring spirit and silver. |
| [Shame](#shame) | [(511, 1565)](https://uomap.vercel.app/?facet=felucca&x=511&y=1565&z=2) | [<img src="/img/maps/dungeon-shame.png" alt="Shame location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=511&y=1565&z=2) | The classic elemental dungeon. |
| [Wrong](#wrong) | [(2043, 238)](https://uomap.vercel.app/?facet=felucca&x=2043&y=238&z=2) | [<img src="/img/maps/dungeon-wrong.png" alt="Wrong location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=2043&y=238&z=2) | The old prison; this shard fills it with Juka and golems. |
| [Destard](#destard) | [(1176, 2637)](https://uomap.vercel.app/?facet=felucca&x=1176&y=2637&z=2) | [<img src="/img/maps/dungeon-destard.png" alt="Destard location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=1176&y=2637&z=2) | Dragon-infested. Not a place to wander into by accident. |
| [Hythloth](#hythloth) | [(4721, 3822)](https://uomap.vercel.app/?facet=felucca&x=4721&y=3822&z=2) | [<img src="/img/maps/dungeon-hythloth.png" alt="Hythloth location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=4721&y=3822&z=2) | Volcanic depths: daemons and balrons. End-game territory. |
| [Fire](#fire-dungeon) | [(2923, 3409)](https://uomap.vercel.app/?facet=felucca&x=2923&y=3409&z=2) | [<img src="/img/maps/dungeon-fire-dungeon.png" alt="Fire Dungeon location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=2923&y=3409&z=2) | Lava caverns of fire elementals, efreet and lava lizards. |
| [Ice](#ice-dungeon) | [(1999, 81)](https://uomap.vercel.app/?facet=felucca&x=1999&y=81&z=2) | [<img src="/img/maps/dungeon-ice-dungeon.png" alt="Ice Dungeon location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=1999&y=81&z=2) | Frozen warren of ice elementals, frost trolls and ratmen. |
| [Khaldun](#khaldun) | [(5571, 1320)](https://uomap.vercel.app/?facet=felucca&x=5571&y=1320&z=2) | [<img src="/img/maps/dungeon-khaldun.png" alt="Khaldun location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=5571&y=1320&z=2) | Ancient Lost Lands tomb; cursed undead and zealots. |
| [Painted Caves](#painted-caves) | [(5765, 2622)](https://uomap.vercel.app/?facet=felucca&x=5765&y=2622&z=2) | [<img src="/img/maps/dungeon-painted-caves.png" alt="Painted Caves location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=5765&y=2622&z=2) | Lost Lands cave system; troglodytes and savages. |
| [Terathan Keep](#terathan-keep) | [(5451, 3143)](https://uomap.vercel.app/?facet=felucca&x=5451&y=3143&z=2) | [<img src="/img/maps/dungeon-terathan-keep.png" alt="Terathan Keep location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=5451&y=3143&z=2) | Terathan vs Ophidian war-fortress in the Lost Lands. |
| [Blighted Grove](#blighted-grove) | [(587, 1641)](https://uomap.vercel.app/?facet=felucca&x=587&y=1641&z=2) | [<img src="/img/maps/dungeon-blighted-grove.png" alt="Blighted Grove location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=587&y=1641&z=2) | Corrupted swamp grove (ML); home of the Corgul-era growths. |
| [Prism of Light](#prism-of-light) | [(3785, 1090)](https://uomap.vercel.app/?facet=felucca&x=3785&y=1090&z=2) | [<img src="/img/maps/dungeon-prism-of-light.png" alt="Prism of Light location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=3785&y=1090&z=2) | Crystal dungeon (ML); wisps, vortices and crystal beasts. |
| [Palace of Paroxysmus](#palace-of-paroxysmus) | [(6166, 1180)](https://uomap.vercel.app/?facet=felucca&x=6166&y=1180&z=2) | — | Acid-drenched lair of the Slasher of Veils' kin (SA). |
| Ankh Dungeon | [(710, 1362)](https://uomap.vercel.app/?facet=felucca&x=710&y=1362&z=2) | [<img src="/img/maps/dungeon-ankh-dungeon.png" alt="Ankh Dungeon location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=710&y=1362&z=2) | Small dungeon near the Ankh. |
| [Wisp Dungeon](#wisp-dungeon) | [(652, 1298)](https://uomap.vercel.app/?facet=felucca&x=652&y=1298&z=2) | [<img src="/img/maps/dungeon-wisp-dungeon.png" alt="Wisp Dungeon location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=652&y=1298&z=2) | Wisp-haunted caverns with balrons and high undead. |
| [Solen Hive](#solen-hive) | [(2607, 763)](https://uomap.vercel.app/?facet=felucca&x=2607&y=763&z=2) | [<img src="/img/maps/dungeon-solen-hive.png" alt="Solen Hive location" width="160" />](https://uomap.vercel.app/?facet=felucca&x=2607&y=763&z=2) | Underground ant hive of the Solen. |

### Ilshenar

| Dungeon | Location | Danger summary |
|---------|----------|----------------|
| [Sorcerer's Dungeon](#sorcerers-dungeon) | (548, 455) | Dark hideout of liches, gargoyles and elementals. |
| [Spectre Dungeon](#spectre-dungeon) | (1363, 1034) | Haunted; spectres, wraiths and shades. |
| [Exodus Dungeon](#exodus-dungeon) | (852, 776) | Stronghold of the mechanical overlord Exodus. |
| [Spider Cave](#spider-cave) | (1222, 1512) | Cramped ratman-and-undead crawl. |
| Blood Dungeon | (2112, 899) | Blood-elemental sink (see spawn data). |
| Rock Dungeon | (2161, 119) | Earth-themed Ilshenar cave (see spawn data). |
| Ankh Dungeon | (475, 755) | Mixed undead and gargoyles beneath the great Ankh. |

### Malas

| Dungeon | Location | Danger summary |
|---------|----------|----------------|
| [Doom (The Gauntlet)](#doom-the-gauntlet) | (2368, 1584) | The Dark Father's realm — the hardest non-SA dungeon. |
| [Bedlam](#bedlam) | (2067, 1371) | Necromancer asylum (ML); named undead and gore fiends. |
| [Labyrinth](#labyrinth) | (1732, 975) | Minotaur maze (ML) with air-elemental tempests. |

### Tokuno

| Dungeon | Location | Danger summary |
|---------|----------|----------------|
| [Fan Dancer's Dojo](#fan-dancers-dojo) | (970, 222) | Demon-overrun dojo; fan dancers and oni. |
| [Yomotsu Mines](#yomotsu-mines) | (258, 786) | Mines of the Yomotsu warriors and priests. |
| [The Citadel](#the-citadel) | (1345, 768) | Fortress of the Black Order ninja clans. |

---

## Despise

Just north of Britain, Despise has always been the dungeon new adventurers are pointed
toward first. On this shard it runs the **revamped Despise**: the entrance splits into a
**Good (light)** wing and an **Evil (dark)** wing, each with its own themed spawn and a
champion-style boss at the bottom, so the easy reputation is a little misleading these days.

- **Map:** ![Despise location](/img/maps/dungeon-despise.png)
- **Features:** Good/Evil branching layout; faction-flavored creatures (fairies, nymphs and unicorns on the light side; corrupt beasts on the dark side); a boss encounter per wing.
- **Monsters found here:** [Lizardman](/bestiary/humanoids/lizardman/), [Ettin](/bestiary/humanoids/ettin/), **BirlingBlades**, **Darkmane**, **Dendrite**, **DespiseUnicorn**, **DivineGuardian**, **Echidnite**, **Fairy**, **ForestNymph**, **Hellion**, **Naba**, **Phantom**, **Prometheoid**, plus 9 more revamped beasts. *(Bolded names are custom revamped-Despise creatures not yet in the bestiary.)*

## Orc Cave

A shallow warren west of Despise, packed with an orc clan. Low ceilings, lots of bodies,
and a steady drip of loot make it a popular grind for new melee and archer characters.

- **Map:** ![Orc Cave location](/img/maps/dungeon-orc-cave.png)
- **Features:** Single-level cave; dense, fast-respawning orc spawn; close to Britain for easy banking.
- **Monsters found here:** [Orc](/bestiary/humanoids/orc/), [Orcish Lord](/bestiary/humanoids/orcish-lord/), [Orc Bomber](/bestiary/humanoids/orc-bomber/), [Orc Captain](/bestiary/humanoids/orc-captain/), [Dire Wolf](/bestiary/monsters/dire-wolf/), [Earth Elemental](/bestiary/elementals/earth-elemental/), [Orcish Mage](/bestiary/humanoids/orcish-mage/), [Giant Rat](/bestiary/monsters/giant-rat/), [Corpser](/bestiary/monsters/corpser/), [Orc Brute](/bestiary/humanoids/orc-brute/).

## Covetous

A deep, multi-level dungeon east of Britain. The upper halls hold harpies, gazers and
corpsers; descend and the spawn turns to undead — skeletons, liches and bone knights —
making it a natural step up from the Orc Cave.

- **Map:** ![Covetous location](/img/maps/dungeon-covetous.png)
- **Features:** Several descending levels of rising difficulty; a champion spawn at the lowest level. Good for [treasure-map](/playing/treasure-hunting/) digging in the surrounding levels.
- **Monsters found here:** [Skeleton](/bestiary/undead/skeleton/), [Corpser](/bestiary/monsters/corpser/), [Harpy](/bestiary/monsters/harpy/), [Gazer](/bestiary/monsters/gazer/), [Zombie](/bestiary/undead/zombie/), [Headless One](/bestiary/humanoids/headless-one/), [Bone Knight](/bestiary/undead/bone-knight/), [Lich](/bestiary/undead/lich/), [Gazer Larva](/bestiary/monsters/gazer-larva/), [Shade](/bestiary/undead/shade/), [Spectre](/bestiary/undead/spectre/), [Slime](/bestiary/monsters/slime/), [Giant Spider](/bestiary/monsters/giant-spider/), [Dread Spider](/bestiary/monsters/dread-spider/), plus 10 more.

## Deceit

An undead-choked dungeon on an island off the northeast coast. Nearly everything here is
a walking corpse, so come prepared with consecrate/silver weapons or [Necromancy](/professions/)
of your own. Liches and lich lords near the bottom drop the best loot.

- **Map:** ![Deceit location](/img/maps/dungeon-deceit.png)
- **Features:** Multi-level undead dungeon; a champion spawn at the deepest point; reachable by boat or recall.
- **Monsters found here:** [Skeleton](/bestiary/undead/skeleton/), [Ghoul](/bestiary/undead/ghoul/), [Lich](/bestiary/undead/lich/), [Zombie](/bestiary/undead/zombie/), [Wraith](/bestiary/undead/wraith/), [Mummy](/bestiary/undead/mummy/), [Shade](/bestiary/undead/shade/), [Spectre](/bestiary/undead/spectre/), [Bone Knight](/bestiary/undead/bone-knight/), [Skeletal Knight](/bestiary/undead/skeletal-knight/), [Bone Mage](/bestiary/undead/bone-magi/), [Silver Serpent](/bestiary/monsters/silver-serpent/), [Fire Elemental](/bestiary/elementals/fire-elemental/), [Poison Elemental](/bestiary/elementals/poison-elemental/), plus 3 more (incl. [Lich Lord](/bestiary/undead/lich-lord/) and [Ancient Lich](/bestiary/undead/ancient-lich/)).

## Shame

The archetypal **elemental dungeon**, south of Britain. Earth, air, fire and water
elementals abound, alongside evil mages — a long-time favorite for mages farming
reagents, scrolls and elemental loot. Blood elementals near the bottom are the prize.

- **Map:** ![Shame location](/img/maps/dungeon-shame.png)
- **Features:** Large multi-level layout with by far the most spawn points of any classic dungeon on this shard; a champion spawn; water sections with sea serpents and a kraken.
- **Monsters found here:** [Earth Elemental](/bestiary/elementals/earth-elemental/), [Scorpion](/bestiary/monsters/scorpion/), [Air Elemental](/bestiary/elementals/air-elemental/), [Dull Copper Elemental](/bestiary/elementals/dull-copper-elemental/), [Fire Elemental](/bestiary/elementals/fire-elemental/), [Water Elemental](/bestiary/elementals/water-elemental/), [Evil Mage](/bestiary/humanoids/evil-mage/), [Evil Mage Lord](/bestiary/humanoids/evil-mage-lord/), [Blood Elemental](/bestiary/elementals/blood-elemental/), [Sea Serpent](/bestiary/sea/sea-serpent/), [Kraken](/bestiary/sea/kraken/), [Poison Elemental](/bestiary/elementals/poison-elemental/), [Elder Gazer](/bestiary/monsters/elder-gazer/), [Acid Elemental](/bestiary/elementals/toxic-elemental/).

## Wrong

Classic Wrong was a prison dungeon of orcs and trolls. **On this shard the spawn is
rebuilt around the Juka** — the crystalline warrior-race — backed by brigands and golems,
so it plays as a tougher, more magical fight than its old reputation suggests.

- **Map:** ![Wrong location](/img/maps/dungeon-wrong.png)
- **Features:** Compact cell-block layout; Juka lords and mages hit hard for a mid-tier dungeon; golem controllers summon reinforcements.
- **Monsters found here:** [Juka Warrior](/bestiary/humanoids/juka-warrior/), [Juka Lord](/bestiary/humanoids/juka-lord/), [Juka Mage](/bestiary/humanoids/juka-mage/), [Brigand](/bestiary/humanoids/brigand/), [Golem](/bestiary/monsters/golem/), [Golem Controller](/bestiary/humanoids/golem-controller/).

## Destard

The dragon dungeon, southwest of Britain. Drakes and wyverns guard the upper levels;
deeper in you'll meet dragons, ancient wyrms and a shadow wyrm. Strictly for well-equipped
parties — soloing it is a tall order.

- **Map:** ![Destard location](/img/maps/dungeon-destard.png)
- **Features:** Two main levels (the lower reserved for the heaviest dracs); a champion spawn; superb scaled/hide and gem loot.
- **Monsters found here:** [Drake](/bestiary/monsters/drake/), [Wyvern](/bestiary/monsters/wyvern/), [Giant Serpent](/bestiary/monsters/giant-serpent/), [Water Elemental](/bestiary/elementals/water-elemental/), [Dragon](/bestiary/monsters/dragon/), [Daemon](/bestiary/monsters/daemon/), [Shadow Wyrm](/bestiary/monsters/shadow-wyrm/), [Ancient Wyrm](/bestiary/monsters/ancient-wyrm/), [Evil Mage](/bestiary/humanoids/evil-mage/), [Fire Elemental](/bestiary/elementals/fire-elemental/).

## Hythloth

The deepest, most dangerous of the original eight, set in volcanic depths beneath the
Lost Lands' eastern reaches. Gargoyles and gazers give way to daemons and **balrons** —
end-game fights that punish under-prepared players hard.

- **Map:** ![Hythloth location](/img/maps/dungeon-hythloth.png)
- **Features:** Multi-level lava dungeon; one of the original eight virtue dungeons (Humility); a champion spawn; balrons are the marquee threat.
- **Monsters found here:** [Gargoyle](/bestiary/humanoids/gargoyle/), [Imp](/bestiary/monsters/imp/), [Hell Hound](/bestiary/monsters/hell-hound/), [Gazer](/bestiary/monsters/gazer/), [Daemon](/bestiary/monsters/daemon/), [Gazer Larva](/bestiary/monsters/gazer-larva/), [Fire Gargoyle](/bestiary/humanoids/fire-gargoyle/), [Balron](/bestiary/monsters/balron/), [Stone Gargoyle](/bestiary/humanoids/stone-gargoyle/), [Elder Gazer](/bestiary/monsters/elder-gazer/), [Undead Gargoyle](/bestiary/undead/undead-gargoyle/).

## Khaldun

A buried Lost Lands tomb-complex steeped in necromantic corruption. Beyond ordinary
undead it spawns **Zealots of Khaldun**, cursed creatures and named figures tied to the
old Khaldun questline — and it connects to the Harrower champion encounter.

- **Map:** ![Khaldun location](/img/maps/dungeon-khaldun.png)
- **Features:** Sprawling tomb with quest geography; ties into the [Harrower](/bestiary/bosses/) champion spawn (note the harrower-tentacle spawn in the data); high-end undead loot.
- **Monsters found here:** **Shadowfiend**, [Zombie](/bestiary/undead/zombie/), [Cursed](/bestiary/monsters/cursed/), [Skeleton](/bestiary/undead/skeleton/), [Skeletal Knight](/bestiary/undead/skeletal-knight/), [Zealot Of Khaldun](/bestiary/monsters/khaldun-zealot/), [Spectral Armour](/bestiary/undead/spectral-armour/), [Ancient Lich](/bestiary/undead/ancient-lich/), [Bone Mage](/bestiary/undead/bone-magi/), [Bone Knight](/bestiary/undead/bone-knight/), [Grimmoch Drummel](/bestiary/monsters/grimmoch-drummel/), [Tentacles Of The Harrower](/bestiary/bosses/harrower-tentacles/), [Lysander Gathenwale](/bestiary/monsters/lysander-gathenwale/), plus more.

## Fire Dungeon

A lava-floored cavern in the Lost Lands, full of fire elementals, hellhounds, efreet and
lava lizards mixed with fire-themed undead mages. Cold-resist and fire-protection gear pay
for themselves here.

- **Map:** ![Fire Dungeon location](/img/maps/dungeon-fire-dungeon.png)
- **Features:** Single large lava-cavern level; heavy fire-damage spawn; a champion spawn; efreet are a worthwhile rare kill.
- **Monsters found here:** [Fire Elemental](/bestiary/elementals/fire-elemental/), [Hell Hound](/bestiary/monsters/hell-hound/), [Evil Mage](/bestiary/humanoids/evil-mage/), [Bone Mage](/bestiary/undead/bone-magi/), [Hell Cat](/bestiary/monsters/hell-cat/), [Skeletal Mage](/bestiary/undead/skeletal-mage/), [Lava Snake](/bestiary/monsters/lava-snake/), [Lich](/bestiary/undead/lich/), [Evil Mage Lord](/bestiary/humanoids/evil-mage-lord/), [Lava Lizard](/bestiary/monsters/lava-lizard/), [Efreet](/bestiary/monsters/efreet/), [Lava Serpent](/bestiary/monsters/lava-serpent/), plus more.

## Ice Dungeon

The frozen counterpart to Fire, a Lost Lands warren of ice and snow elementals, frost
trolls, and a large ratman colony. Deeper sections hide ice fiends and a white wyrm.

- **Map:** ![Ice Dungeon location](/img/maps/dungeon-ice-dungeon.png)
- **Features:** Multi-section ice cave; ratman colony up front, true ice creatures deeper; a champion spawn; cold-damage heavy.
- **Monsters found here:** [Ice Elemental](/bestiary/elementals/ice-elemental/), [Snow Elemental](/bestiary/elementals/snow-elemental/), [Giant Ice Serpent](/bestiary/monsters/ice-serpent/), [Ratman](/bestiary/humanoids/ratman/), [Ratman Archer](/bestiary/humanoids/ratman-archer/), [Frost Troll](/bestiary/humanoids/frost-troll/), [Ratman Mage](/bestiary/humanoids/ratman-mage/), [Frost Ooze](/bestiary/monsters/frost-ooze/), [Frost Spider](/bestiary/monsters/frost-spider/), [Ice Snake](/bestiary/monsters/ice-snake/), [Arctic Ogre Lord](/bestiary/humanoids/arctic-ogre-lord/), [Crystal Vortex](/bestiary/monsters/crystal-vortex/), [Ice Fiend](/bestiary/monsters/ice-fiend/), [White Wyrm](/bestiary/monsters/white-wyrm/).

## Painted Caves

A primitive cave system in the southern Lost Lands. Light spawn — savages, troglodytes
and wildlife — makes it an easy detour, with the named beasts **Grobu** and **Lurg** as
the notable encounters.

- **Map:** ![Painted Caves location](/img/maps/dungeon-painted-caves.png)
- **Features:** Small cave; tribal/savage theme; low-pressure spawn good for newer players exploring the Lost Lands.
- **Monsters found here:** [Troglodyte](/bestiary/monsters/troglodyte/), [Giant Rat](/bestiary/monsters/giant-rat/), [Grobu](/bestiary/monsters/grobu/), [Lurg](/bestiary/monsters/lurg/), plus wildlife ([Cat](/bestiary/animals/cat/), [Dog](/bestiary/animals/dog/), [Rat](/bestiary/animals/rat/)).

## Terathan Keep

A war-fortress in the southern Lost Lands where the **Terathan** insectoids and the
**Ophidian** serpent-folk wage their endless feud. Matriarchs and avengers anchor a
genuinely dangerous spawn, with balrons and dragons in the deepest reaches.

- **Map:** ![Terathan Keep location](/img/maps/dungeon-terathan-keep.png)
- **Features:** Tiered keep interior; both factions spawn (great for faction-specific kill quests); a champion spawn; nightmares and dragons appear at depth.
- **Monsters found here:** [Terathan Drone](/bestiary/monsters/terathan-drone/), [Terathan Warrior](/bestiary/monsters/terathan-warrior/), [Terathan Avenger](/bestiary/monsters/terathan-avenger/), [Ophidian Warrior](/bestiary/monsters/ophidian-warrior/), [Nightmare](/bestiary/monsters/nightmare/), [Ophidian Knight](/bestiary/monsters/ophidian-knight/), [Ophidian Mage](/bestiary/monsters/ophidian-mage/), [Ophidian Matriarch](/bestiary/monsters/ophidian-matriarch/), [Terathan Matriarch](/bestiary/monsters/terathan-matriarch/), [Ophidian Archmage](/bestiary/monsters/ophidian-archmage/), [Balron](/bestiary/monsters/balron/), [Dragon](/bestiary/monsters/dragon/), [Drake](/bestiary/monsters/drake/).

## Blighted Grove

A corrupted swamp grove from the *Mondain's Legacy* era, reachable by boat off the western
coast. Plant-creatures, bog beasts and the named **insane dryad** thrive amid the rot.

- **Map:** ![Blighted Grove location](/img/maps/dungeon-blighted-grove.png)
- **Features:** Open swamp arena (ML); plant/bog spawn; tied to the Blighted Grove quest; whipping vines and tangles immobilize.
- **Monsters found here:** [Bogling](/bestiary/monsters/bogling/), [Harpy](/bestiary/monsters/harpy/), [Giant Serpent](/bestiary/monsters/giant-serpent/), [Alligator](/bestiary/monsters/alligator/), [Giant Toad](/bestiary/monsters/giant-toad/), [Reaper](/bestiary/monsters/reaper/), [Silver Serpent](/bestiary/monsters/silver-serpent/), [Whipping Vine](/bestiary/monsters/whipping-vine/), [Changeling](/bestiary/monsters/changeling/), [Swamp Tentacle](/bestiary/monsters/swamp-tentacle/), [Tangle](/bestiary/monsters/tangle/), [Corpser](/bestiary/monsters/corpser/), plus more.

## Prism of Light

A *Mondain's Legacy* crystal dungeon of luminous caverns. Wisps and crystal-themed
creatures — vortices, lattice seekers, a crystal hydra and crystal daemon — make for an
unusual, energy-heavy fight.

- **Map:** ![Prism of Light location](/img/maps/dungeon-prism-of-light.png)
- **Features:** Crystalline cave layout (ML); energy/cold damage spawn; the Lady-of-the-Snow / crystal-boss encounters; crystal-only crafting reagent drops.
- **Monsters found here:** [Wisp](/bestiary/monsters/wisp/), [Snake](/bestiary/monsters/snake/), [Crystal Lattice Seeker](/bestiary/monsters/crystal-lattice-seeker/), [Ice Snake](/bestiary/monsters/ice-snake/), [Crystal Vortex](/bestiary/monsters/crystal-vortex/), [Ice Elemental](/bestiary/elementals/ice-elemental/), [Protector](/bestiary/monsters/protector/), [Shadow Wisp](/bestiary/monsters/shadow-wisp/), [Crystal Daemon](/bestiary/monsters/crystal-daemon/), [Crystal Hydra](/bestiary/monsters/crystal-hydra/), [Crystal Sea Serpent](/bestiary/sea/crystal-sea-serpent/), plus crystal wisps.

## Palace of Paroxysmus

A *Stygian Abyss*-era dungeon drowned in toxic slime — the corrosive domain of Paroxysmus.
Plague beasts, acid and poison elementals, and a roster of daemons culminate in heavyweight
fights against Putrefier, Moloch and the Interred Grizzle.

- **Features:** Acid/poison-themed dungeon; environmental acid hazards; mini-boss roster (Putrefier, Moloch, Interred Grizzle); part of the Stygian Abyss content.
- **Monsters found here:** [Corrosive Slime](/bestiary/monsters/corrosive-slime/), [Plague Beast](/bestiary/monsters/plague-beast/), [Plague Spawn](/bestiary/monsters/plague-spawn/), [Poison Elemental](/bestiary/elementals/poison-elemental/), [Acid Elemental](/bestiary/elementals/toxic-elemental/), [Daemon](/bestiary/monsters/daemon/), [Succubus](/bestiary/monsters/succubus/), [Balron](/bestiary/monsters/balron/), [Plague Beast Lord](/bestiary/monsters/plague-beast-lord/), [Interred Grizzle](/bestiary/monsters/interred-grizzle/), [Chaos Daemon](/bestiary/monsters/chaos-daemon/), [Moloch](/bestiary/monsters/moloch/), [Putrefier](/bestiary/monsters/putrefier/).

## Wisp Dungeon

An Ilshenar cavern named for its resident **wisps**, but the real danger is the high-end
undead and a balron lurking among them. A short, sharp dungeon that punches above its size.

- **Map:** ![Wisp Dungeon location](/img/maps/dungeon-wisp-dungeon.png)
- **Features:** Compact Ilshenar cave; mixed wisp/undead/demon spawn; cyclopean warriors and titans add melee threat.
- **Monsters found here:** [Wisp](/bestiary/monsters/wisp/), [Shade](/bestiary/undead/shade/), [Imp](/bestiary/monsters/imp/), [Bone Knight](/bestiary/undead/bone-knight/), [Bone Mage](/bestiary/undead/bone-magi/), [Evil Mage](/bestiary/humanoids/evil-mage/), [Evil Mage Lord](/bestiary/humanoids/evil-mage-lord/), [Spectre](/bestiary/undead/spectre/), [Wraith](/bestiary/undead/wraith/), [Balron](/bestiary/monsters/balron/), [Cyclopean Warrior](/bestiary/humanoids/cyclops/), [Ettin](/bestiary/humanoids/ettin/), [Rotting Corpse](/bestiary/undead/rotting-corpse/), [Titan](/bestiary/humanoids/titan/), plus more.

## Solen Hive

An underground ant-colony dungeon reached through tunnels north of Britain (and via the
Lost Lands). It houses two warring colonies — the **Black** and **Red Solen** — of workers,
warriors and queens, plus burrowing ant lions. Players can side with one colony's quests
against the other.

- **Map:** ![Solen Hive location](/img/maps/dungeon-solen-hive.png)
- **Features:** Branching tunnel network split into Black and Red colony halves; Solen friendship questline; zoogi-fungus harvesting; queens as the apex spawn.
- **Monsters found here:** [Black Solen Worker](/bestiary/monsters/black-solen-worker/), [Red Solen Worker](/bestiary/monsters/red-solen-worker/), [Black Solen Warrior](/bestiary/monsters/black-solen-warrior/), [Red Solen Warrior](/bestiary/monsters/red-solen-warrior/), [Ant Lion](/bestiary/monsters/ant-lion/), [Black Solen Queen](/bestiary/monsters/black-solen-queen/), [Red Solen Queen](/bestiary/monsters/red-solen-queen/).

## Sorcerer's Dungeon

A large Ilshenar dungeon of dark mages and their summoned servants — liches, bone mages,
elementals and gargoyles in quantity. With the most distinct creature classes of any
Ilshenar dungeon, it stays varied from entrance to depths.

- **Features:** Multi-level Ilshenar dungeon; mage-heavy spawn (bring magic resist); blood elementals near the bottom; a champion spawn.
- **Monsters found here:** [Blood Elemental](/bestiary/elementals/blood-elemental/), [Gargoyle](/bestiary/humanoids/gargoyle/), [Mongbat](/bestiary/monsters/mongbat/), [Mummy](/bestiary/undead/mummy/), [Bone Mage](/bestiary/undead/bone-magi/), [Hell Hound](/bestiary/monsters/hell-hound/), [Lich Lord](/bestiary/undead/lich-lord/), [Skeletal Mage](/bestiary/undead/skeletal-mage/), [Bone Knight](/bestiary/undead/bone-knight/), [Dull Copper Elemental](/bestiary/elementals/dull-copper-elemental/), [Fire Elemental](/bestiary/elementals/fire-elemental/), [Shade](/bestiary/undead/shade/), [Acid Elemental](/bestiary/elementals/toxic-elemental/), [Gazer](/bestiary/monsters/gazer/), plus 19 more.

## Spectre Dungeon

A small, purely **undead** haunt in eastern Ilshenar. Few spawn points, but every one of
them is a shade, spectre, wraith, ghoul or lich — a quick, focused undead farm.

- **Features:** Tiny Ilshenar dungeon; uniform high-undead spawn; ideal for testing anti-undead loadouts.
- **Monsters found here:** [Shade](/bestiary/undead/shade/), [Spectre](/bestiary/undead/spectre/), [Wraith](/bestiary/undead/wraith/), [Ghoul](/bestiary/undead/ghoul/), [Lich](/bestiary/undead/lich/).

## Exodus Dungeon

The Ilshenar stronghold of **Exodus**, the mechanical demon-king. Golems, exodus minions
and gargoyle constructs defend it, alongside the Dupre's-knights encounter from the Exodus
questline. High-end, mechanically themed loot.

- **Features:** Fortified Ilshenar dungeon; construct/golem spawn; tied to the Exodus encounter quest; juggernaut and overseer mini-bosses.
- **Monsters found here:** **ExodusZealot**, [Golem Controller](/bestiary/humanoids/golem-controller/), **ExodusDrone**, [Exodus Minion](/bestiary/monsters/exodus-minion/), [Exodus Overseer](/bestiary/monsters/exodus-overseer/), [Golem](/bestiary/monsters/golem/), **ExodusSentinel**, [Gargoyle Destroyer](/bestiary/humanoids/gargoyle-destroyer/), [Gargoyle Enforcer](/bestiary/humanoids/gargoyle-enforcer/), [Enslaved Gargoyle](/bestiary/humanoids/enslaved-gargoyle/), **ExodusJuggernaut**, plus the Dupre's knights/champion encounter. *(Bolded names are Exodus-specific creatures not yet in the bestiary.)*

## Spider Cave

A cramped Ilshenar crawl mixing ratmen, undead knights and a **skeletal dragon**. Small but
surprisingly toothy for its footprint.

- **Features:** Single tight cave; ratman + undead spawn; skeletal dragon is the standout kill.
- **Monsters found here:** [Bone Knight](/bestiary/undead/bone-knight/), [Lava Lizard](/bestiary/monsters/lava-lizard/), [Skeletal Knight](/bestiary/undead/skeletal-knight/), [Earth Elemental](/bestiary/elementals/earth-elemental/), [Ratman](/bestiary/humanoids/ratman/), [Ratman Mage](/bestiary/humanoids/ratman-mage/), [Skeletal Dragon](/bestiary/undead/skeletal-dragon/).

## Doom (The Gauntlet)

In Malas lies **Doom**, and within it **The Gauntlet** — a fixed gauntlet of mini-bosses
ending at the **Dark Father**, with the famous artifact loot table. The open dungeon
around it teems with named undead and gore fiends. One of the toughest dungeons on the shard.

- **Features:** The Gauntlet boss-rush culminating in the Dark Father; artifact drops on a point-based system; surrounding halls of high undead; a healer is stationed at the entrance.
- **Monsters found here:** [Vampire Bat](/bestiary/undead/vampire-bat/), [Patchwork Skeleton](/bestiary/undead/patchwork-skeleton/), [Skeleton](/bestiary/undead/skeleton/), [Devourer Of Souls](/bestiary/monsters/devourer/), [Lich](/bestiary/undead/lich/), [Rotting Corpse](/bestiary/undead/rotting-corpse/), [Zombie](/bestiary/undead/zombie/), [Flesh Golem](/bestiary/monsters/flesh-golem/), [Lich Lord](/bestiary/undead/lich-lord/), [Mummy](/bestiary/undead/mummy/), [Gibberling](/bestiary/monsters/gibberling/), [Gore Fiend](/bestiary/undead/gore-fiend/), [Bone Knight](/bestiary/undead/bone-knight/), [Restless Soul](/bestiary/monsters/restless-soul/), plus more.

## Bedlam

A *Mondain's Legacy* necromancer asylum in Malas, accessible via the Bedlam quest. Its
spawn is built around **named undead** — Master Jonath, Lady Marai, Red Death and others —
making it a curated boss-hunt more than a grind.

- **Features:** Asylum interior (ML); roster of named undead casters and fiends; quest-gated access; strong necro-themed loot.
- **Monsters found here:** [Gibberling](/bestiary/monsters/gibberling/), [Gore Fiend](/bestiary/undead/gore-fiend/), [Rotting Corpse](/bestiary/undead/rotting-corpse/), [Skeleton](/bestiary/undead/skeleton/), [Lady Jennifyr](/bestiary/monsters/lady-jennifyr/), [Lady Marai](/bestiary/monsters/lady-marai/), [Master Jonath](/bestiary/monsters/master-jonath/), [Master Mikael](/bestiary/monsters/master-mikael/), [Master Theophilus](/bestiary/monsters/master-theophilus/), [Pyre](/bestiary/monsters/pyre/), [Red Death](/bestiary/monsters/red-death/), [Rend](/bestiary/monsters/rend/), [Sir Patrick](/bestiary/monsters/sir-patrick/), [Skeletal Mage](/bestiary/undead/skeletal-mage/).

## Labyrinth

A *Mondain's Legacy* minotaur maze beneath Malas. Minotaurs and scouts patrol the corridors,
and the air-elemental **Flurry / Grim / Mistral / Tempest** family circulate as roaming
threats. Easy to get lost in — bring a recall route out.

- **Features:** True maze layout (ML); minotaur spawn plus air-elemental "weather" creatures; tied to the Labyrinth/Minotaur quests; miasma encounter.
- **Monsters found here:** [Minotaur](/bestiary/humanoids/minotaur/), [Minotaur Scout](/bestiary/humanoids/minotaur-scout/), [Reptalon](/bestiary/monsters/reptalon/), [Scorpion](/bestiary/monsters/scorpion/), [Flurry](/bestiary/monsters/flurry/), [Grim](/bestiary/monsters/grim/), [Mistral](/bestiary/monsters/mistral/), plus more (incl. maze wildlife and a tempest).

## Fan Dancer's Dojo

A Tokuno dungeon overrun by demons and the spectral **fan dancers** it's named for. Oni,
ronin and a succubus round out an aggressive, fast-moving spawn.

- **Features:** Tokuno dojo interior; demon + samurai-spirit theme; tied to Tokuno minor-artifact drops; balron at depth.
- **Monsters found here:** [Headless One](/bestiary/humanoids/headless-one/), [Fan Dancer](/bestiary/monsters/fan-dancer/), [Horde Minion](/bestiary/monsters/horde-minion/), [Daemon](/bestiary/monsters/daemon/), [Hell Hound](/bestiary/monsters/hell-hound/), [Hell Cat](/bestiary/monsters/hell-cat/), [Succubus](/bestiary/monsters/succubus/), [Balron](/bestiary/monsters/balron/), [Oni](/bestiary/monsters/oni/), [Ronin](/bestiary/monsters/ronin/).

## Yomotsu Mines

A Tokuno mine held by the **Yomotsu** warrior-monks, backed by metal elementals and fire
beetles. Small and fairly approachable by Tokuno standards.

- **Features:** Compact mine; Yomotsu warriors and priests; copper/earth elementals; Tokuno artifact chances.
- **Monsters found here:** [Yomotsu Priest](/bestiary/monsters/yomotsu-priest/), [Yomotsu Warrior](/bestiary/monsters/yomotsu-warrior/), [Dull Copper Elemental](/bestiary/elementals/dull-copper-elemental/), [Earth Elemental](/bestiary/elementals/earth-elemental/), [Fire Beetle](/bestiary/monsters/fire-beetle/).

## The Citadel

A Tokuno fortress held by the **Black Order** ninja clans — the Serpent's Fang, Dragon's
Flame and Tiger's Claw schools — each with assassins, mages, thieves and a master. Many
encounters trigger on proximity, so expect ambushes.

- **Features:** Tokuno fortress; three rival ninja schools with distinct rosters; trigger-based ambush spawns; Black Order loot and Tokuno artifacts.
- **Monsters found here:** [Black Order Assassin](/bestiary/monsters/serpents-fang-assassin/), [Black Order Mage](/bestiary/monsters/dragons-flame-mage/), [Elite Ninja](/bestiary/monsters/elite-ninja/), [Black Order Thief](/bestiary/monsters/tigers-claw-thief/), [Black Order Grand Mage](/bestiary/monsters/dragons-flame-grand-mage/), [Black Order Master](/bestiary/monsters/tigers-claw-master/), [Black Order High Executioner](/bestiary/humanoids/serpents-fang-high-executioner/).

---

## Notes

- **Spawn lists are source-verified** against `../servuo/Spawns/*.xml` and re-extractable
  via `python3 tools/extract_dungeon_spawns.py`. Each list shows the most-frequent
  creatures (by total max-count) first; "plus N more" covers rarer additions in the
  same dungeon. A handful of custom/revamped creatures (bolded, not linked) don't yet
  have [Bestiary](/bestiary/) pages.
- **Coordinates** are uomap POI entrance locations; the spawn files store map-internal
  region coordinates, which is why some dungeons report a different facet (e.g. the
  Trammel copy holds more spawn points than the Felucca one) — the creature lists are
  identical across the mirrored facets.
- In **Felucca**, every dungeon is also a PvP zone, with better loot — see the
  [server rules](/shard/server-rules/). For getting around, see the
  [world map and cities](/world/).
- Heading in? Brush up on [Combat Basics](/playing/combat-basics/),
  [Treasure Hunting](/playing/treasure-hunting/), and your
  [profession's](/professions/) strengths first.
- File a [discrepancy report](/guides/wiki-conventions/) if a spawn doesn't match what
  you find in-game.
