---
title: "7x GM Templates"
description: The classic Ultima Online endgame — seven skills at Grandmaster (100.0 each) inside the 700.0 total cap, organized by purpose with strengths, weaknesses, and stat notes.
status: source-verified
sources:
  - "servuo: Config/PlayerCaps.cfg (TotalSkillCap=7000 → 700.0; SkillCap=1000 → 100.0 per skill; TotalStatCap=225)"
  - "servuo: Server/Skills.cs (m_Table — every named skill exists)"
  - "reference: classic UO template conventions"
  - "general UO community build knowledge"
last_verified: 2026-06-22
generated: false
---

:::note[Community build wisdom]
The skill mechanics cited here (the 700.0 cap, per-skill 100.0 cap, gain behavior) are
source-verified against this shard's [configuration](/shard/) and
[skill gain](/mechanics/skill-gain/). The *templates themselves* are classic UO community
conventions adapted to this server — proven shapes, not field-verified routes. File
discrepancies per [wiki conventions](/guides/wiki-conventions/).
:::

## The 700.0 cap and what "7x GM" means

On this shard your character has a **700.0 total skill cap** and every individual skill caps
at **100.0** — see the [shard summary](/shard/) and [skill gain](/mechanics/skill-gain/).
"Grandmaster" (GM) is the title you earn at 100.0 in a skill. Seven skills × 100.0 = **700.0**,
exactly the total cap. That is the whole idea behind a **7x GM** (also written **7-GM**)
template: pick the seven skills you want at the ceiling, and you have spent your entire skill
budget. Push an eighth skill up and the server forces an equal amount *down* somewhere else —
the cap is a hard wall, not a suggestion.

Because you only get seven slots, you do not choose skills at random — you choose a template
for a **PURPOSE**: what you want to be able to *do*. The common purposes are:

- **Melee** — hit things with a weapon and survive (a "dexxer").
- **Cast** — sling spells for damage and utility (a mage).
- **Tame** — command powerful pets to fight for you.
- **Support / crowd control** — bards who charm, calm, or weaken whole rooms.
- **Stealth** — strike from hiding and vanish.
- **Craft** — produce gear, tools, and consumables.

Stats matter just as much as skills. Your three attributes (STR/DEX/INT) share a separate
**225 total cap**, and how you split them shapes the same seven skills into very different
characters — see [character & stats](/playing/character-and-stats/). Each template below
includes a suggested stat lean.

## How to read a template

Every build below lists:

- **The 7 skills** — each linked to its [skill page](/skills/) for the exact mechanics.
- **Purpose / What it does** — the role and the win condition (how the build actually wins a
  fight or accomplishes its job).
- **Strengths / Weaknesses** — what it is great at and where it falls apart.
- **Suggested stats** — a STR/DEX/INT lean within the 225 cap.

Cross-reference the How-to-Play guides as you read: [combat basics](/playing/combat-basics/),
[spellcasting](/playing/spellcasting/), [meditation & mana](/playing/meditation-and-mana/),
[taming & pets](/playing/taming-and-pets/), [crafting](/playing/crafting/),
[hiding & stealth](/playing/hiding-and-stealth/), and
[notoriety & PvP](/playing/notoriety-and-pvp/). Several of these archetypes also have
dedicated walkthrough pages: [Warrior](/templates/warrior/), [Mage](/templates/mage/),
[Animal Tamer](/templates/animal-tamer/), [Blacksmith](/templates/blacksmith/), and
[Lumberjack](/templates/lumberjack/).

## Sword Dexxer

**Skills:** [Swordsmanship](/skills/swordsmanship/), [Tactics](/skills/tactics/),
[Anatomy](/skills/anatomy/), [Healing](/skills/healing/),
[Resisting Spells](/skills/resisting-spells/), [Magery](/skills/magery/),
[Meditation](/skills/meditation/).

**Purpose / What it does:** The bread-and-butter melee build. Swordsmanship is your weapon
skill, Tactics and Anatomy multiply your damage, and Healing turns bandages into a renewable
health bar (and, at high Anatomy/Healing, a self-resurrection). Resisting Spells blunts enemy
magic. Magery and Meditation are *utility*, not your damage: Recall and Gate for travel,
Greater Heal and Cure to back up bandages, and Meditation to refund the mana. Its win
condition is attrition — out-heal the incoming damage and grind the target down. See
[combat basics](/playing/combat-basics/).

**Strengths:** Cheap to run (bandages, not reagents), forgiving, self-sufficient, mobile
thanks to Recall. Excellent solo PvM.

**Weaknesses:** Limited burst — you win slowly. Split focus means your Magery is weak
offensively, and you have no crowd control.

**Suggested stats:** ~100 STR / ~90 DEX / ~35 INT. STR is hit points and damage, DEX drives
swing and bandage speed; keep INT just high enough to cast utility spells.

