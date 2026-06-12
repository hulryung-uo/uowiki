#!/usr/bin/env python3
"""Emit public/recent.json — a small feed of recent wiki changes for the hub.

The landing site (uotavern.com) fetches this client-side to show a live
"From the Library" panel. Reuses the same git-history parsing as the changelog,
but outputs compact JSON (kind, summary, section links, date) instead of markdown.

Usage: python3 tools/gen_feed.py
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
OUT = WIKI / "public" / "recent.json"
DOCS_PREFIX = "src/content/docs/"
MAX = 14

SECTION_NAMES = {
    "bestiary": "Bestiary", "magic": "Magic", "skills": "Skills", "items": "Items",
    "crafting": "Crafting", "world": "World", "mechanics": "Mechanics",
    "shard": "Our Shard", "guides": "Getting Started", "templates": "Templates",
    "playing": "How to Play", "professions": "Professions", "essays": "Essays",
    "reference": "Reference",
}
FIX_WORDS = ("fix", "correct", "wrong", "actually", "does have")


def git_log():
    raw = subprocess.run(
        ["git", "-C", str(WIKI), "log", "-200", "--date=short",
         "--pretty=format:__C__%h|%ad|%s", "--name-only"],
        capture_output=True, text=True, check=True).stdout
    out = []
    for block in raw.split("__C__"):
        block = block.strip("\n")
        if not block:
            continue
        head, *files = block.split("\n")
        h, date, subject = head.split("|", 2)
        out.append({"hash": h, "date": date, "subject": subject,
                    "files": [f for f in files if f.strip()]})
    return out


def section_of(path):
    rel = path[len(DOCS_PREFIX):]
    top = rel.split("/")[0]
    if top in ("ko", "ja"):  # skip locale mirrors; English drives the feed
        return None
    return SECTION_NAMES.get(top)


def clean(subject):
    import re
    m = re.match(r"^\w+\([^)]*\):\s*(.*)$", subject) or re.match(r"^\w+:\s*(.*)$", subject)
    text = m.group(1) if m else subject
    text = re.sub(r"\s*\((?:[^()]*\b(?:report|source|Scripts/|Spawns/|\.cs|https?://)[^()]*)\)\s*$", "", text)
    return text[:1].upper() + text[1:]


def main():
    items = []
    for c in git_log():
        docs = [f for f in c["files"]
                if f.startswith(DOCS_PREFIX) and not f.startswith(DOCS_PREFIX + ("ko/"))
                and not f.startswith(DOCS_PREFIX + "ja/") and f != DOCS_PREFIX + "changelog.md"]
        if not docs:
            continue
        sections = sorted({s for s in (section_of(f) for f in docs) if s})
        if not sections:
            continue
        sl = c["subject"].lower()
        if "report(" in c["subject"] or any(w in sl for w in FIX_WORDS):
            kind = "Fixed"
        elif any(w in sl for w in ("add ", "add:", "new ", "introduce", "create", " — add", "(add")):
            kind = "Added"
        else:
            kind = "Updated"
        items.append({
            "kind": kind,
            "summary": clean(c["subject"]),
            "sections": sections[:3],
            "date": c["date"],
        })
        if len(items) >= MAX:
            break
    OUT.write_text(json.dumps({"items": items}, ensure_ascii=False, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(WIKI)} with {len(items)} items")


if __name__ == "__main__":
    main()
