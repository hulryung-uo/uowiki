---
title: "Template: Weapon/Halberd Mage (할바드 마사)"
description: The war-mage — a Magery caster who wields a heavy two-handed weapon (a halberd) instead of relying on Wrestling, opening with a weapon special then casting.
status: source-verified
sources:
  - "servuo: Config/PlayerCaps.cfg (700.0 total / 100.0 per-skill / 225 stat caps)"
  - "servuo: Server/Skills.cs (Magery, EvalInt, Resisting Spells, Swordsmanship, Tactics, Anatomy, Meditation all exist)"
  - "servuo: Scripts/Items/Equipment/Weapons/Halberd.cs + BasePoleArm.cs (halberd = BasePoleArm, DefSkill = Swords, two-handed; specials WhirlwindAttack/ConcussionBlow)"
  - "servuo: Scripts/Misc/RegenRates.cs (Meditation bonus zeroed by meditation-blocking armor; weapons do not count toward the armor offset)"
  - "community/era UO build knowledge — adapted to this shard"
last_verified: 2026-06-22
generated: false
---

:::note[Unverified — community/era build, adapted]
A classic Korean-community mage variant adapted to this shard. The **700/225 caps** are
source-verified against ServUO; the build shape and "open with a weapon special then cast"
tactics are era wisdom and **field verification is pending**. File discrepancies per
[wiki conventions](/guides/wiki-conventions/).
:::

In the Korean UO community a mage was called **마사** (*masa*, from 마법사 *mabeopsa*,
"magus/mage"). The **Weapon/Halberd Mage** (**할바드 마사**) is the 마사 variant that, instead
of leaning on Wrestling for its off-hand, wields a **heavy two-handed weapon** — classically a
**halberd** — and opens the fight with a weapon hit or special before falling back to spells.
It is the hybrid "war-mage."

This is one of three 마사 templates here, alongside the [Alchemy Mage](/templates/alchemy-mage/)
and the [Stun Mage](/templates/stun-mage/). For the high-level PvP picture, see
[PvP builds](/professions/pvp/); for the from-scratch caster storyline, see the
[Mage template](/templates/mage/).

## The idea: weapon opener, then cast

A pure tank mage punches with Wrestling so it never has to draw a weapon. The halberd mage
makes the opposite trade: it carries a real **two-handed weapon** for a heavy opening hit (and a
weapon special), then casts. The big up-front weapon damage softens the target before your
Eval-boosted spell combo, and the weapon keeps applying pressure / interrupting the enemy's
casting between your spells.

The weapon of choice is a **halberd** or similar heavy [two-handed weapon](/items/weapons/),
which uses [Swordsmanship](/skills/swordsmanship/). The cost is in your hands: a two-handed
weapon **blocks your off-hand**, so you can't carry a shield with it — your defense is your
spells and your hit points, not a parry.

## The 7 skills (≈700 total)

Seven Grandmaster (100.0) skills sum to **700.0** — this shard's total skill cap
(`Config/PlayerCaps.cfg`):

- **[Magery](/skills/magery/)** — spells and mobility.
- **[Evaluating Intelligence](/skills/evaluating-intelligence/)** — raises spell damage.
- **[Resisting Spells](/skills/resisting-spells/)** — survive enemy magic.
- **[Swordsmanship](/skills/swordsmanship/)** — your halberd weapon skill.
- **[Tactics](/skills/tactics/)** — weapon-damage multiplier (with [Anatomy](/skills/anatomy/)).
- **[Anatomy](/skills/anatomy/)** — more weapon damage (and feeds healing).
- **[Meditation](/skills/meditation/)** — refills mana between casts.

(With seven slots full, Tactics+Anatomy already do a lot of weapon-damage work; some players
swap one of them for [Healing](/skills/healing/) or a flex depending on how melee-heavy they
want to play.)

:::tip[120s come from power scrolls]
The seven-GM (100.0) ceiling is the *base* cap. Individual skills go to **120** via
**Power Scrolls**, which on this shard drop from **champion spawns and treasure** — see
[treasure hunting](/playing/treasure-hunting/).
:::

**Suggested stats (225 cap):** ~75 STR / ~35 DEX / ~115 INT (the 225 stat total is the shard
cap, `Config/PlayerCaps.cfg`) — enough STR and DEX to swing a halberd and survive, with INT
leading for the mana pool.

## How it plays

- **Open with the weapon.** Land a heavy halberd hit (and a weapon special if available), then
  start your spell combo while the target is already hurt. See
  [advanced combat](/playing/combat-advanced/) for weapon specials.
- **Alternate weapon and spell** — the swing keeps pressure and interrupt potential on the
  enemy while your spells reload; the spells finish what the weapon started.
- **No shield.** A halberd is two-handed, so you have no free hand for a shield — lean on
  Resist, hit points, and Greater Heal for defense.
- **Re-arming costs a beat.** Unlike a wrestling tank mage, drawing/sheathing the weapon takes
  time; decide before the fight whether you're opening with steel or with a spell.

## Money

Farms the [Mage template](/templates/mage/) ladder with extra melee punch for tougher,
slower targets — the halberd shortens fights against high-HP monsters that a pure mage would
have to kite for a long time. Recall logistics and elemental/undead farming are the same.

## See also

- [Mage template](/templates/mage/) — the underlying caster storyline.
- [PvP builds](/professions/pvp/) — the 마사 variants in player combat.
- [Swordsmanship](/skills/swordsmanship/), [weapons](/items/weapons/),
  [advanced combat](/playing/combat-advanced/).
- Sibling builds: [Alchemy Mage](/templates/alchemy-mage/), [Stun Mage](/templates/stun-mage/).
