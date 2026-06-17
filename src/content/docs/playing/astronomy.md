---
title: Astronomy
description: Stargazing as a pastime — use a telescope to find and discover Britannia's constellations, chart them, and earn the Astronomer title.
status: source-verified
sources:
  - "servuo: Scripts/Services/Astronomy/AstronomySystem.cs (Enabled=Core.EJ, constellations, discovery)"
  - "servuo: Scripts/Services/Astronomy/{Telescope,StarChart,ConstellationLedger,ConstellationInfo}.cs"
last_verified: 2026-06-17
generated: false
---

**Astronomy** is a quiet collecting pastime added in the *Endless Journey* era — it's enabled
here (`AstronomySystem.Enabled = Core.EJ`). Point a **telescope** at the night sky, line up
the coordinates of a hidden constellation, and **discover** it; fill out your chart over many
nights to earn the **Astronomer** title.

## How it works

- **Get a telescope** (a personal telescope, or use a public Brass Orrery) and a **star
  chart**.
- The sky is a coordinate grid — **Right Ascension** (0–24) and **Declination** (0–90)
  (`MaxRA`, `MaxDEC`). Each **constellation** sits at a specific spot that's only visible at
  the right **time of night**.
- **Aim the telescope** to the right RA/DEC at the right time to spot a constellation, then
  **record the discovery**; it's added to your **discovered constellations** list
  (`DiscoveredConstellations`).
- Track your finds in the **constellation ledger**. There are a great many to find
  (`MaxConstellations` is 1,000), so it's a long-term hobby.

## Why do it

Astronomy is a **non-combat collection activity** — the appeal is the hunt and the
completionist ledger, plus the **Astronomer title** and astronomy-themed rewards. It pairs
well with downtime activities like [gardening](/playing/gardening/) and
[fishing](/skills/fishing/) for players who enjoy the slower side of Britannia.

## See also

- [World & time](/playing/world-and-time/) — day/night and the in-game clock that gates what's visible
- [Gardening](/playing/gardening/) · [Fishing](/skills/fishing/) — other downtime pursuits