**Variations:**

- **Mace / Fencing / Archery dexxer** — swap [Swordsmanship](/skills/swordsmanship/) for
  [Mace Fighting](/skills/mace-fighting/), [Fencing](/skills/fencing/), or
  [Archery](/skills/archery/). Mace ignores some armor and can stun; Fencing is fast and can
  poison; Archery fights at range. The other six skills are unchanged.
- **Parry-dexxer** — drop a caster skill (usually Meditation, sometimes Magery) for
  [Parrying](/skills/parrying/) to block a share of incoming blows with a shield. Trades
  self-cast utility for raw defense.

## Pure Mage

**Skills:** [Magery](/skills/magery/), [Evaluating Intelligence](/skills/evaluating-intelligence/),
[Meditation](/skills/meditation/), [Wrestling](/skills/wrestling/),
[Resisting Spells](/skills/resisting-spells/), [Inscription](/skills/inscription/), plus a
**flex** slot (commonly [Anatomy](/skills/anatomy/) or a bard skill).

**Purpose / What it does:** The glass-cannon caster. Magery is everything you do; Eval Int
raises spell damage; Meditation refills your mana fast so you can keep casting; Inscription
adds a spell-damage bonus and lets you scribe your own scrolls. Resisting Spells protects you
in mage-vs-mage fights. [Wrestling](/skills/wrestling/) is your **unarmed defense** — with no
weapon skill, GM Wrestling keeps you from getting interrupted and lets you land a disarming
or paralyzing blow. The win condition is burst: stack Eval-boosted spells (Explosion +
Energy Bolt combos, Flamestrike) faster than the target can heal. See
[spellcasting](/playing/spellcasting/) and [meditation & mana](/playing/meditation-and-mana/).

**Strengths:** Highest burst damage, total mobility (Recall/Gate), ranged, flexible utility
(Cure, Bless, Reveal, Invisibility, fields).

**Weaknesses:** Fragile — low hit points, dies fast if a melee target closes in. Reagent
costs add up. Vulnerable while a spell is "casting up."

**Suggested stats:** ~25 STR / ~10 DEX / ~100 INT (INT is your mana pool). Pump INT to the
ceiling; a little STR for survivability.

## Tank Mage

**Skills:** [Magery](/skills/magery/), [Evaluating Intelligence](/skills/evaluating-intelligence/),
[Meditation](/skills/meditation/), [Resisting Spells](/skills/resisting-spells/),
[Wrestling](/skills/wrestling/), [Tactics](/skills/tactics/), [Anatomy](/skills/anatomy/).

**Purpose / What it does:** The classic PvP hybrid — it **fights in melee and casts at the
same time**. Wrestling, Tactics, and Anatomy make your fists a real weapon, so you can punch
*and* cast without ever drawing a weapon (no fumbling to re-arm). Magery/Eval/Med deliver the
nuke and the heals; Resist keeps you standing in caster duels. The win condition is pressure
from two directions: keep hitting in melee to interrupt the enemy while landing spell combos.
See [notoriety & PvP](/playing/notoriety-and-pvp/).

**Strengths:** Hard to interrupt, durable for a caster, dangerous at every range, no weapon
to drop or lose.

**Weaknesses:** Lower spell damage than a Pure Mage (no Inscription bonus), lower melee
damage than a dexxer. Master-of-none if played passively — it rewards aggression.

**Suggested stats:** ~75 STR / ~35 DEX / ~115 INT, balanced for hit points, mana, and a
workable punch.

## Animal Tamer

**Skills:** [Animal Taming](/skills/animal-taming/), [Animal Lore](/skills/animal-lore/),
[Veterinary](/skills/veterinary/), [Magery](/skills/magery/), [Meditation](/skills/meditation/),
plus two of [Evaluating Intelligence](/skills/evaluating-intelligence/) /
[Resisting Spells](/skills/resisting-spells/) (one is the **flex** slot).

**Purpose / What it does:** You don't fight — your **pet** does. Animal Taming lets you charm
strong creatures, Animal Lore is required to tame and command the best of them, and Veterinary
keeps the pet alive with bandages and cures. Magery/Meditation give you Recall mobility, heals
to back up Vet, and Greater Heal on the pet. The win condition is a powerful tamed creature
(dragons, the strongest pets) doing the killing while you stay back and support. Full
walkthrough on the [Animal Tamer template](/templates/animal-tamer/); mechanics on
[taming & pets](/playing/taming-and-pets/).

**Strengths:** Highest sustained killing power in PvM — a top-tier pet out-damages most solo
builds. Safe playstyle (you stand back). Two characters in one (you + pet).

**Weaknesses:** Pet management is logistics — stabling, feeding, control chances, and the
risk of losing an expensive pet. Weak personally if the pet dies or is lured away.

