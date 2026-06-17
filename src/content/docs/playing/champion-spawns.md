---
title: Champion Spawns
description: How champion spawns work — the escalating monster levels, the champion bosses, power scrolls and other rewards (Felucca vs other facets), and the Harrower super-boss summoned from champion skulls.
status: source-verified
sources:
  - "servuo: Scripts/Services/ChampionSystem/ChampionSpawn.cs (levels, kills, restart, Felucca power-scroll vs SoT drops)"
  - "servuo: Scripts/Mobiles/Bosses/BaseChampion.cs (GivePowerScrolls, CreateRandomPowerScroll tiers, gold/artifact/primer)"
  - "servuo: Scripts/Services/ChampionSystem/ChampionSpawnType.cs (spawn types → champions)"
  - "servuo: Scripts/Services/ChampionSystem/ChampionSkullPlatform.cs + Mobiles/Bosses/Harrower (six skulls → Harrower)"
  - "servuo: Scripts/Services/ChampionSystem/ChampionSystem.cs (PowerScrollAmount=6)"
last_verified: 2026-06-17
generated: false
---

A **champion spawn** is an escalating monster event: a fixed altar pumps out waves of
increasingly dangerous creatures, and if players kill enough of them a **champion boss**
appears. Champions are the main source of **power scrolls** — the only way to raise a skill's
cap above 100 — which is why a Felucca spawn is as much a **PvP battleground** as a PvM grind.

## How a spawn progresses

Each spawn has an **altar** (the Idol of the Champion marks it) and climbs through **four
levels** of creatures (`ChampionSpawn.cs`):

- You **kill the spawning monsters** to fill a hidden progress meter. Each level spawns a
  tougher set than the last (level 1 rats and headless ones → level 4 dragons and daemons,
  depending on the spawn type).
- Fill a level and the spawn **advances**; the altar's candles light up as it rises.
- **Neglect it and it slides back** — if players stop killing, the level decays, and an
  abandoned spawn fully **resets after ~10 minutes** (`RestartDelay`).
- When the final level is maxed, the **Champion boss spawns**. Kill it for the rewards below.

## The champions

Each spawn is one **type**, with its own themed creatures and boss (`ChampionSpawnType.cs`):

| Spawn type | Champion |
|---|---|
| Abyss | **Semidar** |
| Arachnid | **Mephitis** |
| Cold Blood | **Rikktor** |
| Forest Lord | **Lord Oaks** |
| Vermin Horde | **Barracoon** |
| Unholy Terror | **Neira** |
| Sleeping Dragon | **Serado** |
| Glade | **Twaulo of the Glade** |
| Corrupt | **Ilhenir the Stained** |
| Terror | **Abyssal Infernal** |
| Infuse | **Primeval Lich** |

## Rewards

When the champion dies, rewards go to the players who **did the most damage** during the
fight (`BaseChampion.GivePowerScrolls`):

- **Power scrolls** — the headline reward. **6 scrolls** drop per champion
  (`PowerScrollAmount`), each raising one skill's cap to **105 (Wonderous), 110 (Exalted),
  115 (Mythical), or 120 (Legendary)**. The roll is weighted toward the lower tiers — only
  **~5%** are the coveted **120 Legendary**. They cover combat and crafting skills
  (Swords/Fencing/Macing/Archery/Wrestling, Tactics, Parry, Magery, Blacksmithy, Tailoring, …).
- **⚠️ Power scrolls are Felucca-only.** On a **Felucca** spawn the boss drops power scrolls
  *and* Scrolls of Transcendence; on other facets it drops **Scrolls of Transcendence only**
  (instant partial skill gains). This — plus open PvP — is why serious players run Felucca
  spawns.
- **Gold shower**, a chance at an **artifact**, and **skill-mastery primers** round out the
  loot.

## The Harrower

Every champion also yields a **champion skull** of one of **six types** — **Power,
Enlightenment, Venom, Pain, Greed, and Death** (`ChampionSkullPlatform.cs`). Collect **all
six** and place them on the braziers of a **Champion Skull Platform**, and they summon the
**Harrower** — a super-boss — opening a gate to its lair (the Star Room). The Harrower is the
toughest encounter in this chain and pays out the **largest haul of scrolls** (including the
top-tier 120 power scrolls and stat scrolls) to those who bring it down.

## Where to find them — and the PvP

Champion spawns sit deep in many **[dungeons](/world/dungeons/)** (Despise, Deceit, Shame,
Covetous, Destard, and others all host one). On this shard:

- In **Felucca**, a champion spawn is **open-PvP** — guilds and raiders fight over the boss
  and its power scrolls, so bring friends, an escape plan, and expect company. See
  [Notoriety & PvP](/playing/notoriety-and-pvp/) and [Factions (Vice vs Virtue)](/playing/factions/).
- Come prepared: a spawn is a long fight against scaling numbers. Tactics-and-Anatomy melee,
  a tamer's pets, or a bard's [Provocation](/skills/provocation/) all shine here — see the
  [character templates](/templates/).

## See also

- [Dungeons](/world/dungeons/) — where the spawns and their champions live
- [Notoriety & PvP](/playing/notoriety-and-pvp/) · [Factions (Vice vs Virtue)](/playing/factions/) — fighting over the loot
- [Bestiary: bosses](/bestiary/bosses/) — the champions' stats
- [Treasure hunting](/playing/treasure-hunting/) — the other end-game loot loop
