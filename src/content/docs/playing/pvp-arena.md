---
title: PvP Arena
description: Consensual duels in the arena system — ranked or casual, 1v1 or team, with entry-fee pots, pet-slot and potion rules, all in a safe instanced arena.
status: source-verified
sources:
  - "servuo: Scripts/Services/PVP Arena System/ArenaDuel.cs (Ranked, EntryFee/Pot, PetSlots, PotionRules, teams)"
  - "servuo: Scripts/Services/PVP Arena System/{ArenaStone,ArenaGate,ArenaStats}.cs"
last_verified: 2026-06-17
generated: false
---

The **arena system** lets players fight **consensual duels** in a safe, instanced ring — no
criminal flags, no corpse looting, no risk to your gear. It's how you settle a score or train
PvP without going to Felucca.

## Setting up a duel

Use an **Arena Stone** to create or join a duel. You configure the match:

- **Ranked or casual** — ranked duels record your **arena stats** (wins/losses/rating);
  casual ones don't.
- **1v1 or teams** — duel solo or assemble an **arena team** for group fights.
- **Entry fee → pot** — set an entry fee; both sides pay in, and the **winner takes the pot**
  (`Pot`). Set it to zero for a friendly match.
- **Pet slots** — cap how many follower slots pets may use (up to **5**, `MaxPetSlots`);
  set 0 for a no-pets duel.
- **Potion rules** — restrict or allow combat potions (`PotionRules`).

Once both sides accept, an **arena gate** teleports the participants into the instanced arena;
the gate checks your pet count and collects the entry fee on the way in.

## In the ring

- The fight is **safe**: defeat means you're booted from the arena, not killed/looted.
- Pets you bring count against the duel's pet-slot limit.
- The winner is paid the pot, and **ranked** results update your arena rating/stats.

## See also

- [Notoriety & PvP](/playing/notoriety-and-pvp/) — open-world PvP rules (the risky kind)
- [Factions (Vice vs Virtue)](/playing/factions/) — opt-in open PvP for guilds
- [Combat (advanced)](/playing/combat-advanced/) — the mechanics that decide a duel
