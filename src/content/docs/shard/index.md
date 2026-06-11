---
title: Shard Identity Card
description: This shard at a glance — expansion, skill and stat caps, and core rates, straight from the server configuration.
status: source-verified
sources:
  - "servuo: Config/Expansion.cfg"
  - "servuo: Config/PlayerCaps.cfg"
  - "servuo: Config/General.cfg"
  - "servuo: Config/TestCenter.cfg"
last_verified: 2026-06-11
generated: false
---

:::note[What "ServUO" means here]
A **shard** is a running Ultima Online game world (a server instance). This shard runs on
**[ServUO](https://www.servuo.com/)** — an open-source Ultima Online **server emulator**:
the software that reimplements the UO server so a community can host its own world. So
"ServUO" throughout this wiki refers to that emulator's source code (where the rules and
numbers are defined), not to the live server itself.
:::

One shard, one set of rules — these are the numbers this shard is actually running with, read
directly from `Config/*.cfg` in the ServUO emulator's configuration.

## Expansion

| Setting | Value | Source |
|---------|-------|--------|
| Expansion | **EJ (Endless Journey)** | `Config/Expansion.cfg` (`CurrentExpansion=EJ`) |
| Test Center mode | Disabled | `Config/TestCenter.cfg` (`Enabled=False`) |

EJ is the most modern ruleset the ServUO emulator offers: AOS combat math, ML-era stat gain, SA races and
skills are all in effect. Where this wiki says "AOS-era" or "ML-era" behavior, it applies here.

## Skill caps (`Config/PlayerCaps.cfg`)

| Setting | Value | Notes |
|---------|-------|-------|
| Individual skill cap | **100.0** (`SkillCap=1000`) | Raisable per-skill via Power Scrolls where applicable. |
| Total skill cap | **700.0** (`TotalSkillCap=7000`) | At the cap, new gains require setting another skill to lower (arrow down). |
| Anti-macro code | **Disabled** (`EnableAntiMacro=False`) | No same-spot/same-target gain throttling. See [skill gain](/mechanics/skill-gain/). |

## Stat caps (`Config/PlayerCaps.cfg`)

| Setting | Value |
|---------|-------|
| Total stat cap | **225** (`TotalStatCap=225`) |
| Strength / Dexterity / Intelligence cap | **125** each (`StrCap`/`DexCap`/`IntCap=125`) |
| Enhanced per-stat maximum | **150** each (`StrMaxCap`/`DexMaxCap`/`IntMaxCap=150`) |
| Stat gain chance | **5%** per qualifying skill use (`PlayerChanceToGainStats=5.0`) |
| Stat gain time delay | **Disabled** (`EnablePlayerStatTimeDelay=False`) |
| Pet stat gain chance / delay | 5% / disabled (`PetChanceToGainStats=5.0`, `EnablePetStatTimeDelay=False`) |

Details on how these interact: [stat gain mechanics](/mechanics/stat-gain/).

## World behavior (`Config/General.cfg`)

| Setting | Value |
|---------|-------|
| Ground item decay | **60 minutes** (`DefaultItemDecayTime=60`) |
| Murderers (reds) | **Felucca only** (`RestrictRedsToFel=True`) |

## More

- [Server rules and rates](/shard/server-rules/) — housing, loot budgets, treasure maps,
  vendors, saves and restarts
- [Getting started](/guides/getting-started/) — what kind of shard this is and who lives here
