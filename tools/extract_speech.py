# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Extract spoken command phrases ("verbal commands") from ServUO into
data/speech_commands.json.

Ultima Online has two distinct ways the server reacts to what a player *says*:

1. SPEECH KEYWORDS (the common case). The client owns a speech-keyword table
   (client-side speech.mul / KeywordList). When you type a phrase, the client
   matches it against that table and sends the matching numeric *keyword id(s)*
   alongside the raw text in the encoded-speech packet
   (Server/Network/PacketHandlers.cs UnicodeSpeech -> args.Keywords). Server
   handlers then test `e.HasKeyword(0x..)`. Because the id is resolved on the
   client from the *localized* keyword table, the SAME action fires from the
   French / German / etc. equivalent phrase — the server never sees the literal
   words for these, only the id. So keyword commands are language-independent.

2. LITERAL STRING MATCHES. A few handlers compare the raw text directly
   (`Insensitive.Equals(e.Speech, "...")`, `.StartsWith`, `.IndexOf`). These
   must be said in English (the exact string in the source).

This script mines Scripts/ for both kinds. For keyword handlers it reads the
`e.HasKeyword(0x..)` / `case 0x..:` lines together with the trailing `// *...*`
comment that documents the English trigger phrase (these comments mirror the
client speech-keyword table). For literal matches it pulls the quoted string.
Server reply clilocs (e.g. 502097 "Lock what down?") are resolved through
../anima/data/cliloc.json so the JSON records what the command actually does.

Output: data/speech_commands.json, grouped by category
  { Housing: [...], Pets: [...], "Vendors/Bank": [...], Misc: [...] }
each entry: {phrase, effect, source_file, match_type, keyword_id?}

Note on phrasing: the `phrase` for a keyword command is the canonical English
phrase from the source comment / known UO client table. It is what an
English client maps to that keyword id; localized clients send the same id
from their own equivalent phrase.

Stdlib only. Pragmatic: emits a hand-curated, source-anchored table; every row
cites the ServUO file it came from and (where possible) shows the cliloc reply.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVUO = "/Users/dkkang/dev/uo/servuo"
SCRIPTS = os.path.join(SERVUO, "Scripts")
CLILOC = "/Users/dkkang/dev/uo/anima/data/cliloc.json"


def load_cliloc():
    try:
        with open(CLILOC, encoding="utf-8") as f:
            d = json.load(f)
        return {str(k): v for k, v in d.items()}
    except (OSError, ValueError):
        return {}


def rel(path):
    """ServUO path relative to the servuo root (matches CLAUDE.md citation style)."""
    return os.path.relpath(path, SERVUO).replace(os.sep, "/")


def find_line(path, needle):
    """1-based line number of the first line containing `needle`, or None."""
    try:
        with open(path, encoding="utf-8-sig", errors="replace") as f:
            for n, line in enumerate(f, 1):
                if needle in line:
                    return n
    except OSError:
        pass
    return None


def cl(cliloc, num):
    return cliloc.get(str(num))


# ---------------------------------------------------------------------------
# The command tables. Each row is anchored to a real ServUO source line; the
# `anchor` string is searched for in the file to produce a file:line citation,
# and (for keyword rows) doubles as a self-check that the id is still present.
# `reply` is a cliloc id resolved to the server's response text.
# ---------------------------------------------------------------------------

