---
title: Scribe
description: Inscribe magery scrolls, runebooks, and spellbooks. Skills, the build, the scribing loop, what you make, and how it earns.
status: source-verified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Services/Craft/DefInscription.cs (MainSkill=Inscribe; CanCraft requires the SpellScroll's spell in the crafter's own Spellbook via book.HasSpell(id); each scroll AddRes the spell's reagents + a BlankScroll and SetManaReq a mana cost)"
  - "servuo: Scripts/Services/Craft/Core/CraftItem.cs (success chance keyed off CraftSystem.MainSkill = Inscribe and the recipe min/max skill; EvalInt not referenced anywhere in the craft system)"
  - "servuo: Scripts/Spells/Base/Spell.cs (scribeBonus = Inscribe/200, +10% at GM — Inscription's spell-damage bonus, cross-ref /skills/inscription/)"
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000 = 700.0 skill points)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The scribe writes magic onto paper. Using Inscription, you copy spells from your spellbook
onto blank scrolls — the scrolls mages buy to fill their own books or cast from directly —
and bind runebooks and spellbooks. A scribe must actually be a mage: you can only inscribe a
spell that is already in your own spellbook, and each attempt consumes that spell's reagents,
a blank scroll, and a set amount of mana from your pool. That makes scribing the natural money
arm of a mage build.

## Core skills

- [Inscription](/skills/inscription/) — the headline skill: copy spells onto scrolls and craft runebooks and spellbooks.
- [Magery](/skills/magery/) — required to scribe: you can only inscribe a spell that's in your own spellbook (which means a mage who learned it), and each scribe attempt consumes that spell's reagents, a blank scroll, and mana from your pool.
- [Evaluating Intelligence](/skills/evaluating-intelligence/) — does **not** affect scribing success (that's governed by Inscription and the spell's skill range), but it powers the Magery side of a caster build; a common round-out.

## The build

There is no dedicated scribe template yet — Inscription slots directly onto a
[mage](/professions/mage/) build, since it requires Magery anyway. Add Inscription to a
caster's skill spread and see [7x GM Templates](/templates/seven-gm/) for fitting it under
the 700-point cap alongside Magery, Eval Int, Meditation, and Resisting Spells.

## How to craft

Read [Crafting](/playing/crafting/) for the craft menu and exceptional mechanics. The full
list of scrollable spells and material requirements lives on the
[Inscription crafting](/crafting/inscription/) page.

The loop: carry **blank scrolls**, the [reagents](/items/reagents/) for the spell you want to
copy, and enough mana to cast it. Open the inscription menu, pick the spell, and scribe — a
success produces a scroll of that spell; a failure burns the reagents. Higher Inscription and
Magery raise the success rate (and let you scribe higher-circle spells). Recall and Mark are
the bread-and-butter low-circle scrolls; the high circles are where the gold is.

## What you make / tools

- [Reagents](/items/reagents/) and **blank scrolls** — the inputs every scribe attempt consumes (plus mana from your own pool).
- [Scrolls catalog](/items/catalog/scrolls/) — your main output: **spell scrolls** of every circle, from Recall and Gate to the eighth-circle spells.
- **Runebooks and spellbooks** — Inscription also binds these; runebooks hold marked travel runes, spellbooks hold a mage's spells.

## Making a living

Scribes earn by selling **travel and utility scrolls** — Recall, Gate, and Mark move fast
because every traveler needs them — and **high-circle scrolls** (Energy Bolt, Flamestrike,
and up) at a premium to mages stocking their books or casting from scrolls. A scribe directly
supports a [mage](/professions/mage/) economy. Note **vendor rotation**: NPC shops cap how
much they buy and restock slowly, so spread sales across vendors and lean on player vendors
via [Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [7x GM Templates](/templates/seven-gm/) — fitting inscription onto a mage build
- [Mage](/professions/mage/) — the scribe is a mage with Inscription; your main customer base
- [Alchemist](/professions/alchemist/) — the other reagent-consuming profession; common companion
- [Inscription](/skills/inscription/) · [Magery](/skills/magery/) · [Inscription crafting](/crafting/inscription/) · [Scrolls catalog](/items/catalog/scrolls/)
