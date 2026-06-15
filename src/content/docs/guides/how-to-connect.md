---
title: How to Connect
description: Step-by-step — download a UO client (ClassicUO), point it at this shard (uo.hulryung.com, port 2593), and create your account on first login.
status: source-verified
sources:
  - "anima: config.yaml / config.example.yaml (server uo.hulryung.com:2593, client 7.0.102.3)"
  - "servuo: Config/Accounts.cfg (AutoCreateAccounts=True, AccountsPerIp=999)"
  - "anima: README.md (shard is experimental — not monitored, not persistent)"
last_verified: 2026-06-15
generated: false
---

This page gets you from "I want to try it" to standing in Britannia. If you are brand new to
Ultima Online, read [Getting Started](/guides/getting-started/) first for what the game *is* —
this page is just the connection steps.

:::caution[This is an experimental shard]
This world runs on a [ServUO](https://www.servuo.com/) server kept up **for experimentation
and AI-resident research** — it is **not a monitored, persistent, or production game server**.
It can go down, reset, or wipe characters without notice. Come explore, test, and watch the
[AI residents](/) live — but don't pour weeks into a character expecting it to last. For
serious or offline play, you can run [your own local ServUO shard](https://www.servuo.com/).
:::

## What you need

1. **A UO client** — the free, open-source **[ClassicUO](https://www.classicuo.com/)**
   client is what this shard targets (the [AI residents](/) connect with the same protocol,
   client version **7.0.102.3**). ClassicUO runs on Windows, macOS, and Linux.
2. **UO game data files** — ClassicUO is only the engine; it needs the game's art, maps, and
   sound files. Download the **free official Ultima Online Classic Client** from
   [uo.com](https://uo.com/client-download/) and install it; that gives you the data files
   ClassicUO reads. (You do not need a paid UO account to get the free client files.)

No paid subscription is required to play here — see accounts below.

## Step 1 — Install the client

1. Install the **UO Classic Client** from [uo.com](https://uo.com/client-download/). Note the
   install folder (e.g. `C:\Program Files (x86)\Electronic Arts\Ultima Online Classic`).
2. Download and unzip **[ClassicUO](https://www.classicuo.com/)**.
3. Run ClassicUO once; in its launcher, set the **UO data path** to the folder where the
   Classic Client installed its files.

## Step 2 — Point ClassicUO at this shard

In the ClassicUO launcher, create a profile with:

| Setting | Value |
|---|---|
| **Server / IP** | `uo.hulryung.com` |
| **Port** | `2593` |
| **Client version** | `7.0.102.3` (or a nearby 7.0.x) |
| **Account / Password** | your choice — see Step 3 |

Leave encryption **off** (the default for ClassicUO on ServUO shards).

## Step 3 — Create your account (automatic)

This shard has **auto account creation** turned on
(`AutoCreateAccounts=True`, `AccountsPerIp=999`). You do **not** register on a website:

1. Type a **username** and **password** of your choosing into the ClassicUO login fields.
2. Connect. On your **first login**, the server creates that account automatically.
3. **Remember your username and password** — that *is* your account from now on. There is no
   email recovery; if you forget it, you simply make a new one.

⚠️ Pick a password you don't reuse elsewhere — this is a hobby shard, not a secured service.

## Step 4 — Make a character and log in

1. After logging in, create a character. New characters get the standard chargen budget —
   see [Character creation](/mechanics/character-creation/) (90 stat points, 4 skills,
   1,000 starting gold) and the [character templates](/templates/) for build ideas.
2. Choose a starting city. **Britain** (city index 3) is the central, well-connected default;
   see the [world overview](/world/) and [Getting around](/playing/movement-and-travel/).
3. You're in Britannia. Head to [How to Play](/playing/) for the basics of moving, fighting,
   and using skills.

## Troubleshooting

- **"Can't connect" / timeout** — the experimental shard may simply be down (see the caution
  above). Double-check `uo.hulryung.com` and port `2593`, and that your firewall allows
  ClassicUO.
- **Garbled art / missing tiles** — your ClassicUO **UO data path** isn't pointing at a
  complete Classic Client install (Step 1).
- **Version mismatch** — set the client version to `7.0.102.3` in the ClassicUO profile.
- **Login loops / encryption errors** — make sure encryption is **off** in the ClassicUO
  profile.

## See also

- [Getting Started](/guides/getting-started/) — what UO is, and how it differs from modern MMOs
- [Shard identity card](/shard/) — this world's exact caps, rates, and rules
- [How to Play](/playing/) — moving, combat, skills, and survival
- [Character creation](/mechanics/character-creation/) · [Character templates](/templates/)
- [The Tavern (forum)](https://www.uotavern.com/forum) — say hello and ask questions
