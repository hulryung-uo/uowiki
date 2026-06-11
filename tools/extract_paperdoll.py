# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render UO paperdoll reference images: a nude body gump composited with
layered equipment gumps, exactly as ClassicUO's PaperDollInteractable does.

Algorithm (verified against classicuo/src/ClassicUO.Client/Game/UI/Controls/
PaperDollInteractable.cs + Game/Constants.cs):

  1. Base body gump: MALE = 0x000C, FEMALE = 0x000D, drawn first at (0,0).
  2. Each wearable's paperdoll gump id = item AnimID + MALE_GUMP_OFFSET (50000)
     or + FEMALE_GUMP_OFFSET (60000). AnimID comes from tiledata.mul. If the
     female gump is missing, fall back to the male gump.
  3. Equipment gumps are drawn OVER the body in a fixed layer order (see
     LAYER_ORDER below), each at its own (0,0) — the gump art already carries
     the correct on-doll position. Composited with alpha.
  4. Each item's hue tints its (grayscale) gump via the hues.mul ramp, same as
     tools/apply_hues.py. PartialHue == full hue for grayscale armor/clothing.

Outputs:
  public/img/paperdoll/body-male.png, body-female.png   (nude bodies)
  public/img/paperdoll/suit-<name>.png                  (full outfits, male)
  public/img/paperdoll/item-<slug>.png                  (single equipped item)
  data/paperdoll.json                                   (manifest)

