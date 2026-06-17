---
title: Peerless Bosses
description: How peerless bosses work — assembling the key, the altar, the private instanced boss room, the 90-minute slay timer, helper waves, and the artifact/ingredient rewards. The cooperative counterpart to champion spawns.
status: source-verified
sources:
  - "servuo: Scripts/Services/Peerless/BasePeerless.cs (helper waves, OnDeath rewards: ML minor artifact, ingredients)"
  - "servuo: Scripts/Services/Peerless/PeerlessAltar.cs (key validation → MasterKey, TimeToSlay=90m, DelayAfterBossSlain=15m)"
  - "servuo: Scripts/Services/InstancedPeerless/PeerlessInstance.cs (per-party instanced rooms)"
last_verified: 2026-06-17
generated: false
---

A **peerless** is a keyed, **instanced boss fight** for a small party — the cooperative
counterpart to a [champion spawn](/playing/champion-spawns/). Instead of an open free-for-all,
you assemble a **key**, open the boss's chamber, and fight it in a **private room** that
nobody else can crash. They're the *Mondain's Legacy* / *Stygian Abyss* "mini-raid" bosses,
and they drop **minor artifacts** and the **crafting ingredients** high-end gear is built from.

## Getting in: keys and the altar

Each peerless boss is gated behind its own **altar** (`PeerlessAltar.cs`):

1. **Gather the key ingredients.** Every boss requires a specific set of **key items**
   (`Keys`) — usually dropped by the monsters in that boss's region, so you farm the area
   first.
2. **Drop the ingredients on the altar.** When all required keys are present, the altar
   validates them and forges a **Master Key** (`MasterKey`) for the party.
3. **Enter the chamber.** The master key / altar teleports your party into the boss room.

Once opened, the clock starts:

- **You have 90 minutes to slay the boss** (`TimeToSlay`). Run out and the attempt ends.
- After a kill (or expiry) the altar goes on a **15-minute cooldown** (`DelayAfterBossSlain`)
  before it can be opened again.

## It's instanced — and cooperative

Peerless rooms are **instanced** (`PeerlessInstance`): your party gets **its own private copy**
of the boss. Unlike a Felucca champion spawn, **there's no PvP and no outside raiders** — only
the people you brought can enter or interfere. This makes peerless the place for a guild or a
few friends to fight a hard boss **without** worrying about getting jumped. (Be deliberate
about who you key in with — the loot is shared among whoever's inside.)

## Helper waves

Peerless bosses don't fight alone. As the boss takes damage it **summons waves of helper
creatures** (`MaxHelpersWaves`, `SpawnHelpersChance` in `BasePeerless.cs`) — adds that scale
the fight up and punish a party that ignores crowd control. Clear the helpers or they'll
overwhelm your healers before the boss is down.

## The bosses

The peerless roster (`BasePeerless` and the instanced SA bosses):

| Boss | Era / theme |
|---|---|
| **Travesty** | ML — shapeshifting mimic |
| **Dread Horn** | ML — corrupted unicorn of the Twisted Weald |
| **Chief Paroxysmus** | ML — the acid-drowned Palace of Paroxysmus |
| **Lady Melisande** | ML — the Twisted Weald |
| **Monstrous Interred Grizzle** | ML — putrid horror |
| **Shimmering Effusion** | ML — the Prism of Light |
| **Crimson Dragon** | ML |
| **Medusa** | SA — the petrifying gorgon (Stygian Abyss) |
| **Stygian Dragon** | SA |
| **Slasher of Veils** | SA — daemon of the Abyss |
| **Primeval Lich** | SA |
| **Abyssal Infernal** | SA |

## Rewards

When a peerless dies (`BasePeerless.OnDeath`):

- **ML minor artifact** — roughly a **50% chance** (`GivesMLMinorArtifact`) to drop one of the
  Mondain's Legacy minor artifacts.
- **Crafting ingredients** — peerless drop the **special reagents** end-game crafting and
  [imbuing](/skills/imbuing/) consume — **Blight, Scourge, Taint, Putrefaction, Corruption,
  and Muculent** — in quantity.
- **Boss-specific rares** — each boss also has its own signature loot (e.g. Medusa's scales
  and statue rewards).

Because the room is private and the rewards are rich, a peerless run is a classic **guild
night**: gather keys, pick your party, and split the artifacts.

## See also

- [Champion Spawns](/playing/champion-spawns/) — the open-PvP, power-scroll counterpart
- [Bestiary: bosses](/bestiary/bosses/) — peerless stats and resistances
- [Imbuing](/skills/imbuing/) — what the peerless ingredients are for
- [Dungeons](/world/dungeons/) — the regions you farm for keys
