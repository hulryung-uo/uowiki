---
title: "Template: Bard Tamer"
description: PvM powerhouse — a tamer who debuffs with Discordance so the pet hits harder and gets hit less. Seven GM build, playstyle, pets, and money.
status: unverified
sources:
  - "community UO build knowledge (Stratics, UO Outlands wiki, UO forums) — adapted to this shard"
  - "servuo: Config/PlayerCaps.cfg (caps)"
last_verified: 2026-06-12
generated: false
---

:::note[Unverified community build]
This is a classic-era **community build (Stratics / UO Outlands wiki / UO forums) adapted to
this shard's caps**, not yet field-verified here. Skill values and pet behavior await
in-game confirmation; file discrepancies per [wiki conventions](/guides/wiki-conventions/).
:::

The bard tamer is the quiet end-boss of PvM. A plain [tamer](/templates/animal-tamer/) lets
the pet do the fighting; the bard tamer first walks up and *breaks* the monster — strips a
chunk of its resists and skills with [Discordance](/skills/discordance/) — so the pet then
fights a weaker, dumber version of it. You command, debuff, and heal; the pet does the
damage. It is the control-and-pet archetype in one body.

## The build (seven GM, ~700 total)

On **this shard** skills cap at **100.0 each and 700.0 total**
([`Config/PlayerCaps.cfg`](/shard/)), so the endgame is seven Grandmaster skills:

| Skill | At | Role |
|---|---|---|
| [Animal Taming](/skills/animal-taming/) | 100 | Tame and control the pet |
| [Animal Lore](/skills/animal-lore/) | 100 | Pet command/control + tame checks |
| [Veterinary](/skills/veterinary/) | 100 | Bandage-heal and resurrect the pet |
| [Musicianship](/skills/musicianship/) | 100 | Gates every bard skill; raises their success |
| [Discordance](/skills/discordance/) | 100 | The force multiplier — debuffs the target |
| [Magery](/skills/magery/) | 100 | Recall mobility, utility, backup healing |
| [Meditation](/skills/meditation/) | 100 | Mana to recall, heal, and cast |

Total: **700.0**, seven skills at GM. See [7x GM Templates](/templates/seven-gm/) for the
cap math.

**Flex slot.** [Peacemaking](/skills/peacemaking/) or [Provocation](/skills/provocation/)
can replace Meditation (or Magery) for boss control — area peace calms a dangerous spawn
while your pet finishes a target. You only have seven slots, so pick the one your hunting
grounds reward.

:::tip[Power scrolls go past 100 here]
On modern OSI these builds run **120s** via **power scrolls** — earned from
[champion spawns and treasure chests](/playing/treasure-hunting/). Power scrolls raise a
single skill's cap past 100.0 **on this shard too**, so a 110/120 Taming or Discordance is
reachable; treat the 100s above as the default endgame, not a ceiling.
:::

## What it does

[Discordance](/skills/discordance/) is the whole point. A successful disco (gated by
[Musicianship](/skills/musicianship/)) lowers the target's resistances and skills by a
percentage that scales with your skill — roughly a quarter of its stats at GM. That means:

- the monster's **resists drop**, so your pet's damage lands harder;
- the monster's **own skills drop**, so it hits your pet less often and for less.

Stack that with a pet that already out-tanks you, and a dragon becomes a chew toy. Add
[Veterinary](/skills/veterinary/) to keep the pet topped up and [Peacemaking](/skills/peacemaking/)
to shut down a second attacker, and you can clear content far above your "solo" weight.

[Musicianship](/skills/musicianship/) is mandatory plumbing: every bard attempt rolls
against your Music skill first. Below GM Music, disco fails too often to rely on; over 100
(via power scrolls) it adds extra success to your other bard skills.

## Stages and playstyle

This build layers **on top of** the [Animal Tamer](/templates/animal-tamer/) progression —
read that page for the taming ladder (hinds → bulls → drakes → dragons/nightmares) and pet
economics. The bard half slots in as follows:

- **Early (taming up):** train Taming/Lore/Vet exactly as the tamer template describes.
  Raise [Musicianship](/skills/musicianship/) alongside — it gains just by playing an
  instrument near a creature. Don't bother discording trash mobs; the debuff is wasted.
- **Mid (you have a real combat pet):** start opening fights with Discordance. The rhythm
  becomes **disco the target → send the pet → bandage the pet → re-disco when it wears
  off.** Discordance has a duration and falls off; re-apply on tough targets.
- **Endgame:** dragon/nightmare at your heel, GM disco in your pocket. You debuff bosses
  the pet would otherwise lose to, peace away adds, and out-earn every pure dexxer.

The feel is **orchestration, not reflexes** — you are managing a fight, not winning a
duel. See [combat (advanced)](/playing/combat-advanced/) and the
[taming-and-pets](/playing/taming-and-pets/) guide.

## Gear and pets

- **Instrument:** carry a few — lutes/harps wear out. Buy from bards/provisioners. A
  slayer instrument is not needed for disco; any working instrument plays.
- **Pet:** the same top-tier pets as a pure tamer — dragon (3 control slots), nightmare
  (2 slots, mage AI), white wyrm. Discordance lets a *cheaper* pet punch above its weight,
  so a disco tamer can field a strong second pet within the control-slot budget.
- **Reagents and bandages:** Magery reagents ([reagents](/items/reagents/)) for Recall and
  emergency heals; bandages for [Veterinary](/skills/veterinary/).
- **Stats:** favor INT (mana for music/magery) and STR (carry weight, survival); DEX last —
  pets do the swinging.

## Money

Top-tier PvM income: with a debuffed boss dying fast, you farm **Destard** dragons and
**Deceit** lich lords at the top of the [hunting ladder](/templates/#the-shared-hunting-ladder),
plus champion spawns for the [power scrolls](/playing/treasure-hunting/) that push your
skills past 100. Loot is FilthyRich-tier; the pet tanks what no armor could. Surplus gold
funds power scrolls and a second pet.

## Decision points

- **If disco keeps failing**, your [Musicianship](/skills/musicianship/) is too low — Music
  gates every attempt. Grind Music before relying on the debuff.
- **If the pet is dying on bosses**, you skipped the disco step or it wore off — re-apply
  Discordance and keep [Veterinary](/skills/veterinary/) bandages flowing.
- **If a second monster joins**, [Peacemaking](/skills/peacemaking/) it (area peace) rather
  than splitting the pet's damage.
- **If you want raw control over raw debuff**, consider the
  [Provocation / Tri-Bard](/templates/provocation-bard/) instead — it trades the pet for
  turning the whole room against itself.
- **Mistake:** discording trash. Save it for targets the pet would otherwise struggle with.
- **Mistake:** treating Music as optional. Without GM Music the build's force multiplier
  simply doesn't fire often enough.
