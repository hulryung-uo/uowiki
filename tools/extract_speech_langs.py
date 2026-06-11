# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Extract MULTI-LANGUAGE speech-keyword trigger phrases from the client's
speech.mul into data/speech_languages.json.

The companion tool tools/extract_speech.py mines ServUO for which numeric
keyword id triggers each spoken command and what it does. THIS tool answers the
other half: for a given keyword id, what does a player actually *type*? The
answer depends on the client's language, because the client owns the keyword
table and matches your typed phrase against it to resolve the id (see the page
"How spoken commands are matched"). Our shard's client file is an INTERNATIONAL
build: a single speech.mul that carries the trigger phrases for many languages
at once, so one keyword id (e.g. 0x0023 "lock down") lists its phrase in
Chinese, German, English, Spanish, French, Japanese, and Korean side by side.

speech.mul FORMAT (this international build):
  A flat sequence of entries, each:
    [u16 keyword id,  big-endian]
    [u16 string length, big-endian]
    [UTF-8 bytes of that length]
  ~6128 entries; many entries share a keyword id (one per language / variant).
  Phrases are usually wrapped in `*` wildcards (`*i ban thee*`); some are not.
  Japanese phrases are commonly prefixed with a fullwidth ＠ (U+FF20) and appear
  in hiragana / katakana variants of the same word.

LANGUAGE DETECTION (rules applied in this order — see detect_lang):
  1. Hangul (U+AC00–U+D7A3)                                        -> ko (Korean)
  2. Han ideographs (U+4E00–U+9FFF, U+3400–U+4DBF) and NO kana     -> zh (Chinese)
  3. Katakana/Hiragana (U+3040–U+30FF) OR a leading ＠ (U+FF20)    -> ja (Japanese)
  4. Latin script:
       - has ä/ö/ü/ß                                              -> de (German)
       - has ñ/¿/¡                                                -> es (Spanish)
       - has French diacritics (é è ê à â ç ù î ï)                -> fr (French)
       - matches this keyword's known ServUO English phrase        -> en (English)
         (anchored from data/speech_commands.json BEFORE markers, because in
          this build the German phrase usually precedes English in file order)
       - has a German marker word (ich, alle, wo, …)              -> de (German)
       - has a Spanish marker word (quiero, todos, donde, …)      -> es (Spanish)
       - has a French marker word (je, placer, ou, …)             -> fr (French)
       - else                                                     -> en? (pending)
     Pending plain-ASCII phrases (no diacritic, no marker, not the known English
     phrase) are resolved by ELIMINATION: the first fills the English slot if
     still empty; any remainder is assigned to the single still-missing slot
     among de/es/fr, else labelled "lat" (unknown Latin) rather than guessed.

OUTPUT: data/speech_languages.json
  { "<keyword_hex>": { "en": [...], "de": [...], "es": [...], "fr": [...],
                       "zh": [...], "ja": [...], "ko": [...], "lat": [...] } }
  Phrases are shown CLEAN: surrounding `*` wildcards and the leading ＠ prefix
  are stripped for display. Empty language buckets are omitted per keyword.

