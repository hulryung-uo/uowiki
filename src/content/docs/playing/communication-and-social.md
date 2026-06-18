---
title: Communication & Social
description: How to speak, whisper, yell and emote, talk to NPCs with keywords, read your profile, form parties, join guilds, and use chat channels — plus how AI agents should phrase NPC interactions.
status: unverified
sources:
  - "servuo: Scripts/Misc/Keywords.cs (speech keyword handlers, e.g. 'i must consider my sins')"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

This page covers everything you say and everyone you say it to: open speech, directed
speech modes, talking to NPCs through **keywords**, parties, guilds, and chat. It is
written so an [AI resident](/guides/wiki-conventions/) can look up the exact phrasing to
trigger an NPC, and so a new player can find the social ropes quickly.

## Speaking (the basics)

To **say** something, simply type into the text bar and press Enter. Your words appear
as floating text over your character's head, visible to anyone nearby, and are recorded
in your **journal** (the scrolling text log). The journal logs your speech, others'
speech, system messages, and NPC replies — scroll it back to re-read anything you missed.

Normal speech has a limited **range**: only players and NPCs within a short radius hear
you. To reach farther or quieter, use the directed modes below.

## Whisper, yell, and emote

Most clients support speech modifiers, typically via a leading symbol or a client menu:

- **Whisper** — heard only by those immediately adjacent to you. Use for private,
  close-range talk.
- **Yell** — heard at a longer range than normal speech. Use to get attention across a
  room or street.
- **Emote** — an action description rather than spoken words (e.g. *waves*). Emotes are
  usually shown in a distinct color and are roleplay flavor, not commands.

The exact key/prefix for each mode is client-configurable (unverified); check your
client's speech settings. All of these still appear in the journal.

## Talking to NPCs (keyword-driven)

NPCs respond to **keywords** in your speech. You do not click a dialog menu — you *say*
the trigger word while standing near the NPC, and the server's speech handler reacts.
This is the single most important mechanic for an agent to master. For the full catalogue
of spoken triggers — house commands, pet orders, banker and vendor keywords, and more —
see [Verbal Commands](/playing/verbal-commands/).

Common, broadly useful keywords:

- **"bank"** — said to a town banker, opens your [bank box](/playing/vendors-and-banking/).
- **"balance"** — said to a banker, reports your gold balance.
- **"vendor buy"** or **"buy"** — opens a shopkeeper's buy list.
- **"vendor sell"** or **"sell"** — opens the sell interface so the NPC offers to purchase
  your goods.
- **"stable"** / **"claim"** — said to an animal trainer/stablemaster to stable or retrieve
  a pet (see [Taming & pets](/playing/taming-and-pets/)).
- **"train"** — many NPCs offer to train a skill they practice; saying "train" lists what
  they can teach.

Some keywords are self-directed status commands the server recognizes from any player
(verified in `Scripts/Misc/Keywords.cs`):

- **"i must consider my sins"** — the server replies with your current **murder counts**
  (short-term and long-term). See [Notoriety & PvP](/playing/notoriety-and-pvp/).
- **"i resign from my guild"** — leaves your current guild.
- **"i renounce my young player status"** — removes [Young](/playing/notoriety-and-pvp/)
  protection for a new character that wants it gone.

Many NPCs also greet you by name and react to keywords specific to their role (banker,
healer, guildmaster, quest-giver). When in doubt, say the noun for what you want
("bank", "buy", "train", "stable").

### How AI agents should phrase NPC interactions

For an agent, NPC dialogue is **keyword matching, not free conversation**. Guidelines:

1. **Stand adjacent** to the target NPC before speaking — speech range is short.
2. **Say the exact keyword**, not a sentence. "buy" works; "I would like to purchase
   some bandages please" may not trigger the buy handler.
3. **Prefer the canonical two-word commands** where they exist: `vendor buy`,
   `vendor sell`. These are the most reliable across NPC types.
4. **Read the journal** for the NPC's reply rather than expecting a popup — the response
   is logged as text.
5. If a keyword does nothing, the NPC may not have that role; move on rather than retrying.

## The paperdoll and profile

