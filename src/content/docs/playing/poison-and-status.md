---
title: Poison & Status Effects
description: Poison levels and curing, plus paralysis, bleeding, mortal strike, hunger, and curses — how each works and how to remove it.
status: unverified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (bandage cure thresholds and poison-level scaling)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page covers harmful states that affect your character and how to clear each one.
Healing methods are detailed in [Healing](/playing/healing/); combat-applied effects are
in [Combat (advanced)](/playing/combat-advanced/).

## Poison

**Poison** deals damage over time: once poisoned, you take small **ticks** of damage
repeatedly until it is cured or wears off. Higher poison levels tick harder and resist
curing.

### Poison levels

Poison comes in escalating levels (weakest to strongest):

1. **Lesser**
2. **Regular**
3. **Greater**
4. **Deadly**
5. **Lethal** (creature/special — strongest; availability shard-dependent, unverified)

The higher the level, the more damage per tick and the **harder it is to cure** — cure
chances explicitly divide by the poison level in `Bandage.cs`.

### How you get poisoned

- **Monsters** — many creatures poison on hit or with a venom attack (see the
  [Bestiary](/bestiary/) for which ones and at what level).
- **Poisoned weapons** — a player who has applied venom to a blade via
  [Poisoning](/skills/poisoning/) can poison you when they hit.
- **Traps** — poison-trapped chests/containers (see [Remove Trap](/skills/remove-trap/)
  and [Lockpicking](/skills/lockpicking/)).
- **Food/drink** — eating something poisoned can poison you
  ([food & drink](/items/catalog/food-drink/)).

### How to cure poison

**To remove poison, use any of:**

- **Bandage** — both [Healing](/skills/healing/) **≥ 60** and [Anatomy](/skills/anatomy/)
  **≥ 60** required (verified, `Bandage.cs`); cure chance =
  `(Healing − 30)/50 − (PoisonLevel × 0.1) − (Slips × 0.02)`. Double-click bandage → target
  the poisoned person.
- **Cure spell** — 2nd-circle [Magery](/skills/magery/) cure; or **Arch Cure** (4th
  circle) to cure an area.
- **Cure potion** — instant; stronger potions cure higher levels (effectiveness
  **unverified**). See [potions](/items/catalog/potions/).
- **Arch Cure / Chivalry Cleanse / Mysticism cure** — alternate cures depending on your
  skills (availability unverified).

**Important:** the lesser **Heal/Greater Heal** spells **will not heal a poisoned target** —
you must **cure first**, then heal HP. With bandages you can keep applying them; a bandage
on a poisoned patient tries the cure before healing. Full detail in
[Healing](/playing/healing/).

## Paralysis

**Paralyzed** characters cannot move or act for the duration.

- **Sources:** the **Paralyze** spell ([Magery](/skills/magery/) 5th circle), a
  **Paralyze Field**, the **paralyzing blow** weapon special, and some creatures' attacks.

**To break paralysis:**

- **Take damage** — getting hit typically breaks the Paralyze spell early (a hostile action
  against you ends it).
- **A trapped pouch** — carry a pouch trapped with an explosion potion (made via
  [Tinkering](/skills/tinkering/)/[Alchemy](/skills/alchemy/)); double-click it while
  paralyzed to instantly free yourself. This is the standard PvP counter.
- **Wait it out** — the effect expires after its duration.

[Resisting Spells](/skills/resisting-spells/) lowers the duration/chance of magic
paralysis (unverified specifics).

## Bleeding and Mortal Strike

These are **weapon special-move** effects (see
[Combat (advanced)](/playing/combat-advanced/#special-moves-primary-and-secondary)) — exact
numbers **unverified**:

- **Bleed (Bleed Attack)** — inflicts a wound that deals damage over several seconds. A
  **bandage** can bind the wound and stop the bleeding (`Bandage.cs` handles bleed in the
  same flow as poison/heal).
- **Mortal Strike / Mortal Wound** — for its duration the victim **cannot be healed** by
  normal means; you must wait it out or use specific counters. A bandage on a mortally
  wounded patient reports the wound rather than healing.

## Hunger

Characters get **hungry** over time. If you ignore food:

- Hunger reduces regeneration and can impair stats/stamina recovery (penalty specifics
  **unverified**).
- **To eat:** double-click **[food](/items/catalog/food-drink/)** in your pack — fruit,
  bread, cooked meat ([Cooking](/skills/cooking/)) — until you are full ("You are simply
  too full to eat any more.").

Keep some food on hand, especially on long trips or grinds, so hunger doesn't quietly slow
your recovery.

## Curses and stat debuffs

Various spells/effects **lower your stats or resistances** temporarily:

- **Curse** ([Magery](/skills/magery/) 4th circle) — lowers Strength/Dexterity/Intelligence
  (and may lower resists in AOS).
- **Clumsy / Weaken / Feeblemind** (1st circle) — each lowers a single stat.
- **Mass Curse** — area version.
- Creature **auras** and **debuff** attacks can apply similar reductions.

**To remove a curse/stat debuff:**

- Cast **Remove Curse** ([Chivalry](/skills/chivalry/)) where available, or
- **Wait for the effect to expire** (most stat debuffs are timed), or
- Counter with stat-buff spells (Bless, Strength, Agility, Cunning) to offset the
  reduction.

(Exact durations and stacking rules are **unverified** — see [Magery](/skills/magery/) and
[the magic index](/magic/).)

## Quick reference — what removes what

- **Poison** → bandage (Healing/Anatomy ≥ 60), Cure/Arch Cure spell, Cure potion.
- **Paralysis** → take damage, or trapped pouch, or wait.
- **Bleed** → bandage, or wait.
- **Mortal Strike** → wait it out (blocks healing); specific counters only.
- **Hunger** → eat food.
- **Curse / stat debuff** → Remove Curse, counter-buff, or wait.

## See also

- [Healing](/playing/healing/) — curing and healing procedures
- [Combat (advanced)](/playing/combat-advanced/) — special moves that cause these states
- [Poisoning](/skills/poisoning/), [Magery](/skills/magery/), [Chivalry](/skills/chivalry/)
- [Bestiary](/bestiary/) — which creatures poison or debuff
- [Potions](/items/catalog/potions/), [food & drink](/items/catalog/food-drink/)
