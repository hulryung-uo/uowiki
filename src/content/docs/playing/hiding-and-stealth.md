---
title: Hiding & Stealth
description: How to hide, move while hidden with Stealth, detect and track others, what reveals you, and how to use stealth to escape, scout, or play thief/assassin.
status: source-verified
sources:
  - "servuo: Scripts/Skills/Hiding.cs (combat-range block, skill check, messages)"
  - "servuo: Scripts/Skills/Stealth.cs (must-be-hidden, steps = skill/5, armor penalty)"
  - "servuo: Scripts/Skills/DetectHidden.cs (targeted search, range, skill contest)"
  - "servuo: Scripts/Skills/Tracking.cs (category menu, range, locate-not-reveal)"
  - "servuo: Scripts/Spells/Base/Spell.cs & Scripts/Items/Resource/Bandage.cs (RevealingAction callers)"
last_verified: 2026-06-23
generated: false
---

This page covers staying unseen: [Hiding](/skills/hiding/) to vanish,
[Stealth](/skills/stealth/) to move while hidden, [Detecting Hidden](/skills/detecting-hidden/)
and [Tracking](/skills/tracking/) to find others, and what gives you away. Combat use of
escaping is in [Combat basics → Fleeing](/playing/combat-basics/#fleeing).

## Hiding — vanishing on the spot

**To hide:**

1. Activate the **[Hiding](/skills/hiding/)** skill (open your skill list and use Hiding,
   or use a hide hotkey/macro). Plain Hiding does not let you move while hidden — that
   needs Stealth — but the server has **no "must stand still" check** on the hide attempt
   itself.
2. On success you become **invisible** to other players and most creatures: *"You have
   hidden yourself well."*; if the skill check fails: *"You can't seem to hide here."*

Your **success chance scales with your Hiding skill** — the attempt is a skill check on a
0.0–100.0 difficulty band (`Hiding.cs` `CheckSkill(Hiding, 0.0 - bonus, 100.0 - bonus)`).
Being **inside a house you own or are friended to** lowers the difficulty (a large bonus),
making hiding far more reliable indoors.

You **cannot hide while a nearby enemy is actively in combat with you**: if any combatant
who can see you is within range (roughly `(100 - skill) / 2 + 8`, capped at 18 tiles), the
attempt is refused with *"You can't seem to hide right now."* and the act of trying
**reveals you**. (`Hiding.cs` combat-range check.)

On a successful hide your character also **drops out of war mode** (`Hiding.cs` sets
`Warmode = false`). While hidden you do not appear on screen to others and are skipped by
many auto-targeting attacks — until something reveals you (see below).

## Stealth — moving while hidden

Plain Hiding drops the moment you take a step. **[Stealth](/skills/stealth/)** lets you
**move without breaking your hidden state**:

**To stealth:**

1. **Hide first** (you must already be hidden to begin stealthing — otherwise you get
   *"You must hide first."*). You also need **Hiding of at least 30** to stealth at all on
   this shard (*"You are not hidden well enough. Become better at hiding."* below that).
2. Move one tile at a time; the [Stealth](/skills/stealth/) skill is checked on each step.

- Each successful stealth activation grants a **budget of steps** equal to your **Stealth
  value divided by 5** (minimum 1) on this shard — so GM Stealth gives 20 quiet steps
  before you must re-check. (`Stealth.cs`: `steps = Value / 5.0` in the AOS+ branch that
  applies to our EJ shard; the older pre-AOS rule was value/10.)
- Stealthing works best unarmored or in light armor. Your worn armor is summed into an
  **armor rating**, and the more you wear the harder the per-step check becomes
  (`CheckSkill(Stealth, -20 + armorRating*2, 60 + armorRating*2)`). If your armor rating
  exceeds the cap (**42** on this AOS+ shard) you simply **cannot move quietly** — *"You
  could not hope to move quietly wearing this much armor."*
- A failed Stealth step **reveals you** (*"You fail in your attempt to move unnoticed."*);
  re-hide and continue. A success shows *"You begin to move quietly."*

## Detecting Hidden — revealing others

**[Detecting Hidden](/skills/detecting-hidden/)** finds nearby hidden players and
creatures.

**To detect:**

1. Use the **Detecting Hidden** skill (*"Where will you search?"*).
2. **Target an area/spot** you suspect a hidden character is in (the cursor reaches up to
   12 tiles).
3. Any hidden target within range that you out-roll is revealed (*"You have been
   revealed!"*); if none, you see *"You can see nothing hidden there."*

Your search **range scales with skill** — `max(2, DetectHidden / 10)` tiles, **halved if
your skill check fails**, and raised to 22 inside a house you are friended to (`DetectHidden.cs`).
Whether each hidden mobile is revealed is a **contest**: your `DetectHidden ±10` versus the
hider's `Hiding ±10` (`DetectHidden.cs`), so higher Detecting Hidden relative to the hider's
Hiding wins more often. This is the active counter to stealthers — guards, anti-thieves, and
PvPers train it.

## Tracking — finding creatures and players

**[Tracking](/skills/tracking/)** locates nearby mobiles even if they are not in view.

**To track:**

1. Use the **Tracking** skill.
2. Choose one of four **categories** from the menu — **Animals, Monsters, Human NPCs, or
   Players** (`Tracking.cs` TrackWhatGump).
3. You get a list and a direction toward the nearest matching targets within range.

Your tracking **range is `10 + Tracking / 10`** tiles (`Tracking.cs`), so higher skill
finds targets farther off. Against **hidden players** Tracking runs a difficulty check that
weighs your **Tracking (and Detect Hidden)** against the target's **Hiding + Stealth** — you
only get a fix on them if that check passes. Note Tracking **locates but does not reveal**:
it can tell you a stealther's presence and direction, but you still need **Detecting
Hidden** (or a Reveal spell) to actually unhide them. Useful for hunting, scouting, and
catching thieves.

## What reveals you

You lose your hidden state when you:

- **Attack** or take a hostile action (e.g. Double Strike / Whirlwind call `RevealingAction`).
- **Cast a spell** (a normal cast reveals you — `Spell.cs` `RevealOnCast` is true, calling
  `RevealingAction()`).
- **Use a bandage** (the bandage code calls `RevealingAction()` on both double-click and
  target — `Bandage.cs` — see [Healing](/playing/healing/)).
- **Take damage** / are hit.
- **Are adjacent** to certain creatures or stand too close for too long (proximity reveal —
  unverified specifics).
- Are caught by **Detecting Hidden** or a **Reveal** spell ([Magery](/skills/magery/)
  6th circle, confirmed in `Scripts/Spells/Sixth/Reveal.cs`), which forcibly unhides
  characters in an area.

In short: **acting reveals you.** Hiding/Stealth is for moving and observing, not for
acting while invisible.

## Uses for hiding and stealth

- **Escaping** — break [line of sight](/playing/combat-basics/#range-melee-adjacency-vs-ranged-line-of-sight),
  then Hide to drop pursuers and recover or [Recall](/playing/movement-and-travel/) away.
- **Scouting** — Stealth into a dungeon or PvP zone to spot enemies, count numbers, and
  find loot without being seen.
- **Thief play** — [Stealing](/skills/stealing/) and [Snooping](/skills/snooping/) pair with
  Hiding/Stealth to lift items and slip away; see [Notoriety & PvP](/playing/notoriety-and-pvp/)
  for the criminal flags this triggers.
- **Assassin play** — Stealth into position, open with a strong hit or a
  [Ninjitsu](/skills/ninjitsu/) move; note attacking immediately reveals you.

## See also

- [Hiding](/skills/hiding/), [Stealth](/skills/stealth/), [Detecting Hidden](/skills/detecting-hidden/), [Tracking](/skills/tracking/)
- [Combat basics → Fleeing](/playing/combat-basics/#fleeing)
- [Movement & travel](/playing/movement-and-travel/)
- [Stealing](/skills/stealing/), [Snooping](/skills/snooping/), [Ninjitsu](/skills/ninjitsu/)
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — flags from thief/assassin actions
