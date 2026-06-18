---
title: Aquariums
description: Keep a house aquarium stocked and maintained — feed it, keep the water fresh, and it rewards you over time with fish, decorations, and rare collectibles.
status: source-verified
sources:
  - "servuo: Scripts/Items/Addons/Aquarium/Aquarium.cs (BaseAddonContainer, daily evaluation, food/water states, live/dead creatures)"
last_verified: 2026-06-18
generated: false
---

An **aquarium** is a house addon you stock with fish and **maintain** — a low-key collection
hobby that pays out decorations and rare aquatic items over time, as long as you keep your fish
alive.

## Keeping it alive

The aquarium is a special container (`Aquarium`, a `BaseAddonContainer`) that **evaluates its
state once a day** (`EvaluationInterval = 1 day`). Two things decide whether your fish thrive:

- **Food** — feed the aquarium (fish food); its **food state** runs from empty up through
  **Full** (and even **Overfed**).
- **Water** — keep the **water state** fresh (it degrades and must be refreshed).

Healthy food + water lets more **live creatures** survive (`MaxLiveCreatures` scales with how
well-fed and well-watered it is); neglect it and fish die off (`DeadCreatures`). Stock it with
fish you catch ([Fishing](/skills/fishing/)) or buy.

## Rewards

A well-kept aquarium periodically yields **rewards** — decorative items, rare fish, and aquatic
collectibles — as a payoff for steady upkeep. It's a slow, passive loop: tend it daily, harvest
what it produces.

## See also

- [Fishing](/skills/fishing/) — catch the fish to stock it
- [Decorating](/playing/decorating/) — the aquarium and its rewards as house décor
- [Housing](/playing/housing/) — placing the aquarium addon