def housing(cliloc):
    f = os.path.join(SCRIPTS, "Regions", "HouseRegion.cs")
    rows = [
        # keyword-based — said inside your own house (must be at least a friend)
        dict(phrase="I wish to lock this down", kw=0x23, reply=502097,
             anchor="e.HasKeyword(0x23)",
             effect="Prompts you to target a loose item to lock it down (fixes it "
                    "in place, stops decay). Must be a friend or better, inside the house."),
        dict(phrase="I wish to release this", kw=0x24, reply=502100,
             anchor="e.HasKeyword(0x24)",
             effect="Prompts you to target a locked-down item to release it back to "
                    "loose status so it can be moved/picked up."),
        dict(phrase="I wish to secure this", kw=0x25, reply=502103,
             anchor="e.HasKeyword(0x25)",
             effect="Prompts you to target a container to make it secure storage "
                    "(access-controlled). Co-owner or better."),
        dict(phrase="I wish to unsecure this", kw=0x26, reply=502106,
             anchor="e.HasKeyword(0x26)",
             effect="Prompts you to target a secured container to unsecure it. Owner only."),
        dict(phrase="I wish to place a strongbox", kw=0x27, reply=502109,
             anchor="e.HasKeyword(0x27)",
             effect="A co-owner gets a personal strongbox placed; owners are told they "
                    "do not get one of their own (502109)."),
        dict(phrase="I wish to place a trash barrel", kw=0x28, reply=None,
             anchor="e.HasKeyword(0x28)",
             effect="Places a trash barrel in the house (items dropped in it are "
                    "destroyed). Co-owner or better."),
        dict(phrase="I ban thee", kw=0x34, reply=501325,
             anchor="e.HasKeyword(0x34)",
             effect="Prompts you to target a person to ban them from the house "
                    "(public houses only; on a private AOS house you revoke access "
                    "instead). Friend or better."),
        dict(phrase="Remove thyself", kw=0x33, reply=501326,
             anchor="e.HasKeyword(0x33)",
             effect="Prompts you to target a person to eject (kick) them from the "
                    "house without banning. Friend or better."),
        # literal-string command — must be said in English exactly
        dict(phrase="I wish to resize my house", literal=True, reply=None,
             anchor='"I wish to resize my house"',
             effect="Opens the resize/redemolish confirmation gump for the owner "
                    "(Mondain's Legacy+). Matched as a literal English string, not a "
                    "keyword, so it only works said exactly in English; you must be at "
                    "the house sign and the house must be older than one hour."),
    ]
    out = []
    for r in rows:
        line = find_line(f, r["anchor"])
        src = f"servuo: {rel(f)}" + (f":{line}" if line else "")
        eff = r["effect"]
        if r.get("reply"):
            rtxt = cl(cliloc, r["reply"])
            if rtxt:
                eff += f' Server prompt: "{rtxt}" (cliloc {r["reply"]}).'
        entry = {
            "phrase": r["phrase"],
            "effect": eff,
            "source_file": src,
            "match_type": "literal-string" if r.get("literal") else "keyword",
        }
        if not r.get("literal"):
            entry["keyword_id"] = f"0x{r['kw']:X}"
        out.append(entry)
    return out


