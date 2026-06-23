---
title: Death & Resurrection
description: What happens at 0 HP — becoming a ghost, your corpse and loot, getting resurrected, item insurance, and retrieving your body.
status: source-verified
sources:
  - "servuo: Server/Mobile.cs (OnDeath sets ghost Body; MutateSpeech garbles dead speech to 'o'/'O'; Resurrect restores Hits=10/Stam=full/Mana=0)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (MutateSpeech bypass at Spirit Speak >= 100 for speaker or listener; GetInsuranceCost base 600g; CheckInsuranceOnDeath deduction)"
  - "servuo: Scripts/Items/Corpses/Corpse.cs (7-minute corpse decay, then bones)"
  - "servuo: Scripts/Mobiles/NPCs/WanderingHealer.cs + BaseHealer.cs (NPC healer refuses criminals/murderers; resurrects on approach), Scripts/Items/Functional/Ankhs.cs (shrine/ankh resurrect), Scripts/Items/Addons/AnkhOfSacrifice.cs (1h cooldown)"
  - "servuo: Scripts/Items/Resource/Bandage.cs (bandage res thresholds Healing/Anatomy >= 80; pet res 0.1/skill loss), Scripts/Spells/Eighth/Resurrection.cs (8th circle), Scripts/Spells/Chivalry/NobleSacrifice.cs"
  - "servuo: Scripts/Gumps/ResurrectGump.cs (10% fame loss; Compassion virtue HP bonus; no AOS stat/skill loss)"
last_verified: 2026-06-23
generated: false
---

This page explains dying and coming back. For preventing death see
[Healing](/playing/healing/); for getting res'd specifically by bandage see
[Healing → Resurrecting with a bandage](/playing/healing/#resurrecting-with-a-bandage);
for murderer/notoriety effects see [Notoriety & PvP](/playing/notoriety-and-pvp/).

## What happens at 0 HP

When your hit points reach **0**, you **die** and become a **ghost**:

- Your character turns into a **grey, translucent ghost** and can move freely.
- As a ghost you **cannot be easily heard** by the living — the server replaces every
  letter of your speech with random "**o**/**O**" characters (`Mobile.MutateSpeech`). A
  living listener hears your words normally only if **they** have **Spirit Speak ≥ 100**
  (or you, the dead speaker, have Spirit Speak ≥ 100). Otherwise it's garbled "Oooo".
- You **cannot attack, cast, or interact** with most of the world while dead. You wander
  until you are resurrected.

## Your corpse and loot

When you die, a **corpse** is left at the spot you fell:

- It holds your **loot** — most items you were carrying and wearing drop to the corpse,
  unless they are **blessed**, **newbied**, or **insured** (see below).
- Other players (and, in dungeons, monsters/looters) can take from your corpse, depending
  on the area's ruleset and your notoriety. Recover your body quickly.
- Your corpse **decays after 7 minutes** (`Corpse.cs`), then leaves a bone pile that
  decays after another 7, so don't dawdle.

## What stays with you vs what drops

- **Blessed items** — never drop on death; they stay equipped/in your pack. Starting gear
  and many quest items are blessed.
- **Newbied items** — like blessed for newcomers; remain on you.
- **Insured items** — items you paid to **insure** stay with you on death; a per-item fee is
  deducted on each death (paid from your bank if **auto-renew** is on). This is the modern
  way to protect valuable gear.
- **Everything else** — drops to your corpse and can be looted.

Insurance cost is per item: the base fee is **600 gold** for a normal item, scaled by an
item's imbue weight or buy price (clamped roughly 10–800), and **doubled** for "prized"
(cursed) items (`PlayerMobile.GetInsuranceCost`). A region can apply its own multiplier.
Manage and insure items via [Vendors & banking](/playing/vendors-and-banking/) and
[Items & inventory](/playing/items-and-inventory/); region multipliers live on
[the shard config](/shard/).

## Ghost movement

As a ghost you can **walk and run normally** to reach a place where you can be
resurrected. You pass freely and are not attacked. You generally cannot use doors,
mounts, or most items while dead. Head for the nearest healer, shrine, or living friend.

## Getting resurrected

Several methods bring a ghost back to life:

- **Wandering Healer NPCs** — roving healers in the wilderness will resurrect you on
  approach (double-click them). They are the classic "walk your ghost to a healer" option.
- **Town Healer NPCs** — healers stationed in towns and at healer buildings resurrect you.
  See [the world / towns](/world/). **Note:** town/NPC healers will **not** resurrect
  flagged **murderers** (red characters) — see
  [Notoriety & PvP](/playing/notoriety-and-pvp/).
- **Shrines** — moongate/virtue **shrines** can resurrect a ghost who reaches them; see
  [moongates & shrines](/world/moongates-and-shrines/).
- **A player's Resurrection spell** — a [Magery](/skills/magery/) caster (8th-circle
  Resurrection, `Resurrection.cs`) can res you on the spot.
- **A player's bandage** — a healer with **Healing ≥ 80 and Anatomy ≥ 80** can resurrect
  you with a bandage (verified in `Bandage.cs`; full procedure in
  [Healing](/playing/healing/#resurrecting-with-a-bandage)).
- **Chivalry — Noble Sacrifice** — a [Chivalry](/skills/chivalry/) paladin can resurrect
  nearby allies with Noble Sacrifice (`NobleSacrifice.cs`).

**To accept a resurrection:** you are shown a **resurrect gump** — click to accept and you
return to life at that location.

## Resurrection penalty

On this AOS/EJ shard the penalty for dying is **minimal**: when you accept the res you come
back at just **10 hit points**, **0 mana**, and **full stamina** (`Mobile.Resurrect`), and
you lose **10% of your Fame** (`ResurrectGump.cs`). There is **no permanent stat or skill
loss** for a player resurrection — that old-era penalty only runs on the pre-AOS ruleset,
which this shard does not use. (Being resurrected by a high-Compassion healer instead starts
you at 20–80% HP.) Recover the rest by healing and meditating once you're up.

(Resurrecting a **dead pet** is the one case that costs a small permanent skill loss — about
**0.1 per skill** on the pet, per `Bandage.cs`.)

## Retrieving your corpse and loot

After you are resurrected:

1. **Return to your corpse** (you respawned wherever you got res'd, which may be far away —
   you may need to travel back; see [Movement & travel](/playing/movement-and-travel/)).
2. **Loot your own corpse** — open it and drag your items back. Anything **insured/blessed**
   never left you, so you only need to reclaim the rest.
3. Re-equip your weapon and armor, re-bandage/heal up, and you're ready again.

If you cannot reach the body in time (it decayed or was looted), your dropped items are
gone — which is exactly why insurance and blessed gear matter for valuables.

## See also

- [Healing](/playing/healing/) — including bandage and spell resurrection
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — murderers can't be res'd by town healers
- [The world & towns](/world/), [moongates & shrines](/world/moongates-and-shrines/)
- [Items & inventory](/playing/items-and-inventory/), [Vendors & banking](/playing/vendors-and-banking/)
- [Spirit Speak](/skills/spirit-speak/) — hearing and aiding ghosts
- [The shard rules](/shard/) — insurance and penalty specifics
