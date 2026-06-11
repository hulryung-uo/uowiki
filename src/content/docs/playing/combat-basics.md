---
title: Combat Basics
description: How to fight in UO — war mode, equipping a weapon, attacking a target, melee vs ranged range, switching targets, and fleeing.
status: unverified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (range = AOS ? 2 : 1)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
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

Your character must meet the weapon's **Strength requirement** to wield it effectively;
under-strength penalties apply (unverified). Browse weapons in the
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

Archers and throwers generally must **stand still to fire** in AOS-era rules (moving
delays or cancels the shot — unverified specifics); see [Archery](/skills/archery/) and
[Throwing](/skills/throwing/).

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
- **Stamina** affects your swing speed and your ability to keep moving. Running and being
  hit drain stamina; low stamina slows your attacks (unverified exact thresholds). Eat
  [food](/items/catalog/food-drink/) and rest to recover. Detailed swing-speed mechanics
  are in [Combat (advanced)](/playing/combat-advanced/).

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
