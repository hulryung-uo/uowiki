---
title: Mining
description: Digging ore and stone from mountains and caves — ore types, required skill, vein chances, and training route.
status: source-verified
sources:
  - "servuo: Scripts/Services/Harvest/Mining.cs"
  - "servuo: Scripts/Misc/ResourceInfo.cs"
  - "servuo: Server/Skills.cs (SkillInfo 45)"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/45.gif" alt="Mining skill banner" width="160" />

Swing a pickaxe at a mountainside and Britannia pays you in metal. Mining is the realm's
foundational gathering skill — every smith's career starts in a tunnel.

**Stats:** Strength (primary), Dexterity (secondary) · **Title:** Miner

## How it works

Use a **pickaxe or shovel** on mountainside or cave floor tiles. Per
`Scripts/Services/Harvest/Mining.cs`:

- Resources come in **8×8-tile banks** (`BankWidth = 8`), each rolled to a vein type.
- You can dig tiles up to **2 tiles away** (`MaxRange = 2`); each success yields ore
  (1 unit consumed from the bank per dig).
- Smelt ore at a forge into ingots — see [resources](/items/resources/) for the full
  ore→ingot table.

## Ore types and required skill

From the `HarvestResource` table (required skill to dig / gain range):

| Ore | Required skill | Vein chance |
|-----|---------------|-------------|
| Iron | 0 | 49.6% |
| Dull Copper | 65.0 | 11.2% |
| Shadow Iron | 70.0 | 9.8% |
| Copper | 75.0 | 8.4% |
| Bronze | 80.0 | 7.0% |
| Gold | 85.0 | 5.6% |
| Agapite | 90.0 | 4.2% |
| Verite | 95.0 | 2.8% |
| Valorite | 99.0 | 1.4% |

Digging a colored vein below its required skill yields the fallback (iron). At **100.0 skill**
you can also turn up ML bonus gems (blue diamond, fire ruby, etc., 0.1% each) per the
`BonusResources` table, and dig **sand** (requires 70–100 skill, separate `Sand` definition).

## Training

- **0–10:** buy skill from an NPC miner or just dig — below 10.0 every use gains
  ([skill gain rules](/mechanics/skill-gain/)).
- **10–99+:** dig, endlessly. Gains follow the standard formula; anti-macro is
  **off** on this shard, so one good mountainside works. The GGS timer guarantees progress
  even through dry streaks.
- Carry weight is the real constraint — Strength (this skill's primary stat) conveniently
  trains alongside. Smelt at a forge to convert 2-stone ore into 0.1-stone ingots'
  worth of value.

## Where

[Minoc](/world/minoc/) is the miner's town: mountains, forge, and bank in a tight loop.
Other known areas (per `world_knowledge.yaml`): mountains north-east of Britain, north of
Vesper, and the Lost Lands around Delucia. Vendor and terrain locations on the
[map](https://uomap.vercel.app).

## Related skills

- [Blacksmithy](/skills/blacksmithy/) — the main consumer of your ingots
- Tinkering — makes your shovels
- [Items: resources](/items/resources/) — full resource tables
