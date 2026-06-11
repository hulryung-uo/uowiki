# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""uoplib - reusable reader for UO MythicPackage (.uop) containers.

Format (confirmed against ClassicUO src/ClassicUO.IO/UOFileUop.cs):

  header:
    u32  magic      = 0x50594D ("MYP\0")
    u32  version
    u32  format_timestamp
    i64  next_block_offset
    u32  block_size
    i32  entry_count

  block (at next_block_offset, chained):
    i32  files_count
    i64  next_block_offset       (0 = end of chain)
    files_count entries of:
      i64  data_offset           (0 = unused slot, skip)
      i32  header_length         (added to data_offset)
      i32  compressed_length
      i32  decompressed_length
      u64  name_hash             (HashLittle2 of lowercase virtual path)
      u32  data_hash             (adler32; unused here)
      i16  flag                  (0=raw, 1=zlib, 3=zlib+bwt)

  has_extra files (e.g. gumpartLegacyMUL.uop): for flag != 3 the first
  8 bytes at data_offset+header_length are two i32 "extra" values
  (gump width/height); the real payload starts 8 bytes later and is
  compressed_length-8 bytes long.

Entry names are virtual paths hashed with HashLittle2, e.g.:
  "build/artlegacymul/%08d.tga"     (art; statics at index item_id+0x4000)
  "build/gumpartlegacymul/%08d.tga" (gumps; has_extra=True)
  "build/soundlegacymul/%08d.dat"   (sounds)

Library usage:
    uop = UopFile(path, has_extra=False)
    entry = uop.get_by_name("build/artlegacymul/00016370.tga")
    data = uop.read(entry)          # decompressed payload bytes
