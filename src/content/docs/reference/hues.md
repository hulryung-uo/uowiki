---
title: Hue Reference
description: How UO hue values map to colors — the hues.mul palette, notable craft-resource hues, and why the wiki bakes hues into PNGs.
status: source-verified
sources:
  - "client: hues.mul"
  - "servuo: Scripts/Misc/ResourceInfo.cs"
last_verified: 2026-06-11
generated: false
---

A **hue** in Ultima Online is a 1-based index into the client's `hues.mul` file.
Every colored item, creature, and piece of clothing carries a hue number; the
client looks that number up to decide how to recolor a sprite.

The important thing to understand is that a hue is **not a flat tint**. Each hue
is a 32-shade gradient — a ramp from shadow to highlight. When the client draws a
hued sprite, it walks the sprite's own grayscale shadow→highlight ramp and
**remaps** each gray level to the matching shade of the hue's gradient. A near-
black pixel becomes the hue's darkest shade; a near-white pixel becomes its
lightest. That is why a single grayscale ingot sprite can become nine visibly
different metals while keeping all of its shading and depth.

This remapping is also why this wiki **bakes hues directly into PNGs** rather than
using CSS `filter` or a color overlay: a CSS tint multiplies a flat color across
the whole image and flattens the shading, which cannot reproduce a 32-step palette
remap. We read the gradient out of `hues.mul` and recolor the sprite pixel-by-pixel,
exactly as the client does.

(Hue `0` is the special "unhued" value — it means "draw the sprite as-is," so it
has no gradient entry of its own.)

## The full palette

Below is every hue in `hues.mul`, drawn as a grid of small swatches. Each swatch
shows a representative mid-tone from that hue's 32-shade gradient. Gridlines mark
every 8 columns and rows for orientation. Reading left-to-right, top-to-bottom,
the first swatch is game hue `1`.

![Grid of all UO hue swatches from hues.mul](/img/hues/chart.png)

*All 3000 hues in `hues.mul`, one mid-tone swatch each (40 per row).*

## Notable hues