Stdlib only.
"""

import json
import os
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEECH_MUL = "/Users/dkkang/dev/uo/uo-resource/speech.mul"
OUT = os.path.join(ROOT, "data", "speech_languages.json")

CMDS = os.path.join(ROOT, "data", "speech_commands.json")

LANG_ORDER = ["en", "de", "es", "fr", "zh", "ja", "ko", "lat"]
LANG_LABEL = {
    "en": "English", "de": "German", "es": "Spanish", "fr": "French",
    "zh": "Chinese", "ja": "Japanese", "ko": "Korean", "lat": "Latin (unknown)",
}

# German marker words: catch plain-ASCII German phrases that carry no umlaut
# (the file order in this build puts the German phrase BEFORE the English one for
# many keywords, so a naive "first plain-ASCII = English" guess mislabels them).
DE_MARKERS = {"ich", "alle", "moechte", "wo", "haendler", "eins", "zwei", "drei",
              "vier", "fuenf", "langsam", "schnell", "vorwaerts", "rueckwaerts",
              "du", "dich", "mir", "sollen", "bewachen", "kommen", "bleiben",
              "stehen", "folgen", "toeten", "trete", "verbanne", "verlasse",
              "gilde", "ueberdenke", "gesinnung", "scheck", "zurueckverlangen",
              "wache", "halt", "weiter", "lehre", "lehren", "trainieren",
              "kontostand", "kontoauszug"}
# Spanish / French marker words used to disambiguate plain-ASCII Latin phrases.
ES_MARKERS = {"quiero", "todos", "matad", "colocar", "prohibir", "pecados",
              "considerar", "no", "si", "banco", "todo", "donde", "vendedor",
              "lento", "uno", "dos", "tres", "atras", "detras", "delante",
              "entrenar", "ensenar", "venid", "seguidme", "quedaos", "proteged",
              "deteneos", "dimito", "gremio", "establo", "reclamar", "saldo"}
FR_MARKERS = {"je", "placer", "tuer", "bannis", "peches", "cheque", "oui",
              "non", "retire", "tous", "ou", "vendeur", "lent", "vous", "un",
              "deux", "trois", "avant", "arriere", "suivre", "venir", "rester",
              "garder", "arreter", "quitte", "guilde", "ecurie", "reprendre",
              "relever", "examiner", "former", "enseigner", "solde", "releve"}

DE_UMLAUTS = "äöüßÄÖÜ"
ES_CHARS = "ñ¿¡Ñ"
FR_DIACRITICS = "éèêàâçùîïÉÈÊÀÂÇÙÎÏ"


def has_any(s, chars):
    return any(c in s for c in chars)


def words(s):
    """Lowercased word tokens, accent-stripped, for marker matching."""
    cleaned = []
    for ch in s.lower():
        if ch.isalpha() or ch == " ":
            # fold common accents so markers like "péchés" match "peches"
            cleaned.append({
                "á": "a", "à": "a", "â": "a", "ä": "a",
                "é": "e", "è": "e", "ê": "e",
                "í": "i", "î": "i", "ï": "i",
                "ó": "o", "ô": "o", "ö": "o",
                "ú": "u", "ù": "u", "û": "u", "ü": "u",
                "ç": "c", "ñ": "n",
            }.get(ch, ch))
        else:
            cleaned.append(" ")
    return set("".join(cleaned).split())


def has_han(s):
    return any("一" <= c <= "鿿" or "㐀" <= c <= "䶿" for c in s)


def has_hangul(s):
    return any("가" <= c <= "힣" for c in s)


def has_kana(s):
    return any("぀" <= c <= "ヿ" for c in s)


def detect_lang(raw, en_ref=None):
    """Return a language code per the rules above. `raw` is the cleaned phrase
    (wildcards and the ＠ prefix already stripped). `en_ref` is the set of known
    canonical English phrases for this keyword (from speech_commands.json), used
    to anchor `en` even when the German phrase precedes it in file order."""
    s = raw
    if has_hangul(s):
        return "ko"
    if has_han(s) and not has_kana(s):
        return "zh"
    if has_kana(s):
        return "ja"
    # Latin script from here on.
    if has_any(s, DE_UMLAUTS):
        return "de"
    if has_any(s, ES_CHARS):
        return "es"
    if has_any(s, FR_DIACRITICS):
        return "fr"
    # Anchor English on the keyword's known ServUO phrase before marker tests, so
    # a real English phrase is never stolen by a German/Spanish/French marker.
    if en_ref and s.strip().lower() in en_ref:
        return "en"
    w = words(s)
    if w & DE_MARKERS:
        return "de"
    if w & ES_MARKERS:
        return "es"
    if w & FR_MARKERS:
        return "fr"
    # Plain ASCII, no markers: presumed English, but flagged for elimination.
    return "en?"


def clean_phrase(s):
    """Strip surrounding `*` wildcards and a leading fullwidth ＠ for display.
    Returns (clean_text, had_at)."""
    s = s.strip()
    s = s.strip("*").strip()
    had_at = False
    if s.startswith("＠"):  # fullwidth ＠
        had_at = True
        s = s[1:].strip()
    return s, had_at


def parse_mul(path):
    """Yield (keyword_id, raw_string) entries in file order."""
    with open(path, "rb") as f:
        data = f.read()
    off = 0
    n = len(data)
    while off + 4 <= n:
        kid = struct.unpack_from(">H", data, off)[0]
        ln = struct.unpack_from(">H", data, off + 2)[0]
        start = off + 4
        end = start + ln
        if end > n:
            break
        raw = data[start:end].decode("utf-8", "replace")
        yield kid, raw
        off = end


def load_en_refs():
    """Map keyword id (int) -> set of canonical English phrases (lowercased,
    placeholders/<...> and slash-variants split out) from speech_commands.json.
    Used to anchor the `en` slot regardless of file order."""
    refs = {}
    if not os.path.exists(CMDS):
        return refs
    with open(CMDS, encoding="utf-8") as f:
        doc = json.load(f)
    for section, rows in doc.items():
        if section.startswith("_"):
            continue
        for row in rows:
            kid = row.get("keyword_id")
            phrase = row.get("phrase")
            if not kid or not phrase:
                continue
            kid = int(kid, 16) if isinstance(kid, str) else kid
            variants = set()
            for part in phrase.split("/"):
                # drop <pet name> / <vendor name> style placeholders
                cleaned = part.replace("<pet name>", "").replace("<vendor name>", "")
                cleaned = cleaned.replace("<npc name>", "").replace("<amount>", "")
                cleaned = cleaned.replace("<", "").replace(">", "")
                cleaned = " ".join(cleaned.split()).strip().lower()
                if cleaned:
                    variants.add(cleaned)
            refs.setdefault(kid, set()).update(variants)
    return refs


def resolve_ambiguous(buckets):
    """Assign 'en?' (plain-ASCII, marker-less) phrases for one keyword.

    English was already anchored in detect_lang via the keyword's known ServUO
    phrase. Whatever remains in 'en?' is a plain-ASCII phrase carrying no
    diacritic and no marker word. The first such phrase fills the English slot
    only if it is still empty (a keyword whose English phrase isn't in
    speech_commands.json, e.g. numbers/directions). Any remaining phrases are
    leftover de/es/fr forms; assign each to a single still-missing slot among
    de/es/fr by elimination, else 'lat'.
    """
    pending = buckets.pop("en?", [])
    if not pending:
        return
    if "en" not in buckets:
        buckets.setdefault("en", []).append(pending.pop(0))
    for phrase in pending:
        missing = [l for l in ("de", "es", "fr") if l not in buckets]
        if len(missing) == 1:
            buckets.setdefault(missing[0], []).append(phrase)
        else:
            buckets.setdefault("lat", []).append(phrase)


def main():
    if not os.path.exists(SPEECH_MUL):
        sys.exit(f"ERROR: speech.mul not found at {SPEECH_MUL}")

    en_refs = load_en_refs()

    # Group raw phrases by keyword id (preserve file order).
    grouped = {}
    total_entries = 0
    for kid, raw in parse_mul(SPEECH_MUL):
        total_entries += 1
        grouped.setdefault(kid, []).append(raw)

    result = {}
    for kid in sorted(grouped):
        # ordered-dict buckets keyed by lang code; 'en?' is the pending bucket
        buckets = {}
        seen = set()
        en_ref = en_refs.get(kid)
        for raw in grouped[kid]:
            clean, _had_at = clean_phrase(raw)
            if not clean:
                continue
            lang = detect_lang(clean, en_ref)
            # de-dup identical (lang, text) pairs (e.g. kana hira/kata of same id
            # both clean to distinct text so kept; exact dups dropped)
            key = (lang, clean)
            if key in seen:
                continue
            seen.add(key)
            buckets.setdefault(lang, []).append(clean)
        resolve_ambiguous(buckets)
        # Emit in canonical language order, omitting empty buckets.
        ordered = {l: buckets[l] for l in LANG_ORDER if buckets.get(l)}
        if ordered:
            result[f"0x{kid:04X}"] = ordered

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # ---- stats -------------------------------------------------------------
    lang_counts = {l: 0 for l in LANG_ORDER}
    lang_keywords = {l: 0 for l in LANG_ORDER}
    total_phrases = 0
    for kw in result.values():
        for l, phrases in kw.items():
            lang_counts[l] += len(phrases)
            lang_keywords[l] += 1
            total_phrases += len(phrases)

    real_langs = ("en", "de", "es", "fr", "zh", "ja", "ko")
    multi4 = sum(1 for kw in result.values()
                 if sum(1 for l in real_langs if kw.get(l)) >= 4)

    print(f"speech.mul entries parsed : {total_entries}")
    print(f"keywords covered          : {len(result)}")
    print(f"keywords with >=4 langs   : {multi4}")
    print(f"total clean phrases        : {total_phrases}")
    print("languages present (phrases / keywords):")
    for l in LANG_ORDER:
        if lang_counts[l]:
            print(f"  {l} {LANG_LABEL[l]:18s}: {lang_counts[l]:5d} phrases  "
                  f"in {lang_keywords[l]:4d} keywords")
    print(f"wrote {OUT}")

    # ---- spot checks -------------------------------------------------------
    print("\nSPOT CHECKS (per-language phrases):")
    spot = {
        0x0002: "bank",
        0x0023: "lock down",
        0x0028: "trash barrel",
        0x0034: "ban",
        0x0032: "consider sins",
    }
    for kid, label in spot.items():
        hexk = f"0x{kid:04X}"
        print(f"\n  {hexk}  ({label})")
        kw = result.get(hexk, {})
        for l in LANG_ORDER:
            if kw.get(l):
                print(f"    {l}: {' / '.join(kw[l])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
