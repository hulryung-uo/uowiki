---
title: Lumberjacking
description: Chopping logs from trees — wood types, required skill, board-cutting, and the hidden axe damage bonus.
status: source-verified
sources:
  - "servuo: Scripts/Services/Harvest/Lumberjacking.cs"
  - "servuo: Scripts/Items/Resource/Log.cs (TryCreateBoards)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (lumberBonus)"
  - "servuo: Server/Skills.cs (SkillInfo 44)"
last_verified: 2026-06-11
generated: false
---

There is a particular satisfaction in felling a tree with an axe you forged yourself — and a
particular profit, since carpenters and fletchers buy everything you can carry.

**Stats:** Strength (primary), Dexterity (secondary) · **Title:** Lumberjack

## How it works

Use any **axe** on a tree. Per `Scripts/Services/Harvest/Lumberjacking.cs`:

- Trees hold wood in **4×4-tile banks** (`BankWidth = 4`).
- Each successful chop yields **10 logs** (`ConsumedPerHarvest = 10`).
- Cut logs into boards with an axe (boards weigh less and crafting wants them).

## Wood types and required skill

| Log | Required skill (chop) | Vein chance | Board-cutting skill* |
|-----|----------------------|-------------|---------------------|
| Ordinary | 0 | 49% | 0 |
| Oak | 65.0 | 30% | 65 |
| Ash | 80.0 | 10% | 80 |
| Yew | 95.0 | 5% | 95 |
| Heartwood | 100.0 | 3% | 100 |
| Bloodwood | 100.0 | 2% | 100 |
| Frostwood | 100.0 | 1% | 100 |

\* Board-cutting accepts **Carpentry or Lumberjacking** at the listed value
(`Scripts/Items/Resource/Log.cs`, `TryCreateBoards`).

Chopping also turns up ML bonus resources at 100 skill (bark fragments 10%, luminescent fungi
3%, switches 2%, parasitic plants and brilliant amber 1% each).

## The axe damage bonus

Lumberjacking is secretly a combat skill. In `BaseWeapon.cs`, melee damage includes
`lumberBonus = GetBonus(skill, 0.200, 100.0, 10.00)` — **+0.2% damage per skill point, plus
a +10% bonus at 100.0**, applied **only when wielding an axe**. A GM lumberjack swinging an
axe hits roughly 30% harder from this bonus alone. Pairs famously with
[Swordsmanship](/skills/swordsmanship/) (axes use the Swords skill).

## Training

- **0–10:** buy from an NPC or chop — every use gains below 10.0.
- **10–100:** chop trees. Standard [gain rules](/mechanics/skill-gain/) apply; anti-macro is
  off, and GGS guarantees slow-but-steady progress at high skill. Strength trains alongside
  (primary stat), which also raises your carry capacity for hauling logs.

## Where

[Yew](/world/yew/) — the forest is the town. Also: forests north of Britain, east of
Skara Brae, and west of Vesper (per `world_knowledge.yaml`).

## Related skills

- Carpentry and Bowcraft/Fletching — consume your boards
- [Swordsmanship](/skills/swordsmanship/) — the axe-warrior pairing
- [Items: resources](/items/resources/) — full wood tables
