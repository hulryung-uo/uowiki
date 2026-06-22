---
title: Treasure Hunter
description: Decode maps, dig up chests, beat the guardians — cartography, mining, lockpicking, and remove trap. The skills, the guide, and the payday.
status: source-verified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMap.cs (Cartography decode + dig gate; guardian spawn tables; EJ dig uses Cartography not Mining)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapInfo.cs (NewSystem = Core.EJ; named tiers Stash/Supply/Cache/Hoard/Trove)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapChest.cs (lock/RequiredSkill, TrapType/TrapLevel, power-scroll loot)"
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The treasure hunter turns a cryptic map into buried gold. Decode the map to learn the dig
site, travel there, dig up the chest, disarm its trap, pick its lock, and survive the
guardian monsters the chest summons when you open it. The reward scales with the map's level
(on our EJ shard maps run the five tiers Stash → Supply → Cache → Hoard → Trove):
high-tier chests hold piles of gold, gems, regs, magic gear, and the
coveted **power scrolls**. It's a self-contained adventure profession with a clear payday at
the end of each map.

## Core skills

- [Cartography](/skills/cartography/) — decode the treasure map to reveal its dig location; the gate skill of the profession. On our shard (expansion EJ) Cartography also governs the **dig** itself, including how close to the marked spot you have to be.
- [Mining](/skills/mining/) — you need a **digging tool** (pickaxe or shovel) in your pack to dig the chest, so the t-hunter kit overlaps with mining gear. Note: under EJ the dig is gated by your *Cartography* skill, not your Mining skill — the tool is what Mining provides here, not the skill check.
- [Lockpicking](/skills/lockpicking/) — open the locked chest you've unearthed.
- [Remove Trap](/skills/remove-trap/) — disarm the chest's trap before it explodes in your face.
- **Combat support** — high-level chests spawn tough guardians, so bring fighting power: [Magery](/skills/magery/), the [warrior](/professions/warrior/) kit, or [Animal Taming](/skills/animal-taming/) for a pet to tank them.

## The build

There is **no dedicated treasure-hunter template** in this wiki yet. The core skills
(Cartography + Lockpicking + Remove Trap, plus a digging tool for the dig) leave grandmaster slots for a combat
package — most t-hunters fold this into a [mage](/professions/mage/) or [tamer](/professions/tamer/)
build so one character can both open the chest and kill the guardians. See
[7x GM Templates](/templates/seven-gm/) for fitting all seven under the 700-point cap.

## How to play it

The dedicated **[Treasure Hunting guide](/playing/treasure-hunting/)** is your main
reference — it has the decode-to-dig walkthrough, the map gump, the location map, the chest
levels, and the guardian spawns. Read it before your first map.

The core loop: get a map (loot or buy one), [decode it with Cartography](/skills/cartography/),
travel to the site via [Movement & Travel](/playing/movement-and-travel/),
[dig it up](/skills/mining/) with a pickaxe or shovel in your pack (Cartography sets your dig range),
[remove the trap](/skills/remove-trap/),
[pick the lock](/skills/lockpicking/), then **survive the guardians** before looting the
chest. Going in with a [tamer's](/professions/tamer/) pet or a [mage's](/professions/mage/)
summons to handle the guardians is the standard way to do high-level maps solo.

## Gear & tools

- **A shovel or pickaxe** for the [Mining](/skills/mining/) dig, and a **lockpick** for the chest — see [tools](/items/catalog/tools/) and [Tools](/items/tools/).
- Combat gear for the guardians: [weapons](/items/weapons/) and [armor](/items/armor/), or a spellbook with [reagents](/items/reagents/).
- A way to carry a heavy haul home — the chest loot is bulky.

## Making a living

The payday is the **chest loot itself**: gold, gems, reagents, magic weapons and armor, and —
on higher-level chests — [power scrolls](/items/catalog/scrolls/) that raise skill caps and
sell for serious gold. One good high-level map can out-earn a long farming session. Sell the
haul via [Vendors & Banking](/playing/vendors-and-banking/). Many t-hunters also sell or trade
the maps themselves.

## See also

- [Treasure Hunting guide](/playing/treasure-hunting/) — the full walkthrough, map gump, and locations
- [Tamer](/professions/tamer/) and [Mage](/professions/mage/) — the usual guardian-killing partners
- [Thief](/professions/thief/) — the other rogue profession, shares Lockpicking
- [Cartography](/skills/cartography/) · [Mining](/skills/mining/) · [Lockpicking](/skills/lockpicking/) · [Remove Trap](/skills/remove-trap/)