"""

from __future__ import annotations

import struct
import sys
import zlib
from dataclasses import dataclass

UOP_MAGIC = 0x50594D

# 5-bit -> 8-bit channel expansion table (ClassicUO HuesHelper._table).
# UO 16-bit art/gump colors are ARGB1555: red = (c >> 10) & 0x1F,
# green = (c >> 5) & 0x1F, blue = c & 0x1F.
COLOR_TABLE_5TO8 = bytes([
    0x00, 0x08, 0x10, 0x18, 0x20, 0x29, 0x31, 0x39, 0x41, 0x4A, 0x52, 0x5A,
    0x62, 0x6A, 0x73, 0x7B, 0x83, 0x8B, 0x94, 0x9C, 0xA4, 0xAC, 0xB4, 0xBD,
    0xC5, 0xCD, 0xD5, 0xDE, 0xE6, 0xEE, 0xF6, 0xFF,
])

FLAG_NONE = 0
FLAG_ZLIB = 1
FLAG_ZLIB_BWT = 3


def hash_filename(s: str) -> int:
    """HashLittle2 (Bob Jenkins lookup3) as used for UOP entry names.

    Port of ClassicUO UOFileUop.CreateHash. Input must already be the
    exact virtual path (lowercase by convention).
    """
    M = 0xFFFFFFFF
    length = len(s)
    eax = ecx = edx = 0
    ebx = edi = esi = (length + 0xDEADBEEF) & M
    i = 0

    while i + 12 < length:
        edi = (((ord(s[i + 7]) << 24) | (ord(s[i + 6]) << 16) | (ord(s[i + 5]) << 8) | ord(s[i + 4])) + edi) & M
        esi = (((ord(s[i + 11]) << 24) | (ord(s[i + 10]) << 16) | (ord(s[i + 9]) << 8) | ord(s[i + 8])) + esi) & M
        edx = (((ord(s[i + 3]) << 24) | (ord(s[i + 2]) << 16) | (ord(s[i + 1]) << 8) | ord(s[i])) - esi) & M
        edx = ((edx + ebx) ^ (esi >> 28) ^ ((esi << 4) & M)) & M
        esi = (esi + edi) & M
        edi = ((edi - edx) ^ (edx >> 26) ^ ((edx << 6) & M)) & M
        edx = (edx + esi) & M
        esi = ((esi - edi) ^ (edi >> 24) ^ ((edi << 8) & M)) & M
        edi = (edi + edx) & M
        ebx = ((edx - esi) ^ (esi >> 16) ^ ((esi << 16) & M)) & M
        esi = (esi + edi) & M
        edi = ((edi - ebx) ^ (ebx >> 13) ^ ((ebx << 19) & M)) & M
        ebx = (ebx + esi) & M
        esi = ((esi - edi) ^ (edi >> 28) ^ ((edi << 4) & M)) & M
        edi = (edi + ebx) & M
        i += 12

    rem = length - i
    if rem > 0:
        if rem >= 12:
            esi = (esi + (ord(s[i + 11]) << 24)) & M
        if rem >= 11:
            esi = (esi + (ord(s[i + 10]) << 16)) & M
        if rem >= 10:
            esi = (esi + (ord(s[i + 9]) << 8)) & M
        if rem >= 9:
            esi = (esi + ord(s[i + 8])) & M
        if rem >= 8:
            edi = (edi + (ord(s[i + 7]) << 24)) & M
        if rem >= 7:
            edi = (edi + (ord(s[i + 6]) << 16)) & M
        if rem >= 6:
            edi = (edi + (ord(s[i + 5]) << 8)) & M
        if rem >= 5:
            edi = (edi + ord(s[i + 4])) & M
        if rem >= 4:
            ebx = (ebx + (ord(s[i + 3]) << 24)) & M
        if rem >= 3:
            ebx = (ebx + (ord(s[i + 2]) << 16)) & M
        if rem >= 2:
            ebx = (ebx + (ord(s[i + 1]) << 8)) & M
        if rem >= 1:
            ebx = (ebx + ord(s[i])) & M

        esi = ((esi ^ edi) - ((edi >> 18) ^ ((edi << 14) & M))) & M
        ecx = ((esi ^ ebx) - ((esi >> 21) ^ ((esi << 11) & M))) & M
        edi = ((edi ^ ecx) - ((ecx >> 7) ^ ((ecx << 25) & M))) & M
        esi = ((esi ^ edi) - ((edi >> 16) ^ ((edi << 16) & M))) & M
        edx = ((esi ^ ecx) - ((esi >> 28) ^ ((esi << 4) & M))) & M
        edi = ((edi ^ edx) - ((edx >> 18) ^ ((edx << 14) & M))) & M
        eax = ((esi ^ edi) - ((edi >> 8) ^ ((edi << 24) & M))) & M

        return (edi << 32) | eax

    return (esi << 32) | eax


@dataclass
class UopEntry:
    offset: int          # absolute file offset of payload (past header & extras)
    length: int          # bytes stored at offset (compressed size if zlib)
    decompressed_length: int
    flag: int            # FLAG_NONE / FLAG_ZLIB / FLAG_ZLIB_BWT
    extra1: int = 0      # has_extra files only (gump width)
    extra2: int = 0      # has_extra files only (gump height)


class UopFile:
    def __init__(self, path: str, has_extra: bool = False):
        self.path = path
        self.has_extra = has_extra
        self._f = open(path, "rb")
        self.entries: dict[int, UopEntry] = {}  # name hash -> entry
        self._parse()

    def close(self):
        self._f.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def _parse(self):
        f = self._f
        f.seek(0)
        magic, _version, _ts = struct.unpack("<3I", f.read(12))
        if magic != UOP_MAGIC:
            raise ValueError(f"{self.path}: bad UOP magic 0x{magic:X}")
        (next_block,) = struct.unpack("<q", f.read(8))
        _block_size, _count = struct.unpack("<Ii", f.read(8))

        entry_struct = struct.Struct("<qiiiQIh")
        while next_block != 0:
            f.seek(next_block)
            files_count, next_block = struct.unpack("<iq", f.read(12))
            raw = f.read(files_count * entry_struct.size)
            extras_to_read = []
            for n in range(files_count):
                (offset, header_len, comp_len, decomp_len, name_hash,
                 _data_hash, flag) = entry_struct.unpack_from(raw, n * entry_struct.size)
                if offset == 0:
                    continue
                offset += header_len
                e = UopEntry(offset, comp_len, decomp_len, flag)
                if self.has_extra and flag != FLAG_ZLIB_BWT:
                    e.offset += 8
                    e.length = comp_len - 8
                    extras_to_read.append(e)
                self.entries[name_hash] = e
            for e in extras_to_read:
                f.seek(e.offset - 8)
                e.extra1, e.extra2 = struct.unpack("<ii", f.read(8))

    def get_by_name(self, name: str) -> UopEntry | None:
        return self.entries.get(hash_filename(name))

    def read(self, entry: UopEntry) -> bytes:
        """Return decompressed payload for an entry."""
        self._f.seek(entry.offset)
        data = self._f.read(entry.length)
        if entry.flag == FLAG_NONE:
            return data
        if entry.flag == FLAG_ZLIB:
            return zlib.decompress(data)
        if entry.flag == FLAG_ZLIB_BWT:
            raise NotImplementedError("zlib+bwt entries not supported")
        raise ValueError(f"unknown compression flag {entry.flag}")

    def read_by_name(self, name: str) -> bytes | None:
        e = self.get_by_name(name)
        return self.read(e) if e is not None else None


def _cli(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        print("CLI: uoplib.py <file.uop> [--extra] [--probe <pattern> <start> <end>] [--name <entryname>]")
        print("  pattern uses %d / %08d substitution, e.g. 'build/artlegacymul/%08d.tga'")
        return 1

    path = argv[1]
    has_extra = "--extra" in argv
    uop = UopFile(path, has_extra=has_extra)
    print(f"{path}: {len(uop.entries)} entries, has_extra={has_extra}")

    if "--name" in argv:
        name = argv[argv.index("--name") + 1]
        e = uop.get_by_name(name)
        if e is None:
            print(f"  {name}: NOT FOUND")
        else:
            print(f"  {name}: offset=0x{e.offset:X} len={e.length} dlen={e.decompressed_length} "
                  f"flag={e.flag} extra=({e.extra1},{e.extra2})")
            data = uop.read(e)
            print(f"  payload {len(data)} bytes, head: {data[:32].hex()}")

    if "--probe" in argv:
        i = argv.index("--probe")
        pattern, start, end = argv[i + 1], int(argv[i + 2], 0), int(argv[i + 3], 0)
        found = 0
        for n in range(start, end):
            e = uop.get_by_name(pattern % n)
            if e is not None:
                found += 1
                if found <= 5:
                    print(f"  [{n}] flag={e.flag} len={e.length} dlen={e.decompressed_length} "
                          f"extra=({e.extra1},{e.extra2})")
        print(f"  probe: {found}/{end - start} present")
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv))
