---
title: Notoriety & PvP
description: The notoriety system — innocent (blue), criminal (grey), murderer (red) — how you flag each, guard zones, stealing/snooping, murder-count decay, Young protection, and how an agent reasons about safety.
status: source-verified
sources:
  - "servuo: Scripts/Misc/Notoriety.cs (Mobile_AllowHarmful/Beneficial, felucca HarmfulRestrictions, Young branches, Stealing.ClassicMode/PermaFlags)"
  - "servuo: Server/Notoriety.cs (Innocent=1/Criminal=4/Murderer=6 constants and hues 0x059/0x3B2/0x022)"
  - "servuo: Server/Mobile.cs (Murderer => m_Kills >= 5, line 11846)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (CheckKillDecay: 8h short-term, 40h long-term; OnKillsChange/OnSkillChange Young removal; CheckPoisonImmunity)"
  - "servuo: Scripts/Regions/GuardedRegion.cs (IsGuardCandidate, AllowReds = Core.AOS, CallGuards)"
  - "servuo: Scripts/Misc/Keywords.cs (i must consider my sins / i resign from my guild / i renounce my young player status)"
  - "servuo: Config/General.cfg (RestrictRedsToFel=True)"
  - "wiki: /shard/server-rules/"
last_verified: 2026-06-23
generated: false
---

**Notoriety** is the system that decides who you can attack, who can attack you, and
whether the town guards consider you a criminal. It is the rulebook for PvP and the
single most important thing to understand before you raise a hand against anyone. The
mechanics below are read directly from the server's notoriety code
(`Scripts/Misc/Notoriety.cs`, `Server/Notoriety.cs`, `Server/Mobile.cs`).

## The three notoriety states

Every player and creature is shown to you in one of several highlight colors. The three
that matter for player behavior:

