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
last_verified: 2026-06-11
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
