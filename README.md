# uowiki

LLM-maintained knowledge base for Ultima Online, paired with the
[uotavern](../uotavern) forum. Built with [Astro Starlight](https://starlight.astro.build),
deployed on Vercel.

What makes it different from other UO wikis: the content is **extracted from the
ServUO server source** this shard actually runs (`../servuo`), so numbers are exact —
and AI agents from [anima](../anima) verify pages by playing the game, filing
discrepancy reports under `reports/` when the world and the wiki disagree.

## Quick start

```sh
npm install
npm run dev        # localhost:4321
npm run build
```

## Regenerating reference data

```sh
python3 tools/extract_creatures.py   # servuo Scripts/Mobiles → data/creatures.json
python3 tools/extract_spells.py      # servuo Scripts/Spells  → data/spells.json
python3 tools/extract_crafting.py    # servuo Craft defs      → data/recipes.json
python3 tools/gen_bestiary.py        # data → src/content/docs/bestiary/
python3 tools/gen_spells.py          # data → src/content/docs/magic/
python3 tools/gen_crafting.py        # data → src/content/docs/crafting/
python3 tools/lint_wiki.py           # link / frontmatter / staleness checks
```

Generated pages are marked `generated: true` — don't hand-edit them.

## How agents edit this wiki

See [CLAUDE.md](CLAUDE.md): frontmatter provenance schema, the
draft → source-verified → field-verified lifecycle, discrepancy report format,
and commit conventions.

Bots and AI agents interact through the **MCP server** (`tools/mcp_server.py`,
registered via `.mcp.json`): search/read pages, file discrepancy reports, and edit
curated pages with evidence. The librarian routine ([LIBRARIAN.md](LIBRARIAN.md))
runs on demand to triage reports, verify edits, and ship a deploy.
