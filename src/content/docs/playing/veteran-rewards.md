---
title: Veteran Rewards
description: Account-age rewards on this shard — earn a reward level for every 30 days your account has existed, then claim items like ethereal mounts, statues, special dyes, and house add-ons.
status: source-verified
sources:
  - "servuo: Scripts/Services/VeteranRewards/RewardSystem.cs (Enabled, level = accountAge / RewardInterval, reward lists)"
  - "servuo: Config/VetRewards.cfg (Enabled=True, RewardInterval=30 days, AgeCheckOnUse=False, StartingLevel=0)"
last_verified: 2026-06-17
generated: false
---

**Veteran rewards** are gifts your **account** earns simply for existing over time — ethereal
mounts, decorative statues, special dyes, house add-ons, and more. They're enabled here
(`VetRewards.cfg → Enabled=True`).

## How reward levels work

Your reward standing is based on **account age**, not playtime or skill:

- This shard grants **one reward level for every 30 days** your account has existed
  (`RewardInterval = 30 days`). (That's an accelerated pace — retail UO used a full year per
  level.)
- New accounts start at **level 0** (`StartingLevel=0`) and climb a level each interval.
- Your current level decides **how many** rewards you can claim and **which tiers** are
  available — higher levels unlock progressively better/rarer items.

## Claiming rewards

Open the **reward selection** menu (offered on login when you have unclaimed rewards, or via
the reward gump). Pick from the **list for each level** you've reached — each level offers its
own set of choices (`RewardList`), and you choose one item per available slot. Typical
veteran-reward items include:

- **Ethereal mounts** (a cosmetic mount that never needs feeding and ignores stable slots),
- **Reward statues** and decorative items for your house,
- **Special hair/cloth dyes** and dye tubs,
- **House add-ons** and functional décor.

On this shard **`AgeCheckOnUse=False`**, so once an item is claimed it can be used normally
(it isn't re-checked against account age each time you use it).

## Notes

- Rewards are **per account**, so they follow you across characters on that account.
- Because the interval here is **30 days**, a long-running account accrues a healthy stack of
  reward levels over a few months — check the reward menu periodically for newly unlocked
  tiers.

## See also

- [Housing](/playing/housing/) / [Decorating](/playing/decorating/) — where reward statues and add-ons go
- [Taming & pets](/playing/taming-and-pets/) — ethereal mounts vs real, fed mounts
- [Community Collections](/playing/community-collections/) — the other long-term reward track
