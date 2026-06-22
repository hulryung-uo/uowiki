---
title: "Template: Crafter (the Mule)"
description: The non-combat producer who makes the shard's tools, suits, and potions. Why crafters specialize, two example mule builds, BODs, repairs, and the economy.
status: source-verified
sources:
  - "community UO build knowledge (Stratics, UO Outlands wiki, UO forums) — adapted to this shard"
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000/700.0, SkillCap=1000/100.0, TotalStatCap=225)"
  - "servuo: Server/Skills.cs (Blacksmithy, Tailoring, Tinkering, Arms Lore, Carpentry, Mining, Magery, Alchemy, Taste Identification, Cooking, Inscription all present in SkillInfo)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs:6368 + BaseArmor.cs:3184 (Arms Lore adds ArmsLore.Value/20 to WeaponDamage / resist on EXCEPTIONAL items only; does not affect exceptional chance — GetExceptionalChance in CraftItem.cs has no ArmsLore term)"
last_verified: 2026-06-22
generated: false
---

:::note[Unverified community build]
Classic-era **crafting builds (Stratics / UO Outlands wiki / UO forums) adapted to this
shard's caps**, not yet field-verified here. Exact recipes and BOD reward tables await
in-game confirmation; file discrepancies per [wiki conventions](/guides/wiki-conventions/).
:::

A **mule** is a dedicated non-combat character whose whole job is to *produce* — tools,
armor, potions, deeds, repairs — for everyone else. Crafters don't fight; they're the
backbone of the economy. Every dexxer's suit, every mage's instrument, every tamer's
bandage-budget ultimately traces back to a crafter somewhere.

## Why crafters specialize (the 700-cap problem)

On **this shard** skills cap at **100.0 each and 700.0 total**
([`Config/PlayerCaps.cfg`](/shard/)) — seven Grandmaster skills, no more. You **cannot fit
every craft on one character**: Blacksmithy, Tailoring, Carpentry, Tinkering, Alchemy,
Inscription, Cooking, plus the support skills (Mining, Lumberjacking, Arms Lore, Magery for
recall) add up to far more than 700.

So crafters **specialize**, and players keep **several mules** — one for metal and cloth,
another for potions and tools — and shuttle materials between them. The two builds below are
the classic pair.

:::tip[Power scrolls go past 100 here]
On modern OSI crafting skills run to **120** via **power scrolls** from
[champion spawns and treasure chests](/playing/treasure-hunting/), which improves success
and quality. Power scrolls raise a skill's cap past 100.0 **on this shard too**, but they
**don't add slots** — the 700 total still forces specialization. Treat the GM (100) builds
below as the default.
:::

## Build A — Smith / Tailor mule (the suit factory)

The armorer. Makes metal armor and weapons, cloth and leather suits, and the tools to do it.

| Skill | At | Role |
|---|---|---|
| [Blacksmithy](/skills/blacksmithy/) | 100 | Metal armor and weapons; the big BOD earner |
| [Tailoring](/skills/tailoring/) | 100 | Cloth + leather armor; its own BOD system |
| [Tinkering](/skills/tinkering/) | 100 | Makes the tools every crafter needs (see below) |
| [Arms Lore](/skills/arms-lore/) | 100 | Adds damage/resist to *exceptional* weapons and armor you craft (not exceptional chance) |
| [Carpentry](/skills/carpentry/) | 100 | Furniture, bows, house add-ons, instruments |
| [Mining](/skills/mining/) | 100 | Self-supply ore for the forge |
| [Magery](/skills/magery/) | 100 | Recall — move between forge, bank, and mine |

Total: **700.0**. Drop [Mining](/skills/mining/) for [Lumberjacking](/skills/lumberjacking/)
if you lean carpentry/bowyer, or drop [Magery](/skills/magery/) (use Recall scrolls from a
mule with the runebook) to fit a seventh craft. See [Blacksmith](/templates/blacksmith/) for
the smith-focused storyline.

## Build B — Alchemy / Tinkering mule (the supply line)

The supplier. Brews the potions fighters buy by the hundred and makes the tools every other
crafter consumes.