**Suggested stats:** ~30 STR / ~20 DEX / ~100+ INT — you are effectively a support caster, so
INT (mana) leads.

## Bard

**Skills:** [Musicianship](/skills/musicianship/) plus two or three of
[Provocation](/skills/provocation/) / [Peacemaking](/skills/peacemaking/) /
[Discordance](/skills/discordance/), rounded out with [Magery](/skills/magery/),
[Meditation](/skills/meditation/), and [Resisting Spells](/skills/resisting-spells/).

**Purpose / What it does:** Crowd control and support. **Musicianship** is the gate — every
bard ability requires an instrument and a successful Musicianship check. The three song skills
each do something different:

- **[Provocation](/skills/provocation/)** — turn two monsters against each other so they fight
  *for* you. A provoker can clear a room without taking a hit.
- **[Peacemaking](/skills/peacemaking/)** — calm a target (or an area) so it stops fighting,
  letting you reset a bad pull or escape.
- **[Discordance](/skills/discordance/)** — debuff a target's skills and stats, making
  everything else (your pet, your party, your own attacks) hit harder.

Magery/Med/Resist give the bard mobility, heals, and caster defense. The win condition is
**control**: you decide who fights whom, who fights at all, and how weak they are while doing
it. Many bards pair their songs with a weapon or a pet for the actual killing.

**Strengths:** Unmatched crowd control, can handle groups that overwhelm a solo dexxer,
strong in groups, force-multiplies any party.

**Weaknesses:** Low personal damage — a pure bard kills slowly. Songs can fail against
high-level or "song-immune" creatures, and instruments wear out.

**Suggested stats:** ~25 STR / ~10 DEX / ~100 INT, leaning caster since you cast and meditate
between songs.

## Stealth Archer / Scout

**Skills:** [Archery](/skills/archery/), [Tactics](/skills/tactics/),
[Anatomy](/skills/anatomy/), [Healing](/skills/healing/), [Hiding](/skills/hiding/),
[Stealth](/skills/stealth/), plus a **flex** slot (often
[Resisting Spells](/skills/resisting-spells/) or [Magery](/skills/magery/)).

**Purpose / What it does:** Hit-and-vanish. Archery delivers ranged damage; Tactics and
Anatomy boost it; Healing patches you up. The signature is the stealth pair:
[Hiding](/skills/hiding/) drops you off the screen and [Stealth](/skills/stealth/) lets you
*move while hidden*. You creep up, open with a heavy ranged shot, and slip back into hiding
before the target reaches you. The win condition is initiative and positioning — you choose
when the fight starts and can always disengage. See [hiding & stealth](/playing/hiding-and-stealth/).

**Strengths:** Controls engagement range, excellent for scouting and ambush, strong escape
tools, deadly opening burst.

**Weaknesses:** Frail in a stand-up melee, depends on terrain and line of sight, ammunition
logistics (arrows), and re-hiding can fail when enemies are close.

**Suggested stats:** ~90 STR / ~100 DEX / ~35 INT. DEX drives bow speed; STR for survivability.

## Thief / Rogue

**Skills:** [Stealing](/skills/stealing/), [Snooping](/skills/snooping/),
[Hiding](/skills/hiding/), [Stealth](/skills/stealth/), [Lockpicking](/skills/lockpicking/),
plus two **utility** skills (commonly [Detecting Hidden](/skills/detecting-hidden/),
[Tactics](/skills/tactics/) for a backup weapon, [Magery](/skills/magery/), or
[Resisting Spells](/skills/resisting-spells/)).

**Purpose / What it does:** Larceny and infiltration. **Snooping** peeks inside another
player's pack so you know what is worth taking; **Stealing** lifts it. Hiding and Stealth get
you in and out unseen; Lockpicking opens chests (and disarms the path to loot). The win
condition is the score, not the kill — you take what others earned and disappear. This is a
PvP/interaction-driven playstyle; understand the rules first on
[notoriety & PvP](/playing/notoriety-and-pvp/).

**Strengths:** Unique playstyle, can profit without ever winning a fight, strong stealth and
escape kit, opens locked content.

**Weaknesses:** Little to no combat power on its own, high-risk (getting caught makes you a
target), and effectiveness depends heavily on the shard's theft rules.

**Suggested stats:** ~40 STR / ~80 DEX / ~25 INT — DEX for stealing/escape speed and a light
weapon if you carry one.

## Crafter (Smith / Tailor)

**Skills:** [Blacksmithy](/skills/blacksmithy/), [Mining](/skills/mining/),
[Tinkering](/skills/tinkering/), [Tailoring](/skills/tailoring/),
[Carpentry](/skills/carpentry/), [Arms Lore](/skills/arms-lore/), plus a **flex** slot
(often [Magery](/skills/magery/) for travel or
[Lumberjacking](/skills/lumberjacking/) / [Fishing](/skills/fishing/) for materials).

