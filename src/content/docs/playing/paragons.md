---
title: Paragons
description: Ilshenar's paragon monsters — boosted "champion" versions of ordinary creatures that hit harder, have far more hit points, and drop paragon chests and artifacts.
status: source-verified
sources:
  - "servuo: Scripts/Services/Paragon.cs (Ilshenar-only, stat buffs, spawn chance by fame, chest/artifact chances)"
last_verified: 2026-06-17
generated: false
---

A **paragon** is a supercharged version of an ordinary monster, found only in **Ilshenar**
(`Paragon.cs`, `Map.Ilshenar`). They wear a distinctive **orange-gold hue** and carry a
"(Paragon)" tag — a warning that the lizardman or ogre in front of you hits like something far
nastier, and is carrying far better loot.

## What makes a paragon tougher

When an Ilshenar creature converts to a paragon, its stats are scaled up
(`Paragon.cs` buffs):

| Trait | Multiplier |
|---|---|
| **Hit points** | **×5** (`HitsBuff`) — the big one |
| Strength | ×1.05 |
| Dexterity / Intelligence | ×1.20 |
| Skills | ×1.20 |
| Movement speed | ×1.20 |
| Damage | **+5** flat |
| Fame / Karma | ×1.40 |

So a paragon has **five times the hit points**, moves and casts faster, and adds flat damage —
expect a much longer, more dangerous fight than the base creature.

## How often they appear

Whether a creature spawns as a paragon scales with its **fame** (roughly its power level):
`chance = 1 / round(20 − fame/3200)`, with fame capped at 32,000. In practice, **weak
creatures almost never** become paragons, while **high-fame monsters do so up to ~10%** of the
time. The stronger the base creature, the more likely — and more dangerous — its paragon form.

## The payoff: chests and artifacts

Paragons are worth the trouble because they drop far better loot:

- **Paragon chest** — a **~10% chance** (`ChestChance`) to carry a locked, trapped **paragon
  chest** stuffed with extra gold and loot.
- **Minor artifact** — a fame-and-[luck](/playing/character-and-stats/)-scaled **artifact
  chance** (`CheckArtifactChance`): higher monster fame and higher luck both improve your odds
  of an Ilshenar minor artifact.
- A **~20% chance** to drop a **chocolatiering ingredient**, plus the creature's normal loot at
  boosted amounts.

## Tips

- **Ilshenar only** — you won't find paragons in Felucca/Trammel; this is the facet's
  signature draw.
- **Bring luck.** Artifact odds rise with your luck total, so a luck suit pays off on paragon
  hunts.
- **Respect the ×5 HP.** A paragon of an already-tough creature can be a mini-boss; don't
  pull one expecting the base monster's fight.

## See also

- [Bestiary](/bestiary/) — the base creatures that can become paragons
- [Champion Spawns](/playing/champion-spawns/) · [Peerless Bosses](/playing/peerless-bosses/) — the other boosted-monster loot loops
- [Character & stats](/playing/character-and-stats/) — luck and how it affects drops
- [The world: Ilshenar](/world/) — the paragon facet
