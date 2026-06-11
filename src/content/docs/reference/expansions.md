---
title: UO Expansions
description: A chronological history of every Ultima Online expansion — the lands, races, skills, and systems each added — and how they map onto this shard, which runs the Endless Journey ruleset.
status: unverified
sources:
  - "general Ultima Online history; ultimaonline.fandom.com"
  - "servuo: Config/Expansion.cfg, Server/ExpansionInfo.cs"
last_verified: 2026-06-12
generated: false
---

Ultima Online has been expanded for more than two decades. Each **expansion** is a
named release that bolts new content onto the existing game — fresh lands and
*facets* (parallel maps), new playable **races**, new **skills** and spell schools,
and new **systems** (combat math, crafting, housing, sailing). An **era** is the
period a given expansion defines: when people say something is "AOS-era" they mean
it arrived with, or was reshaped by, *Age of Shadows*.

This matters for documentation because UO is cumulative. A server doesn't pick
features à la carte; it declares a single expansion level and inherits everything
up to and including it. **This shard runs Endless Journey (EJ)** — the most recent
level in the ServUO emulator — so *every* expansion below is present here. The
Lost Lands, all the facets, every race and skill school, custom housing, sailing,
Eodon — it's all live. (See `Config/Expansion.cfg`: `CurrentExpansion=EJ`.)

The list and ordering of expansions comes straight from the server's expansion
enum (`Server/ExpansionInfo.cs`): None → T2A → UOR → UOTD → LBR → AOS → SE → ML →
SA → HS → TOL → EJ. The headline additions for each are below.

## Timeline

| Expansion | Year | Headline additions |
|-----------|------|---------------------|
| Launch | 1997 | The original Britannia (Felucca map) |
| The Second Age (T2A) | 1998 | The Lost Lands; first big land expansion |
| Renaissance (UOR) | 2000 | Trammel/Felucca facet split; consensual vs open PvP |
| Third Dawn (UOTD) | 2001 | Ilshenar facet; first 3D client |
| Lord Blackthorn's Revenge (LBR) | 2002 | New art and creatures across the world |
| Age of Shadows (AOS) | 2003 | Malas; resistances; item properties + insurance; Necromancy, Chivalry; custom housing |
| Samurai Empire (SE) | 2004 | Tokuno Islands; Bushido, Ninjitsu; samurai and ninja |
| Mondain's Legacy (ML) | 2005 | Elves; Spellweaving; the Heartwood; peerless bosses |
| Stygian Abyss (SA) | 2009 | Gargoyles; Ter Mur; Mysticism, Imbuing, Throwing; the Abyss |
| High Seas (HS) | 2010 | Ships and sea combat; fishing overhaul |
| Time of Legends (TOL) | 2015 | Valley of Eodon; Myrmidex; skill masteries |
| Endless Journey (EJ) | 2018 | Free-access tier — **the ruleset this shard runs** |

## Launch (1997)

Ultima Online shipped with a single land: **Britannia**, the map later known as
**Felucca**. There were no facets, no second map, and the world was a single open
ruleset — anyone could attack anyone, anywhere. Everything that follows is built
on top of this original world.

## The Second Age (T2A, 1998)

The first major land expansion. T2A added the **Lost Lands** — a sprawling outdoor
region reached through cave passages and dungeons, with new towns, terrain, and
creatures roughly doubling the explorable surface. It also brought tougher
monsters and the iconic dungeons of that frontier.

On this shard the Lost Lands are fully present. Two of its frontier towns are
documented in our world section: **Delucia** and **Papua**.

- [World atlas](/world/) · [Delucia](/world/delucia/) · [Papua](/world/papua/)

## Renaissance (UOR, 2000)

Renaissance reshaped the *social* game more than the geography. It split the world
into two parallel **facets**: **Trammel**, where players cannot harm one another
without consent, and **Felucca**, which kept the original open-PvP, full-loot
ruleset. The same cities exist on both, but the rules of engagement differ. This
"Tram/Fel" divide is the single most consequential change to how PvP and
notoriety work, and it persists in the game to this day.

- [Notoriety and PvP](/playing/notoriety-and-pvp/)

## Third Dawn (UOTD, 2001)

Third Dawn introduced the **Ilshenar** facet — a large, lore-rich landmass with no
player housing and no moongate ties to the other maps, themed around the
gargoyles and the Ophidians. Its other headline was technical: UO's first
**3D client**, an alternative renderer alongside the classic 2D client.

## Lord Blackthorn's Revenge (LBR, 2002)

LBR was lighter on geography and heavier on presentation. It overhauled a great
deal of the game's **art and creatures** — many monster sprites were redrawn — and
wove in a storyline around the corrupted Lord Blackthorn. It also tightened the
client's support for the newer 3D assets introduced the year before.

## Age of Shadows (AOS, 2003)

The big one. *Age of Shadows* rewrote the rules of equipment and combat more than
any expansion before or since. Its additions:

