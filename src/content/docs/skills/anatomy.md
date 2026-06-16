---
title: Anatomy
description: Knowledge of bodies that boosts melee damage and bandage healing.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (anatomyBonus GetBonus(Anatomy,0.5,100,5) = +55% at GM)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-15
generated: false
---

<img src="/img/skill-flags/1.gif" alt="Anatomy skill banner" width="160" />

Anatomy is a passive support skill that raises melee damage and improves bandage
[healing](/skills/healing/). The prose is community-derived (paraphrased from the
uorenaissance.com skill list plus ServUO behavior) pending field verification; the stats
table and the damage-bonus note are source-verified against ServUO.

## What it does

Studying a creature's physiology lets you strike its weak points harder and tend wounds more
effectively. Anatomy adds a percentage bonus to melee damage and increases how much a
bandage restores, so it sits on nearly every warrior and bandage-medic build. It is purely
support: it has no attack or cast of its own.

## How Anatomy boosts damage

Anatomy is the **second-largest melee damage bonus** after [Tactics](/skills/tactics/). When a
hit lands, `ScaleDamageAOS` (the active damage path on this AOS/EJ shard) computes:

```
anatomyBonus = Anatomy × 0.5%   (+5% extra at exactly 100.0)
```

- It scales **linearly: about +0.5% damage per point**, with a flat **+5% jump at GM**, for
  **+55% at 100 Anatomy** (`GetBonus(Anatomy, 0.5, 100, 5) = (100 × 0.5 + 5) ÷ 100 = 0.55`).
- This is **added** to the other melee bonuses, then the total multiplies base damage:
  `damage = base × (1 + Tactics% + Anatomy% + Str% + …)`. Anatomy and
  [Tactics](/skills/tactics/) together are **+123.75%** at grandmaster — more than doubling a
  weapon's printed damage before Strength, Lumberjacking, and item Damage Increase.
- **Worked example:** a **15**-base-damage weapon at GM Tactics + GM Anatomy + 100 Str scales
  by `1 + 0.6875 + 0.55 + 0.35 = 2.5875` → ~**39**. Drop Anatomy alone and the multiplier
  falls to `2.0375` → ~**31**, a ~21% damage loss — which is why no serious melee build skips
  it.

:::note[Not the old "+30%"]
Community guides written for **pre-AOS** rules quote Anatomy as *1% per 5 points, +10% at GM*
(= +30%). That formula (`ScaleDamageOld`) is **not** used here — this EJ shard runs the **AOS**
path above, where GM Anatomy is **+55%**.
:::

The full melee damage stack is laid out in
[Advanced combat → Damage components](/playing/combat-advanced/#damage-components).

## How to use it

Anatomy works two ways:

- **Passive** — once trained, the bonus applies automatically whenever you swing a melee
  weapon (see [combat basics](/playing/combat-basics/)) or apply a bandage with
  [Healing](/skills/healing/).
- **Active (training)** — use the skill and target a living creature to read its physical
  condition. This is mainly a way to grind the skill.

## How to train it

**Quick start:** buy up from an NPC Healer/Warrior trainer — a trainer teaches up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`), so pay one to ~30–42 first.

Anatomy is an active **"read"** skill — each Use targets a creature and rolls a gain check
whether you learn anything new or not:

- **Low/mid skill** — target yourself or any nearby creature and Use repeatedly; the read
  trains it cheaply without combat. Just keep clicking fresh targets.
- **Alternative / high skill** — let it climb passively while you fight with a melee weapon
  and heal between fights; it gains alongside [Tactics](/skills/tactics/) and
  [Healing](/skills/healing/). GGS guarantees the slow high-end points if you keep using it.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Strength |
| Title | Biologist |
| Mastery skill | No |
| Gain notes | training Anatomy raises **Int** (primary), or **Str** (secondary) — see [Stat gain](/mechanics/stat-gain/) |

The melee damage bonus is `GetBonus(Anatomy, 0.500, 100.0, 5.00)` =
`(Anatomy × 0.5 + 5) ÷ 100` → **+55% at GM** (detailed in
[How Anatomy boosts damage](#how-anatomy-boosts-damage) above). Anatomy's other half is
**healing**: it raises how much a bandage restores and, at **80+**, helps gate the strongest
bandage cures/resurrection — see [Healing](/skills/healing/).

## Related skills & synergies

- **[Tactics](/skills/tactics/) + Anatomy** — the two damage multipliers every melee build
  pairs with a weapon skill.
- **[Healing](/skills/healing/) + Anatomy** — high in both enables faster cures and
  self-resurrection with bandages.
- Featured in the Sword Dexxer and Tank Mage builds on [seven-GM templates](/templates/seven-gm/).

## See also

- [Combat basics](/playing/combat-basics/)
- [Healing](/skills/healing/) · [Tactics](/skills/tactics/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
