---
title: Spellcasting
description: How to cast spells — the spellbook, skill, mana, and reagents you need; how to target, why spells fizzle or are disrupted, and the utility spells every new caster learns first.
status: source-verified
sources:
  - "servuo: Scripts/Spells/Base/Spell.cs (CheckSequence, ConsumeReagents, Disturb, CheckFizzle)"
  - "servuo: Scripts/Spells/Base/MagerySpell.cs (GetCastSkills, mana table, scroll circle offset)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-23
generated: false
---

This page is the practical reference for **casting a spell** on our shard. It covers what
you must carry, how to invoke and target a spell, why casts fail, and the handful of
utility spells most new players learn first. It focuses on **Magery**, the core arcane
school; the other schools cast in a very similar way and are summarized under
[Magic schools](/playing/magic-schools/). For the full per-spell tables (mana, skill,
reagents, words of power) see the [Magery spellbook overview](/magic/).

## What you need to cast a spell

To cast any Magery spell you need **four** things at once:

1. A **[spellbook](/items/catalog/spellbooks-talismans/)** in your pack (or equipped) that
   contains the spell. A spellbook holds the spells you have scribed into it from
   [spell scrolls](/items/catalog/scrolls/); an empty book casts nothing.
2. Enough **[Magery](/skills/magery/) skill** for that spell's circle. Each of the 8
   circles has a minimum skill below which the cast **always fails**, and a higher value
   at which it **never fizzles**. The exact per-circle table is on the
   [spellbook overview](/magic/#circles) — link there rather than memorizing it.
3. Enough **mana**. Each circle costs a fixed amount of mana, rising from the 1st circle
   to the 8th. If you lack the mana the cast aborts with "Insufficient mana for this
   spell." See [Meditation & mana](/playing/meditation-and-mana/) for how mana works.
4. The spell's **[reagents](/items/catalog/reagents/)** in your backpack. Reagents are
   **consumed on every successful cast**, so you must keep a stock. The reagent recipe is
   listed per spell on the [spellbook overview](/magic/) and on each spell page.

If any one of these is missing the spell will not go off — you will be told which (for
example "More reagents are needed for this spell").

## How to cast: step by step

To cast a Magery spell:

1. Make sure your **hands are free** of weapons (a spellbook or runebook is fine to hold).
   Holding a non-channeling weapon blocks casting.
2. **Open your spellbook** (double-click it) and **click the spell's icon**, *or* use a
   bound macro / hotkey for that spell, *or* speak its **words of power**.
3. Your character begins casting: the **words of power** are spoken aloud and a brief
   **casting animation/sound** plays. Higher circles take longer to cast.
4. When the cast completes you are prompted to **target**. Click the recipient:
   - **Self or an ally/pet** for beneficial spells (Heal, Cure, Bless, Magic Reflection).
   - **An enemy** for offensive spells (Magic Arrow, Fireball, Energy Bolt).
   - **The ground / a tile** for area or field spells (Fire Field, Wall of Stone).
   - A spell that affects only you (Night Sight, Reactive Armor) may take effect without a
     target prompt.
5. On success the effect fires, **mana and reagents are deducted**, and a short recovery
   delay passes before you can cast again.

## Fizzling and disruption

A cast can be **wasted** in two main ways:

- **Fizzle (skill failure):** if your Magery is below the circle's "never-fizzle" value
  there is a random chance the spell **fizzles** ("The spell fizzles."). The lower your
  skill relative to the circle, the higher the fizzle chance; below the circle's minimum it
  fails every time. The cast sequence checks mana and consumes reagents *before* rolling
  the skill check, so a fizzle still **consumes your reagents** even though the spell does
  not go off — repeatedly fizzling high-circle spells wastes reagents. Your **mana is only
  deducted on a successful (non-fizzled) cast**, not on a fizzle.
  *(Source: `Spell.cs` CheckSequence — `ConsumeReagents()` runs before `CheckFizzle()`, and
  `m_Caster.Mana -= mana` runs only after `CheckFizzle()` succeeds; `MagerySpell.cs`
  GetCastSkills sets the per-circle skill window.)*
- **Disruption (taking damage):** being **hit while casting** can interrupt the spell
  ("Your concentration is disturbed, thus ruining thy spell."). This is the **disrupt /
  hurt fizzle** mechanic — a melee or ranged hit during your cast bar can ruin the spell.
  Being **frozen, paralyzed, or peacemade (calmed)** also prevents the cast from
  completing. *(Source: `Spell.cs` Disturb / DisturbType.)*

To reduce disruption: cast from out of an enemy's reach, use the **Protection** spell
(reduces interruption at a cost), or finish casts before the enemy closes in.

## Line of sight and range

Most targeted spells require **line of sight** to the target — you cannot cast through a
solid wall — and the target must be within **casting range**. Step around corners or
obstacles to regain line of sight. Field and area spells are placed on a visible tile.
(Exact ranges are spell-specific and **unverified** here; treat "must be able to see and
be reasonably near the target" as the rule.)

## Casting from scrolls

A **[spell scroll](/items/catalog/scrolls/)** lets you cast a spell **with less skill than
casting it from your book**. On our shard, casting from a scroll counts the spell as
**two circles lower** for the skill check, so a scroll is easier to cast successfully than
the same spell from a book (`MagerySpell.cs`: `circle -= 2` when a scroll is used). The
scroll is **consumed** on a successful cast. Scrolls are handy for spells whose circle is
above your current Magery, and for emergency casts when you are low on skill. You still
need the **mana** (reagents are *not* required when casting from a scroll, since the scroll
itself supplies the magic).

## Casting in war mode

You can cast while in **war mode** (the combat stance). Switching to war mode does not by
itself block spellcasting; you still need free hands. Many caster builds alternate between
swinging and casting. Note that being **attacked while casting still risks disruption**
(see above), and your own offensive spells will engage you with the target.

## Utility spells every caster learns early

These are the low-cost, high-value spells new mages train and keep ready:

- **[Heal](/magic/circle-1/heal/)** (1st circle) — restore a target's health. The bread-and-
  butter heal; cheap and castable at very low skill.
- **[Cure](/magic/circle-2/cure/)** (2nd) — remove poison from yourself or an ally.
- **[Reactive Armor](/magic/circle-1/reactive-armor/)** (1st) — reflect part of melee
  damage back at attackers; a cheap self-buff.
- **[Magic Reflection](/magic/circle-5/magic-reflection/)** (5th) — reflect or reduce
  incoming spell damage.
- **[Recall](/magic/circle-4/recall/)** (4th) — teleport yourself to a location stored on a
  **rune**. The standard fast-travel spell.
- **[Mark](/magic/circle-6/mark/)** (6th) — record your current location onto a rune so you
  can Recall or Gate back to it later.
- **[Gate Travel](/magic/circle-7/gate-travel/)** (7th) — open a two-way moongate to a
  marked rune, letting your whole party step through.

For how Recall, Mark, and Gate fit into getting around the map, see
[Movement & travel](/playing/movement-and-travel/).

## Raising your spell damage

Offensive spell damage scales with the **[Evaluating Intelligence](/skills/evaluating-intelligence/)**
skill — a mage typically trains Eval Int alongside Magery so spells like
[Energy Bolt](/magic/circle-6/energy-bolt/) and Flame Strike hit harder. Higher
**Intelligence** also raises your maximum mana, letting you cast more before resting.

## Other schools cast similarly

Necromancy, Mysticism, Chivalry, Spellweaving, and the warrior arts (Bushido, Ninjitsu)
each have their own "spellbook" or invocation and their own fuel (reagents, tithed gold,
arcane focus, forms). The **invoke-then-target** flow is the same. See
[Magic schools](/playing/magic-schools/) for what each one needs and how it is cast.