- **Malas** — a new facet, home to the city of Luna, Umbra, and the Doom dungeon.
- The **resistance system**: armor no longer used a single Armor Rating but five
  separate resistances — Physical, Fire, Cold, Poison, Energy — each capped at 70.
  Damage types matter; you build a suit to balance the five.
- **Item properties and intensity**: magical gear gained dozens of stackable
  properties (Faster Casting, Hit Chance Increase, Damage Increase, Lower Reagent
  Cost, and so on), turning loot and crafting into a min-max game.
- **Item insurance**, so a death no longer meant losing your equipped suit.
- **Custom housing** — the in-game house designer, letting players draw their own
  floor plans instead of choosing from fixed deeds.
- Two new spell schools and the templates built on them: **Necromancy** (the
  necromancer) and **Chivalry** (the paladin).

- [Necromancer](/professions/necromancer/) · [Paladin](/professions/paladin/)
- [Armor and resistances](/items/armor/) · [House types](/playing/house-types/)

## Samurai Empire (SE, 2004)

An Asian-themed expansion centered on the **Tokuno Islands**, a three-island facet
with its own towns, dungeons, and decorative style. It added two skills and the
classes built around them: **Bushido** (the samurai, a melee/parry warrior with
stance abilities) and **Ninjitsu** (the ninja, with stealth, animal forms, and
mirror images).

- [Samurai](/professions/samurai/) · [Ninja](/professions/ninja/)

## Mondain's Legacy (ML, 2005)

Mondain's Legacy added the first new **playable race** since launch — the **elves**
— with their own starting stats and racial traits. Its other pillars:

- **Spellweaving**, an arcane school whose power scales when cast in a group, plus
  the Arcanist template built on it.
- The **Heartwood**, an elven settlement hidden in the forest, with its own
  quest-driven crafting rewards.
- **Peerless bosses** — instanced, key-gated encounters (Travesty, Dreadhorn,
  Lady Melisande, and others) that became the template for endgame fights.
- Early groundwork toward the resource-and-property crafting that *Imbuing* would
  later formalize.

- [Spellweaver](/professions/spellweaver/) · [Spellweaving skill](/skills/spellweaving/)

## Stygian Abyss (SA, 2009)

Stygian Abyss added the second new race — the **gargoyles**, who can fly — and the
**Ter Mur** facet, the gargoyle homeland, reached through the great
**Stygian Abyss** dungeon itself. It brought three skills at once:

- **Mysticism**, a hybrid arcane/divine school (the mystic).
- **Imbuing**, the crafting skill that lets you build magic properties onto items
  to a controlled intensity — the formalization of ML's groundwork.
- **Throwing**, the gargoyle-only ranged combat skill.

- [Mystic](/professions/mystic/) · [Mysticism](/skills/mysticism/)
- [Imbuing](/skills/imbuing/) · [Throwing](/skills/throwing/)

## High Seas (HS, 2010)

High Seas made the oceans matter. It added a full **sailing and naval combat**
system — multi-tile ships with cannons, ship-to-ship battles, and seaborne
enemies like the merfolk and the Corgul boss — and overhauled **fishing** into a
deeper profession with new catches, big fish, and message-in-a-bottle treasure.

- [Fisher](/professions/fisher/) · [Treasure hunting](/playing/treasure-hunting/) (message-in-a-bottle / SOS)

## Time of Legends (TOL, 2015)

Time of Legends opened the **Valley of Eodon**, a prehistoric jungle land with
dinosaurs, the insectoid **Myrmidex**, and the Zhah and Sakkhra tribes. Its
system addition was **skill masteries** — per-skill mastery abilities that give
established characters a new layer of specialization and active powers.

## Endless Journey (EJ, 2018)

Endless Journey is less a content drop than an **access tier**: a free-to-play
ruleset that lets accounts log in and play a broad slice of the game without an
active subscription, with some restrictions on storage and the newest content.
In the ServUO emulator EJ is the **highest expansion level**, which means it
inherits the full content stack of every expansion above.

**This is the ruleset our shard runs.** When you read elsewhere on this wiki that
a skill, spell, or item exists here, it's because EJ carries the whole history
below it forward.

- [Our shard](/shard/)

## What this means for our shard

Because the shard runs **EJ**, none of this history is hypothetical — it's all the
ground you're standing on. Every facet (Felucca, Trammel, Ilshenar, Malas,
Tokuno, Ter Mur, Eodon), both extra races (elf, gargoyle), every spell school
(Necromancy, Chivalry, Bushido, Ninjitsu, Spellweaving, Mysticism), and every
system (resistances, item properties, insurance, custom housing, sailing,
imbuing, masteries) is available to characters here.

That's also why pages across this wiki tag content by **era**. The item and
crafting catalogs mark when each material, item, and recipe was introduced —
those tags come straight from the history on this page, so you can tell at a
glance whether something is a launch-era staple or arrived with a later
expansion. See the [item catalogs](/items/) for the per-item era tags, and the
[shard pages](/shard/) for the caps, rates, and house rules that sit on top of
this EJ baseline.
