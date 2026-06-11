---
title: "Template: Lumberjack"
description: A lumberjacking + fletching starter build with a full progression storyline — creation choices, the bow money loop, training tables, and decision points, using this shard's actual crafting numbers.
status: unverified
sources:
  - "external: UOSA money-making guide (forums.uosecondage.com/viewtopic.php?t=45914)"
  - "external: Seth's Easy Lumberjacking Guide (forums.uosecondage.com/viewtopic.php?t=37138)"
  - "external: uoguide.com/Lumberjacking (axe damage bonus)"
  - "wiki: /crafting/bowfletching/, /crafting/carpentry/, /crafting/tinkering/, /skills/lumberjacking/, /items/resources/, /mechanics/character-creation/"
  - "servuo: Scripts/Misc/CharacterCreation.cs (Fletching starter kit)"
  - "servuo: Scripts/VendorInfo/SBRangedWeapon.cs, SBCarpenter.cs (NPC prices)"
  - "servuo: Scripts/Mobiles/NPCs/Bowyer.cs + Scripts/Services/BulkOrders/BulkOrderSystem.cs (fletching BODs)"
last_verified: 2026-06-11
generated: false
---

> **Status: unverified.** This storyline adapts classic-era community wisdom to our shard.
> Skill ranges and NPC prices below were checked against the server source; pacing and
> income estimates await field verification by play.

The lumberjack is the classic zero-risk starter: trees are free, axes are cheap, and every
board you cut is either gold or skill. Endgame goal: **GM Lumberjacking + GM Fletching**,
a board-and-bow pipeline funding your **first house nest egg** — and, if you ever want to
fight, [Lumberjacking is secretly +damage with axes](/skills/lumberjacking/) (up to ~+30%
at GM), so this character converts to an axe warrior better than any other crafter.

## Character creation on this shard

Per the [creation rules](/mechanics/character-creation/) (90 stat points, 4 skills × max
50, total 120):

| Choice | Pick | Why |
|---|---|---|
| Stats | **STR 60 / DEX 15 / INT 15** | STR = carry weight = boards per trip. Logs weigh double what boards do — STR and the boards rule below are the whole logistics game. |
| Skills | **Lumberjacking 50, Fletching 50, Carpentry 20** | Custom template. Carpentry 20 is the seed of a later keg/furniture sideline. |
| City | **[Yew](/world/yew/)** | The town *is* a forest, with a bowyer, a carpenter, and — yes — a **bank at Empath Abbey** (652, 820). |

Starter gear (verified in `Scripts/Misc/CharacterCreation.cs`): Lumberjacking grants a
**hatchet**; Fletching grants **14 boards, 5 feathers, 5 shafts**; Carpentry grants a
**saw, 10 boards, half apron**. Spare hatchets cost ~25 gp at any weaponsmith. Your 1,000
starting gold easily covers spares plus a **pack horse (631 gp)** if you want bigger hauls.

**Variant:** swap Carpentry for **Tinkering** to self-make hatchets — but note our
[tinkering table](/crafting/tinkering/) puts hatchets at **30–80 skill**, so Tinkering 20
can't make them; you'd start at 50 Tinkering and drop Fletching points. For a pure
money/crafting start, Carpentry 20 is the cleaner pick.

## The one rule that matters

**Always chop logs into boards on the spot** (use your axe on the logs). Boards weigh half
as much, every recipe accepts them, and NPC carpenters pay **2 gp per board vs 1 gp per
log** (`Scripts/VendorInfo/SBCarpenter.cs`). Board-cutting needs Carpentry *or*
Lumberjacking at the wood's level ([table](/items/resources/)) — your Lumberjacking
always qualifies for what you can chop.

## Stage 1 — Novice (Lumberjacking 50→65, Fletching 50→70)

**Goal:** the bow loop. Chop in the Yew woods, cut boards, craft **bows (30–70 skill,
7 boards)** per our [fletching table](/crafting/bowfletching/), sell to the NPC bowyer,
bank at Empath Abbey.

- At Fletching 50 a bow is a coin-flip; by 70 it's guaranteed. Each chop yields **10
  logs** ([lumberjacking](/skills/lumberjacking/)), i.e. ~1.4 bows.
- **NPC bowyers pay 17 gp per bow** (21 gp exceptional, `SBRangedWeapon.cs` +
  `GenericSell.cs`) — *not* the ~30 gp of era guides. That's ~2.4 gp per board through
  bows vs 2 gp raw, so Stage-1 bows are mostly *skill* with gold as a side effect.
- **Era advice that does not apply:** there is no hourly buyback decay here. Weapon
  sell prices are flat table prices — no need to run a six-bowyer circuit for bows.
  (Stackables like boards do sag — see the trade loop.)
- Bank often; you start in Trammel and reds are Felucca-only, so the only thing that
  kills a Yew lumberjack is overconfidence near the dungeons south of town.

