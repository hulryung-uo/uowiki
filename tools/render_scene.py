# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render staged in-world UO scenes (terrain + statics + characters) to PNG.

Composites real Felucca terrain and statics from the client files, then
places creature/dressed-human sprites on top, for the UO Tavern landing
page "living world" vision images.

Formats (verified against ClassicUO sources):
  MAP (classicuo/src/ClassicUO.Assets/MapLoader.cs):
    map0LegacyMUL.uop entries "build/map0legacymul/%08d.dat"; concatenated
    payloads form classic map0.mul: 196-byte blocks = u32 header + 64 cells
    of {u16 TileID, s8 Z} (struct MapBlock/MapCells), cells ordered
    cy*8+cx inside an 8x8 block. Block linear index = bx * heightBlocks + by
    (MapLoader.GetIndex: `block = x * MapBlocksSize[map,1] + y`). Felucca is
    7168x4096 tiles -> 896x512 blocks. Each .dat chunk here is 802816 bytes
    = 4096 blocks.
  STATICS (same file, structs StaidxBlock / StaticsBlock):
    staidx0.mul: 12 bytes/block {u32 Position, u32 Size, u32 Unknown},
    same block ordering. statics0.mul: 7-byte records
    {u16 Color(itemID), u8 X, u8 Y, s8 Z, u16 Hue}.
  LAND ART (classicuo/src/ClassicUO.Assets/ArtLoader.cs LoadLand):
    art index = land tileID directly (< 0x4000). Raw ARGB1555 words, no
    header: rows 0..21 start x=21-i width (i+1)*2; rows 22..43 start x=i
    width (22-i)*2 -> 1012 px / 2024 bytes in a 44x44 diamond.
  STATIC ART: index itemID + 0x4000, RLE (extract_art.decode_static_art).

Screen placement (GameObject.UpdateRealScreenPosition + View.DrawStatic +
LandView): with sx=(x-y)*22, sy=(x+y)*22 - z*4,
  land 44x44 art top-left at (sx-22, sy-22)
  static art top-left at (sx - w/2, sy + 22 - h)   (bottom at the tile's
    south vertex, horizontally centered)
  mobiles anchored the same way (feet at the south vertex).
Painter order: all land first by (x+y, z), then statics+mobiles by
(x+y, z, static<mobile).

