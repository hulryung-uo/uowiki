---
title: Healing
description: The full healing reference — bandages (timing, cure, resurrection), Magery heal/cure spells, healing potions, and Veterinary for pets.
status: source-verified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (GetDelay timing, Range = Core.AOS ? 2 : 1, EndHeal cure/res skill thresholds + chances, AOS heal min/max, slip 0.35 reduction, CheckSkill cap 120, pet res 0.1 skill loss, Khaldun/CanFit res block)"
  - "servuo: Scripts/Spells/First/Heal.cs, Scripts/Spells/Fourth/GreatHeal.cs (heal blocked on poisoned target)"
  - "servuo: Scripts/Spells/Second/Cure.cs, Scripts/Spells/Fourth/ArchCure.cs (cure circle + chance formula, Arch Cure area cure)"
  - "servuo: Scripts/Items/Consumables/BaseHealPotion.cs + LesserHealPotion/HealPotion/GreaterHealPotion.cs (per-potion cooldown 3/8/10 s, blocked while poisoned/mortal)"
last_verified: 2026-06-23
generated: false
---

This is the central reference for restoring hit points and clearing poison, by every
method: **bandages** ([Healing](/skills/healing/) / [Veterinary](/skills/veterinary/)),
**spells** ([Magery](/skills/magery/)), and **potions**
([potions catalog](/items/catalog/potions/)). For poison itself see
[Poison & status](/playing/poison-and-status/); for dying and getting back up see
[Death & resurrection](/playing/death-and-resurrection/).

## Bandages — how to use

**To bandage a wound:**

1. Make sure you have **bandages** in your backpack (cloth crafted with
   [Tailoring](/playing/crafting/), or bought from a healer/vendor).
2. **Double-click** a bandage in your pack — you get a target cursor.
3. **Target** yourself, an injured ally, or a pet. You must be within range
   (**2 tiles** on this AOS shard, per `Bandage.cs` `Range`).
4. Wait for the timer to finish. On success: "You finish applying the bandages." and HP
   is restored.

One bandage is consumed per application. Higher Dexterity makes each application faster;
higher [Healing](/skills/healing/) and [Anatomy](/skills/anatomy/) heal **more HP** and
raise success/cure/resurrection chances. Bandaging trains your Healing (or Veterinary)
and the matching secondary skill up to **120** skill (`CheckSkill` cap in `Bandage.cs`).

## Bandage timing (verified)

From `Scripts/Items/Resource/Bandage.cs` `GetDelay` (AOS path). Times are in **seconds**;
`Dex` is the healer's Dexterity:

- **Self-heal:** `max(4, min(8, ceil(11 − Dex/20)))`. So 4 s at very high Dex, up to 8 s
  at low Dex.
- **Healing another person:** `max(2, ceil(4 − Dex/60))`. As fast as 2 s.
- **[Veterinary](/skills/veterinary/) on a pet:** a flat **2 s**.
- **Resurrection via bandage:** on this AOS/EJ shard a res bandage takes the **same time
  as healing that target** — the AOS delay branches do **not** add the `resDelay = 5.0`
  bonus (that +5 s only applies on the legacy pre-AOS dex branches). So res'ing another
  player runs on the 2 s "heal another" timer; a self-res runs on the 4–8 s self-heal timer.

You can only run **one bandage timer at a time** — starting a new one cancels the old.

## Slipping, interruption, and movement

