---
title: Magic Schools
description: Overview of the casting schools beyond Magery — Necromancy, Chivalry, Bushido, Ninjitsu, Spellweaving, and Mysticism — and how each is fueled and cast.
status: source-verified
sources:
  - "servuo: Scripts/Spells/Base/MagerySpell.cs (mana table 4/6/9/11/14/20/40/50, ConsumeReagents), Scripts/Spells/Base/Spell.cs (DamageSkill defaults to EvalInt)"
  - "servuo: Scripts/Spells/Necromancy/NecromancerSpell.cs (RequiredMana, ConsumeReagents, DamageSkill = SpiritSpeak)"
  - "servuo: Scripts/Spells/Chivalry/PaladinSpell.cs (RequiredMana + RequiredTithing, no reagents)"
  - "servuo: Scripts/Spells/Bushido/SamuraiSpell.cs + Scripts/Spells/Ninjitsu/NinjaSpell.cs + AnimalForm.cs (mana, no reagents)"
  - "servuo: Scripts/Spells/Spellweaving/ArcanistSpell.cs (RequiredMana; FindArcaneFocus from hand/pack, not consumed), ArcaneCircle.cs (group empowerment)"
  - "servuo: Scripts/Spells/Mysticism/MysticSpell.cs (mana + reagents; DamageSkill = higher of Imbuing or Focus)"
  - "servuo: Scripts/Items/Equipment/Spellbooks/ (per-school book items)"
last_verified: 2026-06-23
generated: false
---

Our shard has several **schools of magic**, each with its own skill, its own "spellbook,"
and its own **fuel**. They all share the basic flow you learn in
[Spellcasting](/playing/spellcasting/) — *invoke the ability, then target* — but they
differ in what they cost. This page is a one-stop overview: what each school does, what it
needs, and how you cast it. Follow the skill links for the full spell lists and details.
The **fuel each school spends** is verified against ServUO below; exact per-spell numbers
live on the linked skill pages.

## Magery — reagents + mana (the core school)

- **What it does:** the broadest school — healing, buffs, offense, fields, travel
  (Recall/Gate), summons. 64 spells across 8 circles.
- **What it needs:** a **[spellbook](/items/catalog/spellbooks-talismans/)** with the spell,
  enough **[Magery](/skills/magery/)** skill for the circle, **mana**, and the spell's
  **[reagents](/items/catalog/reagents/)** in your pack (consumed per cast).
- **How you cast it:** open the spellbook and click the spell (or macro / words of power),
  then target. Offensive damage scales with
  **[Evaluating Intelligence](/skills/evaluating-intelligence/)**.
- **Full reference:** [Spellcasting](/playing/spellcasting/) and the
  [spellbook overview](/magic/).

## Necromancy — reagents + mana

- **What it does:** dark magic — curses, fear, debilitation, corpse and undead effects,
  shapeshifting (e.g. wraith/lich forms), and life-draining attacks.
- **What it needs:** a **necromancer spellbook**, enough
  **[Necromancy](/skills/necromancy/)** skill, **mana**, and Necromancy **reagents**
  (a distinct set from Magery reagents — e.g. bat wings, grave dust, daemon blood, nox
  crystal, pig iron). Reagents are consumed per cast.
- **How you cast it:** like Magery — invoke the spell from the necro book (or a macro),
  then target. **[Spirit Speak](/skills/spirit-speak/)** boosts Necromancy: it strengthens
  several necro effects and powers life-draining, so necromancers commonly train Spirit
  Speak alongside Necromancy.

## Chivalry — tithed gold, no reagents

- **What it does:** holy "paladin" magic — healing, cleansing, smiting the undead, removing
  curses, and self-buffs.
- **What it needs:** the **[Chivalry](/skills/chivalry/)** skill, **mana**, and a reserve of
  **tithed gold** instead of reagents. You **tithe gold at a shrine** to build up a tithing
  pool, and Chivalry abilities spend from that pool. **No reagents** are required.
- **How you cast it:** open the **Book of Chivalry** and invoke the ability (or macro), then
  target. Effectiveness tends to be strongest against undead/evil. Replenish tithing by
  visiting a shrine when the pool runs low.

## Bushido — no reagents, weapon + stance

- **What it does:** the samurai discipline — defensive and offensive combat abilities
  (parry-and-counter, honorable strikes, evasion, momentum/whirlwind effects).
- **What it needs:** the **[Bushido](/skills/bushido/)** skill and usually a **weapon**;
  abilities cost **mana** but use **no reagents**.
- **How you cast it:** invoke the ability from the **Book of Bushido** (or a macro) before
  or during melee; many are stances/buffs that change how your next swings behave rather
  than spells you target. Works hand-in-hand with melee and Parrying.

## Ninjitsu — no reagents, forms + stealth

- **What it does:** the ninja arts — stealth attacks, **animal forms** (transformations),
  mirror-image decoys, smoke-bomb vanishing, and surprise strikes.
- **What it needs:** the **[Ninjitsu](/skills/ninjitsu/)** skill; abilities cost **mana**
  and use **no reagents** — Animal Form is pure-mana too (`AnimalForm.cs` consumes only
  mana, no special item).
- **How you cast it:** invoke the ability from the **Book of Ninjitsu** (or a macro).
  Pairs with Hiding/Stealth for stealth openers.

## Spellweaving — arcane focus

- **What it does:** Arcanist magic — area buffs/heals, summons (arcane creatures), word-of-
  power effects whose strength grows when cast by a group ("Arcane Circle").
- **What it needs:** the **[Spellweaving](/skills/spellweaving/)** skill, **mana**, and an
  **arcane focus** item (charged at an Arcane Circle) that empowers and is required by many
  weaves. **No traditional reagents.**
- **How you cast it:** invoke the weave from the **Spellweaving spellbook** (or a macro),
  then target. Casting within an **Arcane Circle** alongside other weavers strengthens the
  effects.

## Mysticism — reagents + Focus/Imbuing

- **What it does:** elemental and spirit magic — healing, debuffs, summons (e.g. rising
  colossus, elementals), and damage spells.
- **What it needs:** a **mysticism spellbook**, the **[Mysticism](/skills/mysticism/)**
  skill, **mana**, and **reagents** (it uses its own reagent set). Its **secondary skill**
  is **[Focus](/skills/focus/)** (or Imbuing) — that secondary raises spell power, so
  mystics train it alongside Mysticism.
- **How you cast it:** invoke the spell from the mysticism book (or a macro), then target —
  the same invoke-and-target flow as Magery.

## Choosing and mixing schools

You can combine schools within your **700-point skill budget** (see
[Using & training skills](/playing/using-and-training-skills/)). Common pairings: Magery +
Eval Int + Meditation for a pure mage; Necromancy + Spirit Speak for a necro; a melee
template with Chivalry or Bushido for support abilities. Whatever the school, the operating
loop is the same — **carry its fuel, invoke the ability, target** — so once you've learned
[Spellcasting](/playing/spellcasting/) and [Meditation & mana](/playing/meditation-and-mana/),
every school will feel familiar.
