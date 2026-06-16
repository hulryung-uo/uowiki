---
title: Stat Gain
description: How Strength, Dexterity, and Intelligence grow from skill use — chances, primary/secondary stats, and the 225 cap.
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs (TryStatGain, IncreaseStat, CheckStatTimer)"
  - "servuo: Server/Skills.cs (SkillInfo primary/secondary stats)"
  - "servuo: Config/PlayerCaps.cfg"
  - "servuo: Server/Skills.cs (per-skill Primary/Secondary StatCode — Snooping primary Dex, etc.)"
last_verified: 2026-06-16
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

## Fast-training one stat (the "spam a skill" trick)

Because stat gain rides on the **primary stat** of whatever skill is gaining, you can pump a
single stat fast by spamming a cheap, fast-gaining skill tied to it. The recipe:

1. **Set the stat arrows.** In your skills/status gump, set the stat you want to **Up** and
   set the other two to **Down** (or *Locked*). This guarantees every successful roll lands on
   your target stat, and — once you're at the 225 total cap — lets the target keep rising by
   swapping points out of a *Down* stat.
2. **Pick a skill whose *primary* stat is your target** (table below).
3. **Spam it.** A skill still climbing (especially below ~70) gains on a large fraction of
   uses, and each gain rolls the flat **5%** stat chance. With the stat-gain timer disabled on
   this shard, those rolls aren't throttled — so the stat climbs quickly.

**The classic example: Dexterity via [Snooping](/skills/snooping/).** Snooping's primary stat
is **Dex**, and you can snoop the same container (a pack animal, a co-operative friend, any
container) over and over with almost no setup — so it's the go-to "just raise my Dex" skill.
Set Dex *Up*, Str/Int *Down*, and snoop repeatedly.

**The Intelligence equivalent: [Poisoning](/skills/poisoning/).** Poisoning's primary stat is
**Int**, and it's wonderfully spammable — keep a stack of cheap **Lesser poison potions** and
apply them to food or an Infectious-Strike weapon over and over (each application is a skill
check that rolls the stat chance). Set Int *Up*, Str/Dex *Down*, and envenom repeatedly. It
raises Poisoning *and* Int together, which is why it's a favorite Int-pump. (Heads-up:
applying poison costs karma, and a failed attempt under 80 skill can poison you — see
[Poisoning](/skills/poisoning/).)

**Best spam-trainers by stat** (primary-stat skills; pick whichever you can repeat fastest):

| Target | Primary-stat skills to spam | Easy choice |
|---|---|---|
| **Dexterity** | Snooping, [Stealing](/skills/stealing/), [Lockpicking](/skills/lockpicking/), [Hiding](/skills/hiding/), [Stealth](/skills/stealth/), [Tailoring](/skills/tailoring/), [Tinkering](/skills/tinkering/), Musicianship | **Snooping** (or Hiding) |
| **Strength** | [Mining](/skills/mining/), [Lumberjacking](/skills/lumberjacking/), [Blacksmithy](/skills/blacksmithy/), [Carpentry](/skills/carpentry/), [Tactics](/skills/tactics/) | **Mining** (dig nonstop) |
| **Intelligence** | [Magery](/skills/magery/), [Meditation](/skills/meditation/), [Evaluating Intelligence](/skills/evaluating-intelligence/), [Poisoning](/skills/poisoning/), [Inscription](/skills/inscription/), [Alchemy](/skills/alchemy/) | **Poisoning** / Meditation |

Caveats: a stat can't pass **125** (or 150 enhanced), and you can't exceed **225 total** unless
a *Down* stat has room to drop (above 10) — that's why step 1 sets the other stats *Down*. And
the skill itself must still be **gaining** (a maxed skill stops rolling); a low or mid skill
you're actively raising is what feeds the stat.

## Practical training notes

- Two birds, one stone: training a skill you *want* also pulls its primary stat along — a
  warrior swinging weapons ([Tactics](/skills/tactics/) → Str) or a mage casting
  ([Magery](/skills/magery/) → Int) raises the right stat naturally without a dedicated
  grind.
- **Fast-gaining skills train stats fastest** — the 5% roll fires per skill-gain event, so a
  skill that gains often (low/mid level) pulls stats faster than a near-maxed one.
- **Stat lock arrows are independent of skill locks** — check both in your status/skills
  gump. A stat left *Locked* never moves no matter what you train.

## Related

- [Skill gain](/mechanics/skill-gain/) — the events that trigger stat rolls
- [Skills index](/skills/) — primary stats for every skill
