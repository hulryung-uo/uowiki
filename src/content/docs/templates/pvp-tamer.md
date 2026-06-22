---
title: "Template: PvP Tamer"
description: A foot-fighting mage tamer built to keep casting while meleed and not get dismounted — pet pressure plus spell burst. Seven GM build and the dismount problem.
status: unverified
sources:
  - "community UO build knowledge (Stratics, UO forums, UO Outlands wiki) — adapted to this shard"
  - "servuo: Config/PlayerCaps.cfg (700.0 total / 100.0 per-skill caps — verified)"
  - "servuo: Server/Skills.cs (Magery, EvalInt, Resisting Spells, Wrestling, Meditation, Animal Taming, Animal Lore all exist)"
  - "servuo: Server/Main.cs + Config/Expansion.cfg (EJ → Core.AOS true → pre-AOS wrestling stun/disarm disabled, per Fists.cs)"
last_verified: 2026-06-12
generated: false
---

:::note[Unverified community build]
A classic-era **community PvP build (Stratics / UO forums / UO Outlands wiki) adapted to
this shard's caps**. PvP is the most era-dependent content there is; the specifics here are
**not field-verified for this shard** and may not match our ruleset. Test on our
[PvP rules](/professions/pvp/) and file discrepancies per
[wiki conventions](/guides/wiki-conventions/).
:::

A PvP tamer fights two wars at once: the mage war (spell bursts, mana, [resist](/skills/resisting-spells/))
and the pet war (a fast, dangerous beast pressuring the enemy while you cast). The whole
build is shaped by one problem — **don't get dismounted, and keep casting while someone is
beating on you.** Your pet is the pressure; you are the burst and the control.

## The build (seven GM, ~700 total)

On **this shard** skills cap at **100.0 each and 700.0 total**
([`Config/PlayerCaps.cfg`](/shard/)). The PvP tamer is a **mage core + a taming half**:

| Skill | At | Role |
|---|---|---|
| [Magery](/skills/magery/) | 100 | Damage, heals, Recall — your offense and escape |
| [Evaluating Intelligence](/skills/evaluating-intelligence/) | 100 | Raises spell damage |
| [Resisting Spells](/skills/resisting-spells/) | 100 | Survive enemy spell bursts |
| [Wrestling](/skills/wrestling/) | 100 | Cast uninterrupted while being meleed (the pre-AOS stun/disarm punch is disabled on this EJ shard) |
| [Meditation](/skills/meditation/) | 100 | Mana regen between bursts |
| [Animal Taming](/skills/animal-taming/) | 100 | Control a combat pet |
| [Animal Lore](/skills/animal-lore/) | 100 | Pet control + tame checks |

Total: **700.0**. Note **[Veterinary](/skills/veterinary/) is dropped** here — there's no
slot for it. You heal the pet (and yourself) with Magery and bandages instead. Compare the
PvM-focused [Bard Tamer](/templates/bard-tamer/), which keeps Vet and drops the resist/wrestle
mage core.

:::tip[Power scrolls go past 100 here]
On modern OSI this build runs **120s** (Magery, Resist, and Taming especially) via **power
scrolls** from [champion spawns and treasure chests](/playing/treasure-hunting/). Power
scrolls raise a skill's cap past 100.0 **on this shard too** — but treat the 100s above as
the default; don't assume 120-based PvP numbers apply here.
:::

## What it does

- **[Wrestling](/skills/wrestling/)** is the keystone. With GM Wrestling you can keep
  casting while an enemy melees you — without it, every hit risks interrupting your spell.
  In pre-AOS rulesets it also gave wrestling specials (stun/disarm), but those are
  **disabled on this EJ shard** — the pre-AOS punch code in `Fists.cs` is gated behind
  `Core.AOS`, which is true on EJ. Here Wrestling is purely your uninterrupted-casting defense
  (plus the AOS Paralyzing Blow special, behavior unverified).
- **[Resisting Spells](/skills/resisting-spells/)** is survival. PvP is decided by spell
  bursts; GM Resist softens incoming magic damage and effects enough to live through them.
- **[Evaluating Intelligence](/skills/evaluating-intelligence/) + [Magery](/skills/magery/)**
  is your offense — explosion/ebolt combos, heals, cures, Recall to escape.
- **The pet** is constant pressure. A fast, mount-class combat beast forces the enemy to
  split attention; while they deal with the pet, you land bursts.

## The dismount problem

The defining weakness: a tamer on foot is fragile, but a tamer who gets **dismounted** is in
even worse shape — knocked off the mount, slowed, and caught. This is why many PvP tamers run
**[Bushido](/skills/bushido/) or [Chivalry](/skills/chivalry/) variants** (anti-dismount
tools, remounts, or counters) in eras that support them, trading a mage skill for mobility
insurance. Whether dismount mechanics and those counters apply on **our shard is unverified**
— check [PvP rules](/professions/pvp/) before committing skill points.

## Stages and playstyle

- **Build the mage core first** (Magery / Eval / Resist / Wrestling / Meditation) the way a
  pure [mage](/templates/mage/) does — it's playable solo PvM the whole way up.
- **Add the taming half** once the mage core is solid. You don't need every high-end pet —
  you need *one* fast, dangerous, mount-viable beast you can control and replace.
- **In a fight:** the pet engages and pressures; you cast from range, kite, and burst when
  the enemy is committed to the pet. [Wrestling](/skills/wrestling/) lets you keep casting
  if they close on you; [Resist](/skills/resisting-spells/) keeps you alive through their
  burst; Recall is the exit.

See [PvP](/professions/pvp/), [notoriety and PvP](/playing/notoriety-and-pvp/), and
[combat (advanced)](/playing/combat-advanced/).

## Gear and pets

- **Pet:** a fast combat beast you can ride/replace — durability and speed matter more than
  raw control-slot count in PvP. Keep it healed via Magery and bandages (no Vet slot).
- **Reagents and bandages:** carry deep — bursts burn reagents fast.
- **Stats:** INT-heavy (mana is everything for a mage), enough STR to survive a melee
  opener; DEX for bandage speed.
- **Mount/anti-dismount items:** era-dependent — verify what our shard allows on the
  [PvP page](/professions/pvp/).

## Money and where it comes from

PvP tamers fund themselves the same way as PvM tamers — farm the
[hunting ladder](/templates/#the-shared-hunting-ladder) and champion spawns between fights.
The real PvP "income" is **[power scrolls](/playing/treasure-hunting/)** and rare drops from
contested spawns; expect to lose reagents and the occasional pet, and budget accordingly.

## Decision points

- **If you keep getting dismounted and caught**, this is the build's core weakness — look at
  a [Bushido](/skills/bushido/)/[Chivalry](/skills/chivalry/) variant **if our shard
  supports the counters** ([PvP rules](/professions/pvp/)).
- **If your casts keep getting interrupted in melee**, your [Wrestling](/skills/wrestling/)
  is too low — it's the keystone, not a flex.
- **If you melt to spell bursts**, [Resist](/skills/resisting-spells/) isn't GM yet — finish
  it before fighting real opponents.
- **If you mostly PvM**, you want the [Bard Tamer](/templates/bard-tamer/) instead — Vet and
  Discordance beat Resist/Wrestle for hunting.
- **Mistake:** treating PvP numbers from OSI/other shards as gospel here. Our ruleset is
  unverified for this template — test, then report.
