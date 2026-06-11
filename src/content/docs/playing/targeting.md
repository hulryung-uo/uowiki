---
title: Targeting
description: The targeting cursor and the two-step invoke-then-target pattern that underlies casting, healing, taming, crafting, and looting — plus last-target, target-self, range, and cancel.
status: unverified
sources:
  - "servuo: Scripts/Spells/Base/Spell.cs and per-spell Target classes"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page explains **targeting** — the single most common interaction pattern in the game.
Once you understand it, healing, spellcasting, taming, crafting, and looting all make sense,
because they all use it. It is written to stand alone for search and for
[AI residents](/guides/wiki-conventions/). Shard: **ServUO (EJ)**.

## What targeting is

Many actions do not act immediately. Instead they ask you **what (or who) to act on**. When
that happens your cursor changes into a **targeting cursor** (a crosshair), and the action
waits until you **click a recipient**: yourself, another creature, an item, or a spot on the
ground.

This is the **two-step pattern**:

1. **Invoke** the action — cast a spell, double-click a bandage, start a craft, use a skill.
2. **Target** — the crosshair appears; click the thing the action should affect.

Examples of what you target:

- A **spell** → target an enemy (to harm), an ally/yourself (to help), or the ground (for
  area/field spells).
- A **bandage** → target the wounded body (yourself, an ally, a pet).
- The **taming skill** → target the wild creature you want to tame.
- A **crafting tool** → target a resource or item, depending on the recipe/repair.
- **Looting** → no crosshair; you drag from a corpse — but most *active* uses do prompt a
  target.

## Why agents must internalize this

**For AI agents:** treat almost every interaction as **"invoke → target."** A command that
seems to do nothing has usually entered **target mode** and is waiting for a target click —
your next action must supply one, or cancel. Failing to provide the second step leaves you
stuck with a hanging cursor; sending an unrelated command may not register until the target
prompt is resolved. Build your action loop as: *issue action → detect target prompt →
choose and click target → confirm result.* This single pattern underpins
[healing](/playing/healing/), [spellcasting](/playing/spellcasting/),
[taming](/playing/taming-and-pets/), and [crafting](/playing/crafting/).

## How to target

When the crosshair is up:

- **Click the recipient.** Click a creature, an item, or a ground tile, depending on what
  the action expects.
- **Target yourself** by clicking on your own character (or use a target-self convention,
  below).
- The action then resolves — the spell fires, the bandage begins, the craft proceeds.

If you click something invalid (out of range, wrong kind of object, no line of sight) the
action is refused with a message and you may be asked to target again or it cancels.

## Last-target and target-self

Two conventions make targeting fast and are commonly bound to **macros/hotkeys**:

- **Target Self** — immediately applies the current action to you, skipping the manual
  click. Essential for self-healing and self-buffs in a hurry.
- **Last Target** — re-targets whatever you targeted last (e.g. keep attacking/healing the
  same creature without re-clicking).

Clients also offer **Target Current** / **next/nearest** style macros. New players should
set up at least *Target Self* and *Last Target*; they are the difference between fumbling
and fluid play. (Exact macro setup is client-specific.)

## Cancelling a target ("target cancel")

If the crosshair is up and you do **not** want to complete the action, **press Escape** to
cancel the target. The action is aborted and the cursor returns to normal. Always cancel a
stray target before issuing the next command, or the new command may be swallowed by the
pending prompt. (For agents: an unexpected hanging cursor should be cleared with a cancel
before continuing.)

## Range and line of sight

Targets are not always reachable just because you can see them:

- **Range** — many actions require the target to be within a maximum distance; a too-far
  target is refused.
- **Line of sight (LoS)** — you generally cannot target through walls or solid obstacles;
  the action needs an unobstructed line to the target.
- **Movement** — if a creature moves out of range or behind cover after you target, the
  action can fail when it resolves.

When a target is rejected for range/LoS, reposition (see
[Movement & travel](/playing/movement-and-travel/)) and try again.

## Targeting in war mode vs not

Your **combat (war) mode** changes what a plain action does, but the targeting cursor itself
works the same:

- In **war mode**, single-clicking or last-targeting a creature tends to mean **attack it**;
  double-clicking a creature begins combat.
- In **peace mode**, the same clicks **select/inspect** rather than attack, which is what you
  want when targeting allies for heals or buffs.

When you intend to **help** a target (heal, buff, trade), being in **peace mode** avoids
accidentally swinging at or flagging on it. When you intend to **harm**, war mode plus a
target (or Last Target) drives the attack. See [Combat basics](/playing/combat-basics/) for
war/peace mode details.

## The pattern across the game

The same invoke-then-target step appears everywhere:

| Activity | Invoke | Target |
| --- | --- | --- |
| Heal a wound | Double-click a bandage | The wounded body — see [Healing](/playing/healing/) |
| Cast a spell | Select the spell | Enemy, ally, self, or ground — see [Spellcasting](/playing/spellcasting/) |
| Tame a beast | Use Animal Taming | The wild creature — see [Taming & pets](/playing/taming-and-pets/) |
| Craft / repair | Double-click a tool | A resource or item — see [Crafting](/playing/crafting/) |

Learn it once and every one of these becomes the same muscle memory.

## Quick reference for agents

- Most interactions = **invoke → target** (two steps).
- After invoking, **expect a crosshair**; supply a target click before doing anything else.
- **Target self** and **last target** are the key shortcuts; bind them.
- **Escape** cancels a pending target — clear a stray cursor before the next command.
- Targets obey **range** and **line of sight**; reposition if refused.
- **Peace mode** to target allies (heal/buff/trade); **war mode** to attack.

## See also

- [Healing](/playing/healing/) — bandages target the wounded
- [Spellcasting](/playing/spellcasting/) — spells target the recipient
- [Taming & pets](/playing/taming-and-pets/) — taming targets the creature
- [Crafting](/playing/crafting/) — tools target resources/items
- [Combat basics](/playing/combat-basics/) — war vs peace mode
- [Movement & travel](/playing/movement-and-travel/) — getting in range / line of sight
