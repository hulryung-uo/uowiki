---
title: Combat Basics
description: How to fight in UO — war mode, equipping a weapon, attacking a target, melee vs ranged range, switching targets, and fleeing.
status: source-verified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (Range = Core.AOS ? 2 : 1)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (GetUsedSkill weapon→skill map, OnEquip StrRequirement gate line 1099, GetDelay stamina/swing-speed line 1541, AccuracySkill = Tactics, DamageBonus from Anatomy/Tactics line 3789)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseSword.cs / BaseAxe.cs / BaseKnife.cs (Swords), BaseBashing.cs / BaseStaff.cs (Macing), BaseSpear.cs / Dagger.cs / Kryss.cs (Fencing), BaseRanged.cs (Archery), BaseThrown.cs (Throwing), Fists.cs (Wrestling)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseRanged.cs (OnSwing stand-still requirement line 61)"
  - "servuo: Scripts/Misc/AOS.cs (Hit Chance Increase cap 45/50, Damage Increase cap 100, direct-damage cap 30/35)"
  - "anima: foundry warrior evals ba2f4/bc201 2026-06-11 (Headless One pack lethality; report 2026-06-11-foundry-claude-stat-block-alone-understates-pack-lethality.md)"
last_verified: 2026-06-23
generated: false
---

This page covers the fundamentals of melee and ranged combat: switching to war mode,
holding a weapon, attacking a target, and getting away. For hit-chance, damage
formulas, special moves and resistances see [Combat (advanced)](/playing/combat-advanced/).
For staying alive see [Healing](/playing/healing/) and
[Death & resurrection](/playing/death-and-resurrection/).

## War mode vs peace mode

Your character is always in one of two states:

- **Peace mode** — the default. You can walk past monsters and other players without
  swinging at anyone, even if you double-click them.
- **War mode** — you will **automatically attack** your current target. Your character
  closes the gap and swings on its own as fast as your weapon allows.

**To toggle war mode:** click the war/peace button on your status bar (the toggle that
shows a peace or war icon), or press the war-mode hotkey (default **Tab** in most
clients — Tab toggles, hold-Tab behavior is client-configurable). When you are in war
mode your character's frame/health bar typically turns red.

You only deal blows while in war mode. If you are in peace mode, double-clicking a
monster just selects/opens it; it does not start a fight.

## Equipping a weapon

**To equip a weapon:**

1. Open your **backpack** (double-click the pack icon, or use the paperdoll).
2. **Double-click** the weapon, or **drag** it onto your paperdoll's hand slot.

A one-handed weapon uses one hand; a two-handed weapon (most axes, spears, bows, and
staves) occupies both hands and prevents holding a shield. To **unequip**, drag the
weapon from the paperdoll back into your pack.

Your character must meet the weapon's **Strength requirement** to equip it at all: if
your Strength is below the requirement you simply **cannot wear it** — "You are not strong
enough to equip that." (`BaseWeapon.cs` `OnEquip`). There is no "swing slower / weaker"
under-strength penalty in the source; it is a hard equip gate. Browse weapons in the
[weapons catalog](/items/catalog/weapons/).

## Weapon choice maps to a combat skill

The weapon you hold determines which skill governs your accuracy. Every swing trains
that skill ([see using & training skills](/playing/using-and-training-skills/)):

- **Swords, axes, large blades** → [Swordsmanship](/skills/swordsmanship/)
- **Maces, hammers, staves** → [Mace Fighting](/skills/mace-fighting/)
- **Daggers, kryss, spears, fencing weapons** → [Fencing](/skills/fencing/)
- **Bows and crossbows** → [Archery](/skills/archery/)
- **Throwing weapons (gargoyle)** → [Throwing](/skills/throwing/)
- **No weapon (bare hands)** → [Wrestling](/skills/wrestling/)

If you are unarmed, you fight with Wrestling automatically — there is no "equip" step.
Wrestling also has defensive value even when you carry a weapon (it can be used to
parry/block in some rules; see [Combat (advanced)](/playing/combat-advanced/)).

Regardless of which weapon skill you use, two support skills increase the **damage** you
deal: [Tactics](/skills/tactics/) is the universal melee damage multiplier, and
[Anatomy](/skills/anatomy/) adds a further damage bonus. Train both alongside your weapon
skill for maximum output.

## Attacking a target

**To attack a monster or player:**

1. **Hold a weapon** (or go bare-handed for Wrestling).
2. Switch to **war mode**.
3. **Double-click** the target, or use a target cursor / "attack last target" hotkey to
   designate it. You can also single-click a creature's health bar to target it in war mode.

