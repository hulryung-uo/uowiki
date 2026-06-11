---
title: Skill Gain
description: How skill gain actually works on this server — the gain-chance formula, GGS guaranteed gains, cap behavior, and anti-macro status.
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs"
  - "servuo: Server/Skills.cs (SkillInfo.GainFactor)"
  - "servuo: Config/PlayerCaps.cfg (EnableAntiMacro, caps)"
last_verified: 2026-06-11
generated: false
---

Every swing, dig, and incantation rolls the same dice. This page documents the actual logic in
`Scripts/Misc/SkillCheck.cs` — the file the server runs.

## The basic flow

When you use a skill, the server makes a **skill check** against a difficulty window
(`minSkill`–`maxSkill`, or a direct `chance`):

- Below `minSkill`: automatic failure, **no gain possible** ("too difficult").
- At or above `maxSkill`: automatic success, **no gain possible** ("no challenge").
- In between: success chance = `(value − minSkill) / (maxSkill − minSkill)`, and a **gain roll**
  happens whether or not the attempt succeeds.

So the training sweet spot is work that is *hard but possible* — and once a task is trivial,
it stops teaching you anything.

## The gain chance (`CheckSkill` → `GetGainChance`)

For each qualifying use, the chance to gain 0.1 skill is computed as:

```
gc = ( (TotalCap − TotalSkills) / TotalCap        // room left under the 700.0 cap
     + (SkillCap − SkillBase) / SkillCap ) / 2    // room left in this skill
gc = ( gc + (1 − difficultyChance) × bonus ) / 2  // harder tasks gain more
gc × = GainFactor                                  // per-skill factor (1.0 for all skills here)
gc = max(gc, 0.01)                                 // never below 1%
```

where `bonus` is **0.5 on a successful attempt** and **0.0 on a failure** (post-AOS rules,
which apply on this EJ shard). Controlled pets get a 100% bonus (doubled chance). The result is
capped at 100%.

Practical consequences:

- **Low skills gain fast, high skills gain slowly** — both your total and the individual skill
  shrink `gc` as they fill up.
- **Any skill below 10.0 gains on every use** (`skill.Base < 10.0` bypasses the roll), and each
  gain below 10.0 is a random 0.1–0.4 jump.
- The floor is 1% per qualifying use, even at 99.9 skill.

## GGS — the Guaranteed Gain System

GGS is **active on this shard** (`GGSActive = !Siege.SiegeShard`, and this is not a Siege
shard). Each skill tracks a `NextGGSGain` time; if you use a skill after that timer expires,
you **gain even if the random roll fails**.

The timer length comes from `GGSTable`, indexed by the skill's level (rows of 5.0 skill) and
your total skill (columns: under 350.0 total / 350.0–699.9 / 700.0). Examples (in minutes):

| Skill level | Total < 350 | Total 350–699.9 | Total 700 |
|------------|------------|-----------------|-----------|
| 0–4.9 | 1 | 3 | 5 |
| 50–54.9 | 27 | 72 | 138 |
| 95–99.9 | 540 | 1440 | 2580 |
| 110–114.9 | 618 | 1662 | 3060 |

In short: keep using a stuck skill and the system eventually pays out — but at high skill the
"eventually" stretches to days.

## Skill cap behavior

- The individual cap is **100.0** and the total cap is **700.0**
  (`Config/PlayerCaps.cfg`; see [the shard card](/shard/)).
- A skill only gains when its lock is set to **up** and it is below its cap.
- At (or near) the total cap, `CheckReduceSkill` lowers a skill you have set to **down** by the
  same amount you gain. No down-flagged skill, no gain. Set your skill arrows deliberately.
- Skill gain is disabled entirely in jail.

## Gain amounts and accelerators

- A normal gain is **0.1** (modified by region `SkillGain`, normally ×1).
- **Scroll of Alacrity** on a skill: each gain becomes 0.2–0.5 while active.
- Mondain's Legacy quest skill bonuses: gains ×2–4 while flagged.

## Anti-macro: disabled

`SkillCheck.cs` contains the classic anti-macro system (max 3 gains per location/target per 5
minutes for flagged skills), but it only runs when `PlayerCaps.EnableAntiMacro` is true — and
this shard has **`EnableAntiMacro=False`** (`Config/PlayerCaps.cfg`). You can train in one
spot without the server pretending not to notice you.

## Related

- [Stat gain](/mechanics/stat-gain/) — every skill gain also rolls for a stat gain
- [Skills index](/skills/) — per-skill training guides
