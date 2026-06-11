---
title: Tools
description: Trade and utility tools — what each tinker, smith, tailor, carpenter, scribe, and gathering tool does, which skill it serves, how many uses it has, and where to get it.
status: source-verified
sources:
  - "servuo: Scripts/Items/Tools/BaseTool.cs"
  - "servuo: Scripts/Items/Tools/BaseHarvestTool.cs"
  - "servuo: Scripts/Items/Tools (TinkerTools, SmithHammer, Tongs, SewingKit, Scissors, Saw, DovetailSaw, MouldingPlane, JointingPlane, DrawKnife, Froe, Inshave, FletcherTools, ScribesPen, MortarPestle, Skillet, FlourSifter, RollingPin, MapmakersPen, Shovel, FishingPole)"
  - "servuo: Scripts/Items/Equipment/Weapons/Pickaxe.cs, Hatchet.cs, Axe.cs"
  - "servuo: Scripts/Items/Consumables/LockPick.cs"
  - "servuo: Scripts/Services/Craft/DefTinkering.cs (craft recipes + skill ranges)"
  - "client: artLegacyMUL.uop"
last_verified: 2026-06-11
generated: false
---

A tool is a consumable item with a limited number of **uses**. Double-click most tools to
open a **craft menu** (a gump listing everything that tool can make at your skill); other
tools fire a one-shot action when you double-click them and then target the world — a
pickaxe at a rock, a fishing pole at water. Either way, every successful use chips away at
the tool's durability, and when its **uses remaining** hit zero the tool crumbles and you
reach for the next one.

Almost every metal tool in this list is made by a tinker — [Tinkering](/skills/tinkering/)
turns iron ingots (and, for a few wooden tools, boards) into the whole toolkit of Britannia.
The rest are bought from town vendors. See [Crafting](/playing/crafting/) for how craft
gumps work and [Targeting](/playing/targeting/) for the point-and-click step the gathering
tools use.

A few facts that hold for the whole family, straight from `Scripts/Items/Tools/BaseTool.cs`:

- A freshly **tinker-made** metal tool starts with a *random* 25–75 uses
  (`BaseTool(int itemID) : this(Utility.RandomMinMax(25, 75), itemID)`) — exceptional
  craftsmanship and higher-grade ingots scale that number up.
- A tool's quality and uses ride on the maker, not the menu: a better tinker makes a
  longer-lasting tool.
- Tools are **not** soulbound — you can stockpile them, sell them, or hand a fresh sewing
  kit to a guildmate mid-session.

## Crafting tools

These open a craft gump for their trade. Unless noted, each is forged by a tinker from iron
ingots; the skill range in parentheses is the Tinkering skill where you can *first* attempt
to *last* guarantee the recipe (from `DefTinkering.cs`). You can also just buy them from the
matching NPC vendor — see [Vendors & banking](/playing/vendors-and-banking/).

### Tinker's Tools — [Tinkering](/skills/tinkering/)

<img src="/img/items/0x1EB8.png" class="uo-sprite" alt="" width="56" />

