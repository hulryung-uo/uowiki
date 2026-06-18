---
title: Mysticism
description: The Stygian Abyss spell school — eight circles spanning damage, healing stones, summons, and debuffs. Mana + reagents, governed by Mysticism with Focus (or Imbuing) as the secondary.
status: source-verified
sources:
  - "servuo: Scripts/Spells/Mysticism/MysticSpell.cs (8 circles, mana table {4,6,9,11,14,20,40,50})"
  - "servuo: Scripts/Spells/Mysticism/SpellDefinitions/*.cs (the 16 spells and their circles)"
last_verified: 2026-06-18
generated: false
---

**Mysticism** is the *Stygian Abyss* spell school — a versatile mix of elemental damage,
healing, summons, and debuffs across **eight circles**. Spells cost **mana** and **reagents**,
and their power is set by your **[Mysticism](/skills/mysticism/)** skill paired with a
**secondary** (your highest of **[Focus](/skills/focus/)** or **[Imbuing](/skills/imbuing/)**).

Mana scales by circle (`MysticSpell` table): **4 / 6 / 9 / 11 / 14 / 20 / 40 / 50** for circles
1–8 — the same ladder as [Magery](/magic/), so higher-circle spells cost much more.

## Spells by circle

| Circle | Mana | Spells |
|---|---|---|
| **1** | 4 | **Nether Bolt** (single-target damage) · **Healing Stone** (drop a stone that heals on use) |
| **2** | 6 | **Enchant** (imbue your weapon with an element/effect) · **Purge** (cleanse harmful effects) |
| **3** | 9 | **Eagle Strike** (summoned eagle hits a foe) · **Sleep** (put a target to sleep) |
| **4** | 11 | **Stone Form** (turn to stone — defensive buff) · **Animated Weapon** (a floating weapon fights for you) |
| **5** | 14 | **Spell Trigger** (store a stoneform/heal to trigger later) · **Mass Sleep** (area sleep) |
| **6** | 20 | **Bombard** (heavy single-target hit + knockdown) · **Cleansing Winds** (area heal + cure) |
| **7** | 40 | **Spell Plague** (escalating damage debuff) · **Hail Storm** (cold area burst) |
| **8** | 50 | **Rising Colossus** (summon a powerful colossus) · **Nether Cyclone** (mana/stam-draining area storm) |

Mystics pair well with **[Spellweaving](/magic/spellweaving/)** or melee, and **Stone Form** +
**Healing Stone** make even a low-skill mystic surprisingly tanky.

## See also

- [Mysticism skill](/skills/mysticism/) · [Focus](/skills/focus/) · [Imbuing](/skills/imbuing/) — what governs the spells
- [Magery](/magic/) — the parallel circle-based school
- [Magic overview](/magic/) · [Reagents](/magic/reagents/)
