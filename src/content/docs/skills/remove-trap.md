---
title: Remove Trap
description: Disarm trapped containers.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 48, Remove Trap)"
  - "servuo: Scripts/Skills/RemoveTrap.cs"
  - "servuo: Scripts/Mobiles/Normal/BaseCreature.cs (CheckTeach EJ guard)"
  - "servuo: Config/Expansion.cfg (CurrentExpansion=EJ)"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/48.gif" alt="Remove Trap skill banner" width="160" />

Remove Trap detects and disables traps on containers. The stats table and timing/mechanic
notes below are source-verified against ServUO; the general training advice is community
guidance pending field verification.

## What it does

Remove Trap lets you disarm the traps on chests and containers — explosion, dart, and poison
traps on dungeon and treasure chests — so you can loot them safely instead of eating the
blast. It is the companion to [Lockpicking](/skills/lockpicking/) and
[Detecting Hidden](/skills/detecting-hidden/) on a treasure hunter.

## How to use it

Stand next to the trapped container (you must be in range), use the skill, and target it. A
successful roll clears the trap. On treasure chests the work takes longer the higher the
chest tier. See [gathering resources](/playing/gathering-resources/).

## How to train it

**Quick start:** an NPC Tinker or Thief Guildmaster teaches Remove Trap up to **one-third of
its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
`baseToSet = ourSkill.BaseFixedPoint / 3`; on this EJ shard the old Lockpicking/Detect-Hidden
prerequisite for being taught is waived — see CheckTeach's `!Core.EJ` guard) — buy to ~30–42.

The classic rig: **have a [Tinker](/skills/tinkering/) trap boxes at a difficulty matched to
your skill, then disarm them in a loop** (re-trap and repeat).

- **Low/mid skill** — disarm those tinker-trapped boxes; you must first **detect** the trap
  ([Detect Hidden](/skills/detecting-hidden/) helps) before you can remove it.
- **High skill** — disarm real dungeon and treasure-map chests. GGS guarantees the slow late
  points as long as you keep disarming.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Trap Specialist |
| Mastery skill | No |
| Gain notes | no stat gain on use (Str +0 / Dex +0 / Int +0) |

From `Scripts/Skills/RemoveTrap.cs`: there is a **10-second** reuse delay (the OnUse return),
the disarm target reaches only **2 tiles** (`InternalTarget : base(2, …)`), and on success the
chest's `TrapPower`, `TrapLevel`, and `TrapType` are all cleared. An ordinary trapped container
rolls `CheckTargetSkill(RemoveTrap, chest, TrapPower, TrapPower + 10)`.

New-system treasure chests use a longer timed disarm instead. With Remove Trap **≥ 100** the
work is a fixed safety window by tier — **20 / 60 / 180 / 420 / 540 seconds** for
Stash / Supply / Cache / Hoard / Trove (measured from when the chest was dug). Below 100 it is
a repeating 10-second skill-check loop that can spawn an Ancient Chest Guardian on a failed
tick.

On this shard (**EJ** expansion, per `Config/Expansion.cfg`) the old requirement to *use*
Remove Trap — Lockpicking ≥ 50 and Detecting Hidden ≥ 50 — is also waived by the same
`!Core.EJ` guards in `OnUse`, so any skill level can attempt a disarm.

## Related skills & synergies

- **[Lockpicking](/skills/lockpicking/) + [Detecting Hidden](/skills/detecting-hidden/) +
  [Cartography](/skills/cartography/) + [Mining](/skills/mining/)** — the treasure-hunter
  toolkit.
- **[Tinkering](/skills/tinkering/)** — crafts the trapped boxes used to train.

## See also

- [Gathering resources](/playing/gathering-resources/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