Once a target is set in war mode, your character **moves toward it and swings
automatically**. You do not click for each swing — the engine paces your attacks by the
weapon's speed (see [weapon speed below](#weapon-speed-stamina-and-range)). Movement and
targeting are covered in [Movement & travel](/playing/movement-and-travel/) and
[Targeting](/playing/targeting/).

When you successfully designate a hostile target, attacking it may flag you for
**criminal/aggressor** notoriety depending on the target — see
[Notoriety & PvP](/playing/notoriety-and-pvp/) before attacking other players or
"innocent" (blue) NPCs.

## Range: melee adjacency vs ranged line of sight

- **Melee weapons** (and Wrestling) require you to be **adjacent** to the target — one
  tile away, including diagonals. Your character walks into range on its own when you set
  a target in war mode. (The bandage/beneficial action range in this shard is 2 tiles, per
  `Bandage.cs`; melee attack reach is the adjacent tile.)
- **Ranged weapons** (bows, crossbows, throwing) hit at a **distance** but require a clear
  **line of sight** — no wall, tree, or obstacle directly between you and the target. If
  line of sight is broken, your shots miss or do not fire until you reposition.

Archers and throwers must **stand still briefly to fire**: a ranged swing only lands once
you have been stationary since your last move (about **0.25 s** on this SE/EJ-era shard —
the delay is 0.25/0.5/1 s by era), so moving resets that timer and delays the shot
(`BaseRanged.cs` `OnSwing`). See [Archery](/skills/archery/) and [Throwing](/skills/throwing/).

## Switching and "last target"

You can change who you are fighting at any time:

- **Switch target:** double-click a new enemy (or target its health bar). Your character
  immediately redirects its swings to the new target.
- **Last target:** most clients support an "attack last target" and a "set last target"
  hotkey, letting you re-acquire your previous target without clicking. Razor/assist tools
  add more target macros. See [Targeting](/playing/targeting/).

## Weapon speed, stamina, and range

- **Weapon speed** sets how often you swing. Faster weapons (daggers, fencing weapons)
  swing more often for less damage per hit; slow weapons (war hammers, two-handed axes)
  hit hard but slowly.
- **Stamina** directly affects your swing speed: the swing-delay formula divides by your
  stamina, so **as stamina falls your swings come slower** (`BaseWeapon.cs` `GetDelay` —
  the SE/ML path subtracts `Stam/30` swing-ticks, faster the more stamina you have). Swing
  speed is capped at one swing per **1.25 s** no matter how high your stamina or Swing-Speed
  bonuses. Running and being hit drain stamina; eat [food](/items/catalog/food-drink/) and
  rest to recover. Detailed swing-speed mechanics are in
  [Combat (advanced)](/playing/combat-advanced/).

## Packs are far more dangerous than the stat block suggests

A creature's [bestiary](/bestiary/) entry shows its stats **one-on-one**. Damage from a
**group** stacks because every member swings on the same window, so a monster that is
trivial alone can overwhelm a fresh character in seconds when it spawns in numbers.

Worked example (anima foundry warrior evals, 2026-06-11): a
[Headless One](/bestiary/humanoids/headless-one/) is a pushover singly, but **eight**
spawned together killed a Swordsmanship/Tactics/Healing-35 warrior — katana and 100
bandages — in under ~110 seconds across multiple fresh characters. With **four** of the
same creature, that build survives and trains safely. The rule of thumb that held in
testing: *trivial 1-on-1, lethal at ~8-up against a ~35-skill melee character, roughly
4 concurrent is farmable.*

Practical takeaway for low-skill characters: pull packs apart, fight in a doorway or
chokepoint so only one or two reach you at a time, and keep an exit — see
[Fleeing](#fleeing) below. The danger scales with count and your skill, not with the
single-target numbers on the page.

## Fleeing

**To break off a fight and run:**

1. **Switch to peace mode** so you stop auto-attacking.
2. **Run away** — click far ahead repeatedly to keep running (running costs stamina).
3. Use terrain and **line of sight** to break a ranged attacker's shots, or
   [Hide](/playing/hiding-and-stealth/) once you have a moment out of sight.
4. If you have travel magic, **Recall** to a safe rune (see
   [Movement & travel](/playing/movement-and-travel/)) — but note casting can be disrupted
   if you are being hit (see [Combat (advanced)](/playing/combat-advanced/)).

A fleeing target that out-distances its attacker will eventually be left alone, since
melee enemies must stay adjacent to swing and ranged enemies need line of sight.

## See also

- [Combat (advanced)](/playing/combat-advanced/) — hit chance, damage, resistances, special moves
- [Healing](/playing/healing/) — bandages, heal spells and potions
- [Tactics](/skills/tactics/), [Anatomy](/skills/anatomy/) — damage boosters
- [Death & resurrection](/playing/death-and-resurrection/)
- [Bestiary](/bestiary/) — what you are fighting and its resistances
