---
title: Parrying
description: Block incoming blows with a shield or weapon.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 5)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (CheckParry — shield (Parry-Bushido)/400, weapon (Parry*Bushido)/48000|41140, AOS Parry/800)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-15
generated: false
---

<img src="/img/skill-flags/5.gif" alt="Parrying skill banner" width="160" />

Parrying is the active-block defensive skill. The prose is community-derived (paraphrased
from the uorenaissance.com skill list plus ServUO behavior) pending field verification; the
stats table is source-verified against ServUO.

## What it does

Parrying gives a chance to block incoming melee and ranged hits outright. The block chance
scales with your Parrying skill and the **shield** equipped (or, for weapon-parry builds, the
weapon). It is a core survivability skill for sword-and-board warriors and a Mastery skill on
this shard.

## How to use it

Equip a shield (or a parrying weapon) and fight normally — blocks happen automatically when
you take hits, no activation needed. Higher skill and a better shield raise the block rate.
See [combat basics](/playing/combat-basics/) and [advanced combat](/playing/combat-advanced/).

## How to train it

**Quick start:** an NPC trainer who knows Parry (a Ninja or Samurai) teaches up to
**one-third of its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`,
CheckTeach: `baseToSet = ourSkill.BaseFixedPoint / 3`) — buy to ~30–42 first.

Parrying is passive: it rolls on **each incoming blow you successfully block**, so the method
is to **stand and tank**.

- **Low/high skill** — equip a shield (or, with Bushido/Ninjitsu, a weapon) and let a
  creature that hits you steadily swing away. The harder it hits, the more block-checks you
  bank. Pair with [Healing](/skills/healing/) and bandages to outlast the punishment, and pin
  a low-damage durable monster so you tank without dying. GGS covers the slow late points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Strength |
| Title | Duelist |
| Mastery skill | Yes |
| Gain notes | skill-ups can raise Str +0.75, Dex +0.25 (per-use stat gain weights) |

Block chance is computed in `BaseWeapon.CheckParry`. **With a shield equipped:**

```
blockChance = (Parrying − Bushido) ÷ 400      (+5% if Parrying or Bushido ≥ 100)
```

- At **GM Parrying (100) with no [Bushido](/skills/bushido/)**, that is `100 ÷ 400 + 5% = 30%`
  — the practical ceiling for a pure shield tank.
- **Low Dexterity penalty:** if Dex < 80, the chance is scaled by `(20 + Dex) ÷ 100`, so keep
  Dex at 80+ to parry at full rate.

**Weapon-parry without a shield** (requires Bushido) is `(Parry × Bushido) ÷ 48000`
(one-handed) or `÷ 41140` (two-handed), falling back to `Parry ÷ 800` if higher — so weapon
parry is weak until you invest in Bushido, while a shield reliably reaches 30% on Parrying
alone. As a Mastery skill, high Parrying also enables related mastery effects. Full context in
[Advanced combat → Parrying](/playing/combat-advanced/#parrying).

## Related skills & synergies

- **A weapon skill + [Tactics](/skills/tactics/) + [Anatomy](/skills/anatomy/) +
  [Healing](/skills/healing/)** — the parry-dexxer drops a caster skill for Parrying on the
  Sword-Dexxer skeleton; see [seven-GM templates](/templates/seven-gm/).
- **[Bushido](/skills/bushido/)** — pairs with Parrying for the defensive samurai.

## See also

- [Combat basics](/playing/combat-basics/) · [Advanced combat](/playing/combat-advanced/)
- [Shields catalog](/items/catalog/shields/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
