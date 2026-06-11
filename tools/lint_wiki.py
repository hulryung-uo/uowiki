#!/usr/bin/env python3
"""Lint wiki content under src/content/docs/.

Checks, per page:
  a) frontmatter exists, has a title, and a valid status
     (draft | unverified | source-verified | field-verified)
  b) internal markdown links (/section/slug/ style) resolve to an existing
     content file (or a file in public/)
  c) last_verified is present on non-draft pages and not older than 90 days
  d) pages with generated: true contain an AUTO-GENERATED banner

Any finding is an error; exits non-zero if any are found.

Usage:
  python3 tools/lint_wiki.py                          # lint everything
  python3 tools/lint_wiki.py src/content/docs/magic   # lint one section
  python3 tools/lint_wiki.py magic                    # shorthand for the same

Link targets are resolved against the FULL content tree regardless of the
path argument, so cross-section links are validated properly.
Stdlib only.
"""

import datetime
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = WIKI_ROOT / "src" / "content" / "docs"
PUBLIC_ROOT = WIKI_ROOT / "public"

VALID_STATUS = {"draft", "unverified", "source-verified", "field-verified"}
STALE_DAYS = 90
BANNER_MARK = "AUTO-GENERATED"

# [text](/path/) or [text](/path/#anchor) — absolute internal links only
RE_LINK = re.compile(r"\]\((/[^)\s]*)\)")
RE_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_frontmatter(text):
    """Minimal YAML front-matter reader: top-level `key: value` pairs only."""
    m = RE_FRONTMATTER.match(text)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if not line or line[0] in " \t#":
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
            value = value[1:-1]
        fm[key.strip()] = value
    return fm, text[m.end():]


def link_resolves(href: str) -> bool:
    path = href.split("#", 1)[0].strip("/")
    if not path:  # site root
        return (DOCS_ROOT / "index.md").exists() or (DOCS_ROOT / "index.mdx").exists()
    candidates = [
        DOCS_ROOT / f"{path}.md",
        DOCS_ROOT / f"{path}.mdx",
        DOCS_ROOT / path / "index.md",
        DOCS_ROOT / path / "index.mdx",
        PUBLIC_ROOT / path,  # static assets (images, downloads)
    ]
    return any(c.exists() for c in candidates)


def lint_page(path: Path, today: datetime.date):
    errors = []
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    if fm is None:
        return ["no frontmatter block found"]

    # (a) title + status
    if not fm.get("title"):
        errors.append("frontmatter missing `title`")
    status = fm.get("status", "")
    if status not in VALID_STATUS:
        errors.append(
            f"invalid status {status!r} (expected one of: {', '.join(sorted(VALID_STATUS))})"
        )

    # (b) internal links
    for href in RE_LINK.findall(body):
        if not link_resolves(href):
            errors.append(f"broken internal link: {href}")

    # (c) last_verified freshness (drafts are exempt)
    lv_raw = fm.get("last_verified", "")
    if status != "draft":
        if not lv_raw:
            errors.append("missing `last_verified` on non-draft page")
        else:
            try:
                lv = datetime.date.fromisoformat(lv_raw)
            except ValueError:
                errors.append(f"unparseable last_verified: {lv_raw!r}")
            else:
                age = (today - lv).days
                if age > STALE_DAYS:
                    errors.append(f"stale: last_verified {lv_raw} is {age} days old (> {STALE_DAYS})")

    # (d) generated pages need the banner
    if fm.get("generated", "false").lower() == "true" and BANNER_MARK not in body:
        errors.append("generated: true but no AUTO-GENERATED banner in body")

    return errors


def main():
    if len(sys.argv) > 2:
        sys.exit(__doc__)
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        target = Path(arg)
        if not target.is_absolute():
            # accept "magic", "src/content/docs/magic", or cwd-relative paths
            for base in (DOCS_ROOT, WIKI_ROOT, Path.cwd()):
                if (base / arg).exists():
                    target = base / arg
                    break
        if not target.exists():
            sys.exit(f"ERROR: path not found: {arg}")
    else:
        target = DOCS_ROOT

    pages = sorted(p for p in target.rglob("*") if p.suffix in (".md", ".mdx")) \
        if target.is_dir() else [target]
    if not pages:
        sys.exit(f"ERROR: no markdown pages found under {target}")

    today = datetime.date.today()
    total_errors = 0
    clean = 0
    for page in pages:
        errs = lint_page(page, today)
        rel = page.relative_to(WIKI_ROOT) if page.is_relative_to(WIKI_ROOT) else page
        if errs:
            print(f"FAIL {rel}")
            for e in errs:
                print(f"     - {e}")
            total_errors += len(errs)
        else:
            clean += 1

    print(f"\n{len(pages)} pages checked: {clean} clean, "
          f"{len(pages) - clean} with problems, {total_errors} errors")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
