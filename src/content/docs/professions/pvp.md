---
title: PvP Builds
description: The classic player-vs-player character archetypes — tank mage, nox mage, dexxer, stealth archer, and more — and the skills that separate a fighter from a farmer.
status: unverified
sources:
  - "servuo: Config/PlayerCaps.cfg (700 skill cap, 225 stat cap)"
  - "servuo: Scripts/Spells/Base/SpellHelper.cs (PvP SDI cap)"
  - "wiki cross-references; classic UO PvP practice"
last_verified: 2026-06-22
generated: false
---

The PvM [Professions](/professions/) hub answers "I want to *be* a tamer/smith." This page
answers a different question: **"what do people build to fight other players?"** These are
the combat archetypes — the templates tuned for killing other characters rather than monsters.

## PvP on this shard

The **rules** of player combat live in [Notoriety & PvP](/playing/notoriety-and-pvp/):
criminal and murderer flagging, guard zones, and Felucca-style open PvP. That page tells you
*when and where* you can attack someone and what happens to your notoriety when you do.

**This** page is about the *characters* people build to win those fights. Whether open PvP is
available, and exactly how flagging works, is governed by the shard rules — read that page
first, then come back here to pick a build.

:::note[What's verified here]
The hard numbers on this page — the 700 skill / 225 stat caps and the PvP Spell Damage
Increase cap — are confirmed against ServUO source (see frontmatter). The **archetype
recommendations and combos** are PvP practice and opinion, not code claims; they don't
contradict the source, but they aren't promoted to source-verified. The Stun Mage section in
particular is flagged unverified below.
:::

## What makes a PvP build different

A PvM farmer optimizes raw, sustained damage against predictable monsters. A PvP build
optimizes **speed and survivability** against a thinking opponent who is trying to kill *you*
in a two-second combo. The priorities shift:

- **Instant burst** — winning is usually about dumping a lethal combo faster than the enemy can react, not grinding HP down.
- **Spell interruption** — taking damage disrupts a caster mid-spell, so both landing hits to interrupt *them* and casting *through* being hit matters.
- **Escape and mobility** — Recall, Teleport, and stamina to run; a fight you can leave is a fight you can't lose.
- **Curing and healing through pressure** — surviving poison ticks and incoming damage with bandages, Cure, and Greater Heal.
- **Not dying to the combo** — enough HP, resists, and reactive healing to live through the opener.

Because of this, [Resisting Spells](/skills/resisting-spells/) (to shrug off enemy magic),
[Wrestling](/skills/wrestling/) (so a meleed mage can still cast and isn't auto-interrupted),
and fast [bandage healing](/playing/healing/) matter far more in PvP than in PvM.

## The classic build archetypes

These are templates within the **700-point skill cap** (see [7x GM Templates](/templates/seven-gm/));
the cap is what forces the hard choices below. That budget is real and shard-configured:
`Config/PlayerCaps.cfg` sets `TotalSkillCap=7000` (700.0 skill) and a `TotalStatCap=225`
(125 max in any one stat) — so seven grandmaster skills exactly fill the sheet, and every
build below is a choice about which seven.

### Tank Mage

**Skills:** Magery, Eval Int, Resisting Spells, Wrestling, Anatomy, Healing, Meditation.

The all-rounder and the **benchmark PvP template**. It casts offensive magic, **bandage-heals**
through damage (Anatomy + Healing), and **wrestles** so melee can't lock its casting. The jack
of all trades: hard to kill, never out of options, no glaring weakness — which is exactly why
it's the template everything else is measured against. See [Mage](/professions/mage/).

### Nox (Poison) Mage

**Skills:** Magery, Poisoning, Eval Int, Resisting Spells, Wrestling, Meditation, + a little Healing.

A tank mage that trades some sustain for [Poisoning](/skills/poisoning/). It opens with a
**poison + explosion/energy-bolt** combo: the poison ticks pressure the enemy's healing while
the burst lands, and a poisoned opponent must spend actions curing instead of fighting back.
Strong offense; thinner on its own healing than a pure tank mage.

### Stun Mage

**Skills:** Magery, Wrestling, Resisting Spells (era-dependent extras).

Uses **stun and lock-down** tricks — classic Wrestling stun, or disarm + paralyze combos — to
freeze the target while a kill combo lands. Devastating when it works because the victim can't
react.

:::caution[Mechanics unverified for our shard]
Wrestling stun and the para-combo lock are **heavily era-dependent** (pre-AOS Wrestling stun
behaves very differently from later expansions). The exact mechanics on our EJ shard are
**unverified** — treat this archetype as a concept, not a confirmed recipe, until checked
against the ServUO source and in-game testing.
:::

### Pure / 5x Mage (scribe mage)

**Skills:** Magery, Eval Int, Resisting Spells, Meditation, Wrestling + Inscription.

A **glass cannon**. [Inscription](/professions/scribe/) (scribe) boosts spell damage and
supplies the scrolls the build burns through, trading the dexxer's bandage healing for maximum
magical burst. It hits harder than a tank mage but has less margin for error — win the opener or
struggle to outlast a tankier foe. See [Scribe](/professions/scribe/).

### Dexxer (melee PvP)

**Skills:** a weapon skill (Swordsmanship / Fencing / Mace), Tactics, Anatomy, Healing,
Resisting Spells, Parrying — often plus a splash of Magery for Recall.

The melee fighter: **chase and burst**. It closes distance, lands disarm / concussion-blow /
paralyzing-blow special moves to lock the target, and bursts it down with weapon damage and
bandages. [Parrying](/skills/parrying/) and [Resisting Spells](/skills/resisting-spells/) keep
it alive against mages; the little Magery is mostly for Recall mobility. See
[Warrior](/professions/warrior/) and [Combat Advanced](/playing/combat-advanced/) for the
special moves this build lives on.

### Stealth Archer / Ninja

**Skills:** Archery (or Ninjitsu), Hiding, Stealth, Tactics, Anatomy, Healing or Chivalry.

Opens from concealment with a **heavy alpha strike**, then repositions and re-hides to reset.
The gameplay is ambush-and-vanish: deal a huge opening hit, break line of sight, and disappear
before the target can retaliate. See [Ninja](/professions/ninja/), [Archer](/professions/archer/),
and [Hiding & Stealth](/playing/hiding-and-stealth/).

### Bard / Disco-mage

**Skills:** Discordance + Provocation (and Musicianship), layered on a mage core.

A mage that adds **[Discordance](/skills/discordance/)** to debuff the target's stats and skills
before the kill, and Provocation for control. The song-based debuff softens the enemy so the
magic finishes faster. See [Bard](/professions/bard/).

### Sampire-style melee / Necro-dexxer

**Skills:** a weapon skill with vampiric leech + Bushido and/or Necromancy for survivability.

In group fights, **weapon life-leech** (Vampiric Embrace / Hit Life Leech) plus Bushido or
Necromancy keeps a melee fighter standing where a plain dexxer would fall. Less a duelist than a
durable bruiser for the scrum. See [Sampire](/professions/sampire/).

### Thief (PvP)

**Skills:** Stealing, Hiding, Stealth (often a little combat or Magery to escape).

A specialist: uses **[Stealing](/skills/stealing/)** to snatch items — or disarm a weapon — out
of the chaos of a fight, then [Hiding & Stealth](/playing/hiding-and-stealth/) to vanish with the
loot. Thrives in crowded PvP where no one notices the hand in their pack. See
[Thief](/professions/thief/).

## Skills that define PvP

- [Resisting Spells](/skills/resisting-spells/) — reduces the effect of enemy magic; near-mandatory.
- [Wrestling](/skills/wrestling/) — lets a meleed caster keep casting (and powers stun builds).
- [Healing](/skills/healing/) + [Anatomy](/skills/anatomy/) — bandage healing, your reactive lifeline.
- [Magery](/skills/magery/) — burst, Cure, Greater Heal, and Recall mobility.
- [Poisoning](/skills/poisoning/) — pressures the enemy's healing.
- [Tactics](/skills/tactics/) — the weapon-damage multiplier for any dexxer.
- [Parrying](/skills/parrying/) — block hits and survive focus fire.
- [Meditation](/skills/meditation/) — regenerate mana between exchanges.

:::note[Spell Damage Increase is capped in PvP]
Item Spell Damage Increase (SDI) does **not** scale without limit against other players.
On our EJ shard the PvP SDI cap is **20%** from gear, rising to **30%** if you've focused a
spell school (`PvPSpellDamageCap` in `Scripts/Spells/Base/SpellHelper.cs`; the older "15%"
figure applies only to pre-Stygian-Abyss eras). PvM has no such cap — which is part of why a
high-SDI burst mage that flattens monsters does proportionally less in a duel.
:::

## Templates note

Every build above is squeezed into the **700-point cap** — see
[7x GM Templates](/templates/seven-gm/) for why that budget forces the trade-offs (drop Anatomy
for Inscription, drop Healing for Poisoning, and so on). For the PvM counterparts of these
builds, compare the [Professions](/professions/) hub.

## See also

- [Notoriety & PvP](/playing/notoriety-and-pvp/) — the flagging and guard-zone rules.
- [Combat Basics](/playing/combat-basics/) — the fundamentals all of this sits on.
- [Combat Advanced](/playing/combat-advanced/) — special moves and weapon mechanics.
- [Healing](/playing/healing/) — bandages, Cure, and reactive survival.
- [7x GM Templates](/templates/seven-gm/) — building within the point cap.
