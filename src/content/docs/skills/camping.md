---
title: Camping
description: Pitch a campfire to log out safely in the wild.
status: source-verified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 10, Camping)"
  - "servuo: Scripts/Items/Consumables/Kindling.cs"
  - "servuo: Scripts/Items/Functional/Campfire.cs"
  - "servuo: Scripts/Mobiles/NPCs/Provisioner.cs"
last_verified: 2026-06-22
generated: false
---

<img src="/img/skill-flags/10.gif" alt="Camping skill banner" width="160" />

Camping lets you light a campfire to rest and log out safely away from town. The stats table,
trainers, and campfire mechanics below are source-verified against ServUO; the general
training advice is community guidance pending field verification.

## What it does

Camping turns kindling into a campfire. Once the fire settles you gain a safe place to log
out in the wilderness (avoiding the normal grace-period vulnerability) and can rest. It is a
minor convenience/survival skill favored by explorers and travelers who roam far from a city.

## How to use it

Carry kindling (chop logs into kindling, or buy it), then use it to attempt a campfire. After
the fire is established you can safely log out near it or rest. See
[movement & travel](/playing/movement-and-travel/) and
[world & time](/playing/world-and-time/).

## How to train it

**Quick start:** several NPCs carry the Camping skill and so teach it up to **one-third of
their own skill, capped at 42.0** (`Scripts/Mobiles/Normal/BaseCreature.cs`, `CheckTeachSkills`:
`baseToSet = ourSkill.BaseFixedPoint / 3`). Trainers include the **Provisioner** (a common town
vendor, Camping 45–68), **Ranger** and **Furtrader** (55–78), **Ranger Guildmaster** (75–98),
and **Wandering Healers** (80–100) — see their `SetSkill(SkillName.Camping, …)` lines. So
buying to ~30–42 first is easy. After that the method is: **make kindling, then light a
campfire, repeatedly.**

- **Low/high skill** — chop a log into kindling (or buy kindling) and Use it to pitch a
  campfire, over and over. Each ignite rolls `CheckSkill(Camping, 0.0, 100.0)`, so it gains
  across its whole range. It is a slow, low-stakes skill; just keep pitching camps in a loop
  and let GGS carry the slow points.

See [skill gain](/mechanics/skill-gain/) and [using & training skills](/playing/using-and-training-skills/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Dexterity |
| Secondary stat | Intelligence |
| Title | Explorer |
| Mastery skill | No |
| Gain notes | skill-ups can raise Str +2, Dex +1.5, Int +1.5 (per-use stat gain weights) |

Camping is a niche utility skill; the safe-logout benefit is its main draw. The verified
specifics, from `Scripts/Items/Consumables/Kindling.cs` and `Scripts/Items/Functional/Campfire.cs`:

- Igniting kindling rolls `CheckSkill(Camping, 0.0, 100.0)`; on failure you get "You fail to
  ignite the campfire."
- **You cannot light a campfire inside a dungeon region** ("There is not a spot nearby to
  place your campfire").
- A lit campfire **secures after you stand within 7 tiles of it for 30 seconds** ("The camp is
  now secure"). The fire then begins extinguishing at 60 seconds and is gone by ~100 seconds,
  so the secure window is short.

## Related skills & synergies

- **[Lumberjacking](/skills/lumberjacking/)** — chop logs into the kindling camping needs.
- **[Tracking](/skills/tracking/) / [Cartography](/skills/cartography/)** — round out an
  explorer/treasure-hunter who lives in the wild.

## See also

- [Movement & travel](/playing/movement-and-travel/)
- [World & time](/playing/world-and-time/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
