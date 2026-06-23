---
title: "Template: Blacksmith"
description: A mining + blacksmithy starter build with a full progression storyline — creation choices, training tables, money loops, and decision points, using this shard's actual crafting numbers.
status: unverified
sources:
  - "external: UOSA Beginners Guide (wiki.uosecondage.com/Beginners_Guide)"
  - "external: UOSA Blacksmithy guide (wiki.uosecondage.com/Blacksmithy)"
  - "external: UOSA smith training discussion (forums.uosecondage.com/viewtopic.php?t=389)"
  - "wiki: /crafting/blacksmithy/, /crafting/tinkering/, /skills/mining/, /items/resources/, /mechanics/character-creation/"
  - "servuo: Scripts/Items/Resource/Ore.cs (smelting skill check)"
  - "servuo: Scripts/Services/Craft/Core/Resmelt.cs (66% ingot recovery)"
  - "servuo: Scripts/VendorInfo/SBBlacksmith.cs, SBMiner.cs, SBAnimalTrainer.cs (NPC prices)"
  - "servuo: Scripts/Services/BulkOrders/BulkOrderSystem.cs (BOD timing)"
last_verified: 2026-06-11
generated: false
---

> **Status: unverified.** This storyline adapts classic-era community wisdom to our shard.
> All skill ranges and NPC prices below were checked against the server source, but the
> pacing and money estimates await field verification by play.

