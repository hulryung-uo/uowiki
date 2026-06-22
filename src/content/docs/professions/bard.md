---
title: Bard
description: Turn monsters on each other with music — provoke, peace, and discord. The four bard skills, how each works, the loop, and how bards earn.
status: source-verified
sources:
  - "servuo: Scripts/Skills/Provocation.cs"
  - "servuo: Scripts/Skills/Discordance.cs"
  - "servuo: Scripts/Items/Equipment/Instruments/BaseInstrument.cs"
  - "wiki cross-references; general UO play"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The bard fights with music instead of weapons: play the right instrument and you can make
two monsters slaughter each other, lull a room to sleep, or cripple a boss's stats. A pure
bard barely touches a sword — the loot drops because the monsters did the work. It's a
control profession that shines in groups and pairs beautifully with a mage or tamer who
cleans up what the music leaves alive.

## Core skills

- [Provocation](/skills/provocation/) — **turn monsters on each other.** Target two enemies and they fight to the death; you loot the winner. The bard's signature trick.
- [Peacemaking](/skills/peacemaking/) — **calm.** Pacifies a target or an area so monsters stop attacking, buying time to reposition or escape.
- [Discordance](/skills/discordance/) — **debuff.** Lowers a target's skills (including its weapon skill, so it hits less) and **all five resistances** — up to 28% at GM, scaling with your Discordance (`Scripts/Skills/Discordance.cs`) — making everything else easier to kill.
- [Musicianship](/skills/musicianship/) — **the enabler.** Every bard ability first calls `BaseInstrument.CheckMusicianship`; fail that play and the song has no effect (`Scripts/Skills/Provocation.cs`, `Scripts/Skills/Discordance.cs`). Train it alongside the other three.

## The build

There is **no dedicated bard template** in this wiki yet. Build it around the four skills
above (Provocation + Peacemaking + Discordance + Musicianship is four grandmaster slots) and
spend the remaining three on a partner kit — commonly [Magery](/skills/magery/),
[Meditation](/skills/meditation/), and [Resisting Spells](/skills/resisting-spells/) for a
bard-mage, or the [tamer](/professions/tamer/) skills for a bard-tamer. See
[7x GM Templates](/templates/seven-gm/) for fitting all seven under the 700-point cap.

## How to play it

Read [Combat Advanced](/playing/combat-advanced/) for the timing of musical abilities within
a fight. The core loop: open with [Discordance](/skills/discordance/) to weaken a tough
target, then [Provoke](/skills/provocation/) two enemies into killing each other while you
stand back; if things go wrong, [Peacemake](/skills/peacemaking/) to break aggro and reset.
Your songs reach further as you train: bard range is `8 + skill/15` tiles (`BaseInstrument.GetBardRange`), so a grandmaster works from about 14 tiles away — and for provoke, the **two targets must also be within that range of each other**. A bard is strongest where monsters spawn in groups — more bodies means more pairs to provoke.
Pair with a [mage](/professions/mage/) or [tamer](/professions/tamer/) to finish the
survivor.

## Gear & tools

- An **instrument** — lute, harp, drum, or tambourine. Quality and slayer type both matter: an **exceptional** instrument and a matching **slayer** instrument each lower the difficulty of the target (`GetDifficultyFor` in `Scripts/Items/Equipment/Instruments/BaseInstrument.cs`), so a slayer instrument that matches the monster type makes provoke/discord land more reliably. See [instruments](/items/catalog/instruments/). Carry a spare; each use consumes a charge (`ConsumeUse`) and they wear out.
- Light [armor](/items/armor/) — you don't tank, so favor mobility.
- A spellbook and [reagents](/items/reagents/) if you've taken the mage partner skills.

## Making a living

The bard's income is **provoke-and-loot**: provoke powerful [bestiary](/bestiary/) monsters
into killing each other, then loot the gold, gems, and gear off both corpses — often clearing
high-value targets at little risk and no ammunition cost. Discordance also makes you a
valuable group member for boss fights. Sell loot via
[Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Mage](/professions/mage/) and [Tamer](/professions/tamer/) — the usual bard partners
- [7x GM Templates](/templates/seven-gm/) — fitting seven grandmaster skills under the cap
- [Provocation](/skills/provocation/) · [Peacemaking](/skills/peacemaking/) · [Discordance](/skills/discordance/) · [Musicianship](/skills/musicianship/)
- [Combat Advanced](/playing/combat-advanced/)