The tinker's own kit. Double-click to open the Tinkering menu and build clocks, traps, keys,
tools (including more tinker's tools), jewelry, and a wide spread of small metal goods.
Tinker-made from 2 iron ingots at **Tinkering 10.0–60.0**. Sold by tinker NPCs. Uses default
to the 25–75 range.

### Smith's Hammer & Tongs — [Blacksmithy](/skills/blacksmithy/)

<img src="/img/items/0x13E3.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0FBB.png" class="uo-sprite" alt="" width="56" />

A **smith's hammer** opens the Blacksmithy menu at a forge to hammer ingots into weapons and
armor (`CraftSystem => DefBlacksmithy.CraftSystem`). **Tongs** belong to the same trade and
are the tool used to convert ore into the in-hand state and handle the forge work.
Tinker-made — hammer from 4 ingots at **Tinkering 40.0–90.0**, tongs from 1 ingot at
**35.0–85.0** — or bought from blacksmith and tinker vendors. (Under AOS the craftable hammer
class is `SmithyHammer`; the older `SmithHammer` art is `0x13E3`.)

### Sewing Kit & Scissors — [Tailoring](/skills/tailoring/)

<img src="/img/items/0x0F9D.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F9F.png" class="uo-sprite" alt="" width="56" />

A **sewing kit** opens the Tailoring menu to stitch cloth and leather into clothing and light
armor (`DefTailoring.CraftSystem`). **Scissors** double as a tailoring tool *and* the
all-purpose cutting implement: cut **bolts of cloth into cloth, cloth into bandages, and
hides into leather** (see [Resources](/items/resources/)). Scissors are special-cased to a
fixed **50 uses** (`m_UsesRemaining = 50` in `Scissors.cs`), not the random 25–75 default.
Both are tinker-made (sewing kit: 2 ingots at **10.0–70.0**; scissors: 2 ingots at
**5.0–55.0**) or bought from tailor and provisioner vendors.

### Carpentry tools — [Carpentry](/skills/carpentry/)

<img src="/img/items/0x1034.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1028.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x102C.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1030.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E4.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E5.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E6.png" class="uo-sprite" alt="" width="56" />

The carpenter carries a small arsenal, and **any one of them opens the same Carpentry menu**
(every class returns `DefCarpentry.CraftSystem`): the **saw**, **dovetail saw**, **moulding
plane**, **jointing plane**, **smoothing plane**, **draw knife**, **froe**, and **inshave**.
They differ only in art and recipe cost — pick whichever your tinker handed you and build
furniture, instruments, bows, and house add-ons from boards. The metal-bladed ones (saw,
dovetail saw, draw knife, froe, inshave) are tinker-made from iron at **Tinkering 30.0–80.0**;
the wooden planes and jointing/moulding planes are tinker-made from **boards** at **0.0–50.0**.
All are sold by carpenter and tinker NPCs.

### Fletcher's Tools — [Bowcraft & Fletching](/skills/bowcraft-fletching/)

<img src="/img/items/0x1022.png" class="uo-sprite" alt="" width="56" />

Opens the Bowcraft menu (`DefBowFletching.CraftSystem`) to fashion bows, crossbows, arrows,
and bolts from boards and feathers. Tinker-made from 3 ingots at **Tinkering 35.0–85.0**, or
bought from bowyer/fletcher vendors.

### Scribe's Pen — [Inscription](/skills/inscription/)

<img src="/img/items/0x0FBF.png" class="uo-sprite" alt="" width="56" />

Opens the Inscription menu (`DefInscription.CraftSystem`) to scribe spell scrolls and books
(reagents + a blank scroll). Tinker-made from 1 ingot at **Tinkering 25.0–75.0**, or bought
from scribe and mage vendors. Shares art `0x0FBF` with the mapmaker's pen.

### Mortar & Pestle — [Alchemy](/skills/alchemy/)

<img src="/img/items/0x0E9B.png" class="uo-sprite" alt="" width="56" />

Opens the Alchemy menu (`DefAlchemy.CraftSystem`) to grind reagents into potions. Tinker-made
from 3 ingots at **Tinkering 20.0–70.0**, or bought from alchemist and mage vendors. (It is
also the targeting tool used to pound reagents in some quest steps.) See
[Alchemy](/skills/alchemy/).

### Cooking tools — [Cooking](/skills/cooking/)

<img src="/img/items/0x097F.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x103E.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1043.png" class="uo-sprite" alt="" width="56" />

The **skillet**, **flour sifter**, and **rolling pin** each open the Cooking menu
(`DefCooking.CraftSystem`) — in practice you reach for whichever recipe a dish needs (sifting
flour, rolling dough, frying). Tinker-made: skillet (4 ingots, **30.0–80.0**), flour sifter
(3 ingots, **50.0–100.0**), rolling pin (5 **boards**, **0.0–50.0**). Bought from cook,
baker, and provisioner vendors.

### Mapmaker's Pen — [Cartography](/skills/cartography/)

<img src="/img/items/0x0FBF.png" class="uo-sprite" alt="" width="56" />

Opens the Cartography menu (`DefCartography.CraftSystem`) to draw blank maps and pinpoint
treasure-map locations. Tinker-made from 1 ingot at **Tinkering 25.0–75.0**, or bought from
mapmaker/scribe vendors. Same art as the scribe's pen (`0x0FBF`).

## Gathering tools

These don't open a menu — double-click, then **target** the resource node (see
[Gathering resources](/playing/gathering-resources/)). They serve the harvest skills rather
than a craft system.

