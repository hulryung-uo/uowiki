---
title: Doom — The Gauntlet
description: The Halls of Doom in Malas — a boss-rush gauntlet of mini-bosses ending at the Dark Father, with a point-based artifact reward system and the lever-puzzle entry.
status: source-verified
sources:
  - "servuo: Scripts/Services/Doom/GauntletSpawner.cs (sequenced boss rooms, PlayersPerSpawn=5)"
  - "servuo: Scripts/Services/Doom/{LeverPuzzleController,GuardianRoom}.cs; Scripts/Mobiles/Bosses/DarkFather.cs"
last_verified: 2026-06-18
generated: false
---

**Doom** (the Halls of Doom, in **Malas**) is one of the shard's signature high-end dungeons.
Its centerpiece is **The Gauntlet** — a fixed sequence of mini-boss chambers culminating in the
**Dark Father** — backed by a famous **point-based artifact** reward table. It's the classic
"work for your artifact" grind.

## The Gauntlet

The Gauntlet is a **sequenced boss rush** (`GauntletSpawner`): each chamber spawns a powerful
mini-boss, and clearing one opens the path to the next, room by room, until you reach the
**Dark Father** at the end. The spawn scales around a party (the system sizes encounters with
`PlayersPerSpawn = 5` in mind), so it's built for a group, not a soloer.

## Artifact rewards

Doom's draw is its **artifact loot**: powerful named artifacts awarded for participation. Rather
than a flat drop, your **contribution** to the fights builds toward an artifact reward — keep
fighting the Gauntlet and the Dark Father and your odds of a major artifact accrue. The
surrounding halls also teem with high-end undead and gore fiends for ordinary loot.

## The lever puzzle

Part of Doom is gated behind a **lever puzzle** (`LeverPuzzleController`) and the **Guardian
Room** — a mechanical trial you solve to progress deeper, adding a non-combat wrinkle to the
dungeon.

## Tips

- **Bring a group.** The Gauntlet is tuned for a party; the Dark Father and the mini-bosses hit
  hard.
- A **healer is stationed at the entrance** for convenience — but you'll still need your own
  sustain inside.
- It's in **Malas** — see the [Dungeons](/world/dungeons/) page for the entry and spawn list.

## See also

- [Dungeons](/world/dungeons/) — Doom's location and surrounding spawn
- [Champion Spawns](/playing/champion-spawns/) · [Peerless Bosses](/playing/peerless-bosses/) — the other boss-loot loops
- [Bestiary: bosses](/bestiary/bosses/) — the Dark Father and Doom's mini-bosses
