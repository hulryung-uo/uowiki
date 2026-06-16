---
title: Arms Lore
description: Inspect weapon and armor quality — and how a crafter's Arms Lore adds bonus properties to exceptional weapons and armor on this shard.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 4 — primary Int, secondary Str)"
  - "servuo: Scripts/Skills/ArmsLore.cs (identify weapon/armor on use)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs OnCraft (exceptional: WeaponDamage += ArmsLore/20, ML)"
  - "servuo: Scripts/Items/Equipment/Armor/BaseArmor.cs DistributeExceptionalBonuses (exceptional: +ArmsLore/20 random resists, ML)"
  - "servuo: Scripts/Services/Craft/ (Arms Lore is NOT referenced — no success/exceptional-chance bonus)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-17
generated: false
---

<img src="/img/skill-flags/4.gif" alt="Arms Lore skill banner" width="160" />

Arms Lore is the appraisal skill for arms and armor: it reads a weapon or armor piece's
condition and quality. On this shard it also gives a **crafter** a small bonus to the
**exceptional** weapons and armor they make. The behaviour below is verified against ServUO
source.

## What it does

Two distinct things:

1. **Inspect gear** — `Use` the skill and target a weapon or armor piece to learn its
   **durability** (how worn it is) and a description of its **damage** (weapons) or **armor
   rating** (armor). A failed check just says you're *"not certain"* — higher skill reads more
   reliably. This is its active function (`Scripts/Skills/ArmsLore.cs`).
2. **Improve your exceptional crafts** — see the next section.

## How to use it

Activate the skill and target a weapon or armor piece — in your pack, equipped, or on a
vendor — to read its details. The crafting bonus is **automatic**: it applies when you craft,
and crafting also trains Arms Lore passively (each exceptional craft rolls a gain check).

## Does Arms Lore affect weapon-making?

**Yes — but not the way it's often assumed.** Reading the source settles a common
misconception:

- **It does *not* raise your success or exceptional chance.** Arms Lore is **not referenced
  anywhere in the crafting engine** (`Scripts/Services/Craft/`). Your chance to succeed and to
  produce an *exceptional* item comes from your **crafting skill, Strength/Dex**, and tools —
  Arms Lore plays no part in *whether* a craft turns out exceptional.
- **It *does* sweeten an item that's already exceptional** (on this ML/EJ shard). When you
  craft an **exceptional** piece, your Arms Lore adds bonus properties on top, scaled by
  `ArmsLore / 20`:
  - **Weapons** (`BaseWeapon.OnCraft`): `Damage Increase += ArmsLore / 20`. At **GM (100)
    Arms Lore that's +5% DI** baked in — *on top of* the +35% DI an exceptional weapon already
    grants.
  - **Armor** (`BaseArmor.DistributeExceptionalBonuses`): `ArmsLore / 20` extra **resist
    points**, each randomly assigned to Physical/Fire/Cold/Poison/Energy. At GM that's **+5
    total resist** spread across the five types, on top of the normal exceptional bonus.
  - **Clothing** gets a similar bonus (capped at +4).
  - *(On a Siege-ruleset shard the divisor is 12.5 instead of 20, i.e. +8 at GM; this shard
    uses the standard 20.)*

So a smith or tailor who maxes Arms Lore turns out **better exceptional gear** — more damage
on weapons, more resist on armor — even though Arms Lore never changes how *often* they hit
exceptional. For a crafter, GM Arms Lore is a genuine (if modest) upgrade to every exceptional
weapon and suit they make. See [Crafting](/playing/crafting/) and
[Blacksmithy](/skills/blacksmithy/) / [Tailoring](/skills/tailoring/).

## How to train it

**Quick start:** an NPC trainer (a Samurai or weapon/armor vendor with the skill) teaches up
to **one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

Arms Lore is an active **"read"** skill — Use it on a weapon or armor piece and it rolls a
gain check each time:

- **Low/mid skill** — keep a stack of crafted daggers or looted armor and examine them over
  and over; it is one of the faster read-skills to raise.
- **High skill** — keep examining gear, or let it ride along while you craft. GGS guarantees
  the slow late points if you keep reading.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Weapon Master |
| Mastery skill | No |
| Gain notes | training Arms Lore raises **Int** (primary), or **Str** (secondary) — see [Stat gain](/mechanics/stat-gain/) |

Arms Lore's primary stat is Intelligence — it is an appraisal/knowledge skill, not a combat
one.

## Related skills & synergies

- **[Blacksmithy](/skills/blacksmithy/) / [Tailoring](/skills/tailoring/)** — supports the
  quality of crafted gear.
- **[Item Identification](/skills/item-identification/)** — the broader appraisal skill for
  non-weapon items.
- **Weapon skills** ([Swordsmanship](/skills/swordsmanship/) and the rest) — fighters who
  want to read their gear at a glance.

## See also

- [Crafting (how to play)](/playing/crafting/)
- [Weapons](/items/catalog/weapons/) · [Armor](/items/catalog/armor/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
