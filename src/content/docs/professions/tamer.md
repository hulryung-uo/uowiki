---
title: Tamer
description: Command legendary beasts to fight for you — taming, lore, vet, and the magery that backs them. Skills, the build, the loop, and how tamers earn.
status: source-verified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Skills/AnimalTaming.cs (tame gate by CurrentTameSkill; control-slot check vs FollowersMax; passive AnimalLore check)"
  - "servuo: Scripts/Skills/AnimalLore.cs (lore inspection / pet stats)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (GetControlChance from Taming+Lore+loyalty; ControlSlots; MaxLoyalty=100; loyalty loss on failed command)"
  - "servuo: Scripts/Items/Resource/Bandage.cs (Veterinary+AnimalLore heal pets; ResurrectPet)"
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The tamer charms wild creatures into loyal pets and sends them into battle. At the top end a
tamer commands dragons, nightmares, and worse — pets that out-fight almost any solo build —
while standing back to heal them and cast support. It's a slow, expensive profession to
train but one of the most powerful and self-sufficient once mature.

## Core skills

- [Animal Taming](/skills/animal-taming/) — the gate skill: determines what you can tame and how hard.
- [Animal Lore](/skills/animal-lore/) — required to tame and to inspect a creature's stats; tells you whether a beast is worth taming.
- [Veterinary](/skills/veterinary/) — heals, cures, and resurrects your pets with bandages; your pet's lifeline mid-fight.
- [Magery](/skills/magery/) — Recall to drag pets around the map, plus offensive and support casting alongside them.
- [Meditation](/skills/meditation/) — regenerates the mana that Magery burns.
- [Evaluating Intelligence](/skills/evaluating-intelligence/) and [Resisting Spells](/skills/resisting-spells/) — optional rounding-out for damage and survivability.

## The build

Follow the [Animal Tamer Template](/templates/animal-tamer/) for stats, the taming skill
order, and where to tame at each stage. The mature loadout is Taming + Lore + Vet + Magery +
Meditation + two more (commonly Eval Int and Resisting Spells). For fitting seven grandmaster
skills under the 700-point cap, see [7x GM Templates](/templates/seven-gm/).

## How to play it

Read [Taming & Pets](/playing/taming-and-pets/) for the tame attempt, control slots,
loyalty, and stabling, and [Verbal Commands](/playing/verbal-commands/) for the pet command
keywords ("all kill", "all follow me", "all stay", "all guard me") that drive them in combat.
Browse the [bestiary](/bestiary/) to find tamable targets — the index lists the
**notable tamables** like dragons and the Dread Warhorse.

The core loop: bring your pet to a target, command "all kill", and **keep it alive with Vet
bandages** while it does the killing; resurrect and re-heal as needed. Loyalty drops if you
let a pet starve or take it somewhere it dies — feed it and don't overreach.

## Gear & tools

- **Bandages** for [Veterinary](/skills/veterinary/) — carry a deep stack; they are your pet's health bar. See [Tools](/items/tools/).
- A **spellbook** and [reagents](/items/reagents/) for the Magery side — see [spellbooks & talismans](/items/catalog/spellbooks-talismans/).
- Light [armor](/items/armor/) — you stand back, so survivability comes from the pet, not your plate.

## Making a living

Tamers earn two ways. First, **breeding and selling pets**: a freshly tamed nightmare,
dragon, or other [notable tamable](/bestiary/) sells well to other players. Second,
**dungeon farming** — your pet tanks and kills tough monsters while you loot gold, gems, and
gear, often clearing content no solo build could. Sell pets and loot via
[Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Animal Tamer Template](/templates/animal-tamer/) — the full build and progression
- [Mage](/professions/mage/) — the casting half of a tamer is a mage in miniature
- [Bestiary](/bestiary/) — find tamable creatures and their stats
- [Taming & Pets](/playing/taming-and-pets/) · [Verbal Commands](/playing/verbal-commands/)
