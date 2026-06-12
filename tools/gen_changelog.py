# /// script
# requires-python = ">=3.11"
# ///
"""Generate the wiki's Recent Changes page for READERS, from git history.

This page exists so someone browsing the wiki can see what game knowledge was
recently added, updated, or corrected — not a developer commit log. So it only
reports commits that actually changed reader-facing content (anything under
src/content/docs/), and describes each in plain language with links to the
pages and sections that changed. Tooling, config, deploy, and MCP commits never
touch docs/, so they are filtered out automatically.

Each entry is classified Added / Updated / Fixed from the files' git status and
the commit message, and corrections traced to an in-game discrepancy report are
flagged as such.

Regenerate at ship time (LIBRARIAN.md step 7) or any time:
    python3 tools/gen_changelog.py

Generated page — never hand-edit. Well-formed commit messages
(`wiki(<section>): <plain summary>`) are what make it read well.
"""

from __future__ import annotations

import datetime as dt
import re
import subprocess
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
DOCS_PREFIX = "src/content/docs/"
OUT = WIKI_ROOT / "src" / "content" / "docs" / "changelog.md"
REL_OUT = OUT.relative_to(WIKI_ROOT).as_posix()

REMOTE = subprocess.run(
    ["git", "-C", str(WIKI_ROOT), "config", "--get", "remote.origin.url"],
    capture_output=True, text=True,
).stdout.strip()
_slug = re.sub(r"\.git$", "", re.sub(r"^git@github\.com:", "", REMOTE))
_slug = re.sub(r"^https?://github\.com/", "", _slug)
REPO_SLUG = _slug if "/" in _slug else ""
COMMIT_BASE = f"https://github.com/{REPO_SLUG}/commit/" if REPO_SLUG else ""

MAX_COMMITS = 500

# Directory under docs/ -> the label readers see in the sidebar.
SECTION_LABELS = {
    "bestiary": "Bestiary", "magic": "Magic", "skills": "Skills",
    "items": "Items", "crafting": "Crafting", "world": "World",
    "mechanics": "Mechanics", "shard": "Our Shard", "guides": "Guides",
    "templates": "Character Templates",
}
# When few pages change we link them; beyond this we just give a section + count.
LIST_PAGES_UP_TO = 6
# Words in a commit summary that mark a correction.
FIX_RE = re.compile(r"\b(fix|correct|wrong|actually|does have|mistake|error)\b", re.I)
# A trailing parenthetical that is provenance (file paths / urls / reports), not content.
PROVENANCE_RE = re.compile(
    r"\s*\((?:[^()]*\b(?:report|source|Scripts/|Spawns/|\.cs|https?://)[^()]*)\)\s*$"
)


def path_to_slug(path: str) -> str | None:
    """src/content/docs/world/yew.md -> /world/yew/ ; index files -> section root."""
    if not path.startswith(DOCS_PREFIX):
        return None
    rel = path[len(DOCS_PREFIX):]
    rel = re.sub(r"\.(md|mdx)$", "", rel)
    if rel in ("index", ""):
        return "/"
    rel = re.sub(r"/index$", "", rel)
    return f"/{rel}/"


def section_of(path: str) -> str:
    rel = path[len(DOCS_PREFIX):]
    top = rel.split("/")[0]
    if "/" not in rel:  # a file sitting directly in docs/
        return "Home"
    return SECTION_LABELS.get(top, top.capitalize())


def git_log() -> list[dict]:
    """Commits newest-first, each with (status, path) for every file touched."""
    raw = subprocess.run(
        ["git", "-C", str(WIKI_ROOT), "log", f"-{MAX_COMMITS}", "--date=short",
         "--pretty=format:__C__%h|%ad|%s", "--name-status"],
        capture_output=True, text=True, check=True,
    ).stdout
    commits: list[dict] = []
    for block in raw.split("__C__"):
        block = block.strip("\n")
        if not block:
            continue
        head, *rows = block.split("\n")
        h, date, subject = head.split("|", 2)
        files: list[tuple[str, str]] = []
        for row in rows:
            if not row.strip():
                continue
            cols = row.split("\t")
            status = cols[0][0]  # A/M/D/R...
            path = cols[-1]      # for renames, the new path
            files.append((status, path))
        commits.append({"hash": h, "date": date, "subject": subject, "files": files})
    return commits


