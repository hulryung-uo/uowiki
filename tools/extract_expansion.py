#!/usr/bin/env python3
"""Extract expansion-introduction era for every craftable item from ServUO.

Parses each Scripts/Services/Craft/Def*.cs and records, for every
`AddCraft(typeof(X), ...)` call, the innermost enclosing `if (Core.<EXP>)`
expansion gate (AOS/SE/ML/SA/HS/TOL/EJ). An AddCraft inside such a gate is
craftable only from that expansion onward -> that is its introduction era.
AddCraft calls outside any Core gate are available from the base game ->
"Classic" (T2A-era).

When gates are nested (e.g. `if (Core.HS) { ... if (Core.EJ) { AddCraft... } }`)
the LATEST / highest expansion wins, since it is the most restrictive gate
that actually controls availability.

Note: a `Core.X ? a : b` ternary that appears only inside an AddCraft *argument*
is NOT a gate — it just tunes a value. Only `if (Core.<EXP>)` statements that
open a block (or guard a single statement) gate availability.

Output: data/item_expansion.json
  {"_schema": ...,
   "by_class": {"PlateChest": "Classic", "Wakizashi": "SE", ...},
   "_meta": {"counts": {era: n, ...}, "total": n, ...}}

Usage: python3 tools/extract_expansion.py
"""

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRAFT_DIR = os.path.join(
    ROOT, "..", "servuo", "Scripts", "Services", "Craft")
OUT_PATH = os.path.join(ROOT, "data", "item_expansion.json")

# Canonical era labels and their ordering (higher index = later/more
# restrictive). "Classic" is the ungated base game (T2A-era).
ERA_ORDER = ["Classic", "AOS", "SE", "ML", "SA", "HS", "TOL", "EJ"]
ERA_RANK = {e: i for i, e in enumerate(ERA_ORDER)}

# Only these Core flags represent expansion gates we tag.
GATE_EXPANSIONS = {"AOS", "SE", "ML", "SA", "HS", "TOL", "EJ"}

# `if (Core.AOS)` / `if(Core.SE)` etc. — must be a statement-opening if whose
# condition is exactly a Core.<EXP> flag (optionally negated handling below).
IF_CORE_RE = re.compile(r"^\s*if\s*\(\s*Core\.(\w+)\s*\)\s*(\{)?\s*$")
# `if (Core.AOS) AddCraft(...);` single-line guarded statement.
IF_CORE_INLINE_RE = re.compile(r"^\s*if\s*\(\s*Core\.(\w+)\s*\)\s*(\S.*)$")
# else handling
ELSE_RE = re.compile(r"^\s*else\b")

ADDCRAFT_RE = re.compile(r"AddCraft\s*\(\s*typeof\s*\(\s*([\w.]+)\s*\)")


def strip_comments(line):
    """Remove // line comments (good enough; block comments are rare here)."""
    # naive: cut at // not inside a string. Craft defs don't put // in strings.
    idx = line.find("//")
    if idx != -1:
        line = line[:idx]
    return line


def count_braces(line):
    """Net brace delta on a line, ignoring braces inside string/char literals."""
    depth = 0
    in_str = False
    in_chr = False
    esc = False
    for ch in line:
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = True
            continue
        if in_str:
            if ch == '"':
                in_str = False
            continue
        if in_chr:
            if ch == "'":
                in_chr = False
            continue
        if ch == '"':
            in_str = True
            continue
        if ch == "'":
            in_chr = True
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
    return depth


