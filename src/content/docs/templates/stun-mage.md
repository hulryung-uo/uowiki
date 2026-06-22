---
title: "Template: Stun Mage (스턴 마사)"
description: The lockdown caster — a Magery mage built around the pre-AOS wrestling stun punch (Anatomy 80 + Wrestling 80). Note the stun punch is disabled on this EJ shard; documented as an era variant.
status: unverified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/Fists.cs (pre-AOS stun: Anatomy >= 80.0 AND Wrestling >= 80.0, 4s Freeze; disarm: ArmsLore >= 80.0 AND Wrestling >= 80.0 — BUT all gated behind `if (Core.AOS) return;`, so disabled on this shard)"
  - "servuo: Server/Main.cs:147 + Config/Expansion.cfg (EJ → Core.AOS == true → pre-AOS stun punch unreachable)"
  - "servuo: Config/PlayerCaps.cfg (700 total / 100 per-skill / 225 stat caps)"
  - "servuo: Server/Skills.cs (Magery, EvalInt, Resisting Spells, Wrestling, Anatomy, Meditation, Inscription all exist)"
  - "community/era UO build knowledge — adapted to this shard"
last_verified: 2026-06-22
generated: false
---

:::danger[The classic stun punch is OFF on this shard]
This page documents the **pre-AOS wrestling stun punch** (Anatomy 80 + Wrestling 80 → a
StunReady punch that freezes the target). That mechanic is real ServUO code, but it is gated
behind `if (Core.AOS) return;` in
[`Scripts/Items/Equipment/Weapons/Fists.cs`](/shard/). Our shard runs expansion **EJ**
(`Config/Expansion.cfg`), and `Core.AOS` is true for any expansion at or past AOS
([`Server/Main.cs`](/shard/)). **So the pre-AOS stun punch described below does NOT function
here.** On EJ the Fists weapon instead uses the AOS special-move system (a
**Paralyzing Blow** weapon special), gated by weapon skill and mana rather than the 80/80
threshold. Treat this build as a **historical/era variant**, not a working template on this
server, until the AOS-special version is documented and field-verified. The **700/225 caps**
are source-verified; the stun mechanic is not available. File discrepancies per
[wiki conventions](/guides/wiki-conventions/).
:::

In the Korean UO community a mage was called **마사** (*masa*, from 마법사 *mabeopsa*,
"magus/mage"). The **Stun Mage** (**스턴 마사**) is the 마사 variant built around the pre-AOS
**stun punch**: a wrestling move that briefly **freezes** the target, giving you a free window
to land a spell combo while they can't act.

This is one of three 마사 templates here, alongside the [Alchemy Mage](/templates/alchemy-mage/)
and the [Weapon/Halberd Mage](/templates/weapon-mage/). For the high-level PvP picture of all
three, see [PvP builds](/professions/pvp/); for the from-scratch caster storyline, see the
[Mage template](/templates/mage/).

## The idea: stun, then nuke (era mechanic — NOT active on this shard)

The classic stun mage is built on the **pre-AOS stun punch**. In
`servuo: Scripts/Items/Equipment/Weapons/Fists.cs` that move exists and **readying it requires**:

> **Anatomy ≥ 80.0 AND Wrestling ≥ 80.0** — a successful punch then `Freeze`s the target for 4
> seconds (the related disarm move requires **Arms Lore ≥ 80 AND Wrestling ≥ 80** instead).

**But that whole code path is disabled on this shard.** Both the stun/disarm request handlers and
the on-swing check are gated behind `Core.AOS` (`if (Core.AOS) return;` / `if (!Core.AOS && …)`).
Our server runs expansion **EJ**, which is past AOS, so `Core.AOS` is true and the StunReady punch
never triggers. On EJ the Fists weapon exposes the AOS **Paralyzing Blow** special move instead
(`PrimaryAbility = Disarm`, `SecondaryAbility = ParalyzingBlow` in `Fists.cs`), which is gated by
weapon skill and a mana cost (`Scripts/Abilities/WeaponAbility.cs`) — not by the Anatomy-80 /
Wrestling-80 threshold or a StunReady toggle.

