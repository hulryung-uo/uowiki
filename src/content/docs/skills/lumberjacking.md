---
title: Lumberjacking
description: Chopping logs from trees — wood types, required skill, board-cutting, and the hidden axe damage bonus.
status: source-verified
sources:
  - "servuo: Scripts/Services/Harvest/Lumberjacking.cs"
  - "servuo: Scripts/Items/Resource/Log.cs (TryCreateBoards)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (lumberBonus in ScaleDamageAOS, axe-only gate)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseAxe.cs (WeaponType.Axe)"
  - "servuo: Server/Skills.cs (SkillInfo 44)"
last_verified: 2026-06-17
generated: false
---

<img src="/img/skill-flags/44.gif" alt="Lumberjacking skill banner" width="160" />

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

Lumberjacking is secretly a **combat skill** — but only with an axe in hand. When a hit lands,
`ScaleDamageAOS` (the active damage path on this AOS/EJ shard) adds:

```
lumberBonus = Lumberjacking × 0.2%   (+10% extra at exactly 100.0)   → +30% at GM
if (weapon Type != Axe) lumberBonus = 0      // axes only
```

- It scales **linearly: ~+0.2% damage per point**, with a flat **+10% jump at GM**, for
  **+30% at 100 Lumberjacking** (`GetBonus(Lumberjacking, 0.2, 100, 10)`).
- **Axe-only.** The bonus is zeroed unless the weapon's type is **Axe** — i.e. a weapon that
  inherits `BaseAxe` (the whole Axes family: hatchet, war axe, battle axe, double axe,
  large/two-handed axe, executioner's axe, ornate/heavy ornate axe, and the gargish axes).
  Swing a sword, mace, or bow and Lumberjacking adds **nothing**.
- It's **added** to the other melee bonuses, then multiplies base damage:
  `damage = base × (1 + Tactics% + Anatomy% + Str% + Lumber%)`. For an axe warrior at GM
  Tactics + GM Anatomy + GM Lumberjacking + 100 Str that's `1 + 0.6875 + 0.55 + 0.30 + 0.35 =
  **×2.8875**` — the highest pure-skill melee multiplier in the game, which is exactly why the
  **axe-lumberjack** is a classic damage build.
- **Worked example:** a **15**-base-damage battle axe, GM Tactics+Anatomy+Lumber+100 Str →
  ~**43** before item Damage Increase. The same swing with a *non-axe* loses the +30% (×2.5875
  → ~39). Axes use the [Swordsmanship](/skills/swordsmanship/) skill, so this pairs with
  Swords + Tactics + Anatomy.

:::note[Not the old "+20%"]
Pre-AOS rules capped the lumber bonus at **+20%** (`ScaleDamageOld`). That path isn't used
here — this EJ shard runs the **AOS** formula above, where GM Lumberjacking with an axe is
**+30%**.
:::

The full melee damage stack is laid out in
[Advanced combat → Damage components](/playing/combat-advanced/#damage-components).

## Training

- **0–10:** buy from an NPC who knows it (a trainer teaches up to **one-third of its own
  skill, capped at 42.0** — `Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
  `baseToSet = ourSkill.BaseFixedPoint / 3`) or just chop — every use gains below 10.0.
- **10–100:** chop trees in a loop — it's a pure resource grind and GGS carries it. Standard
  [gain rules](/mechanics/skill-gain/) apply; anti-macro is off, and GGS guarantees
  slow-but-steady progress at high skill. Strength trains alongside (primary stat), which also
  raises your carry capacity for hauling logs. See
  [using & training skills](/playing/using-and-training-skills/).

## Where

[Yew](/world/yew/) — the forest is the town. Also: forests north of Britain, east of
Skara Brae, and west of Vesper (per `world_knowledge.yaml`).

## Related skills

- Carpentry and Bowcraft/Fletching — consume your boards
- [Swordsmanship](/skills/swordsmanship/) — the axe-warrior pairing
- [Items: resources](/items/resources/) — full wood tables
