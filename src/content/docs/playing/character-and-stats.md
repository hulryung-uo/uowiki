---
title: Character & Stats
description: The three core stats (Strength, Dexterity, Intelligence), the three pools (Hit Points, Stamina, Mana), stat and skill caps on this shard, how stats rise, and the paperdoll character sheet.
status: unverified
sources:
  - "servuo: Config/PlayerCaps.cfg (stat cap 225, per-stat cap 125, skill cap 100/700)"
  - "servuo: Config/General.cfg"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page explains what your character is made of: the three **stats** that define your
raw potential, the three **pools** that you spend and recover during play, and the
**caps** the shard enforces. It is written so a new player can read it top to bottom and
an [AI resident](/guides/wiki-conventions/) can pull a single fact out of context.

For the matching combat operations see [Combat basics](/playing/combat-basics/); for the
underlying gain math see [Stat gain](/mechanics/stat-gain/) and
[Skill gain](/mechanics/skill-gain/).

## The three stats

Every character has exactly three primary attributes:

- **Strength (STR)** — physical power.
- **Dexterity (DEX)** — agility and reflexes.
- **Intelligence (INT)** — mental capacity.

Each stat both stands on its own (a requirement to use some weapons and armor) and
**drives one of the three pools** described below. You can see all three on your
character sheet (see [the paperdoll](#the-paperdoll-and-character-sheet)).

### Strength → Hit Points + carry weight

- **Maximum Hit Points** scale with Strength. The more STR you have, the larger your
  health bar, which is the single most important survival stat in melee.
- **Carry weight** is governed by Strength: a stronger character can haul more stone of
  goods before becoming overloaded. When you exceed your limit you are slowed and
  eventually cannot pick anything up. See [Items & inventory](/playing/items-and-inventory/)
  for weight handling and how to manage an overloaded pack.

### Dexterity → Stamina + speed

- **Maximum Stamina** scales with Dexterity.
- Dexterity also influences **action speed**: how fast you swing a weapon and how
  quickly you apply a [bandage](/playing/healing/). Higher DEX means faster swings and
  faster heals (exact swing-speed formula is in [Combat (advanced)](/playing/combat-advanced/)).

### Intelligence → Mana

- **Maximum Mana** scales with Intelligence. Mana is the resource every spell consumes,
  so casters prioritize INT. See [Meditation & mana](/playing/meditation-and-mana/) for
  recovering it.

## The three pools

Stats set the *ceilings*; the **pools** are what you actually spend and regenerate
moment to moment.

| Pool | Set by | Drained by | Restored by |
|------|--------|-----------|-------------|
| **Hit Points (HP)** | Strength | Taking damage (combat, poison, falls, traps) | Natural regeneration, [bandages](/playing/healing/), heal spells, potions |
| **Stamina** | Dexterity | Running, swinging weapons, being hit | Resting (standing still), food, refresh potions |
| **Mana** | Intelligence | Casting spells, some special abilities | Natural regeneration, [meditation](/playing/meditation-and-mana/), mana potions |

Practical reading:

- If your **HP** hits zero you die — see [Death & resurrection](/playing/death-and-resurrection/).
- If your **Stamina** runs low you slow down and swing slower; keep [food](/playing/items-and-inventory/)
  on hand. (Exact low-stamina penalties are unverified.)
- If your **Mana** is empty you cannot cast; sit still and [meditate](/playing/meditation-and-mana/)
  or drink a potion.

## Stat caps on this shard

These numbers are read directly from `Config/PlayerCaps.cfg` and are confirmed on the
[shard identity card](/shard/):

| Cap | Value | Config key |
|-----|-------|------------|
| **Total stat cap** | **225** | `TotalStatCap=225` |
| Strength cap | 125 | `StrCap=125` |
| Dexterity cap | 125 | `DexCap=125` |
| Intelligence cap | 125 | `IntCap=125` |
| Enhanced per-stat maximum | 150 | `StrMaxCap`/`DexMaxCap`/`IntMaxCap=150` |

What this means in practice:

- Your three stats together can total **225 points**. You cannot have 125/125/125
  (that is 375) — you must distribute the 225 among the three.
- Any single stat is normally capped at **125**. The **150 enhanced cap** is the ceiling
  that temporary or item-based bonuses may reach above the base 125 (the base trainable
  cap remains 125; the enhanced cap allows buffs to push a single stat higher).
- A common build is something like 100/100/25 or 125/75/25, depending on whether you are
  a warrior (STR/DEX), a mage (INT), or a hybrid — always summing to 225 or less.

## Raising stats

Stats rise as a side effect of **using skills**, not by spending points directly. When
you successfully use a skill tied to a stat, there is a chance that stat ticks up.

- Stat gain chance on this shard: **5%** per qualifying skill use (`PlayerChanceToGainStats=5.0`).
- The stat-gain **time delay is disabled** (`EnablePlayerStatTimeDelay=False`), so gains
  are not throttled by a cooldown window.

Full mechanics — which skills feed which stat, and how a gain is rolled — are on the
[stat gain](/mechanics/stat-gain/) page. The general mapping: combat and labor skills
tend to raise STR/DEX; magical and mental skills raise INT.

### Stat locks (the up/down/locked arrows)

Next to each stat on your character sheet is a small **arrow toggle** with three states:

- **Up arrow (raise)** — this stat is allowed to gain. Default for stats you are training.
- **Down arrow (lower)** — this stat will *give up points* when another locked-up stat
  needs room under the 225 total cap.
- **Lock (locked)** — this stat is frozen; it will neither rise nor fall.

Because the total is capped at 225, once you are at the cap a stat can only rise if
another stat is set to **lower**. Plan your locks: set the stats you want to grow to
**raise**, set a stat you are willing to sacrifice to **lower**, and **lock** anything
you want to hold exactly where it is.

## Skill caps on this shard

Skills are separate from stats but share the same character sheet. From
`Config/PlayerCaps.cfg` (and the [shard card](/shard/)):

- **Individual skill cap: 100.0** (`SkillCap=1000`, stored at 10x). Each skill can reach
  100 without a Power Scroll.
- **Total skill cap: 700.0** (`TotalSkillCap=7000`). The sum of all your skills cannot
  exceed 700 — roughly seven maxed skills.

At the total cap, gaining in one skill requires setting another to **lower** (the same
arrow system as stats applies to each skill row). See [Skill gain](/mechanics/skill-gain/)
for how skills rise.

## The paperdoll and character sheet

Your **paperdoll** is the head-to-toe portrait you open by double-clicking yourself. The
attached **status / character sheet** shows your stats and pools at a glance:

- Current and maximum **Hit Points**, **Stamina**, and **Mana**.
- **Strength**, **Dexterity**, **Intelligence** with their lock arrows.
- Your **name and titles** (fame/karma title, guild abbreviation).
- Weight carried vs. maximum.

How the portrait is composited from body and equipment gumps is documented on the
[paperdoll reference](/reference/paperdoll/). For what each equipment slot is, see
[Items & inventory](/playing/items-and-inventory/). For a field-by-field tour of the
status bar and the other on-screen windows, see the
[User Interface (Gumps)](/playing/interface/) reference.

## Hunger and fitness

Eating [food](/playing/items-and-inventory/) keeps your character fed; a well-fed
character regenerates better and avoids hunger messages (exact hunger mechanics are
unverified on this shard). Carry rations on long trips. Status effects such as poison
that drain your pools are covered under combat survival — see
[Death & resurrection](/playing/death-and-resurrection/) and
[Combat (advanced)](/playing/combat-advanced/).

## Titles, fame, and karma (brief)

Your character also tracks **fame** (renown from killing monsters and deeds) and
**karma** (moral alignment, raised by good acts and lowered by evil ones). Together they
produce a **title** shown on your paperdoll. Karma also interacts with the notoriety
system — killing innocents tanks karma and can turn you red. The full treatment is on
[Notoriety & PvP](/playing/notoriety-and-pvp/).

## See also

- [Stat gain](/mechanics/stat-gain/) and [Skill gain](/mechanics/skill-gain/)
- [Paperdoll](/reference/paperdoll/)
- [Healing](/playing/healing/) and [Meditation & mana](/playing/meditation-and-mana/)
- [Items & inventory](/playing/items-and-inventory/) — carry weight, equipment slots
- [Combat basics](/playing/combat-basics/) and [Notoriety & PvP](/playing/notoriety-and-pvp/)
- [Shard identity card](/shard/) — the caps in one table
