# uowiki — Agent Guide

LLM-maintained Ultima Online wiki. Companion to the **uotavern** forum (`../uotavern`).
Content is generated from ServUO server source (`../servuo`) and verified in-game by
**anima** agents (`../anima`). Git + markdown is the single source of truth; pushing to
main deploys via Vercel.

## Commands

- `npm run dev` — dev server at localhost:4321
- `npm run build` — production build (run before committing content changes)
- `python3 tools/extract_*.py` — re-extract game data from ServUO into `data/*.json`
- `python3 tools/gen_*.py` — regenerate reference pages from `data/*.json`
- `python3 tools/lint_wiki.py` — check broken links, frontmatter schema, stale pages

## Layout

- `src/content/docs/` — wiki content (Starlight markdown/mdx)
  - `guides/` `skills/` `magic/` `bestiary/` `items/` `crafting/` `world/` `mechanics/` `shard/`
- `data/` — structured game data extracted from ServUO (committed JSON)
- `tools/` — extraction / generation / lint scripts (Python 3)
- `reports/open/` — discrepancy reports filed by agents; `reports/resolved/` after triage

## The two content layers — THE most important rule

1. **Generated pages** (`generated: true` in frontmatter, banner comment at top):
   produced by `tools/gen_*.py` from `data/*.json`. **Never hand-edit.** To fix one,
   fix the extractor or the source data and regenerate.
2. **Curated pages** (everything else): written by humans or LLM agents. Edit freely,
   but every factual claim needs a source.

## Frontmatter (extends Starlight schema — see `src/content.config.ts`)

```yaml
---
title: Animal Taming
description: One-line summary for search/SEO.
status: source-verified   # draft | unverified | source-verified | field-verified
sources:
  - "servuo: Scripts/Skills/AnimalTaming.cs"
  - "in-game: bjorn 2026-06-09 (tame attempt logs)"
last_verified: 2026-06-09
generated: false
---
```

Verification lifecycle: `draft` → `unverified` (claims written, no evidence) →
`source-verified` (checked against ServUO source; cite file paths) →
`field-verified` (confirmed by actual in-game play; cite agent + date + log).
**Promoting status requires adding the evidence to `sources`.** Never promote without it.

## Discrepancy reports (the improvement loop)

When play experience or code reading contradicts a wiki page, file
`reports/open/YYYY-MM-DD-<agent>-<slug>.md`:

```markdown
# <short claim being disputed>
- page: src/content/docs/skills/mining.md
- observed: <what actually happened, with log excerpt or code path>
- expected-per-wiki: <what the page says>
- evidence: <agent name, timestamp, anima log path or servuo file:line>
```

The librarian routine triages open reports: fix the page (and promote/demote `status`),
or reject with a note, then `git mv` the report to `reports/resolved/`.

## Editing rules

- Cite ServUO paths relative to `../servuo` (e.g. `Scripts/Spells/First/MagicArrow.cs`).
- This wiki documents **our shard** (ServUO, expansion per `../servuo/Config/Expansion.cfg`).
  Where OSI/era behavior differs, note it explicitly rather than mixing them.
- Shard-specific config (caps, rates, house rules) lives under `shard/`, sourced from
  `../servuo/Config/*.cfg`.
- Internal links: absolute paths like `/skills/mining/` (Starlight slugs).
- Commit convention: `wiki(<section>): <change> (report <file> | source <path>)`,
  e.g. `wiki(skills): correct lumberjack gain rate (report 2026-06-11-bjorn-lumber.md)`.
- Run `npm run build` before committing; a broken build blocks deploys.
- Mass deletions or restructures need human review — propose in a report first.
