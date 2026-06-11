---
title: Plants & Gardening
description: How the ServUO plant system works — grow decorative and useful plants from seeds in a bowl of dirt, water them daily through the growth stages (seed, sapling, plant, full-grown, decorative), keep them healthy against infestation, fungus, poison and disease, cross-pollinate for rare colours, and harvest seeds, clippings, resources and plant pigments.
status: source-verified
sources:
  - "servuo: Scripts/Services/Plants/PlantItem.cs (PlantStatus growth stages, watering, planting, decorative)"
  - "servuo: Scripts/Services/Plants/PlantSystem.cs (growth check, water, maladies, potions, fertile dirt, pollination)"
  - "servuo: Scripts/Services/Plants/PlantType.cs (44 plant types, categories, crossable/reproduces)"
  - "servuo: Scripts/Services/Plants/PlantHue.cs (19 plant hues, bright/rare, cross-breeding rules)"
  - "servuo: Scripts/Services/Plants/PlantResources.cs (plant resource yields)"
  - "servuo: Scripts/Services/Plants/MainPlantGump.cs (gardening UI gump)"
  - "servuo: Scripts/Services/BasketWeaving/PlantPigment.cs (plant pigments)"
  - "servuo: Scripts/Mobiles/NPCs/Naturalist.cs (Study of Solen seed reward)"
  - "client art: artLegacyMUL.uop (plant item sprites)"
last_verified: 2026-06-11
generated: false
---

**Gardening** is a self-contained mini-game in Ultima Online: you plant a seed in a bowl
of dirt, water it once a day, and over about a week it grows into a plant you can keep as a
decoration or harvest for useful materials. It needs no skill points and no combat — just
patience and attention. People grow plants for **rare coloured varieties** (prized for
[house decorating](/playing/decorating/) and resale), for **plant resources** used in
crafting, for **plant pigments** that dye items, and simply as a relaxing collection game:
there are 44 plant types and 19 colours to chase, many of them obtainable only by careful
**cross-pollination**.

All numbers and behaviour below come from the ServUO server-emulator's plant scripts under
`Scripts/Services/Plants/` (cited per section). Structured data lives in `data/plants.json`,
extracted by `tools/extract_plants.py`.

## How to grow a plant

The growth loop is:

