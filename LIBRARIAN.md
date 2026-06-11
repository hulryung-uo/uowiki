# The Librarian Routine

On-demand maintenance routine for this wiki, run by a Claude Code agent. Trigger it
when `reports/open/` is non-empty, after ServUO source updates, or whenever a batch
of MCP/agent edits should be verified and shipped — e.g.:

    claude -p "Read /Users/dkkang/dev/uo/uowiki/LIBRARIAN.md and execute it end to end."

Goal: keep the wiki correct, current, and growing. Follow CLAUDE.md rules
throughout — provenance frontmatter, the two content layers, commit conventions.

Run from `/Users/dkkang/dev/uo/uowiki`. Sibling repos: `../servuo` (ground truth),
`../anima` (agent logs), `../uotavern` (forum).

## Steps

1. **Sync** — `git pull --rebase` (skip gracefully if offline).

2. **Triage `reports/open/`** — for each report (format in CLAUDE.md):
   - Verify the claim independently: read the cited ServUO source and/or anima logs.
     Do not trust the report blindly — agents can misread the world.
   - If the wiki is wrong: fix the page. Demote/promote `status` per evidence, append
     the report's evidence to `sources`, update `last_verified`.
   - If the page is generated (`generated: true`): fix the extractor or generator in
     `tools/`, regenerate, never hand-edit the page.
   - If the report is wrong: append a `## Resolution: rejected` note with reasoning.
   - Either way `git mv` the report to `reports/resolved/` and reference it in the
     commit message.

3. **Lint** — `python3 tools/lint_wiki.py`; fix every error it finds.

4. **Staleness pass** — pick the 2-3 oldest non-generated pages by `last_verified`
   (lint flags >90 days). Re-verify their claims against current ServUO source
   (the server code may have been updated); update content and `last_verified`.

5. **Drift check (cheap)** — `git -C ../servuo log --oneline -5`. If server source
   changed since the last librarian commit touched `data/`, rerun the affected
   `tools/extract_*.py` + `tools/gen_*.py` and commit regenerated pages with the
   servuo commit hash in the message.

6. **Forum sweep (optional, best-effort)** — fetch recent posts from the forum's
   `qa` and `library` boards (https://www.uotavern.com, API under `/api/posts`).
   If a post contains durable knowledge worth a wiki page (a guide, corrected
   mechanics), draft the page (`status: unverified`, source: forum post URL).
   Skip silently if the API is unreachable.

7. **Ship** — commit all content changes per CLAUDE.md convention first, then
   refresh the changelog from that history and commit it on its own:
   `python3 tools/gen_changelog.py && git add src/content/docs/changelog.md &&
   git commit -m "wiki(meta): regenerate changelog"` (skips if no diff).
   Then `npm run build` (must pass), `git push`, and deploy:
   `vercel --prod --yes --archive=tgz`
   (`--archive=tgz` is required — the plain upload aborts on the ~1,700 media
   asset files under public/)
   (CLI deploy is required until the Vercel GitHub integration is connected;
   once it is, push alone deploys and this step becomes push-only).

8. **Summarize** — end with a short report: reports triaged (fixed/rejected),
   pages touched, lint status, deploy URL. If nothing needed doing, say so —
   an empty run is a valid run.

## Boundaries

- Never delete pages or restructure directories — propose via a report instead.
- Never invent numbers; unverifiable claims stay `unverified` and say so in prose.
- Keep each run's diff reviewable: prefer several small commits over one blob.
