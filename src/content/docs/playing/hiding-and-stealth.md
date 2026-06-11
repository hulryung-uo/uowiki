---
title: Hiding & Stealth
description: How to hide, move while hidden with Stealth, detect and track others, what reveals you, and how to use stealth to escape, scout, or play thief/assassin.
status: unverified
sources:
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page covers staying unseen: [Hiding](/skills/hiding/) to vanish,
[Stealth](/skills/stealth/) to move while hidden, [Detecting Hidden](/skills/detecting-hidden/)
and [Tracking](/skills/tracking/) to find others, and what gives you away. Combat use of
escaping is in [Combat basics → Fleeing](/playing/combat-basics/#fleeing).

## Hiding — vanishing on the spot

**To hide:**

1. **Stand still** (you cannot hide while moving — that needs Stealth).
2. Activate the **[Hiding](/skills/hiding/)** skill (open your skill list and use Hiding,
   or use a hide hotkey/macro).
3. On success you become **invisible** to other players and most creatures: "You have
   hidden yourself well."; on failure: "You can't seem to hide here."

Your **success chance scales with your Hiding skill** — higher skill hides more reliably
and in riskier situations (near enemies). Standing still and being away from observers
helps; some clients/contexts add modifiers (unverified specifics).

While hidden you do not appear on screen to others and are skipped by many auto-targeting
attacks — until something reveals you (see below).

## Stealth — moving while hidden

Plain Hiding drops the moment you take a step. **[Stealth](/skills/stealth/)** lets you
**move without breaking your hidden state**:

**To stealth:**

1. **Hide first** (you must already be hidden to begin stealthing).
2. Move one tile at a time; the [Stealth](/skills/stealth/) skill is checked on each step.

- You can stealth a **limited number of steps** before you must re-check or risk being
  revealed; **the number of safe steps scales with your Stealth skill** (higher skill =
  more steps). Exact step counts are **unverified** — see [Stealth](/skills/stealth/).
- Stealthing is generally **slower** than open running and works best unarmored or in
  light armor (heavy armor penalizes stealth — unverified specifics).
- A failed Stealth check **reveals you**; re-hide and continue.

## Detecting Hidden — revealing others

**[Detecting Hidden](/skills/detecting-hidden/)** finds nearby hidden players and
creatures.

**To detect:**

1. Use the **Detecting Hidden** skill.
2. **Target an area/spot** you suspect a hidden character is in.
3. On success any hidden target within range is revealed.

Higher Detecting Hidden vs the hider's Hiding/Stealth determines whether you find them.
This is the active counter to stealthers — guards, anti-thieves, and PvPers train it.

## Tracking — finding creatures and players

**[Tracking](/skills/tracking/)** locates nearby mobiles even if they are not in view.

**To track:**

1. Use the **Tracking** skill.
2. Choose a **category** (animals, monsters, humanoids/people, etc.) from the menu.
3. You get a list/arrow toward the nearest matching targets within range.

Higher Tracking shows targets at greater range and can help **reveal** or at least
**locate** stealthers (Tracking can detect the presence/direction of hidden movers —
combine with Detecting Hidden to pin them down). Useful for hunting, scouting, and
catching thieves.

## What reveals you

You lose your hidden state when you:

- **Attack** or take a hostile action.
- **Cast a spell** (casting reveals you — `RevealingAction`).
- **Use a bandage** or many skills/items (the bandage code calls `RevealingAction` on
  use — see [Healing](/playing/healing/)).
- **Take damage** / are hit.
- **Are adjacent** to certain creatures or stand too close for too long (proximity reveal —
  unverified specifics).
- Are caught by **Detecting Hidden** or a **Reveal** spell ([Magery](/skills/magery/)
  6th circle), which forcibly unhides everyone in an area.

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
