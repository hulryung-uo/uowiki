---
title: Soulstones
description: Move skill points between characters on the same account — store a skill on a soulstone and absorb it onto another character to rebuild a template without re-grinding.
status: source-verified
sources:
  - "servuo: Scripts/Items/Consumables/SoulStone.cs (account-bound, stores one Skill + SkillValue; extract/absorb)"
last_verified: 2026-06-18
generated: false
---

A **soulstone** is the respec tool: it lets you **move skill points off one character and onto
another on the same account**, without grinding the skill back up. It's how you reshape a
template, free up skill points for a new build, or shuffle a trained skill to an alt.

## How it works

A soulstone stores **one skill at a time** (`SoulStone.cs` holds a single `Skill` and its
`SkillValue`), and it is **bound to your account** (`Account`):

1. **Store a skill** — use the soulstone and pick a skill; the points are **pulled off your
   current character** and saved on the stone (your character loses that skill).
2. **Switch characters** — log into another character **on the same account**.
3. **Absorb the skill** — use the soulstone again to **transfer the stored points onto** that
   character (raising or setting that skill).

Because it's account-bound, you **can't** trade skills to another player's account — only
between your own characters.

## What it's for

- **Respec a template** — park a skill you no longer want and free its points for something
  new, then bring it back later if you change your mind.
- **Share trained skills** — grind a skill once and move it to whichever alt needs it.
- **Stay under the cap** — temporarily store a skill to drop under the **700 total skill cap**
  while you train another, then juggle as needed.

Mind your **skill caps** when absorbing — the receiving character still can't exceed the
per-skill and total caps (see [Stat gain](/mechanics/stat-gain/) and the
[shard caps](/shard/)).

## See also

- [Using & training skills](/playing/using-and-training-skills/) — how skills are raised normally
- [Skill gain](/mechanics/skill-gain/) — the grind soulstones let you skip
- [Shard identity card](/shard/) — the 700 total / 100 per-skill caps
