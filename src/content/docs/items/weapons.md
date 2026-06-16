---
title: Weapons
description: How weapons work in Ultima Online — damage, swing speed, the skill each trains, strength requirements, one- vs two-handed, and special moves — plus a source-verified stat table for every weapon family.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/*.cs"
  - "servuo: Scripts/Items/Equipment/Weapons/WeaponEnums.cs (Damage/Accuracy/Durability tiers)"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (tier bonuses, HitPoints/MaxHitPoints, OnCraft)"
  - "servuo: Scripts/Abilities/WeaponAbility.cs"
  - "uo-resource: tiledata.mul (weapon layer)"
  - "uowiki: data/weapons.json (extracted via tools/extract_weapons.py)"
last_verified: 2026-06-17
generated: false
---

Your weapon decides how a melee or ranged character actually fights: how hard you hit,
how fast you swing, which **combat skill** you train, and which two **special moves** you
can unleash. This page explains the stats, then gives a source-verified stat table for
every one of the **135 weapons** in the ServUO source, grouped by family.

:::tip
Stats below are the **AOS-era** values our shard (EJ) uses, read straight from each
weapon's `.cs` class. Swing speeds are shown in **seconds** (the ML/EJ `MlSpeed` value —
*lower is faster*). For a browsable, art-rich index of every weapon by era, see the
[Weapons catalog](/items/catalog/weapons/).
:::

## How weapons work

Every equippable weapon shares the same handful of stats. Understanding them is the whole
game of picking a weapon.

### Damage range

Each weapon lists a **minimum and maximum base damage** (e.g. a katana is 10–14). Every
swing rolls a random value in that range, and that base is then heavily modified before it
lands — by your **[Tactics](/skills/tactics/)** and **[Anatomy](/skills/anatomy/)** skills,
**Strength**, the weapon's damage-increase properties, and the target's resistances. The
table values are the *base* range only; a GM warrior with high Tactics and Anatomy hits for
far more. See [Combat Basics](/playing/combat-basics/) for the full damage pipeline and
[Mechanics](/mechanics/) for the underlying formulas.

### Weapon speed (swing delay)

**Speed** is how often you can attack. On our ML/EJ shard each weapon has an `MlSpeed` in
seconds — the table shows this directly, and **lower is faster** (a 2.0s dagger swings more
than twice as often as a 4.5s heavy crossbow). The *actual* delay between swings is shortened
by your **Stamina** and by **Swing Speed Increase** properties on gear: more stamina = faster
swings, and losing stamina in a fight slows you down. Because fast weapons land more hits,
they apply on-hit effects (poison, leech, specials) more often, while slow weapons put more
raw damage into each blow. See [Combat Advanced](/playing/combat-advanced/) for how stamina
and swing-speed bonuses combine.

### The governing skill

Each weapon trains exactly one **combat skill**, set by its class. The four melee skills and
the two ranged skills are:

- [**Swordsmanship**](/skills/swordsmanship/) — swords, axes, polearms
- [**Mace Fighting**](/skills/mace-fighting/) — maces, hammers, staves, wands
- [**Fencing**](/skills/fencing/) — daggers, kryss, spears, forks
- [**Archery**](/skills/archery/) — bows and crossbows
- **Throwing** — gargoyle thrown weapons

Your combat skill governs your **chance to hit**; **[Tactics](/skills/tactics/)** and
**[Anatomy](/skills/anatomy/)** then boost your **damage** and apply to *every* weapon, which
is why almost every melee template carries them (see the [7×GM warrior template](/templates/seven-gm/)).
A few weapons are built on one family's chassis but train a different skill — those are flagged
in the tables (<sup>Sw</sup> Swordsmanship, <sup>Fe</sup> Fencing, <sup>Ma</sup> Mace Fighting).

### Strength requirement

Each weapon has a **Strength requirement**. Equip a weapon while below its requirement and
you swing at a penalty. Heavy two-handers (halberd, war hammer, heavy crossbow) demand 80–95
Strength; light daggers and wands need as little as 5–10.

### One- vs two-handed

A **one-handed** weapon leaves your other hand free for a **shield** (Parrying) or a spellbook.
A **two-handed** weapon occupies both hands: **no shield, and it blocks casting** that needs a
free hand. Two-handers generally hit harder to compensate. The Hands column shows **1H** or **2H**.

### Damage types

Weapons deal a base **damage type** tied to their family: swords and knives **slash**, spears
and kryss **pierce**, maces and staves **bash**. The damage type is matched against the
target's resistances, and magical weapons can split their damage across fire/cold/poison/energy.

## Special moves

Every weapon grants two **special moves** — a **primary** and a **secondary** weapon ability.
You arm one from your combat book or the war-mode buttons; the next qualifying hit spends
**mana** (and sometimes stamina) to trigger it. Your **primary** ability unlocks around 70
skill in the weapon's combat skill, the **secondary** around 90. The two abilities a weapon
offers are fixed by its class — choosing a weapon is partly choosing its specials. See
[Combat Advanced](/playing/combat-advanced/) for activation, mana costs and timing.

The common abilities (from `Scripts/Abilities/WeaponAbility.cs`):

| Ability | What it does |
|---|---|
| **Armor Ignore** | Bypasses the target's armor — lower damage, but it lands almost in full. |
| **Bleed Attack** | Inflicts a bleed that deals damage over time. |
| **Concussion Blow** | Burst damage scaled to the target's current mana. |
| **Crushing Blow** | A heavy hit for roughly +50% damage. |
| **Disarm** | Knocks the target's weapon from their hands (needs a free hand). |
| **Dismount** | Knocks a mounted target off their mount — a PvP staple. |
| **Double Strike** | Two swings in one action. |
| **Infectious Strike** | Delivers the weapon's poison without consuming all charges. |
| **Mortal Strike** | Wounds the target so healing fails for several seconds. |
| **Moving Shot** | (Ranged) lets you fire while moving. |
| **Paralyzing Blow** | Freezes the target in place for a short time. |
| **Shadow Strike** | A hit that briefly hides/stealths the attacker. |
| **Whirlwind Attack** | Strikes *every* enemy adjacent to you at once. |
| **Frenzied Whirlwind** | An area attack that hits nearby foes repeatedly. |
| **Riding Swipe** | Dismounts the target and can lame their mount. |
| **Block / Defense Mastery** | Defensive specials that raise your damage reduction. |
| **Feint** | Reduces the damage the target deals to you for a few seconds. |
| **Dual Wield / Double Shot** | Extra-swing / extra-shot specials on certain Tokuno and ranged weapons. |
| **Armor Pierce** | Reduces the target's physical resistance on hit. |
| **Bladeweave** | Randomly triggers one of several abilities on hit. |
| **Force Arrow / Lightning Arrow / Serpent Arrow** | Elven bow specials adding elemental or magic effects. |
| **Psychic Attack** | Raises the target's mana cost and lowers their damage output. |
| **Mystic Arc / Infused Throw** | Gargoyle throwing specials (arcing/multi-target throws). |

:::note
Some weapons (e.g. the **Thin Longsword**) define no special moves and fall back to the
engine default of *none* — those show "—" in the Primary/Secondary columns.
:::

## Quality, magic properties & durability

Two weapons of the same family can be worlds apart. Beyond the base stats above, a weapon
carries **quality**, optional **magic properties**, and **durability**.

### Quality: normal vs exceptional

A crafted weapon is either **normal** or **exceptional**. An **exceptional** weapon gets
**+35% Damage Increase** baked in and **+20% durability**, and can bear the crafter's
**maker's mark**. A high-[Arms Lore](/skills/arms-lore/) crafter adds a little more Damage
Increase on top (`ArmsLore / 20`, so **+5% at GM**). See [Crafting](/playing/crafting/).

### The named magic tiers (Accuracy / Damage / Durability)

Magic weapons carry up to three independent enchantment lines, and their tier shows **right in
the weapon's name** (`WeaponEnums.cs`). A fully-loaded one reads like *"Supremely Accurate
Vanquishing [weapon] of [slayer]."*

| Accuracy prefix → **Hit Chance** | Damage prefix → **Damage Increase** | Durability prefix → **max durability** |
|---|---|---|
| Accurate **+2%** | Ruin **+15%** | Durable **+20%** |
| Surpassingly Accurate **+4%** | Might **+20%** | Substantial **+50%** |
| Eminently Accurate **+6%** | Force **+25%** | Massive **+70%** |
| Exceedingly Accurate **+8%** | Power **+30%** | Fortified **+100%** |
| Supremely Accurate **+10%** | **Vanquishing +35%** | Indestructible **+120%** |

So *Vanquishing* is the top damage tier (+35% DI), *Supremely Accurate* the top accuracy tier
(+10% hit chance), and *Indestructible* the toughest. These stack with each other and with
quality.

### AOS magic attributes

On this AOS/EJ shard, looted and **runic-crafted** weapons can also roll modern **attributes**
on top of (or instead of) the named tiers — e.g. **Hit Chance / Defense Chance Increase**,
**Damage Increase**, **Swing Speed Increase**, on-hit effects (**Hit Lightning/Fireball/Lower
Defense/Life Leech/Mana Leech**), **Slayer** (extra damage vs a creature type), **Spell
Channeling**, **Mage Weapon**, and **Use Best Weapon Skill**. Runic hammers/kits from
[Bulk Order Deeds](/mechanics/bulk-order-deeds/) are the crafted source of these.

### Durability and repair

Every weapon has **current / maximum hit points** (`HitPoints` / `MaxHitPoints` in
`BaseWeapon.cs`) — its durability. Using and fighting with a weapon slowly wears its current
durability down; at 0 it can break. **Repairing** it (with the matching craft skill — e.g.
[Blacksmithy](/skills/blacksmithy/) for metal weapons — or a repair contract) restores current
hit points, but each repair shaves a little off the **maximum**, so a weapon has a finite
life and eventually wears out. **Powder of Fortifying** (a [BOD reward](/mechanics/bulk-order-deeds/))
can raise an item's maximum durability back up. The durability **tier** above (Durable …
Indestructible) and exceptional quality both raise that maximum so the weapon lasts longer.

## Weapon families

Each section below gives the family's combat skill, its playstyle, and a stat table built
straight from the ServUO source. Table legend: **Damage** = base min–max; **Speed** = seconds
per swing (lower is faster); **Hands** = 1H/2H; **Str** = strength requirement; flags after a
weapon name mean <sup>G</sup> = Gargoyle-only, and <sup>Sw/Fe/Ma</sup> = trains a different
skill than its family's default.

Crafted weapons come from [Blacksmithy](/crafting/blacksmithy/) (metal weapons) and
[Bowfletching](/crafting/bowfletching/) (bows, crossbows and ammunition). For the full
art-and-era index, see the [Weapons catalog](/items/catalog/weapons/).

### Swords

**Skill:** [Swordsmanship](/skills/swordsmanship/) · **Weapons:** 33

The **Swordsmanship** family is the broadest in the game: katanas and longswords for fast one-handed DPS, two-handed slashers, and a deep roster of Samurai (Tokuno) and Gargoyle blades. Most are slashing-damage, one-handed weapons that pair with a shield. A handful declared as swords actually train **Fencing** (the kryss and lance — flagged <sup>Fe</sup>).

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x08FE.png" class="uo-sprite" alt="" width="40" /> | Blood Blade <sup>G·Fe</sup> | 10–12 | 2s | 1H | 10 | Bleed Attack | Paralyzing Blow |
| <img src="/img/items/0x27A8.png" class="uo-sprite" alt="" width="40" /> | Bokuto | 10–12 | 2s | 1H | 20 | Feint | Nerve Strike |
| <img src="/img/items/0x26BB.png" class="uo-sprite" alt="" width="40" /> | Bone Harvester | 12–16 | 3s | 1H | 25 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x2D35.png" class="uo-sprite" alt="" width="40" /> | Bone Machete | 11–15 | 2.75s | 1H | 20 | Defense Mastery | Bladeweave |
| <img src="/img/items/0x0F5E.png" class="uo-sprite" alt="" width="40" /> | Broadsword | 13–17 | 3.25s | 1H | 30 | Crushing Blow | Armor Ignore |
| <img src="/img/items/0x26C1.png" class="uo-sprite" alt="" width="40" /> | Crescent Blade | 12–15 | 2.5s | 2H | 55 | Double Strike | Mortal Strike |
| <img src="/img/items/0x1441.png" class="uo-sprite" alt="" width="40" /> | Cutlass | 10–14 | 2.5s | 1H | 25 | Bleed Attack | Shadow Strike |
| <img src="/img/items/0x27A9.png" class="uo-sprite" alt="" width="40" /> | Daisho | 13–16 | 2.75s | 2H | 40 | Feint | Double Strike |
| <img src="/img/items/0x090B.png" class="uo-sprite" alt="" width="40" /> | Dread Sword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Crushing Blow | Concussion Blow |
| <img src="/img/items/0x2D35.png" class="uo-sprite" alt="" width="40" /> | Elven Machete | 11–15 | 2.75s | 1H | 20 | Defense Mastery | Bladeweave |
| <img src="/img/items/0x48C6.png" class="uo-sprite" alt="" width="40" /> | Gargish Bone Harvester <sup>G</sup> | 12–16 | 3s | 1H | 25 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x48D0.png" class="uo-sprite" alt="" width="40" /> | Gargish Daisho <sup>G</sup> | 13–16 | 2.75s | 2H | 40 | Feint | Double Strike |
| <img src="/img/items/0x48BA.png" class="uo-sprite" alt="" width="40" /> | Gargish Katana <sup>G</sup> | 10–14 | 2.5s | 1H | 25 | Double Strike | Armor Ignore |
| <img src="/img/items/0x48BC.png" class="uo-sprite" alt="" width="40" /> | Gargish Kryss <sup>G·Fe</sup> | 10–12 | 2s | 1H | 10 | Armor Ignore | Infectious Strike |
| <img src="/img/items/0x48CA.png" class="uo-sprite" alt="" width="40" /> | Gargish Lance <sup>G·Fe</sup> | 18–22 | 4.25s | 1H | 95 | Dismount | Concussion Blow |
| <img src="/img/items/0xA345.png" class="uo-sprite" alt="" width="40" /> | Gargish Skull Longsword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x0908.png" class="uo-sprite" alt="" width="40" /> | Gargish Talwar <sup>G</sup> | 16–19 | 3.5s | 2H | 40 | Whirlwind Attack | Dismount |
| <img src="/img/items/0x090C.png" class="uo-sprite" alt="" width="40" /> | Glass Sword <sup>G</sup> | 11–15 | 2.75s | 1H | 20 | Bleed Attack | Mortal Strike |
| <img src="/img/items/0x13FF.png" class="uo-sprite" alt="" width="40" /> | Katana | 10–14 | 2.5s | 1H | 25 | Double Strike | Armor Ignore |
| <img src="/img/items/0x1401.png" class="uo-sprite" alt="" width="40" /> | Kryss <sup>Fe</sup> | 10–12 | 2s | 1H | 10 | Armor Ignore | Infectious Strike |
| <img src="/img/items/0x26C0.png" class="uo-sprite" alt="" width="40" /> | Lance <sup>Fe</sup> | 18–22 | 4.25s | 1H | 95 | Dismount | Concussion Blow |
| <img src="/img/items/0x0F61.png" class="uo-sprite" alt="" width="40" /> | Longsword | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x27A2.png" class="uo-sprite" alt="" width="40" /> | No Dachi | 16–19 | 3.5s | 2H | 40 | Crushing Blow | Riding Swipe |
| <img src="/img/items/0x26CE.png" class="uo-sprite" alt="" width="40" /> | Paladin Sword | 20–24 | 5s | 1H | 85 | Whirlwind Attack | Disarm |
| <img src="/img/items/0x2D33.png" class="uo-sprite" alt="" width="40" /> | Radiant Scimitar | 10–14 | 2.5s | 1H | 20 | Whirlwind Attack | Bladeweave |
| <img src="/img/items/0x2D32.png" class="uo-sprite" alt="" width="40" /> | Rune Blade | 14–17 | 3s | 2H | 30 | Disarm | Bladeweave |
| <img src="/img/items/0x13B6.png" class="uo-sprite" alt="" width="40" /> | Scimitar | 12–16 | 3s | 1H | 25 | Double Strike | Paralyzing Blow |
| <img src="/img/items/0x0907.png" class="uo-sprite" alt="" width="40" /> | Shortblade <sup>G·Fe</sup> | 10–13 | 2.25s | 1H | 45 | Armor Ignore | Mortal Strike |
| <img src="/img/items/0xA341.png" class="uo-sprite" alt="" width="40" /> | Skull Longsword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x0900.png" class="uo-sprite" alt="" width="40" /> | Stone War Sword <sup>G</sup> | 15–19 | 3.75s | 1H | 40 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x13B8.png" class="uo-sprite" alt="" width="40" /> | Thin Longsword | 15–16 | 3.5s | 1H | 35 | — | — |
| <img src="/img/items/0x13B9.png" class="uo-sprite" alt="" width="40" /> | Viking Sword | 15–19 | 3.75s | 1H | 40 | Crushing Blow | Paralyzing Blow |
| <img src="/img/items/0x27A4.png" class="uo-sprite" alt="" width="40" /> | Wakizashi | 10–14 | 2.5s | 1H | 20 | Frenzied Whirlwind | Double Strike |


### Axes

**Skill:** [Swordsmanship](/skills/swordsmanship/) · **Weapons:** 14

Axes also train **Swordsmanship** but skew toward heavy two-handed weapons with high damage and strength requirements. Many double as **lumberjacking** tools (the hatchet, two-handed axe, large battle axe), and lumberjacks get a bonus to axe damage. The war axe (<sup>Ma</sup>) is the odd one out — it trains Mace Fighting.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0F49.png" class="uo-sprite" alt="" width="40" /> | Axe | 14–17 | 3s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x0F47.png" class="uo-sprite" alt="" width="40" /> | Battle Axe | 16–19 | 3.5s | 2H | 35 | Bleed Attack | Concussion Blow |
| <img src="/img/items/0x0F4B.png" class="uo-sprite" alt="" width="40" /> | Double Axe | 15–18 | 3.25s | 2H | 45 | Double Strike | Whirlwind Attack |
| <img src="/img/items/0x08FD.png" class="uo-sprite" alt="" width="40" /> | Dual Short Axes <sup>G</sup> | 14–17 | 3s | 2H | 35 | Double Strike | Infectious Strike |
| <img src="/img/items/0x0F45.png" class="uo-sprite" alt="" width="40" /> | Executioners Axe | 15–18 | 3.25s | 2H | 40 | Bleed Attack | Mortal Strike |
| <img src="/img/items/0x48B2.png" class="uo-sprite" alt="" width="40" /> | Gargish Axe <sup>G</sup> | 14–17 | 3s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x48B0.png" class="uo-sprite" alt="" width="40" /> | Gargish Battle Axe <sup>G</sup> | 16–19 | 3.5s | 2H | 35 | Bleed Attack | Concussion Blow |
| <img src="/img/items/0x0F43.png" class="uo-sprite" alt="" width="40" /> | Hatchet | 13–16 | 2.75s | 2H | 20 | Armor Ignore | Disarm |
| <img src="/img/items/0x2D28.png" class="uo-sprite" alt="" width="40" /> | Heavy Ornate Axe | 17–20 | 3.75s | 2H | 45 | Disarm | Crushing Blow |
| <img src="/img/items/0x13FB.png" class="uo-sprite" alt="" width="40" /> | Large Battle Axe | 17–20 | 3.75s | 2H | 80 | Whirlwind Attack | Bleed Attack |
| <img src="/img/items/0x2D28.png" class="uo-sprite" alt="" width="40" /> | Ornate Axe | 17–20 | 3.75s | 2H | 45 | Disarm | Crushing Blow |
| <img src="/img/items/0x0E86.png" class="uo-sprite" alt="" width="40" /> | Pickaxe | 12–16 | 3s | 1H | 50 | Double Strike | Disarm |
| <img src="/img/items/0x1443.png" class="uo-sprite" alt="" width="40" /> | Two Handed Axe | 16–19 | 3.5s | 2H | 40 | Double Strike | Shadow Strike |
| <img src="/img/items/0x13B0.png" class="uo-sprite" alt="" width="40" /> | War Axe <sup>Ma</sup> | 12–16 | 3s | 1H | 35 | Armor Ignore | Bleed Attack |


### Maces & Hammers

**Skill:** [Mace Fighting](/skills/mace-fighting/) · **Weapons:** 20

Maces train **Mace Fighting** and deal bashing damage. Their signature trait: against players, mace weapons can damage stamina and (in older rulesets) ignore part of armor. They range from the light club to the brutal two-handed war hammer. A couple of decorative "wand" items (the magic wand / fireworks wand) are actually bashing weapons and sit here, not in the Wands family.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | A Fireworks Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x13B4.png" class="uo-sprite" alt="" width="40" /> | Club | 10–14 | 2.5s | 1H | 40 | Crushing Blow | Dismount |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Diamond Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x0903.png" class="uo-sprite" alt="" width="40" /> | Disc Mace <sup>G</sup> | 11–15 | 2.75s | 1H | 45 | Armor Ignore | Disarm |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Emerald Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x48C2.png" class="uo-sprite" alt="" width="40" /> | Gargish Maul <sup>G</sup> | 14–18 | 3.5s | 1H | 45 | Double Strike | Concussion Blow |
| <img src="/img/items/0x48CC.png" class="uo-sprite" alt="" width="40" /> | Gargish Tessen <sup>G</sup> | 10–13 | 2s | 2H | 10 | Feint | Dual Wield |
| <img src="/img/items/0x48C0.png" class="uo-sprite" alt="" width="40" /> | Gargish War Hammer <sup>G</sup> | 17–20 | 3.75s | 2H | 95 | Whirlwind Attack | Crushing Blow |
| <img src="/img/items/0x143D.png" class="uo-sprite" alt="" width="40" /> | Hammer Pick | 13–17 | 3.25s | 1H | 45 | Armor Ignore | Mortal Strike |
| <img src="/img/items/0x0F5C.png" class="uo-sprite" alt="" width="40" /> | Mace | 11–15 | 2.75s | 1H | 45 | Concussion Blow | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Magic Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x143B.png" class="uo-sprite" alt="" width="40" /> | Maul | 14–18 | 3.5s | 1H | 45 | Double Strike | Concussion Blow |
| <img src="/img/items/0x27AE.png" class="uo-sprite" alt="" width="40" /> | Nunchaku | 12–15 | 2.5s | 2H | 15 | Block | Double Strike |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Ruby Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x26BC.png" class="uo-sprite" alt="" width="40" /> | Scepter | 14–18 | 3.5s | 1H | 40 | Crushing Blow | Mortal Strike |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Silver-Etched Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x27A3.png" class="uo-sprite" alt="" width="40" /> | Tessen | 10–13 | 2s | 2H | 10 | Feint | Dual Wield |
| <img src="/img/items/0x27A6.png" class="uo-sprite" alt="" width="40" /> | Tetsubo | 12–15 | 2.5s | 2H | 35 | Frenzied Whirlwind | Crushing Blow |
| <img src="/img/items/0x1439.png" class="uo-sprite" alt="" width="40" /> | War Hammer | 17–20 | 3.75s | 2H | 95 | Whirlwind Attack | Crushing Blow |
| <img src="/img/items/0x1407.png" class="uo-sprite" alt="" width="40" /> | War Mace | 16–20 | 4s | 1H | 80 | Crushing Blow | Mortal Strike |


### Staves

**Skill:** [Mace Fighting](/skills/mace-fighting/) · **Weapons:** 10

Quarterstaves, gnarled staves and black staves are two-handed **Mace Fighting** weapons. They are popular on mages and tamers because the two-handed staff art still allows certain caster builds, and several gnarled staves carry the Gargoyle *Force of Nature* special.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF0.png" class="uo-sprite" alt="" width="40" /> | Black Staff | 13–16 | 2.75s | 2H | 35 | Whirlwind Attack | Paralyzing Blow |
| <img src="/img/items/0x48B8.png" class="uo-sprite" alt="" width="40" /> | Gargish Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0xA347.png" class="uo-sprite" alt="" width="40" /> | Gargish Skull Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x0905.png" class="uo-sprite" alt="" width="40" /> | Glass Staff <sup>G</sup> | 11–14 | 2.25s | 2H | 20 | Double Strike | Mortal Strike |
| <img src="/img/items/0x13F8.png" class="uo-sprite" alt="" width="40" /> | Gnarled Staff | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x0E89.png" class="uo-sprite" alt="" width="40" /> | Quarter Staff | 11–14 | 2.25s | 2H | 30 | Double Strike | Concussion Blow |
| <img src="/img/items/0x0906.png" class="uo-sprite" alt="" width="40" /> | Serpent Stone Staff <sup>G</sup> | 16–19 | 3.5s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x0E81.png" class="uo-sprite" alt="" width="40" /> | Shepherds Crook | 13–16 | 2.75s | 2H | 20 | Crushing Blow | Disarm |
| <img src="/img/items/0xA343.png" class="uo-sprite" alt="" width="40" /> | Skull Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x2D25.png" class="uo-sprite" alt="" width="40" /> | Wild Staff | 10–13 | 2.25s | 1H | 15 | Block | Force of Nature |


### Daggers & Knives

**Skill:** [Fencing](/skills/fencing/) · **Weapons:** 17

Light, very fast **Fencing** weapons. Daggers swing about as fast as anything in the game and excel at applying poison and the Infectious Strike special. The butchering knives (butcher knife, cleaver, skinning knife — flagged <sup>Sw</sup>) are knife-shaped but train **Swordsmanship** and double as skinning tools.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x2D21.png" class="uo-sprite" alt="" width="40" /> | Assassin Spike | 10–12 | 2s | 1H | 15 | Infectious Strike | Shadow Strike |
| <img src="/img/items/0x13F6.png" class="uo-sprite" alt="" width="40" /> | Butcher Knife <sup>Sw</sup> | 10–13 | 2.25s | 1H | 10 | Infectious Strike | Disarm |
| <img src="/img/items/0x0EC3.png" class="uo-sprite" alt="" width="40" /> | Cleaver <sup>Sw</sup> | 10–14 | 2.5s | 1H | 10 | Bleed Attack | Infectious Strike |
| <img src="/img/items/0x0F52.png" class="uo-sprite" alt="" width="40" /> | Dagger | 10–12 | 2s | 1H | 10 | Shadow Strike | Infectious Strike |
| <img src="/img/items/0x2D20.png" class="uo-sprite" alt="" width="40" /> | Elven Spellblade | 12–15 | 2.5s | 2H | 35 | Psychic Attack | Bleed Attack |
| <img src="/img/items/0x48B6.png" class="uo-sprite" alt="" width="40" /> | Gargish Butcher Knife <sup>G·Sw</sup> | 10–13 | 2.25s | 1H | 10 | Infectious Strike | Disarm |
| <img src="/img/items/0x48AE.png" class="uo-sprite" alt="" width="40" /> | Gargish Cleaver <sup>G·Sw</sup> | 10–14 | 2.5s | 1H | 10 | Bleed Attack | Infectious Strike |
| <img src="/img/items/0x0902.png" class="uo-sprite" alt="" width="40" /> | Gargish Dagger <sup>G</sup> | 10–12 | 2s | 1H | 10 | Shadow Strike | Infectious Strike |
| <img src="/img/items/0x48CE.png" class="uo-sprite" alt="" width="40" /> | Gargish Tekagi <sup>G</sup> | 10–13 | 2s | 2H | 10 | Dual Wield | Talon Strike |
| <img src="/img/items/0x27AD.png" class="uo-sprite" alt="" width="40" /> | Kama | 10–13 | 2s | 2H | 15 | Whirlwind Attack | Defense Mastery |
| <img src="/img/items/0x27A7.png" class="uo-sprite" alt="" width="40" /> | Lajatang | 16–19 | 3.5s | 2H | 65 | Defense Mastery | Frenzied Whirlwind |
| <img src="/img/items/0x2D22.png" class="uo-sprite" alt="" width="40" /> | Leafblade | 11–15 | 2.75s | 1H | 20 | Feint | Armor Ignore |
| <img src="/img/items/0x27AF.png" class="uo-sprite" alt="" width="40" /> | Sai | 10–13 | 2s | 2H | 15 | Dual Wield | Armor Pierce |
| <img src="/img/items/0x2D2F.png" class="uo-sprite" alt="" width="40" /> | Serrated War Cleaver | 10–13 | 2.25s | 2H | 15 | Disarm | Bladeweave |
| <img src="/img/items/0x0EC4.png" class="uo-sprite" alt="" width="40" /> | Skinning Knife <sup>Sw</sup> | 10–13 | 2.25s | 1H | 5 | Shadow Strike | Bleed Attack |
| <img src="/img/items/0x27AB.png" class="uo-sprite" alt="" width="40" /> | Tekagi | 10–13 | 2s | 2H | 10 | Dual Wield | Talon Strike |
| <img src="/img/items/0x2D2F.png" class="uo-sprite" alt="" width="40" /> | War Cleaver | 10–13 | 2.25s | 2H | 15 | Disarm | Bladeweave |


### Spears & Forks

**Skill:** [Fencing](/skills/fencing/) · **Weapons:** 11

Spears, pikes and war forks are piercing **Fencing** weapons, mostly two-handed with good reach-style damage. The bladed staff (<sup>Sw</sup>) is built on the spear chassis but trains Swordsmanship.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x26BD.png" class="uo-sprite" alt="" width="40" /> | Bladed Staff <sup>Sw</sup> | 14–17 | 3s | 2H | 40 | Armor Ignore | Dismount |
| <img src="/img/items/0x26BF.png" class="uo-sprite" alt="" width="40" /> | Double Bladed Staff | 11–14 | 2.25s | 2H | 50 | Double Strike | Infectious Strike |
| <img src="/img/items/0x0904.png" class="uo-sprite" alt="" width="40" /> | Dual Pointed Spear <sup>G</sup> | 11–14 | 2.25s | 2H | 50 | Double Strike | Disarm |
| <img src="/img/items/0x48C8.png" class="uo-sprite" alt="" width="40" /> | Gargish Pike <sup>G</sup> | 14–17 | 3s | 2H | 50 | Paralyzing Blow | Infectious Strike |
| <img src="/img/items/0x48BE.png" class="uo-sprite" alt="" width="40" /> | Gargish War Fork <sup>G</sup> | 10–14 | 2.5s | 1H | 45 | Bleed Attack | Disarm |
| <img src="/img/items/0x26BE.png" class="uo-sprite" alt="" width="40" /> | Pike | 14–17 | 3s | 2H | 50 | Paralyzing Blow | Infectious Strike |
| <img src="/img/items/0x0E87.png" class="uo-sprite" alt="" width="40" /> | Pitchfork | 12–15 | 2.5s | 2H | 55 | Bleed Attack | Dismount |
| <img src="/img/items/0x1403.png" class="uo-sprite" alt="" width="40" /> | Short Spear | 10–13 | 2s | 2H | 40 | Shadow Strike | Mortal Strike |
| <img src="/img/items/0x0F62.png" class="uo-sprite" alt="" width="40" /> | Spear | 13–16 | 2.75s | 2H | 50 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x0F62.png" class="uo-sprite" alt="" width="40" /> | Tribal Spear | 13–15 | 2.75s | 2H | 50 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x1405.png" class="uo-sprite" alt="" width="40" /> | War Fork | 10–14 | 2.5s | 1H | 45 | Bleed Attack | Disarm |


### Polearms

**Skill:** [Swordsmanship](/skills/swordsmanship/) · **Weapons:** 5

Bardiches, halberds and scythes are massive two-handed **Swordsmanship** polearms — the highest base damage and strength requirements in melee, traded against slow swing speed. They are whirlwind/area-damage staples.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0F4D.png" class="uo-sprite" alt="" width="40" /> | Bardiche | 17–20 | 3.75s | 2H | 45 | Paralyzing Blow | Dismount |
| <img src="/img/items/0x48B4.png" class="uo-sprite" alt="" width="40" /> | Gargish Bardiche <sup>G</sup> | 17–20 | 3.75s | 2H | 45 | Paralyzing Blow | Dismount |
| <img src="/img/items/0x48C4.png" class="uo-sprite" alt="" width="40" /> | Gargish Scythe <sup>G</sup> | 16–19 | 3.5s | 2H | 45 | Bleed Attack | Paralyzing Blow |
| <img src="/img/items/0x143E.png" class="uo-sprite" alt="" width="40" /> | Halberd | 18–21 | 4s | 2H | 95 | Whirlwind Attack | Concussion Blow |
| <img src="/img/items/0x26BA.png" class="uo-sprite" alt="" width="40" /> | Scythe | 16–19 | 3.5s | 2H | 45 | Bleed Attack | Paralyzing Blow |


### Bows & Crossbows

**Skill:** [Archery](/skills/archery/) · **Weapons:** 11

Ranged **Archery** weapons. Every bow and crossbow is two-handed, requires a free hand (no shield), and consumes ammunition — arrows for bows, bolts for crossbows. Heavier crossbows hit harder but swing slowly; repeating crossbows and shortbows trade damage for speed.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | An Orcish Bow | 17–21 | 4.25s | 2H | 30 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | Bow | 17–21 | 4.25s | 2H | 30 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x26C2.png" class="uo-sprite" alt="" width="40" /> | Composite Bow | 16–20 | 4s | 2H | 45 | Armor Ignore | Moving Shot |
| <img src="/img/items/0x0F50.png" class="uo-sprite" alt="" width="40" /> | Crossbow | 18–22 | 4.5s | 2H | 35 | Concussion Blow | Mortal Strike |
| <img src="/img/items/0x2D1E.png" class="uo-sprite" alt="" width="40" /> | Elven Composite Longbow | 15–19 | 3.75s | 2H | 45 | Force Arrow | Serpent Arrow |
| <img src="/img/items/0x13FD.png" class="uo-sprite" alt="" width="40" /> | Heavy Crossbow | 20–24 | 5s | 2H | 80 | Moving Shot | Dismount |
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | Juka Bow | 17–21 | 4.25s | 2H | 100 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x2D2B.png" class="uo-sprite" alt="" width="40" /> | Lightweight Shortbow | 12–16 | 3s | 2H | 45 | Lightning Arrow | Psychic Attack |
| <img src="/img/items/0x2D2B.png" class="uo-sprite" alt="" width="40" /> | Magical Shortbow | 12–16 | 3s | 2H | 45 | Lightning Arrow | Psychic Attack |
| <img src="/img/items/0x26C3.png" class="uo-sprite" alt="" width="40" /> | Repeating Crossbow | 11–15 | 2.75s | 2H | 30 | Double Strike | Moving Shot |
| <img src="/img/items/0x27A5.png" class="uo-sprite" alt="" width="40" /> | Yumi | 13–17 | 3.25s | 2H | 35 | Armor Pierce | Double Shot |


### Thrown

**Skill:** [Throwing](/skills/throwing/) · **Weapons:** 3

Gargoyle-only **Throwing** weapons (boomerang, cyclone, soul glaive). They are thrown at range like archery but governed by the Throwing skill and benefit from Strength for extra range. One-handed.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x08FF.png" class="uo-sprite" alt="" width="40" /> | Boomerang <sup>G</sup> | 11–15 | 2.75s | 1H | 25 | Mystic Arc | Concussion Blow |
| <img src="/img/items/0x0901.png" class="uo-sprite" alt="" width="40" /> | Cyclone <sup>G</sup> | 13–17 | 3.25s | 1H | 40 | Moving Shot | Infused Throw |
| <img src="/img/items/0x090A.png" class="uo-sprite" alt="" width="40" /> | Soul Glaive <sup>G</sup> | 16–20 | 4s | 1H | 60 | Armor Ignore | Mortal Strike |


### Wands

**Skill:** [Mace Fighting](/skills/mace-fighting/) · **Weapons:** 11

Wands are one-handed **Mace Fighting** weapons that also hold magic charges (Heal, Harm, Fireball, etc.). As melee weapons they are uniformly weak (9–11 damage, low str requirement) with the Dismount/Disarm special set inherited from `BaseWand`; their value is the spell charges, not the swing.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Clumsy Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Feeble Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Fireball Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Greater Heal Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Harm Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Heal Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Id Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Lightning Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Magic Arrow Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Mana Drain Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Weakness Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |


## See also

- [Combat Basics](/playing/combat-basics/) and [Combat Advanced](/playing/combat-advanced/) — how swings, hit chance, damage and specials resolve
- [Swordsmanship](/skills/swordsmanship/) · [Mace Fighting](/skills/mace-fighting/) · [Fencing](/skills/fencing/) · [Archery](/skills/archery/) — the combat skills
- [Tactics](/skills/tactics/) and [Anatomy](/skills/anatomy/) — the universal damage skills every warrior carries
- [7×GM warrior template](/templates/seven-gm/) — a complete melee build
- [Blacksmithy](/crafting/blacksmithy/) and [Bowfletching](/crafting/bowfletching/) — crafting your own weapons
- [Weapons catalog](/items/catalog/weapons/) — every weapon by era, with art and item IDs
