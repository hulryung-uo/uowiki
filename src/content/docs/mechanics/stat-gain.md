---
title: Stat Gain
description: How Strength, Dexterity, and Intelligence grow from skill use — chances, primary/secondary stats, and the 225 cap.
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs (TryStatGain, IncreaseStat, CheckStatTimer)"
  - "servuo: Server/Skills.cs (SkillInfo primary/secondary stats)"
  - "servuo: Config/PlayerCaps.cfg"
last_verified: 2026-06-11
generated: false
---

Muscles grow by swinging hammers, minds by reading scrolls — and both are governed by
`Scripts/Misc/SkillCheck.cs`.

## When stats gain

Stat gain piggybacks on **skill use**: whenever a skill with lock set to *up* processes a gain
event, `TryStatGain` runs. On this EJ shard the modern (ML-era) path is used.

1. **Chance roll:** **5%** for players (`PlayerChanceToGainStats=5.0` in
   `Config/PlayerCaps.cfg`); also 5% for pets (`PetChanceToGainStats=5.0`).
2. **Stat selection:** every skill defines a **primary** and **secondary** stat in the
   `SkillInfo` table (`Server/Skills.cs`). If both stats are set to *up*:
   - **3/4 chance** the primary stat gains,
   - **1/4 chance** the secondary gains.
   If only one is set to *up*, that one gains. If neither, nothing happens.
3. **Timer check:** the per-stat gain delay is **disabled** on this shard
   (`EnablePlayerStatTimeDelay=False`), which the code collapses to an effective 0.5-second
   cooldown per stat — in practice, no throttle.

Examples of primary/secondary pairs (from `Server/Skills.cs`):

| Skill | Primary | Secondary |
|-------|---------|-----------|
| Swordsmanship, Blacksmithy, Mining, Lumberjacking, Tactics | Str | Dex |
| Magery, Evaluating Intelligence, Meditation | Int | Str |
| Healing, Veterinary | Int | Dex |
| Hiding, Fencing, Snooping | Dex | (Int / Str) |
| Animal Taming | Str | Int |

So a smith bulks up, a mage gets clever, and a tamer somehow gets both.

### Note on StrGain/DexGain/IntGain factors

`SkillInfo` also carries per-skill `StrGain`/`DexGain`/`IntGain` values (e.g. Blacksmithy
1.0/0.0/0.0, Magery 0.0/0.0/1.5). These drive the **pre-ML** gain path
(`(info.StrGain / 33.3) > random`), which is *not* used on this EJ shard — here only the
primary/secondary designation and the flat 5% roll matter.

## Caps and the swap rule

From `Config/PlayerCaps.cfg` (see [the shard card](/shard/)):

- Per-stat cap: **125** (`StrCap`/`DexCap`/`IntCap`), enhanceable to **150**
  (`StrMaxCap` etc. — e.g. via stat-boosting items).
- Total stat cap: **225** (`TotalStatCap`).

When your three raw stats already total 225, `IncreaseStat` performs a **swap**: the gaining
stat goes up by 1 only if another stat is set to *down* and can afford to drop (it must stay
above 10). The lower of the two eligible down-stats is reduced first. With no stat set to
*down*, you gain nothing at the cap — so set your stat arrows, not just your skill arrows.

## Practical training notes

- Train skills whose **primary stat** is the one you want: chopping wood
  ([Lumberjacking](/skills/lumberjacking/)) for Str, casting ([Magery](/skills/magery/))
  for Int.
- Because the chance is flat 5% per skill-gain event, **fast-gaining skills also train stats
  fastest** — low-level skills below 10.0 gain on every use and pull stats along.
- Stat lock arrows are independent of skill locks; check both in your skills gump.

## Related

- [Skill gain](/mechanics/skill-gain/) — the events that trigger stat rolls
- [Skills index](/skills/) — primary stats for every skill