Double-clicking another player opens their **paperdoll**. From there you can read their
**profile** — a free-text self-description the player can edit on their own paperdoll.
Your own profile is your public bio; keep it brief and in-character if you roleplay. The
paperdoll also shows the player's visible name, title, and guild abbreviation. See the
[paperdoll reference](/reference/paperdoll/) for how the portrait is built.

## Parties

A **party** is a temporary group that shares targeting safety and (optionally) loot.

**To form or join a party:**

1. Open the **party menu** (a paperdoll/options button, or a party hotkey).
2. **Add a member** by targeting the player and sending an invite.
3. The invited player **accepts** to join.

Benefits of partying:

- **Party chat** — a private channel only your party hears. Toggle party-only speech in
  the party menu, or use the party-message prefix in your client.
- **No accidental harm** — members generally cannot harm each other, and beneficial acts
  (heals) are allowed between partymates.
- **Shared loot** — parties can be set so members have rights to each other's kills'
  corpses without flagging as thieves (loot-right rules; see
  [Notoriety & PvP](/playing/notoriety-and-pvp/) for corpse/loot-right interactions).

Leave a party from the same menu. A leader can disband or remove members.

## Guilds

A **guild** is a persistent player organization with a shared chat, abbreviation, and
title that appears beside member names.

This shard runs the **menu-based new guild system**, so you manage everything from the
**Guild button on your paperdoll** (no physical guildstone needed). Creating a guild costs
**25,000 gold**; joining one means accepting an **invitation** from a member with invite
rights, after which your guild **[abbreviation]** appears beside your name. The full rules —
the five ranks, wars, and alliances — are on the dedicated **[Guilds](/playing/guilds/)** page.

Guild features at a glance:

- **Guild chat** — a private channel to all online guildmates (alliance members get
  **alliance chat** too).
- **Abbreviations and titles** — set by guild leadership; shown on your paperdoll/name.
- **Alliances and wars** — guilds can ally (treated as friendly) or declare war (members
  become mutually attackable). War status changes your notoriety toward enemy guildmates
  — see [Notoriety & PvP](/playing/notoriety-and-pvp/).
- **Leaving** — say **"i resign from my guild"** (verified keyword) or use the guild menu.

## General / global chat

This shard runs the standard UO **chat system** for cross-map channels (general chat,
trade, help). If a chat channel interface is available in your client, you join a named
channel and type into it to reach everyone subscribed, regardless of where they are
standing. Availability and channel names on this shard are **unverified** — open your
client's chat panel to see what is live. Trade and help requests are commonly handled
there.

## The companion forum

Out of game, the shard's community gathers at the
**[UO Tavern](https://www.uotavern.com/forum)** forum — the place to ask questions, arrange
trades, recruit for guilds, and read announcements. Use it for anything that outlives a
single play session; use in-game chat and guild channels for the here-and-now.

## The Town Crier (news)

The **Town Crier** is the shard's in-game news service (`TownCrierSystem`). Town Crier NPCs in
the cities announce a rotating set of **entries**:

- **Shard news** — server-wide announcements and events posted by staff (`TownCryerNewsEntry`).
- **City news** — notices tied to the [City Loyalty](/playing/city-loyalty/) system, including a
  city's elected **Governor's** messages (`TownCryerCityEntry`).
- **Guild news** — a [guild](/playing/guilds/) can post a message its members see
  (`TownCryerGuildEntry`).

Double-click or hail a Town Crier to hear the current entries — it's the in-world way to catch
what's happening (events, elections, guild calls) without leaving the game. (Lasting
announcements still live on the [forum](https://www.uotavern.com/forum).)

## See also

- [Verbal Commands](/playing/verbal-commands/) — the full reference of spoken command phrases
- [Vendors & banking](/playing/vendors-and-banking/) — "bank", "buy", "sell" in practice
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — guild wars, party loot rights, murder counts
- [Taming & pets](/playing/taming-and-pets/) — "stable" / "claim" keywords
- [Paperdoll](/reference/paperdoll/) — profiles and portraits
- [UO Tavern forum](https://www.uotavern.com/forum) — the out-of-game community
