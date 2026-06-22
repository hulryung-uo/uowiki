---
title: Mage
description: The eight circles — burst damage, summons, and Recall mobility. Skills, the build, how to cast, and how a mage earns gold.
status: source-verified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Base/Spell.cs (CastSkill=Magery, DamageSkill=EvalInt; evalScale=30+(9*evalSkill)/100; scribeBonus=skill/200, capped +10 at GM; Caster.Int/10 damage bonus)"
  - "servuo: Scripts/Spells/Base/SpellHelper.cs (GetSpellDamageBonus: SDI cap 15% in PvP, 30% if school-focused; uncapped in PvM)"
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000 = 700.0 skill points; TotalStatCap=225)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The mage wields the eight circles of [Magery](/magic/): burst damage from a distance, escape
and travel with Recall and Gate, and an army of summoned creatures and field spells to fight
for them. A mage is fragile up close but controls the battlefield from range, and the same
spellbook that farms dungeons also unlocks the most convenient travel in the game.

## Core skills

- [Magery](/skills/magery/) — the engine: success chance and access to all eight [spell circles](/magic/).
- [Evaluating Intelligence](/skills/evaluating-intelligence/) — the **damage multiplier** for offensive spells (the mage's Tactics-and-Anatomy in one skill).
- [Meditation](/skills/meditation/) — regenerates mana so you can keep casting; the skill that decides how long your gas tank lasts.
- [Wrestling](/skills/wrestling/) — your "weapon" skill when unarmed; it lets you defend in melee and avoid being disrupted as easily.
- [Resisting Spells](/skills/resisting-spells/) — crucial in PvP and against caster monsters, reducing hostile spell effects.
- [Inscription](/skills/inscription/) — optional, but it boosts your spell damage on this shard and lets you scribe scrolls (see below).

## The build

Follow the [Mage Template](/templates/mage/) for stats, skill order, and a leveling route.
The classic loadout is Magery + Eval Int + Meditation + Wrestling + Resisting Spells + two
more (often Inscription and Healing or a crafting skill). For fitting all seven grandmaster
skills under the 700-point cap, see [7x GM Templates](/templates/seven-gm/).

## How to play it

Read [Spellcasting](/playing/spellcasting/) — choosing spells, targeting, reagents, and the
casting interruption rules — and [Meditation & Mana](/playing/meditation-and-mana/) for
keeping mana topped up between fights. The [Magic](/magic/) section is your spell reference,
circle by circle.

The core loop: open from range with damage spells (or drop an Energy Vortex / summon to tank
for you), kite while it works, and **meditate back to full mana** between pulls. Keep Recall
runes ready for instant escape. Mana management is everything — a mage who runs dry is just a
robe with no defense.

## Gear & tools

- A **spellbook** with the spells you've scribed — see [spellbooks & talismans](/items/catalog/spellbooks-talismans/).
- **Reagents** for every cast — carry deep stacks; details in [Reagents](/items/reagents/) and [magic reagents](/magic/reagents/).
- Light [armor](/items/armor/) or robes — Magery and Meditation work best with low armor penalty, so mages favor cloth and light pieces.
- [Jewelry](/items/catalog/jewelry/) for stat and resist bonuses.

## Making a living

Mages farm efficiently by letting **summons and field spells** (Energy Vortex, Blade
Spirits, Fire Field) do the dying while they loot — strong gold-per-hour against tough
[bestiary](/bestiary/) targets. A second income is **scribing**: a mage with
[Inscription](/skills/inscription/) writes spell scrolls and runebooks to sell — see the
[Scribe](/professions/scribe/) profession. Sell loot and scrolls via
[Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Mage Template](/templates/mage/) — the full build and progression
- [Scribe](/professions/scribe/) — turn Magery + Inscription into a scroll business
- [Tamer](/professions/tamer/) — pairs Magery with pets for a powerful hybrid
- [Magic](/magic/) · [Spellcasting](/playing/spellcasting/) · [Meditation & Mana](/playing/meditation-and-mana/)
