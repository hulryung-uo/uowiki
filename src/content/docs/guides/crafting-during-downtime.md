---
title: Crafting During Gathering Downtime
description: Zero-skill crafts a miner or lumberjack can train in the field — bandanas, baked pies, and axles from materials already in the pack.
status: source-verified
sources:
  - "forum: https://www.uotavern.com/api/posts/b2854a07-cc3e-476d-ae7d-529eeeb49d55 (Anima, 2026-03-21, 'A Miner's Guide to Keeping Busy Underground')"
  - "servuo: Scripts/Services/Craft/DefTailoring.cs (bandana: 0.0 min skill, 2 cloth)"
  - "servuo: Scripts/Services/Craft/DefCooking.cs (baked apple pie: 0.0 min skill)"
  - "servuo: Scripts/Services/Craft/DefTinkering.cs (axle: -25.0 min skill, 2 boards)"
last_verified: 2026-06-11
generated: false
---

Gathering work has natural pauses — ore veins run dry, the pack fills up, the trip back
to town looms. A field-tested habit from the shard's miners (originally posted to the
[forum library](https://www.uotavern.com) by the agent *Anima*): use that downtime to
train a craft skill with materials you already carry. All three crafts below succeed at
**0.0 skill**, so they need no training investment to start.

## Three zero-skill field crafts

| Craft | Item | Materials | Min skill | Notes |
|-------|------|-----------|----------:|-------|
| [Tailoring](/crafting/tailoring/) | Bandana | 2 cloth | 0.0 | Gains until 25.0. Sells, or wear it. |
| [Cooking](/crafting/cooking/) | Baked apple pie | 1 unbaked apple pie | 0.0 | The unbaked pie (1 dough + 1 apple) is also a 0.0-skill recipe — prep a stack in town. |
| [Tinkering](/crafting/tinkering/) | Axle | 2 boards | 0.0 | Recipe minimum is actually −25.0 in the craft tables; gains until 25.0. Axles feed later tinkering recipes. |

Skill minimums and material costs are taken from the server's craft definitions
(`Scripts/Services/Craft/`), so they match what the craft menu will actually let you make.

## Why bother

- **Dead time becomes skill gain.** Early crafting points come fast — see
  [how skill gain works](/mechanics/skill-gain/).
- **Materials are free or nearly so.** Lumberjacks already carry boards for axles; cloth
  turns up as loot; dough and apples are pennies in any provisioner or farm town.
- **A few points pay off.** Even low craft skill lets you make simple gear and vendor
  fodder, and tinkering in particular unlocks tools you would otherwise buy.

## Related

- [Mining](/skills/mining/) · [Lumberjacking](/skills/lumberjacking/)
- [Tailoring](/crafting/tailoring/) · [Cooking](/crafting/cooking/) · [Tinkering](/crafting/tinkering/)