| Skill | At | Role |
|---|---|---|
| [Alchemy](/skills/alchemy/) | 100 | Heal/cure/refresh/explosion potions — fighters buy these endlessly |
| [Tinkering](/skills/tinkering/) | 100 | Tools (tongs, sewing kits, etc.), traps, clocks, kegs hardware |
| [Magery](/skills/magery/) | 100 | Recall; some reagent/utility synergy |
| [Taste Identification](/skills/taste-identification/) | 100 | The alchemy support skill (poison/potion ID) |
| [Cooking](/skills/cooking/) | 100 | Food, kegs-adjacent supply; cheap to GM |
| [Inscription](/skills/inscription/) | 100 | Spell scrolls and runebooks — the scribe's trade |
| [Mining](/skills/mining/) | 100 | Ingots for Tinkering tools, or swap for a gathering skill |

Total: **700.0**. This is a flexible block — swap [Cooking](/skills/cooking/) or
[Mining](/skills/mining/) for whatever supply gap your shard's market has. The two anchors
are **Alchemy** (potions everyone consumes) and **Tinkering** (the tools everyone needs).

**Why Tinkering is on both builds:** Tinkering makes the **tools every other crafter
needs** — tongs for smithing, sewing kits and scissors for tailoring, and the like — so it's
the craft that bootstraps all the others. A shard with no tinker is a shard buying tools from
NPCs at a markup. See [Tinker](/professions/tinker/) and [tools](/items/tools/).

## BODs — the crafter's quest system

**Bulk Order Deeds** are the crafter's grind and gold sink. An NPC hands you a deed asking
for *N* of an item at a given quality/material; fill it, turn it in, and earn gold plus
**reward items** (rare materials, deco, and the runic/special tools that let you craft magic
gear). Smithing and Tailoring each have their own BOD chain — see
[Blacksmith](/professions/blacksmith/) and [Tailor](/professions/tailor/). BODs are why
crafters keep grinding long past GM: the rewards, not the base items, are the prize.

## Repairs and the economy

- **Repairs.** A GM crafter repairs gear for players and NPCs — a steady trickle of gold and
  goodwill, and the reason a smith mule is welcome at every bank.
- **The supply chain.** Miners feed smiths; lumberjacks feed carpenters; alchemists feed
  fighters; tinkers feed *everyone*. A crafter sits at the center of it. See
  [crafting](/playing/crafting/) for the production loop and
  [scribe](/professions/scribe/) / [alchemist](/professions/alchemist/) for the
  consumable trades.
- **Vendors.** Most crafters sell from a [player vendor](/playing/vendors-and-banking/) at a
  house rather than spamming the bank — passive income while you mine or BOD.

## Stages and playstyle

- **Early:** pick ONE anchor craft and a way to feed it (Mining for a smith, reagent buying
  for an alchemist). Grind it toward GM on cheap materials; sell or recycle the output.
- **Mid:** add the support skills (Arms Lore, Tinkering, Taste ID) and start filling
  [BODs](/professions/blacksmith/) for reward tools. Set up a vendor.
- **Endgame:** GM specialist with runic/reward tools, a stocked vendor, and a second mule for
  the crafts you couldn't fit. You are now the person other players come *to*.

## Decision points

- **If you're trying to fit every craft on one character**, stop — the 700 cap won't allow
  it. Build two mules instead (A and B above).
- **If you have no way to make tools**, put [Tinkering](/skills/tinkering/) on the build —
  it's the craft that supplies the others.
- **If income is flat**, lean into [BODs](/professions/blacksmith/) and repairs, and sell
  consumables ([Alchemy](/skills/alchemy/) potions, [Inscription](/skills/inscription/)
  scrolls) that players burn through.
- **If you don't want to gather**, drop [Mining](/skills/mining/)/[Lumberjacking](/skills/lumberjacking/)
  and buy materials — but you'll trade margin for convenience.
- **Mistake:** spreading thin across many half-trained crafts. A GM specialist out-earns a
  jack-of-all-trades every time.