def clean_summary(subject: str) -> tuple[str, bool]:
    """Strip the `wiki(section):` prefix and provenance tail; flag report-driven."""
    from_report = bool(re.search(r"\(report\b", subject))
    m = re.match(r"^\w+\([^)]*\):\s*(.*)$", subject) or re.match(r"^\w+:\s*(.*)$", subject)
    text = m.group(1) if m else subject
    text = PROVENANCE_RE.sub("", text).strip()
    return text[:1].upper() + text[1:], from_report


def md(text: str) -> str:
    return text.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def render_entry(c: dict) -> str | None:
    docs = [(s, p) for s, p in c["files"]
            if p.startswith(DOCS_PREFIX) and p != REL_OUT]
    if not docs:
        return None  # not a content change — skip (tooling/config/reports)

    added = [p for s, p in docs if s == "A"]
    changed = [p for s, p in docs if s != "A"]  # M, R, D...
    summary, from_report = clean_summary(c["subject"])

    if from_report or FIX_RE.search(c["subject"]):
        kind = "Fixed"
    elif added and not changed:
        kind = "Added"
    elif added and len(added) >= len(changed):
        kind = "Added"
    else:
        kind = "Updated"

    # Affected pages grouped by section (skip deletes from the visible list).
    visible = [(s, p) for s, p in docs if s != "D"]
    pages = [p for _, p in visible]
    sections: dict[str, int] = {}
    for _, p in visible:
        sections[section_of(p)] = sections.get(section_of(p), 0) + 1

    if 0 < len(pages) <= LIST_PAGES_UP_TO:
        links = []
        for p in pages:
            slug = path_to_slug(p)
            title = slug.strip("/").split("/")[-1].replace("-", " ").title() if slug and slug != "/" else "Home"
            # Only link to a page that still exists — pages moved/deleted since the
            # commit would otherwise leave a broken link in the changelog.
            exists = (WIKI_ROOT / p).exists() or p == "src/content/docs/index.mdx"
            links.append(f"[{title}]({slug})" if slug and exists else title)
        where = " · ".join(links)
    else:
        where = " · ".join(
            f"[{name}]({_section_link(name)}) ({n})" if _section_link(name) else f"{name} ({n})"
            for name, n in sorted(sections.items(), key=lambda kv: -kv[1])
        )

    note = " — from an in-game report" if from_report else ""
    detail = f" <sub>[details]({COMMIT_BASE}{c['hash']})</sub>" if COMMIT_BASE else ""
    return f"- **{kind}** — {md(summary)}.{note}  \n  {where}{detail}"


def _section_link(label: str) -> str | None:
    """Link a section to its index page only if that index actually exists."""
    for dir_, name in SECTION_LABELS.items():
        if name == label:
            docs = WIKI_ROOT / "src" / "content" / "docs" / dir_
            if (docs / "index.md").exists() or (docs / "index.mdx").exists():
                return f"/{dir_}/"
            return None
    return None


def render(commits: list[dict]) -> str:
    today = dt.date.today().isoformat()
    out = [
        "---",
        "title: Recent Changes",
        "description: What was recently added, updated, or corrected on the wiki.",
        "status: source-verified",
        "sources:",
        '  - "git: commit history of this repository"',
        f"last_verified: {today}",
        "generated: true",
        "---",
        "",
        "<!-- AUTO-GENERATED by tools/gen_changelog.py from git history — do not hand-edit -->",
        "",
        "What's new and what's been corrected on the wiki. Entries marked",
        '"from an in-game report" are fixes an [AI resident filed](/guides/wiki-conventions/)',
        "after the game contradicted a page.",
        "",
    ]

    by_date: dict[str, list[str]] = {}
    for c in commits:
        entry = render_entry(c)
        if entry:
            by_date.setdefault(c["date"], []).append(entry)

    for date, entries in by_date.items():  # newest-first (git order preserved)
        out.append(f"## {date}")
        out.append("")
        out.extend(entries)
        out.append("")

    if COMMIT_BASE and REPO_SLUG:
        out.append("---")
        out.append("")
        out.append(f"Every change is a tracked git commit — "
                   f"[full history on GitHub](https://github.com/{REPO_SLUG}/commits/).")

    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    commits = git_log()
    OUT.write_text(render(commits), encoding="utf-8")
    n = sum(1 for c in commits if render_entry(c))
    print(f"wrote {REL_OUT}: {n} content change(s)")


if __name__ == "__main__":
    main()
