---
title: Combat (Advanced)
description: Hit chance and defense, damage components, damage types and resistances, weapon speed, special moves, spell disruption, and mounted combat.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (CheckHit hit-chance, ScaleDamageAOS, GetDelay swing speed, CheckParry)"
  - "servuo: Server/Mobile.cs (MaxPlayerResistance = 70)"
  - "servuo: Scripts/Items/Resource/Bandage.cs (bandage/beneficial range)"
last_verified: 2026-06-15
generated: false
---

This page builds on [Combat basics](/playing/combat-basics/) with the systems that decide
whether you hit, how much damage you deal, and how to use special moves and mounts. The
formulas below are read from ServUO source (`BaseWeapon.cs`, `Mobile.cs`) and apply to this
shard's expansion (**EJ** — the AOS/ML code paths). Where a number is still unconfirmed it
is marked **(unverified)**.

## Hit chance and defense

**Whether a swing lands** is a contest between the attacker's accuracy and the defender's
ability to avoid the blow. On this shard (AOS rules), the chance is computed in
`BaseWeapon.CheckHit`:

```
hitChance = (atkSkill + 20) × (100 + HCI)
            ─────────────────────────────────
            (defSkill + 20) × (100 + DCI) × 2
```

- **atkSkill / defSkill** — the attacker's and defender's effective **weapon skill**
  ([Swordsmanship](/skills/swordsmanship/), [Mace Fighting](/skills/mace-fighting/),
  [Fencing](/skills/fencing/), [Archery](/skills/archery/), [Throwing](/skills/throwing/),
  or [Wrestling](/skills/wrestling/) if unarmed).
- **HCI** = your **Hit Chance Increase** item bonus, **capped at 45%** (50% for Gargoyles).
- **DCI** = the defender's **Defense Chance Increase**, also **capped at 45%**.
- **Floor: 2%** — every swing always has at least a 2% chance to land.

