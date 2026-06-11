---
title: Cartography
description: Draw and decode maps, including treasure maps.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo)"
  - "servuo: Scripts/Services/Craft/DefCartography.cs"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapInfo.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/12.gif" alt="Cartography skill banner" width="160" />

Cartography draws maps and, more importantly, decodes treasure maps. The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table and skill thresholds below are source-verified
against ServUO.

## What it does

Cartography lets you craft local, city, and world maps from blank maps, and decode the
treasure maps dropped by monsters so the buried chest can be located and dug. It is the gateway
skill for treasure hunting, paired with [Mining](/skills/mining/) (to dig) and
[Lockpicking](/skills/lockpicking/)/[Remove Trap](/skills/remove-trap/) (to open the chest).

## How to use it

- **Crafting maps** — use a mapmaker's pen on a blank map to open the menu and draw a map.
- **Decoding treasure maps** — double-click an unmarked treasure map; a skill check decodes
  it and marks the dig location. See [gathering resources](/playing/gathering-resources/).

## How to train it

- **Low skill** — craft local and city maps from blank maps (cheap, repeatable).
- **Mid skill** — sea charts and world maps; then begin decoding low-level treasure maps.
- **High skill** — decode higher-level treasure maps for the steadiest gains and the loot.

See [skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Cartographer |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +0.75, Int +0.75 (per-use stat gain weights) |

Map crafting thresholds (from `Scripts/Services/Craft/DefCartography.cs`): Local Map **10.0**,
City Map **25.0**, Sea Chart **35.0**, World Map **39.5** minimum skill. Treasure-chest
required skills scale by level (`Scripts/Services/TreasureMaps/TreasureMapInfo.cs`): roughly
**5 / 45 / 75 / 80 / 80** by tier, with the chest's lock level set to required skill − 10 and
max lock level required skill + 40 — informing the [Lockpicking](/skills/lockpicking/) needed
to open it.

## Related skills & synergies

- **[Mining](/skills/mining/)** — dig the chest once the map is decoded.
- **[Lockpicking](/skills/lockpicking/) + [Remove Trap](/skills/remove-trap/)** — open the
  trapped chest.
- **[Tracking](/skills/tracking/) + [Camping](/skills/camping/)** — round out an
  explorer/treasure hunter who roams the wilds.

## See also

- [Gathering resources](/playing/gathering-resources/) · [Cartography crafting](/crafting/cartography/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
