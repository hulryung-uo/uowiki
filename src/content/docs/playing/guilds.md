---
title: Guilds
description: How guilds work on this shard — the menu-based new guild system, the 25,000 gold registration, the five ranks and their powers, invitations, guild/alliance chat, wars, and alliances.
status: source-verified
sources:
  - "servuo: Scripts/Misc/Guild.cs (NewGuildSystem=Core.SE, RegistrationFee, ranks/RankFlags, alliances, war, voting)"
  - "servuo: Server/Guild.cs (GuildType enum)"
  - "servuo: Scripts/Misc/Notoriety.cs (guild war/ally beneficial & harmful rules)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (name suffix [abbreviation], guild title display)"
last_verified: 2026-06-17
generated: false
---

A **guild** is a player-run organization — a name, a tag over your head, a private chat, and
the machinery for alliances and wars. This shard runs the **modern "new guild system"**
(`Guild.NewGuildSystem = Core.SE`, and our expansion is **EJ**, well past SE), which is
**menu-driven**: you don't need to place a physical guildstone the way the old system did.

## Joining or creating a guild

Open the **Guild menu** from your paperdoll (the Guild button). If you're not in a guild it
offers to **create** one; if you are, it opens your guild's roster and controls.

**To create a guild** you pay a **25,000 gold registration fee** (`RegistrationFee`) and choose:

- a **name** — up to **40 characters** (`NameLimit`), and
- an **abbreviation** — up to **4 characters** (`AbbrevLimit`), shown in brackets after your
  name, e.g. *Lyra Dawnblade **[DAWN]***.

**To join an existing guild**, a member with invite rights (Emissary or higher) sends you an
**invitation** through their guild menu; accept it and you join at the lowest rank
(**Ronin**), to be promoted once you've proven yourself.

## Ranks and what they can do

Every member holds one of **five ranks** (`RankDefinition.Ranks`), each granting a set of
permissions (`RankFlags`):

| Rank | Can do |
|---|---|
| **Ronin** | Probationary — newly accepted, **no privileges** (not even voting) until promoted. |
| **Member** | Vote in guild votes, access guild items, remove the lowest rank (Ronin). |
| **Emissary** | Member powers **+ invite players, remove players, promote/demote, set guild titles** — the officer/recruiter rank. |
| **Warlord** | Member powers **+ control war status** (declare and end wars). |
| **Leader** | **All powers**, including **alliance control**. Every guild has one Leader. |

Leadership can change by a guild **vote** — a candidate needs a **66% majority**
(`MajorityPercentage`) to take over. Members inactive for **30 days** (`InactiveTime`) stop
counting toward votes (so a dead guild can still be reformed by its active members).

## Identity: tag, title, and chat

- **Name tag** — your guild's **[abbreviation]** is appended to your character's name for
  everyone to see (`PlayerMobile` name suffix).
- **Guild title** — an Emissary can grant each member a custom **title** (e.g. "Quartermaster");
  you can toggle whether your title is shown.
- **Guild chat** — members share a private channel (guild messages), and members of an
  **alliance** share **alliance chat** on top of it.

## Wars

A **Warlord or Leader** can **declare war** on another guild from the guild menu; when a war
is active between two guilds (`IsWar`), their members become **enemies**:

- Enemy guild members can **attack each other freely, anywhere** — no criminal flag, no guard
  whacking for the fight itself (`Notoriety.cs` treats warring guilds as a harmful-allowed
  relationship). This is the sanctioned way for guilds to fight without going "red".
- A guild **at war is no longer "peaceful"** for notoriety purposes, which also limits
  beneficial acts toward non-allies.
- War ends when the war is rescinded / peace is agreed.

## Alliances

Guilds can band together into an **alliance** (`AllianceInfo`), controlled by guild **Leaders**:

- Allied guilds (members of the same alliance) treat each other as **allies** — beneficial
  acts (healing, buffs) are allowed between them and they **can't be warred** as enemies.
- Alliances share **alliance chat**, and have an **alliance leader** guild.
- Wars are fought at the alliance level too — declaring war reaches the alliance leaders.

## A note on Order vs Chaos

You may see the **Order / Chaos / Regular** guild *types* (`GuildType`) referenced in old UO
guides as a built-in PvP system (Order guilds vs Chaos guilds attacking on sight). **Under the
new guild system this is legacy** — enemy status is decided purely by **declared wars**
(`IsEnemy` returns `IsWar`), not by guild type. To fight another guild here, **declare war**;
to fight alongside one, **ally** with it.

## See also

- [Factions (Vice vs Virtue)](/playing/factions/) — opt-in guild-based open PvP and city sieges
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — criminal flags, guards, and open-PvP Felucca
- [Communication & social](/playing/communication-and-social/) — chat channels and grouping
- [Housing](/playing/housing/) — a guild often shares a house as a base
