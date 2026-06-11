#!/usr/bin/env python3
"""Extract per-dungeon spawn data from ServUO Spawns/*.xml.

Parses every spawn-point definition in ../servuo/Spawns/*.xml, groups the points
by the dungeon they belong to, and records, per dungeon:

  * facet        — which spawn file (felucca/trammel/ilshenar/malas/tokuno/termur/...)
  * centre       — average CentreX/CentreY of its spawn points (rough map location)
  * creatures    — the set of creature classes that spawn there, each with the
                   total MX (max-count) summed across points as a rough frequency,
                   plus a bestiary link (/bestiary/<group>/<slug>/) when the class
                   matches a creature in data/creatures.json
  * point_count  — number of spawn points grouped under the dungeon

Spawn points are grouped by a normalised dungeon key. ServUO's spawn <Name>s are
inconsistent ("Despise#25", "shame 84", "mal doom lich/...", "CovetousSpawner3"),
so a mapping table + heuristics fold the many name variants onto canonical dungeon
names. Non-dungeon points (overworld regions, towns, vendors, wildlife, quests,
healers) are filtered out.

Output: data/dungeon_spawns.json
Pure stdlib (xml.etree, json, re, glob).
"""

import glob
import json
import os
import re
import xml.etree.ElementTree as ET
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # uowiki/
SPAWNS = os.path.join(ROOT, "..", "servuo", "Spawns")
CREATURES_JSON = os.path.join(ROOT, "data", "creatures.json")
OUT = os.path.join(ROOT, "data", "dungeon_spawns.json")

# --- canonical dungeon table -------------------------------------------------
# Maps a regex (matched case-insensitively against the spawn <Name>, after the
# part before '#' is taken) to a canonical dungeon name. First match wins, so
# order matters (more specific patterns first). A None value means "drop it".
#
# These are the actual DUNGEONS — overworld regions, towns, farms, vendor and
# healer spawners, and quest givers are intentionally excluded.
DUNGEON_RULES = [
    (r"^despiserevamped", "Despise"),
    (r"^despise", "Despise"),
    (r"\bdespise\b", "Despise"),
    (r"^deceit", "Deceit"),
    (r"\bdeceit\b", "Deceit"),
    (r"^covetous", "Covetous"),
    (r"\bcovetous\b", "Covetous"),
    (r"^shame", "Shame"),
    (r"\bshame\b", "Shame"),
    (r"^wrong", "Wrong"),
    (r"\bwrong\b", "Wrong"),
    (r"^hythloth", "Hythloth"),
    (r"\bhythloth\b", "Hythloth"),
    (r"^destard", "Destard"),
    (r"\bdestard\b", "Destard"),
    (r"^khaldun", "Khaldun"),
    (r"^orccaves?", "Orc Cave"),
    (r"^orccave", "Orc Cave"),
    (r"^ratmancave", "Spider Cave"),  # Spider Cave / ratman cave (LL)
    (r"^terathankeep", "Terathan Keep"),
    (r"^tera[ /]", "Terathan Keep"),
    (r"^paintedcaves", "Painted Caves"),
    (r"painted cave", "Painted Caves"),
    (r"^prismoflight", "Prism of Light"),
    (r"prism of light", "Prism of Light"),
    (r"^palaceofparoxysmus", "Palace of Paroxysmus"),
    (r"^blightedgrove", "Blighted Grove"),
    (r"^sanctuary", "Sanctuary"),
    (r"^fire\b", "Fire Dungeon"),
    (r"^fire ?2?$", "Fire Dungeon"),
    (r"^ice\b", "Ice Dungeon"),
    (r"\bwind\b", "Wind"),
    (r"^wisp$", "Wisp Dungeon"),
    (r"^ankh$", "Ankh Dungeon"),
    (r"^ahnkdungeon", "Ankh Dungeon"),
    # Ilshenar
    (r"^sorcerers", "Sorcerer's Dungeon"),
    (r"^scorcersdungeon", "Sorcerer's Dungeon"),
    (r"^scorers", "Sorcerer's Dungeon"),
    (r"^spectre", "Spectre Dungeon"),
    (r"^exodus", "Exodus Dungeon"),
    (r"^blood$", "Blood Dungeon"),
    (r"^rock$", "Rock Dungeon"),
    (r"^ancientlair", "Ancient Lair"),
    # Malas
    (r"^doom$", "Doom"),
    (r"^doomgauntlet", "Doom"),
    (r"\bdoom\b", "Doom"),
    (r"^labyrinth", "Labyrinth"),
    (r"\blabyrinth\b", "Labyrinth"),
    (r"^bedlam", "Bedlam"),
    (r"\bbedlam\b", "Bedlam"),
    # Tokuno
    (r"^fandancersdojo", "Fan Dancer's Dojo"),
    (r"^yom?utso?mines", "Yomotsu Mines"),
    (r"^yamotsu mine", "Yomotsu Mines"),
    (r"^thecitadel", "The Citadel"),
    (r"^citadel$", "The Citadel"),
    # Twisted Weald (ML)
    (r"^twistedweald", "Twisted Weald"),
    # Underworld (SA)
    (r"underworld", "Underworld"),
    # Solen Hives (Felucca/Trammel underground) — descriptive spawn names
    (r"\bsolen\b", "Solen Hive"),
    (r"^ant ?lion", "Solen Hive"),
]
DUNGEON_RE = [(re.compile(p, re.I), name) for p, name in DUNGEON_RULES]

