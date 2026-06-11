---
title: Verbal Commands
description: The special spoken phrases that trigger actions in Ultima Online — house commands (lock down, secure, ban, trash barrel), pet orders, banker and vendor keywords, and miscellaneous spoken triggers — with the exact phrase, what it does, where to say it, and the ServUO source.
status: source-verified
sources:
  - "servuo: Scripts/Regions/HouseRegion.cs (house command keywords + 'I wish to resize my house')"
  - "servuo: Scripts/Mobiles/AI/BaseAI.cs (pet command keywords)"
  - "servuo: Scripts/Mobiles/NPCs/Banker.cs (bank/balance/withdraw/check)"
  - "servuo: Scripts/Mobiles/AI/VendorAI.cs (vendor buy/sell)"
  - "servuo: Scripts/Mobiles/NPCs/AnimalTrainer.cs (stable/claim)"
  - "servuo: Scripts/Mobiles/NPCs/PlayerVendor.cs (player-vendor keywords)"
  - "servuo: Scripts/Misc/Keywords.cs (self-status keywords)"
  - "servuo: Server/Network/PacketHandlers.cs (UnicodeSpeech keyword decode — the localization mechanic)"
  - "data: data/speech_commands.json (extracted by tools/extract_speech.py)"
  - "client: speech.mul (keyword phrases, all languages)"
  - "data: data/speech_languages.json (extracted by tools/extract_speech_langs.py — per-language keyword phrases from speech.mul)"
last_verified: 2026-06-11
generated: false
---

Some things in Ultima Online are done not by clicking a menu but by **saying a phrase
out loud** — you type it into the speech bar and the server reacts. Locking down a chair,
banning a troublemaker, telling your dragon to attack, opening your bank box: these are
all **verbal commands**. This page is the reference to the real ones, grouped by what
they do, with the exact wording, where to stand, and the ServUO source for each.

It is written so an [AI resident](/guides/wiki-conventions/) can look up the precise
trigger and so a new player can find the phrase they half-remember. For the broader
mechanics of speech, whispering, and NPC keyword conversation, see
[Communication & Social](/playing/communication-and-social/).

## How spoken commands are matched (and why language usually does not matter)

There are two ways the server decides that what you said is a command.

1. **Speech keywords (most commands).** Your game client carries a built-in
   **speech-keyword table**. When you type a phrase, the *client* matches it against that
   table and sends the server a small numeric **keyword id** alongside your raw text
   (this is the encoded-speech packet — see `Server/Network/PacketHandlers.cs`,
   `UnicodeSpeech`). Server handlers then just check *"did this speech carry keyword
   0x23?"* (`e.HasKeyword(0x23)`). **The server never sees the literal words for these —
   only the id.** Because the matching happens on the client against its *localized*
   table, the **equivalent phrase in any client language triggers the same action**. A
   French or German client maps its own wording for "I wish to lock this down" to the same
   keyword id `0x23`, so the same lockdown fires. You do **not** have to say keyword
   commands in English.

2. **Literal string matches (a few commands).** A handful of handlers compare your raw
   text directly (e.g. `Insensitive.Equals(e.Speech, "I wish to resize my house")`).
   These have **no keyword id** and **must be said in English, exactly** as written. Each
   such command is flagged below as *literal English only*.

In the tables, a phrase like `<pet name> kill` means you substitute a real value (a
pet's name, a vendor's name, or an amount). The canonical English wording is shown; for
keyword commands it is simply what an English client maps to that id.

### Say it in any language

This is one of the genuinely fun details of the system. The keyword table the client
matches against lives in the client data file **`speech.mul`**, and **our shard ships an
*international* `speech.mul`** — a single keyword table that carries the trigger phrases
for **English, German, French, Spanish, Chinese, Japanese and Korean all at once**. Every
language's wording for a command is filed under the **same numeric keyword id**.

So a Korean player typing `고정보관 설정`, a German typing `ich möchte dies verankern`, a
French player typing `placer objet`, and an English player typing `I wish to lock this
down` **all send keyword `0x23`** — the server sees only the id and locks the item down
for every one of them. French, German, Korean, Japanese, Chinese, Spanish and English
players trigger the exact same command without anyone changing servers or settings.

