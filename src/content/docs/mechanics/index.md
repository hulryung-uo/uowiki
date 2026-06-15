---
title: Game Mechanics
description: Index of mechanics pages — how the numbers under the hood actually work on this shard.
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs"
last_verified: 2026-06-11
generated: false
---

Britannia runs on dice, but the dice are public — this shard's server source is open, and these
pages document what it actually rolls.

## Pages

- **[Skill gain](/mechanics/skill-gain/)** — the gain-chance formula, the Guaranteed Gain
  System (GGS), behavior at the skill cap, and why anti-macro checks are off here.
- **[Stat gain](/mechanics/stat-gain/)** — how Strength, Dexterity, and Intelligence grow
  from skill use, and what happens at the 225 stat cap.
- **[Bulk Order Deeds (BODs)](/mechanics/bulk-order-deeds/)** — the point-based crafting-contract
  system: how to obtain small/large deeds, skill gates, and the runic-tool reward catalogs.

## Related references

- [Shard identity card](/shard/) — the configured caps and rates these mechanics read from
- [Skills](/skills/) — the full skill table and per-skill training guides
- [Magic](/magic/) — spell mechanics live in their own section

## A note on verification

Mechanics pages cite exact files in the ServUO source (paths relative to `../servuo`), chiefly
`Scripts/Misc/SkillCheck.cs` and `Server/Skills.cs`. If in-game behavior disagrees with a
formula here, that's a bug in the page or the server — either way,
[file a report](/guides/wiki-conventions/).
