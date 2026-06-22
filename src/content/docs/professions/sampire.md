---
title: Sampire
description: The legendary hybrid — a melee character that leeches life on every hit (Vampiric Embrace) and uses Bushido to whirlwind packs. The famous solo PvM monster-slayer.
status: source-verified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Necromancy/VampiricEmbrace.cs (RequiredSkill 99.0 Necromancy, 23 mana, FireResistOffset -25)"
  - "servuo: Scripts/Spells/Necromancy/NecromancerSpell.cs (CastSkill=Necromancy, DamageSkill=SpiritSpeak)"
  - "servuo: Scripts/Spells/Bushido/ (HonorableExecution.cs, LightningStrike.cs, MomentumStrike.cs, Confidence.cs, Evasion.cs)"
  - "servuo: Scripts/Services/Virtues/Honor.cs (Honor virtue + Perfection, damage scales with Bushido)"
  - "servuo: Scripts/Spells/Chivalry/ (ConsecrateWeapon.cs, EnemyOfOne.cs); PaladinSpell.cs (mana + tithing cost)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (Bushido parry, Anatomy/Tactics damage)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The sampire ("samurai + vampire") is the most famous PvM template in Ultima Online: a melee
character that **leeches life on every hit** and shrugs off packs of monsters that would
flatten a normal dexxer. On this shard all the pieces are real (the EJ expansion stack includes
AOS, SE, and ML skills). It's a fusion build — not its own skill — combining three schools:

- [Necromancy](/professions/necromancer/) + Spirit Speak → **Vampiric Embrace** (life-leech form)
- [Bushido](/professions/samurai/) → Lightning Strike, Evasion, two-handed parrying, plus the Honor-virtue Perfection bonus
- a little [Chivalry](/professions/paladin/) → Consecrate Weapon and Enemy of One

## Core skills

- [Necromancy](/skills/necromancy/) — needed to cast **Vampiric Embrace**, the leech form that defines the build. This is **not** a token investment: Vampiric Embrace requires **99.0 Necromancy** (`VampiricEmbrace.cs`), so you carry near-GM Necromancy.
- [Spirit Speak](/skills/spirit-speak/) — Necromancy's casting/damage skill (`DamageSkill = SpiritSpeak`). With Necromancy ≥ 99 the form casts off Spirit Speak (80–120 range), so you want real Spirit Speak too — it is a genuine slot, not free.
- [Bushido](/skills/bushido/) — for **Lightning Strike**, **Confidence**, **Evasion**, and improved parrying with two-handers (`BaseWeapon.cs` CheckParry uses Bushido). It also powers the **Honor virtue**'s Perfection damage bonus (see below).
- [Chivalry](/skills/chivalry/) — a small investment for **Consecrate Weapon** (hit the target's weakest resist) and **Enemy of One** (big single-type damage). Each cast costs **mana plus tithing points**, not tithing alone (see [paladin](/professions/paladin/)).
- A weapon skill — usually [Swordsmanship](/skills/swordsmanship/) (a two-handed weapon with a **Whirlwind** special and built-in leech).
- [Tactics](/skills/tactics/) and [Anatomy](/skills/anatomy/) — the damage multipliers, mandatory.
- [Parrying](/skills/parrying/) is common; [Healing](/skills/healing/) is optional because the leech replaces bandages.

## The build

There is **no dedicated sampire template page** yet. Build it as a dexxer that borrows from
three schools: start from the [Warrior Template](/templates/warrior/) for the weapon + Tactics +
Anatomy core, then fit Necromancy, Bushido, and a little Chivalry around it. This is a tight
fit — see [7x GM Templates](/templates/seven-gm/) for the 700-point budgeting; sampires often
run Necromancy and Chivalry below GM (only as high as their key spells need) to free points for
the combat core.

## How to play it — the loop

Read [Combat Advanced](/playing/combat-advanced/) for special moves and weapon speed; this build
lives and dies on them. The signature loop:

1. **Vampiric Embrace** active (cast it and stay in form) — every blow now heals you.
2. **Honor** a tough target — this is the **Honor *virtue*** (`Scripts/Services/Virtues/Honor.cs`), invoked on the creature, not the Bushido move "Honorable Execution". Honoring builds *Perfection*, a damage bonus that scales with your Bushido. Then **Consecrate Weapon** + **Enemy of One** (Chivalry) before engaging.
3. **Whirlwind** into a pack — hitting many enemies at once means many simultaneous life-leeches, so a crowd actually *heals* you faster than it hurts.
4. Sprinkle **Lightning Strike** for accuracy on key swings; lean on **Confidence**/**Evasion** and Parrying when focused.

Because the leech scales with how many things you're hitting, the sampire is near-unkillable
solo against monster packs — the reason it's the legendary go-to PvM farmer. (Mechanics
confirmed: `servuo: Scripts/Spells/Necromancy/VampiricEmbrace.cs`, the Bushido files,
`Scripts/Services/Virtues/Honor.cs`, and `Scripts/Spells/Chivalry/ConsecrateWeapon.cs` /
`EnemyOfOne.cs`.)

## Gear

- [Weapons](/items/weapons/) and the [weapon catalog](/items/catalog/weapons/) — a two-handed weapon with a **Whirlwind** special and **Hit Life Leech**; many players favor a no-dachi or double axe.
- [Magic item properties](/magic/) — stack **Hit Life Leech**, **Hit Lower Defense**, **Swing Speed Increase**, **Stamina/Mana** sustain, and the resist cap. Faster Casting helps only the few buff casts.
- [Armor](/items/armor/) — Vampiric Embrace carries a concrete elemental weakness: it applies a **−25 fire resist** offset while in form (`VampiricEmbrace.cs` `FireResistOffset`). Over-cap your fire resist on gear so you stay protected once the form drops it. (At Necromancy > 99 the form also grants poison immunity.)

## Making a living

The sampire is the premier **solo PvM farmer**: it clears high-tier dungeon packs and bosses
that other solo templates can't survive, looting everything. Tithe gold for Chivalry, keep
Necromancy reagents for re-casting the form, and sell the haul via [Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Necromancer](/professions/necromancer/) · [Samurai](/professions/samurai/) · [Paladin](/professions/paladin/) — the three schools it fuses
- [Warrior](/professions/warrior/) — the dexxer base
- [Combat Advanced](/playing/combat-advanced/) · [7x GM Templates](/templates/seven-gm/)