def pets(cliloc):
    f = os.path.join(SCRIPTS, "Mobiles", "AI", "BaseAI.cs")
    # (phrase, keyword_id, named?, effect) -- 'named' means you must include the
    # pet's name (WasNamed); the all* group commands every pet in earshot.
    rows = [
        ("All kill / All attack", 0x168,
         "Every controlled pet in earshot attacks a target you then pick. (0x169 "
         "= 'all attack' fires the same handler.)"),
        ("All guard / All guard me", 0x166,
         "Every pet goes into guard mode, guarding you. (0x16B = 'all guard me'.)"),
        ("All follow me", 0x16C, "Every pet follows you."),
        ("All follow", 0x165, "Every pet follows a target you then pick."),
        ("All come", 0x164, "Every pet comes to you."),
        ("All stay", 0x170, "Every pet stays put."),
        ("All stop", 0x167, "Every pet stops its current order (idle)."),
        ("<pet name> kill / attack", 0x15D,
         "Named pet attacks a target you pick. Owner only; name required."),
        ("<pet name> guard", 0x15C,
         "Named pet guards. Owner only; name required."),
        ("<pet name> follow / follow me", 0x15A,
         "Named pet follows a target you pick ('follow') or follows you "
         "('follow me', 0x163)."),
        ("<pet name> come", 0x155, "Named pet comes to you. Owner only."),
        ("<pet name> stay", 0x16F, "Named pet stays put."),
        ("<pet name> stop", 0x161, "Named pet stops its current order."),
        ("<pet name> patrol", 0x15F, "Named pet patrols its home area. Owner only."),
        ("<pet name> drop", 0x156,
         "Named pet drops what it is carrying (pack animals). Owner only; not for "
         "summons/dead pets."),
        ("<pet name> friend", 0x15B,
         "Prompts you to target a player to add as a pet-friend (they can command "
         "it too). Owner only; not for summons."),
        ("<pet name> transfer", 0x16E,
         "Prompts you to target a player to transfer ownership of the pet to them. "
         "Owner only; not for summons/dead pets."),
        ("<pet name> release", 0x16D,
         "Releases the pet from your control (opens a confirm gump for tamed pets; "
         "summons are dismissed immediately). Owner only."),
    ]
    out = []
    for phrase, kw, eff in rows:
        line = find_line(f, f"case 0x{kw:X}:") or find_line(f, f"0x{kw:X}")
        src = f"servuo: {rel(f)}" + (f":{line}" if line else "")
        out.append({
            "phrase": phrase,
            "effect": eff,
            "source_file": src,
            "match_type": "keyword",
            "keyword_id": f"0x{kw:X}",
        })
    # GM-only literal 'obey'
    line = find_line(f, '"obey"')
    out.append({
        "phrase": "<pet name> obey",
        "effect": "Game Master only: forces the named creature to accept you as its "
                  "control master. Matched as the literal word 'obey' after the "
                  "creature's name.",
        "source_file": f"servuo: {rel(f)}" + (f":{line}" if line else ""),
        "match_type": "literal-string",
    })
    return out


def vendors_bank(cliloc):
    banker = os.path.join(SCRIPTS, "Mobiles", "NPCs", "Banker.cs")
    vai = os.path.join(SCRIPTS, "Mobiles", "AI", "VendorAI.cs")
    trainer = os.path.join(SCRIPTS, "Mobiles", "NPCs", "AnimalTrainer.cs")
    pv = os.path.join(SCRIPTS, "Mobiles", "NPCs", "PlayerVendor.cs")
    out = []

    def add(phrase, eff, f, anchor, kw=None, literal=False, reply=None):
        line = find_line(f, anchor)
        src = f"servuo: {rel(f)}" + (f":{line}" if line else "")
        if reply:
            rtxt = cl(cliloc, reply)
            if rtxt:
                eff += f' (e.g. "{rtxt}")'
        e = {"phrase": phrase, "effect": eff, "source_file": src,
             "match_type": "literal-string" if literal else "keyword"}
        if kw is not None:
            e["keyword_id"] = f"0x{kw:X}"
        out.append(e)

    # Banker (said to any banker within 12 tiles)
    add("Bank", "Opens your bank box.", banker, "case 0x0002:", kw=0x2)
    add("Balance", "The banker tells you your current gold balance.", banker,
        "case 0x0001:", kw=0x1, reply=1042759)
    add("Withdraw <amount>", "Withdraws that much gold from your bank to your "
        "backpack (e.g. \"withdraw 1000\"). The amount is parsed from the words "
        "after the keyword.", banker, "case 0x0000:", kw=0x0)
    add("Check <amount>", "The banker writes you a bank check for that amount, "
        "drawn from your bank balance.", banker, "case 0x0003:", kw=0x3)
    # Shopkeeper vendors (BaseVendor via VendorAI)
    add("Vendor buy", "Opens the shopkeeper's buy window.", vai,
        "0x3C", kw=0x3C)
    add("Vendor sell", "Opens the shopkeeper's sell window so you can sell goods.",
        vai, "0x14D", kw=0x14D)
    add("<vendor name> buy", "Opens the buy window of the named shopkeeper "
        "('buy' alone works when you name them).", vai, "0x171", kw=0x171)
    add("<vendor name> sell", "Opens the sell window of the named shopkeeper "
        "('sell' alone works when you name them).", vai, "0x177", kw=0x177)
    # Animal trainer (stablemaster)
    add("Stable", "The animal trainer offers to stable a pet (target the pet).",
        trainer, "e.HasKeyword(0x0008)", kw=0x8)
    add("Claim", "The animal trainer brings out your stabled pets, or claim a "
        "specific one by saying its name after 'claim'.", trainer,
        "e.HasKeyword(0x0009)", kw=0x9)
    # Player vendors (in houses)
    add("Vendor buy", "On a player vendor: opens its for-sale list to buy items.",
        pv, "0x3C", kw=0x3C)
    add("<vendor name> browse", "Browse a player vendor's stock without buying.",
        pv, "0x3D", kw=0x3D)
    add("<vendor name> collect", "Owner: collect the gold the vendor has earned.",
        pv, "0x3E", kw=0x3E)
    add("<vendor name> status", "Owner: check the vendor's fees/funds status.",
        pv, "0x3F", kw=0x3F)
    add("<vendor name> dismiss", "Owner: dismiss (fire) the player vendor.",
        pv, "0x40", kw=0x40)
    add("<vendor name> cycle", "Owner: cycle/reorganize the vendor's display.",
        pv, "0x41", kw=0x41)
    return out


