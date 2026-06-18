---
title: Huntmaster Challenge
description: Hunt the biggest specimen of a target creature, document the kill with a hunting permit, mount it as a trophy, and compete on the best-kill leaderboard.
status: source-verified
sources:
  - "servuo: Scripts/Services/HuntmasterChallenge/ (HuntingSystem, HuntingPermit, BestKillBoard, HuntTrophy, taxidermy)"
last_verified: 2026-06-18
generated: false
---

The **Huntmaster Challenge** is a recurring hunting competition: take a **hunting permit**, slay
the **biggest specimen** of the season's target creature, and either mount it as a **trophy** or
submit it to the **leaderboard** to compete for the title of best hunter.

## How a hunt works

1. **Get a hunting permit** (`HuntingPermit`) — it's the document that records your kill.
2. **Hunt the target creature.** When you make a qualifying kill, the permit captures it as a
   **documented kill** (with a measured "size" for that specimen).
3. **Make it count** — you can either:
   - **Taxidermy it into a trophy** (`HuntTrophy` / display trophy) to hang in your house — a
     bigger specimen makes a more impressive mounted trophy; or
   - **Submit it to the Best Kill Board** (`BestKillBoard`) to enter your specimen on the
     **leaderboard** for that creature.

## Competing

- The **best-kill board** tracks the largest documented kills — beat the record to top the
  board. It's a recurring/seasonal challenge, so records turn over.
- Participation and standout kills pay out **hunter rewards** (`HuntMasterRewardGump`,
  resource satchels and reward items).

## Why do it

It's a **PvE bragging-rights** loop with house-décor payoff — a wall of measured trophies from
Britannia's most dangerous game, plus a shot at the leaderboard. A natural fit for combat
characters who want a goal beyond loot.

## See also

- [Bestiary](/bestiary/) — the creatures you'll be hunting
- [Where to find creatures](/world/where-to-find-creatures/) — where the targets roam
- [Decorating](/playing/decorating/) — mounting your trophies
