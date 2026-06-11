# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Extract house-type data from ServUO into data/houses.json.

Two categories are produced:

1. CLASSIC (pre-set) houses — one row per HouseDeed subclass in
   Scripts/Multis/Deeds.cs. For each deed we read:
     * class           — the deed class name (e.g. StonePlasterHouseDeed)
     * multi_id         — first ctor arg to base(0x..., offset)
     * LabelNumber      — the deed's cliloc, resolved to a human name via
                          ../anima/data/cliloc.json
     * house_class      — the BaseHouse subclass returned by GetHouse(...)
   The BaseHouse subclass is then looked up in Scripts/Multis/Houses.cs for
   its footprint (AreaArray bounding box) and its MaxLockDown / MaxSecure
   constructor args (base(id, owner, MaxLockDown, MaxSecure)).
   Storage (lockdowns) and gold price are taken from the authoritative
   HousePlacementEntry table in Scripts/Multis/HousePlacementTool.cs, keyed
   by MultiID. Vendor sell price (per deed type) comes from
   Scripts/VendorInfo/SBHouseDeed.cs.

2. CUSTOMIZABLE FOUNDATIONS — the HouseFoundation entries from the same
   HousePlacementEntry table (2-Story and 3-Story sizes, plus the custom
   keep/castle plots). Each has its size label (cliloc), storage, lockdowns,
   cost, and multi_id.

Output: data/houses.json
  {
    "classic": [ {class, name, multi_id, footprint, lockdowns, secures,
                  price, house_class, deed_price, label_cliloc}, ... ],
    "foundations": [ {name, multi_id, footprint, lockdowns, secures,
                      price, category}, ... ]
  }

Stdlib only. Pragmatic: captures what parses, reports what it can't resolve.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVUO = "/Users/dkkang/dev/uo/servuo"
CLILOC = "/Users/dkkang/dev/uo/anima/data/cliloc.json"

DEEDS = os.path.join(SERVUO, "Scripts", "Multis", "Deeds.cs")
HOUSES = os.path.join(SERVUO, "Scripts", "Multis", "Houses.cs")
PLACEMENT = os.path.join(SERVUO, "Scripts", "Multis", "HousePlacementTool.cs")
SBHOUSE = os.path.join(SERVUO, "Scripts", "VendorInfo", "SBHouseDeed.cs")


def load_cliloc():
    with open(CLILOC, encoding="utf-8") as f:
        d = json.load(f)
    # keys may be str; normalise lookup by str(id)
    return {str(k): v for k, v in d.items()}


# --- Deeds.cs : deed class -> {multi_id, label, house_class} ----------------

DEED_CLASS_RE = re.compile(
    r"public\s+class\s+(\w+Deed|\w+Cottage\w*Deed)\s*:\s*HouseDeed\b", re.M)
# more general: any class X : HouseDeed
DEED_CLASS_RE = re.compile(r"public\s+class\s+(\w+)\s*:\s*HouseDeed\b", re.M)


def parse_deeds():
    text = open(DEEDS, encoding="utf-8-sig", errors="replace").read()
    # split into class bodies
    matches = list(DEED_CLASS_RE.finditer(text))
    deeds = []
    for i, m in enumerate(matches):
        name = m.group(1)
        if name == "HouseDeed":
            continue
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]

        # MultiID: first ctor arg of `: base(0x.., new Point3D(..))`
        # constructor is `public <Name>() : base(0x64, new Point3D(0, 4, 0))`
        mid = None
        bm = re.search(r":\s*base\s*\(\s*(0x[0-9A-Fa-f]+|\d+)\s*,", body)
        if bm:
            mid = int(bm.group(1), 0)

        # LabelNumber cliloc
        label = None
        lm = re.search(r"LabelNumber\b.*?return\s+(\d+)\s*;", body, re.S)
        if lm:
            label = int(lm.group(1))

        # GetHouse(...) -> `return new <HouseClass>(...)`
        hc = None
        gm = re.search(r"GetHouse\s*\([^)]*\)\s*\{[^}]*?return\s+new\s+(\w+)",
                       body, re.S)
        if gm:
            hc = gm.group(1)

        deeds.append({
            "class": name,
            "multi_id": mid,
            "label_cliloc": label,
            "house_class": hc,
        })
    return deeds


# --- Houses.cs : BaseHouse subclass -> footprint + MaxLockDown/MaxSecure -----