def misc(cliloc):
    out = []

    def add(phrase, eff, f, anchor, kw=None, literal=False, reply=None):
        path = os.path.join(SCRIPTS, *f.split("/"))
        line = find_line(path, anchor)
        src = f"servuo: {rel(path)}" + (f":{line}" if line else "")
        if reply:
            rtxt = cl(cliloc, reply)
            if rtxt:
                eff += f' Reply: "{rtxt}".'
        e = {"phrase": phrase, "effect": eff, "source_file": src,
             "match_type": "literal-string" if literal else "keyword"}
        if kw is not None:
            e["keyword_id"] = f"0x{kw:X}"
        out.append(e)

    # Self-status keywords handled globally (Scripts/Misc/Keywords.cs)
    add("I must consider my sins",
        "The server reports your short-term and long-term murder counts.",
        "Misc/Keywords.cs", "0x0032", kw=0x32)
    add("I resign from my guild", "Leaves your current player guild.",
        "Misc/Keywords.cs", "0x002A", kw=0x2A)
    add("I renounce my young player status",
        "Opens the confirmation to give up Young-player protection.",
        "Misc/Keywords.cs", "0x0035", kw=0x35)
    add("Guild", "Opens your guild info window (if you are in a guild).",
        "Misc/Keywords.cs", "case 0x6:", kw=0x6)
    # Guards
    add("Guards", "Calls the town guards to your location (in a guarded region).",
        "Regions/GuardedRegion.cs", "0x0007", kw=0x7)
    # Town crier / news objects
    add("News", "The town crier (or a news-reading object like Coral the Owl / "
        "Sherry the Mouse) recites the current news. Works within ~12 tiles.",
        "Mobiles/NPCs/TownCrier.cs", "0x30", kw=0x30)
    # NPC guildmasters
    add("Join / Member", "Said (with the guildmaster named) to an NPC "
        "guildmaster to ask to join their guild.",
        "Mobiles/NPCs/BaseGuildmaster.cs", "0x0004", kw=0x4)
    add("Resign / Quit", "Said to your NPC guildmaster to resign from the guild.",
        "Mobiles/NPCs/BaseGuildmaster.cs", "0x0005", kw=0x5)
    # Real estate broker
    add("Appraise", "A real-estate broker asks you to target a house deed and "
        "appraises its value.", "Mobiles/NPCs/RealEstateBroker.cs", "0x38",
        kw=0x38, reply=500608),
    # Escortable NPCs
    add("Destination", "An escortable NPC tells you where it wants to go.",
        "Mobiles/NPCs/BaseEscortable.cs", "0x1D", kw=0x1D)
    add("I will take thee", "Accept the escort quest for an escortable NPC.",
        "Mobiles/NPCs/BaseEscortable.cs", "0x1E", kw=0x1E)
    # Thief guildmaster
    add("Disguise", "Ask the Thieves' Guildmaster about a disguise kit (members "
        "only).", "Mobiles/NPCs/ThiefGuildmaster.cs", "0x1F", kw=0x1F)
    # Hireable NPCs
    add("Hire / Servant", "Asks a hireable NPC to work for you; it quotes its "
        "daily wage.", "Mobiles/NPCs/BaseHire.cs", "0x0162", kw=0x162)
    # Faction guard orders
    add("Orders", "A town sheriff issues orders to a faction guard (sheriff "
        "only).", "Services/Factions/Mobiles/Guards/BaseFactionGuard.cs",
        "0xE6", kw=0xE6)
    # NPC trainers (skill training)
    add("<npc name> train", "Asks a townsperson NPC what skills they can teach "
        "you; '<npc name> <skillname>' then trains that skill a little.",
        "Mobiles/AI/BaseAI.cs", "0x6C", kw=0x6C)
    add("<npc name> time", "Asks an NPC for the in-game time.",
        "Mobiles/AI/BaseAI.cs", "0x9E", kw=0x9E)
    return out