In other words: the 80/80 stun requirement is correctly described above as *era* code, but you
**cannot ready a pre-AOS stun on this shard**. If you want a wrestling-based lockdown here, it
runs through the AOS Paralyzing Blow special, whose exact behavior on EJ is **not yet documented
or field-verified**. The rest of this page describes the historical playstyle for context.

## The 7 skills (≈700 total)

Seven Grandmaster (100.0) skills sum to **700.0** — this shard's total skill cap
(`Config/PlayerCaps.cfg`):

- **[Magery](/skills/magery/)** — your spell combo and mobility.
- **[Evaluating Intelligence](/skills/evaluating-intelligence/)** — raises spell damage.
- **[Resisting Spells](/skills/resisting-spells/)** — survive enemy magic.
- **[Wrestling](/skills/wrestling/)** — your unarmed defense (uninterrupted casting) and, in
  pre-AOS rulesets, the stun (≥80 needed). On EJ it also enables the AOS Paralyzing Blow special.
- **[Anatomy](/skills/anatomy/)** — boosts melee/heal; was the pre-AOS stun's second requirement
  (≥80), which **does not apply on this EJ shard** (see warning above).
- **[Meditation](/skills/meditation/)** — refills mana between combos.
- **Flex: [Inscription](/skills/inscription/)** (spell-damage bonus + scribing) or another
  utility skill.

:::tip[120s come from power scrolls]
The seven-GM (100.0) ceiling is the *base* cap. Individual skills go to **120** via
**Power Scrolls**, which on this shard drop from **champion spawns and treasure** — see
[treasure hunting](/playing/treasure-hunting/).
:::

**Suggested stats (225 cap):** ~75 STR / ~35 DEX / ~115 INT (the 225 stat total is the shard
cap, `Config/PlayerCaps.cfg`) — STR and a workable punch for the stun, INT leading for mana.

## How it plays

- **(Era playstyle) Ready the stun** — in a pre-AOS ruleset you'd ready the stun (Anatomy 80 +
  Wrestling 80, per `Fists.cs`), close to wrestling range, and land the punch to freeze the
  target. **This does not work on our EJ shard** (see the warning above); it's described for
  context.
- **What works here instead:** a wrestling-based lockdown on EJ goes through the AOS
  **Paralyzing Blow** weapon special (gated by skill + mana), whose timing/effect on this shard
  is unverified. Otherwise play it as a tank/war mage: GM Wrestling for uninterrupted casting.
- **Dump in any window:** when the target is locked or pressured, chain your Eval-boosted spell
  combo (the classic Explosion → Energy Bolt style burst) so it lands before they recover.
- **Stay un-interrupted** with GM Wrestling so an enemy melee can't lock *you* out of casting.
- **The stun mechanic itself is unavailable on this shard, and PvP timings are unverified** —
  test against live targets and report. This is a player-combat build; read
  [advanced combat](/playing/combat-advanced/) and [PvP builds](/professions/pvp/) first.

## Money

In PvM it plays like the [Mage template](/templates/mage/) — Recall in, burst, Recall out. Its
intended edge was **PvP**: locking a player for a guaranteed combo window. Note that the pre-AOS
lockdown punch this relied on is disabled on our EJ shard (above), so on this server it functions
as a tank/war mage with an AOS Paralyzing Blow option rather than the classic guaranteed-stun
build.

## See also

- [Mage template](/templates/mage/) — the underlying caster storyline.
- [PvP builds](/professions/pvp/) — the tank/nox/stun mage overview.
- [Wrestling](/skills/wrestling/), [Anatomy](/skills/anatomy/),
  [advanced combat](/playing/combat-advanced/).
- Sibling builds: [Alchemy Mage](/templates/alchemy-mage/), [Weapon/Halberd Mage](/templates/weapon-mage/).