# Spawn names that look dungeon-ish but are support/quest entries we never want
# as dungeon spawn points (they hold healers, quest NPCs, crates, etc.).
DROP_RE = re.compile(
    r"healer|quest|crate|trigger|entrance|entrence|barrier|magickey|"
    r"questgiver|teleroom|spawnerbarrier|spawnerrose",
    re.I,
)

FACET_FROM_FILE = {
    "felucca": "Felucca",
    "trammel": "Trammel",
    "ilshenar": "Ilshenar",
    "malas": "Malas",
    "tokuno": "Tokuno",
    "termur": "Ter Mur",
    "twistedweald": "Felucca",       # Twisted Weald sits on Felucca facet
    "underworld": "Ter Mur",         # Stygian Abyss / Underworld
    "solenhives": "Felucca",
    "eodon": "Ter Mur",
    "gravewaterlake": "Trammel",
    "treasuresofkotl": "Ter Mur",
    "theexodusencounterquest": "Ilshenar",
}


def dungeon_for(name):
    """Return canonical dungeon name for a spawn <Name>, or None to drop it."""
    base = name.split("#", 1)[0].strip()
    if DROP_RE.search(name):
        return None
    for rx, canon in DUNGEON_RE:
        if rx.search(base):
            return canon
    return None


# Non-creature spawn objects (treasure chests, loot/static items) to skip.
NON_CREATURE_RE = re.compile(
    r"^(treasurelevel|treasure|.*chest$|.*addon$|relic|barrier|teleporter)",
    re.I,
)


def parse_objects(objects2):
    """Yield (creature_class, max_count) from an Objects2 string.

    Format: 'Type:MX=n:...:OBJ=Type2:MX=m:...'. Split on ':OBJ=', take the
    leading word of each chunk as the class, and MX=n as the max count. The
    class token can carry random-spawn syntax like 'Silenii,{RND,4,8}', so we
    keep only the part before the first comma. Treasure/loot objects are skipped.
    """
    if not objects2:
        return
    for chunk in objects2.split(":OBJ="):
        chunk = chunk.strip()
        if not chunk:
            continue
        # The class token can carry trailing spawn syntax: random-count
        # ',{RND,4,8}' or trigger-mob '/Combatant/TRIGMOB/...'. Keep the
        # leading word before the first comma or slash.
        cls = chunk.split(":", 1)[0].split(",", 1)[0].split("/", 1)[0].strip()
        if not cls or NON_CREATURE_RE.match(cls):
            continue
        m = re.search(r"\bMX=(\d+)", chunk)
        mx = int(m.group(1)) if m else 1
        yield cls, mx


BESTIARY_DIR = os.path.join(ROOT, "src", "content", "docs", "bestiary")