def main():
    cliloc = load_cliloc()
    data = {
        "Housing": housing(cliloc),
        "Pets": pets(cliloc),
        "Vendors/Bank": vendors_bank(cliloc),
        "Misc": misc(cliloc),
    }

    doc = {
        "_schema": {
            "description": "Spoken command phrases ('verbal commands') the ServUO "
                           "server reacts to. Most are SPEECH KEYWORDS: the client "
                           "matches your (localized) phrase against its speech-keyword "
                           "table and sends a numeric keyword id (keyword_id) in the "
                           "encoded-speech packet; server handlers test "
                           "e.HasKeyword(0x..). Because the id is resolved client-side "
                           "from the localized table, the equivalent phrase in any "
                           "client language triggers the same action — the server only "
                           "sees the id, not the words. A few commands (match_type "
                           "'literal-string') compare the raw text and must be said in "
                           "English exactly. 'phrase' is the canonical English wording; "
                           "for keyword commands it is what an English client maps to "
                           "that id. <...> denotes a value you supply (a pet/vendor/NPC "
                           "name or an amount). Server reply text resolved via anima "
                           "cliloc.json where available.",
            "extracted_by": "tools/extract_speech.py",
            "sources": [
                "servuo: Scripts/Regions/HouseRegion.cs",
                "servuo: Scripts/Misc/Keywords.cs",
                "servuo: Scripts/Mobiles/AI/BaseAI.cs",
                "servuo: Scripts/Mobiles/AI/VendorAI.cs",
                "servuo: Scripts/Mobiles/NPCs/Banker.cs",
                "servuo: Scripts/Mobiles/NPCs/AnimalTrainer.cs",
                "servuo: Scripts/Mobiles/NPCs/PlayerVendor.cs",
                "servuo: Server/Network/PacketHandlers.cs (UnicodeSpeech keyword decode)",
                "anima: data/cliloc.json (reply text)",
            ],
            "match_types": {
                "keyword": "matched by client-resolved speech keyword id "
                           "(e.HasKeyword); language-independent.",
                "literal-string": "matched against the raw text "
                                  "(Insensitive.Equals/StartsWith/IndexOf); "
                                  "must be said in English exactly.",
            },
        },
    }
    doc.update(data)

    out = os.path.join(ROOT, "data", "speech_commands.json")
    with open(out, "w") as f:
        json.dump(doc, f, indent=2, sort_keys=False)
        f.write("\n")

    total = sum(len(v) for v in data.values())
    for cat, rows in data.items():
        missing = [r["phrase"] for r in rows if ":" not in r["source_file"]]
        note = f"  (UNANCHORED: {', '.join(missing)})" if missing else ""
        print(f"{cat:14s}: {len(rows)} commands{note}")
    print(f"{'TOTAL':14s}: {total}")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
