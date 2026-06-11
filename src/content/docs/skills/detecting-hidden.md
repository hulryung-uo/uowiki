---
title: Detecting Hidden
description: Reveal hidden players, creatures, and traps.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Skills/DetectHidden.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/14.gif" alt="Detecting Hidden skill banner" width="160" />

Detecting Hidden is the counter to [Hiding](/skills/hiding/) and [Stealth](/skills/stealth/).
The prose is community-derived (paraphrased from the uorenaissance.com skill list plus ServUO
behavior) pending field verification; the stats table and range formula below are
source-verified against ServUO.

## What it does

Detecting Hidden reveals hidden or stealthing characters and creatures in an area around a
chosen spot, and helps spot trapped containers. It is the scout's and PvP defender's answer
to anyone sneaking up — and on a treasure hunter, a way to find trapped chests. See
[hiding & stealth](/playing/hiding-and-stealth/).

## How to use it

Activate the skill and target a location. If the roll succeeds, hidden things within range of
that point are revealed (your own roll vs. their Hiding/Stealth). See
[targeting](/playing/targeting/).

## How to train it

- **Low/high skill** — use the skill repeatedly in areas where hidden things plausibly are
  (dungeons, near other players). Reveals against actual concealed targets are the reliable
  gainers; a training partner who hides repeatedly is the fastest route.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Scout |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +0.4, Int +0.6 (per-use stat gain weights) |

From `Scripts/Skills/DetectHidden.cs`: the reveal radius is `max(2, skill / 10)` tiles — so
about **10 tiles at GM**. On a **failed** skill check the range is **halved**. Whether a given
hidden target is revealed is then an opposed roll using the detector's skill (±10 random)
against the target's concealment.

## Related skills & synergies

- **Counters [Hiding](/skills/hiding/) + [Stealth](/skills/stealth/)** — the cat to their
  mouse.
- **[Tracking](/skills/tracking/)** — Tracking's reveal chance against hidden targets
  factors in Detect Hidden (see Tracking).
- **[Remove Trap](/skills/remove-trap/) + [Lockpicking](/skills/lockpicking/)** — spotting
  trapped chests fits the treasure-hunter kit.

## See also

- [Hiding & stealth](/playing/hiding-and-stealth/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