### Pickaxe & Shovel — [Mining](/skills/mining/)

<img src="/img/items/0x0E86.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F39.png" class="uo-sprite" alt="" width="56" />

Both run the Mining harvest (`HarvestSystem => Mining.System`). A **pickaxe** is the
versatile miner's tool — it works veins and harvests ore in caves and against mountainsides,
and because it derives from `BaseAxe` it is also a usable (weak) weapon; it starts with a
fixed **50 uses** (`UsesRemaining = 50` in `Pickaxe.cs`). A **shovel** digs ore and is the
tool of choice for the cleaner "dig at the ground" workflow; it too defaults to **50 uses**
(`Shovel() : this(50)`). What you pull from the rock — iron through valorite, plus granite,
sand, and gems — is on the [Resources](/items/resources/) page. Pickaxes are tinker/blacksmith
goods; shovels are tinker-made from 4 ingots at **Tinkering 40.0–90.0** and sold by miners
and provisioners.

### Hatchet & Axe — [Lumberjacking](/skills/lumberjacking/)

<img src="/img/items/0x0F43.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F49.png" class="uo-sprite" alt="" width="56" />

Any axe-type weapon (**hatchet**, **axe**, battle axe, etc. — all derive from `BaseAxe`) does
double duty: swing it at a tree to chop **logs** for [Lumberjacking](/skills/lumberjacking/),
then use it to cut logs into **boards**, and carry it as a real melee weapon besides. Made by
blacksmiths and sold by weapon/provisioner vendors. Yields and the log→board table are on
[Resources](/items/resources/).

### Fishing Pole — [Fishing](/skills/fishing/)

<img src="/img/items/0x0DC0.png" class="uo-sprite" alt="" width="56" />

Double-click and target water to fish (`FishingPole` runs the Fishing harvest). It is also an
equippable one-handed item and is itself craftable (Bowcraft/Carpentry from wood). A standard
pole starts with **150 uses** (`UsesRemaining = 150` in `FishingPole.cs`) — far more than a
metal tool, since fishing is a long grind. Sold by fishmonger and provisioner vendors. See
[Fishing](/skills/fishing/).

## Utility tools

Smaller one-job items that aren't tied to a craft gump:

- **Lockpicks** <img src="/img/items/0x14FC.png" class="uo-sprite" alt="" width="56" /> —
  double-click, target a locked chest or door, and pit your
  [Lockpicking](/skills/lockpicking/) skill against the lock's level; a failed pick on a hard
  lock can break. Unlike the menu tools, lockpicks are a **stackable consumable** (`Amount`,
  not per-tool uses — `LockPick.cs`). Tinker-made from 1 ingot at **Tinkering 45.0–95.0**, or
  bought from thief/tinker vendors.
- **Keys & key rings** — tinkers craft keys (and the locks they fit) for chests and houses; a
  key ring holds a bundle of them. Made at the Tinkering menu (`Key` from 3 ingots,
  **20.0–70.0**).
- **Tinker traps** — the Tinkering menu also builds trappable containers (dart, poison, and
  explosion traps) for guarding loot. See [Tinkering](/skills/tinkering/) and
  [Crafting → Tinkering](/crafting/tinkering/).
- **Dye tubs** <img src="/img/items/0x0FAB.png" class="uo-sprite" alt="" width="56" /> —
  not a craft tool but a colouring utility: drop cloth or an item in, pick a hue, and dye it.
  The colour space is the [Hue Reference](/reference/hues/).

## Quick reference

