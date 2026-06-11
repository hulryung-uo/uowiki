---
title: Forensic Evaluation
description: Read corpses and crime scenes for clues.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Skills/ForensicEval.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/19.gif" alt="Forensic Evaluation skill banner" width="160" />

Forensic Evaluation is a niche investigative skill. The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table and skill-check ranges below are source-verified against
ServUO.

## What it does

Forensic Evaluation examines corpses and certain targets to recover information: who looted a
corpse, how a creature died, and details tied to thieves. On a rogue/thief it can expose who
robbed a corpse; on an investigator it reads the scene. It is a flavorful, low-demand skill
with limited combat or economic payoff.

## How to use it

Activate the skill and target a corpse (or eligible target). A successful roll reveals the
forensic information — for example, the names of those who have looted the body. See
[notoriety & PvP](/playing/notoriety-and-pvp/).

## How to train it

**No town trainer.** Forensic Evaluation is taught only by Healer-type NPCs, not standard
town vendors — for most players there is no convenient trainer, so train it by use from the
start. (Where a Healer does teach it, the cap is **one-third of its skill, capped at 42.0** —
`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach.)

Forensics is an active **"read"** skill — Use it on a corpse (or to inspect a thief's loot
record) and it rolls a gain check each time:

- **Low/mid skill** — evaluate every corpse you come across; your own kills give a steady
  supply, so fight something weak and read each body.
- **High skill** — keep evaluating; harder reads hold the gain window open, and GGS pays out
  the slow late points if you keep using it. Some high-end specifics are **unverified**.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Detective |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +0.2, Int +0.8 (per-use stat gain weights) |

From `Scripts/Skills/ForensicEval.cs`, the skill runs several checks depending on target: a
corpse read uses `CheckTargetSkill(Forensics, target, minSkill, 55.0)`, while higher-tier
reads use ranges up to **36.0–100.0** and **41.0–100.0** — so the upper reads stay useful all
the way to GM.

## Related skills & synergies

- **[Snooping](/skills/snooping/) + [Stealing](/skills/stealing/) +
  [Tracking](/skills/tracking/)** — the rogue/investigator toolkit; Forensics is the
  detective counterpart that exposes thieves.

## See also

- [Notoriety & PvP](/playing/notoriety-and-pvp/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
