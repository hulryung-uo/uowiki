# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render dressed paperdoll renders for humanoid mobs that wear/wield equipment.

For every creature in data/creatures.json that has an `equipment` list (worn /
wielded AddItem pieces, produced by tools/extract_creatures.py), this script:

  1. Resolves each equipped item to its data/items.json entry (name, item_id,
     png) and reads its paperdoll AnimID + equip LAYER from tiledata.mul.
  2. If the creature's body is a humanoid paperdoll body, composites a dressed
     paperdoll: the nude body gump first, then each equipped item's gump in
     ClassicUO PaperDollInteractable layer order. Non-optional items are always
     drawn; for layers that have only optional (random/conditional) pieces, the
     FIRST such piece is drawn as a representative (e.g. a brigand's one random
     weapon). → public/img/paperdoll/mob-<slug>.png
  3. Writes data/mob_appearance.json: per creature class →
       {paperdoll: "/img/paperdoll/mob-...png" | null,
        worn: [{class, name, item_id, png, layer, optional, hue_random}]}

Body → paperdoll body gump mapping (PaperDollInteractable.cs):
  0x190 male human  → 0x000C        0x191/0x193 female human → 0x000D
  0x25D elf male    → 0x000E        0x25E elf female         → 0x000F
  0x29A garg male   → 0x029A        0x29B garg female        → 0x0299
  savage 183/185 (male) / 184/186 (female) are not a paperdoll race; per the
  feature spec they're approximated with the human male body 0x000C.

Creatures whose body is NOT a humanoid paperdoll body (orcs on body 0x11, wisps,
etc.) get NO paperdoll (paperdoll: null) but still record their worn item list so
the page can show item icons only.

Reuses the gump reader, tiledata parser, hues loader and hue tinting from
tools/extract_paperdoll.py.

