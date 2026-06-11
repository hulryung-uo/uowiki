---
title: Blacksmithy
description: Forging weapons and armor from ingots — requirements, example difficulties, colored metals, and training.
status: source-verified
sources:
  - "servuo: Scripts/Services/Craft/DefBlacksmithy.cs"
  - "servuo: Scripts/Misc/ResourceInfo.cs (metal attributes)"
  - "servuo: Server/Skills.cs (SkillInfo 7)"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/7.gif" alt="Blacksmithy skill banner" width="160" />

The ring of hammer on anvil is the sound of Minoc — and of half the realm's economy.
Blacksmiths turn miners' ingots into everything that cuts, bashes, or deflects.

**Stats:** Strength (primary), Dexterity (secondary) · **Title:** Blacksmith

## How it works

Use a **smith's hammer or tongs** while standing near both an **anvil and a forge**
(`DefBlacksmithy.cs`, `CheckAnvilAndForge`, range 2). Pick an item from the craft gump; each
attempt consumes ingots and makes a skill check. Smiths can also **repair** equipment and
**smelt** items back into ingots.

## Example craft difficulties

From the `AddCraft` table (min skill – max skill, iron ingots used):

| Item | Min skill | Max skill | Ingots |
|------|-----------|-----------|--------|
| Dagger | −0.4 | 49.6 | 3 |
| Longsword | 28.0 | 78.0 | 12 |
| Chain tunic | 39.1 | 89.1 | 20 |
| Katana | 44.1 | 94.1 | 8 |
| Plate chest | 75.0 | 125.0 | 25 |

Success chance scales linearly across the min–max window — the standard
[skill check](/mechanics/skill-gain/). A plate chest is not reliably craftable even at 100.0;
exceptional quality demands more still.

## Colored metals

Working colored ingots requires the same skill as mining them (`AddSubRes` table):

| Metal | Skill to work | Metal | Skill to work |
|-------|--------------|-------|---------------|
| Iron | 0 | Gold | 85.0 |
| Dull Copper | 65.0 | Agapite | 90.0 |
| Shadow Iron | 70.0 | Verite | 95.0 |
| Copper | 75.0 | Valorite | 99.0 |
| Bronze | 80.0 | | |

Each metal carries its own attribute bundle (resists, durability, etc.) defined in
`Scripts/Misc/ResourceInfo.cs` — Valorite is the prize. Dragon scales (red, etc.) are a second
resource class for scale armor.

## Training

- **0–30ish:** buy initial skill from an NPC smith — a trainer teaches up to **one-third of
  its own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, CheckTeach:
  `baseToSet = ourSkill.BaseFixedPoint / 3`). Then forge daggers — cheap at a few ingots.
- **Mid skill:** craft items whose difficulty window brackets your skill (the gump shows
  success percentages); **smelt the results back** to recover most ingots and repeat.
- **High skill:** katanas and plate pieces keep the check challenging into the 90s+.
- Crafting "use all resources" batches registers multiple gain checks at once
  (`SkillCheck.cs`, Craft All Gains region). Keep a **bulk ingot supply** so a session never
  stops, and GGS guarantees the slow late points as long as you keep making the hardest item
  you still succeed at. See [using & training skills](/playing/using-and-training-skills/).

## Where

[Minoc](/world/minoc/) — forge, anvil, mountain, and bank within a minute's walk. Every major
city has a smithy; see the [map](https://uomap.vercel.app) for all 295 plotted vendors.

## Related skills

- [Mining](/skills/mining/) — feed the forge
- Tinkering — makes hammers and tongs; Arms Lore historically aids exceptional chance
- [Items: resources](/items/resources/) — ore→ingot tables
