# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Extract creature sounds from soundLegacyMUL.uop to public/audio/*.mp3.

Sound-offset mapping (confirmed in ServUO Server/Mobile.cs, the virtual
Get*Sound methods used by BaseCreature; BaseCreature does not override
the BaseSoundID arithmetic):
    GetAngerSound  -> BaseSoundID + 0
    GetIdleSound   -> BaseSoundID + 1
    GetAttackSound -> BaseSoundID + 2
    GetHurtSound   -> BaseSoundID + 3
    GetDeathSound  -> BaseSoundID + 4
The server's sound id is sent verbatim in packet 0x54 and used directly
as the file index by the client (ClassicUO PacketHandlers.PlaySoundEffect
-> AudioManager -> SoundsLoader.TryGetSound) — no id offset.

Sound entry format (confirmed in ClassicUO
src/ClassicUO.Assets/SoundsLoader.cs TryGetSound + IO/Audio/Sound.cs):
    UOP entry "build/soundlegacymul/%08d.dat", then a 40-byte header
    (32-byte zero-padded ASCII name field, e.g. "dragon1.wav", plus
    8 extra bytes), followed by raw signed 16-bit little-endian PCM,
    mono, 22050 Hz (Sound.cs: Frequency = 22050, Channels = Mono).

Output:
  public/audio/<soundid>.mp3   (mono 64 kbps, via ffmpeg)
  data/creature_sounds.json
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uoplib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UO_DIR = "/Users/dkkang/dev/uo/uo-resource"
SOUND_UOP = os.path.join(UO_DIR, "soundLegacyMUL.uop")
SOUND_PATTERN = "build/soundlegacymul/%08d.dat"
HEADER_SIZE = 40  # 32-byte name field + 8 extra bytes (ClassicUO skips 40)
SAMPLE_RATE = 22050

AUDIO_DIR = os.path.join(ROOT, "public", "audio")
OUT_JSON = os.path.join(ROOT, "data", "creature_sounds.json")

# offset -> label, per ServUO Server/Mobile.cs Get*Sound
SOUND_OFFSETS = [
    (0, "anger"),
    (1, "idle"),
    (2, "attack"),
    (3, "hurt"),
    (4, "death"),
]


def extract_pcm(uop: uoplib.UopFile, sound_id: int) -> bytes | None:
    """Return raw s16le mono PCM for a sound id, or None if missing."""
    data = uop.read_by_name(SOUND_PATTERN % sound_id)
    if data is None or len(data) <= HEADER_SIZE:
        return None
    return data[HEADER_SIZE:]


def encode_mp3(pcm: bytes, out_path: str) -> None:
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "s16le", "-ar", str(SAMPLE_RATE), "-ac", "1", "-i", "-",
            "-ac", "1", "-b:a", "64k", out_path,
        ],
        input=pcm,
        check=True,
    )


def mp3_duration(path: str) -> float:
    out = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", path,
        ],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def main() -> int:
    with open(os.path.join(ROOT, "data", "creatures.json")) as f:
        creatures = json.load(f)["creatures"]

    # creature class -> base sound id (skip null/0)
    base_by_class: dict[str, int] = {}
    for c in creatures:
        base = c.get("base_sound_id")
        if base:
            base_by_class[c["class"]] = base
    base_ids = sorted(set(base_by_class.values()))
    print(f"{len(base_by_class)} creatures with BaseSoundID, "
          f"{len(base_ids)} unique base ids")

    os.makedirs(AUDIO_DIR, exist_ok=True)

    uop = uoplib.UopFile(SOUND_UOP)
    extracted: set[int] = set()
    missing: list[int] = []
    needed = sorted({b + off for b in base_ids for off, _ in SOUND_OFFSETS})

    for sid in needed:
        pcm = extract_pcm(uop, sid)
        if pcm is None:
            missing.append(sid)
            continue
        encode_mp3(pcm, os.path.join(AUDIO_DIR, f"{sid}.mp3"))
        extracted.add(sid)
    uop.close()

    print(f"extracted {len(extracted)} mp3s, {len(missing)} missing ids")
    if missing:
        print("missing UOP entries:", " ".join(map(str, missing)))

    # duration sanity check
    outliers = []
    for sid in sorted(extracted):
        dur = mp3_duration(os.path.join(AUDIO_DIR, f"{sid}.mp3"))
        if not 0.2 <= dur <= 10.0:
            outliers.append((sid, dur))
    if outliers:
        print("duration outliers (outside 0.2-10 s):")
        for sid, dur in outliers:
            print(f"  {sid}: {dur:.3f} s")
    else:
        print("all durations within 0.2-10 s")

    # sounds: base id -> {label: /audio/N.mp3} for extracted offsets only
    sounds: dict[str, dict[str, str]] = {}
    for base in base_ids:
        entry = {
            label: f"/audio/{base + off}.mp3"
            for off, label in SOUND_OFFSETS
            if base + off in extracted
        }
        if entry:
            sounds[str(base)] = entry

    # creatures: class -> base id, only when base has >= 1 extracted file
    creature_map = {
        cls: base for cls, base in sorted(base_by_class.items())
        if str(base) in sounds
    }

    out = {
        "_schema": {
            "sounds": "BaseSoundID -> {anger/idle/attack/hurt/death: mp3 url}; "
                      "offsets +0..+4 per ServUO Server/Mobile.cs Get*Sound",
            "creatures": "creature class name -> BaseSoundID (only creatures "
                         "with at least one extracted sound file)",
            "format": "mp3 mono 64kbps from s16le mono 22050 Hz PCM "
                      "(40-byte header skipped, ClassicUO SoundsLoader.cs)",
            "sources": [
                "uo-resource/soundLegacyMUL.uop",
                "servuo: Server/Mobile.cs (Get*Sound)",
                "data/creatures.json (base_sound_id)",
            ],
        },
        "sounds": sounds,
        "creatures": creature_map,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    print(f"wrote {OUT_JSON}: {len(sounds)} base ids, "
          f"{len(creature_map)} creatures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
