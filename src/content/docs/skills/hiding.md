---
title: Hiding
description: Vanish from sight anywhere, no tools or targets required — the lowest-friction skill to train in Britannia.
status: field-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 21)"
  - "servuo: Scripts/Skills/Hiding.cs (10s reuse delay, success/fail messages)"
  - "in-game: foundry thief evals 2026-06-11 (anima run bc201 cycles 5-6, agents Shade — data/trajectories/eval-evobc201c5*/c6*, agent logs data/eval_logs/agent-evobc201c5*)"
  - "in-game: foundry thief eval 2026-06-12 (run c16f4 cycle 2 — 14 'must wait' throttles per 600s seed at ~7s pacing, agent logs data/eval_logs/agent-evoc16f4c2s*)"
last_verified: 2026-06-12
generated: false
---

<img src="/img/skill-flags/21.gif" alt="Hiding skill banner" width="160" />

Step into shadow and the world forgets you. Hiding is the foundation of every
sneak's career — and the single easiest skill in Britannia to practice, because
it needs **nothing**: no tool, no target, no reagent, no particular terrain.

**Stats:** Dexterity (primary), Intelligence (secondary) · **Title:** Rogue

## How it works

Use the skill (skill button or `UseSkill` request) and the server rolls your
Hiding against the situation. Success turns you invisible until you move at speed,
attack, or otherwise reveal yourself. Failure simply costs the attempt's cooldown.

A successful or failed attempt starts a **10-second reuse delay** (the server
answers early retries with *"You must wait a few moments to use another skill"*).
Attempts fired inside the delay are completely wasted — they roll nothing and
gain nothing.

The skill check follows the standard [skill-gain rules](/mechanics/skill-gain/):
gains roll on both success and failure while the task sits inside your gain
window, so early training is fast even when you fail often.

## Training (field-verified)

Repeated use in open terrain trains it reliably — verified by AI field agents
standing on the Minoc mountainside, far from any cover gimmick:

- From base **35.0**, repeated use over a 10-minute session produced steady
  **+0.1 gains** on both successes and failures (three independent sessions,
  fresh characters each).
- **Pace your attempts to the 10-second lockout.** An agent retrying every ~7
  seconds ate 14 *"must wait"* throttles per 10-minute session — one of every
  three attempts wasted. Waiting the full delay between uses is strictly more
  skill per hour.
- **Speaking between attempts does not interrupt training** — a thief who
  muttered a line after every practice run gained at the same rate as a silent
  one (and slightly out-earned it overall in the same window).
- Nearby activity (miners working the same mountainside) did not block
  attempts.

There is no consumable cost, so Hiding is pure time-for-skill — the cheapest
profession entry in the game. The concrete method is simply **stand still away
from others and Use Hide on repeat** (gains best when no one is near); pair it
with [Stealth](/skills/stealth/) once Hiding clears its requirement so you can
move while hidden.

No standard town vendor teaches Hiding (only Ranger/Thief NPCs carry it), so
there's no real buy-up shortcut — but GGS still guarantees the slow late points
as long as you keep hiding. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/).
