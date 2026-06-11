---
title: Swordsmanship
description: The art of blades and axes — the AOS hit chance formula, weapon coverage, and training.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (CheckHit)"
  - "servuo: Server/Skills.cs (SkillInfo 40)"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/40.gif" alt="Swordsmanship skill banner" width="160" />

From the duelling katana to the woodsman's double axe, Swordsmanship covers every edged weapon
in Britannia — the most popular weapon skill for good reason.

**Stats:** Strength (primary), Dexterity (secondary) · **Title:** Swordsman

## What it does

Swordsmanship is your **to-hit skill** when wielding swords and axes. This shard uses the AOS
hit formula (`BaseWeapon.cs`, `CheckHit`):

```
attacker = (attackSkill + 20) × (100 + HitChanceIncrease)    // HCI capped at 45
defender = (defendSkill + 20) × (100 + DefenseChanceIncrease) // DCI capped at 45
hit chance = attacker / (defender × 2), minimum 2%
```

Against an equal-skill opponent with no item bonuses, that is a 50% hit rate; skill gaps and
HCI/DCI gear move it from there. The damage you do on a hit is scaled by
[Tactics](/skills/tactics/), Anatomy, Strength — and, for axes,
[Lumberjacking](/skills/lumberjacking/).

Swordsmanship weapons also carry **special moves** (AOS weapon abilities) that unlock with
skill; per-weapon move lists are out of scope here (see the weapons reference when available).

## Training

The skill gains when you swing at something your level — the standard
[gain rules](/mechanics/skill-gain/) apply to combat checks:

- **0–30:** buy from an NPC weaponsmith/warrior trainer; then bash training dummies (low cap)
  and harmless wildlife.
- **30–70:** escalate through the bestiary — the [Britain](/world/britain/) graveyard, Orc
  Cave, and Despise are the classic ladder.
- **70–100+:** tougher dungeon spawn keeps checks challenging; GGS covers the dry spells.
  Fighting alongside [Healing](/skills/healing/) and bandages keeps sessions long.

A practical note: the *gain* comes from the swing's difficulty check, not from killing —
durable, low-damage opponents are training partners, not loot.

## Equipment

Iron is fine to start; colored-metal and crafted exceptional weapons (see
[Blacksmithy](/skills/blacksmithy/)) add damage and durability. Axe users: Lumberjacking's
damage bonus makes the axe line the hardest-hitting choice at GM.

## Related skills

- [Tactics](/skills/tactics/) — mandatory damage companion
- **Anatomy**, **Parrying**, [Healing](/skills/healing/) — the classic warrior kit
- [Jhelom](/world/jhelom/) — the warrior city, fighting pits included
