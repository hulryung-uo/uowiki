---
title: How to Play — Taming and Pets
description: Step-by-step pet workflow — finding tamable creatures, taming, controlling with Lore, the full command list, bonding, stabling, control slots, feeding, healing, death, transfer and combat with pets.
status: unverified
sources:
  - "servuo: Scripts/Mobiles/AI/BaseAI.cs (pet speech command keywords, OrderType handling)"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (BondingDelay 7 days, BondingAbandonDelay 1 day, MaxLoyalty 100, default ControlSlots 1, loyalty feed/decay)"
  - "servuo: Scripts/Mobiles/NPCs/AnimalTrainer.cs (stable: 30 gold/week, GetMaxStabled skill scaling)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This guide walks a new player or AI agent through the full life cycle of a tamed pet:
finding a creature you can tame, taming it, taking control of it, commanding it in and
out of combat, keeping it loyal and alive, and handling its death or transfer. The three
skills that make a tamer are [Animal Taming](/skills/animal-taming/) (acquiring pets),
[Animal Lore](/skills/animal-lore/) (controlling and inspecting them), and
[Veterinary](/skills/veterinary/) (healing them). For a complete starting build see the
[Animal Tamer template](/templates/animal-tamer/).

**Definitions used on this page:**
- **Tamable** — a creature the game allows you to attempt to tame. Most wild animals are
  tamable; most undead, humanoids and elementals are not.
- **MinTameSkill** — the minimum [Animal Taming](/skills/animal-taming/) value that gives
  any chance to tame a given creature. Every creature's value is listed on its
  [bestiary](/bestiary/) page.
- **Control slot** — a unit of "follower capacity." Each pet costs one or more slots; you
  can only control as many slots' worth of pets as your follower cap allows.
- **Loyalty** — a hidden 0–100 happiness value (`MaxLoyalty = 100`, per `BaseCreature.cs`)
  that drops over time and rises when you feed the pet. Low loyalty makes a pet disobey
  and eventually go wild.

## Step 1 — Find a tamable creature

Not every creature can be tamed. Tamable beasts are mostly the **animals** in the
[bestiary](/bestiary/animals/) — horses, llamas, bulls, big cats, bears, dragons, and so
on — plus some reptiles and birds.

To find a target you can actually handle:

1. Open the creature's [bestiary](/bestiary/) page and read its **MinTameSkill**.
2. Compare it to your current [Animal Taming](/skills/animal-taming/) skill. You need at
   least that much skill for any chance, and a comfortable margin above it for a reliable
   chance.
