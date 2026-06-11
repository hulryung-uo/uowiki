---
title: Character Creation
description: Server-enforced rules for new characters — stat and skill point budgets, starting equipment per skill, starting gold, and where new characters actually appear.
status: source-verified
sources:
  - "servuo: Scripts/Misc/CharacterCreation.cs"
  - "servuo: Scripts/Accounting/AccountHandler.cs (StartingCitiesSA list)"
  - "servuo: Scripts/Accounting/Account.cs (Young status, YoungDuration)"
  - "servuo: Scripts/Items/Containers/BagOfReagents.cs"
  - "servuo: Config/PlayerCaps.cfg, Config/Siege.cfg, Config/TestCenter.cfg, Config/Expansion.cfg"
last_verified: 2026-06-11
generated: false
---

Everything below is what the server actually enforces in `Scripts/Misc/CharacterCreation.cs` —
whatever the client gump shows, these are the numbers that stick.

## Starting stats

| Rule | Value |
|---|---|
| Total stat points | **90** (clients 7.0.16+; older clients get 80) |
| Per-stat minimum | 10 |
| Per-stat maximum | 60 |
| Invalid submission | Reset to 10/10/10 |

The server rescales whatever the client sends to exactly the point budget (`FixStats`), then
rejects anything outside 10–60 per stat or off-total. Picking a **profession template**
overrides your stats entirely (Warrior 45/35/10, Magician 25/20/45, Blacksmith 60/15/15,
Necromancer 25/20/45, Paladin 45/20/25, Samurai/Ninja 40/30/20). All eight templates are
available since the shard runs EJ. See [Stat Gain](/mechanics/stat-gain/) for growth after
creation (stat cap 125 / total 225 per `Config/PlayerCaps.cfg`).

## Starting skills

| Rule | Value |
|---|---|
| Skills chosen | up to 4 (advanced/custom template) |
| Per-skill maximum | 50.0 |
| Total skill points | exactly **120** (or 100 on old 3-skill clients) |
| Duplicates | rejected |
| Blocked at creation | Stealth (unless Ninja profession), Remove Trap, Spellweaving — silently zeroed |

Profession templates instead grant four fixed skills at 30 each (e.g. Warrior: Swords,
Tactics, Anatomy, Healing). Per-skill cap is 100.0 and the total cap is 700.0 — see
[Skill Gain](/mechanics/skill-gain/).

## Everyone starts with

- Backpack containing: a red book, **1,000 gold**, a candle, and a dagger
- Shirt, pants/skirt, and shoes (random style, your chosen hues)
- 100% Hunger; item insurance set to auto-renew
- **Bank box: empty** (Test Center mode is off), except Young players get a **New Player Ticket**

**Young status**: accounts are Young by default; every new character is flagged Young until the
account logs **40 hours of game time** (or you say "I renounce my young player status"). Young
players are protected from most monster aggression and player attacks.

## Skill → starting equipment (highlights)

Items are granted per chosen skill (custom template only — professions get fixed kits instead).
Human versions shown; elves and gargoyles get racial equivalents.

| Skill | You receive |
|---|---|
| [Swordsmanship](/skills/swordsmanship/) | Katana |
| [Tactics](/skills/tactics/) | Katana (a second one if you also took Swords) |
| [Magery](/skills/magery/) | Spellbook with **12 spells** (Heal, Magic Arrow, Night Sight, Cure, Harm, Strength, Fireball, Poison, Teleport, Fire Field, Greater Heal, Lightning), bag of **50 of each of the 8 reagents**, 3 random scrolls, wizard's hat, blue robe |
| [Mining](/skills/mining/) | Pickaxe |
| [Lumberjacking](/skills/lumberjacking/) | Hatchet |
| Bowcraft/Fletching | 14 boards, 5 feathers, 5 shafts ([crafting guide](/crafting/bowfletching/)) |
| [Blacksmithy](/skills/blacksmithy/) | Tongs, **two** pickaxes, 50 iron ingots, half apron |
| [Animal Taming](/skills/animal-taming/) | **Nothing** — taming has no case in `AddSkillItems` (Animal Lore gives a shepherd's crook + robe) |
| Tailoring | Bolt of cloth, sewing kit ([crafting guide](/crafting/tailoring/)) |
| [Healing](/skills/healing/) | **50 bandages**, scissors |
| Anatomy | 3 bandages, robe |
| Archery | Bow, 25 arrows |
| Parrying | Wooden shield |
| Wrestling | Leather gloves |
| Tinkering | Tinker's tools, 50 iron ingots, axle, gears, springs, clock frame |
| Carpentry | Saw, 10 boards, half apron |
| Alchemy | Mortar and pestle, 4 bottles, pink robe |
| Musicianship / Provocation / Peacemaking / Discordance | Random instrument (each) |
| Lockpicking / Stealing / Snooping | 20 lockpicks (each) |

Necromancy grants a necromancer spellbook (Animate Dead, Evil Omen, Pain Spike, Summon
Familiar, Wraith Form) plus a bag of 50 of each necro reagent; Chivalry grants a full Book of
Chivalry.

## Starting location

This is **not Siege** (`Config/Siege.cfg: IsSiege=false`) and the expansion is EJ, so the
client is offered the full `StartingCitiesSA` list — you genuinely start wherever you pick:

| City | Inn | Map |
|---|---|---|
| New Haven | New Haven Bank | Trammel |
| [Britain](/world/britain/) | The Wayfarer's Inn | Trammel |
| [Yew](/world/yew/) | The Empath Abbey | Trammel |
| [Minoc](/world/minoc/) | The Barnacle | Trammel |
| [Moonglow](/world/moonglow/) | The Scholars Inn | Trammel |
| [Trinsic](/world/trinsic/) | The Traveler's Inn | Trammel |
| [Jhelom](/world/jhelom/) | The Mercenary Inn | Trammel |
| [Skara Brae](/world/skara-brae/) | The Falconer's Inn | Trammel |
| [Vesper](/world/vesper/) | The Ironwood Inn | Trammel |
| Royal City (Ter Mur) | Royal City Inn | Ter Mur |

The character is moved exactly to the chosen city's inn (`MoveToWorld(city.Location, map)`).
There is no forced New Haven funnel and no New Haven quest intro.

## Differences from OSI expectations

- **Free choice of starting city.** On modern OSI, new players are pushed into New Haven;
  here all ten cities (including Royal City for gargoyles) work as listed.
- **1,000 starting gold** — generous next to the classic ~100gp.
- **Skill picks are 4 × up to 50 (total 120)** with full starter gear per skill — the old
  "advanced" template, always available.
- Stealth, Remove Trap, and Spellweaving cannot be taken at creation even if the client
  offers them; the server zeroes them.

New here? Start with the [Getting Started guide](/guides/getting-started/) and the
[shard rules](/shard/server-rules/).