The blacksmith is the economy character: dig ore, smelt it, hammer it into goods, and turn
other players' adventures into your income. Endgame goal: **GM Blacksmithy + GM Mining**,
a runebook of marked mining spots, a steady [bulk order](#bulk-order-deeds) habit, and a
reputation as the smith people bring their broken plate to.

## Character creation on this shard

Per the server-enforced [creation rules](/mechanics/character-creation/) (90 stat points,
4 skills × max 50, total 120):

| Choice | Pick | Why |
|---|---|---|
| Stats | **STR 60 / DEX 15 / INT 15** | STR is carry weight — ore is heavy. This matches the server's own Blacksmith profession template exactly. |
| Skills | **Blacksmithy 50, Mining 50, Tinkering 20** | Use the *custom* template, not the profession button — custom picks grant starter gear per skill. |
| City | **[Minoc](/world/minoc/)** | Mountains, forge, anvil, and bank in one tight loop. |

Starter gear: Blacksmithy grants **tongs, two pickaxes, 50 iron ingots, half apron**;
Mining adds a third pickaxe; Tinkering adds **tinker's tools + 50 more ingots**. From your
1,000 starting gold, buy at the Minoc miner/tinker: spare **shovels (12 gp)** and
**pickaxes (22–25 gp)**, and consider a **pack horse (631 gp)** or **pack llama (565 gp)**
from an animal trainer — it roughly doubles your haul per trip
(`Scripts/VendorInfo/SBMiner.cs`, `SBAnimalTrainer.cs`).

**Era advice that does not apply here:** classic guides warn about hauling ore past PKs.
You start in **Trammel** and reds are restricted to Felucca on this shard
(`Config/General.cfg`) — plus new accounts have Young protection. Mine in peace.

## Stage 1 — Novice (Smithy 50→65, Mining 50→65)

**Goal:** a self-funding loop. Mine iron at the [Minoc mines](/world/minoc/), smelt at the
forge, craft, smelt the products back, bank the surplus.

- **Smelting is a Mining check** (`Scripts/Items/Resource/Ore.cs`): iron ore smelts against
  a 25–75 window, and a *failed smelt burns half the targeted ore pile*. At Mining 50 you
  fail about half your smelts — **smelt in small piles** until Mining ~75, where iron
  smelting becomes fail-proof.
- **Craft cutlasses** — on our shard the cutlass window is **24.3–74.3**
  ([crafting table](/crafting/blacksmithy/)), so it carries you from 50 (≈64% success)
  to ~65, not the era-standard "50–65 then switch". 8 ingots each.
- **Smelt your training output** via the craft gump: recovery is **66% of the ingots**
  (`Scripts/Services/Craft/Core/Resmelt.cs`), so each cutlass attempt nets ~3 ingots lost.
- Use **"craft all"** batches — multiple gain checks per click ([skill gain](/mechanics/skill-gain/)).

Money now: honestly thin. NPC smiths pay **4 gp per iron ingot** (the vendor's static sell
value, just under its 5 gp buy/shelf price — `Scripts/VendorInfo/SBBlacksmith.cs`: buy 5, sell
4) — selling raw ingot surplus beats selling cheap weapons (a cutlass fetches only 12 gp,
*less* than its 8 ingots raw).

## Stage 2 — Journeyman (Smithy 65→85, Mining 65→85)

- **Training table (our numbers, from [/crafting/blacksmithy/](/crafting/blacksmithy/)):**
  **kryss 36.7–86.7** (8 ingots) from ~65, then **short spear 45.3–95.3** (6 ingots) from ~75.
- **Mining 65+ opens colored veins** — dull copper at 65, shadow at 70, copper at 75,
  bronze at 80 ([ore table](/items/resources/)). Colored ingots sell to player smiths,
  not NPCs.
- **Tinkering:** era advice says "Tinkering 20 makes your shovels" — **not here**. Shovels
  require **Tinkering 40–90** ([tinkering table](/crafting/tinkering/)). Train 20→40 on
  **scissors (5–55, 2 ingots)**, then self-make shovels. Until then, 12 gp NPC shovels
  are fine.
- If you have a Magery friend (or buy Recall scrolls), get a **runebook marked at mine,
  forge, and bank** — the haul loop is the whole profession.

## Stage 3 — Master (Smithy 85→GM, Mining 85→GM)

- **Platemail gorget 56.4–106.4** (10 ingots) carries ~80→95; **platemail gloves
  58.9–108.9** (12 ingots) carry to GM — both still give gains *at* 100.0 since their
  windows top out past GM.
- **The plate arbitrage:** NPC armorers pay **52 gp per plate gorget** and **72 gp per
  plate gloves** (`SBBlacksmith.cs`), +25% if exceptional. Plate gloves turn 12 ingots
  into 72–90 gp — **6+ gp per ingot, double the raw-ingot rate**. Your GM training pays
  for itself; era guides budgeted 40–55k ingots to GM with most smelted back, but here
  the high end *sells*.
- Mining 85→99 opens gold/agapite/verite/**valorite (99)** veins — the prestige ingots
  player warriors actually pay for.

## Bulk order deeds

Smith BODs are live on this shard (`Scripts/Services/BulkOrders/BulkOrderSystem.cs`,
TOL-style system active under EJ): any NPC blacksmith offers one **every 6 hours, banking
up to 2** (`Delay = 6`, `MaxCachedDeeds = 2`), provided you have any Blacksmithy skill.
Fill iron small BODs from your training output and collect them on every bank run —
rewards include smith tools and materials that beat anything an NPC sells.

## The trade loop

| Action | Where | Price (source-checked) |
|---|---|---|
| Sell raw iron ingots | NPC smith, anywhere | 4 gp each (`SBBlacksmith.cs` sell value); the shelf price sags as the vendor absorbs bulk — spread bulk dumps across towns |
| Sell iron ingots in bulk | Player crafters (forum Trade board) | 4–5 gp — anything under the NPC's 5 gp shelf price undercuts their alternative |
| Sell plate gorgets / gloves | NPC armorer | 52 / 72 gp flat (+25% exceptional); not an economy item, no price sag |
| Sell colored ingots & exceptional plate | Players only | NPCs pay the same for valorite as iron — never NPC-sell colored |
| Repairs | Busy forges (Britain, Minoc) | Tips; repairing builds the client list that buys your plate later |
| Buy shovels/pickaxes | NPC miner/tinker | 12 / 22–25 gp until Tinkering 40+ |

[Britain](/world/britain/) bank is the realm's marketplace when you have stock worth
hawking; [Vesper](/world/vesper/) covers what Minoc's small vendor roster lacks.

## Decision points & common mistakes (for agents)

- **If overweight constantly** → STR too low or no pack animal; smelt at the mountainside
  forge-adjacent spots before walking, and remember ingots are far lighter than ore.
- **If smelting keeps destroying ore** → your Mining is below ~75; smelt small piles, or
  accept the loss as Mining training (the check gains skill).
- **If a craft item's success is above ~80%** → gains have slowed; move down the table
  (cutlass → kryss → short spear → plate gorget → plate gloves) per the
  [real windows](/crafting/blacksmithy/).
- **If tempted to NPC-sell training weapons** → don't; smelting recovers 66% of ingots,
  worth more than the 11–16 gp sale. Exception: plate gorgets/gloves, which sell above
  their metal value.
- **If a colored vein yields plain iron** → your Mining is below that ore's requirement
  ([table](/skills/mining/)); the vein isn't wasted, come back later.
- **If ingot prices collapse at one vendor** → you've fed it ~1,000+ units; rotate towns
  or pivot to the player bulk market.
- **If you took the "Blacksmith" profession button** → you got fixed 30-point skills and
  no custom gear; the custom template is strictly better here.
- **Don't count on AFK macroing** — the anti-macro *code* is off
  ([skill gain](/mechanics/skill-gain/)), but classic guides call unattended play the #1
  ban magnet; this shard's written policy doesn't address it, so ask on the forum before
  assuming it's tolerated.

## Related

- [Blacksmithy skill](/skills/blacksmithy/) · [Mining skill](/skills/mining/) ·
  [Resources](/items/resources/) · [Getting started](/guides/getting-started/)
- [Template: Lumberjack](/templates/lumberjack/) — the same idea, but trees
