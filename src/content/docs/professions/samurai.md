---
title: Samurai
description: The Bushido swordsman — a dexxer whose discipline turns swings into burst damage and counter-defense. Skills, build, play, gear, income.
status: source-verified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Bushido/ (Confidence.cs, Evasion.cs, CounterAttack.cs, LightningStrike.cs, MomentumStrike.cs, HonorableExecution.cs)"
  - "servuo: Scripts/Services/Virtues/Honor.cs (Honor virtue + Perfection, scales with Bushido)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (CheckParry uses Bushido; two-handed parry without shield)"
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000 i.e. 700.0, TotalStatCap=225)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The samurai is a melee fighter who uses [Bushido](/skills/bushido/) to amplify the warrior's
craft: honor-based burst damage, reactive defense, and tighter weapon special-move play. On
this shard Bushido is real (the EJ expansion stack includes Samurai-Empire-era skills). At
heart it's still a [warrior](/professions/warrior/) — Bushido is the seasoning, the weapon is
the meal.

## Core skills

- [Bushido](/skills/bushido/) — the discipline skill; sets the power and success of its abilities and improves parrying with two-handed weapons.
- A weapon skill — most often [Swordsmanship](/skills/swordsmanship/) (katana, no-dachi, lajatang), but [Fencing](/skills/fencing/) and [Mace Fighting](/skills/mace-fighting/) work too.
- [Tactics](/skills/tactics/) and [Anatomy](/skills/anatomy/) — the damage multipliers.
- [Parrying](/skills/parrying/) — Bushido synergizes with it; a samurai can parry effectively even with a two-handed weapon.
- [Healing](/skills/healing/) for bandages; optional [Resisting Spells](/skills/resisting-spells/).

## The build

There is **no dedicated samurai template page** yet. Build it as a dexxer with a Bushido slot:
start from the [Warrior Template](/templates/warrior/) for stats, weapon order, and a hunting
route, then add [Bushido](/skills/bushido/). A common spread is weapon + Tactics + Anatomy +
Bushido + Parrying + Healing + one more. See [7x GM Templates](/templates/seven-gm/) for the
700-point math. Bushido is also a pillar of the [sampire](/professions/sampire/).

## How to play it

[Combat Basics](/playing/combat-basics/) covers the swing loop; [Combat Advanced](/playing/combat-advanced/)
covers weapon special moves and speed — essential, because Bushido is built around them.
[Magic Schools](/playing/magic-schools/) places Bushido among the schools.

The toolkit (all confirmed under `servuo: Scripts/Spells/Bushido/`):

- **Honorable Execution** — a weapon special move (`HonorableExecution.cs`, needs 25 Bushido): a damage swing that, on the killing blow, restores you and grants a bonus. Distinct from the **Honor *virtue*** (`Scripts/Services/Virtues/Honor.cs`) you invoke on a creature for the *Perfection* damage bonus that scales with your Bushido — both are common openers for big fights.
- **Confidence** — a defensive heal-over-time that rewards successful parries.
- **Evasion** — a short window of greatly improved blocking.
- **Counter Attack** — strike back automatically when you parry.
- **Lightning Strike** — a fast, cheap special that boosts your next hit's accuracy/crit.
- **Momentum Strike** — hits your target and others around it; pairs with crowd fighting.

These layer on top of your weapon's own primary/secondary specials — read the weapon entry and
chain them with the Bushido abilities.

## Gear

- [Weapons](/items/weapons/) and the [weapon catalog](/items/catalog/weapons/) — two-handed Swordsmanship weapons (no-dachi) suit Bushido's parry synergy; pick mods for leech and swing speed.
- [Armor](/items/armor/) — balanced resists; a shield is optional thanks to two-handed parrying.
- [Magic item properties](/magic/) — Hit Lower Defense, Hit Leech, and Swing Speed Increase shine on a samurai. Carry **bandages**.

## Making a living

Samurai farm dungeons like any dexxer, with Bushido giving better single-target burst (Honor
+ Lightning Strike) and crowd control (Momentum Strike). Clear rooms, loot corpses, and sell
surplus via [Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Warrior](/professions/warrior/) — the dexxer base
- [Sampire](/professions/sampire/) — Bushido + Necromancy leech hybrid
- [Ninja](/professions/ninja/) — the other Tokuno discipline, built on stealth
- [Bushido skill](/skills/bushido/) · [Combat Advanced](/playing/combat-advanced/)
