# /// script
# requires-python = ">=3.11"
# dependencies = ["mcp"]
# ///
"""MCP server exposing the UO Wiki to AI agents.

Lets any MCP client (Claude Code, anima's self-improvement loop, other bots)
search and read wiki pages, file discrepancy reports, and update curated pages
— enforcing the rules in CLAUDE.md (generated pages are read-only, edits are
committed to git with provenance).

Run (stdio):        uv run --script tools/mcp_server.py
Register in Claude: claude mcp add uowiki -- uv run --script /Users/dkkang/dev/uo/uowiki/tools/mcp_server.py
Self-test:          uv run --script tools/mcp_server.py --selftest
"""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
DOCS = WIKI_ROOT / "src" / "content" / "docs"
REPORTS_OPEN = WIKI_ROOT / "reports" / "open"

VALID_STATUS = {"draft", "unverified", "source-verified", "field-verified"}


# ---------------------------------------------------------------- helpers


def _slug_to_path(slug: str) -> Path | None:
    """Resolve a wiki slug like 'world/yew' or 'bestiary' to a content file."""
    slug = slug.strip("/")
    for candidate in (
        DOCS / f"{slug}.md",
        DOCS / f"{slug}.mdx",
        DOCS / slug / "index.md",
        DOCS / slug / "index.mdx",
    ):
        if candidate.is_file():
            return candidate
    return None


def _path_to_slug(path: Path) -> str:
    rel = path.relative_to(DOCS)
    slug = str(rel.with_suffix(""))
    if slug.endswith("/index"):
        slug = slug[: -len("/index")]
    return "/" if slug == "index" else f"/{slug}/"


