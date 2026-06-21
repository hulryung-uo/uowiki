#!/usr/bin/env python3
"""tools/cliloc.py — multilingual UO cliloc string lookup with English fallback.

The classic client stores all localized strings (item/spell/skill names, system
messages, tooltips) in per-language Cliloc.* files, keyed by an integer cliloc
number. The anima pipeline parses those binaries into committed JSON tables that
both this wiki and anima read (same files the extractors already use for English
names, e.g. extract_items.py / extract_weapons.py):

    ../anima/data/cliloc.json        — English (enu), the base/fallback
    ../anima/data/cliloc.kor.json    — Korean
    ../anima/data/cliloc.jpn.json    — Japanese
    ../anima/data/cliloc.{cht,chs,deu,esp,fra}.json — extra languages (available,
                                       not built by the wiki today)

A localized file only carries the numbers that language actually translated; the
rest fall back to English exactly as the client does. So every lookup resolves:

    locale string  ->  English string  ->  caller-supplied fallback

Public API:
    Cliloc(locale)            — string table for one locale, English-backed.
        .get(number, fallback=None)   localized text, English fallback, then `fallback`
        .has(number)                  True if known in locale or English
        number in cliloc              same as .has()
        cliloc[number]                like .get() but raises KeyError if unknown
    loader(locale)            — cached Cliloc instance (reuse across a generator run)
    text(number, locale, fallback)    — one-shot convenience over loader()

Locale codes match i18n_labels.LOCALES (en/ko/ja) plus the extra language codes
above. Unknown locales raise KeyError. Numbers may be int or str.

Usage:
    from cliloc import loader
    name = loader("ko").get(1015012, fallback="Greater Heal")   # -> "상급 치료"

Self-test: python3 tools/cliloc.py --selftest
Stdlib only (Python 3.8+).
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WIKI = os.path.dirname(HERE)
ROOT = os.path.dirname(WIKI)
CLILOC_DIR = os.path.join(ROOT, "anima", "data")

ENGLISH_FILE = "cliloc.json"

# wiki/locale code -> cliloc json filename under CLILOC_DIR.
LOCALE_FILES = {
    "en": ENGLISH_FILE,
    "ko": "cliloc.kor.json",
    "ja": "cliloc.jpn.json",
    # extra languages parsed and available, but not part of LOCALES yet:
    "cht": "cliloc.cht.json",
    "chs": "cliloc.chs.json",
    "de": "cliloc.deu.json",
    "es": "cliloc.esp.json",
    "fr": "cliloc.fra.json",
}

_tables = {}   # filename -> {str(number): text}
_loaders = {}  # locale   -> Cliloc


def _load(filename):
    """Load and cache one cliloc table by filename."""
    table = _tables.get(filename)
    if table is None:
        path = os.path.join(CLILOC_DIR, filename)
        with open(path, encoding="utf-8") as f:
            table = json.load(f)
        _tables[filename] = table
    return table


class Cliloc:
    """Localized cliloc string table for one locale, backed by English.

    Resolution order for get(n): locale string -> English string -> fallback.
    A localized entry that is missing or empty falls through to English, so the
    table behaves like the client (untranslated numbers show English).
    """

    def __init__(self, locale="en"):
        filename = LOCALE_FILES.get(locale)
        if filename is None:
            raise KeyError(
                "cliloc: unknown locale %r (known: %s)"
                % (locale, ", ".join(sorted(LOCALE_FILES)))
            )
        self.locale = locale
        self.english = _load(ENGLISH_FILE)
        self.local = self.english if filename == ENGLISH_FILE else _load(filename)

    def get(self, number, fallback=None):
        key = str(number)
        txt = self.local.get(key)
        if not txt:  # missing or empty -> English fallback
            txt = self.english.get(key)
        return txt if txt is not None else fallback

    def has(self, number):
        key = str(number)
        return key in self.local or key in self.english

    __contains__ = has

    def __getitem__(self, number):
        sentinel = object()
        txt = self.get(number, sentinel)
        if txt is sentinel:
            raise KeyError(number)
        return txt


def loader(locale="en"):
    """Cached Cliloc for `locale` (reuse across a generator run)."""
    inst = _loaders.get(locale)
    if inst is None:
        inst = _loaders[locale] = Cliloc(locale)
    return inst


def text(number, locale="en", fallback=None):
    """One-shot localized lookup with English fallback, then `fallback`."""
    return loader(locale).get(number, fallback)


def _selftest():
    # (cliloc number, English, expected Korean, expected Japanese)
    cases = [
        (1015012, "Greater Heal", "상급 치료", "回復-強"),
        (1023003, "Bard", "음유시인", "Bard (バード)"),
        (3000091, "Cancel", "취소", "キャンセル"),
    ]
    en, ko, ja = loader("en"), loader("ko"), loader("ja")
    ok = True
    for num, e, k, j in cases:
        for name, ld, want in (("en", en, e), ("ko", ko, k), ("ja", ja, j)):
            got = ld.get(num)
            flag = "ok " if got == want else "FAIL"
            if got != want:
                ok = False
            print("  [%s] %-3s %-8d %r" % (flag, name, num, got))
    # English fallback: a number absent from the Korean table must yield English.
    missing = next(
        (n for n in en.english if n not in ko.local and en.english[n]), None
    )
    if missing is not None:
        got = ko.get(missing)
        want = en.english[missing]
        flag = "ok " if got == want else "FAIL"
        if got != want:
            ok = False
        print("  [%s] ko-fallback %s -> English %r" % (flag, missing, got))
    # caller fallback for a number nobody knows.
    got = ko.get(999999999, fallback="<none>")
    flag = "ok " if got == "<none>" else "FAIL"
    if got != "<none>":
        ok = False
    print("  [%s] unknown -> caller fallback %r" % (flag, got))
    print("tables loaded:", ", ".join(sorted(_tables)))
    return ok


def main(argv):
    if "--selftest" in argv:
        return 0 if _selftest() else 1
    if len(argv) >= 2 and argv[1].lstrip("-").isdigit():
        num = int(argv[1].lstrip("-")) if argv[1].startswith("-") is False else int(argv[1])
        loc = argv[2] if len(argv) >= 3 else "en"
        print(loader(loc).get(num, fallback="(not found)"))
        return 0
    print(__doc__)
    print("Examples:\n  python3 tools/cliloc.py --selftest"
          "\n  python3 tools/cliloc.py 1015012 ko")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
