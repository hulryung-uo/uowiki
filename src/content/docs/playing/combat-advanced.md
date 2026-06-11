---
title: Combat (Advanced)
description: Hit chance and defense, damage components, damage types and resistances, weapon speed, special moves, spell disruption, and mounted combat.
status: unverified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (bandage/beneficial range)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page builds on [Combat basics](/playing/combat-basics/) with the systems that decide
whether you hit, how much damage you deal, and how to use special moves and mounts. Exact
formulas vary by ServUO build; numbers below are marked **(unverified)** unless trivially
known, and should be confirmed against the relevant `Scripts/` files or in-game logs.

## Hit chance and defense

**Whether a swing lands** is a contest between the attacker's accuracy and the defender's
ability to avoid the blow:

- **Attacker side:** your **weapon skill** ([Swordsmanship](/skills/swordsmanship/),
  [Mace Fighting](/skills/mace-fighting/), [Fencing](/skills/fencing/),
  [Archery](/skills/archery/), [Throwing](/skills/throwing/), or
  [Wrestling](/skills/wrestling/)) plus the weapon's hit-chance properties.
- **Defender side:** their own weapon skill (or [Wrestling](/skills/wrestling/) if
  unarmed), and especially [Parrying](/skills/parrying/) when holding a shield or
  two-handed weapon — a successful parry blocks the hit outright.

In AOS-and-later rules the two values are compared and turned into a percentage chance to
hit (the precise curve is **unverified** here — confirm in `Scripts/Items/Weapons/` /
combat code). Higher relative skill, and weapon "Hit Chance Increase" / defender "Defense
Chance Increase" item properties, shift the odds.

## Damage components

When a hit lands, its damage is built from several stacked components:

- **Base weapon damage** — the weapon's min–max damage range (see
  [weapons catalog](/items/catalog/weapons/)).
- **[Tactics](/skills/tactics/) bonus** — the universal melee damage multiplier; scales
  with your Tactics skill.
- **[Anatomy](/skills/anatomy/) bonus** — an additional damage percentage from Anatomy.
- **Strength bonus** — higher Strength adds a damage bonus
  (see [character & stats](/playing/character-and-stats/) and [Mechanics](/mechanics/)).
- **Item modifiers** — "Damage Increase", slayer bonuses vs the right creature type, and
  elemental damage conversions.

The exact percentages and how they combine are **(unverified)** in this page — see
[Mechanics](/mechanics/) and the weapon scripts for the build-specific numbers. The
qualitative rule to remember: **weapon + Tactics + Anatomy + Strength** is the core melee
damage stack, and training all of them together is what makes a melee character hit hard.

## Damage types and resistances

Every hit deals one or more of **five damage types**:

- **Physical**
- **Fire**
- **Cold**
- **Poison**
- **Energy**

The defender reduces incoming damage by their **resistance** to that type:

- **Players** get resistances from worn [armor](/items/catalog/armor/) and
  [jewelry](/items/catalog/jewelry/); each piece lists its Physical/Fire/Cold/Poison/Energy
  resist values, and they sum up to a capped total per type.
- **Creatures** have their own innate resistances — listed per monster in the
  [Bestiary](/bestiary/). A dragon shrugs off fire; an elemental resists its own element.

**To fight efficiently:** check the target's weaknesses in the
[Bestiary](/bestiary/) and bring a weapon (or spells) that deal the damage type it
resists *least*. Conversely, wear armor that covers the damage types the enemy deals.

## Weapon speed and stamina

- **Swing speed** is set by the weapon's base speed, your **Stamina**, and swing-speed
  item bonuses. More stamina and "Swing Speed Increase" mean more swings per second.
- **Low stamina slows your attacks** and your movement. Stamina drains from running and
  from being hit; eat [food](/items/catalog/food-drink/) and rest to recover. (Exact
  swing-speed formula is **unverified** — see weapon scripts.)
- Fast weapons favor special-move spam and on-hit effects; slow weapons favor big single
  hits. See [Combat basics](/playing/combat-basics/#weapon-speed-stamina-and-range).

## Special moves (primary and secondary)

Most weapons grant **two special moves** — a **primary** and a **secondary** ability —
unlocked at certain [Tactics](/skills/tactics/) and/or weapon-skill thresholds. Examples
of common effects (the exact set depends on the weapon): armor-ignoring strikes, bleeding
wounds, mortal/wound effects that block healing, paralyzing blows, area hits, and
disarms.

**To use a special move:**

1. Open the weapon-ability bar/gump in your client.
2. **Toggle the primary or secondary ability on**; it stays armed.
3. Land your **next qualifying hit** — the ability fires and consumes **mana**.

Special moves **cost mana** (amount varies by ability and is reduced by mastery — **exact
costs unverified**). If you lack the mana when the hit lands, the special does not trigger.
[Bushido](/skills/bushido/) and [Ninjitsu](/skills/ninjitsu/) add their own weapon
specials. See the individual weapon-skill pages for which moves each weapon type offers.

## Spell and weapon disruption ("fizzle")

- **Casting while being hit can be disrupted.** If you take a hit (or otherwise lose
  concentration) mid-cast, the spell **fizzles** — it fails, you may lose reagents/mana,
  and you must recast. This is why mages kite and heal between casts; see
  [Spellcasting](/playing/spellcasting/) and [Magery](/skills/magery/).
- A bandage application can likewise **slip** ("Your fingers slip!") or fail to finish if
  you are interrupted or move out of range — see [Healing](/playing/healing/).
- Holding still, keeping distance, and protective spells/abilities reduce disruption
  (resisting-spells and protection effects are **unverified** in specifics — see
  [Resisting Spells](/skills/resisting-spells/)).

## Mounts in combat

- **Riding a mount** lets you move at the faster mounted speed and chase or flee more
  effectively. You can fight from horseback with melee and ranged weapons.
- Some abilities and special moves (notably certain dismount specials, and lances) can
  **knock you off your mount**; on foot you move slower. (Specifics **unverified**.)
- Mounts are creatures: they can be targeted and, if a war-horse/pet, healed or killed.
  See [Taming & pets](/playing/taming-and-pets/) and
  [Movement & travel](/playing/movement-and-travel/).

## Fleeing and line of sight (recap)

To disengage: drop to **peace mode**, run, and use terrain to break a ranged attacker's
**line of sight**. Melee enemies must stay adjacent to swing; ranged enemies need an
unobstructed line. Once out of sight you can [Hide](/playing/hiding-and-stealth/) or
**Recall** away. Full procedure in
[Combat basics → Fleeing](/playing/combat-basics/#fleeing).

## See also

- [Combat basics](/playing/combat-basics/)
- [Tactics](/skills/tactics/), [Anatomy](/skills/anatomy/), [Parrying](/skills/parrying/)
- [Healing](/playing/healing/), [Poison & status](/playing/poison-and-status/)
- [Bestiary](/bestiary/) — creature resistances and damage types
- [Mechanics](/mechanics/) — the underlying numbers
