---
title: Poisoning
description: Coat blades and food with poison.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 30 — primary Int, secondary Dex)"
  - "servuo: Scripts/Skills/Poisoning.cs (apply flow, Infectious Strike rule, charges, self-poison, -20 karma)"
  - "servuo: Scripts/Items/Consumables/*PoisonPotion.cs (per-potion skill windows)"
  - "servuo: Scripts/Misc/Poison.cs (AOS poison tiers Lesser..Lethal, Darkglow, Parasitic)"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-17
generated: false
---

<img src="/img/skill-flags/30.gif" alt="Poisoning skill banner" width="160" />

Poisoning applies poison to weapons (and, classically, food). The prose is community-derived
(paraphrased from the uorenaissance.com skill list plus ServUO behavior) pending field
verification; the stats table, potion skill ranges, and charge formula below are
source-verified against ServUO.

## What it does

Poisoning lets you coat a bladed or piercing weapon — or food/drink — with poison from a
poison potion, so that creatures struck (or fed) take poison damage over time. Higher skill
lets you apply **stronger** poisons more reliably. It is a Mastery skill favored by assassins
and a nasty addition to a [Fencer's](/skills/fencing/) infectious-strike blade.

## How to apply poison

To envenom something: **use the Poisoning skill, target a poison potion** in your pack, then
**target the item** to coat. After a ~2-second application a skill check decides whether the
poison takes; on success the potion is consumed (you keep the empty bottle) and the item
carries that poison (`Scripts/Skills/Poisoning.cs`).

**What can be poisoned (on this AOS/EJ shard):**

- **Weapons with the *Infectious Strike* special move.** This is the AOS rule the server
  enforces — *not* "any bladed weapon." The weapon's primary or secondary ability must be
  **Infectious Strike**; anything else is rejected with *"You can only poison infectious
  weapons, food or drink."* A poisoned weapon delivers its dose when you land an **Infectious
  Strike**.
- **Food and drink** — a poisoned meal hits whoever eats it (the classic assassin's trick).
- **Throwing weapons** — *fukiya darts* and *shuriken*.

Applying poison is an **evil act** (**−20 karma** each time), and at **under 80.0 skill** a
failed attempt has a **5% chance to poison *you* instead** (*"You make a grave mistake…"*).
See [Poison & status](/playing/poison-and-status/) for curing and
[Combat basics](/playing/combat-basics/).

## How to train it

**No town trainer.** Poisoning has no standard NPC vendor that teaches it (only a Dryad
carries it), so train it by use from the start. The method: **apply a poison potion to a
weapon, food, or dart, repeatedly** — `Scripts/Skills/Poisoning.cs` runs
`CheckTargetSkill(SkillName.Poisoning, target, potion.MinPoisoningSkill,
potion.MaxPoisoningSkill)`, so the **potion tier sets the difficulty window**. Step the potion
up as your skill climbs:

- **Low skill (0–60)** — apply **lesser** poison potions; matched to skill 0.0–60.0.
- **Mid skill (30–70 / 60–100)** — **regular** then **greater** poison potions.
- **High skill (80–100)** — **deadly** poison potions for the steadiest late gains.

Keep a [potion](/skills/alchemy/) supply and a stack of weapons/food to envenom so a session
never stops; GGS guarantees the slow late points. See [skill gain](/mechanics/skill-gain/) and
[using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Assassin |
| Mastery skill | Yes |
| Gain notes | training Poisoning raises **Int** (primary), or **Dex** (secondary) — a popular fast Int-trainer; see [Stat gain](/mechanics/stat-gain/) |

Verified from ServUO. The check is `CheckTargetSkill(Poisoning, target, min, max)`
(`Scripts/Skills/Poisoning.cs`); the **potion you use sets the difficulty window** (next
section). A successful weapon application gives **`18 − (level × 2)` charges** (a weaker
poison yields more charges). On **failure** there is a **5% chance to poison yourself** below
80 skill.

## Poison types and their effects

Poison comes in five strength tiers, each stronger and longer-lasting than the last
(`Scripts/Misc/Poison.cs`, AOS values). The **potion** you apply determines the tier, and the
potion's skill window is what you train against:

| Poison | Apply with (potion) | Poisoning skill | Weapon charges | Strength |
|---|---|---|---|---|
| **Lesser** | Lesser Poison Potion | 0–60 | 18 | weakest — light damage over ~10 ticks |
| **Regular** | Poison Potion | 30–70 | 16 | moderate |
| **Greater** | Greater Poison Potion | 60–100 | 14 | strong |
| **Deadly** | Deadly Poison Potion | 80–100 | 12 | very strong — bigger ticks, ~15 ticks |
| **Lethal** | *(not craftable — high-end monsters only)* | — | 10 | strongest — hardest hits, up to ~20 ticks |

Higher tiers deal **more damage per tick, run for more ticks, and are harder to cure** (a
[Cure](/skills/magery/) spell or cure potion can fail outright against Deadly/Lethal). Damage
also scales with the victim — poison is brutal on low-HP targets and a steady drain on tough
ones. Charges count down per Infectious Strike; re-apply when they run out.

**Special poisons (Stygian Abyss):** two exotic potions exist at **95–100** Poisoning:

- **Darkglow Poison** — a Greater-tier venom that **reveals and lingers**, tuned to punish
  anyone who tries to out-wait it.
- **Parasitic Poison** — a Deadly-tier venom that **heals the attacker** for a share of the
  poison damage it deals — the assassin's life-leech.

The cure side (cure chances, *Lesser/Greater/Arch Cure*, cure potions) is covered on
[Poison & status](/playing/poison-and-status/).

## Related skills & synergies

- **[Fencing](/skills/fencing/) / a weapon skill** — poisoned blades + infectious strike.
- **[Alchemy](/skills/alchemy/)** — brews the poison potions you apply.
- **[Healing](/skills/healing/) / [Taste Identification](/skills/taste-identification/)** —
  cure poison / detect poisoned food.

## See also

- [Poison & status (how to play)](/playing/poison-and-status/)
- [Potions catalog](/items/catalog/potions/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