def parse_file(path):
    """Return (mapping class->era, list of warnings) for one Def file.

    Algorithm: walk lines tracking the current brace depth. Maintain a stack
    of (depth_at_which_gate_opened, era) for active `if (Core.X)` gates that
    opened a `{` block. When the depth falls back to a gate's opening depth,
    that gate is popped. A single-statement `if (Core.X)` (no brace) applies
    only to the immediately following statement / inline statement.
    """
    mapping = {}
    warnings = []

    with open(path, encoding="utf-8") as f:
        raw_lines = f.readlines()

    depth = 0
    # stack entries: dict(open_depth=int, era=str)
    gate_stack = []
    # pending single-statement gate (applies to next non-blank statement)
    pending_gate = None

    for lineno, raw in enumerate(raw_lines, 1):
        line = strip_comments(raw)
        stripped = line.strip()
        if not stripped:
            continue

        # Effective gate era for anything emitted *at this line's current
        # context*: latest of active block gates and any pending single gate.
        def current_era():
            eras = [g["era"] for g in gate_stack]
            if pending_gate is not None:
                eras.append(pending_gate)
            if not eras:
                return "Classic"
            return max(eras, key=lambda e: ERA_RANK.get(e, 0))

        # --- detect a Core gate opening on this line ---
        m_block = IF_CORE_RE.match(line)
        m_inline = None if m_block else IF_CORE_INLINE_RE.match(line)

        gate_opened_here = None
        if m_block:
            exp = m_block.group(1)
            if exp in GATE_EXPANSIONS:
                gate_opened_here = exp
            # else: a Core flag we don't gate on (e.g. Core.UOR) -> treat as
            # no expansion gate (still classic). We pop/no-op below.
            has_brace = m_block.group(2) == "{"
            # apply brace count for the rest of the line normally afterwards
            if gate_opened_here:
                if has_brace:
                    # gate opens a block at the NEW depth after this {
                    gate_stack.append(
                        {"open_depth": depth, "era": gate_opened_here})
                    # the { will be counted by count_braces below -> depth+1
                else:
                    # block-style if whose { is on the NEXT line, OR a
                    # single-statement if. We set pending and resolve when we
                    # see the next line.
                    pending_gate = gate_opened_here
            # account for any AddCraft on this same line (rare for block ifs)
            for cls in ADDCRAFT_RE.findall(line):
                _record(mapping, cls, current_era())
            depth += count_braces(line)
            # If a pending single-gate's statement was on this very line via
            # inline, that's handled by m_inline branch instead.
            continue

        if m_inline:
            exp = m_inline.group(1)
            rest = m_inline.group(2).strip()
            era_for_rest = "Classic"
            if exp in GATE_EXPANSIONS:
                era_for_rest = exp
            # combine with any already-active gates
            active = [g["era"] for g in gate_stack]
            if exp in GATE_EXPANSIONS:
                active.append(exp)
            combined = (max(active, key=lambda e: ERA_RANK.get(e, 0))
                        if active else "Classic")
            if rest == "{":
                # `if (Core.X) {` written as separate token shouldn't reach
                # here (m_block handles trailing {), but guard anyway.
                if exp in GATE_EXPANSIONS:
                    gate_stack.append({"open_depth": depth, "era": exp})
                depth += count_braces(line)
                continue
            # inline statement: record any AddCraft on this line with combined
            for cls in ADDCRAFT_RE.findall(line):
                _record(mapping, cls, combined)
            depth += count_braces(line)
            # inline single-statement gate does not persist
            continue

        # --- resolve a pending single-statement / next-line-brace gate ---
        if pending_gate is not None:
            if stripped == "{":
                # the block's opening brace was on its own line
                gate_stack.append({"open_depth": depth, "era": pending_gate})
                pending_gate = None
                depth += count_braces(line)
                continue
            else:
                # single statement guarded by the pending gate
                era = current_era()
                for cls in ADDCRAFT_RE.findall(line):
                    _record(mapping, cls, era)
                pending_gate = None
                depth += count_braces(line)
                continue

        # --- normal line: record AddCraft under active block gates ---
        for cls in ADDCRAFT_RE.findall(line):
            _record(mapping, cls, current_era())

        depth += count_braces(line)

        # --- pop any block gates whose scope just closed ---
        while gate_stack and depth <= gate_stack[-1]["open_depth"]:
            gate_stack.pop()

        if depth < 0:
            warnings.append("%s:%d brace depth went negative" %
                            (os.path.basename(path), lineno))
            depth = 0

    return mapping, warnings


def _record(mapping, cls, era):
    """Record class->era, keeping the LATEST (highest) era if seen twice."""
    cls = cls.split(".")[-1]  # strip any namespace qualifier
    prev = mapping.get(cls)
    if prev is None or ERA_RANK.get(era, 0) > ERA_RANK.get(prev, 0):
        mapping[cls] = era


def main():
    craft_dir = os.path.normpath(CRAFT_DIR)
    files = sorted(
        fn for fn in os.listdir(craft_dir)
        if fn.startswith("Def") and fn.endswith(".cs"))

    by_class = {}
    all_warnings = []
    per_file = {}
    for fn in files:
        path = os.path.join(craft_dir, fn)
        mapping, warnings = parse_file(path)
        per_file[fn] = len(mapping)
        all_warnings += warnings
        for cls, era in mapping.items():
            prev = by_class.get(cls)
            if prev is None or ERA_RANK.get(era, 0) > ERA_RANK.get(prev, 0):
                by_class[cls] = era

    # counts per era
    counts = {e: 0 for e in ERA_ORDER}
    for era in by_class.values():
        counts[era] = counts.get(era, 0) + 1

    by_class_sorted = dict(sorted(by_class.items()))

    out = {
        "_schema": {
            "description": "Expansion-introduction era per craftable item "
                           "class, derived from Core.<EXP> gates around "
                           "AddCraft(typeof(X)) calls in ServUO Def*.cs craft "
                           "definitions. Ungated = Classic (T2A base game).",
            "source": "servuo: Scripts/Services/Craft/Def*.cs",
            "eras": ERA_ORDER,
            "generated_by": "tools/extract_expansion.py",
        },
        "by_class": by_class_sorted,
        "_meta": {
            "counts": counts,
            "total": len(by_class_sorted),
            "files_parsed": files,
            "per_file_class_count": per_file,
            "warnings": all_warnings,
        },
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print("wrote %s" % os.path.relpath(OUT_PATH, ROOT))
    print("total tagged classes: %d" % len(by_class_sorted))
    for e in ERA_ORDER:
        print("  %-8s %d" % (e, counts[e]))
    if all_warnings:
        print("warnings (%d):" % len(all_warnings))
        for w in all_warnings:
            print("  " + w)
    else:
        print("no parse warnings")


if __name__ == "__main__":
    main()
