#!/usr/bin/env python3
"""Extract the skill table from ServUO core into data/skills.json.

Reads ../servuo/Server/Skills.cs — the SkillInfo[] m_Table with one entry per
skill: id, name, stat scales (str/dex/int contribution to combat ability),
title, stat gain weights, gain factor, primary/secondary stats, and the
mastery / use-while-casting flags.

Usage: python3 tools/extract_skills.py
Stdlib only.
"""

import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
SKILLS_CS = WIKI_ROOT.parent / "servuo" / "Server" / "Skills.cs"
OUT_PATH = WIKI_ROOT / "data" / "skills.json"

# Matches one table row:
# new SkillInfo(0, "Alchemy", 0.0, 5.0, 5.0, "Alchemist", null,
#               0.0, 0.5, 0.5, 1.0, StatCode.Int, StatCode.Dex[, true[, true]]),
RE_ENTRY = re.compile(
    r"new\s+SkillInfo\s*\(\s*"
    r"(?P<id>\d+)\s*,\s*"
    r'"(?P<name>[^"]+)"\s*,\s*'
    r"(?P<str_scale>[\d.]+)\s*,\s*"
    r"(?P<dex_scale>[\d.]+)\s*,\s*"
    r"(?P<int_scale>[\d.]+)\s*,\s*"
    r'"(?P<title>[^"]+)"\s*,\s*'
    r"null\s*,\s*"
    r"(?P<str_gain>[\d.]+)\s*,\s*"
    r"(?P<dex_gain>[\d.]+)\s*,\s*"
    r"(?P<int_gain>[\d.]+)\s*,\s*"
    r"(?P<gain_factor>[\d.]+)\s*,\s*"
    r"StatCode\.(?P<primary>\w+)\s*,\s*"
    r"StatCode\.(?P<secondary>\w+)\s*"
    r"(?:,\s*(?P<mastery>true|false)\s*)?"
    r"(?:,\s*(?P<use_while_casting>true|false)\s*)?"
    r"\)"
)


def main():
    src = SKILLS_CS.read_text(encoding="utf-8", errors="replace")

    m = re.search(r"m_Table\s*=\s*new\s+SkillInfo\[(\d+)\]\s*\{(.*?)\n\s*\};",
                  src, re.DOTALL)
    if not m:
        sys.exit(f"ERROR: could not find SkillInfo table in {SKILLS_CS}")
    declared = int(m.group(1))
    table_src = m.group(2)

    skills = []
    for e in RE_ENTRY.finditer(table_src):
        skills.append({
            "id": int(e.group("id")),
            "name": e.group("name"),
            "title": e.group("title"),
            "primary_stat": e.group("primary"),
            "secondary_stat": e.group("secondary"),
            # combat-ability stat scales (percent / 100 in code)
            "str_scale": float(e.group("str_scale")),
            "dex_scale": float(e.group("dex_scale")),
            "int_scale": float(e.group("int_scale")),
            # stat gain weights when the skill is used
            "str_gain": float(e.group("str_gain")),
            "dex_gain": float(e.group("dex_gain")),
            "int_gain": float(e.group("int_gain")),
            "gain_factor": float(e.group("gain_factor")),
            "is_mastery": e.group("mastery") == "true",
            "use_while_casting": e.group("use_while_casting") == "true",
        })

    if len(skills) != declared:
        sys.exit(f"ERROR: parsed {len(skills)} skills but table declares {declared}")
    ids = [s["id"] for s in skills]
    if ids != list(range(declared)):
        sys.exit("ERROR: skill ids are not contiguous — parser missed an entry")

    out = {
        "_schema": {
            "description": "Skill table extracted from ServUO core by tools/extract_skills.py. Do not hand-edit; re-run the extractor.",
            "extracted_from": "servuo: Server/Skills.cs (SkillInfo.m_Table)",
            "skills": "list of {id, name, title, primary_stat, secondary_stat, str_scale, dex_scale, int_scale, str_gain, dex_gain, int_gain, gain_factor, is_mastery, use_while_casting}",
        },
        "skills": skills,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(skills)} skills -> {OUT_PATH}")


if __name__ == "__main__":
    main()