Run:  uv run --script tools/extract_paperdoll.py
"""

from __future__ import annotations

import json
import os
import struct
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
TILEDATA = os.path.join(UO_DIR, "tiledata.mul")
HUES_MUL = os.path.join(UO_DIR, "hues.mul")
GUMP_PATTERN = "build/gumpartlegacymul/%08d.tga"

MALE_GUMP_OFFSET = 50000
FEMALE_GUMP_OFFSET = 60000
BODY_MALE = 0x000C
BODY_FEMALE = 0x000D

# Layer draw order (back to front), from PaperDollInteractable._layerOrder.
LAYER_ORDER = [
    "Cloak", "Shirt", "Pants", "Shoes", "Legs", "Arms", "Torso", "Tunic",
    "Ring", "Bracelet", "Face", "Gloves", "Skirt", "Robe", "Waist",
    "Necklace", "Hair", "Beard", "Earrings", "Helmet", "OneHanded",
    "TwoHanded", "Talisman",
]
LAYER_RANK = {name: i for i, name in enumerate(LAYER_ORDER)}


# --------------------------------------------------------------------------- #
# tiledata.mul  ->  ItemID -> AnimID
# --------------------------------------------------------------------------- #
def parse_tiledata_animid(path: str) -> dict[int, int]:
    """Map static ItemID -> AnimID from tiledata.mul (High Seas / 'new' format).

    Layout (TileDataLoader.Load): 512 land groups, each a 4-byte header + 32
    land entries of [flags u64][TexID u16][name 20] = 30 bytes. Then the static
    section: groups of a 4-byte header + 32 static entries of
    [flags u64][weight u8][layer u8][count i32][AnimID u16][hue u16]
    [lightIndex u16][height u8][name 20] = 41 bytes. ItemID = group*32 + index.
    """
    data = open(path, "rb").read()
    land_entry = 8 + 2 + 20            # 30
    land_group = 4 + 32 * land_entry   # 964
    static_entry = 8 + 1 + 1 + 4 + 2 + 2 + 2 + 1 + 20  # 41
    static_group = 4 + 32 * static_entry               # 1316

    pos = 512 * land_group
    animid: dict[int, int] = {}
    group = 0
    while pos + static_group <= len(data):
        pos += 4  # group header
        for j in range(32):
            # AnimID sits at entry offset 8(flags)+1(weight)+1(layer)+4(count) = 14
            aid = struct.unpack_from("<H", data, pos + 14)[0]
            animid[group * 32 + j] = aid
            pos += static_entry
        group += 1
    return animid


# --------------------------------------------------------------------------- #
# hues.mul  ->  32-color ramp per hue index   (mirrors tools/apply_hues.py)
# --------------------------------------------------------------------------- #
def load_hues(path: str) -> list[list[tuple[int, int, int]]]:
    data = open(path, "rb").read()
    GROUP = 708  # 4-byte header + 8 * 88-byte entries
    hues: list[list[tuple[int, int, int]]] = []
    for g in range(len(data) // GROUP):
        base = g * GROUP + 4
        for e in range(8):
            off = base + e * 88
            colors = struct.unpack_from("<32H", data, off)
            table = []
            for c in colors:
                r = (c >> 10) & 0x1F
                g5 = (c >> 5) & 0x1F
                b = c & 0x1F
                table.append((
                    (r << 3) | (r >> 2),
                    (g5 << 3) | (g5 >> 2),
                    (b << 3) | (b >> 2),
                ))
            hues.append(table)
    return hues


def apply_hue(img: Image.Image, table: list[tuple[int, int, int]]) -> Image.Image:
    """Tint a grayscale gump by remapping each opaque pixel's R-ramp index
    through the hue table (partial-hue == full-hue for grayscale art)."""
    out = img.copy()
    px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            px[x, y] = (*table[r >> 3], a)
    return out


# --------------------------------------------------------------------------- #
# gump decoder  (mirrors tools/extract_spell_icons.py)
# --------------------------------------------------------------------------- #
class GumpReader:
    def __init__(self, uop_path: str):
        self.uop = uoplib.UopFile(uop_path, has_extra=True)

    def get(self, gump_id: int) -> Image.Image | None:
        """Return an RGBA Image for the gump id, or None if absent/empty."""
        entry = self.uop.get_by_name(GUMP_PATTERN % gump_id)
        if entry is None:
            return None
        payload = self.uop.read(entry)
        if entry.flag == uoplib.FLAG_NONE:
            w, h = entry.extra1, entry.extra2
        else:
            w, h = struct.unpack_from("<II", payload, 0)
            payload = payload[8:]
        if w <= 0 or h <= 0:
            return None
        row_lookup = struct.unpack_from("<%di" % h, payload, 0)
        total_words = len(payload) // 4
        tbl = uoplib.COLOR_TABLE_5TO8
        out = bytearray(w * h * 4)
        for y in range(h):
            pos = row_lookup[y] * 4
            gsize = (row_lookup[y + 1] if y < h - 1 else total_words) - row_lookup[y]
            x = 0
            for _ in range(gsize):
                value, run = struct.unpack_from("<HH", payload, pos)
                pos += 4
                if value != 0:
                    r = tbl[(value >> 10) & 0x1F]
                    g = tbl[(value >> 5) & 0x1F]
                    b = tbl[value & 0x1F]
                    px = struct.pack("<4B", r, g, b, 255)
                    base = (y * w + x) * 4
                    out[base:base + run * 4] = px * run
                x += run
        return Image.frombytes("RGBA", (w, h), bytes(out))


# --------------------------------------------------------------------------- #
# layer assignment from class name
# --------------------------------------------------------------------------- #
def layer_for_class(cls: str) -> str | None:
    """Map an armor/clothing class name to its paperdoll layer.

    Order matters: check more specific tokens first."""
    c = cls
    if "Cloak" in c:
        return "Cloak"
    if "Robe" in c:
        return "Robe"
    if "Gorget" in c:
        return "Necklace"
    if "Gloves" in c or c.endswith("Mitts"):
        return "Gloves"
    if "Arms" in c:
        return "Arms"
    if "Legs" in c:
        return "Legs"
    if "Skirt" in c or "Kilt" in c:
        return "Skirt"
    if "Pants" in c:
        return "Pants"
    if "Shirt" in c:
        return "Shirt"
    if any(t in c for t in ("Helm", "Cap", "Hat", "Coif", "Kabuto", "Hatsuburi")):
        return "Helmet"
    if "Chest" in c or "Tunic" in c or "Bustier" in c:
        return "Torso"
    return None


# Curated armor suits: material -> ordered candidate class names (use whatever
# exists in items.json; skip missing pieces).
ARMOR_SUITS = {
    "leather": ["LeatherChest", "LeatherArms", "LeatherLegs", "LeatherGloves",
                "LeatherGorget", "LeatherCap"],
    "studded": ["StuddedChest", "StuddedArms", "StuddedLegs", "StuddedGloves",
                "StuddedGorget"],
    "bone": ["BoneChest", "BoneArms", "BoneLegs", "BoneGloves", "BoneHelm"],
    "ringmail": ["RingmailChest", "RingmailArms", "RingmailLegs", "RingmailGloves"],
    "chainmail": ["ChainChest", "ChainLegs", "ChainCoif"],
    "plate": ["PlateChest", "PlateArms", "PlateLegs", "PlateGloves",
              "PlateGorget", "PlateHelm"],
    "dragon": ["DragonChest", "DragonArms", "DragonLegs", "DragonGloves",
               "DragonHelm"],
}

# Clothing outfits: name -> ordered candidate class names.
CLOTHING_OUTFITS = {
    "robe": ["Robe"],
    "fancy-shirt-and-pants": ["FancyShirt", "LongPants"],
    "wizard": ["Robe", "WizardsHat"],
}

# Single equipped item demos: slug -> (class, optional hue override int).
# Hue overrides illustrate dyed clothing where the base item is uncolored.
ITEM_DEMOS = [
    ("plate-chest", "PlateChest", None),
    ("dragon-helm", "DragonHelm", None),
    ("bone-chest", "BoneChest", None),
    ("robe-blue", "Robe", 0x0005),
    ("robe-red", "Robe", 0x0026),
    ("wizards-hat-green", "WizardsHat", 0x0048),
]


# --------------------------------------------------------------------------- #
def main() -> int:
    items_doc = json.load(open(os.path.join(ROOT, "data", "items.json")))
    by_class: dict[str, dict] = {}
    for it in items_doc["items"]:
        by_class.setdefault(it["class"], it)  # first wins

    animid = parse_tiledata_animid(TILEDATA)
    hues = load_hues(HUES_MUL)
    gumps = GumpReader(os.path.join(UO_DIR, "gumpartLegacyMUL.uop"))

    out_dir = os.path.join(ROOT, "public", "img", "paperdoll")
    os.makedirs(out_dir, exist_ok=True)

    skipped: list[str] = []

    def item_hue_int(it: dict, override: int | None) -> int | None:
        if override is not None:
            return override
        ih = it.get("item_hue") or it.get("hue")
        return int(ih, 0) if ih else None

    def piece_gump(it: dict, hue: int | None, label: str) -> Image.Image | None:
        """Decode an item's male paperdoll gump and tint by hue."""
        iid = int(it["item_id"], 0)
        aid = animid.get(iid)
        if not aid:
            skipped.append(f"{label}: no AnimID for item {it['item_id']}")
            return None
        img = gumps.get(aid + MALE_GUMP_OFFSET)
        if img is None:
            skipped.append(f"{label}: no male gump {aid + MALE_GUMP_OFFSET} "
                           f"(AnimID {aid})")
            return None
        if hue:
            idx = (hue & 0x3FFF) - 1
            if 0 <= idx < len(hues):
                img = apply_hue(img, hues[idx])
        return img

    # --- bodies ---------------------------------------------------------- #
    body_male = gumps.get(BODY_MALE)
    body_female = gumps.get(BODY_FEMALE)
    if body_male is None or body_female is None:
        print("FATAL: could not decode body gumps", file=sys.stderr)
        return 1
    body_male.save(os.path.join(out_dir, "body-male.png"))
    body_female.save(os.path.join(out_dir, "body-female.png"))
    bodies_doc = {
        "male": {"gump_id": f"0x{BODY_MALE:04X}", "png": "/img/paperdoll/body-male.png",
                 "size": list(body_male.size)},
        "female": {"gump_id": f"0x{BODY_FEMALE:04X}", "png": "/img/paperdoll/body-female.png",
                   "size": list(body_female.size)},
    }

    # --- armor suits ----------------------------------------------------- #
    suits_doc = {}
    suit_count = 0
    for name, classes in ARMOR_SUITS.items():
        pieces = []  # (rank, class, gump, layer, hue)
        for cls in classes:
            it = by_class.get(cls)
            if it is None:
                skipped.append(f"suit-{name}: class {cls} not in items.json")
                continue
            layer = layer_for_class(cls)
            if layer is None:
                skipped.append(f"suit-{name}: no layer for class {cls}")
                continue
            hue = item_hue_int(it, None)
            gimg = piece_gump(it, hue, f"suit-{name}/{cls}")
            if gimg is None:
                continue
            pieces.append((LAYER_RANK[layer], cls, gimg, layer, hue, it["item_id"]))
        if not pieces:
            skipped.append(f"suit-{name}: no renderable pieces")
            continue
        pieces.sort(key=lambda p: p[0])
        canvas = body_male.copy()
        for _, _, gimg, _, _, _ in pieces:
            canvas.alpha_composite(gimg)
        canvas.save(os.path.join(out_dir, f"suit-{name}.png"))
        suit_count += 1
        suits_doc[name] = {
            "png": f"/img/paperdoll/suit-{name}.png",
            "size": list(canvas.size),
            "pieces": [
                {"class": cls, "item_id": iid, "layer": layer,
                 "hue": f"0x{hue:04X}" if hue else None}
                for _, cls, _, layer, hue, iid in pieces
            ],
        }

    # --- clothing outfits (rendered the same way, listed under suits) ---- #
    for name, classes in CLOTHING_OUTFITS.items():
        pieces = []
        for cls in classes:
            it = by_class.get(cls)
            if it is None:
                skipped.append(f"outfit-{name}: class {cls} not in items.json")
                continue
            layer = layer_for_class(cls)
            if layer is None:
                skipped.append(f"outfit-{name}: no layer for class {cls}")
                continue
            hue = item_hue_int(it, None)
            gimg = piece_gump(it, hue, f"outfit-{name}/{cls}")
            if gimg is None:
                continue
            pieces.append((LAYER_RANK[layer], cls, gimg, layer, hue, it["item_id"]))
        if not pieces:
            skipped.append(f"outfit-{name}: no renderable pieces")
            continue
        pieces.sort(key=lambda p: p[0])
        canvas = body_male.copy()
        for _, _, gimg, _, _, _ in pieces:
            canvas.alpha_composite(gimg)
        canvas.save(os.path.join(out_dir, f"suit-{name}.png"))
        suit_count += 1
        suits_doc[name] = {
            "png": f"/img/paperdoll/suit-{name}.png",
            "size": list(canvas.size),
            "kind": "clothing",
            "pieces": [
                {"class": cls, "item_id": iid, "layer": layer,
                 "hue": f"0x{hue:04X}" if hue else None}
                for _, cls, _, layer, hue, iid in pieces
            ],
        }

    # --- single item demos ---------------------------------------------- #
    items_demo_doc = {}
    demo_count = 0
    for slug, cls, override in ITEM_DEMOS:
        it = by_class.get(cls)
        if it is None:
            skipped.append(f"item-{slug}: class {cls} not in items.json")
            continue
        hue = item_hue_int(it, override)
        gimg = piece_gump(it, hue, f"item-{slug}/{cls}")
        if gimg is None:
            continue
        canvas = body_male.copy()
        canvas.alpha_composite(gimg)
        canvas.save(os.path.join(out_dir, f"item-{slug}.png"))
        demo_count += 1
        items_demo_doc[slug] = {
            "class": cls,
            "item_id": it["item_id"],
            "layer": layer_for_class(cls),
            "hue": f"0x{hue:04X}" if hue else None,
            "png": f"/img/paperdoll/item-{slug}.png",
            "size": list(canvas.size),
        }

    # --- manifest -------------------------------------------------------- #
    doc = {
        "_schema": {
            "description": "Paperdoll reference renders: nude body gumps "
                           "composited with layered equipment gumps, per "
                           "ClassicUO PaperDollInteractable. Equipment gump id "
                           "= item AnimID (tiledata.mul) + 50000 (male). "
                           "Pieces drawn in PaperDollInteractable layer order, "
                           "tinted by item hue via hues.mul.",
            "extracted_by": "tools/extract_paperdoll.py",
            "sources": ["uo-resource/gumpartLegacyMUL.uop",
                        "uo-resource/tiledata.mul", "uo-resource/hues.mul"],
            "layer_order": LAYER_ORDER,
            "male_gump_offset": MALE_GUMP_OFFSET,
            "female_gump_offset": FEMALE_GUMP_OFFSET,
        },
        "bodies": bodies_doc,
        "suits": suits_doc,
        "items": items_demo_doc,
    }
    with open(os.path.join(ROOT, "data", "paperdoll.json"), "w") as f:
        json.dump(doc, f, indent=2)
        f.write("\n")

    # --- stats ----------------------------------------------------------- #
    print(f"tiledata AnimID entries parsed : {len(animid)}")
    print(f"bodies rendered                : 2 (male 0x000C, female 0x000D)")
    print(f"armor/clothing suits rendered  : {suit_count}")
    print(f"single item demos rendered     : {demo_count}")
    print(f"skipped ({len(skipped)}):")
    for s in skipped:
        print(f"  - {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
