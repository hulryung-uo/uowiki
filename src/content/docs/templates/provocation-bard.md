---
title: "Template: Provocation Bard (Tri-Bard)"
description: The battlefield controller — turn monsters on each other with Provocation, debuff with Discordance, calm with Peacemaking, and loot the survivor. Seven GM build.
status: source-verified
sources:
  - "community UO build knowledge (Stratics, UO Outlands wiki, UO forums) — adapted to this shard"
  - "servuo: Config/PlayerCaps.cfg (700.0 total / 100.0 per-skill caps)"
  - "servuo: Server/Skills.cs (Musicianship, Provocation, Discordance, Peacemaking, weapon skills, Tactics, Anatomy all exist)"
  - "servuo: Scripts/Items/Equipment/Instruments/BaseInstrument.cs (GetBardRange = 8 + skill/15; CheckMusicianship gate = Music/100 roll)"
  - "servuo: Scripts/Skills/Provocation.cs (Musicianship gates the attempt; Music > 100 reduces difficulty)"
last_verified: 2026-06-22
generated: false
---

:::note[Unverified community build]
A classic-era **community bard build (Stratics / UO Outlands wiki / UO forums) adapted to
this shard's caps**, not yet field-verified here. Bard ranges and success rates await
in-game confirmation; file discrepancies per [wiki conventions](/guides/wiki-conventions/).
:::

The provocation bard wins without a pet and without out-damaging anything. You stand at the
edge of a fight and make the monsters kill *each other* — provoke the dragon onto its own
kin, discord whatever's left, peace the one that's still angry at you, and walk in to loot
the survivor. The "tri-bard" runs all three song skills plus a weapon to finish stragglers.
It is pure crowd control.

## The build (seven GM, ~700 total)

On **this shard** skills cap at **100.0 each and 700.0 total**
([`Config/PlayerCaps.cfg`](/shard/)). The four bard skills are the core; the last three
slots make you self-sufficient:

| Skill | At | Role |
|---|---|---|
| [Musicianship](/skills/musicianship/) | 100 | Gates and boosts every bard skill |
| [Provocation](/skills/provocation/) | 100 | Turn monsters on each other |
| [Discordance](/skills/discordance/) | 100 | Debuff a target's resists and skills |
| [Peacemaking](/skills/peacemaking/) | 100 | Stop a monster attacking (calm/area peace) |
| weapon skill ([Swordsmanship](/skills/swordsmanship/) / [Fencing](/skills/fencing/) / [Mace Fighting](/skills/mace-fighting/) — pick one) | 100 | Finish stragglers |
| [Tactics](/skills/tactics/) | 100 | Damage multiplier for the weapon |
| [Anatomy](/skills/anatomy/) | 100 | Damage + bandage healing |

Total: **700.0**. The weapon/Tactics/Anatomy block makes you a competent dexxer between
songs; swap that block for [Magery](/skills/magery/) + [Meditation](/skills/meditation/) +
[Eval Int](/skills/evaluating-intelligence/) if you'd rather finish with spells and have
Recall built in. Either way, the **four bard skills are non-negotiable.**

:::tip[Power scrolls go past 100 here]
On modern OSI this build runs **120s** via **power scrolls** from
[champion spawns and treasure chests](/playing/treasure-hunting/). Power scrolls raise a
skill's cap past 100.0 **on this shard too** — useful here because every point of bard skill
extends your range and success. Treat the 100s above as the default endgame, not a ceiling.
:::

## What it does

The three songs are a control toolkit; [Musicianship](/skills/musicianship/) gates all of
them (each attempt rolls against Music first), and Music over 100 adds extra success to the
other three.

- **[Provocation](/skills/provocation/)** — pick two monsters; on success they fight each
  other. This is the engine: a roomful of spawn becomes two sides killing themselves while
  you watch. In ServUO a failed provoke produces *no effect* ("Your music fails to incite
  enough anger") rather than redirecting the target onto you — but a poorly handled pull can
  still leave a monster attacking you, so success rate (and therefore Music) matters a lot
  ([`Scripts/Skills/Provocation.cs`](/shard/)).
- **[Discordance](/skills/discordance/)** — debuff a target's resists and skills so it loses
  the duel you started, or so your weapon finishes it faster.
- **[Peacemaking](/skills/peacemaking/)** — calm a monster so it stops attacking; area peace
  shuts down a whole pull. Your panic button when a provoke goes wrong.

**Range.** Bard skills reach about **8 tiles, +1 per 15 skill** — so at GM you work from a
comfortable distance and don't have to be in the scrum. That standoff range is the build's
safety margin.

## Stages and playstyle

- **Early:** [Musicianship](/skills/musicianship/) first — it gates everything and gains
  just by playing near creatures. Start [Peacemaking](/skills/peacemaking/) (safest to
  train) and your weapon block on trash mobs.
- **Mid:** introduce [Provocation](/skills/provocation/) on **paired** spawn — two of the
  same nearby monsters provoke most reliably. Learn the rhythm: **provoke A onto B → disco
  the winner → peace anything that targets you → finish with the weapon.**
- **Endgame:** stand at range in a dense dungeon, set the whole room against itself, and
  loot the survivor. You clear group content solo because you never take the hits — the
  monsters do.

The feel is a **conductor's, not a fighter's**: positioning, timing, and managing several
targets at once. See [bard](/professions/bard/) and
[combat (advanced)](/playing/combat-advanced/).

## Gear and pets

- **Instruments:** carry several — they wear out. A **slayer instrument** improves bard
  success against its monster type and is worth buying for tough spawn.
- **Weapon + armor:** for the dexxer finish — a fast weapon and a real suit, since you do
  occasionally get hit.
- **No pet** — this build's "army" is the enemy. That keeps your control-slot and upkeep
  costs near zero.
- **Stats:** STR/DEX for the weapon half (or INT if you take the Magery variant).

## Money

Excellent gold-per-hour at the top of the [hunting ladder](/templates/#the-shared-hunting-ladder):
dense spawn is where provocation shines, so you farm packed dungeon rooms and champion
spawns that would overwhelm a solo dexxer. You loot every corpse including the ones the
monsters killed for you, and champion spawns drop the
[power scrolls](/playing/treasure-hunting/) that extend your bard skills. Slayer instruments
and a good weapon are the only real upkeep.

## Decision points

- **If provokes keep failing (or turning on you)**, your [Musicianship](/skills/musicianship/)
  is too low — Music gates and boosts every song. Grind it first.
- **If two monsters won't provoke onto each other**, they may be too far apart or out of
  range — close to within ~8 tiles (+1 per 15 skill) or pick a closer pair.
- **If a monster ends up attacking you** (a failed provoke leaves it unchanged, but a bad
  pull can still bring one onto you), [Peacemaking](/skills/peacemaking/) it immediately —
  that's what the song is for.
- **If you want a pet army instead of an enemy army**, see the
  [Bard Tamer](/templates/bard-tamer/) — same Discordance core, very different feel.
- **Mistake:** skimping on Music to fit more "real" skills. Every bard attempt rolls against
  Music; under-investing there makes the whole build unreliable.
- **Mistake:** provoking into a pull you can't peace out of. Always keep Peacemaking ready as
  the escape valve.
