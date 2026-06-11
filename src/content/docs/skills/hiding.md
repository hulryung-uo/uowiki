---
title: Hiding
description: Vanish from sight anywhere, no tools or targets required — the lowest-friction skill to train in Britannia.
status: field-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 21)"
  - "in-game: foundry thief evals 2026-06-11 (anima run bc201 cycles 5-6, agents Shade — data/trajectories/eval-evobc201c5*/c6*, agent logs data/eval_logs/agent-evobc201c5*)"
last_verified: 2026-06-11
generated: false
---

Step into shadow and the world forgets you. Hiding is the foundation of every
sneak's career — and the single easiest skill in Britannia to practice, because
it needs **nothing**: no tool, no target, no reagent, no particular terrain.

**Stats:** Dexterity (primary), Intelligence (secondary) · **Title:** Rogue

## How it works

Use the skill (skill button or `UseSkill` request) and the server rolls your
Hiding against the situation. Success turns you invisible until you move at speed,
attack, or otherwise reveal yourself. Failure simply costs the attempt's cooldown.

The skill check follows the standard [skill-gain rules](/mechanics/skill-gain/):
gains roll on both success and failure while the task sits inside your gain
window, so early training is fast even when you fail often.

## Training (field-verified)

Repeated use in open terrain trains it reliably — verified by AI field agents
standing on the Minoc mountainside, far from any cover gimmick:

- From base **35.0**, repeated use over a 10-minute session produced steady
  **+0.1 gains** on both successes and failures (three independent sessions,
  fresh characters each).
- **Speaking between attempts does not interrupt training** — a thief who
  muttered a line after every practice run gained at the same rate as a silent
  one (and slightly out-earned it overall in the same window).
- Nearby activity (miners working the same mountainside) did not block
  attempts.

There is no consumable cost, so Hiding is pure time-for-skill — the cheapest
profession entry in the game. Pair it with [Stealth](/skills/) once Hiding is
high enough to move while hidden.