def load_creature_index():
    """class-lower -> {'class','name','group','slug'} from data/creatures.json.

    The slug and display name mirror gen_bestiary; the *group* is read from the
    actual generated bestiary files on disk (slug -> group dir) so the links are
    guaranteed to resolve, rather than reproducing classify() heuristics.
    """
    def slug(cls):
        return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])",
                      "-", cls).lower()

    def display(c):
        name = c.get("name")
        if name:
            name = re.sub(r"^(a|an|the)\s+", "", name.strip(), flags=re.I)
            if name:
                return name.title()
        return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])",
                      " ", c["class"])

    # slug -> group, scanned from the generated bestiary tree
    slug_group = {}
    if os.path.isdir(BESTIARY_DIR):
        for grp in os.listdir(BESTIARY_DIR):
            gdir = os.path.join(BESTIARY_DIR, grp)
            if not os.path.isdir(gdir):
                continue
            for fn in os.listdir(gdir):
                if fn.endswith(".md") and fn != "index.md":
                    slug_group[fn[:-3]] = grp

    creatures = json.load(open(CREATURES_JSON))["creatures"]
    idx = {}
    for c in creatures:
        s = slug(c["class"])
        grp = slug_group.get(s)
        entry = {"class": c["class"], "name": display(c), "slug": s}
        if grp:
            entry["group"] = grp
        idx[c["class"].lower()] = entry
    return idx


def main():
    cidx = load_creature_index()

    # dungeon -> facet -> aggregation
    data = defaultdict(lambda: {
        "facets": defaultdict(int),
        "sumx": 0, "sumy": 0, "n_centre": 0,
        "creatures": defaultdict(int),
        "point_count": 0,
    })

    for path in sorted(glob.glob(os.path.join(SPAWNS, "*.xml"))):
        fkey = os.path.splitext(os.path.basename(path))[0].lower()
        facet = FACET_FROM_FILE.get(fkey, fkey.title())
        try:
            tree = ET.parse(path)
        except ET.ParseError:
            continue
        for pt in tree.getroot().findall("Points"):
            name = (pt.findtext("Name") or "").strip()
            if not name:
                continue
            dn = dungeon_for(name)
            if not dn:
                continue
            d = data[dn]
            d["point_count"] += 1
            d["facets"][facet] += 1
            cx, cy = pt.findtext("CentreX"), pt.findtext("CentreY")
            if cx and cy:
                try:
                    d["sumx"] += int(cx)
                    d["sumy"] += int(cy)
                    d["n_centre"] += 1
                except ValueError:
                    pass
            for cls, mx in parse_objects(pt.findtext("Objects2")):
                # Aggregate case-insensitively; prefer the canonical class name
                # from the bestiary index when it matches.
                hit = cidx.get(cls.lower())
                key = hit["class"] if hit else cls
                d["creatures"][key] += mx

    out = {}
    for dn, d in sorted(data.items()):
        # dominant facet
        facet = max(d["facets"].items(), key=lambda kv: kv[1])[0]
        centre = None
        if d["n_centre"]:
            centre = [round(d["sumx"] / d["n_centre"]),
                      round(d["sumy"] / d["n_centre"])]
        creatures = []
        for cls, mx in sorted(d["creatures"].items(),
                              key=lambda kv: (-kv[1], kv[0].lower())):
            entry = {"class": cls, "max": mx}
            hit = cidx.get(cls.lower())
            if hit:
                entry["name"] = hit["name"]
                if "group" in hit:
                    entry["link"] = f"/bestiary/{hit['group']}/{hit['slug']}/"
            creatures.append(entry)
        out[dn] = {
            "facet": facet,
            "centre": centre,
            "creatures": creatures,
            "point_count": d["point_count"],
        }

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"wrote {OUT}")
    print(f"dungeons: {len(out)}")
    for dn in sorted(out):
        info = out[dn]
        linked = sum(1 for c in info["creatures"] if "link" in c)
        print(f"  {dn:24s} {info['facet']:9s} "
              f"pts={info['point_count']:4d} "
              f"creatures={len(info['creatures']):3d} (linked {linked}) "
              f"centre={info['centre']}")

    def sample(dn):
        cs = out.get(dn, {}).get("creatures", [])
        names = [c.get("name", c["class"]) for c in cs[:18]]
        print(f"\n{dn} ({len(cs)} creature classes): " + ", ".join(names))

    sample("Despise")
    sample("Deceit")
    sample("Destard")


if __name__ == "__main__":
    main()
