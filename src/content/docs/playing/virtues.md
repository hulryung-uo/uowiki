---
title: Virtues
description: The eight virtues of Britannia — how you gain each one, the Seeker/Follower/Knight paths, and the power each virtue grants (self-resurrection, champion challenge, honor combat, and more).
status: source-verified
sources:
  - "servuo: Scripts/Services/Virtues/VirtueHelper.cs (VirtueName, VirtueLevel: Seeker/Follower/Knight, Award/GetLevel)"
  - "servuo: Scripts/Services/Virtues/{Sacrifice,Valor,Justice,Compassion,Honor,Humility,Spirituality,Honesty}.cs (each power)"
last_verified: 2026-06-17
generated: false
---

Britannia is built on **eight virtues**, and they're a real game system — not just lore. By
acting in a virtue's spirit you **gain** in it, and at high enough standing you can **invoke**
a power tied to it. Open the **virtue menu** (the gump on your paperdoll) to see your standing
and invoke the ones that are activated that way.

## The three paths

Each virtue is gained in stages (`VirtueLevel`): **Seeker → Follower → Knight**. Most powers
require at least **Seeker** to invoke, and the strength of the power scales with your level.
Acting *against* a virtue can also cost you standing in it.

## The eight virtues

| Virtue | How you gain it | What it does |
|---|---|---|
| **Sacrifice** | Killing certain powerful/evil creatures for the cause | Grants **resurrections** — invoke to raise the dead (yourself or others); your number of available resurrects scales with your level (`AvailableResurrects`). |
| **Valor** | Fighting champion-spawn creatures | **Invoke on a Champion Idol** to challenge the spawn — instantly advancing it / summoning the champion without grinding every level. See [Champion Spawns](/playing/champion-spawns/). |
| **Honor** | Honorable combat (fighting fair, sparing the helpless) | **"Embrace honor"**, then target a creature to fight it honorably for a **combat bonus** (perfection / extra damage as you fight cleanly). Has a cooldown between uses. |
| **Justice** | Sparing/protecting others rather than killing | **Invoke to protect another player**; when your protectee earns champion **power scrolls**, you receive a share too — the classic protector's reward. |
| **Compassion** | **Escorting NPCs** to their destinations (*not* invoked from the menu) | Passive standing that reflects acts of mercy; built up purely through escort quests. |
| **Humility** | Acts of humility / handicap challenges | Invoke (Seeker+) to **embrace a pet** with humility — a self-handicap for greater reward. |
| **Spirituality** | Spiritual acts | Invoke (Seeker+) to embrace a living target with spirituality. |
| **Honesty** | Returning **lost "honesty" items** | Trove/lost items spawn in the world tagged to an owner or region; **return them** to gain Honesty (and a reward for honest behavior). |

(`VirtueName` order in source: Humility, Sacrifice, Compassion, Spirituality, Valor, Honor,
Justice, Honesty.)

## Why bother

Virtues are quietly powerful end-game tools:

- **Sacrifice** is a free, no-skill **resurrection** option — handy for a fighter with no
  Healing or Magery.
- **Valor** lets a prepared group **skip a champion spawn's grind** and jump to the boss.
- **Justice** is how **protectors** at a Felucca champion spawn share in the power-scroll
  payout without landing the killing blows.
- **Honor** is a real melee **damage buff** for players who fight by its rules.

Most are slow to build — they reward playing *in character* over time — but each pays off with
a power no amount of gold can buy.

## See also

- [Champion Spawns](/playing/champion-spawns/) — where Valor and Justice shine
- [Death & resurrection](/playing/death-and-resurrection/) — Sacrifice as a rez option
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — honor and justice in player conflict
- [The world & its towns](/world/) — Minoc (Sacrifice), Trinsic (Honor), and the virtue cities