def parse_houses():
    text = open(HOUSES, encoding="utf-8-sig", errors="replace").read()
    cls_re = re.compile(r"public\s+class\s+(\w+)\s*:\s*BaseHouse\b", re.M)
    matches = list(cls_re.finditer(text))
    houses = {}
    for i, m in enumerate(matches):
        name = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]

        # MaxLockDown / MaxSecure from `: base(id, owner, ML, MS)`
        ml = ms = None
        bm = re.search(
            r":\s*base\s*\(\s*[^,]+,\s*owner\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", body)
        if bm:
            ml, ms = int(bm.group(1)), int(bm.group(2))

        # footprint = bounding box over ALL Rectangle2D(x, y, w, h) in the
        # first AreaArray declaration. Multi-rect houses (Keep, Tower) have an
        # odd shape, so the union bbox is the meaningful "plot" size.
        # Some classes (SmallShop) use AreaArray1 / AreaArray2 instead.
        footprint = None
        am = re.search(
            r"AreaArray\d*\s*=\s*new\s+Rectangle2D\[\]\s*\{(.*?)\}\s*;", body, re.S)
        if am:
            rects = re.findall(
                r"new\s+Rectangle2D\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)",
                am.group(1))
            if rects:
                xs0 = min(int(x) for x, y, w, h in rects)
                ys0 = min(int(y) for x, y, w, h in rects)
                xs1 = max(int(x) + int(w) for x, y, w, h in rects)
                ys1 = max(int(y) + int(h) for x, y, w, h in rects)
                footprint = f"{xs1 - xs0}x{ys1 - ys0}"

        houses[name] = {
            "max_lockdown": ml,
            "max_secure": ms,
            "footprint": footprint,
        }
    return houses


# --- HousePlacementTool.cs : HousePlacementEntry table -----------------------
# ctor: (type, description, storage, lockdowns, newStorage, newLockdowns,
#        vendors, cost, xOffset, yOffset, zOffset, multiID)

ENTRY_RE = re.compile(
    r"new\s+HousePlacementEntry\s*\(\s*typeof\(\s*(\w+)\s*\)\s*,\s*"
    r"(\d+)\s*,\s*"           # description cliloc
    r"(\d+)\s*,\s*(\d+)\s*,\s*"  # storage, lockdowns (old)
    r"(\d+)\s*,\s*(\d+)\s*,\s*"  # newStorage, newLockdowns
    r"(\d+)\s*,\s*"           # vendors
    r"(\d+)\s*,\s*"           # cost
    r"(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*"  # offsets
    r"(0x[0-9A-Fa-f]+)\s*\)", re.M)


def parse_placement():
    """Return list of dicts in file order, each tagged with which array it
    belongs to (classic / housesEJ / customContest / twoStory / threeStory)."""
    text = open(PLACEMENT, encoding="utf-8-sig", errors="replace").read()

    # find the array declarations to bound them
    array_markers = [
        ("classic", "m_ClassicHouses"),
        ("housesEJ", "m_HousesEJ"),
        ("customContest", "m_CustomHouseContest"),
        ("twoStory", "m_TwoStoryFoundations"),
        ("threeStory", "m_ThreeStoryFoundations"),
    ]
    bounds = []
    for tag, marker in array_markers:
        idx = text.find(marker + " =")
        if idx < 0:
            idx = text.find(marker)
        bounds.append((idx, tag))
    bounds.sort()

    def tag_for(pos):
        cur = None
        for idx, tag in bounds:
            if idx <= pos:
                cur = tag
            else:
                break
        return cur

    entries = []
    for m in ENTRY_RE.finditer(text):
        (htype, desc, storage, lockdowns, new_storage, new_lockdowns,
         vendors, cost, xo, yo, zo, multi) = m.groups()
        entries.append({
            "type": htype,
            "description": int(desc),
            "storage": int(storage),
            "lockdowns": int(lockdowns),
            "new_storage": int(new_storage),
            "new_lockdowns": int(new_lockdowns),
            "vendors": int(vendors),
            "cost": int(cost),
            "multi_id": int(multi, 16),
            "array": tag_for(m.start()),
        })
    return entries


# --- SBHouseDeed.cs : deed class -> vendor buy price -------------------------

def parse_deed_prices():
    text = open(SBHOUSE, encoding="utf-8-sig", errors="replace").read()
    prices = {}
    for m in re.finditer(
            r"GenericBuyInfo\([^,]+,\s*typeof\((\w+)\)\s*,\s*(\d+)", text):
        prices[m.group(1)] = int(m.group(2))
    return prices


