---
title: Skill Masteries
description: The deepest layer of skill progression — per-skill mastery abilities learned from primers in three volumes, with one mastery active at a time. Bardic, caster, warrior, and even taming masteries.
status: source-verified
sources:
  - "servuo: Scripts/Spells/Skill Masteries/Core/MasteryInfo.cs (skill→mastery map, Volume None/One/Two/Three, GetMasteryLevel)"
  - "servuo: Scripts/Spells/Skill Masteries/Core/SkillMasteryPrimer.cs (learning volumes)"
  - "servuo: Scripts/Spells/Skill Masteries/Core/SelectMasteryGump.cs (one CurrentMastery at a time)"
  - "servuo: Scripts/Mobiles/Bosses/BaseChampion.cs + Services/Peerless/BasePeerless.cs (primer drops)"
last_verified: 2026-06-17
generated: false
---

**Skill masteries** are the top tier of skill progression — a set of powerful **per-skill
abilities** unlocked once your skill is high. Almost every combat, magic, and bardic skill has
its own mastery, and a few support skills (even [Animal Taming](/skills/animal-taming/)) do
too. This is a *Time of Legends* feature, and our shard runs **EJ**, so masteries are live.

## Learning a mastery: primers and volumes

Each skill's mastery comes in **three volumes** (`Volume` = One / Two / Three). You learn them
from **Mastery Primers** — books that each teach **one volume** of one skill
(`SkillMasteryPrimer`): double-click a primer to learn that volume. Learning higher volumes
raises your **mastery level** in that skill, unlocking and strengthening its abilities.

Where primers come from:

- **[Champion spawns](/playing/champion-spawns/)** and **[peerless bosses](/playing/peerless-bosses/)**
  drop them as rewards (alongside power scrolls).
- A few high-end encounters (certain High Seas bosses, the Time of Legends quest line) award
  them too.
- **Bard masteries** are earned through the dedicated **Bard Mastery quest line** (the knights
  Berran, Felean, and Hareus).

## Using a mastery: one at a time

You can have **only one mastery active at a time**. Pick your **current mastery** from the
mastery menu (`SelectMasteryGump` sets `CurrentMastery`) — choosing one of the skills you've
learned volumes in. Only *that* skill's mastery abilities are then available to you; switch
masteries to change your active toolkit. Mastery strength scales with the **volumes learned**
and your skill level.

## What each skill gets

A sampling of the signature mastery abilities by role (`MasteryInfo`):

| Role | Skill | Mastery abilities |
|---|---|---|
| **Bard** | Provocation | **Inspire**, **Invigorate** (party damage/heal buffs) |
| | Peacemaking | **Resilience**, **Perseverance** |
| | Discordance | **Tribulation**, **Despair** |
| **Caster** | Magery | **Death Ray**, **Ethereal Burst** |
| | Mysticism | **Nether Blast**, **Mystic Weapon** |
| | Necromancy | **Command Undead**, **Conduit** |
| | Spellweaving | **Mana Shield**, **Summon Reaper** |
| | Chivalry | **Rejuvenate**, **Holy Fist** |
| **Warrior** | Swordsmanship | **Onslaught** |
| | Fencing | **Thrust**, **Pierce** |
| | Mace Fighting | **Stagger**, **Toughness** |
| | Archery | **Flaming Shot**, **Playing the Odds** |
| | Parrying | **Shield Bash** |
| | Bushido / Ninjitsu | **Warcry** / **Shadow**, **White Tiger Form** |
| **Tamer** | Animal Taming | **Combat Training** (buffs your pet) |

Bardic masteries (Inspire/Invigorate especially) are the classic group-PvM force-multiplier —
which is why a mastery bard is prized at champion spawns and peerless fights. Caster and warrior
masteries add burst abilities and survivability tools that a non-mastery character simply can't
match.

## See also

- [Champion Spawns](/playing/champion-spawns/) — the main source of mastery primers (and power scrolls)
- [Peerless Bosses](/playing/peerless-bosses/) — also drop primers
- [Skills index](/skills/) — the underlying skills you're mastering
- [Provocation](/skills/provocation/) · [Magery](/skills/magery/) — two of the strongest mastery skills
