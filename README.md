# uowiki

**A living, LLM-maintained knowledge base for Ultima Online.** Companion to the
[uotavern](../uotavern) forum, built with [Astro Starlight](https://starlight.astro.build)
and deployed on Vercel → **https://uowiki.vercel.app**

What makes it different from every other UO wiki: the content is **extracted directly
from the source of the ServUO server emulator** this shard runs on (`../servuo`) and the client
art files (`../uo-resource`), so the numbers and pictures are exact — not OSI lore or
guesswork. AI agents from [anima](../anima) then verify pages by *playing the game*,
filing discrepancy reports when the world and the wiki disagree.

## What's inside

- **Bestiary** — 562 creatures with stats, resistances, loot, taming difficulty, an
  animated sprite (GIF), and the creature's actual sounds.
- **Magic** — all 64 Magery spells with reagents, mana, skill windows, and icons.
- **Crafting** — every recipe the server knows (~1,200), with materials, skill ranges,
  item pictures, and the expansion each recipe was introduced in.
- **Item catalog** — all ~3,700 items, classified by gameplay type (Weapons by family
  and skill, Armor by material, Shields, Jewelry, Clothing, Potions, Scrolls, …), each
  with its client sprite. Colored variants (the nine metal ingots, leathers, scales,
  dyed clothing) are shown in their real [UO hue](src/content/docs/reference/hues.md).
- **World** — cities, dungeons, moongates and shrines with annotated region maps and
  deep links into the interactive [uomap](../uomap).
- **Skills, Mechanics, Character Templates, Our Shard** — curated, source-cited guides:
  skill-gain formulas, character creation, build-and-progression storylines.
- **Recent Changes** — a reader-facing changelog generated from git history.

## How it stays correct

Every page carries provenance frontmatter:

```yaml
status: source-verified   # draft → unverified → source-verified → field-verified
sources: ["servuo: Scripts/Skills/AnimalTaming.cs", "in-game: bjorn 2026-06-09"]
last_verified: 2026-06-11
```

Content is two layers: **generated** reference pages (rebuilt from `data/*.json` — never
hand-edited) and **curated** guides (written by humans/agents, every claim cited). When
play contradicts a page, an agent files a report in `reports/open/`; the
[librarian routine](LIBRARIAN.md) triages it into a fix. See [CLAUDE.md](CLAUDE.md) for
the full editing rules, report format, and commit conventions.

## Quick start

```sh
npm install
npm run dev        # localhost:4321
npm run build      # production build (run before committing)
```

Deploy: `vercel --prod --yes --archive=tgz` (the `--archive=tgz` flag is required — the
plain upload aborts on the ~2,000 media asset files under `public/`).

## Regenerating reference data

The data pipeline turns server source + client files into JSON, then into pages.
Run it top-to-bottom; order matters for the item art steps:

```sh
# --- extract: servuo source → structured JSON ---
python3 tools/extract_creatures.py    # Scripts/Mobiles      → data/creatures.json
python3 tools/extract_spells.py       # Scripts/Spells       → data/spells.json
python3 tools/extract_skills.py       # Server/Skills.cs     → data/skills.json
python3 tools/extract_crafting.py     # Craft Def*.cs        → data/recipes.json
python3 tools/extract_items.py        # all item classes     → data/items.json (+ item PNGs)
python3 tools/extract_expansion.py    # Craft Core.X gates   → data/item_expansion.json

# --- item art post-processing (order matters) ---
python3 tools/trim_item_art.py        # crop transparent padding off item PNGs
python3 tools/apply_hues.py           # bake UO hues onto colored variants (ingots, leather, …)

# --- client asset extraction (uo-resource .uop/.mul → public/img, public/audio) ---
python3 tools/uoplib.py --probe       # UOP container reader (shared lib; CLI for inspection)
python3 tools/extract_art.py          # item sprites      → public/img/items/
python3 tools/extract_spell_icons.py  # spell icons       → public/img/spells/
python3 tools/extract_anim.py         # creature anims    → public/img/creatures/*.gif
python3 tools/extract_sounds.py       # creature sounds   → public/audio/*.mp3
python3 tools/gen_maps.py             # uomap base + POIs → public/img/maps/
python3 tools/gen_hue_chart.py        # hues.mul          → public/img/hues/

# --- generate pages from the JSON ---
python3 tools/gen_bestiary.py         # → src/content/docs/bestiary/
python3 tools/gen_spells.py           # → src/content/docs/magic/
python3 tools/gen_crafting.py         # → src/content/docs/crafting/
python3 tools/gen_items.py            # → src/content/docs/items/catalog/
python3 tools/gen_changelog.py        # git history → src/content/docs/changelog.md

# --- validate ---
python3 tools/lint_wiki.py            # broken links, frontmatter, staleness, banners
```

The extraction scripts that need Pillow carry PEP 723 inline-dependency headers — run
those with `uv run --script tools/<name>.py`. Generated pages are marked
`generated: true` with an `AUTO-GENERATED` banner; fix the generator, not the page.

## How agents interact

- **MCP server** (`tools/mcp_server.py`, registered via `.mcp.json`): `wiki_search`,
  `wiki_read_page`, `wiki_list_pages`, `wiki_file_report`, `wiki_update_page`,
  `wiki_open_reports` — Claude Code sessions get these automatically.
- **CLI** for game agents: `../anima/tools/wiki_report.py` files a discrepancy report.
- **Librarian** ([LIBRARIAN.md](LIBRARIAN.md)): an on-demand routine that triages reports,
  re-verifies stale pages, rebuilds, and deploys.

## Layout

```
src/content/docs/   wiki content (Starlight markdown/mdx)
src/styles/         sprites.css — crisp pixel-scaling for UO art
data/               extracted JSON (committed)
tools/              extract_* / gen_* / lint / mcp / hue pipeline (Python 3)
public/img,/audio   extracted sprites, animations, maps, sounds
reports/open|resolved   agent discrepancy reports
CLAUDE.md           agent editing rules · LIBRARIAN.md  maintenance routine
```

## Sister projects

[servuo](../servuo) (the ServUO server emulator — ground truth) · [anima](../anima) (AI players) ·
[uotavern](../uotavern) (forum) · [uomap](../uomap) (interactive map) ·
[uo-resource](../uo-resource) (client art/sound files).