def main():
    cliloc = load_cliloc()
    deeds = parse_deeds()
    houses = parse_houses()
    entries = parse_placement()
    deed_prices = parse_deed_prices()

    # index placement entries by multi_id (classic array gives storage/lockdowns)
    classic_by_mid = {}
    for e in entries:
        if e["array"] in ("classic", "housesEJ"):
            classic_by_mid.setdefault(e["multi_id"], e)

    warnings = []

    # --- classic houses (one per deed) ---
    classic = []
    for d in deeds:
        mid = d["multi_id"]
        name = None
        if d["label_cliloc"] is not None:
            name = cliloc.get(str(d["label_cliloc"]))
        if not name:
            name = d["class"]
            warnings.append(f"no cliloc name for {d['class']} (label={d['label_cliloc']})")

        hc = d["house_class"]
        hinfo = houses.get(hc, {})
        footprint = hinfo.get("footprint")
        secures = hinfo.get("max_secure")
        ml_class = hinfo.get("max_lockdown")

        pe = classic_by_mid.get(mid)
        house_name = None
        if pe:
            lockdowns = pe["lockdowns"]
            storage = pe["storage"]
            price = pe["cost"]
            # the placement-tool description cliloc reads cleaner than the
            # deed label (e.g. "Stone and plaster house" vs "deed to a ...")
            house_name = cliloc.get(str(pe["description"]))
        else:
            lockdowns = ml_class
            storage = None
            price = None
            warnings.append(f"no placement entry for multi 0x{mid:X} ({d['class']})")

        if not hc:
            warnings.append(f"no GetHouse class for {d['class']}")
        if footprint is None and hc:
            warnings.append(f"no footprint for house class {hc} ({d['class']})")

        # exterior render path (written by tools/render_house.py), if present
        png = None
        if mid is not None:
            cand = os.path.join(ROOT, "public", "img", "houses", f"0x{mid:X}.png")
            if os.path.exists(cand):
                png = f"/img/houses/0x{mid:X}.png"

        classic.append({
            "class": d["class"],
            "name": house_name or name,
            "deed_label": name,
            "multi_id": f"0x{mid:X}" if mid is not None else None,
            "png": png,
            "footprint": footprint or "standard for size",
            "lockdowns": lockdowns,
            "secures": secures if secures is not None else "standard for size",
            "price": price,                      # placement-tool gold cost
            "deed_price": deed_prices.get(d["class"]),  # NPC vendor buy price
            "house_class": hc,
            "label_cliloc": d["label_cliloc"],
        })

    # --- customizable foundations ---
    foundations = []
    seen_found = set()
    for e in entries:
        if e["array"] not in ("twoStory", "threeStory", "customContest"):
            continue
        if e["type"] != "HouseFoundation":
            continue
        if e["multi_id"] in seen_found:
            continue
        seen_found.add(e["multi_id"])
        label = cliloc.get(str(e["description"])) or f"cliloc {e['description']}"
        cat = {
            "twoStory": "2-Story Customizable",
            "threeStory": "3-Story Customizable",
            "customContest": "Custom Keep/Castle",
        }[e["array"]]
        foundations.append({
            "name": label,
            "multi_id": f"0x{e['multi_id']:X}",
            "lockdowns": e["lockdowns"],
            "secures": e["storage"],   # 'storage' column = secure storage budget
            "price": e["cost"],
            "category": cat,
        })

    doc = {
        "_schema": {
            "description": "ServUO house types. 'classic' = pre-set HouseDeed "
                           "houses (Scripts/Multis/Deeds.cs); 'foundations' = "
                           "customizable HouseFoundation plots. Storage/lockdowns/"
                           "price from the HousePlacementEntry table in "
                           "Scripts/Multis/HousePlacementTool.cs; secures (per "
                           "classic house) and footprint from Scripts/Multis/"
                           "Houses.cs base(id,owner,MaxLockDown,MaxSecure) and "
                           "AreaArray; deed_price from Scripts/VendorInfo/"
                           "SBHouseDeed.cs; names resolved via anima cliloc.json. "
                           "Note: lockdown/secure totals scale by "
                           "BaseHouse.GlobalBonusStorageScalar in-game.",
            "extracted_by": "tools/extract_houses.py",
            "sources": [
                "servuo: Scripts/Multis/Deeds.cs",
                "servuo: Scripts/Multis/Houses.cs",
                "servuo: Scripts/Multis/HousePlacementTool.cs",
                "servuo: Scripts/VendorInfo/SBHouseDeed.cs",
                "anima: data/cliloc.json",
            ],
        },
        "classic": classic,
        "foundations": foundations,
    }

    out = os.path.join(ROOT, "data", "houses.json")
    with open(out, "w") as f:
        json.dump(doc, f, indent=2, sort_keys=False)
        f.write("\n")

    print(f"classic houses : {len(classic)}")
    print(f"foundations    : {len(foundations)}")
    print(f"wrote {out}")
    if warnings:
        print(f"\nwarnings ({len(warnings)}):")
        for w in warnings:
            print(f"  {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
