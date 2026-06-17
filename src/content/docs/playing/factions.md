---
title: Factions (Vice vs Virtue)
description: The shard's faction-style open-PvP system — Vice vs Virtue. How to sign up, what open PvP means, silver, the 30-minute city battles across eight towns, and the silver reward shop. The classic four factions are disabled here.
status: source-verified
sources:
  - "servuo: Scripts/Services/ViceVsVirtue/ViceVsVirtueSystem.cs (Enabled, AddPlayer/resign, IsEnemy/IsAllied, silver)"
  - "servuo: Scripts/Services/ViceVsVirtue/VvVBattle.cs (Duration 30, Cooldown 5, ScoreToWin 10000, sigils/altars)"
  - "servuo: Scripts/Services/ViceVsVirtue/CityInfo.cs (eight battle cities)"
  - "servuo: Scripts/Services/ViceVsVirtue/VvVRewards.cs (silver reward catalog)"
  - "servuo: Scripts/Services/Factions/Core/Faction.cs (Enabled = !VvV.Enabled — classic factions off)"
  - "servuo: Config/VvV.cfg (Enabled=True, StartSilver=2000)"
last_verified: 2026-06-17
generated: false
---

"Factions" on this shard means **Vice vs Virtue (VvV)** — an **opt-in, guild-based open-PvP
system** layered on top of [guilds](/playing/guilds/). It is enabled here
(`VvV.cfg → Enabled=True`), and it **replaces the classic four factions**: ServUO sets
`Faction.Enabled = !ViceVsVirtueSystem.Enabled`, so Minax, the Council of Mages, the True
Britannians, and the Shadowlords are **switched off** on this world. If a guide mentions
joining one of those four, that's the old system — here it's VvV.

## Joining VvV

VvV is joined **per guild member**, and you must be **in a [guild](/playing/guilds/)** to take
part. You sign up through the **Vice vs Virtue signup** window and confirm; the game replies
*"You have joined Vice vs Virtue!"* and your guild's VvV stats start tracking. New
participants begin with **2,000 silver** (`StartSilver`).

## What being in VvV means: open PvP

This is the important part — **VvV is consensual open PvP**:

- Once you're a VvV combatant, **every other VvV player who isn't your ally is your enemy**
  (`IsEnemy` returns true unless you're [allied](/playing/guilds/) — same guild or same guild
  alliance). Enemies can **attack each other on sight**, and the notoriety system permits it
  (`Notoriety.cs` treats VvV enemies as a harmful-allowed relationship).
- Vice and Virtue are the two thematic **alignments** (they flavor the reward cosmetics — Vice
  vs Virtue hues); combat itself is **guild-based** — you fight every non-allied VvV guild,
  not one fixed opposing team.
- **Leaving isn't instant.** Resigning starts a cooldown (about **3 days**) during which you
  stay attackable, and **quitting your guild while in VvV** makes you *"freely attackable by
  members of Vice vs Virtue until your resignation period has ended."* Don't join casually.

Non-VvV players are not dragged in — this is why it's called opt-in.

## Silver

**Silver** is the VvV currency. You earn it by:

- **Killing enemy VvV players** — each kill awards silver, with a **5-minute cooldown per
  victim** (`KillCooldownDuration`) so you can't farm the same person.
- **Battle objectives** — activating altars and winning city battles (below).

Spend silver at the **VvV reward vendor** (next section).

## City battles

The heart of VvV is a rotating **city siege**. A battle besieges one of **eight cities**
(`CityInfo`): **Britain, Jhelom, Minoc, Moonglow, Ocllo, Skara Brae, Trinsic, and Yew.**

How a battle works (`VvVBattle.cs`):

- A battle runs for **30 minutes**, with a **5-minute cooldown** before the next one.
- The contested city spawns a **Sigil** to capture and **Altars** to activate. Holding the
  sigil and **activating altars scores points** (≈ **1,000 points per altar**, plus silver),
  and kills during the battle score too.
- The first guild to reach **10,000 points** (`ScoreToWin`) **wins the battle** and earns
  bonus silver. Scores are tracked **per guild**.
- Joining an active battle is announced to VvV members (*"The City of ~city~ is besieged!"*),
  with on-screen status and a quest-arrow to the action.

## Rewards (the silver shop)

Silver buys VvV-exclusive gear from the reward catalog (`VvVRewards.cs`). A sampling:

| Reward | Silver |
|---|---|
| **Vice / Virtue War Horse** or **War Ostard** statuette (alignment-hued mount) | 500 |
| Potion kegs — Greater Stamina, Supernova, Anti-Paralysis | 500 |
| Trap kits — Poison / Freezing / Shocking / Blades | 250 |
| Essence of Courage | 250 |
| **Stat-Loss Removal** keg | 500 |
| Vice / Virtue hair dye (cosmetic) | 2,500 |

The alignment-hued **war steeds** and dyes are the signature VvV status symbols.

## See also

- [Guilds](/playing/guilds/) — VvV is built on guilds; you join, ally, and score as a guild
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — how attackable status and guard zones work
- [World map](/world/) — the eight battle cities