**Worked examples:** at 100 vs 100 skill with no item bonuses,
`(120 × 100) / (120 × 100 × 2) = 50%`. Stack 45% HCI against the same defender and you rise
to `(120 × 145) / (120 × 100 × 2) = 72.5%`. This is why HCI is a priority property for PvP
and high-end PvM builds. A successful [Parry](/skills/parrying/) can still block a hit that
would otherwise land (see [Parrying](#parrying) below).

## Damage components

When a hit lands, ServUO scales the weapon's **base damage** by a stack of percentage
bonuses (`BaseWeapon.ScaleDamageAOS`):

```
damage = baseDamage × (1 + Strength% + Tactics% + Anatomy% + Lumberjack% + DamageIncrease%)
```

| Component | Formula | At grandmaster / 100 Str |
|---|---|---|
| **Base weapon damage** | weapon's min–max range (see [weapons](/items/catalog/weapons/)) | — |
| **[Tactics](/skills/tactics/)** | `Tactics × 0.625%` (+6.25% at 100) | **+68.75%** |
| **[Anatomy](/skills/anatomy/)** | `Anatomy × 0.5%` (+5% at 100) | **+55%** |
| **Strength** | `Str × 0.3%` (+5% at 100) | **+35%** |
| **[Lumberjacking](/skills/lumberjacking/)** (axes only) | `Lumberjack × 0.2%` (+10% at 100) | **+30%** |
| **Damage Increase** (item property) | added directly, **capped at +100%** | up to +100% |

These bonuses are **additive**, then the total multiplies base damage — so a maxed melee
character with an axe roughly *doubles-and-more* the weapon's printed damage before item DI.
On top of the scaled number come **slayer** multipliers vs the right creature type and
**elemental damage conversions** from the weapon. The takeaway: **weapon + Tactics + Anatomy
+ Strength** (plus Lumberjacking for axes) is the core melee damage stack, and Tactics is the
single largest contributor.

## Damage types and resistances

Every hit deals one or more of **five damage types**:

- **Physical**
- **Fire**
- **Cold**
- **Poison**
- **Energy**

The defender reduces incoming damage by their **resistance** to that type:

- **Players** get resistances from worn [armor](/items/catalog/armor/) and
  [jewelry](/items/catalog/jewelry/); each piece lists its Physical/Fire/Cold/Poison/Energy
  resist values, and they sum up to a capped total per type.
- **Resistance cap: 70% per damage type** for players (`Mobile.cs`,
  `MaxPlayerResistance = 70`). Once a type hits 70%, additional resist gear of that type is
  wasted on standing defense — balance your five resists rather than over-stacking one.
- **Creatures** have their own innate resistances — listed per monster in the
  [Bestiary](/bestiary/). A dragon shrugs off fire; an elemental resists its own element.

**To fight efficiently:** check the target's weaknesses in the
[Bestiary](/bestiary/) and bring a weapon (or spells) that deal the damage type it
resists *least*. Conversely, wear armor that covers the damage types the enemy deals.

## Weapon speed and stamina

On this shard (ML code path), the delay between swings is (`BaseWeapon.GetDelay`):

```
ticks       = floor( (weaponSpeed × 4 − Stamina ÷ 30) × 100 ÷ (100 + SSI) )
swingDelay  = ticks × 0.25 seconds          (minimum 5 ticks = 1.25 s)
```

- **weaponSpeed** is the weapon's base speed value; faster weapons have a lower number.
- **Stamina** directly speeds you up — every 30 points of Stam shaves one tick off the raw
  swing, so losing Stamina visibly slows your attacks in real time.
- **SSI** = "Swing Speed Increase" item bonus, **capped at 60%**.
- **Floor: 1.25 seconds** — no build can swing faster than once every 1.25 s (5 ticks).

Stamina drains from running and from being hit; eat [food](/items/catalog/food-drink/) and
rest to recover. Fast weapons favor special-move spam and on-hit effects; slow weapons favor
big single hits. See [Combat basics](/playing/combat-basics/#weapon-speed-stamina-and-range).

## Parrying

Holding a **shield** (or, with [Bushido](/skills/bushido/), a weapon) gives a chance to
**block a hit outright** before damage is rolled. With a shield equipped
(`BaseWeapon.CheckParry`):

```
blockChance = (Parrying − Bushido) ÷ 400      (+5% if Parrying or Bushido ≥ 100)
```

- At **GM Parrying (100) with no Bushido**, that is `100 ÷ 400 + 5% = 30%` block — the
  practical ceiling for a pure shield tank.
- **Low Dexterity hurts you:** if Dex < 80 the chance is scaled by `(20 + Dex) ÷ 100`, so a
  fragile-Dex character parries noticeably less.
- **Weapon parry without a shield** (needs Bushido) uses `(Parry × Bushido) ÷ 48000`
  one-handed or `÷ 41140` two-handed, falling back to `Parry ÷ 800` if that is higher — so
  weapon-parry is weak until you invest in Bushido.

A successful parry blocks the blow regardless of the attacker's hit chance, which is why a
shield + GM Parrying is the backbone of a survivable melee or PvP build.

## Special moves (primary and secondary)

Most weapons grant **two special moves** — a **primary** and a **secondary** ability —
unlocked at certain [Tactics](/skills/tactics/) and/or weapon-skill thresholds. Examples
of common effects (the exact set depends on the weapon): armor-ignoring strikes, bleeding
wounds, mortal/wound effects that block healing, paralyzing blows, area hits, and
disarms.

**To use a special move:**

1. Open the weapon-ability bar/gump in your client.
2. **Toggle the primary or secondary ability on**; it stays armed.
3. Land your **next qualifying hit** — the ability fires and consumes **mana**.

Special moves **cost mana** (amount varies by ability and is reduced by mastery — **exact
costs unverified**). If you lack the mana when the hit lands, the special does not trigger.
[Bushido](/skills/bushido/) and [Ninjitsu](/skills/ninjitsu/) add their own weapon
specials. See the individual weapon-skill pages for which moves each weapon type offers.

## Spell and weapon disruption ("fizzle")

- **Casting while being hit can be disrupted.** If you take a hit (or otherwise lose
  concentration) mid-cast, the spell **fizzles** — it fails, you may lose reagents/mana,
  and you must recast. This is why mages kite and heal between casts; see
  [Spellcasting](/playing/spellcasting/) and [Magery](/skills/magery/).
- A bandage application can likewise **slip** ("Your fingers slip!") or fail to finish if
  you are interrupted or move out of range — see [Healing](/playing/healing/).
- Holding still, keeping distance, and protective spells/abilities reduce disruption
  (resisting-spells and protection effects are **unverified** in specifics — see
  [Resisting Spells](/skills/resisting-spells/)).

## Mounts in combat

- **Riding a mount** lets you move at the faster mounted speed and chase or flee more
  effectively. You can fight from horseback with melee and ranged weapons.
- Some abilities and special moves (notably certain dismount specials, and lances) can
  **knock you off your mount**; on foot you move slower. (Specifics **unverified**.)
- Mounts are creatures: they can be targeted and, if a war-horse/pet, healed or killed.
  See [Taming & pets](/playing/taming-and-pets/) and
  [Movement & travel](/playing/movement-and-travel/).

## Fleeing and line of sight (recap)

To disengage: drop to **peace mode**, run, and use terrain to break a ranged attacker's
**line of sight**. Melee enemies must stay adjacent to swing; ranged enemies need an
unobstructed line. Once out of sight you can [Hide](/playing/hiding-and-stealth/) or
**Recall** away. Full procedure in
[Combat basics → Fleeing](/playing/combat-basics/#fleeing).

## See also

- [Combat basics](/playing/combat-basics/)
- [Tactics](/skills/tactics/), [Anatomy](/skills/anatomy/), [Parrying](/skills/parrying/)
- [Healing](/playing/healing/), [Poison & status](/playing/poison-and-status/)
- [Bestiary](/bestiary/) — creature resistances and damage types
- [Mechanics](/mechanics/) — the underlying numbers
