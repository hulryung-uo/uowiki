---
title: Fire Casino
description: Gamble gold on dice games at the casino — Chuckle's Luck, Hi-Middle-Low, and Dice Rider, played against a casino dealer.
status: source-verified
sources:
  - "servuo: Scripts/Services/FireCasino/DiceGames.cs (BaseDiceGame, ChucklesLuck, HiMiddleLow, DiceRider; betting/roll/payout)"
  - "servuo: Scripts/Services/FireCasino/{CasinoGumps,Mobiles,Generate}.cs (dealers, tents)"
last_verified: 2026-06-18
generated: false
---

The **Fire Casino** is a gambling spot where you wager **gold** on **dice games** run by a
**casino dealer** NPC (set up under the casino tents). Place a bet, the dice roll, and you win
or lose against the house — a pure game of chance for the gold in your pack.

## How a game works

Step up to a **casino dealer** and start a game (`BaseDiceGame`). Each game runs in stages:
**place your bet** → the **dice are rolled** → **payout** if you won. You're betting your own
gold, so only stake what you can afford to lose.

## The dice games

| Game | How you bet |
|---|---|
| **Chuckle's Luck** | Bet on a **specific number**; multiple dice are rolled and you're paid by how many of them **match** your number — more matches, bigger payout. |
| **Hi-Middle-Low** | Bet whether the roll's total lands **high, middle, or low**, and win if the dice fall in your chosen band. |
| **Dice Rider** | A streak/escalation dice game — ride your luck across rolls for a larger return (and a larger risk). |

## Notes

- It's **pure gambling** — there's no skill check; the dice are random, and the house edge means
  you'll lose over time. Treat it as entertainment / a gold sink, not income.
- A fun gold-sink and social spot rather than a progression system.

## See also

- [Vendors & banking](/playing/vendors-and-banking/) — where the gold you gamble comes from
- [Daily Rares](/playing/daily-rares/) · [Seasonal Events](/playing/seasonal-events/) — other side-content