Run:  uv run --script tools/extract_mob_appearance.py
"""

from __future__ import annotations

import json
import os
import struct
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_paperdoll as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = pd.UO_DIR
TILEDATA = pd.TILEDATA
HUES_MUL = pd.HUES_MUL

# Representative ServUO hue ranges (shared with extract_paperdoll).
#   skin    : RandomSkinHue()    = 1002..1058  -> body tone
#   clothing: RandomNeutralHue() = 1801..1908  -> random-dyed worn cloth/leather
SKIN_HUE = pd.SKIN_HUE
NEUTRAL_CLOTHING_HUE = pd.NEUTRAL_CLOTHING_HUE

# UO equip-layer byte (tiledata) -> paperdoll draw-order layer name.
# Layer enum from classicuo Game/Data/Layers.cs; only wearable layers mapped.
LAYER_BY_BYTE = {
    0x01: "OneHanded", 0x02: "TwoHanded", 0x03: "Shoes", 0x04: "Pants",
    0x05: "Shirt", 0x06: "Helmet", 0x07: "Gloves", 0x08: "Ring",
    0x09: "Talisman", 0x0A: "Necklace", 0x0B: "Hair", 0x0C: "Waist",
    0x0D: "Torso", 0x0E: "Bracelet", 0x0F: "Face", 0x10: "Beard",
    0x11: "Tunic", 0x12: "Earrings", 0x13: "Arms", 0x14: "Cloak",
    0x16: "Robe", 0x17: "Skirt", 0x18: "Legs",
}

# Body id -> (paperdoll body gump, label). Female human variants map to the
# female doll; everything else uses the representative male doll where a body
# has both sexes (creatures pick a sex at random, so we render one canonical).
BODY_TO_DOLL = {
    0x190: (0x000C, "human-male"),
    0x191: (0x000D, "human-female"),
    0x193: (0x000D, "human-female"),
    0x25D: (0x000E, "elf-male"),
    0x25E: (0x000F, "elf-female"),
    0x29A: (0x029A, "gargoyle-male"),
    0x29B: (0x0299, "gargoyle-female"),
    # Savage bodies are not a paperdoll race — approximate with human male.
    183: (0x000C, "human-male"),
    184: (0x000C, "human-male"),
    185: (0x000C, "human-male"),
    186: (0x000C, "human-male"),
}


def parse_tiledata_layer(path: str) -> dict[int, int]:
    """Map static ItemID -> equip LAYER byte from tiledata.mul (new format).

    Same layout as extract_paperdoll.parse_tiledata_animid; the layer byte sits
    at entry offset 8(flags)+1(weight) = 9 (verified against classicuo
    TileDataLoader: flags u64, weight u8, layer u8, ...)."""
    data = open(path, "rb").read()
    land_entry = 8 + 2 + 20
    land_group = 4 + 32 * land_entry
    static_entry = 8 + 1 + 1 + 4 + 2 + 2 + 2 + 1 + 20
    static_group = 4 + 32 * static_entry

    pos = 512 * land_group
    layer: dict[int, int] = {}
    group = 0
    while pos + static_group <= len(data):
        pos += 4
        for j in range(32):
            lb = struct.unpack_from("<B", data, pos + 9)[0]
            layer[group * 32 + j] = lb
            pos += static_entry
        group += 1
    return layer


def pick_body(body) -> tuple[int, str] | None:
    """Resolve a creature body (int or list) to a (paperdoll gump, label).

    For a list (sex variants / RandomList), prefer the first humanoid match,
    favouring a male doll for consistency when both sexes are present."""
    ids = body if isinstance(body, list) else [body]
    ids = [b for b in ids if b is not None]
    # Prefer a male doll if any male body is present.
    males = [b for b in ids if b in (0x190, 0x25D, 0x29A, 183, 185)]
    for b in males + ids:
        if b in BODY_TO_DOLL:
            return BODY_TO_DOLL[b]
    return None


def main() -> int:
    creatures = json.load(open(os.path.join(ROOT, "data", "creatures.json")))["creatures"]
    items_doc = json.load(open(os.path.join(ROOT, "data", "items.json")))
    by_class: dict[str, dict] = {}
    for it in items_doc["items"]:
        by_class.setdefault(it["class"], it)

    animid = pd.parse_tiledata_animid(TILEDATA)
    layerb = parse_tiledata_layer(TILEDATA)
    hues = pd.load_hues(HUES_MUL)
    gumps = pd.GumpReader(os.path.join(UO_DIR, "gumpartLegacyMUL.uop"))

    out_dir = os.path.join(ROOT, "public", "img", "paperdoll")
    os.makedirs(out_dir, exist_ok=True)

    def slug(cls: str) -> str:
        import re
        return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "-", cls).lower()

    def item_hue_int(it: dict) -> int | None:
        ih = it.get("item_hue") or it.get("hue")
        try:
            return int(ih, 0) if ih else None
        except (TypeError, ValueError):
            return None

    def piece_gump(it: dict, female: bool, hue: int | None):
        iid = int(it["item_id"], 0)
        aid = animid.get(iid)
        if not aid:
            return None
        off = pd.FEMALE_GUMP_OFFSET if female else pd.MALE_GUMP_OFFSET
        img = gumps.get(aid + off)
        if img is None and female:                       # female→male fallback
            img = gumps.get(aid + pd.MALE_GUMP_OFFSET)
        if img is None:
            return None
        if hue:
            idx = (hue & 0x3FFF) - 1
            if 0 <= idx < len(hues):
                img = pd.apply_hue(img, hues[idx])
        return img

    def tint_by_index(img: Image.Image, hue: int):
        idx = (hue & 0x3FFF) - 1
        if 0 <= idx < len(hues):
            return pd.apply_hue(img, hues[idx])
        return img

    appearance: dict[str, dict] = {}
    not_found: list[str] = []
    paperdoll_count = 0
    itemlist_only_count = 0
    no_render_pieces: list[str] = []

    for c in creatures:
        equip = c.get("equipment")
        if not equip:
            continue
        cls = c["class"]

        # Resolve each worn item against items.json.
        worn = []  # dicts in equipment order
        for e in equip:
            it = by_class.get(e["class"])
            if it is None:
                not_found.append(f"{cls}/{e['class']}")
                continue
            iid = int(it["item_id"], 0)
            lb = layerb.get(iid, 0)
            baked = item_hue_int(it)
            entry = {
                "class": e["class"],
                "name": it.get("name"),
                "item_id": it["item_id"],
                "png": it.get("png"),
                "layer": LAYER_BY_BYTE.get(lb),
                "optional": e["optional"],
                "hue_random": e["hue_random"],
            }
            # Random-dyed at spawn with no baked hue -> our paperdoll tints it
            # with a representative neutral clothing hue; flag it for the caption.
            if e["hue_random"] and not baked:
                entry["hue"] = f"0x{NEUTRAL_CLOTHING_HUE:04X}"
                entry["hue_note"] = "representative (server randomizes)"
            worn.append(entry)

        doll = pick_body(c.get("body"))
        paperdoll_path = None

        if doll is not None and worn:
            body_gump_id, label = doll
            female = label.endswith("-female")
            body_img = gumps.get(body_gump_id)
            if body_img is not None:
                # Skin-tone the grayscale body gump.
                body_img = tint_by_index(body_img, SKIN_HUE)
                # Choose pieces to draw: for each paperdoll layer, take the
                # non-optional pieces; if a layer has ONLY optional pieces, take
                # the first one (representative random weapon/garment).
                by_layer: dict[str, list[dict]] = {}
                for w in worn:
                    if w["layer"] in pd.LAYER_RANK:
                        by_layer.setdefault(w["layer"], []).append(w)
                draw: list[dict] = []
                for lyr, ws in by_layer.items():
                    req = [w for w in ws if not w["optional"]]
                    draw.extend(req if req else ws[:1])
                draw.sort(key=lambda w: pd.LAYER_RANK[w["layer"]])

                canvas = body_img.copy()
                rendered_any = False
                for w in draw:
                    it = by_class[w["class"]]
                    baked = item_hue_int(it)
                    # Random-dyed-no-baked pieces were stamped with the
                    # representative neutral clothing hue above; use it so the
                    # piece shows colour instead of bare grey.
                    if w["hue_random"] and not baked:
                        hue = NEUTRAL_CLOTHING_HUE
                    else:
                        hue = baked
                    gimg = piece_gump(it, female, hue)
                    if gimg is None:
                        continue
                    canvas.alpha_composite(gimg)
                    rendered_any = True
                if rendered_any:
                    fn = f"mob-{slug(cls)}.png"
                    canvas.save(os.path.join(out_dir, fn))
                    paperdoll_path = f"/img/paperdoll/{fn}"
                    paperdoll_count += 1
                else:
                    no_render_pieces.append(cls)

        if paperdoll_path is None:
            itemlist_only_count += 1

        appearance[cls] = {"paperdoll": paperdoll_path, "worn": worn}

    doc = {
        "_schema": {
            "description": "Dressed-paperdoll renders and worn-item lists for "
                           "humanoid mobs that AddItem clothing/armor/masks/"
                           "weapons. paperdoll: composited body + equipment gump "
                           "(null when the body is not a humanoid paperdoll body "
                           "or no piece could be rendered). worn: each equipped "
                           "item resolved against items.json with its paperdoll "
                           "equip layer, optional (random/conditional) and "
                           "hue_random flags. The body gump is tinted with a "
                           "representative human skin hue; hue_random pieces with "
                           "no baked hue are tinted with a representative neutral "
                           "clothing hue and carry hue_note=\"representative "
                           "(server randomizes)\".",
            "extracted_by": "tools/extract_mob_appearance.py",
            "sources": ["data/creatures.json", "data/items.json",
                        "uo-resource/tiledata.mul", "uo-resource/hues.mul",
                        "uo-resource/gumpartLegacyMUL.uop"],
            "body_to_doll": {f"0x{k:04X}" if k > 255 else str(k):
                             f"0x{v[0]:04X} ({v[1]})" for k, v in BODY_TO_DOLL.items()},
        },
        "creatures": appearance,
    }
    with open(os.path.join(ROOT, "data", "mob_appearance.json"), "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"creatures with equipment        : {len(appearance)}")
    print(f"  dressed paperdolls rendered   : {paperdoll_count}")
    print(f"  item-list only (no paperdoll) : {itemlist_only_count}")
    if no_render_pieces:
        print(f"  humanoid body but no piece gump rendered: {no_render_pieces}")
    if not_found:
        print(f"items not in items.json ({len(not_found)}):")
        for nf in not_found:
            print(f"  - {nf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
