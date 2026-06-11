---
title: Meditation & Mana
description: What mana is, how it regenerates passively over time, and how to use the Meditation skill (and Focus) to recover it faster — plus why armor and weapons block meditation.
status: unverified
sources:
  - "servuo: Scripts/Skills/Meditation.cs (OnUse, CheckOkayHolding, armor offset check)"
  - "servuo: Scripts/Misc/RegenRates.cs (GetArmorOffset, regen)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page explains **mana** — the resource that powers spells — and how to recover it,
both passively and with the **[Meditation](/skills/meditation/)** skill. It is written for
casters who want to spend less time standing around and more time casting.

## What mana is

**Mana** is the energy spent to cast spells. Every Magery spell has a fixed mana cost that
rises by circle (see the [spellbook overview](/magic/#circles)); other schools spend mana
too. When you cast, mana is deducted; if you do not have enough, the cast fails with
"Insufficient mana for this spell."

Your **maximum mana scales with Intelligence** — the higher your Int, the larger your mana
pool and the more spells you can cast before resting. See
[Character & stats](/playing/character-and-stats/) for how Intelligence and the other stats
work, and the stat cap (225 total across Str/Dex/Int — see [shard caps](/shard/)).

## How mana regenerates

Mana comes back on its own over time — **passive regeneration**. The base rate is slow.
Three things speed it up:

- **Meditation skill** — even when you are *not* actively meditating, having Meditation
  skill increases your passive mana regeneration (the "passive meditation" benefit).
- **Active Meditation** — invoking the skill to enter a trance regenerates mana much faster
  (see below).
- **The [Focus](/skills/focus/) skill** — Focus adds passive **stamina and mana**
  regeneration, and unlike Meditation it works regardless of what you are wearing or
  holding. It stacks usefully with Meditation for hybrid builds.

Armor matters: heavy/metal armor **reduces or blocks** mana regeneration (the
"medable armor" rule, below).

## Active meditation: step by step

**Active meditation** puts your character into a trance that recovers mana quickly until it
is interrupted. To meditate:

1. **Stand still** and stop any other action.
2. Make sure your **hands are free** — a weapon in hand blocks meditation. (A spellbook or
   runebook is allowed.) On our shard, if you are holding a non-channeling weapon you are
   told "Your hands must be free to cast spells or meditate."
   *(Source: `Meditation.cs` CheckOkayHolding — Spellbook, Runebook, and SpellChanneling
   items are permitted.)*
3. Make sure you are **not wearing meditation-blocking armor** (see below). If your armor
   blocks it you get "Regenative forces cannot penetrate your armor!" and the trance fails.
   *(Source: `Meditation.cs` checks `RegenRates.GetArmorOffset(m) > 0`.)*
4. **Invoke the Meditation skill** — open your skill list and **use** Meditation, or trigger
   a bound macro/hotkey.
5. On success you see "You enter a meditative trance." and your mana climbs rapidly. The
   chance to enter the trance improves with higher Meditation skill (and is harder when you
   are nearly full on mana). If it fails you see "You cannot focus your concentration." —
   simply try again. *(Source: `Meditation.cs` OnUse: trance chance derived from skill vs.
   missing mana.)*

If you try to meditate while already at full mana you are told "You are at peace."

### What stops a meditation trance

The trance ends when you:

- **Move** (take a step), or
- **Take damage**, or
- **Take another action** (cast, attack, pick something up) — meditating requires you to be
  busy with nothing else; the skill refuses if you currently have a target cursor up ("You
  are busy doing something else and cannot focus.").

Because of this, meditate in a **safe spot** away from enemies.

## The medable-armor rule

Meditation (active and passive) is **reduced or blocked by armor that is too heavy or
metal**. On our shard the active trance checks an **armor offset** and refuses entirely if
that offset is above zero — heavy/metal armor stops it cold
(`Meditation.cs` -> `RegenRates.GetArmorOffset`). Lighter, "medable" materials (such as
leather and cloth) let meditation work. The exact per-piece thresholds and which materials
count as fully medable are **unverified** here; the practical rule is:

> Wear **light, non-metal armor** (leather/cloth, or other "medable" pieces) if you want to
> meditate. Plate, chain, and other metal armor will choke your mana regen.

The **[Focus](/skills/focus/)** skill is the workaround for warriors who must wear heavy
armor: it regenerates mana passively without the armor restriction.

## Managing mana cost

Even with good regen, mana is finite in a fight. Practical habits:

- **Match the spell to the job** — don't open with an 8th-circle spell when a 1st-circle
  one will do. Lower circles cost far less mana.
- **Carry [reagents](/items/catalog/reagents/)** generously; running out mid-fight is as
  bad as running out of mana.
- **Raise Intelligence** to enlarge your mana pool (see
  [Character & stats](/playing/character-and-stats/)).
- **Rest between fights** — step somewhere safe, free your hands, and meditate back to full
  before re-engaging.

## Tips for mage builds

- **Wear light armor** (leather/cloth) so you can meditate, and keep **Wrestling** as your
  defensive melee skill — it lets you defend yourself with empty hands, which also keeps
  hands free for casting and meditating.
- **Train [Meditation](/skills/meditation/) high** for both the passive regen and a reliable
  active trance.
- **Add [Focus](/skills/focus/)** if your build sometimes wears heavier gear or you want
  extra stamina regen.
- Use the gaps between fights to meditate; treat mana like ammunition you reload while safe.

For how casting itself works — invoking, targeting, fizzles — see
[Spellcasting](/playing/spellcasting/). For training the skill, see
[Meditation](/skills/meditation/) and [skill gain](/mechanics/skill-gain/).
