---
title: Resources
description: Gathering yields and skill requirements — ores and ingots, logs and boards, leathers, and cloth.
status: source-verified
sources:
  - "servuo: Scripts/Services/Harvest/Mining.cs"
  - "servuo: Scripts/Services/Harvest/Lumberjacking.cs"
  - "servuo: Scripts/Items/Resource/Log.cs"
  - "servuo: Scripts/Misc/ResourceInfo.cs"
last_verified: 2026-06-11
generated: false
---

Every empire is built on somebody hauling rocks. These are the raw materials of Britannia's
economy, with the skill numbers from the harvest definitions in the server source.

## Ore and ingots ([Mining](/skills/mining/))

Dig ore from mountains and caves, smelt at a forge into ingots of the same metal. Skill
requirements and vein rarity from `Scripts/Services/Harvest/Mining.cs`; the ore→ingot type
mapping from `Scripts/Misc/ResourceInfo.cs`:

| | Ore → Ingot | Mining required | Vein chance | Smith skill to work |
|---|-------------|-----------------|-------------|---------------------|
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Iron | 0 | 49.6% | 0 |
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Dull Copper | 65.0 | 11.2% | 65.0 |
| | Shadow Iron | 70.0 | 9.8% | 70.0 |
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Copper | 75.0 | 8.4% | 75.0 |
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Bronze | 80.0 | 7.0% | 80.0 |
| | Gold | 85.0 | 5.6% | 85.0 |
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Agapite | 90.0 | 4.2% | 90.0 |
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Verite | 95.0 | 2.8% | 95.0 |
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Valorite | 99.0 | 1.4% | 99.0 |

Mining also yields matching **granite** (for stonecraft), **sand** at 70+ skill (glassblowing),
and — at 100.0 — rare gems and blackrock as bonus finds.

## Logs and boards ([Lumberjacking](/skills/lumberjacking/))

Chop trees for logs (10 per swing), cut logs into boards with an axe. Chop requirements from
`Lumberjacking.cs`; board-cutting accepts **Carpentry or Lumberjacking** at the listed skill
(`Log.cs`):

| Log | Board | Lumberjacking to chop | Vein chance | Skill to cut boards |
|---|---|---|---|---|
| <img src="/img/items/0x1BDD.png" class="uo-sprite" alt="" width="56" /> | Ordinary | 0 | 49% | 0 |
| <img src="/img/items/0x1BDD.png" class="uo-sprite" alt="" width="56" /> | Oak | 65.0 | 30% | 65 |
| <img src="/img/items/0x1BDD.png" class="uo-sprite" alt="" width="56" /> | Ash | 80.0 | 10% | 80 |
| <img src="/img/items/0x1BDD.png" class="uo-sprite" alt="" width="56" /> | Yew | 95.0 | 5% | 95 |
| <img src="/img/items/0x1BDD.png" class="uo-sprite" alt="" width="56" /> | Heartwood | 100.0 | 3% | 100 |
| <img src="/img/items/0x1BDD.png" class="uo-sprite" alt="" width="56" /> | Bloodwood | 100.0 | 2% | 100 |
| <img src="/img/items/0x1BDD.png" class="uo-sprite" alt="" width="56" /> | Frostwood | 100.0 | 1% | 100 |

Bonus chops at 100.0: bark fragments, luminescent fungi, switches, parasitic plants,
brilliant amber.

## Leather

Skin animal corpses with a bladed tool for **hides**, cut into **leather** with scissors.
Four types per `ResourceInfo.cs` (`m_AOSLeatherInfo`):

| | Leather | Comes from |
|---|---------|-----------|
| <img src="/img/items/0x1081.png" class="uo-sprite" alt="" width="56" /> | Normal | Common animals (cows, deer, etc.) |
| | Spined | Tougher beasts |
| | Horned | Dangerous monsters |
| | Barbed | The top predators (dragons and kin) |

Which specific creatures yield which leather is bestiary territory — see the
[Bestiary](/bestiary/). Each leather grade carries its own crafting attribute bundle
(`CraftAttributeInfo`).

## Cloth

Cloth is commerce, not gathering: buy **bolts of cloth** (or wool/cotton to spin and weave)
from tailor and provisioner vendors, cut bolts into cloth, and cut cloth into **bandages** —
the fuel of [Healing](/skills/healing/). Tailors turn the same cloth into clothing.

## Related

- [Items overview](/items/) · [Blacksmithy](/skills/blacksmithy/) · [Crafting](/crafting/)
- [Interactive map](https://uomap.vercel.app) — find vendors and terrain