- If you take a hit or are disturbed mid-application your **fingers can slip** ("Your
  fingers slip!"). Each slip reduces the HP healed (in AOS, by ~35% per slip) and lowers
  cure/res chance.
- If you **move out of range** (more than 2 tiles from the patient) before the timer
  ends, you get "You did not stay close enough to heal your target." and the heal fails.
- If **you die** before it finishes: "You were unable to finish your work before you
  died." and it fails.

**Best practice:** stand still and stay adjacent while a bandage finishes, especially when
healing someone else.

## How much a bandage heals

The amount scales with **Healing** and **Anatomy** (AOS path, `Bandage.cs`):

- `min = Anatomy/8 + Healing/5 + 4`
- `max = Anatomy/6 + Healing/2.5 + 4`
- The actual heal is a random value between `min` and `max`, reduced by slips, and reduced
  if you simultaneously cured poison/bleed in the same application.

In short: **more Anatomy and more Healing = bigger heals.** Maxing both
([Healing](/skills/healing/) 100, [Anatomy](/skills/anatomy/) 100) gives the largest and
most reliable bandage heals.

## Curing poison with a bandage

A bandage on a **poisoned** patient attempts to cure the poison instead of (or before)
healing HP.

- **Skill requirement (verified):** both **Healing ≥ 60** and **Anatomy ≥ 60**
  (`checkSkills = healing >= 60.0 && anatomy >= 60.0`).
- **Cure chance** = `(Healing − 30)/50 − (PoisonLevel × 0.1) − (Slips × 0.02)`. Higher
  poison levels (deadly > greater > regular > lesser) are harder to cure; slips hurt.
- On success: "You have been cured of all poisons." On failure: "You have failed to cure
  your target!" — apply another bandage and try again.

See [Poison & status](/playing/poison-and-status/) for poison levels and other cures.

## Resurrecting with a bandage

A bandage applied to a **dead** player (or dead pet, via Veterinary) can bring them back.

- **Skill requirement (verified):** both **Healing ≥ 80** and **Anatomy ≥ 80**
  (`checkSkills = healing >= 80.0 && anatomy >= 80.0`). For pets, the Veterinary/Animal Lore
  equivalents apply.
- **Success chance** = `(Healing − 68)/50 − (Slips × 0.02)`.
- On success the patient gets a **resurrection gump** to accept; resurrecting a dead pet
  costs the pet a small skill loss (0.1 per skill, looped over every skill — `Bandage.cs`).
- The res bandage takes the **same time as healing that target** on this AOS/EJ shard (the
  +5 s legacy res delay does not apply here). The patient's body must be at a spot that
  "can fit" a corpse (`Map.CanFit`), and some regions (e.g. **Khaldun**) block resurrection
  outright — "The veil of death in this area is too strong…".

Full death/ghost procedure: [Death & resurrection](/playing/death-and-resurrection/).

## Magery healing spells

If you have [Magery](/skills/magery/) and a spellbook + reagents (see
[Spellcasting](/playing/spellcasting/) and [the magic index](/magic/)):

- **Heal** (1st circle) — restores a modest amount of HP. **Does not work on a poisoned
  target** — you must cure the poison first.
- **Greater Heal** (4th circle) — restores more HP. Likewise the lesser heals are blocked
  by poison; cure first.
- **Cure** (2nd circle) — removes poison; success vs higher poison levels scales with
  Magery (unverified thresholds).
- **Arch Cure** (4th circle) — area cure that clears poison from multiple targets.

Spellcasting is **interruptible**: taking a hit can fizzle the heal (see
[Combat advanced](/playing/combat-advanced/#spell-and-weapon-disruption-fizzle)). Mages
usually create distance, then heal/cure.

## Healing potions

Potions are **instant** (no cast/bandage timer) but heal potions share a **cooldown** —
after drinking one you cannot drink another heal potion until its delay expires ("You must
wait 10 seconds before using another healing potion."). On this AOS shard the delay depends
on the potion (`BaseHealPotion.Delay`):

- **Lesser Heal potion** — small instant HP; **3 s** cooldown.
- **Heal potion** — moderate instant HP; **8 s** cooldown.
- **Greater Heal potion** — larger instant HP; **10 s** cooldown.
- **Cure potion** — removes poison (cure potions are a separate item, not on the heal-potion
  cooldown; stronger potions cure higher levels — effectiveness scaling **unverified**).

**Important:** a heal potion **will not work while you are poisoned or mortally wounded**
("You can not heal yourself in your current state.") — cure the poison first, exactly like
the lesser heal spells. Carry them as an emergency button. See the
[potions catalog](/items/catalog/potions/):

**To use a potion:** double-click it in your pack. Potions are made with
[Alchemy](/skills/alchemy/).

## Healing pets — Veterinary

Healing animals and tamed creatures uses **[Veterinary](/skills/veterinary/)** (with
[Animal Lore](/skills/animal-lore/) as its secondary), not Healing. The bandage procedure
is identical — double-click bandage, target the pet — and a vet bandage on a pet is a
flat **2 s** (`Bandage.cs`). Vet can also resurrect a **dead pet** if your owner/friend is
nearby to sanctify it. See [Taming & pets](/playing/taming-and-pets/).

## When to use which

- **Bandages** — your sustainable, mana-free main heal. Best HP-per-resource; trains a
  skill; but takes seconds and can slip. Use as your default in and out of combat.
- **Heal/Greater Heal spells** — fast burst heals if you have mana, but cost reagents and
  can fizzle when hit; blocked by poison.
- **Cure (spell/potion/bandage) / Arch Cure** — to clear poison before you can use a
  lesser heal effectively.
- **Heal/Greater Heal potions** — instant emergency healing when you can't afford the
  bandage timer or a fizzle, accepting the cooldown.
- **Veterinary bandages** — the way to heal/res pets.

A common survival pattern: **cure poison first** (bandage/Cure), then **bandage or heal
HP**, and keep **heal potions** in reserve for the moment you would otherwise die.

## See also

- [Healing skill](/skills/healing/), [Anatomy](/skills/anatomy/), [Veterinary](/skills/veterinary/)
- [Poison & status](/playing/poison-and-status/)
- [Death & resurrection](/playing/death-and-resurrection/)
- [Spellcasting](/playing/spellcasting/), [Magery](/skills/magery/), [magic index](/magic/)
- [Potions catalog](/items/catalog/potions/), [Alchemy](/skills/alchemy/)
- [Meditation & mana](/playing/meditation-and-mana/) — to fund heal spells