def _frontmatter(text: str) -> dict[str, str]:
    """Crude single-level frontmatter reader (title/status/generated only)."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    fields: dict[str, str] = {}
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
            if kv:
                fields[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return fields


def _git(args: list[str]) -> str:
    out = subprocess.run(
        ["git", "-C", str(WIKI_ROOT), *args], capture_output=True, text=True
    )
    if out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout.strip()


def _all_pages() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*") if p.suffix in {".md", ".mdx"})


# ---------------------------------------------------------------- tool impls
# Plain functions so they are testable without an MCP client; the MCP tool
# definitions below are thin wrappers.


def search(query: str, limit: int = 10) -> list[dict]:
    """Case-insensitive search over titles and bodies.

    Multi-word queries match pages containing ALL terms (anywhere on the page);
    pages are ranked by total term occurrences, title hits weighted highest.
    """
    terms = [re.compile(re.escape(t), re.IGNORECASE) for t in query.split()]
    if not terms:
        return []
    hits: list[dict] = []
    for path in _all_pages():
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = _frontmatter(text)
        title = fm.get("title", path.stem)
        if not all(rx.search(text) or rx.search(title) for rx in terms):
            continue
        score = sum(10 for rx in terms if rx.search(title))
        excerpt = ""
        for line in text.splitlines():
            matched = [rx for rx in terms if rx.search(line)]
            score += len(matched)
            if matched and not excerpt and not line.startswith(("---", "#")):
                excerpt = line.strip()[:200]
        if score:
            hits.append(
                {
                    "slug": _path_to_slug(path),
                    "title": title,
                    "status": fm.get("status", "draft"),
                    "score": score,
                    "excerpt": excerpt,
                }
            )
    hits.sort(key=lambda h: -h["score"])
    return hits[:limit]


def read_page(slug: str) -> dict:
    path = _slug_to_path(slug)
    if path is None:
        raise FileNotFoundError(f"no wiki page for slug '{slug}'")
    text = path.read_text(encoding="utf-8")
    fm = _frontmatter(text)
    return {
        "slug": _path_to_slug(path),
        "file": str(path.relative_to(WIKI_ROOT)),
        "title": fm.get("title", ""),
        "status": fm.get("status", "draft"),
        "generated": fm.get("generated", "false").lower() == "true",
        "markdown": text,
    }


def list_pages(section: str = "") -> list[dict]:
    base = DOCS / section.strip("/") if section else DOCS
    if not base.is_dir():
        raise FileNotFoundError(f"no section '{section}'")
    out = []
    for path in sorted(p for p in base.rglob("*") if p.suffix in {".md", ".mdx"}):
        fm = _frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        out.append(
            {
                "slug": _path_to_slug(path),
                "title": fm.get("title", path.stem),
                "status": fm.get("status", "draft"),
                "generated": fm.get("generated", "false").lower() == "true",
            }
        )
    return out


def file_report(
    agent: str, page: str, claim: str, observed: str, expected: str, evidence: str
) -> dict:
    """File a discrepancy report into reports/open/ and commit it."""
    page = page.strip()
    page_path = WIKI_ROOT / page
    if not page_path.is_file() and _slug_to_path(page) is None:
        raise FileNotFoundError(
            f"page '{page}' not found — pass a repo path like "
            "src/content/docs/skills/mining.md or a slug like skills/mining"
        )
    today = dt.date.today().isoformat()
    slug_words = re.sub(r"[^a-z0-9 ]", "", claim.lower()).split()[:6]
    base = f"{today}-{agent}-{'-'.join(slug_words)}"
    dest = REPORTS_OPEN / f"{base}.md"
    n = 2
    while dest.exists():
        dest = REPORTS_OPEN / f"{base}-{n}.md"
        n += 1
    dest.write_text(
        f"# {claim}\n"
        f"- page: {page}\n"
        f"- observed: {observed}\n"
        f"- expected-per-wiki: {expected}\n"
        f"- evidence: {evidence}\n",
        encoding="utf-8",
    )
    rel = str(dest.relative_to(WIKI_ROOT))
    _git(["add", rel])
    _git(["commit", "-m", f"report({agent}): {claim}", "--", rel])
    return {"report": rel, "committed": True}


def update_page(
    slug: str, markdown: str, commit_message: str, agent: str = "agent"
) -> dict:
    """Replace a curated page's full markdown content and commit.

    Refuses generated pages (fix tools/ + regenerate instead) and content
    whose frontmatter is missing title or a valid status. Does not push;
    run the librarian routine (LIBRARIAN.md) to ship a batch of changes.
    """
    path = _slug_to_path(slug)
    if path is None:
        raise FileNotFoundError(f"no wiki page for slug '{slug}' — create via report first")
    current = _frontmatter(path.read_text(encoding="utf-8"))
    if current.get("generated", "false").lower() == "true":
        raise PermissionError(
            f"'{slug}' is generated from data/ — edit the extractor/generator in "
            "tools/ and regenerate; see CLAUDE.md"
        )
    new_fm = _frontmatter(markdown)
    if not new_fm.get("title"):
        raise ValueError("new content must keep frontmatter with a title")
    if new_fm.get("status") not in VALID_STATUS:
        raise ValueError(f"frontmatter status must be one of {sorted(VALID_STATUS)}")
    path.write_text(markdown, encoding="utf-8")
    rel = str(path.relative_to(WIKI_ROOT))
    _git(["add", rel])
    _git(["commit", "-m", f"wiki: {commit_message} (via mcp, {agent})", "--", rel])
    return {"file": rel, "committed": True, "note": "not pushed — librarian ships batches"}


def open_reports() -> list[dict]:
    out = []
    for f in sorted(REPORTS_OPEN.glob("*.md")):
        first = f.read_text(encoding="utf-8").splitlines()
        out.append({"report": f.name, "claim": first[0].lstrip("# ") if first else ""})
    return out


# ---------------------------------------------------------------- MCP server


def serve() -> None:
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP(
        "uowiki",
        instructions=(
            "UO Wiki knowledge base (https://uowiki.vercel.app). Search/read for "
            "game facts; file a report when reality contradicts a page; update "
            "curated pages only with evidence, per the wiki's CLAUDE.md."
        ),
    )
    mcp.tool(name="wiki_search")(search)
    mcp.tool(name="wiki_read_page")(read_page)
    mcp.tool(name="wiki_list_pages")(list_pages)
    mcp.tool(name="wiki_file_report")(file_report)
    mcp.tool(name="wiki_update_page")(update_page)
    mcp.tool(name="wiki_open_reports")(open_reports)
    mcp.run()


def selftest() -> None:
    hits = search("yew bank", limit=3)
    assert hits, "search returned nothing"
    print("search ok:", [h["slug"] for h in hits])
    page = read_page("world/yew")
    assert "Empath Abbey" in page["markdown"]
    print("read_page ok:", page["title"], page["status"])
    pages = list_pages("guides")
    print("list_pages ok:", len(pages), "guide pages")
    try:
        update_page("bestiary/monsters/dragon", "x", "nope")
    except PermissionError:
        print("update_page correctly refuses generated pages")
    print("reports open:", open_reports())
    print("ALL OK")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        serve()
