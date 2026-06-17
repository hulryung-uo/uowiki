---
title: Pet Training
description: How to train and grow a tamed pet on this shard — the training profile, filling the progress bar in combat, Power Hour, spending training points on stats/skills/resists/abilities, and how control slots grow.
status: source-verified
sources:
  - "servuo: Scripts/Services/Pet Training/PetTrainingHelper.cs (Enabled=Core.TOL, training points, per-creature definitions, caps)"
  - "servuo: Scripts/Services/Pet Training/TrainingProfile.cs (progress, Power Hour 1h/24h, control-slot growth)"
  - "servuo: Scripts/Services/Pet Training/TrainingDefinition.cs + AbilityProfile.cs (class, abilities, slot range)"
last_verified: 2026-06-17
generated: false
---

Taming a creature is only the start. This shard runs the modern **Pet Training** system
(`PetTrainingHelper.Enabled = Core.TOL`, and our expansion is **EJ**), which lets you **grow a
pet** — raising its stats, skills, and resistances and unlocking new abilities — turning a
plain tame into a customized battle companion. If you've only [tamed](/skills/animal-taming/) a
pet, this is the half of the system that makes it strong.

## 1. Begin training

Open the pet's **context menu** and choose **Begin Training**. The pet receives a pool of
**training points** sized to how strong it already is (`AssignStartingTrainingPoints`), and a
**training progress bar** appears. You spend points on upgrades — but only **after** you've
filled that bar.

## 2. Fill the progress bar (fight things)

Training progress comes from **fighting with the pet** (`TrainingProfile.CheckProgress`):

- Your pet earns progress by **killing creatures** — tougher targets relative to the pet feed
  the bar faster. Park a weak pet on weak mobs and it barely moves; push it against real
  threats and it climbs.
- **Power Hour** is the accelerator: once a day you can trigger a **1-hour** window
  (`PowerHourDuration`) where progress gains are **multiplied**, on a **24-hour cooldown**
  (`PowerHourDelay`). Line up a strong hunting spot before you pop it.
- When the bar hits **100%**, the pet is ready to **apply upgrades** (`CanApplyOptions`).

## 3. Spend training points

With the bar full, open the training gump and spend points to improve the pet:

- **Stats** — raise **Strength, Dexterity, Intelligence** (and the Hits/Stamina/Mana that
  follow) toward the pet's stat cap.
- **Resistances** — add to the five resists.
- **Skill caps** — raise combat and magic skill caps (Wrestling, Tactics, Magery, Resisting
  Spells, etc.); the cap scales with points invested (`cap = 100 + value/10`).
- **Abilities** — unlock **special abilities, weapon abilities, area effects, and magical
  abilities** (including spellcasting schools) — *limited to what the pet's class allows*
  (next section).

Each upgrade costs points; bigger upgrades cost more, so you're budgeting a finite pool into
the build you want (tank, nuker, caster, all-rounder).

## 4. Control slots: stronger pets cost more

The catch: as you train a pet up, its **control-slot footprint grows**. Every pet has a
**minimum and maximum control slot** range in its training definition
(`TrainingDefinition`) — e.g. a **Cu Sidhe** or **Bane Dragon** starts around **3 slots and can
be trained up to 5**. A fully-trained 5-slot pet fills your **entire follower budget** (you can
control up to 5 slots of followers), so a maxed pet means *no* second pet. Train toward the
slot cost you can afford.

Use the **planning** mode ("Add to Plan") to map out a full build before committing points, so
you don't waste your pool.

## What a given pet can become

Not every creature can learn everything — each has a **class** and a fixed menu of abilities in
its definition. Magical classes can be taught spellcasting; clawed/tailed classes get melee
special moves; some get **area effects** (auras, explosive goo, etc.). Top-tier trainable pets
(Cu Sidhe, Bane Dragon, dragons, and other 5-slot creatures) can reach the highest stats,
multiple resist 70s, GM-capped skills, magery, and an area effect — which is why a
well-trained one rivals a champion-spawn party member by itself.

Don't forget **bonding**: a bonded pet can be resurrected and won't wander off — see
[Taming & pets](/playing/taming-and-pets/).

## See also

- [Animal Taming](/skills/animal-taming/) — taming the creature in the first place (and the first-tame skill penalty)
- [Taming & pets](/playing/taming-and-pets/) — commands, bonding, stabling, feeding
- [Animal Lore](/skills/animal-lore/) — read a pet's stats and training options
- [Champion Spawns](/playing/champion-spawns/) / [Peerless](/playing/peerless-bosses/) — where a strong pet earns its keep