These are the craft-resource hues defined in
[ServUO's `ResourceInfo.cs`](https://github.com/ServUO/ServUO) — the colors the
crafting system applies to metals, leather, dragon scales, and wood. Each swatch
shows the full 32-shade gradient (shadow at top, highlight at bottom).

### Metals

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x0973.png" class="uo-sprite" alt="Dull Copper hue ramp" width="48" height="48" /> | `0x0973` | 2419 | Dull Copper |
| <img src="/img/hues/h-0x0966.png" class="uo-sprite" alt="Shadow Iron hue ramp" width="48" height="48" /> | `0x0966` | 2406 | Shadow Iron |
| <img src="/img/hues/h-0x096D.png" class="uo-sprite" alt="Copper hue ramp" width="48" height="48" /> | `0x096D` | 2413 | Copper |
| <img src="/img/hues/h-0x0972.png" class="uo-sprite" alt="Bronze hue ramp" width="48" height="48" /> | `0x0972` | 2418 | Bronze |
| <img src="/img/hues/h-0x08A5.png" class="uo-sprite" alt="Gold hue ramp" width="48" height="48" /> | `0x08A5` | 2213 | Gold |
| <img src="/img/hues/h-0x0979.png" class="uo-sprite" alt="Agapite hue ramp" width="48" height="48" /> | `0x0979` | 2425 | Agapite |
| <img src="/img/hues/h-0x089F.png" class="uo-sprite" alt="Verite hue ramp" width="48" height="48" /> | `0x089F` | 2207 | Verite |
| <img src="/img/hues/h-0x08AB.png" class="uo-sprite" alt="Valorite hue ramp" width="48" height="48" /> | `0x08AB` | 2219 | Valorite |

### Leather

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x0283.png" class="uo-sprite" alt="Spined leather hue ramp" width="48" height="48" /> | `0x0283` | 643 | Spined |
| <img src="/img/hues/h-0x0227.png" class="uo-sprite" alt="Horned leather hue ramp" width="48" height="48" /> | `0x0227` | 551 | Horned |
| <img src="/img/hues/h-0x01C1.png" class="uo-sprite" alt="Barbed leather hue ramp" width="48" height="48" /> | `0x01C1` | 449 | Barbed |

### Dragon scales

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x066D.png" class="uo-sprite" alt="Red Scales hue ramp" width="48" height="48" /> | `0x066D` | 1645 | Red Scales |
| <img src="/img/hues/h-0x08A8.png" class="uo-sprite" alt="Yellow Scales hue ramp" width="48" height="48" /> | `0x08A8` | 2216 | Yellow Scales |
| <img src="/img/hues/h-0x0455.png" class="uo-sprite" alt="Black Scales hue ramp" width="48" height="48" /> | `0x0455` | 1109 | Black Scales |
| <img src="/img/hues/h-0x0851.png" class="uo-sprite" alt="Green Scales hue ramp" width="48" height="48" /> | `0x0851` | 2129 | Green Scales |
| <img src="/img/hues/h-0x08FD.png" class="uo-sprite" alt="White Scales hue ramp" width="48" height="48" /> | `0x08FD` | 2301 | White Scales |
| <img src="/img/hues/h-0x08B0.png" class="uo-sprite" alt="Blue Scales hue ramp" width="48" height="48" /> | `0x08B0` | 2224 | Blue Scales |

### Wood

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x07DA.png" class="uo-sprite" alt="Oak hue ramp" width="48" height="48" /> | `0x07DA` | 2010 | Oak |
| <img src="/img/hues/h-0x04A7.png" class="uo-sprite" alt="Ash hue ramp" width="48" height="48" /> | `0x04A7` | 1191 | Ash |
| <img src="/img/hues/h-0x04A8.png" class="uo-sprite" alt="Yew hue ramp" width="48" height="48" /> | `0x04A8` | 1192 | Yew |
| <img src="/img/hues/h-0x04A9.png" class="uo-sprite" alt="Heartwood hue ramp" width="48" height="48" /> | `0x04A9` | 1193 | Heartwood |
| <img src="/img/hues/h-0x04AA.png" class="uo-sprite" alt="Bloodwood hue ramp" width="48" height="48" /> | `0x04AA` | 1194 | Bloodwood |
| <img src="/img/hues/h-0x047F.png" class="uo-sprite" alt="Frostwood hue ramp" width="48" height="48" /> | `0x047F` | 1151 | Frostwood |

## Same sprite, every metal

Every ingot color uses the **same** grayscale art (item `0x1BF2`). The only thing
that changes is the hue. Below is that one sprite, drawn nine times — plain Iron
plus the eight colored metals — to show how the remap turns one piece of art into
nine distinct ingots:

<img src="/img/items/0x1BF2.png" class="uo-sprite" alt="Iron ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0973.png" class="uo-sprite" alt="Dull Copper ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0966.png" class="uo-sprite" alt="Shadow Iron ingot" width="44" height="44" />
<img src="/img/hues/demo-0x096D.png" class="uo-sprite" alt="Copper ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0972.png" class="uo-sprite" alt="Bronze ingot" width="44" height="44" />
<img src="/img/hues/demo-0x08A5.png" class="uo-sprite" alt="Gold ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0979.png" class="uo-sprite" alt="Agapite ingot" width="44" height="44" />
<img src="/img/hues/demo-0x089F.png" class="uo-sprite" alt="Verite ingot" width="44" height="44" />
<img src="/img/hues/demo-0x08AB.png" class="uo-sprite" alt="Valorite ingot" width="44" height="44" />

*Iron, Dull Copper, Shadow Iron, Copper, Bronze, Gold, Agapite, Verite, Valorite —
one sprite, nine hues.*

To see where these resources come from and how they're used, visit the
[Resources gathering guide](/items/resources/) and the
[Resources item catalog](/items/catalog/resources/).