Output: /Users/dkkang/dev/uo/uohub/img/vision/<scene>.png 1200x686.
Usage: uv run --script tools/render_scene.py [scene ...]   (default: all)
"""

import os
import struct
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib
from extract_art import decode_static_art

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
OUT_DIR = "/Users/dkkang/dev/uo/uohub/img/vision"
CREATURES = os.path.join(ROOT, "public", "img", "creatures")

ART_PATTERN = "build/artlegacymul/%08d.tga"
MAP_PATTERN = "build/map0legacymul/%08d.dat"
STATIC_OFFSET = 0x4000

MAP_W_BLOCKS, MAP_H_BLOCKS = 896, 512   # Felucca 7168x4096 tiles
BLOCK_BYTES = 196
CHUNK_BYTES = 802816                    # blocks per uop chunk * 196
BLOCKS_PER_CHUNK = CHUNK_BYTES // BLOCK_BYTES

TILE_HALF = 22
Z_STEP = 4

CANVAS_W, CANVAS_H = 1400, 800
FINAL_W, FINAL_H = 1200, 686
BG = (10, 9, 14, 255)


# --------------------------------------------------------------------------
# map / statics readers
# --------------------------------------------------------------------------

class MapReader:
    """Felucca land blocks out of map0LegacyMUL.uop."""

    def __init__(self):
        self.uop = uoplib.UopFile(os.path.join(UO_DIR, "map0LegacyMUL.uop"))
        self._chunks = {}
        self._blocks = {}

    def _chunk(self, idx):
        if idx not in self._chunks:
            entry = self.uop.get_by_name(MAP_PATTERN % idx)
            self._chunks[idx] = self.uop.read(entry) if entry else b""
        return self._chunks[idx]

    def block(self, bx, by):
        """64 (tileID, z) cells, ordered cy*8+cx; None if out of range."""
        if not (0 <= bx < MAP_W_BLOCKS and 0 <= by < MAP_H_BLOCKS):
            return None
        lin = bx * MAP_H_BLOCKS + by
        if lin in self._blocks:
            return self._blocks[lin]
        off = lin * BLOCK_BYTES
        chunk = self._chunk(off // CHUNK_BYTES)
        o = off % CHUNK_BYTES
        if o + BLOCK_BYTES > len(chunk):
            return None
        cells = []
        p = o + 4  # skip u32 header
        for _ in range(64):
            tid, z = struct.unpack_from("<Hb", chunk, p)
            cells.append((tid, z))
            p += 3
        self._blocks[lin] = cells
        return cells

    def tile(self, x, y):
        cells = self.block(x >> 3, y >> 3)
        if cells is None:
            return (0, 0)
        return cells[(y & 7) * 8 + (x & 7)]


class StaticsReader:
    def __init__(self):
        self.idx = open(os.path.join(UO_DIR, "staidx0.mul"), "rb").read()
        self.mul = open(os.path.join(UO_DIR, "statics0.mul"), "rb").read()
        self._cache = {}

    def block(self, bx, by):
        """list of (itemID, cellX, cellY, z, hue) for an 8x8 block."""
        key = (bx, by)
        if key in self._cache:
            return self._cache[key]
        out = []
        lin = bx * MAP_H_BLOCKS + by
        p = lin * 12
        if 0 <= p and p + 12 <= len(self.idx):
            pos, size, _extra = struct.unpack_from("<III", self.idx, p)
            if pos != 0xFFFFFFFF and size > 0 and pos + size <= len(self.mul):
                for o in range(pos, pos + size - 6, 7):
                    iid, cx, cy, z, hue = struct.unpack_from(
                        "<HBBbH", self.mul, o)
                    out.append((iid, cx, cy, z, hue))
        self._cache[key] = out
        return out


# --------------------------------------------------------------------------
# art
# --------------------------------------------------------------------------

class ArtCache:
    def __init__(self):
        self.uop = uoplib.UopFile(os.path.join(UO_DIR, "artLegacyMUL.uop"))
        self._land = {}
        self._static = {}

    def land(self, tile_id):
        if tile_id in self._land:
            return self._land[tile_id]
        img = None
        entry = self.uop.get_by_name(ART_PATTERN % tile_id)
        if entry:
            img = self._decode_land(self.uop.read(entry))
        self._land[tile_id] = img
        return img

    @staticmethod
    def _decode_land(payload):
        """Raw 44x44 diamond, ARGB1555 words (ClassicUO LoadLand)."""
        if len(payload) < 2024:
            return None
        vals = struct.unpack_from("<1012H", payload, 0)
        tbl = uoplib.COLOR_TABLE_5TO8
        out = bytearray(44 * 44 * 4)
        n = 0
        for i in range(22):
            x = 21 - i
            base = (i * 44 + x) * 4
            for _ in range((i + 1) * 2):
                v = vals[n]; n += 1
                out[base] = tbl[(v >> 10) & 0x1F]
                out[base + 1] = tbl[(v >> 5) & 0x1F]
                out[base + 2] = tbl[v & 0x1F]
                out[base + 3] = 255
                base += 4
        for i in range(22):
            base = ((i + 22) * 44 + i) * 4
            for _ in range((22 - i) * 2):
                v = vals[n]; n += 1
                out[base] = tbl[(v >> 10) & 0x1F]
                out[base + 1] = tbl[(v >> 5) & 0x1F]
                out[base + 2] = tbl[v & 0x1F]
                out[base + 3] = 255
                base += 4
        return Image.frombytes("RGBA", (44, 44), bytes(out))

    def static(self, item_id):
        if item_id in self._static:
            return self._static[item_id]
        img = None
        entry = self.uop.get_by_name(ART_PATTERN % (item_id + STATIC_OFFSET))
        if entry:
            img = decode_static_art(self.uop.read(entry))
        self._static[item_id] = img
        return img


def sprite(name, flip=False, scale=1.0):
    img = Image.open(os.path.join(CREATURES, name)).convert("RGBA")
    if flip:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    if scale != 1.0:
        img = img.resize((max(1, round(img.width * scale)),
                          max(1, round(img.height * scale))),
                         Image.LANCZOS)
    return img


# --------------------------------------------------------------------------
# scene compositor
# --------------------------------------------------------------------------

class Scene:
    """Render a (2R+1)^2 tile region centered at (cx, cy), then characters."""

    def __init__(self, world, statics, art, cx, cy, radius=28):
        self.world, self.statics, self.art = world, statics, art
        self.cx, self.cy = cx, cy
        self.radius = radius

    def land_z(self, x, y):
        return self.world.tile(x, y)[1]

    def screen(self, x, y, z):
        """Tile reference point relative to scene center, in canvas coords."""
        sx = (x - y) * TILE_HALF
        sy = (x + y) * TILE_HALF - z * Z_STEP
        cz = self.land_z(self.cx, self.cy)
        ox = (self.cx - self.cy) * TILE_HALF
        oy = (self.cx + self.cy) * TILE_HALF - cz * Z_STEP
        return sx - ox + CANVAS_W // 2, sy - oy + CANVAS_H // 2

    def render(self, characters, extra_statics=(), frame_dx=0, frame_dy=0):
        """characters: list of (png_name, x, y, dz, flip).
        extra_statics: list of (itemID, x, y, dz) staged props/effects.
        Returns image."""
        cx, cy, R = self.cx, self.cy, self.radius
        land = []     # (sortkey, canvasx, canvasy, img)
        objs = []     # statics + mobiles

        for bx in range((cx - R) >> 3, ((cx + R) >> 3) + 1):
            for by in range((cy - R) >> 3, ((cy + R) >> 3) + 1):
                cells = self.world.block(bx, by)
                if cells is None:
                    continue
                for cyy in range(8):
                    for cxx in range(8):
                        x, y = bx * 8 + cxx, by * 8 + cyy
                        if abs(x - cx) > R or abs(y - cy) > R:
                            continue
                        tid, z = cells[cyy * 8 + cxx]
                        img = self.art.land(tid)
                        if img is None:
                            continue
                        sx, sy = self.screen(x, y, z)
                        land.append(((x + y, z), sx - 22, sy - 22, img))
                for iid, sxx, syy, z, _hue in self.statics.block(bx, by):
                    x, y = bx * 8 + sxx, by * 8 + syy
                    if abs(x - cx) > R or abs(y - cy) > R:
                        continue
                    img = self.art.static(iid)
                    if img is None:
                        continue
                    sx, sy = self.screen(x, y, z)
                    w, h = img.size
                    objs.append(((x + y, z, 0),
                                 sx - w // 2, sy + TILE_HALF - h, img))

        for iid, x, y, dz in extra_statics:
            img = self.art.static(iid)
            if img is None:
                continue
            z = self.land_z(x, y) + dz
            sx, sy = self.screen(x, y, z)
            w, h = img.size
            objs.append(((x + y, z, 1), sx - w // 2, sy + TILE_HALF - h, img))

        for name, x, y, dz, flip in characters:
            img = sprite(name, flip=flip)
            z = self.land_z(x, y) + dz
            sx, sy = self.screen(x, y, z)
            w, h = img.size
            objs.append(((x + y, z, 1), sx - w // 2, sy + TILE_HALF - h, img))

        canvas = Image.new("RGBA", (CANVAS_W, CANVAS_H), BG)
        land.sort(key=lambda p: p[0])
        objs.sort(key=lambda p: p[0])
        for _k, bx, by, img in land + objs:
            bx += frame_dx
            by += frame_dy
            if bx + img.width < 0 or bx > CANVAS_W:
                continue
            if by + img.height < 0 or by > CANVAS_H:
                continue
            canvas.alpha_composite(img, dest=(max(bx, 0), max(by, 0)),
                                   source=(max(-bx, 0), max(-by, 0)))
        return canvas


def finish(canvas, out_path):
    """Brighten, vignette, downscale to FINAL size and save."""
    canvas = canvas.convert("RGB")
    canvas = ImageEnhance.Brightness(canvas).enhance(1.12)
    canvas = ImageEnhance.Color(canvas).enhance(1.12)

    # subtle dark vignette
    mask = Image.new("L", (CANVAS_W, CANVAS_H), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((-CANVAS_W * 0.45, -CANVAS_H * 0.55,
               CANVAS_W * 1.45, CANVAS_H * 1.55), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(130))
    dark = Image.new("RGB", (CANVAS_W, CANVAS_H), (8, 7, 12))
    canvas = Image.composite(canvas, dark, mask)

    canvas = canvas.resize((FINAL_W, FINAL_H), Image.LANCZOS)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    canvas.save(out_path)
    print(f"wrote {out_path}")


# --------------------------------------------------------------------------
# the four scenes
# --------------------------------------------------------------------------

def scene_bank(world, statics, art):
    """Market crowd at West Britain Bank."""
    cx, cy = 1425, 1692
    sc = Scene(world, statics, art, cx, cy)
    chars = [
        # outfit png, x, y, dz, flip
        ("dressed-brigand.png",           cx - 1, cy + 2, 0, False),
        ("dressed-gypsy.png",             cx + 1, cy + 3, 0, True),
        ("dressed-militia-fighter.png",   cx + 3, cy + 1, 0, False),
        ("dressed-executioner.png",       cx - 3, cy + 4, 0, True),
        ("dressed-lysander-gathenwale.png", cx + 2, cy + 5, 0, False),
        ("dressed-tavara-sewel.png",      cx - 2, cy + 6, 0, False),
        ("dressed-barracoon.png",         cx + 5, cy + 3, 0, True),
        ("dressed-forgotten-servant.png", cx,     cy + 7, 0, True),
        ("dressed-cursed.png",            cx - 5, cy + 5, 0, False),
        ("226.png",                       cx + 7, cy + 5, 0, True),   # horse
        ("291.png",                       cx - 5, cy + 7, 0, False),  # pack horse
    ]
    # nudge the frame so the crowd (south-west of center) sits mid-frame
    return sc.render(chars, frame_dx=60, frame_dy=-70)


def scene_lumberjack(world, statics, art):
    """Woodcutters in the deep forest near Yew."""
    cx, cy = 600, 1010
    sc = Scene(world, statics, art, cx, cy)
    chars = [
        # axe-carriers right at tree trunks (trunks at 596,1005 and 604,1014)
        ("dressed-brigand.png",           596, 1006, 0, False),
        ("dressed-forgotten-servant.png", 604, 1015, 0, True),
        ("291.png",                       600, 1011, 0, False),  # pack horse
    ]
    return sc.render(chars)


def scene_duel(world, statics, art):
    """Two fighters squared off on the open road north of Britain."""
    cx, cy = 1380, 1500
    sc = Scene(world, statics, art, cx, cy)
    chars = [
        ("dressed-militia-fighter.png", cx,     cy,     0, False),
        ("dressed-executioner.png",     cx + 3, cy - 3, 0, True),
        ("dressed-gypsy.png",           cx + 3, cy + 4, 0, False),  # spectator
    ]
    effects = [
        (0x36D4, cx + 2, cy - 2, 6),  # fireball mid-flight between them
    ]
    return sc.render(chars, extra_statics=effects)


def scene_hunting(world, statics, art):
    """A hunting party engaging a dragon below the mountains near Despise."""
    cx, cy = 1389, 1118
    sc = Scene(world, statics, art, cx, cy)
    chars = [
        ("12.png",                      cx + 2, cy - 1, 0, False),  # dragon
        ("dressed-militia-fighter.png", cx,     cy + 2, 0, False),
        ("dressed-brigand.png",         cx - 4, cy + 4, 0, False),
        ("dressed-lysander-gathenwale.png", cx - 3, cy + 7, 0, False),
        ("225.png",                     cx - 1, cy + 3, 0, False),  # wolf
    ]
    return sc.render(chars)


SCENES = {
    "bank-gathering": scene_bank,
    "lumberjack": scene_lumberjack,
    "pvp-duel": scene_duel,
    "hunting": scene_hunting,
}


def main(argv):
    names = argv[1:] or list(SCENES)
    world, statics, art = MapReader(), StaticsReader(), ArtCache()
    for name in names:
        fn = SCENES.get(name)
        if fn is None:
            print(f"unknown scene {name}; have {', '.join(SCENES)}")
            return 1
        canvas = fn(world, statics, art)
        finish(canvas, os.path.join(OUT_DIR, f"{name}.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
