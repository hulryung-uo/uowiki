---
title: Paladin
description: The holy warrior — a dexxer who casts Chivalry off tithing points. Core skills, build, how to fight, gear, and income in one place.
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Chivalry/ (PaladinSpell.cs tithing cost; ConsecrateWeapon.cs, EnemyOfOne.cs, DivineFury.cs, CloseWounds.cs, CleanseByFire.cs, HolyLight.cs, DispelEvil.cs, RemoveCurse.cs, SacredJourney.cs)"
last_verified: 2026-06-11
generated: false
---

## What this profession is

The paladin is a melee fighter with a holy spellbook bolted on. At its core it's a
[warrior](/professions/warrior/) — weapon, Tactics, bandages — but [Chivalry](/skills/chivalry/)
layers on self-buffs, light healing, curse removal, and free travel. Chivalry on this shard
is real (the expansion stack includes AOS-era skills), and it costs no mana: its power runs
on **tithing points**.

## Core skills

- [Chivalry](/skills/chivalry/) — the holy school. Higher Chivalry means stronger, more reliable spell effects and longer buff durations.
- **A weapon skill** — [Swordsmanship](/skills/swordsmanship/), [Fencing](/skills/fencing/), or [Mace Fighting](/skills/mace-fighting/). Chivalry is support; your weapon does the killing.
- [Tactics](/skills/tactics/) and [Anatomy](/skills/anatomy/) — the two damage multipliers, exactly as for a warrior; Anatomy also powers bandage healing.
- [Healing](/skills/healing/) — bandages remain your bread-and-butter recovery; Close Wounds only tops it up.
- Optional [Focus](/skills/focus/) or [Resisting Spells](/skills/resisting-spells/) for survivability against hostile casters.

## Tithing points, not mana

Chivalry spells are paid for in **tithing points**, not mana. You earn them by donating gold
at a shrine (use the shrine and choose to tithe). Each cast spends points from that pool;
when it's empty, re-tithe. This is confirmed in the emulator — `PaladinSpell.cs` checks and
deducts `Caster.TithingPoints` rather than mana (`servuo: Scripts/Spells/Chivalry/PaladinSpell.cs`).
Keep a few thousand gold tithed so buffs are always available.

## The build

There is **no dedicated paladin template page** on the wiki yet. Build it as a dexxer with a
Chivalry slot: start from the [Warrior Template](/templates/warrior/) for stats, weapon-skill
order, and a hunting route, then swap one utility slot for [Chivalry](/skills/chivalry/). A
typical endgame spread is weapon + Tactics + Anatomy + Healing + Chivalry + Parrying + one
more. For fitting seven skills under the 700-point cap see [7x GM Templates](/templates/seven-gm/).
(If you also want dark magic and life-leech, see the [sampire](/professions/sampire/), which
fuses Chivalry with Necromancy and Bushido.)

## How to play it

Read [Magic Schools](/playing/magic-schools/) for where Chivalry sits among the casting
schools, and [Spellcasting](/playing/spellcasting/) for the cast mechanics. For the melee
half, [Combat Basics](/playing/combat-basics/) then [Combat Advanced](/playing/combat-advanced/)
cover the swing loop and weapon special moves; [Healing](/playing/healing/) covers bandage timing.

The loop: tithe gold first. Before a fight, cast **Consecrate Weapon** (matches your damage
type to the target's weakest resist) and **Enemy of One** (big damage bonus versus a single
creature type — but you take extra from everything else). **Divine Fury** adds swing speed at
the cost of defense. In a pinch, **Close Wounds** heals and **Cleanse by Fire** / **Remove
Curse** strip poison and curses; **Holy Light** is an area nuke; **Dispel Evil** scatters
summons; **Sacred Journey** is the paladin's Recall and gate. All of these are confirmed files
under `servuo: Scripts/Spells/Chivalry/`.

## Gear

- [Weapons](/items/weapons/) and the [weapon catalog](/items/catalog/weapons/) — pick to match your weapon skill; mods that help dexxers (hit-leech, swing speed) apply normally.
- [Armor](/items/armor/) — favor balanced resists; a shield enables [Parrying](/skills/parrying/).
- [Magic item properties](/magic/) — Faster Casting matters little here (few casts), so prioritize melee and survivability mods. Carry **bandages**.

## Making a living

Paladins farm like warriors: clear dungeon rooms and loot corpses. The Chivalry kit makes
**undead and "evil" content** especially profitable — Consecrate plus Enemy of One shreds a
graveyard or undead dungeon, and the holy buffs cost only the gold you tithe. Sell surplus
loot via [Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Warrior](/professions/warrior/) — the dexxer base this build sits on
- [Sampire](/professions/sampire/) — the leech-melee hybrid that also uses a little Chivalry
- [Chivalry skill](/skills/chivalry/) · [Magic Schools](/playing/magic-schools/)