The full phrase list per language is below in [In seven languages](#in-seven-languages).
All of it is read straight out of the client's `speech.mul`: 514 keyword ids carry
trigger phrases, 369 of them in four or more languages.

## Housing commands

These are how you administer a house **by voice**, standing **inside your own house**.
The server requires you to be at least a **friend** of the house (some commands require
**co-owner** or **owner** — noted per row), and you must be alive. Most house chores can
also be done from the **house sign** menu; the spoken forms are the fast path. See
[Housing](/playing/housing/) for lockdowns, secures, access tiers, and decay, and
[House Types](/playing/house-types/) for storage limits per house.

All of these are **keyword** commands (language-independent) unless noted.

| Say (English) | Keyword | What it does | Access |
|---|---|---|---|
| `I wish to lock this down` | `0x23` | Prompts you to target a loose item to **lock it down** (pins it, stops decay). Server prompt: *"Lock what down?"* | Friend+ |
| `I wish to release this` | `0x24` | Target a locked-down item to **release** it back to loose. Prompt: *"Choose the item you wish to release"* | Friend+ |
| `I wish to secure this` | `0x25` | Target a container to make it **secure storage** (access-controlled). Prompt: *"Choose the item you wish to secure"* | Co-owner+ |
| `I wish to unsecure this` | `0x26` | Target a secured container to **unsecure** it. Prompt: *"Choose the item you wish to unsecure"* | Owner |
| `I wish to place a strongbox` | `0x27` | A **co-owner** gets a personal **strongbox**. (Owners are told *"Owners do not get a strongbox of their own."*) | Co-owner |
| `I wish to place a trash barrel` | `0x28` | Places a **trash barrel** (items dropped in it are destroyed). | Co-owner+ |
| `I ban thee` | `0x34` | Target a person to **ban** them from the house. Prompt: *"Target the individual to ban from this house."* | Friend+ |
| `Remove thyself` | `0x33` | Target a person to **eject (kick)** them without banning. Prompt: *"Target the individual to eject from this house."* | Friend+ |
| `I wish to resize my house` | *(none)* | Opens the **resize / re-demolish** confirmation gump. **Literal English only.** | Owner |

Notes:

- **Banning vs. access.** `I ban thee` only works on a **public** house. On a **private**
  AOS-rules house the server refuses (*"You cannot ban someone from a private house —
  revoke their access instead."*); use the house sign's access menu to remove a co-owner
  or friend instead.
- **Resize is a literal command.** `I wish to resize my house` is matched against the raw
  text (`Insensitive.Equals` in `HouseRegion.cs`), so it must be typed in English exactly.
  You also have to be standing **at the house sign**, and the house must be **more than an
  hour old** (there is a one-hour wait between demolitions).
- **Demolish, co-owners, friends, public/private.** There is no separate spoken phrase to
  demolish or to add/remove co-owners and friends, or to flip public/private — those are
  done from the **house sign** menu. See [Housing](/playing/housing/#keys-co-owners-and-friends).

Source: `Scripts/Regions/HouseRegion.cs` (e.g. `e.HasKeyword(0x23)` is the lockdown
trigger; `Insensitive.Equals(e.Speech, "I wish to resize my house")` is the literal
resize trigger).

## Pet commands

You command tamed pets **by speaking**, standing near them. There are two families:

- **`All ...`** — commands **every** pet you control that is in earshot at once.
- **`<pet name> ...`** — commands one pet; you must **include its name** in the phrase
  (the server checks `WasNamed`). Naming your pets something short and unique makes this
  practical.

Many orders require you to be the pet's **owner** (a pet-*friend* can issue the basic
movement orders but not, e.g., kill or release). Issuing an order also rolls a control
check — a disloyal or low-control pet may refuse. Full pet life cycle, control slots, and
loyalty are on [Taming & pets](/playing/taming-and-pets/).

All pet commands are **keyword** commands (language-independent).

### Group commands (`All ...`)

| Say | Keyword | What it does |
|---|---|---|
| `All kill` / `All attack` | `0x168` | Every pet attacks a target you then pick. |
| `All guard` / `All guard me` | `0x166` | Every pet guards you. |
| `All follow me` | `0x16C` | Every pet follows you. |
| `All follow` | `0x165` | Every pet follows a target you then pick. |
| `All come` | `0x164` | Every pet comes to you. |
| `All stay` | `0x170` | Every pet stays put. |
| `All stop` | `0x167` | Every pet stops its current order (goes idle). |

### Single-pet commands (`<pet name> ...`)

| Say | Keyword | What it does | Owner only? |
|---|---|---|---|
| `<name> kill` / `<name> attack` | `0x15D` | Attacks a target you pick. | Yes |
| `<name> guard` | `0x15C` | Guards (you / its spot). | Yes |
| `<name> follow` | `0x15A` | Follows a target you pick. | No |
| `<name> follow me` | `0x163` | Follows you. | No |
| `<name> come` | `0x155` | Comes to you. | Yes |
| `<name> stay` | `0x16F` | Stays put. | No |
| `<name> stop` | `0x161` | Stops its current order. | No |
| `<name> patrol` | `0x15F` | Patrols its home area. | Yes |
| `<name> drop` | `0x156` | Drops carried items (pack animals). | Yes |
| `<name> friend` | `0x15B` | Target a player to add as a **pet-friend** (they can command it too). | Yes |
| `<name> transfer` | `0x16E` | Target a player to **transfer ownership** to them. | Yes |
| `<name> release` | `0x16D` | **Releases** the pet from your control (a confirm gump appears for tamed pets; summons are dismissed immediately). | Yes |

There is also a Game-Master-only literal command, `<pet name> obey`, that forces a
creature to accept the speaker as its control master.

Source: `Scripts/Mobiles/AI/BaseAI.cs` (e.g. `case 0x168: // all kill`,
`case 0x16D: // *release`).

> **"Release" elsewhere:** saying `claim` to an animal trainer brings stabled pets out;
> there is no spoken "release" for stabling — see the vendor table below.

## Vendor & banking keywords

These are said **to an NPC** (or a player vendor), standing close to it. Bankers respond
within **12 tiles**; shopkeeper and player vendors want you adjacent. See
[Vendors & banking](/playing/vendors-and-banking/) for the full buying/selling flow and
[Communication & Social](/playing/communication-and-social/#talking-to-npcs-keyword-driven)
for keyword conversation in general.

All keyword commands here are **language-independent**.

### Bankers

Say these near any **banker** NPC. (You cannot bank while flagged **criminal**.)

| Say | Keyword | What it does |
|---|---|---|
| `Bank` | `0x2` | Opens your **bank box**. |
| `Balance` | `0x1` | The banker states your current gold balance. |
| `Withdraw <amount>` | `0x0` | Withdraws that much gold to your backpack, e.g. `withdraw 1000`. |
| `Check <amount>` | `0x3` | Writes you a **bank check** for that amount, drawn from your balance. |

### Shopkeeper (NPC) vendors

| Say | Keyword | What it does |
|---|---|---|
| `Vendor buy` | `0x3C` | Opens the shopkeeper's **buy** window. |
| `Vendor sell` | `0x14D` | Opens the **sell** window so you can sell goods. |
| `<vendor name> buy` | `0x171` | Buy from a vendor you name (`buy` alone works once named). |
| `<vendor name> sell` | `0x177` | Sell to a vendor you name (`sell` alone works once named). |

The two-word forms `vendor buy` / `vendor sell` are the most reliable — they do not
require you to know the NPC's name.

### Animal trainers (stablemasters)

| Say | Keyword | What it does |
|---|---|---|
| `Stable` | `0x8` | The trainer offers to **stable** a pet (target the pet). |
| `Claim` | `0x9` | Brings out your **stabled** pets; or `claim <pet name>` to retrieve one. |

(The same `stable` / `claim` keywords work at a **hitching post** and a **chicken coop**.)

### Player vendors (in houses)

| Say | Keyword | What it does |
|---|---|---|
| `Vendor buy` | `0x3C` | Opens the player vendor's for-sale list. |
| `<vendor name> browse` | `0x3D` | Browse the stock without buying. |
| `<vendor name> collect` | `0x3E` | **Owner:** collect the gold the vendor earned. |
| `<vendor name> status` | `0x3F` | **Owner:** check the vendor's fees/funds. |
| `<vendor name> dismiss` | `0x40` | **Owner:** dismiss (fire) the vendor. |
| `<vendor name> cycle` | `0x41` | **Owner:** cycle/reorganize its display. |

Source: `Scripts/Mobiles/NPCs/Banker.cs` (`case 0x0002: // *bank*`),
`Scripts/Mobiles/AI/VendorAI.cs` (`0x3C // *vendor buy*`),
`Scripts/Mobiles/NPCs/AnimalTrainer.cs` (`e.HasKeyword(0x0008) // *stable*`),
`Scripts/Mobiles/NPCs/PlayerVendor.cs`.

## Miscellaneous spoken triggers

A grab-bag of other commands the server listens for. All are **keyword** commands
(language-independent) unless noted.

### Self-status (say anywhere)

Handled globally in `Scripts/Misc/Keywords.cs` — no NPC needed:

| Say | Keyword | What it does |
|---|---|---|
| `I must consider my sins` | `0x32` | Reports your **murder counts** (short-term and long-term). See [Notoriety & PvP](/playing/notoriety-and-pvp/). |
| `I resign from my guild` | `0x2A` | **Leaves** your current player guild. |
| `I renounce my young player status` | `0x35` | Opens the prompt to give up **Young**-player protection. |
| `Guild` | `0x6` | Opens your **guild info** window. |

### NPCs and the world

| Say | Keyword | Where | What it does |
|---|---|---|---|
| `Guards` | `0x7` | In a guarded town | Calls the **town guards** to your location. |
| `News` | `0x30` | Near a **town crier** (or a news object) | Recites the current **news** (within ~12 tiles). |
| `Join` / `Member` | `0x4` | To an NPC **guildmaster** (named) | Ask to **join** their NPC guild. |
| `Resign` / `Quit` | `0x5` | To your NPC guildmaster | **Resign** from the NPC guild. |
| `Appraise` | `0x38` | To a **real-estate broker** | Target a house deed to **appraise** its value. |
| `Destination` | `0x1D` | To an **escortable** NPC | The NPC tells you where it wants to go. |
| `I will take thee` | `0x1E` | To an escortable NPC | **Accept the escort** quest. |
| `Disguise` | `0x1F` | To the **Thieves' Guildmaster** | Ask about a disguise kit (members only). |
| `Hire` / `Servant` | `0x162` | To a **hireable** NPC | Asks it to work for you; it quotes a daily wage. |
| `Orders` | `0xE6` | To a **faction guard** | A town sheriff issues orders (sheriff only). |
| `<npc name> train` | `0x6C` | To a townsperson | Lists skills it can teach; `<npc name> <skill>` then trains it a little. |
| `<npc name> time` | `0x9E` | To any NPC | Asks for the in-game **time**. |

Source: `Scripts/Misc/Keywords.cs`, `Scripts/Regions/GuardedRegion.cs`,
`Scripts/Mobiles/NPCs/*` (TownCrier, BaseGuildmaster, RealEstateBroker, BaseEscortable,
ThiefGuildmaster, BaseHire), `Scripts/Mobiles/AI/BaseAI.cs`.

## In seven languages

Because our `speech.mul` is an international build, the major keyword commands can be typed
in any of seven languages and all resolve to the same keyword id (the **Key** column). The
English wording is documented in the sections above; the phrases below are the equivalents
the **same** client file maps to that id, verified from `speech.mul`. Multiple forms in one
cell (separated by `/`) are alternates the file lists — for Japanese these are usually the
hiragana and katakana spellings of the same word. A dash (—) means the file carries no
distinct phrase for that language on that keyword.

| Command (English) | Key | 🇩🇪 German | 🇫🇷 French | 🇪🇸 Spanish | 🇨🇳 Chinese | 🇯🇵 Japanese | 🇰🇷 Korean |
|---|---|---|---|---|---|---|---|
| Lock down | `0x23` | ich möchte dies verankern | placer objet | quiero fijar esto | 我要將它鎖定 | ロックダウン / ろっくだうん | 고정보관 설정 |
| Release | `0x24` | ich möchte dies losmachen | libérer objet | quiero soltar esto | 我要解除鎖定 | ロックダウン解除 / ろっくだうんかいじょ / ロックダウンカイジョ | 고정보관 해제 |
| Secure | `0x25` | ich möchte dies sichern | verrouiller objet | quiero proteger esto | 我要將它保全 | セキュア / せきゅあ | 잠금 설정 |
| Unsecure | `0x26` | ich möchte dies entsichern | déverrouiller objet | quiero desproteger esto | 我要解除保全 | セキュア解除 / せきゅあかいじょ / セキュアカイジョ | 잠금 해제 |
| Place strongbox | `0x27` | ich möchte eine geldkassette platzieren | placer coffre-fort | quiero colocar una caja fuerte | 我要放一個保險櫃 | ストロングボックス / すとろんぐぼっくす | 스트롱박스 설치 |
| Place trash barrel | `0x28` | ich möchte eine mülltonne platzieren | placer poubelle | quiero colocar un cubo de basura | 我要放一個垃圾桶 | ゴミ箱 / ごみばこ / ゴミバコ | 쓰레기통 설치 |
| Ban (*I ban thee*) | `0x34` | ich verbanne dich | je te bannis | prohibir la entrada | 出去 | バン / ばん | 추방 |
| Eject (*Remove thyself*) | `0x33` | ich verstoße dich | — | — | 將自己移除 | 追い出す / おいだす / オイダス | 내쫓기 |
| All kill | `0x168` | alle töten | tous tuer | matad a todos | 全部宰殺 | おーるきる / オールキル | 모두 죽여 |
| All guard | `0x166` | alle bewachen | tous garder | proteged todos | 全部守衛 | オールガード / おーるがーど | 모두 지켜 |
| All follow me | `0x16C` | alle sollen mir folgen | tous me suivre | seguidme todos | 全部跟隨我 | おーるふぉろーみー / オールフォローミー | 모두 날 따라와 |
| All come | `0x164` | alle kommen | tous venir | venid todos | 全部過來 | オールカム / おーるかむ | 모두 이리와 |
| All stay | `0x170` | alle sollen bleiben | tous rester | quedaos todos | 全部停止 | おーるすてい / オールステイ | 모두 대기 |
| All stop | `0x167` | alle stehen bleiben | tous arrêter | deteneos todos | 全部停止 | おーるすとっぷ / オールストップ | 모두 정지 |
| Bank | `0x2` | — | — | banco | 銀行 | バンク / ばんく | 은행 |
| Balance | `0x1` | kontostand / Kontoauszug | solde / relevé | saldo | 結存 / 結單 / 残高 | バランス / ばらんす / ざんだか / ザンダカ | 잔고 / 잔액 |
| Withdraw | `0x0` | — | — | — | 提領 | 払い戻し / ひきだし / はらいもどし / ヒキダシ / ハライモドシ | 출금 |
| Check | `0x3` | scheck über | cheque / chèque | — | 支票 / 小切手 | こぎって / コギッテ | 수표 |
| Vendor buy | `0x3C` | händler kaufen | vendeur acheter / vendeur acquérir | compra vendedor / adquisición vendedor | 買 / 購買 / 購入 | こうにゅう / コウニュウ / 買う / かう / カウ | 물건 사기 / 물건 구입 |
| Vendor sell | `0x14D` | händler verkaufen | vendeur vendre | vender vendedor | 向小販賣東西 | 売る / うる / ウル | 물건 팔기 |
| Stable | `0x8` | stall | écurie | establo | 寄放寵物 | 預ける / あずける / アズケル | 마구간 |
| Claim | `0x9` | zurückverlangen | reprendre | reclamar | 提領寵物 / 返却 | へんきゃく / ヘンキャク | 찾기 |
| I must consider my sins | `0x32` | ich überdenke meine gesinnung | je dois examiner mes péchés | quiero considerar mis pecados | 我必須反省我的罪過 / 反省 | はんせい / ハンセイ | 범죄 상태 확인 |
| I resign from my guild | `0x2A` | ich trete aus meiner gilde aus | je quitte ma guilde | dimito del gremio | 退出公會 | ギルド脱退 / ぎるどだったい / ギルドダッタイ | 길드 탈퇴 |
| Guards | `0x7` | wächter | — | — | 警衛 | ガード / がーど | 경비병 |
| News | `0x30` | — | — | — | 新聞 | ニュース / にゅーす | 뉴스 |

This table is data-driven: the phrases come from `data/speech_languages.json`, extracted
from `speech.mul` by `tools/extract_speech_langs.py`. A dash usually just means the
international file did not include a separate localized form for that keyword (for the rare
keywords with no localized phrase, players on that client say the English form).

## Tips for AI agents

- **Keyword commands are forgiving about language** — the client resolves them — but they
  still need the **right wording your client knows**, said near the right target. Stand
  adjacent (bankers tolerate ~12 tiles).
- **Named commands need the name.** `kill` does nothing to a pet; `Rex kill` works. Same
  for `<vendor> collect`.
- **Watch the journal** for the server's prompt (e.g. *"Lock what down?"*) and then
  **target** what it asks for — many house and pet commands hand you a targeting cursor.
- **The literal commands must be English**: `I wish to resize my house` and the GM-only
  `obey` are matched on raw text, unlike everything else here.

## See also

- [Housing](/playing/housing/) — lockdowns, secures, access tiers, decay (these commands in context)
- [House Types](/playing/house-types/) — storage limits per house
- [Taming & pets](/playing/taming-and-pets/) — the full pet life cycle behind the pet orders
- [Vendors & banking](/playing/vendors-and-banking/) — buying, selling, bank checks
- [Communication & Social](/playing/communication-and-social/) — speech modes and NPC keyword conversation
- [Notoriety & PvP](/playing/notoriety-and-pvp/) — murder counts ("I must consider my sins")