1. **Get a seed.** Seeds come from full-grown plants you already own (see
   [What plants give you](#what-plants-give-you)), from monster/treasure drops, and as a
   quest reward from the **Naturalist** (see below). A seed records a plant **type** and a
   **hue**.
2. **Prepare a bowl of dirt.** A fresh plant bowl starts at the `BowlOfDirt` stage
   (`Scripts/Services/Plants/PlantItem.cs`). Pour **water** on it until the dirt softens —
   the dirt must be at least lightly watered (`Water >= 2`) before a seed will take, or you
   get *"The dirt needs to be softened first."*
3. **Plant the seed** on the prepared soil. The bowl advances to the `Seed` stage and now
   holds your chosen type and hue.
4. **Water it daily.** Pour a beverage containing **water** on it. The water level runs
   **0–4** and the plant wants to sit at exactly **2** (`PlantSystem.cs`). Each daily growth
   check the soil dries out by one, so a splash of water a day keeps it healthy. Too much
   *or* too little water damages the plant.
5. **Let it grow.** Once a day (the growth check runs on a **23-hour** timer,
   `PlantSystem.CheckDelay`, and is also re-checked when you log in or the world saves), a
   healthy plant advances one stage.

The plant must be in your **backpack, bank box, or locked down** in your house for the
growth check to count (`ValidGrowthLocation` in `PlantItem.cs`). You interact with it by
**double-clicking** it, which opens the gardening gump.

### Growth stages

The plant climbs through these stages (`enum PlantStatus`, `PlantItem.cs`). Internally the
growth check counts stages 1–9; the labelled states the client shows are:

| Stage | `PlantStatus` | What it looks like |
|------:|---------------|--------------------|
| 0 | `BowlOfDirt` | An empty bowl. Soften with water, then plant a seed. |
| 1 | `Seed` | A seed is in the dirt; it will sprout. |
| 2–3 | `Sapling` | A young sapling, still growing each day. |
| 4–6 | `Plant` | A recognisable plant; the bowl turns green. |
| 7–9 | `FullGrownPlant` | Fully grown — shows its type and colour, can pollinate, and yields seeds/resources. |
| 10 | `DecorativePlant` | "Set to decorative": a finished houseplant. No more watering needed. |
| 11 | `DeadTwigs` | Neglected to death — only twigs remain. |

Once a plant reaches **full-grown** you can leave it producing seeds/resources, or **set it
to decorative** (`SetToDecorativeGump.cs`) — a one-way step that turns it into a permanent
ornament that no longer needs care and can be placed in a house.

### The gardening gump

Double-clicking a growing plant opens the main gardening interface
(`MainPlantGump.cs`). It shows the plant's art in the centre and a panel of controls: the
**reproduction** menu, the four **maladies** (infestation, fungus, poison, disease) with
their current levels, the **water** level, the four **potion** slots (poison/cure/heal/
strength), a growth-stage indicator, a help button, and an "empty the bowl" button. The
panel is built from a generic dark frame (gump `0xE10`) plus item-art tiles rather than one
bespoke picture.

The plant sprites below are rendered straight from the client art for the item IDs in
`data/plants.json`:

![A montage of example plant types: campion flowers, poppies, lilies, fern, ponytail palm, century plant, barrel and tribarrel cactus, bonsai, cocoa tree and sugar canes](/img/plants/montage.png)

## Keeping it healthy

A plant has **hits** (a health pool) and a `Health` rating of **Dying / Wilted / Healthy /
Vibrant**. A plant only *grows* when it is at least **Healthy** (`PlantSystem.Grow`), so
keeping it well is the whole job. Health is threatened by four **maladies** and by wrong
watering (all in `Scripts/Services/Plants/PlantSystem.cs`):

| Hazard | What causes it | How you treat it |
|--------|----------------|------------------|
| **Infestation** | Random each day (more likely on **flowery** and **bright**-hued plants, and when over-watered). | Pour a **greater poison potion** on the plant. |
| **Fungus** | Random each day (more likely when over-watered). | Pour a **greater cure potion**. |
| **Poison** | Caused by over-applying poison potion (it carries over). | Pour a **greater heal potion**. |
| **Disease** | Caused by over-applying cure potion (it carries over). | Pour a **greater heal potion**. |

Each malady runs **0–2**. Only the **greater** potions work — lesser/regular potions give
*"This potion is not powerful enough"* (`PlantItem.ApplyPotion`). Potions stack up to **2**
charges in the bowl and are consumed on the next growth check, where they cancel out the
matching malady before any remaining health is restored.

**Watering matters as much as the maladies.** Water sits at **0–4** and the plant wants
**2**. On each growth check, every point of water **above or below 2** deals
`3–6` damage, as does each level of each active malady (`ApplyMaladiesEffects`). Let the
hits fall to zero and the plant **dies**: a full-grown plant collapses to **dead twigs**,
an immature one drops back to an empty bowl of dirt (`PlantItem.Die`).

**Beneficial care.** If a plant has **no maladies** and correct water, it slowly heals
(`+2` hits per check, or `+7` per **greater heal potion** charge). A **greater strength
potion** lowers the infestation/fungus chance for the next check by `0.075` per charge. And
planting in **fertile dirt** (a *bag of bones* / fertile-dirt bowl) gives a **10% chance to
double-grow** — skipping a whole stage — up to stage 5 (`Grow`).

> **Neglect is forgiving in one way:** the growth check only fires roughly once a day and
> on login/world-save, so a plant can sit idle without progressing. But the moment a check
> runs with bad water or untreated maladies, it takes damage — so a long absence with a
> sick plant is fatal.

## Plant types & colours

There are **44 growable plant types** and **19 plant hues** (`PlantType.cs`,
`PlantHue.cs`). Types fall into categories:

- **Default (17)** — the everyday garden plants: campion flowers, poppies, snowdrops,
  bulrushes, lilies, pampas grass, rushes, elephant-ear plant, fern, ponytail palm, small
  palm, century plant, water plant, snake plant, prickly-pear / barrel / tribarrel cactus.
  These are the only types that can be **cross-bred** and that **reproduce** (make seeds).
- **Bonsai (8)** — common, uncommon, rare, exceptional and exotic **bonsai trees** (green
  and pink variants for the lower tiers). These are special drops; they neither cross-breed
  nor reproduce.
- **Peculiar (18)** — decorative-only oddities: cactus, flax flowers, foxglove, hops,
  orfluer flowers, twisted/straight cypress, short/tall hedge, juniper bush, snowdrop &
  poppy patches, cattails, spider tree, water lily, sugar canes (bamboo art), and vanilla.
- **Fragrant (1)** — the **cocoa tree** (the *o'hii tree* in older art), source of cocoa.

### Hues and cross-pollination

Seeds carry a **hue**. The natural starting colours are **Plain, Red, Blue, Yellow** (the
`RandomFirstGeneration` set). From these, three derived colours come from mixing primaries
— **Purple** (red+blue), **Green** (blue+yellow), **Orange** (red+yellow) — and each colour
has a **Bright** variant. There are also five **rare** hues that don't come from normal
mixing: **Black, White, Pink, Magenta, Aqua, Fire Red** (`PlantHue.cs`).

Colours are produced by **cross-pollination** (`PlantHue.Cross`, `PlantType.Cross`):

1. A full-grown **crossable** plant becomes **pollen-producing** (`PollenProducing`).
2. Using the gump's reproduction/pollinate target (`PollinateTarget.cs`,
   `ReproductionGump.cs`) you pollinate one plant with another. Its seeds then carry the
   **crossed** type and hue instead of its own.
3. Hue crossing rules: **same colour → that colour, made Bright**; **two primaries → their
   blend** (red+blue = purple, etc.); a primary crossed with a non-primary keeps the
   primary; otherwise the shared component. Any cross also has a **1% chance to yield Black
   or White** — the classic way "accidental" rare plants appear.
4. Type crossing nudges toward the **average** of the two types in the table, so you can
   walk seeds toward a target plant over several generations.

Only **crossable** hues/types can be bred, and only **reproducing** ones make seeds at all
(`IsCrossable`, `Reproduces`). The rare hues (Black, White, Pink, Magenta, Aqua, Fire Red)
and the Peculiar/Bonsai types are **not** crossable — they're collected, not bred.

A full machine-readable list of every type and hue (with item IDs, category, and the
crossable/reproduces/bright flags) is in `data/plants.json`.

## What plants give you

A full-grown plant is a renewable little factory. On each growth check at full size it can
produce (`PlantSystem.Grow`):

- **Seeds** — a pollinated, reproducing plant yields seeds (up to 8 over its life) carrying
  the crossed type/hue. This is how you propagate and trade colours. Loose seeds and the
  **seed box** (`Scripts/Items/Functional/SeedBox/`) let you store and sort a collection.
- **Plant clippings / resources** — certain **type + hue** combinations drop a crafting
  material (up to 8 over its life). From `PlantResources.cs`:

  | Resource | Plant + required hue |
  |----------|----------------------|
  | Red leaves | Elephant-ear plant, ponytail palm, or century plant — **Bright Red** |
  | Orange petals | Poppies, bulrushes, or pampas grass — **Bright Orange** |
  | Green thorns | Snake plant or barrel cactus — **Bright Green** |
  | Cocoa pulp | Cocoa tree — **Plain** |
  | Sack of sugar | Sugar canes — **Plain** |
  | Flax | Flax flowers — **Plain** |
  | Bark fragment | Straight or twisted cypress — **Plain** |
  | Vanilla | Vanilla — **Plain** |
  | Poppies dust | Poppy patch — **Plain** |

  Note this is why hue matters beyond looks: only the **bright** colour of a leaf/petal/
  thorn plant yields its reagent. **Cocoa pulp**, **sack of sugar** and **vanilla** feed
  the [Cooking](/skills/cooking/) chain (chocolate and baking recipes).
- **Plant pigments** — full-grown and decorative plant colours can be turned into **plant
  pigments** (`Scripts/Services/BasketWeaving/PlantPigment.cs`), used to dye items in the
  plant-colour palette. See the [Hues reference](/reference/hues/) for how dyeing colours
  work on this shard.
- **Decorative plants** — set a finished plant to decorative and it becomes a permanent
  potted houseplant for [house decorating](/playing/decorating/).

### The Naturalist

The **Naturalist** NPC (`Scripts/Mobiles/NPCs/Naturalist.cs`) is tied to the **Study of
Solen** quest. Completing it rewards a **random plant seed**. Studying an ordinary nest
yields one of the three semi-rare hues (**Pink, Magenta, Aqua**); studying a *special* nest
yields a truly rare hue (**Fire Red, White, or Black**) — a reliable way to seed a
collection with colours you can't simply breed. *(This shard's Naturalist is a quest giver,
not a plant appraiser/vendor.)*

## See also

- [Decorating](/playing/decorating/) — placing potted plants and decorative trees in a house.
- [House Types](/playing/house-types/) — the house shells you'll lock plants down in.
- [Hues](/reference/hues/) — how plant colours and plant pigments fit the dye palette.
- [Resources](/items/resources/) — where plant-grown materials sit among gathered resources.
- [Cooking](/skills/cooking/) — cocoa, sugar and vanilla from the garden feed baking recipes.
- [Professions](/professions/) — a dedicated gardener is a fun, peaceful niche profession.
