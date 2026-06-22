---
title: "Template: Lumberjack Warrior (Axer)"
description: The axe dexxer — a melee warrior who takes Lumberjacking to swing axes for +30% damage at Grandmaster, presented as a seven-GM build.
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (lumberBonus = GetBonus(Lumberjacking, 0.200, 100.0, 10.00); GetBonus = value*scalar + offset(at threshold), /100 → +30% at GM; zeroed unless WeaponType.Axe)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseAxe.cs (DefType = Axe; DefSkill = Swords; harvest system = Lumberjacking.System)"
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000/700.0, SkillCap=1000/100.0, TotalStatCap=225)"
  - "servuo: Server/Skills.cs (Swordsmanship, Tactics, Anatomy, Healing, Lumberjacking, Resisting Spells, Parry, Chivalry, Magery all present in SkillInfo)"
  - "community/era UO build knowledge — adapted to this shard"
status: source-verified
last_verified: 2026-06-22
generated: false
---

:::note[Unverified — community/era build, adapted]
This is a classic-era community build ("lumberjack dexxer" / "axer") adapted to this shard.
The **+30% axe bonus** and the **700/225 caps** are source-verified against ServUO; the build
shape and money advice are era wisdom. **Field verification is pending** — as you play it, file
discrepancies per [wiki conventions](/guides/wiki-conventions/).
:::

The lumberjack warrior is a [Warrior](/templates/warrior/) with one twist that makes it hit
harder than a plain sword dexxer: it takes **[Lumberjacking](/skills/lumberjacking/)** and
fights with an **axe**. On this shard an axe-class weapon gets a flat damage bonus scaled by
your Lumberjacking skill (up to +30% at GM), so a Grandmaster lumberjack swings for noticeably
more than the same character holding a katana.

## Why the axe hits harder (source-verified)

Per `servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs`, total weapon damage adds a
**lumber bonus**:

```
lumberBonus = GetBonus(Lumberjacking, 0.200, 100.0, 10.00)
```

where `GetBonus(value, scalar, threshold, offset)` returns `(value * scalar + offset) / 100`
once `value` hits the threshold. Plugging in 100.0 Lumberjacking gives
`(100 × 0.200 + 10.00) / 100 = 0.30`, i.e. **+30% damage at GM** (the 20% scalar plus a 10%
bonus that only kicks in at 100.0). The damage line is zeroed unless your weapon is an axe
(`BaseWeapon.cs`: `if (Type != WeaponType.Axe) lumberBonus = 0.0`), and `BaseAxe.cs` sets
`DefType = Axe`, so the bonus applies only when you wield an axe. Axes also train and use
[Swordsmanship](/skills/swordsmanship/) (`BaseAxe.cs`: `DefSkill = Swords`), so the lumberjack
warrior is a **swordsman who specialises in axes** — a [War Axe](/items/catalog/weapons/),
Large Battle Axe, or Two-Handed Axe rather than a katana.

The +30% stacks on top of your STR, Anatomy, and Tactics bonuses (which use the same `GetBonus`
helper), so it is a real, free damage tier the plain dexxer never gets. The price is one of your
seven skill slots spent on Lumberjacking instead of, say, Magery.

## The 7 skills (≈700 total)

Seven Grandmaster (100.0) skills sum to **700.0** — this shard's total skill cap
(`Config/PlayerCaps.cfg`). One sensible split:

- **[Swordsmanship](/skills/swordsmanship/)** — your weapon skill; axes train and use it.
- **[Tactics](/skills/tactics/)** — core damage multiplier.
- **[Anatomy](/skills/anatomy/)** — more damage, and feeds bandage healing.
- **[Healing](/skills/healing/)** — bandages; at 80/80 Healing+Anatomy, self-resurrection.
- **[Lumberjacking](/skills/lumberjacking/)** — the +30% axe bonus at GM (and free wood; see below).
- **[Resisting Spells](/skills/resisting-spells/)** — blunts enemy magic.
- **Flex: [Parrying](/skills/parrying/)** (a shield share of blocks — but note a two-handed axe
  leaves no hand for a shield, so pair Parry with a one-handed [War Axe](/items/catalog/weapons/)),
  or **[Chivalry](/skills/chivalry/)/[Magery](/skills/magery/)** for utility (heals, cure,
  travel).

:::tip[120s come from power scrolls]
The seven-GM (100.0) ceiling above is the *base* cap. Individual skills can be pushed to **120**
with **Power Scrolls**, which on this shard drop from **champion spawns and treasure** — see
[treasure hunting](/playing/treasure-hunting/). A 120 Swordsmanship / 120 Tactics axer is the
end-state of this template.
:::

**Suggested stats (225 cap):** ~100 STR / ~90 DEX / ~35 INT. STR is hit points and damage, DEX
drives swing and bandage speed; keep INT low (just enough for a utility flex). The 225 stat
total is the shard cap (`Config/PlayerCaps.cfg`).

## How it plays

You play it like the [Warrior](/templates/warrior/) — close, swing, bandage, loot — but with an
axe in hand and the damage edge that comes with it. The win condition is the same attrition
game: out-heal the incoming damage and grind the target down, only faster.

- **Open with a two-handed axe** for the biggest hits when you can afford to give up a shield;
  drop to a one-handed [War Axe](/items/catalog/weapons/) + shield when you want Parry's defense.
- **Keep Lumberjacking at GM** — every point below 100 costs you damage, so don't let it sit at
  90 "for now."
- **Self-sufficient woodcutter.** Lumberjacking isn't just a damage stat: it lets you
  **harvest wood** from trees, so the same character that out-damages a sword dexxer can also
  cut logs to sell or fuel a fletcher/carpenter. Many players run the axer as a fighter that
  pays for itself.

See [advanced combat](/playing/combat-advanced/) for weapon specials and timing.

## Money

The axer farms the same [dungeon](/world/dungeons/) ladder as the plain warrior, but the +30%
damage edge means faster kills and more gold per hour at every rung. On top of that:

- **Wood income.** Cut logs on the way to and from a dungeon; boards sell to carpenters and
  fletchers, or feed your own crafting mule.
- **Dungeon farming.** Earth elementals, ogres, liches, and up the ladder — the damage bonus
  shortens every fight. Felucca spawns pay more if you accept the PvP risk.

## See also

- [Warrior template](/templates/warrior/) — the full novice→master storyline this build layers on.
- [7x GM Templates](/templates/seven-gm/) — where this sits among the endgame builds.
- [Lumberjacking](/skills/lumberjacking/), [Swordsmanship](/skills/swordsmanship/),
  [Tactics](/skills/tactics/).
- [Warrior profession](/professions/warrior/), [advanced combat](/playing/combat-advanced/).
