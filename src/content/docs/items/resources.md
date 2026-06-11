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
| <img src="/img/items/0x1BF2-h0973.png" class="uo-sprite" alt="" width="56" /> | Dull Copper | 65.0 | 11.2% | 65.0 |
| <img src="/img/items/0x1BF2-h0966.png" class="uo-sprite" alt="" width="56" /> | Shadow Iron | 70.0 | 9.8% | 70.0 |
| <img src="/img/items/0x1BF2-h096D.png" class="uo-sprite" alt="" width="56" /> | Copper | 75.0 | 8.4% | 75.0 |
| <img src="/img/items/0x1BF2-h0972.png" class="uo-sprite" alt="" width="56" /> | Bronze | 80.0 | 7.0% | 80.0 |
| <img src="/img/items/0x1BF2-h08A5.png" class="uo-sprite" alt="" width="56" /> | Gold | 85.0 | 5.6% | 85.0 |
| <img src="/img/items/0x1BF2-h0979.png" class="uo-sprite" alt="" width="56" /> | Agapite | 90.0 | 4.2% | 90.0 |
| <img src="/img/items/0x1BF2-h089F.png" class="uo-sprite" alt="" width="56" /> | Verite | 95.0 | 2.8% | 95.0 |
| <img src="/img/items/0x1BF2-h08AB.png" class="uo-sprite" alt="" width="56" /> | Valorite | 99.0 | 1.4% | 99.0 |

Mining also yields matching **granite** (for stonecraft), **sand** at 70+ skill (glassblowing),
and — at 100.0 — rare gems and blackrock as bonus finds.

## Logs and boards ([Lumberjacking](/skills/lumberjacking/))

Chop trees for logs (10 per swing), cut logs into boards with an axe. Chop requirements from
`Lumberjacking.cs`; board-cutting accepts **Carpentry or Lumberjacking** at the listed skill
(`Log.cs`):

| Log | Board | Lumberjacking to chop | Vein chance | Skill to cut boards |
|---|---|---|---|---|
| <img src="/img/items/0x1BD7.png" class="uo-sprite" alt="" width="56" /> | Ordinary | 0 | 49% | 0 |
| <img src="/img/items/0x1BD7-h07DA.png" class="uo-sprite" alt="" width="56" /> | Oak | 65.0 | 30% | 65 |
| <img src="/img/items/0x1BD7-h04A7.png" class="uo-sprite" alt="" width="56" /> | Ash | 80.0 | 10% | 80 |
| <img src="/img/items/0x1BD7-h04A8.png" class="uo-sprite" alt="" width="56" /> | Yew | 95.0 | 5% | 95 |
| <img src="/img/items/0x1BD7-h04A9.png" class="uo-sprite" alt="" width="56" /> | Heartwood | 100.0 | 3% | 100 |
| <img src="/img/items/0x1BD7-h04AA.png" class="uo-sprite" alt="" width="56" /> | Bloodwood | 100.0 | 2% | 100 |
| <img src="/img/items/0x1BD7-h047F.png" class="uo-sprite" alt="" width="56" /> | Frostwood | 100.0 | 1% | 100 |

Bonus chops at 100.0: bark fragments, luminescent fungi, switches, parasitic plants,
brilliant amber.

## Leather

Skin animal corpses with a bladed tool for **hides**, cut into **leather** with scissors.
Four types per `ResourceInfo.cs` (`m_AOSLeatherInfo`):

| | Leather | Comes from |
|---|---------|-----------|
| <img src="/img/items/0x1081.png" class="uo-sprite" alt="" width="56" /> | Normal | Common animals (cows, deer, etc.) |
| <img src="/img/items/0x1081-h0283.png" class="uo-sprite" alt="" width="56" /> | Spined | Tougher beasts |
| <img src="/img/items/0x1081-h0227.png" class="uo-sprite" alt="" width="56" /> | Horned | Dangerous monsters |
| <img src="/img/items/0x1081-h01C1.png" class="uo-sprite" alt="" width="56" /> | Barbed | The top predators (dragons and kin) |

Which specific creatures yield which leather is bestiary territory — see the
[Bestiary](/bestiary/). Each leather grade carries its own crafting attribute bundle
(`CraftAttributeInfo`).

## Cloth — from sheep and fields to a bolt

Cloth isn't gathered with a skill; it's *manufactured* from raw fibre through a spinning
wheel and a loom. The chain (from `Scripts/Items/Resource/Cotton.cs`, `Wool.cs`, `Flax.cs`,
`YarnsAndThreads.cs`, `BoltOfCloth.cs`):

| Step | Tool | Yields |
|---|---|---|
| Raw fibre — <img src="/img/items/0x0DF9.png" class="uo-sprite" alt="" width="56" /> **cotton** (pick from cotton plants), <img src="/img/items/0x0DF8.png" class="uo-sprite" alt="" width="56" /> **wool** (shear sheep), or <img src="/img/items/0x1A9C.png" class="uo-sprite" alt="" width="56" /> **flax** (harvest flax plants) | — | the fibre itself |
| **Spin** the fibre | Spinning wheel | <img src="/img/items/0x0FA0.png" class="uo-sprite" alt="" width="56" /> **spools of thread / yarn** (6 per use) |
| **Weave** the thread | Loom | <img src="/img/items/0x0F95.png" class="uo-sprite" alt="" width="56" /> **bolt of cloth** |
| **Cut** the bolt | Scissors | <img src="/img/items/0x1766.png" class="uo-sprite" alt="" width="56" /> **cloth** (50 per bolt) |
| **Cut** the cloth | Scissors | <img src="/img/items/0x0E21.png" class="uo-sprite" alt="" width="56" /> **bandages** — the fuel of [Healing](/skills/healing/) |

Spinning wheels and looms stand in tailor shops and many homes (both are craftable house
addons). No skill check gates spinning or weaving — anyone can run fibre all the way to
cloth; the skill comes later, when a tailor turns cloth into clothing and armor.

You can also just **buy** bolts of cloth, wool, and cotton from tailor and provisioner
vendors and skip straight to the scissors. Cloth takes any dye, so colored clothing is a
dye-tub job rather than a separate material — see the [Hue Reference](/reference/hues/).

Tailoring turns cloth into clothing and light armor — see [Tailoring](/crafting/tailoring/)
and the [Clothing catalog](/items/catalog/clothing/).

## Related

- [Items overview](/items/) · [Blacksmithy](/skills/blacksmithy/) · [Crafting](/crafting/)
- [Interactive map](https://uomap.vercel.app) — find vendors and terrain
