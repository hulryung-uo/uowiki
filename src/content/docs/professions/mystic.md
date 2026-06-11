---
title: Mystic
description: The Mysticism caster — a hard-hitting elemental and debuff school powered by Focus or Imbuing. Skills, build, play, gear, income.
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Mysticism/ (MysticSpell.cs power-skill = max(Imbuing, Focus); SpellDefinitions/: NetherBoltSpell.cs, EagleStrikeSpell.cs, SpellPlague.cs, CleansingWindsSpell.cs, RisingColossusSpell.cs, HealingStoneSpell.cs, NetherCycloneSpell.cs, StoneForm.cs)"
last_verified: 2026-06-11
generated: false
---

## What this profession is

The mystic is a caster built on [Mysticism](/skills/mysticism/), a Stygian-Abyss-era school of
elemental damage, debuffs, healing, and a powerful summon. On this shard Mysticism is real (the
EJ expansion stack includes SA skills). It's a strong standalone caster and combines well with
[Magery](/skills/magery/) or [Spellweaving](/skills/spellweaving/) for a multi-school caster.

## Core skills

- [Mysticism](/skills/mysticism/) — the casting skill; sets which spells you can use and base success.
- [Focus](/skills/focus/) **or Imbuing** — the **power skill** that scales Mysticism's damage and effect strength. The emulator uses whichever is higher: `MysticSpell.cs` takes `max(Imbuing, Focus)` (`servuo: Scripts/Spells/Mysticism/MysticSpell.cs`). Focus is the lighter pick; Imbuing doubles as a crafting skill.
- A secondary caster school — [Magery](/skills/magery/) + [Evaluating Intelligence](/skills/evaluating-intelligence/), or [Spellweaving](/skills/spellweaving/).
- [Meditation](/skills/meditation/) and [Resisting Spells](/skills/resisting-spells/) to fuel and survive.

## Reagents

Mysticism spells consume reagents (it shares several with mage and necro lines) plus mana. Keep
a stocked reagent pouch; the power of the cast still comes from Focus/Imbuing, not the regs.

## The build

There is **no dedicated mystic template page** yet. Build it from the [Mage Template](/templates/mage/):
keep the caster stat spread (high Int, plenty of mana) and swap the school slots for Mysticism +
Focus (or Imbuing) alongside Magery/Eval + Meditation + Resist. See [7x GM Templates](/templates/seven-gm/)
for fitting it under the 700-point cap.

## How to play it

[Magic Schools](/playing/magic-schools/) places Mysticism among the schools; [Spellcasting](/playing/spellcasting/)
covers the cast mechanics and [Meditation & Mana](/playing/meditation-and-mana/) covers recovery.

The toolkit (all confirmed under `servuo: Scripts/Spells/Mysticism/SpellDefinitions/`):

- **Nether Bolt** / **Eagle Strike** — reliable single-target damage nukes.
- **Spell Plague** — a debuff that detonates extra damage when the target keeps taking hits.
- **Cleansing Winds** — area heal and cure.
- **Healing Stone** — a self-heal item you conjure and carry.
- **Rising Colossus** — a powerful conjured combat ally; **Stone Form** is a defensive self-transform.
- **Nether Cyclone** / **Hail Storm** — area nukes for clearing packs.

## Gear

- [Magic item properties](/magic/) — prioritize **Spell Damage Increase**, **Lower Mana Cost**, **Lower Reagent Cost**, and **Faster Casting**; Mysticism Focus/Casting mods where available.
- [Armor](/items/armor/) — mage-friendly (no meditation penalty) with balanced resists.
- Keep a full **reagent** stock and a [spellbook](/items/) for the school.

## Making a living

Mystics farm dungeons as casters: open with debuffs (Spell Plague), nuke with Nether Bolt/Eagle
Strike, drop a Rising Colossus for tough targets, and heal with Cleansing Winds / Healing Stone.
Strong area spells make pack-clearing profitable. Sell loot via [Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [Mage](/professions/mage/) — the caster base this build borrows from
- [Spellweaver](/professions/spellweaver/) — a complementary support school to pair with
- [Mysticism skill](/skills/mysticism/) · [Focus](/skills/focus/) · [Magic Schools](/playing/magic-schools/)
