---
title: Inscription
description: Scribe scrolls, spellbooks, and runebooks.
status: unverified
sources:
  - "servuo: Server/Skills.cs (SkillInfo 23)"
  - "servuo: Scripts/Skills/Inscribe.cs"
  - "servuo: Scripts/Services/Craft/DefInscription.cs"
  - "reference: uorenaissance.com skill list"
last_verified: 2026-06-11
generated: false
---

<img src="/img/skill-flags/23.gif" alt="Inscription skill banner" width="160" />

Inscription is the scribe's [crafting skill](/playing/crafting/). The prose is
community-derived (paraphrased from the uorenaissance.com skill list plus ServUO behavior)
pending field verification; the stats table is source-verified against ServUO.

## What it does

Inscription writes [Magery](/skills/magery/) spell scrolls from reagents and mana, and crafts
spellbooks, runebooks, and (in expansion content) some spell-school books. Scribed scrolls
are a steady gold earner, and on a caster high Inscription adds a small **spell-damage bonus**
to Magery, which is why it appears on Pure Mage templates.

## How to use it

Have a spellbook with the spell, the required reagents, and the mana, then use a scribe's pen
to inscribe the scroll. For spellbooks/runebooks, use the pen on the blank book material. See
[crafting](/playing/crafting/), [spellcasting](/playing/spellcasting/), and
[reagents](/items/reagents/).

## How to train it

- **Low skill** — scribe low-circle scrolls (circle 1–2); cheap reagents.
- **Mid/high skill** — work up to the highest-circle scrolls you can cast; these give the
  steadiest gains and the best resale.

Recipe thresholds live in `Scripts/Services/Craft/DefInscription.cs`. See
[skill gain](/mechanics/skill-gain/).

## Mechanics & numbers

| | |
|---|---|
| Primary stat | Intelligence |
| Secondary stat | Dexterity |
| Title | Scribe |
| Mastery skill | No |
| Gain notes | skill-ups can raise Dex +0.2, Int +0.8 (per-use stat gain weights) |

Inscription requires the spell to be in your book and consumes the same reagents as casting
it. The Magery spell-damage bonus from high Inscription is applied in the spell damage math;
exact magnitude is **unverified** here.

## Related skills & synergies

- **[Magery](/skills/magery/) + [Evaluating Intelligence](/skills/evaluating-intelligence/)**
  — Inscription's damage bonus stacks on the mage core; see the Pure Mage build on
  [seven-GM templates](/templates/seven-gm/) and the [Mage template](/templates/mage/).
- **[Alchemy](/skills/alchemy/)** — the sister reagent craft.

## See also

- [Crafting (how to play)](/playing/crafting/) · [Inscription crafting](/crafting/inscription/)
- [Reagents](/items/reagents/) · [Scrolls catalog](/items/catalog/scrolls/)
- [Skill gain](/mechanics/skill-gain/) · [Skills index](/skills/)

Banner icon courtesy of [uorenaissance.com](https://www.uorenaissance.com/).
