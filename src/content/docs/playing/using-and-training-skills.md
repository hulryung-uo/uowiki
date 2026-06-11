---
title: Using & Training Skills
description: How skills work operationally — invoking active skills, how they rise with use, the 100-per-skill and 700-total caps, locking skills up/down, buying skill from NPC trainers, and reaching Grandmaster.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo table, skill caps)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page explains how **skills** actually work day to day: how to use them, how they go
up, and how to manage your character's total skill budget. For the per-skill detail (what
each skill does, primary stats, titles) browse the [skills index](/skills/); for the math
of how points are awarded see [skill gain](/mechanics/skill-gain/).

## What a skill is

A **skill** is a trained ability — Magery, Swordsmanship, Healing, Mining, and so on. Each
skill has a value from **0.0 to 100.0**. At **100.0 you are a Grandmaster (GM)** of that
skill and earn its mastery title. Your character has many skills, but you cannot max them
all (see caps, below), so a "build" is the set of skills you choose to raise.

Open the **skill list** (the Skills section of the paperdoll / character window) to see all
your skills, their current values, and their lock state.

## Using a skill

Skills come in two operational kinds:

- **Active skills** — you *invoke* them. To use one:
  1. Open your **skill list**.
  2. **Click "Use"** next to the skill (the blue active-skill name), *or* trigger a bound
     **macro / hotkey** for it.
  3. If the skill needs a target (e.g. Animal Taming, Anatomy, Detect Hidden), a **target
     cursor** appears — click the creature, person, or tile.
  Examples: Hiding, Stealing, Animal Taming, Meditation, Begging, Detect Hidden.
- **Passive skills** — they work automatically whenever the situation calls for them; you
  never invoke them. Examples: Resisting Spells, Parrying, Tactics, Anatomy (as a damage
  bonus), Magic Resist. You raise these simply by being in situations where they apply.

Some skills are both: usable on demand *and* checked passively.

## How skills go up

You raise a skill by **using it against an appropriately difficult task**. The game rolls a
skill check on each use; success or failure against a task near your current level can grant
a small **gain**. Tasks that are too easy or too hard for your level grant little or
nothing — you progress fastest against challenges matched to your skill. The exact gain
formula, difficulty bands, and rates are documented in [skill gain](/mechanics/skill-gain/);
read that page before grinding a skill so you target the right difficulty.

Practical rule: **do the activity the skill is for**, against targets that are neither
trivial nor impossible for you, and the number climbs over time.

## Stat gain from using skills

Using skills also slowly raises your **stats** (Strength, Dexterity, Intelligence). Each
skill is tied to a primary and secondary stat, and using it gives a chance to gain in those
stats. For example, casting raises Intelligence; melee fighting raises Strength and
Dexterity. See [stat gain](/mechanics/stat-gain/) for which skills feed which stats and how
the rolls work. Stats are capped (225 total — see [shard caps](/shard/)), and you can lock
individual stats to steer where gains go.

## The skill caps: 100 per skill, 700 total

Two limits shape every build:

- **Per-skill cap: 100.0.** No single skill goes above Grandmaster.
- **Total cap: 700.0** across all skills. The sum of all your skill values cannot exceed
  700 — roughly **seven** skills at GM, or more skills at lower values.

Because of the 700 total, raising one skill past the cap would force another down. You
manage this with **skill locks**.

## Locking skills: up, down, locked

Next to each skill in the skill list is a small **arrow / lock toggle** with three states.
It controls what happens to that skill as you approach the 700 total:

- **Up arrow (raise / ↑):** the skill is *allowed to gain*. Skills you are training should
  be set to Up.
- **Down arrow (lower / ↓):** the skill is *allowed to fall* to make room. When you are at
  the 700 total and a different skill gains, a skill set to **Down** will lose points to
  keep the total legal. Set skills you want to retire to Down.
- **Locked (padlock / ▬):** the skill is **frozen** — it will neither gain nor lose. Use
  this to protect a skill at its current value.

To re-spec a character at the cap: set the skill you want **gone** to **Down**, set the new
skill to **Up**, and train the new skill — the old one bleeds off as the new one rises.
Lock everything else you want to keep.

## Buying skill from NPC trainers

You don't have to grind from zero. **NPC trainers** in towns will teach a skill they know
**up to about 30.0** in exchange for gold (the cap on bought skill is low — roughly the
30 range; exact value **unverified** here). To buy training:

1. Find an NPC who practices the skill (e.g. a Mage for Magery, a Healer for Healing).
2. Say the skill name or ask to learn, or use the context menu, and pay the fee.
3. Each purchase nudges the skill up a little, until the NPC will teach you no more.

Buying gets a new skill off the ground quickly; past the trainer cap you must **use** the
skill to keep raising it.

## Reading the skill list

In the skill list each row shows:

- the **skill name** (clickable = active skill you can Use),
- its current **value** (0.0–100.0),
- its **lock state** (Up / Down / Locked toggle).

At **70** you earn the journeyman-tier title; at **100.0** you become a **Grandmaster** and
display that skill's GM title. Watch the **total** at the bottom against the 700 cap to know
how much room you have left.

## See also

- [Skills index](/skills/) — every skill, what it does, and its primary stat.
- [Skill gain](/mechanics/skill-gain/) — how gains are rolled and how to train efficiently.
- [Stat gain](/mechanics/stat-gain/) — how skill use raises Str/Dex/Int.
- [Spellcasting](/playing/spellcasting/) and [Meditation & mana](/playing/meditation-and-mana/)
  for the caster skills in action.