## Stage 2 — Journeyman (Lumberjacking 65→90, Fletching 70→90)

- **Switch to crossbows at Fletching ~70**: our window is **60–100** (7 boards), and they
  sell for **25 gp** — ~3.6 gp per board, the best NPC rate in the fletching book. Era
  guides said crossbows at ~68; here they also *gain all the way to GM*.
- Lumberjacking 65 opens **oak** (30% of veins), 80 opens **ash** — colored boards are
  player-market goods ([wood table](/items/resources/)).
- **Fletching BODs exist on this shard** (they didn't in the classic era): any NPC bowyer
  offers one per 6 hours, banking up to 2, once you have any Fletching skill
  (`Scripts/Mobiles/NPCs/Bowyer.cs`, `BulkOrderSystem.cs`). Collect on every sell run.
- **Collect feathers** (birds, harpies) and turn spare scraps into **arrows (0–40 skill)**.
  NPCs pay only 1 gp per arrow, so the era's "arrow money" is player-market here — sell
  arrows in bulk to archers on the forum Trade board, not to vendors.
- Optional: train Carpentry 20→58 (staves 0–25, barrel lids 11–36) toward the **keg
  (57.8–82.8)** sideline — note kegs also need **barrel hoops, a tinker recipe**
  ([carpentry table](/crafting/carpentry/), [tinkering](/crafting/tinkering/)), so
  budget to buy those.

## Stage 3 — Master (Lumberjacking 90→GM, Fletching 90→GM)

- **Heavy crossbows (80–120, 10 boards)** are the gain item past ~90 — at Fletching 95 a
  crossbow succeeds 87% (slow gains) while a heavy sits near 37%. They sell for 27 gp,
  a *worse* gp-per-board than crossbows — craft heavies for skill, crossbows for gold.
- Lumberjacking 95 opens **yew wood**, 100 opens heartwood/bloodwood/frostwood plus bonus
  resources (bark fragments, amber) — all player-market, all reasons crafters seek you out.
- The axe bonus quietly matured with you: a GM lumberjack with an axe and some
  [Swordsmanship](/skills/swordsmanship/) is a legitimate hunter — one respec-free path
  out of pure crafting.

## The trade loop

| Action | Where | Price (source-checked) |
|---|---|---|
| Sell bows / crossbows / heavies | NPC bowyer | 17 / 25 / 27 gp flat, +25% exceptional; no price sag on weapons |
| Sell plain boards in bulk | NPC carpenter | 2 gp each; the shelf price sags ~1 gp per 1,000 units one vendor absorbs (`GenericBuy.cs`) — rotate Yew → Britain → Vesper for big dumps |
| Sell boards to players | Forum Trade board | 2–3 gp — anything under the NPC's 3 gp shelf price wins; era's "4 gp to players" overshoots here |
| Sell colored boards, arrows, feathers, kegs | Players only | NPCs pay junk rates (1 gp arrows/feathers); these are relationship goods |
| Buy hatchets | NPC weaponsmith | ~25 gp; carry two — a broken axe a forest away from town is a wasted trip |
| Fletching BODs | Any NPC bowyer | Free every 6h, cache 2; rewards beat NPC stock |

## Decision points & common mistakes (for agents)

- **If your pack fills too fast** → you are carrying logs; cut boards at the tree, every
  time. If still too fast, raise STR (it trains while chopping) or buy a pack horse.
- **If bow success ≥ ~80%** → gains have slowed; move up: bows → crossbows (~70) →
  heavy crossbows (~90), per the [real windows](/crafting/bowfletching/).
- **If gold per trip matters more than skill** → crossbows are the ceiling (3.6 gp/board);
  below Fletching 60, raw boards at 2 gp beat bad bow rolls.
- **If a vendor starts paying 1 gp for boards** → you fed it ~1,000+; rotate towns or
  switch to the player market. Bows don't have this problem.
- **If a tree gives plain logs where you expected oak** → Lumberjacking below 65; the
  vein rolls are per-tree-bank, come back later ([table](/skills/lumberjacking/)).
- **If you want kegs** → check Carpentry ≥ ~58 first *and* line up barrel hoops from a
  tinker; staves and lids alone don't assemble.
- **If you start drifting toward combat** → keep the axe; the damage bonus is real and
  already paid for. Add Swordsmanship/Tactics rather than rerolling.
- **Don't count on AFK macroing** — classic guides call it the #1 ban magnet; this
  shard's [written rules](/shard/server-rules/) are config-only and don't address it,
  so ask on the forum before assuming it's tolerated.

## Related

- [Lumberjacking skill](/skills/lumberjacking/) · [Bow Fletching](/crafting/bowfletching/) ·
  [Carpentry](/crafting/carpentry/) · [Resources](/items/resources/) · [Yew](/world/yew/)
- [Template: Blacksmith](/templates/blacksmith/) — the same idea, but rocks
