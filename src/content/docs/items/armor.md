---
title: Armor
description: How armor and the five resistances work, every material from cloth to dragon scale, body slots, shields, and how to assemble a balanced suit.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Armor/BaseArmor.cs"
  - "servuo: Scripts/Items/Equipment/Armor/ArmorEnums.cs"
  - "servuo: Scripts/Items/Equipment/Armor/*.cs (per-piece base resists, str req, material)"
  - "servuo: Server/Mobile.cs (MaxPlayerResistance = 70)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (GetMinResistance — Magic Resist floor)"
  - "servuo: Scripts/Misc/RegenRates.cs (GetArmorMeditationValue — meditation/mana penalty)"
  - "client art: static art for piece sprites"
  - "data: data/armor.json (gallery — 148 piece sprites grouped by material)"
  - "servuo: Scripts/Items/Equipment/Armor/ArmorEnums.cs (Protection/Durability tiers)"
last_verified: 2026-06-17
generated: false
---

Armor is what stands between your hit points and a dragon's breath. On our shard
(ServUO, Endless Journey / AOS rules), every piece you wear contributes **resistances**
that soak a share of each damage type. A good suit is not about one heavy chestplate —
it is about covering all six body slots and balancing five resist numbers under a hard
cap.

The numbers in the tables below are the **base** values defined per piece in the server
source. The amount that actually shows on your paperdoll adds bonuses from the craft
**resource** (ore or leather type), **exceptional** quality, and any magic properties —
see [Materials](#materials) and [Suits & strategy](#suits--strategy).

## How armor works (AOS / EJ)

### The five resistances

Modern armor is rated by five **resistances**, each reducing one damage type:

- **Physical** — swords, arrows, most melee and physical spells
- **Fire** — Fireball, Flamestrike, fire-breathing creatures
- **Cold** — frost spells and cold-based creatures
- **Poison** — Poison spells, poisoned weapons, venomous creatures
- **Energy** — Energy Bolt, Lightning, and energy attacks

A resistance of *N* means that damage type is reduced by *N* percent. Each armor piece
you wear adds its resists to your totals; the paperdoll shows the sum across all worn
pieces. Damage is applied against whichever resist matches the incoming type, so a
fire-heavy suit melts to an energy mage.

### The 70% resist cap

Player resistances are capped. In ServUO `Server/Mobile.cs` sets
`MaxPlayerResistance = 70` — **no single resistance can exceed 70%** no matter how much
armor or how many bonuses you stack. Suit-building is therefore a game of reaching 70 in
the types you care about without wasting overflow. (Some monsters and special effects can
lower your effective cap; the 70 ceiling is the normal player maximum.)

High **Magic Resistance** skill works the *other* way: it raises your resist *floor*
(`PlayerMobile.GetMinResistance`), pulling low resists up toward a minimum at GM Resist,
so a Resist mage is never fully naked to any element. See
[Combat (advanced)](/playing/combat-advanced/).

### Strength requirement

Every piece has a **Strength requirement** — heavier materials demand more. A plate chest
needs **95 Strength**; a leather chest only **25** (AOS values). Wear a piece below its
requirement and you suffer the consequences, which is why low-Strength casters lean toward
leather. Some armor mods and resources lower the requirement. See
[Character & Stats](/playing/character-and-stats/).

### Meditation penalty (mana regen)

Heavy and metal armor **chokes mana regeneration**. ServUO's
`RegenRates.GetArmorMeditationValue` checks each worn piece's **meditation allowance**:

- **All** (medable) — no penalty (leather, cloth, and most mage-friendly armor)
- **Half** — subtracts half the piece's scaled armor rating from mana regen (studded)
- **None** (non-medable) — subtracts the full scaled armor rating (bone, ring, chain,
  plate, dragon, stone)

The penalties from all worn pieces are summed and divided, dragging your mana regen down.
Two escapes exist: the **Mage Armor** property (and **Spell Channeling**) make any piece
count as fully medable for this calculation, and on Stygian Abyss / EJ rules non-medable
**metal** armor instead grants inherent **Lower Mana Cost** (a small tradeoff that helps
melee-casters). Full mechanics — including why mages favor leather — live in
[Meditation & Mana](/playing/meditation-and-mana/).

### Body slots and the "suit"

Armor covers six body slots, plus the off-hand for shields:

| Slot | Pieces |
|---|---|
| Helm | helmet, cap, coif, circlet, kabuto |
| Gorget / Neck | gorget, collar, mempo |
| Chest | chest, tunic, bustier |
| Arms | arms, sleeves, sode, pauldrons |
| Gloves | gloves, mitts |
| Legs | legs, leggings, kilt, skirt |

A full **suit** is one piece per slot. Because resists *add* across slots, a complete
suit of a modest material easily out-resists a single heavyweight chestplate worn alone.
The chest contributes the most armor rating (its scalar is the largest — see below), but
every empty slot is resist you are leaving on the table.

ServUO scales each slot's pre-AOS armor-rating contribution by a fixed table
(`BaseArmor.ArmorScalars`): Gorget `0.07`, Gloves `0.07`, Helmet `0.14`, Arms `0.15`,
Legs `0.22`, Chest `0.35`. The chest is roughly half the suit's rating.

### A note on the old Armor Rating

Before AOS, armor used a single **Armor Rating (AR)** number rather than five resists.
Our shard runs AOS/EJ rules, so resistances are what matter in play, but the underlying
`ArmorBase` value (the `ar=` column in the tables below) still feeds the pre-AOS armor
rating and the meditation penalty calculation, which is why a higher-AR plate piece
punishes mana regen more than a low-AR leather one.

## Materials

Materials run from soft cloth and leather up through metal mail and plate to exotic
dragon scale and gargish stone. Each row below is the **base resist profile of that
material's chest piece** with its Strength requirement, base armor rating, and meditation
allowance, taken straight from the per-piece source. Other slots in the same material
share the resist profile but carry lower Strength requirements and armor ratings.

| | Material | Phys | Fire | Cold | Poison | Energy | Str (chest) | AR | Medable | Crafted by |
|---|---|---|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x13CC.png" class="uo-sprite" alt="" width="48" /> | **Leather** | 2 | 4 | 3 | 3 | 3 | 25 | 13 | **All** | [Tailoring](/crafting/tailoring/) |
| <img src="/img/items/0x13DB.png" class="uo-sprite" alt="" width="48" /> | **Studded** | 2 | 4 | 3 | 3 | 4 | 35 | 16 | Half | [Tailoring](/crafting/tailoring/) |
| <img src="/img/items/0x144F.png" class="uo-sprite" alt="" width="48" /> | **Bone** | 3 | 3 | 4 | 2 | 4 | 60 | 30 | None | [Tailoring](/crafting/tailoring/) |
| <img src="/img/items/0x13EC.png" class="uo-sprite" alt="" width="48" /> | **Ringmail** | 3 | 3 | 1 | 5 | 3 | 40 | 22 | None | [Blacksmithy](/crafting/blacksmithy/) |
| <img src="/img/items/0x13BF.png" class="uo-sprite" alt="" width="48" /> | **Chainmail** | 4 | 4 | 4 | 1 | 2 | 60 | 28 | None | [Blacksmithy](/crafting/blacksmithy/) |
| <img src="/img/items/0x1415.png" class="uo-sprite" alt="" width="48" /> | **Plate** | 5 | 3 | 2 | 3 | 2 | 95 | 40 | None | [Blacksmithy](/crafting/blacksmithy/) |
| <img src="/img/items/0x2641.png" class="uo-sprite" alt="" width="48" /> | **Dragon scale** | 3 | 3 | 3 | 3 | 3 | 75 | 40 | None | [Blacksmithy](/crafting/blacksmithy/) |
| <img src="/img/items/0x2B67.png" class="uo-sprite" alt="" width="48" /> | **Woodland** | 5 | 3 | 2 | 3 | 2 | 95 | 40 | None | [Tailoring](/crafting/tailoring/) |
| <img src="/img/items/0x0286.png" class="uo-sprite" alt="" width="48" /> | **Stone (gargish)** | 6 | 6 | 4 | 8 | 6 | 40 | — | None | [Tailoring](/crafting/tailoring/) |

*Source: `Scripts/Items/Equipment/Armor/*.cs`, chest piece per material. Numbers are
base resists before resource, quality, and magic bonuses.*

Reading the table:

- **Cloth** is technically the lightest "armor" but standard cloth lives on the clothing
  layer (BaseClothing, not BaseArmor) and contributes almost nothing on its own — its
  value to mages is that it is fully medable and dyeable. Gargoyle "cloth" armor pieces
  are a special case: they look cloth but are mechanically **Leather** material in the
  source.
- **Leather** is the mage's and archer's friend: fully **medable** (no mana-regen
  penalty), lowest Strength requirement, balanced low resists. Barbed/horned/spined hides
  (see below) push its resists up significantly.
- **Studded** trades half its mana regen for slightly better physical/energy coverage.
- **Bone** is a tailored medium armor (crafted from bone) with even, mid-range resists
  and a hefty Strength cost.
- **Ringmail → Chainmail → Plate** are the blacksmith's metal line: rising armor rating
  and Strength requirement, no meditation allowed. Plate is the warrior's standard —
  highest base physical and armor rating.
- **Dragon scale** is the exotic outlier. Its base resists are a flat **3/3/3/3/3**, but
  scale armor's appeal is the high resists granted by **colored dragon scales** layered on
  top, plus its even spread — there are no weak elements to exploit.
- **Woodland** (elven) mirrors plate's profile but is **tailored** from wood/leather.
- **Stone** is the gargoyle heavyweight: the highest base resists on this list (and a
  notably high poison resist), reflecting its end-game material status.

### Crafting and hides

- **Tailoring** crafts leather, studded, bone, woodland, and gargish armor. The leather
  line scales with the hide used: ordinary leather → **spined** → **horned** → **barbed**,
  each a distinct `ArmorMaterialType` with progressively better resists and armor rating.
  See [Tailoring](/crafting/tailoring/) and [Resources](/items/resources/).
- **Blacksmithy** forges ringmail, chainmail, plate, and dragon-scale armor. The ore used
  (dull copper → valorite) adds resist and armor bonuses and a colored **hue**.


## Armor gallery

Every craftable armor piece on this shard, grouped by material (helm → gorget → chest → arms → gloves → legs). Sprites are the base client art; in play, the craft resource (ore or hide) recolors and boosts each piece. Browse with stats and item IDs in the [Armor catalog](/items/catalog/armor/).

### Leather

<div class="uo-gallery">
  <figure><img src="/img/items/0x782D.png" alt="Dragon Turtle Hide Helm" loading="lazy" /><figcaption>Dragon Turtle Hide Helm</figcaption></figure>
  <figure><img src="/img/items/0x7828.png" alt="Tiger Pelt Helm" loading="lazy" /><figcaption>Tiger Pelt Helm</figcaption></figure>
  <figure><img src="/img/items/0x1DB9.png" alt="leather cap" loading="lazy" /><figcaption>leather cap</figcaption></figure>
  <figure><img src="/img/items/0x2776.png" alt="leather jingasa" loading="lazy" /><figcaption>leather jingasa</figcaption></figure>
  <figure><img src="/img/items/0x278E.png" alt="leather ninja hood" loading="lazy" /><figcaption>leather ninja hood</figcaption></figure>
  <figure><img src="/img/items/0x7829.png" alt="Tiger Pelt Collar" loading="lazy" /><figcaption>Tiger Pelt Collar</figcaption></figure>
  <figure><img src="/img/items/0xA40F.png" alt="elegant collar" loading="lazy" /><figcaption>elegant collar</figcaption></figure>
  <figure><img src="/img/items/0xA40F.png" alt="elegant collar of fortune" loading="lazy" /><figcaption>elegant collar of fortune</figcaption></figure>
  <figure><img src="/img/items/0x2FC7.png" alt="leaf gorget" loading="lazy" /><figcaption>leaf gorget</figcaption></figure>
  <figure><img src="/img/items/0x13C7.png" alt="leather gorget" loading="lazy" /><figcaption>leather gorget</figcaption></figure>
  <figure><img src="/img/items/0x277A.png" alt="leather mempo" loading="lazy" /><figcaption>leather mempo</figcaption></figure>
  <figure><img src="/img/items/0x782B.png" alt="Dragon Turtle Hide Bustier" loading="lazy" /><figcaption>Dragon Turtle Hide Bustier</figcaption></figure>
  <figure><img src="/img/items/0x782A.png" alt="Dragon Turtle Hide Chest" loading="lazy" /><figcaption>Dragon Turtle Hide Chest</figcaption></figure>
  <figure><img src="/img/items/0x7823.png" alt="Tiger Pelt Bustier" loading="lazy" /><figcaption>Tiger Pelt Bustier</figcaption></figure>
  <figure><img src="/img/items/0x7822.png" alt="Tiger Pelt Chest" loading="lazy" /><figcaption>Tiger Pelt Chest</figcaption></figure>
  <figure><img src="/img/items/0x0405.png" alt="female gargish cloth chest armor" loading="lazy" /><figcaption>female gargish cloth chest armor</figcaption></figure>
  <figure><img src="/img/items/0x0303.png" alt="female gargish leather chest" loading="lazy" /><figcaption>female gargish leather chest</figcaption></figure>
  <figure><img src="/img/items/0x2FCB.png" alt="female leaf chest" loading="lazy" /><figcaption>female leaf chest</figcaption></figure>
  <figure><img src="/img/items/0x1C06.png" alt="female leather chest" loading="lazy" /><figcaption>female leather chest</figcaption></figure>
  <figure><img src="/img/items/0x0406.png" alt="gargish cloth chest armor" loading="lazy" /><figcaption>gargish cloth chest armor</figcaption></figure>
  <figure><img src="/img/items/0x0304.png" alt="gargish leather chest" loading="lazy" /><figcaption>gargish leather chest</figcaption></figure>
  <figure><img src="/img/items/0x2FC5.png" alt="leaf chest" loading="lazy" /><figcaption>leaf chest</figcaption></figure>
  <figure><img src="/img/items/0x13CC.png" alt="leather chest" loading="lazy" /><figcaption>leather chest</figcaption></figure>
  <figure><img src="/img/items/0x2793.png" alt="leather ninja jacket" loading="lazy" /><figcaption>leather ninja jacket</figcaption></figure>
  <figure><img src="/img/items/0x782E.png" alt="Dragon Turtle Hide Arms" loading="lazy" /><figcaption>Dragon Turtle Hide Arms</figcaption></figure>
  <figure><img src="/img/items/0x0403.png" alt="female gargish cloth arms armor" loading="lazy" /><figcaption>female gargish cloth arms armor</figcaption></figure>
  <figure><img src="/img/items/0x0301.png" alt="female gargish leather arms" loading="lazy" /><figcaption>female gargish leather arms</figcaption></figure>
  <figure><img src="/img/items/0x0404.png" alt="gargish cloth arms armor" loading="lazy" /><figcaption>gargish cloth arms armor</figcaption></figure>
  <figure><img src="/img/items/0x0302.png" alt="gargish leather arms" loading="lazy" /><figcaption>gargish leather arms</figcaption></figure>
  <figure><img src="/img/items/0x457E.png" alt="gargish leather wing armor" loading="lazy" /><figcaption>gargish leather wing armor</figcaption></figure>
  <figure><img src="/img/items/0x2FC8.png" alt="leaf arms" loading="lazy" /><figcaption>leaf arms</figcaption></figure>
  <figure><img src="/img/items/0x13CD.png" alt="leather arms" loading="lazy" /><figcaption>leather arms</figcaption></figure>
  <figure><img src="/img/items/0x1C0A.png" alt="leather bustier arms" loading="lazy" /><figcaption>leather bustier arms</figcaption></figure>
  <figure><img src="/img/items/0x277E.png" alt="leather hiro sode" loading="lazy" /><figcaption>leather hiro sode</figcaption></figure>
  <figure><img src="/img/items/0x2FC6.png" alt="leaf gloves" loading="lazy" /><figcaption>leaf gloves</figcaption></figure>
  <figure><img src="/img/items/0x13C6.png" alt="leather gloves" loading="lazy" /><figcaption>leather gloves</figcaption></figure>
  <figure><img src="/img/items/0x2792.png" alt="leather ninja mitts" loading="lazy" /><figcaption>leather ninja mitts</figcaption></figure>
  <figure><img src="/img/items/0x782C.png" alt="Dragon Turtle Hide Leggings" loading="lazy" /><figcaption>Dragon Turtle Hide Leggings</figcaption></figure>
  <figure><img src="/img/items/0x7824.png" alt="Tiger Pelt Leggings" loading="lazy" /><figcaption>Tiger Pelt Leggings</figcaption></figure>
  <figure><img src="/img/items/0x7826.png" alt="Tiger Pelt Long Skirt" loading="lazy" /><figcaption>Tiger Pelt Long Skirt</figcaption></figure>
  <figure><img src="/img/items/0x7825.png" alt="Tiger Pelt Shorts" loading="lazy" /><figcaption>Tiger Pelt Shorts</figcaption></figure>
  <figure><img src="/img/items/0x7827.png" alt="Tiger Pelt Skirt" loading="lazy" /><figcaption>Tiger Pelt Skirt</figcaption></figure>
  <figure><img src="/img/items/0x0407.png" alt="female gargish cloth kilt armor" loading="lazy" /><figcaption>female gargish cloth kilt armor</figcaption></figure>
  <figure><img src="/img/items/0x0409.png" alt="female gargish cloth legs armor" loading="lazy" /><figcaption>female gargish cloth legs armor</figcaption></figure>
  <figure><img src="/img/items/0x0310.png" alt="female gargish leather kilt" loading="lazy" /><figcaption>female gargish leather kilt</figcaption></figure>
  <figure><img src="/img/items/0x0305.png" alt="female gargish leather legs" loading="lazy" /><figcaption>female gargish leather legs</figcaption></figure>
  <figure><img src="/img/items/0x0408.png" alt="gargish cloth kilt armor" loading="lazy" /><figcaption>gargish cloth kilt armor</figcaption></figure>
  <figure><img src="/img/items/0x040A.png" alt="gargish cloth legs armor" loading="lazy" /><figcaption>gargish cloth legs armor</figcaption></figure>
  <figure><img src="/img/items/0x0311.png" alt="gargish leather kilt" loading="lazy" /><figcaption>gargish leather kilt</figcaption></figure>
  <figure><img src="/img/items/0x0305.png" alt="gargish leather legs" loading="lazy" /><figcaption>gargish leather legs</figcaption></figure>
  <figure><img src="/img/items/0x2FC9.png" alt="leaf legs" loading="lazy" /><figcaption>leaf legs</figcaption></figure>
  <figure><img src="/img/items/0x2FCA.png" alt="leaf tonlet" loading="lazy" /><figcaption>leaf tonlet</figcaption></figure>
  <figure><img src="/img/items/0x27C6.png" alt="leather do" loading="lazy" /><figcaption>leather do</figcaption></figure>
  <figure><img src="/img/items/0x278A.png" alt="leather haidate" loading="lazy" /><figcaption>leather haidate</figcaption></figure>
  <figure><img src="/img/items/0x13CB.png" alt="leather legs" loading="lazy" /><figcaption>leather legs</figcaption></figure>
  <figure><img src="/img/items/0x2791.png" alt="leather ninja pants" loading="lazy" /><figcaption>leather ninja pants</figcaption></figure>
  <figure><img src="/img/items/0x1C00.png" alt="leather shorts" loading="lazy" /><figcaption>leather shorts</figcaption></figure>
  <figure><img src="/img/items/0x1C08.png" alt="leather skirt" loading="lazy" /><figcaption>leather skirt</figcaption></figure>
  <figure><img src="/img/items/0x2786.png" alt="leather suneate" loading="lazy" /><figcaption>leather suneate</figcaption></figure>
</div>

### Studded

<div class="uo-gallery">
  <figure><img src="/img/items/0x2B76.png" alt="hide gorget" loading="lazy" /><figcaption>hide gorget</figcaption></figure>
  <figure><img src="/img/items/0x13D6.png" alt="studded gorget" loading="lazy" /><figcaption>studded gorget</figcaption></figure>
  <figure><img src="/img/items/0x279D.png" alt="studded mempo" loading="lazy" /><figcaption>studded mempo</figcaption></figure>
  <figure><img src="/img/items/0x1C02.png" alt="female studded chest" loading="lazy" /><figcaption>female studded chest</figcaption></figure>
  <figure><img src="/img/items/0x2B74.png" alt="hide chest" loading="lazy" /><figcaption>hide chest</figcaption></figure>
  <figure><img src="/img/items/0x2B79.png" alt="hide female chest" loading="lazy" /><figcaption>hide female chest</figcaption></figure>
  <figure><img src="/img/items/0x13DB.png" alt="studded chest" loading="lazy" /><figcaption>studded chest</figcaption></figure>
  <figure><img src="/img/items/0x2B77.png" alt="hide pauldrons" loading="lazy" /><figcaption>hide pauldrons</figcaption></figure>
  <figure><img src="/img/items/0x13DC.png" alt="studded arms" loading="lazy" /><figcaption>studded arms</figcaption></figure>
  <figure><img src="/img/items/0x1C0C.png" alt="studded bustier arms" loading="lazy" /><figcaption>studded bustier arms</figcaption></figure>
  <figure><img src="/img/items/0x277F.png" alt="studded hiro sode" loading="lazy" /><figcaption>studded hiro sode</figcaption></figure>
  <figure><img src="/img/items/0x2B75.png" alt="hide gloves" loading="lazy" /><figcaption>hide gloves</figcaption></figure>
  <figure><img src="/img/items/0x13D5.png" alt="studded gloves" loading="lazy" /><figcaption>studded gloves</figcaption></figure>
  <figure><img src="/img/items/0x2B78.png" alt="hide pants" loading="lazy" /><figcaption>hide pants</figcaption></figure>
  <figure><img src="/img/items/0x27C7.png" alt="studded do" loading="lazy" /><figcaption>studded do</figcaption></figure>
  <figure><img src="/img/items/0x278B.png" alt="studded haidate" loading="lazy" /><figcaption>studded haidate</figcaption></figure>
  <figure><img src="/img/items/0x13DA.png" alt="studded legs" loading="lazy" /><figcaption>studded legs</figcaption></figure>
  <figure><img src="/img/items/0x27D2.png" alt="studded suneate" loading="lazy" /><figcaption>studded suneate</figcaption></figure>
</div>

### Bone

<div class="uo-gallery">
  <figure><img src="/img/items/0x1F0B.png" alt="an evil orc helm" loading="lazy" /><figcaption>an evil orc helm</figcaption></figure>
  <figure><img src="/img/items/0x1451.png" alt="bone helm" loading="lazy" /><figcaption>bone helm</figcaption></figure>
  <figure><img src="/img/items/0x1F0B.png" alt="orc helm" loading="lazy" /><figcaption>orc helm</figcaption></figure>
  <figure><img src="/img/items/0x144F.png" alt="bone chest" loading="lazy" /><figcaption>bone chest</figcaption></figure>
  <figure><img src="/img/items/0x144E.png" alt="bone arms" loading="lazy" /><figcaption>bone arms</figcaption></figure>
  <figure><img src="/img/items/0x1450.png" alt="bone gloves" loading="lazy" /><figcaption>bone gloves</figcaption></figure>
  <figure><img src="/img/items/0x1452.png" alt="bone legs" loading="lazy" /><figcaption>bone legs</figcaption></figure>
</div>

### Ringmail

<div class="uo-gallery">
  <figure><img src="/img/items/0x13EC.png" alt="ringmail chest" loading="lazy" /><figcaption>ringmail chest</figcaption></figure>
  <figure><img src="/img/items/0x13EE.png" alt="ringmail arms" loading="lazy" /><figcaption>ringmail arms</figcaption></figure>
  <figure><img src="/img/items/0x13EB.png" alt="ringmail gloves" loading="lazy" /><figcaption>ringmail gloves</figcaption></figure>
  <figure><img src="/img/items/0x13F0.png" alt="ringmail legs" loading="lazy" /><figcaption>ringmail legs</figcaption></figure>
</div>

### Chainmail

<div class="uo-gallery">
  <figure><img src="/img/items/0x13BB.png" alt="chain coif" loading="lazy" /><figcaption>chain coif</figcaption></figure>
  <figure><img src="/img/items/0x2774.png" alt="chain hatsuburi" loading="lazy" /><figcaption>chain hatsuburi</figcaption></figure>
  <figure><img src="/img/items/0x13BF.png" alt="chain chest" loading="lazy" /><figcaption>chain chest</figcaption></figure>
  <figure><img src="/img/items/0x13BE.png" alt="chain legs" loading="lazy" /><figcaption>chain legs</figcaption></figure>
</div>

### Plate

<div class="uo-gallery">
  <figure><img src="/img/items/0x140C.png" alt="bascinet" loading="lazy" /><figcaption>bascinet</figcaption></figure>
  <figure><img src="/img/items/0x2B6E.png" alt="circlet" loading="lazy" /><figcaption>circlet</figcaption></figure>
  <figure><img src="/img/items/0x1408.png" alt="close helm" loading="lazy" /><figcaption>close helm</figcaption></figure>
  <figure><img src="/img/items/0x2778.png" alt="decorative plate kabuto" loading="lazy" /><figcaption>decorative plate kabuto</figcaption></figure>
  <figure><img src="/img/items/0x2B70.png" alt="gemmed circlet" loading="lazy" /><figcaption>gemmed circlet</figcaption></figure>
  <figure><img src="/img/items/0x2777.png" alt="heavy plate jingasa" loading="lazy" /><figcaption>heavy plate jingasa</figcaption></figure>
  <figure><img src="/img/items/0x140A.png" alt="helmet" loading="lazy" /><figcaption>helmet</figcaption></figure>
  <figure><img src="/img/items/0x2781.png" alt="light plate jingasa" loading="lazy" /><figcaption>light plate jingasa</figcaption></figure>
  <figure><img src="/img/items/0x140E.png" alt="norse helm" loading="lazy" /><figcaption>norse helm</figcaption></figure>
  <figure><img src="/img/items/0x2785.png" alt="plate battle kabuto" loading="lazy" /><figcaption>plate battle kabuto</figcaption></figure>
  <figure><img src="/img/items/0x2775.png" alt="plate hatsuburi" loading="lazy" /><figcaption>plate hatsuburi</figcaption></figure>
  <figure><img src="/img/items/0x1412.png" alt="plate helm" loading="lazy" /><figcaption>plate helm</figcaption></figure>
  <figure><img src="/img/items/0x2B71.png" alt="raven helm" loading="lazy" /><figcaption>raven helm</figcaption></figure>
  <figure><img src="/img/items/0x2B6F.png" alt="royal circlet" loading="lazy" /><figcaption>royal circlet</figcaption></figure>
  <figure><img src="/img/items/0x2784.png" alt="small plate jingasa" loading="lazy" /><figcaption>small plate jingasa</figcaption></figure>
  <figure><img src="/img/items/0x2789.png" alt="standard plate kabuto" loading="lazy" /><figcaption>standard plate kabuto</figcaption></figure>
  <figure><img src="/img/items/0x2B72.png" alt="vulture helm" loading="lazy" /><figcaption>vulture helm</figcaption></figure>
  <figure><img src="/img/items/0x2B73.png" alt="winged helm" loading="lazy" /><figcaption>winged helm</figcaption></figure>
  <figure><img src="/img/items/0x1413.png" alt="plate gorget" loading="lazy" /><figcaption>plate gorget</figcaption></figure>
  <figure><img src="/img/items/0x2779.png" alt="plate mempo" loading="lazy" /><figcaption>plate mempo</figcaption></figure>
  <figure><img src="/img/items/0x0309.png" alt="female gargish plate chest" loading="lazy" /><figcaption>female gargish plate chest</figcaption></figure>
  <figure><img src="/img/items/0x1C04.png" alt="female plate chest" loading="lazy" /><figcaption>female plate chest</figcaption></figure>
  <figure><img src="/img/items/0x030A.png" alt="gargish plate chest" loading="lazy" /><figcaption>gargish plate chest</figcaption></figure>
  <figure><img src="/img/items/0x1415.png" alt="plate chest" loading="lazy" /><figcaption>plate chest</figcaption></figure>
  <figure><img src="/img/items/0x0307.png" alt="female gargish plate arms" loading="lazy" /><figcaption>female gargish plate arms</figcaption></figure>
  <figure><img src="/img/items/0x0308.png" alt="gargish plate arms" loading="lazy" /><figcaption>gargish plate arms</figcaption></figure>
  <figure><img src="/img/items/0x1410.png" alt="plate arms" loading="lazy" /><figcaption>plate arms</figcaption></figure>
  <figure><img src="/img/items/0x2780.png" alt="plate hiro sode" loading="lazy" /><figcaption>plate hiro sode</figcaption></figure>
  <figure><img src="/img/items/0x1414.png" alt="plate gloves" loading="lazy" /><figcaption>plate gloves</figcaption></figure>
  <figure><img src="/img/items/0x030B.png" alt="female gargish plate kilt" loading="lazy" /><figcaption>female gargish plate kilt</figcaption></figure>
  <figure><img src="/img/items/0x030D.png" alt="female gargish plate legs" loading="lazy" /><figcaption>female gargish plate legs</figcaption></figure>
  <figure><img src="/img/items/0x030C.png" alt="gargish plate kilt" loading="lazy" /><figcaption>gargish plate kilt</figcaption></figure>
  <figure><img src="/img/items/0x030E.png" alt="gargish plate legs" loading="lazy" /><figcaption>gargish plate legs</figcaption></figure>
  <figure><img src="/img/items/0x277D.png" alt="plate do" loading="lazy" /><figcaption>plate do</figcaption></figure>
  <figure><img src="/img/items/0x278D.png" alt="plate haidate" loading="lazy" /><figcaption>plate haidate</figcaption></figure>
  <figure><img src="/img/items/0x1411.png" alt="plate legs" loading="lazy" /><figcaption>plate legs</figcaption></figure>
  <figure><img src="/img/items/0x2788.png" alt="plate suneate" loading="lazy" /><figcaption>plate suneate</figcaption></figure>
</div>

### Dragon scale

<div class="uo-gallery">
  <figure><img src="/img/items/0x2645.png" alt="dragon helm" loading="lazy" /><figcaption>dragon helm</figcaption></figure>
  <figure><img src="/img/items/0x2641.png" alt="dragon chest" loading="lazy" /><figcaption>dragon chest</figcaption></figure>
  <figure><img src="/img/items/0x2657.png" alt="dragon arms" loading="lazy" /><figcaption>dragon arms</figcaption></figure>
  <figure><img src="/img/items/0x2643.png" alt="dragon gloves" loading="lazy" /><figcaption>dragon gloves</figcaption></figure>
  <figure><img src="/img/items/0x2647.png" alt="dragon legs" loading="lazy" /><figcaption>dragon legs</figcaption></figure>
</div>

### Woodland (elven)

<div class="uo-gallery">
  <figure><img src="/img/items/0x2B69.png" alt="woodland gorget" loading="lazy" /><figcaption>woodland gorget</figcaption></figure>
  <figure><img src="/img/items/0x2B6D.png" alt="female elven plate chest" loading="lazy" /><figcaption>female elven plate chest</figcaption></figure>
  <figure><img src="/img/items/0x2B67.png" alt="woodland chest" loading="lazy" /><figcaption>woodland chest</figcaption></figure>
  <figure><img src="/img/items/0x2B6C.png" alt="woodland arms" loading="lazy" /><figcaption>woodland arms</figcaption></figure>
  <figure><img src="/img/items/0x2B6A.png" alt="woodland gloves" loading="lazy" /><figcaption>woodland gloves</figcaption></figure>
  <figure><img src="/img/items/0x2B6B.png" alt="woodland legs" loading="lazy" /><figcaption>woodland legs</figcaption></figure>
</div>

### Stone (gargish)

<div class="uo-gallery">
  <figure><img src="/img/items/0x0285.png" alt="female gargish stone chest" loading="lazy" /><figcaption>female gargish stone chest</figcaption></figure>
  <figure><img src="/img/items/0x0286.png" alt="gargish stone chest" loading="lazy" /><figcaption>gargish stone chest</figcaption></figure>
  <figure><img src="/img/items/0x0283.png" alt="female gargish stone arms" loading="lazy" /><figcaption>female gargish stone arms</figcaption></figure>
  <figure><img src="/img/items/0x0284.png" alt="gargish stone arms" loading="lazy" /><figcaption>gargish stone arms</figcaption></figure>
  <figure><img src="/img/items/0x0287.png" alt="female gargish stone kilt" loading="lazy" /><figcaption>female gargish stone kilt</figcaption></figure>
  <figure><img src="/img/items/0x0289.png" alt="female gargish stone legs" loading="lazy" /><figcaption>female gargish stone legs</figcaption></figure>
  <figure><img src="/img/items/0x0288.png" alt="gargish stone kilt" loading="lazy" /><figcaption>gargish stone kilt</figcaption></figure>
  <figure><img src="/img/items/0x028A.png" alt="gargish stone legs" loading="lazy" /><figcaption>gargish stone legs</figcaption></figure>
</div>

## Quality, magic properties & durability

Like weapons, armor carries **quality**, optional **magic tiers**, and **durability** on top
of its base resists.

- **Quality** — **exceptional** armor rolls higher resists than normal, can carry the
  crafter's maker's mark, and gains extra resist points from the crafter's
  [Arms Lore](/skills/arms-lore/) (`ArmsLore / 20`, **+5 at GM**, spread randomly across the
  five types).
- **Protection tier (resist prefix)** — magic armor's defensive tier shows in its name
  (`ArmorEnums.cs`): **Defense → Guarding (+1) → Hardening (+2) → Fortification (+3) →
  Invulnerability (+4)**, adding to the piece's protection.
- **Durability tier** — the same ladder as weapons: **Durable +20%, Substantial +50%, Massive
  +70%, Fortified +100%, Indestructible +120%** maximum durability.
- **AOS attributes** — looted and **runic-crafted** armor (kits from
  [Bulk Order Deeds](/mechanics/bulk-order-deeds/)) can also roll resist bonuses, **Mage
  Armor**, **Lower Mana Cost**, regeneration, **Self Repair**, and more.
- **Durability & repair** — each piece has current / maximum hit points; it wears as you take
  hits, and **repairing** (with the crafting skill that made it, or a repair contract)
  restores current durability while slowly lowering the maximum, so armor wears out over time.
  **Powder of Fortifying** can raise the maximum back up.

## Shields

Shields occupy the off-hand (two-handed) slot and are governed by the
[Parrying](/skills/parrying/) skill, which gives a chance to **block an incoming melee or
ranged hit outright**. The block rate scales with Parrying skill and the shield equipped —
heavier shields block more but weigh more and demand more Strength.

Shield types run from the light **buckler** through wooden and bronze shields up to the
**heavy metal** and **kite** shields, plus order/chaos and gargish variants. All metal
shields default to **Plate** material and, like plate armor, count as **non-medable** —
though on AOS/EJ rules a shield does **not** add to the meditation/mana penalty (only the
six body slots do; `RegenRates.GetArmorOffset` skips the shield under AOS). A mage who
wants to parry will still prefer a **Spell Channeling** shield to keep casting.

Browse every shield with art in the [Shields catalog](/items/catalog/shields/), and see
[Parrying](/skills/parrying/) for block-chance details.

## Suits & strategy

Assembling a suit is about **maximising resists under the 70% cap** across all five types,
on top of the armor and mana-regen profile your character can afford.

- **Balanced suit** — aim for the highest minimum resist rather than spiking one. A
  monster's damage type decides which resist matters; a balanced 60s-across-the-board suit
  survives more encounters than a 70-physical / 20-energy one. Because resists add across
  slots, fill **every slot** before chasing higher per-piece numbers.
- **The mage tradeoff** — metal armor blocks meditation, so casters historically wore all
  leather/cloth and accepted lower physical resist. The **Mage Armor** property breaks the
  rule: it lets a mage wear high-resist non-medable armor (even plate) with no mana-regen
  penalty. Weigh resist coverage against Strength requirement and mana regen for your
  template — see [Meditation & Mana](/playing/meditation-and-mana/) and the seven-GM mage
  build in [Seven GM templates](/templates/seven-gm/).
- **Colored armor from resources** — crafting with better ore or hide both raises resists
  *and* recolors the armor; the hue tells everyone the material at a glance. Dull copper,
  shadow iron, copper, bronze, gold, agapite, verite, and valorite each add increasing
  armor and a distinct color (see the [Hue Reference](/reference/hues/)). Exceptional
  quality from a skilled crafter adds further durability and resist.
- **Gargish & elven variants** — gargoyle characters use **gargish** plate/stone/leather
  pieces (and cannot wear human-shaped helms); elves use **woodland** armor. They share
  the underlying material mechanics but have race restrictions, so build the suit for the
  race you play.

For training the skills that make a suit worth wearing, see
[Tactics](/skills/tactics/), [Parrying](/skills/parrying/), and the
[Seven-GM templates](/templates/seven-gm/). To browse specific pieces with art and item
IDs, see the [Armor catalog](/items/catalog/armor/) and
[Shields catalog](/items/catalog/shields/).
