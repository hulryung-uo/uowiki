---
title: City Loyalty & Governors
description: Earn loyalty to a city for titles, elect a player Governor, and fund city-wide Trade Deals — the civic system that turns the towns into player-run institutions.
status: source-verified
sources:
  - "servuo: Scripts/Services/City Loyalty System/CityLoyaltySystem.cs (Enabled, CityTitle ladder, TradeDeal list/cost, Governor/election)"
  - "servuo: Scripts/Services/City Loyalty System/{Election,CityDefinition}.cs"
last_verified: 2026-06-18
generated: false
---

The **City Loyalty** system turns Britannia's towns into player-run institutions: you build
**loyalty** to a city, earn civic **titles**, the citizens **elect a Governor**, and that
Governor can buy **Trade Deals** that benefit everyone in the city. It's enabled here
(`CityLoyalty.Enabled`).

## Earning loyalty and titles

Acting in a city's interest (turning in goods, completing its quests, spending there) builds
your **loyalty** to that city. As it rises you climb a ladder of **civic titles**
(`CityTitle`) you can wear:

**Citizen → Knight → Baronet → Baron → Viscount → Earl → Marquis → Duke**

Higher standing makes you eligible to **vote** in that city's elections (and to run for office).

## Governors and elections

Each city periodically **elects a Governor** (`CityElection`) from its loyal citizens —
players vote, and the winner takes the office. The Governor represents the city and, crucially,
controls its **Trade Deals**.

## Trade Deals

A Governor can spend **2,000,000 gold** (`TradeDealCost`) to activate one of the city's
**Trade Deals** — a temporary city-wide perk lasting about a week (`TradeDealCostPeriod` ≈ 7
days, with a cooldown after). Each deal is themed to a guild/profession and buffs that activity
for everyone in the city (`TradeDeal`):

- **Guild of Arcane Arts**, **Bardic Collegium**, **Society of Clothiers**, **Order of
  Engineers**, **Guild of Healers**, **Maritime Guild**, **Merchants Association**, **Mining
  Cooperative**, **League of Rangers**, **Guild of Assassins**, **Warriors Guild**.

So a city whose Governor funds the **Mining Cooperative** is a better place to mine that week; a
**Merchants Association** deal helps traders, and so on — a real incentive to back a Governor
who funds the deal you want.

## Why it matters

- **Titles** are a visible mark of civic standing.
- **Voting and running for Governor** is player politics — guilds court loyalty to install
  their candidate.
- **Trade Deals** make your home city tangibly better for your profession when funded.

## See also

- [The world & its towns](/world/) — the cities you can be loyal to
- [Guilds](/playing/guilds/) — guilds organize loyalty and elections
- [Vendors & banking](/playing/vendors-and-banking/) — spending that supports a city