| State | Highlight | Meaning |
|-------|-----------|---------|
| **Innocent** | **Blue** (hue `0x59`) | Law-abiding. Attacking one is a crime. |
| **Criminal** | **Grey** (hue `0x3B2`) | Has done something illegal recently; freely attackable, guards hostile. |
| **Murderer** | **Red** (hue `0x22`) | A repeat killer (5+ long-term kills); attackable on sight by anyone. On this AOS-era ruleset guards do **not** kill a red merely for being red — see [Guard zones](#guard-zones-towns-are-safe). |

(Constants and hues verified in `Server/Notoriety.cs`: `Innocent=1`, `Criminal=4`,
`Murderer=6`.) Other states exist for guilds and factions — **Ally** (green) and **Enemy**
(orange) appear when guild war/alliance or faction status applies — but blue/grey/red are
the everyday cases.

## How you become criminal (grey)

You flag **criminal** by committing an illegal act. The most common triggers:

- **Attacking an innocent** (blue) player or innocent NPC who has not aggressed you. The
  notoriety handler refuses to even let you harm a blue target in most cases, and acting
  against one makes you the aggressor/criminal (`Mobile_AllowHarmful` in `Notoriety.cs`).
- **Stealing** from another player, or **snooping** (peeking into) their pack — see
  [Stealing and snooping](#stealing-and-snooping-flag-you-criminal) below.
- Other criminal acts (looting a corpse you have no right to, etc.).

Criminal status is **temporary** — it wears off after a short time if you commit no
further crimes. While grey you are freely attackable by anyone and the town guards will
side against you.

## How you become a murderer (red)

Killing **innocent** players accrues **murder counts** ("kills"). The threshold is
verified in `Server/Mobile.cs`:

> `public virtual bool Murderer { get { return m_Kills >= 5; } }`

- You turn **red** once your **long-term murder count reaches 5**.
- Each murder of an innocent adds to both a **short-term** and a **long-term** count.
- Killing greys/reds/monsters does **not** give murder counts — only killing innocents
  does.

A red is attackable by anyone without penalty. Note that on this shard's
**AOS-era ruleset** the town guards do **not** automatically attack a red on sight (the
guarded-region rule `AllowReds` returns true once `Core.AOS` is set — verified in
`Scripts/Regions/GuardedRegion.cs`, `IsGuardCandidate`). Guards act against a red only if
that red also commits a **criminal act** in town. See [Guard zones](#guard-zones-towns-are-safe).

## Murder-count decay

Murder counts **decay over time** as you avoid further killing. From
`PlayerMobile.CheckKillDecay()` (verified):

- **Short-term** murders drop by **1 every 8 hours** of game time
  (`m_ShortTermElapse += TimeSpan.FromHours(8)`).
- **Long-term** murders (the count that keeps you red) drop by **1 every 40 hours** of game
  time (`m_LongTermElapse += TimeSpan.FromHours(40)`).

Because the **long-term** count is what sets the red flag, working off your red status is
slow: from 5 long-term kills you need to fall below 5, i.e. at least one 40-hour decay tick
with no new murders. Check your counts anytime by saying **"i must consider my sins"** — the
server reports both numbers (verified in `Scripts/Misc/Keywords.cs`).

## Guard zones (towns are safe)

Towns are **guard zones**. The mechanics below are verified in
`Scripts/Regions/GuardedRegion.cs`. Inside a guard zone:

- A **criminal or aggressor** who acts up becomes a **guard candidate**
  (`CheckGuardCandidate`). Guards arrive and kill the offender **near-instantly** — either
  when someone says **"guards"** (`CallGuards`, keyword `0x0007`), or automatically because a
  nearby townsperson "calls" them on the spot (the `fakeCall` path in `CheckGuardCandidate`).
  A summoned guard one-shots its target.
- A **red who has committed no crime is NOT a guard candidate** on this ruleset. Because the
  region rule `AllowReds` returns true once `Core.AOS` is set (true on EJ), guards ignore reds
  for simply being red — `IsGuardCandidate` flags only `m.Criminal`, aggressive monsters, and
  (only when `!AllowReds`) murderers. A red is whacked by guards **only if it also acts
  criminally** in town.
- Therefore, **you are largely safe from open aggression while standing in a guarded town** —
  a player who attacks you there flags criminal and draws the guards. (Do not assume a red
  standing peacefully in town will be struck down automatically; on this shard it will not.)

This makes towns your refuge: bank, repair, restock, and regroup there. Step outside the
guard zone (wilderness, dungeons) and that protection ends. See
[World & time](/playing/world-and-time/) for how regions and guard zones are laid out.

## Consensual vs. open PvP on this shard

This shard uses **Felucca-style ruleset separation**:

- **Felucca** is the open-PvP facet. Harmful actions between players are allowed there —
  the notoriety code explicitly notes "in felucca, anything goes" once you are flagged
  (`Mobile_AllowHarmful`: maps without `HarmfulRestrictions` permit harm).
- **Other facets** (Trammel, Ilshenar, Malas, Tokuno) apply **harmful restrictions**, so
  open PvP between non-consenting players is blocked there; PvP is effectively
  **consensual** (guild war, duels, factions/arena).
- **Murderers (reds) are restricted to Felucca** — `RestrictRedsToFel=True` in
  `Config/General.cfg` (see [shard card](/shard/)). You will not meet a red outside
  Felucca.

Guild **war** and **alliance** override the defaults between the guilds involved: warring
guildmates become mutually **Enemy** (attackable) even in otherwise-protected facets, and
allies become **Ally** (protected) — logic in `Notoriety.cs` (`GetGuildFor`,
`IsAlly`/`IsEnemy`).

## Stealing and snooping flag you criminal

- **Snooping** — opening and peeking inside another player's backpack without permission is
  a criminal act and flags you grey (and can set "perma-grey" flags toward the victim under
  classic stealing rules; `Stealing.ClassicMode` / `PermaFlags` in `Notoriety.cs`).
- **Stealing** — successfully or unsuccessfully lifting an item from another player flags
  you criminal and makes you attackable by the victim (and their party/guild) without the
  victim becoming a criminal themselves.

If you intend to play a thief, expect grey status and the loss of guard protection while
flagged. Snooping/stealing mechanics and skill use are covered under the Stealing/Snooping
skills.

## Young (new-player) protection

New characters carry **Young** status, a protective new-player flag (verified in
`PlayerMobile.cs`). While Young:

- You are **immune to poison** (`CheckPoisonImmunity` returns true for Young).
- You receive new-player safety on death and reduced item loss (Young death handling moves
  items to your pack rather than leaving a lootable corpse in many cases).
- Older players cannot perform harmful actions on you, and you cannot perform beneficial
  actions on non-Young players (`Mobile_AllowBeneficial`/`Mobile_AllowHarmful` Young
  branches).

You **lose Young status** when (verified):

- You **kill** someone (any rise in your kill count removes Young — `OnKillsChange` calls
  `RemoveYoungStatus`), or
- You voluntarily renounce it by saying **"i renounce my young player status"** (verified
  keyword `0x0035` in `Scripts/Misc/Keywords.cs`) — this opens a confirmation gump
  (`RenounceYoungGump`) you must accept.

There is also a "respectable skill level" removal path in the code (`OnSkillChange` →
`RemoveYoungStatus` at `SkillsTotal >= 4500`), but on this shard it **never fires**: it is
gated by `!Core.AOS && Skills[skill].Base >= 80.0`, and `Core.AOS` is **true** on EJ
(verified in `PlayerMobile.OnSkillChange`). So on this ruleset Young is lost only by killing
or by renouncing — not by gaining skill.

New players should keep Young protection while learning, and not throw it away by picking a
fight.

## How an agent should reason about safety

For an [AI resident](/guides/wiki-conventions/), the safe defaults are simple and follow
straight from the rules above:

1. **Stay blue.** Never attack an innocent (blue) player or innocent NPC. The engine will
   usually block it, and crossing that line costs you guard protection or turns you red.
2. **Only fight what is grey, red, or a monster.** Those are lawful targets.
3. **Bank before risky travel.** Deposit gold and valuables in a guarded town before
   leaving for the wilderness or Felucca — a death there can cost everything on your corpse
   (see [Death & resurrection](/playing/death-and-resurrection/)).
4. **Prefer non-Felucca facets** when you do not want open PvP; reds cannot follow you
   there.
5. **Retreat to a guard zone** when threatened by a player killer — guards neutralize
   criminals and reds in town.
6. **Track your own counts.** If you have killed players, say "i must consider my sins" and
   avoid further kills so your long-term count can decay below 5.

## See also

- [Guilds](/playing/guilds/) — wars and alliances, the sanctioned way for guilds to fight
- [Factions (Vice vs Virtue)](/playing/factions/) — opt-in guild-based open PvP and city sieges
- [Champion Spawns](/playing/champion-spawns/) — Felucca power-scroll hotspots and PvP flashpoints
- [World & time](/playing/world-and-time/) — guard zones, facets, reds-to-Felucca
- [Death & resurrection](/playing/death-and-resurrection/) — what you lose on a corpse
- [Communication & social](/playing/communication-and-social/) — guild war/ally, "i must consider my sins"
- [Vendors & banking](/playing/vendors-and-banking/) — banking before risky travel
- [Shard identity card](/shard/) and [server rules](/shard/server-rules/)