**Purpose / What it does:** Production. This build *makes* the gear everyone else buys —
weapons and armor (Blacksmithy), clothing and leather armor (Tailoring), furniture, bows, and
houses (Carpentry), tools and useful gadgets (Tinkering). Mining feeds the forge with ore;
Arms Lore raises the quality of crafted weapons and armor. The win condition is economic: a
GM crafter is a shop. See [crafting](/playing/crafting/) and
[gathering resources](/playing/gathering-resources/); full route on the
[Blacksmith template](/templates/blacksmith/).

**Strengths:** Makes money and gear indefinitely, never short on consumables, valuable to a
guild, low combat risk.

**Weaknesses:** **Almost no combat ability.** This is the clearest example of the 700 cap as
a forcing function: a 7x crafter has spent all seven slots on production, so it *cannot* also
be a 7x fighter. Most players run a crafter as a **separate character**.

**Suggested stats:** ~100 STR / ~25 DEX / ~100 INT. STR raises mining yield and crafting
success on some recipes; INT supports a Magery flex.

## Necro-Mage / Spellweaver / Mystic

**Skills:** a modern caster school —
[Necromancy](/skills/necromancy/) (+[Spirit Speak](/skills/spirit-speak/)),
[Spellweaving](/skills/spellweaving/) (+[Focus](/skills/focus/)), or
[Mysticism](/skills/mysticism/) (+[Focus](/skills/focus/)) — combined with
[Magery](/skills/magery/), [Evaluating Intelligence](/skills/evaluating-intelligence/),
[Meditation](/skills/meditation/), [Resisting Spells](/skills/resisting-spells/), and
[Wrestling](/skills/wrestling/).

**Purpose / What it does:** Expansion-era hybrid casters that bolt a second spell school onto
a Magery core. A **Necro-mage** adds curses, summons, and life-drain (Spirit Speak amplifies
necro effects); a **Spellweaver** adds Arcane focus, summons, and area buffs; a **Mystic** adds
its own elemental and summoning lines (Focus powers both Spellweaving and Mysticism). The win
condition is the same as a mage's burst — but with extra debuffs, summons, and damage types to
work around resistances. These are briefer here because they are **expansion-era** content;
see [magic schools](/playing/magic-schools/) for which schools this shard runs and how they
interact.

**Strengths:** Versatile damage types and debuffs, summons as disposable allies, strong PvM
and PvP flexibility.

**Weaknesses:** Reagent- and resource-hungry, more complex to play, and availability depends
entirely on the shard's [expansion](/shard/) settings — confirm the school exists here before
committing.

**Suggested stats:** ~30 STR / ~10 DEX / ~110 INT — pure caster lean, like the Pure Mage.

## The 700 cap as a forcing function

The cap is the design of the game, not a limitation to fight. **You cannot do everything.**
Seven slots means every build is a set of deliberate trade-offs:

- **Hybrids trade depth for breadth.** A Tank Mage fights *and* casts, but it nukes worse than
  a Pure Mage and hits worse than a dexxer. A Parry-dexxer gains a shield by giving up
  self-cast utility. Each "and" you add costs an "as well as."
- **Some purposes simply don't share a character.** A 7x crafter and a 7x fighter both want all
  seven slots — you can't be both. This is why most players keep **multiple characters**: a
  combat main and a crafter (and maybe a tamer, a bard, and a thief) on the same account.
- **The cap also enforces choices within a role.** A mage who wants Inscription's damage bonus
  gives up a slot a bard skill or Anatomy could have used. There is always an opportunity cost.

:::caution[Skill scrolls / power scrolls — unverified for this shard]
On some shards, **Power Scrolls** (and similar skill scrolls) raise an *individual* skill's cap
above 100.0 — and on some they also raise the total budget, which would change the entire
7×100 math. **Whether any such items exist on this shard, and what they do, is unverified
here.** Treat the 700.0 total / 100.0-per-skill model above as the baseline until confirmed
against this server's [configuration](/shard/) and [skill gain](/mechanics/skill-gain/) rules.
:::

## See also

- [Skill gain mechanics](/mechanics/skill-gain/) — how skills rise and what the cap does at 700.
- [Character & stats](/playing/character-and-stats/) — the separate 225 stat cap.
- [Shard summary](/shard/) — this server's caps and expansion at a glance.
- Walkthrough templates: [Warrior](/templates/warrior/), [Mage](/templates/mage/),
  [Animal Tamer](/templates/animal-tamer/), [Blacksmith](/templates/blacksmith/),
  [Lumberjack](/templates/lumberjack/).
- [All skills](/skills/) — every skill, with the exact mechanics each template depends on.