Skill ranges are the Tinkering skill to first attempt → last guarantee the recipe
(`DefTinkering.cs`). "Random 25–75" is the `BaseTool` default for a tinker-made tool.

| Tool | Skill served | What it does | Uses | How to get |
|------|--------------|--------------|------|------------|
| Tinker's Tools | [Tinkering](/skills/tinkering/) | Opens Tinkering menu | random 25–75 | Tinker (10–60) or tinker vendor |
| Smith's Hammer | [Blacksmithy](/skills/blacksmithy/) | Smith weapons & armor at a forge | random 25–75 | Tinker (40–90) or smith vendor |
| Tongs | [Blacksmithy](/skills/blacksmithy/) | Forge / ore handling | random 25–75 | Tinker (35–85) or smith vendor |
| Sewing Kit | [Tailoring](/skills/tailoring/) | Opens Tailoring menu | random 25–75 | Tinker (10–70) or tailor vendor |
| Scissors | [Tailoring](/skills/tailoring/) | Tailoring menu; cut cloth/bolts/hides | **50** | Tinker (5–55) or tailor vendor |
| Saw / Dovetail Saw | [Carpentry](/skills/carpentry/) | Opens Carpentry menu | random 25–75 | Tinker (30–80) or carpenter vendor |
| Moulding/Jointing/Smoothing Plane | [Carpentry](/skills/carpentry/) | Opens Carpentry menu | random 25–75 | Tinker from **boards** (0–50) or carpenter vendor |
| Draw Knife / Froe / Inshave | [Carpentry](/skills/carpentry/) | Opens Carpentry menu | random 25–75 | Tinker (30–80) or carpenter vendor |
| Fletcher's Tools | [Bowcraft](/skills/bowcraft-fletching/) | Opens Bowcraft menu | random 25–75 | Tinker (35–85) or bowyer vendor |
| Scribe's Pen | [Inscription](/skills/inscription/) | Opens Inscription menu | random 25–75 | Tinker (25–75) or scribe vendor |
| Mortar & Pestle | [Alchemy](/skills/alchemy/) | Opens Alchemy menu | random 25–75 | Tinker (20–70) or alchemist vendor |
| Skillet / Flour Sifter / Rolling Pin | [Cooking](/skills/cooking/) | Opens Cooking menu | random 25–75 | Tinker (skillet 30–80, sifter 50–100, pin boards 0–50) or cook vendor |
| Mapmaker's Pen | [Cartography](/skills/cartography/) | Opens Cartography menu | random 25–75 | Tinker (25–75) or mapmaker vendor |
| Pickaxe | [Mining](/skills/mining/) | Mine ore (also a weak axe-weapon) | **50** | Tinker/smith or provisioner |
| Shovel | [Mining](/skills/mining/) | Dig ore | **50** | Tinker (40–90) or provisioner |
| Hatchet / Axe | [Lumberjacking](/skills/lumberjacking/) | Chop logs, cut boards (also a weapon) | weapon durability | Smith or weapon vendor |
| Fishing Pole | [Fishing](/skills/fishing/) | Fish (target water) | **150** | Fisher/provisioner vendor or craft |
| Lockpicks | [Lockpicking](/skills/lockpicking/) | Pick locked chests/doors | stackable (consumed) | Tinker (45–95) or thief vendor |
| Keys / Key Rings | — | Lock/unlock chests & houses | n/a | Tinker (key 20–70) |
| Dye Tub | — | Recolour cloth/items by [hue](/reference/hues/) | reusable | Tinker vendor / reward |

## See also

- [Tinkering](/skills/tinkering/) — the skill that makes most of these · [Crafting overview](/crafting/) · [How crafting menus work](/playing/crafting/)
- [Gathering resources](/playing/gathering-resources/) · [Resources](/items/resources/) — what the gathering tools pull from the world
- [Vendors & banking](/playing/vendors-and-banking/) — where to buy tools · [Targeting](/playing/targeting/)
- [Tools catalog](/items/catalog/tools/) — every tool item in the source, with art and item IDs · [Items overview](/items/)
