---
title: Snooping
description: Peek into other characters' packs.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 28)"
  - "servuo: Scripts/Skills/Snooping.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/28.gif" alt="Snooping skill banner" width="160" />

Snooping lets you secretly look inside another character's backpack. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and skill-check note below are source-verified
against ServUO.

## What it does

Snooping opens the backpack of another player or NPC so you can see what they carry — the
reconnaissance step before a [Stealing](/skills/stealing/) attempt. Done to a player it can
flag you as a **criminal** if you are caught, so rogues snoop from
[hiding](/skills/hiding/)/[stealth](/skills/stealth/). See
[notoriety & PvP](/playing/notoriety-and-pvp/).

## How to use it

Activate the skill and target another character's pack (you must be adjacent). A successful
roll reveals the contents; a noticed snoop on a player risks criminal status. See
[items & inventory](/playing/items-and-inventory/).

## How to train it

**No regular town trainer.** Like Stealing, Snooping is a thief skill no ordinary vendor
teaches (only a wandering Gypsy/Thief NPC carries it), so train it by use.

The trick: **open and peek into other packs, repeatedly.**

- **Low/high skill** — snoop packs over and over. A fellow thief who lets you snoop a stocked
  pack is the classic training partner; **NPC backpacks also work**, so snoop wandering town
  NPCs in a loop. GGS guarantees the slow late points as long as you keep snooping.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Spy |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +2.5 (per-use stat gain weights) |

From `Scripts/Skills/Snooping.cs`: a player snoop succeeds outright if
`Snooping.Value > Random(100)`; otherwise it rolls `CheckTargetSkill(Snooping, container, 0.0,
100.0)`. Being caught snooping another player marks you criminal.

## Related skills & synergies

- **[Stealing](/skills/stealing/) + [Hiding](/skills/hiding/) + [Stealth](/skills/stealth/)**
  — the thief core: hide, stealth in, snoop, steal; see the Thief/Rogue build on
  [seven-GM templates](/templates/seven-gm/).

## See also

- [Notoriety & PvP](/playing/notoriety-and-pvp/) · [Items & inventory](/playing/items-and-inventory/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