3. Check its **control-slot cost** (see [Control slots](#control-slots-and-follower-cap)
   below). A creature that costs more slots than you have free cannot be controlled even
   if you tame it.

New tamers start on low-MinTameSkill animals (the common farm and forest animals) and work
upward as their skill climbs. See [Skill gain](/mechanics/skill-gain/) for how training
works in general.

## Step 2 — Tame the creature

To tame a wild creature:

1. Make sure the creature is **not already someone's pet** and is **not in combat with
   you** if you want it peaceful (some tamers tame mid-fight, but it is harder).
2. Double-click your [Animal Taming](/skills/animal-taming/) skill in the skill list (or
   use a skill macro) to get a **target cursor**.
3. **Target the creature.** Your character begins a taming attempt and may say a calming
   line. The attempt takes a few seconds.
4. Watch the result message. Success tames the creature and it becomes **yours** (its name
   bar turns to your control). Failure simply means *try again* — re-target and repeat.

**Repeated attempts are normal.** A single tame on a tougher creature often takes many
tries. Higher [Animal Taming](/skills/animal-taming/) and [Animal Lore](/skills/animal-lore/)
relative to the creature's MinTameSkill raise your per-attempt chance (the chance formula in
`BaseCreature.cs` rewards skill above the creature's difficulty). Some powerful creatures
can become **temporarily enraged** while you tame and attack you — be ready to back off or
have a way to survive.

**Warning:** once you start taming a difficult creature, other players can sometimes tame
it out from under you. Tame in a safe spot when possible.

## Step 3 — Take control with Animal Lore

[Animal Lore](/skills/animal-lore/) does two jobs:

- **It reveals the creature's stats** — hit points, resistances, str/dex/int, damage,
  and (for tamers shopping for pets) its taming difficulty. To inspect: double-click the
  Animal Lore skill and target the creature.
- **It improves control.** Your effective control over a pet — the chance each command
  actually obeys — scales with your **Animal Taming + Animal Lore**. A tamer with high
  Taming but no Lore will be **disobeyed frequently**.

Every command you issue runs a **control check** (`CheckControlChance` in `BaseAI.cs`). If
the check fails the pet ignores that order — you simply repeat the command. Low
[loyalty](#feeding-and-loyalty) further lowers the control chance, so keep your pet fed.

## Pet commands (verified keyword set)

Pets obey **typed speech commands**. You say the command out loud (type it in the chat
bar) and the pet parses it. There are two forms:

- **"all &lt;command&gt;"** — every pet you control that hears you obeys.
- **"&lt;pet name&gt; &lt;command&gt;"** — only the named pet obeys (you must include the
  pet's exact name).

The following command set is confirmed from `Scripts/Mobiles/AI/BaseAI.cs`:

| Command | What it does |
| --- | --- |
| `all follow me` / `<name> follow me` | The pet follows **you**, staying at your side as you move. |
| `all follow` / `<name> follow` | Prompts a **target**; the pet follows whatever (or whoever) you target. |
| `all come` / `<name> come` | The pet moves to your current location once. |
| `all stay` / `<name> stay` | The pet **holds position** and stops following until ordered otherwise. |
| `all stop` / `<name> stop` | The pet cancels its current order and stands down. |
| `all kill` / `all attack` / `<name> kill` / `<name> attack` | Prompts a **target**; the pet attacks it (see [Combat with pets](#combat-with-pets)). |
| `all guard` / `all guard me` / `<name> guard` | The pet **guards** you, attacking things that attack you. |
| `<name> patrol` | The pet patrols between marked points (advanced; single-pet only). |
| `<name> friend` | Prompts a target; grants another player limited control of this pet (cannot friend a summoned pet or during a pending trade). |
| `<name> drop` | The pet drops what it is carrying (pack animals; not for dead or summoned pets). |
| `<name> release` | **Releases** the pet — it becomes wild again and is no longer yours. Opens a confirmation for non-summoned pets. |
| `<name> transfer` | Prompts a target player to **transfer ownership** of the pet to them (not for summoned pets or during a pending trade). |

Notes confirmed from source:
- `kill`/`attack`, `follow`, `friend` and `transfer` first ask you to **pick a target**
  (`BeginPickTarget`), so after the command you get a target cursor.
- Most owner-only orders (`guard`, `release`, `transfer`, `drop`, `patrol`, `come`) work
  only for the owner; a "friended" player gets a reduced set.
- Every order is gated by the **control check**, so a low-skill or unhappy pet may not
  comply on the first try — just repeat the command.

## Bonding

**Bonding** ties a pet permanently to you so it is not lost on death and can be
**resurrected**. A bonded pet that dies leaves a corpse and a ghost you can revive rather
than vanishing forever.

- A newly tamed pet is **not** bonded. It becomes eligible after a bonding period spent in
  your care: `BondingDelay = 7 days` (`BaseCreature.cs`). Keep the pet with you, fed and
  loyal during that window.
- A bonded pet that dies and is **left abandoned** can still be lost: `BondingAbandonDelay
  = 1 day` (`BaseCreature.cs`) — resurrect it before that window expires.

Always bond pets you intend to keep. The difference between a bonded and unbonded pet at
the moment of death is the difference between a quick resurrection and a total loss.

## Control slots and follower cap

Each pet costs a number of **control slots** (the default is `ControlSlots = 1` in
`BaseCreature.cs`; stronger creatures cost more — check the [bestiary](/bestiary/) page).
You can only control pets whose slot costs sum to your **follower cap**. The control check
in `PlayerMobile.cs` confirms a pet is only accepted when
`Followers + pet.ControlSlots <= FollowersMax`.

To stay under your cap:
- Add up the slot cost of every pet currently following or guarding you.
- If a new pet would push you over, **stable** an existing pet first
  (see [Stabling](#stabling-and-claiming-pets)).
- Pets you `stay` somewhere still count against your cap until stabled or released.

## Feeding and loyalty

A pet's **loyalty** is its happiness (0–100). It **decays over time** and falls when the
pet is hurt or neglected; it **rises when you feed it**. An unfed pet grows disloyal,
disobeys commands more often, and if loyalty bottoms out it **goes wild** and is lost.

To feed a pet:
1. Carry the right **food** for its diet (carnivores eat meat/fish; herbivores eat
   grains, fruit and vegetables; see the [bestiary](/bestiary/) page for diet).
2. **Drag the food onto the pet**, or in some clients target the pet with the food.
3. A successful feed raises loyalty (per `BaseCreature.cs`, a feed nudges loyalty up; a
   newly tamed/claimed pet starts at the top, "Wonderfully Happy").

Feed pets regularly — especially before long trips or when you notice commands being
ignored.

## Stabling and claiming pets

An **Animal Trainer** NPC (found in most towns) stores pets safely so they do not count
against your follower cap and cannot wander, starve, or be killed.

To stable a pet:
1. Bring the pet to an [Animal Trainer](/bestiary/) NPC.
2. Say **"stable"** (or use the NPC's context menu).
3. Target the pet. It is stored. Per `AnimalTrainer.cs`, the trainer charges **30 gold per
   pet per real week** of stable time.

To get a pet back:
1. Say **"claim"** to the trainer (or use the context menu).
2. The pet is returned to your control — but only if you have **enough free control
   slots**; a pet that would exceed your cap stays in the stable (the trainer warns
   *"…remained in the stables because you have too many followers."*).

**Stable capacity is limited and scales with your animal skills.** Per
`AnimalTrainer.GetMaxStabled`, your maximum stabled pets grows with your combined
**Animal Taming + Animal Lore + Veterinary** (and certain reward bonuses): base capacity
of about 2 slots rises to 3, 4, then 5 as that skill sum passes the 160 / 200 / 240
thresholds, with extra slots at very high Taming. (Exact totals depend on shard
expansion/reward settings — pending in-game verification.)

## Healing pets (Veterinary)

[Veterinary](/skills/veterinary/) is the pet-healing skill — it is to pets what Healing is
to players. You heal pets with **bandages**:

1. Have **bandages** in your pack.
2. Double-click a bandage to get a target cursor.
3. **Target your pet.** After a short delay your Veterinary skill applies, restoring hit
   points and curing poison/raising the dead pet depending on skill.

A bandage on a pet completes in roughly **2 seconds** (per our [Veterinary](/skills/veterinary/)
and [Combat Basics](/playing/combat-basics/) pages; the exact delay scales with skill and
dexterity). [Animal Lore](/skills/animal-lore/) boosts your healing the way Anatomy boosts
player healing. Keep bandages stocked before any fight where your pet tanks.

## Pet death and resurrection

When a pet's hit points hit zero it **dies**:

- A **bonded** pet leaves a corpse and a ghost. **Resurrect** it with high
  [Veterinary](/skills/veterinary/) (bandage the dead pet) or have a healer/NPC resurrect
  it, then bandage it back to health. Do this before the `BondingAbandonDelay` (1 day)
  abandons it.
- An **unbonded** pet that dies is **gone** — another reason to bond every keeper.

After resurrection the pet returns with low health; bandage it back up and **feed it** to
restore loyalty before fighting again.

## Releasing and transferring

- **Release** (`<name> release`) makes the pet **wild again** and removes it from your
  control — used to free a pet you no longer want or to clear a control slot. Non-summoned
  pets prompt a confirmation gump.
- **Transfer** (`<name> transfer`) hands ownership to **another player** you target. You
  cannot transfer a summoned creature or a pet with a pending trade. Use this to sell or
  gift tamed pets.

## Riding mounts

Many tamed creatures — horses, llamas, ostards, beetles, and others — can be **ridden**.
Once tamed and controlled, **double-click the mount** to ride it; double-click again to
dismount. Riding lets you move at mount speed and the creature still obeys commands. Full
mount and travel mechanics (mount speed, dismounting in combat, sailing, recall) are
covered in [Movement & travel](/playing/movement-and-travel/).

## Combat with pets

Pets are a tamer's main weapon. To fight with a pet:

1. Make sure the pet is following or guarding you and is **fed/loyal** (low loyalty = it
   may refuse the order).
2. Say **`all kill`** (or `<name> kill`) and **target the enemy**. The pet engages.
3. Use **`all guard me`** to make pets defend you automatically, or **`all stop`** /
   **`all stay`** to pull them off a fight.
4. **Heal the pet** with [Veterinary](/skills/veterinary/) bandages while it tanks, and
   re-issue `all kill` if it loses its target.

You do not have to fight alongside the pet, but doing so (with your own weapon — see
[Combat Basics](/playing/combat-basics/)) kills faster. Re-target with `all kill` whenever
you want the pet to switch enemies. Pull pets back with `all stop` before they chase into
danger or aggro extra monsters.

## See also

- [Pet Training](/playing/pet-training/) — grow a tamed pet's stats, skills, and abilities
- [Animal Taming](/skills/animal-taming/) · [Animal Lore](/skills/animal-lore/) ·
  [Veterinary](/skills/veterinary/) · [Herding](/skills/herding/)
- [Animal Tamer template](/templates/animal-tamer/) — a full starting build
- [Bestiary](/bestiary/) and [animals](/bestiary/animals/) — MinTameSkill and slot costs
- [Movement & travel](/playing/movement-and-travel/) — riding mounts
- [Combat Basics](/playing/combat-basics/) · [Healing](/playing/healing/) ·
  [Targeting](/playing/targeting/)
- [Skill gain](/mechanics/skill-gain/)
