---
title: "Template: Stun Mage (스턴 마사)"
description: The lockdown caster — a Magery mage who readies a wrestling stun punch (Anatomy 80 + Wrestling 80) to freeze the target, then lands a spell combo.
status: unverified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/Fists.cs (stun requires Anatomy >= 80.0 AND Wrestling >= 80.0; disarm requires Arms Lore >= 80 + Wrestling >= 80)"
  - "servuo: Config/PlayerCaps.cfg (700 total / 100 per-skill / 225 stat caps)"
  - "community/era UO build knowledge — adapted to this shard"
last_verified: 2026-06-12
generated: false
---

:::note[Unverified — community/era build, adapted]
A classic Korean-community mage variant adapted to this shard. The **80/80 stun requirement**
and the **700/225 caps** are source-verified against ServUO; the build shape and PvP combo
tactics are era wisdom. **Exact PvP timings are unverified** — field verification is pending.
File discrepancies per [wiki conventions](/guides/wiki-conventions/).
:::

In the Korean UO community a mage was called **마사** (*masa*, from 마법사 *mabeopsa*,
"magus/mage"). The **Stun Mage** (**스턴 마사**) is the 마사 variant built around the pre-AOS
**stun punch**: a wrestling move that briefly **freezes** the target, giving you a free window
to land a spell combo while they can't act.

This is one of three 마사 templates here, alongside the [Alchemy Mage](/templates/alchemy-mage/)
and the [Weapon/Halberd Mage](/templates/weapon-mage/). For the high-level PvP picture of all
three, see [PvP builds](/professions/pvp/); for the from-scratch caster storyline, see the
[Mage template](/templates/mage/).

## The idea: stun, then nuke (source-verified requirement)

This shard implements the pre-AOS stun punch. Per
`servuo: Scripts/Items/Equipment/Weapons/Fists.cs`, **readying a stun requires**:

> **Anatomy ≥ 80.0 AND Wrestling ≥ 80.0**

(The related disarm move requires **Arms Lore ≥ 80 AND Wrestling ≥ 80** instead.) With those two
skills, you ready a stun and your next successful wrestling hit briefly locks the target down —
the stun mage uses that window to land an Eval-boosted spell combo before the enemy can react or
heal. Lock, then dump.

Because the requirement is **80**, not 100, you don't strictly need Anatomy and Wrestling at GM
to *use* the stun — but GM Wrestling is also your unarmed defense and improves your hit/stun
chance, so this template carries both at 100.

## The 7 skills (≈700 total)

Seven Grandmaster (100.0) skills sum to **700.0** — this shard's total skill cap
(`Config/PlayerCaps.cfg`):

- **[Magery](/skills/magery/)** — your spell combo and mobility.
- **[Evaluating Intelligence](/skills/evaluating-intelligence/)** — raises spell damage.
- **[Resisting Spells](/skills/resisting-spells/)** — survive enemy magic.
- **[Wrestling](/skills/wrestling/)** — the stun (≥80 required) and your unarmed defense.
- **[Anatomy](/skills/anatomy/)** — the stun (≥80 required); also boosts melee/heal.
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

- **Ready the stun** (needs Anatomy 80 + Wrestling 80, per `Fists.cs`), close to wrestling
  range, and land the punch to lock the target.
- **Dump in the window:** while the target is stunned, chain your Eval-boosted spell combo
  (the classic Explosion → Energy Bolt style burst) so it lands before they recover.
- **Stay un-interrupted** with GM Wrestling so an enemy melee can't lock *you* out of casting.
- **Exact stun duration and the PvP timing of the stun→combo window are unverified on this
  shard** — test against live targets and report. This is a player-combat build; read
  [advanced combat](/playing/combat-advanced/) and [PvP builds](/professions/pvp/) first.

## Money

In PvM it plays like the [Mage template](/templates/mage/) — Recall in, burst, Recall out — with
the stun as an extra control tool against melee-fast spawn. Its real edge is **PvP**: locking a
player for a guaranteed combo window is what the build is for.

## See also

- [Mage template](/templates/mage/) — the underlying caster storyline.
- [PvP builds](/professions/pvp/) — the tank/nox/stun mage overview.
- [Wrestling](/skills/wrestling/), [Anatomy](/skills/anatomy/),
  [advanced combat](/playing/combat-advanced/).
- Sibling builds: [Alchemy Mage](/templates/alchemy-mage/), [Weapon/Halberd Mage](/templates/weapon-mage/).
