---
title: Poison & Status Effects
description: Poison levels and curing, plus paralysis, bleeding, mortal strike, hunger, and curses — how each works and how to remove it.
status: source-verified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (bandage cure thresholds Healing/Anatomy >= 60 and chance = (Healing-30)/50 - PoisonLevel*0.1 - Slips*0.02; bleed bound in same flow; Mortal wound blocks healing)"
  - "servuo: Server/Poison.cs + Scripts/Misc/Poison.cs (Lesser=0/Regular=1/Greater=2/Deadly=3/Lethal=4 registered; PoisonTimer ticks damage over time)"
  - "servuo: Scripts/Spells/Second/Cure.cs (2nd circle, chance = 10000 + Magery*75 - (RealLevel+1)*penalty), Scripts/Spells/Fourth/ArchCure.cs (4th circle, area cure of all targets in range 2)"
  - "servuo: Scripts/Spells/Fifth/Paralyze.cs (AOS duration = DamageSkill/10 - ResistSkill/10), Server/Mobile.cs (Damage() clears Paralyzed when amount > 0)"
  - "servuo: Scripts/Items/Containers/TrapableContainer.cs (explosion trap deals self-damage that breaks paralysis)"
  - "servuo: Scripts/Spells/Fourth/Curse.cs (lowers Str/Dex/Int via AddStatCurse)"
last_verified: 2026-06-23
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

1. **Lesser** (internal level 0)
2. **Regular** (1)
3. **Greater** (2)
4. **Deadly** (3)
5. **Lethal** (4 — strongest; mostly creature/special venom)

All five are registered in the server (`Server/Poison.cs` / `Scripts/Misc/Poison.cs`), so
**Lethal does exist** on this shard. The higher the level, the more damage per tick (poison
runs on a repeating `PoisonTimer` that ticks damage scaled to the victim's hit points until
cured or expired) and the **harder it is to cure** — both the bandage cure chance and the
Cure-spell chance get a penalty multiplied by the poison level.

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
- **Cure spell** — 2nd-circle [Magery](/skills/magery/) (`Cure.cs`); cure chance scales with
  Magery and is penalized by poison level: roughly `(10000 + Magery×75 − (level+1)×penalty) /
  100` vs a d100 roll, so higher Magery cures reliably and high poison levels can still fail.
- **Arch Cure** — 4th-circle [Magery](/skills/magery/) (`ArchCure.cs`); cures every valid
  target within **2 tiles**, using the same per-target chance — the area cure.
- **Cure potion** — instant; stronger potions cure higher levels (effectiveness
  **unverified**). See [potions](/items/catalog/potions/).
- **Chivalry Cleanse by Fire / Mysticism Cleansing Winds** — alternate cures depending on
  your skills (availability/specifics unverified).

**Important:** the lesser **Heal/Greater Heal** spells **will not heal a poisoned target** —
you must **cure first**, then heal HP. With bandages you can keep applying them; a bandage
on a poisoned patient tries the cure before healing. Full detail in
[Healing](/playing/healing/).

## Paralysis

**Paralyzed** characters cannot move or act for the duration.

- **Sources:** the **Paralyze** spell ([Magery](/skills/magery/) 5th circle), a
  **Paralyze Field**, the **paralyzing blow** weapon special, and some creatures' attacks.

**To break paralysis:**

- **Take damage** — any blow that deals damage clears paralysis immediately
  (`Mobile.Damage` sets `Paralyzed = false` whenever the amount is greater than 0).
- **A trapped pouch** — you can still double-click a container while paralyzed, so opening
  a **container trapped with an explosion trap** ([Tinkering](/skills/tinkering/)) sets the
  trap off; the explosion's self-damage then breaks the paralysis (it works *because* the
  trap damages you, per the rule above). This is the standard PvP counter.
- **Wait it out** — the effect expires after its duration.

[Resisting Spells](/skills/resisting-spells/) shortens magic paralysis: in AOS the
duration is `(caster's damage skill − your Resisting Spells)/10` seconds, so higher Resist
directly cuts the time you are held (`Paralyze.cs`).

## Bleeding and Mortal Strike

These are **weapon special-move** effects (see
[Combat (advanced)](/playing/combat-advanced/#special-moves-primary-and-secondary)) — exact
damage/duration numbers **unverified**, but the bandage interactions below are confirmed in
`Bandage.cs`:

- **Bleed (Bleed Attack)** — inflicts a wound that deals damage over several seconds. A
  **bandage binds the wound and stops the bleeding** ("You bind the wound and stop the
  bleeding") — `Bandage.cs` ends the bleed in the same flow it uses for poison/heal.
- **Mortal Strike / Mortal Wound** — for its duration the victim **cannot be healed** by
  normal means. A bandage on a mortally wounded patient just reports the wound and heals
  nothing (`Bandage.cs` checks `MortalStrike.IsWounded` before applying any heal); wait it
  out or use a specific counter.

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

- **Curse** ([Magery](/skills/magery/) 4th circle) — lowers **Strength, Dexterity, and
  Intelligence** together (`Curse.cs` applies a stat curse to all three). On this shard it
  does **not** lower your elemental resistances — despite the OSI-era reputation, the server
  code only debuffs the three stats.
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
