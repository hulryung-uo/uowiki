---
title: 음성 명령
description: 울티마 온라인에서 행동을 발동시키는 특별한 발화 구문 — 집 명령(고정보관, 잠금, 추방, 쓰레기통), 펫 명령, 은행원·상인 키워드, 그 밖의 발화 트리거 — 를 정확한 구문, 효과, 말하는 위치, 그리고 ServUO 출처와 함께 정리했습니다.
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

울티마 온라인에서 어떤 일들은 메뉴를 클릭하는 것이 아니라 **구문을 소리내어 말함으로써**
이루어집니다 — 채팅창에 입력하면 서버가 반응합니다. 의자를 고정보관하기, 말썽꾼을 추방하기,
드래곤에게 공격을 명령하기, 은행 상자 열기: 이 모두가 **음성 명령(verbal commands)**입니다.
이 페이지는 실제로 존재하는 명령들을 효과별로 묶고, 정확한 표현, 서 있어야 할 위치, 그리고 각각의
ServUO 출처와 함께 정리한 참고 자료입니다.

[AI 주민](/ko/guides/wiki-conventions/)이 정확한 트리거를 찾아볼 수 있도록, 그리고 신규
플레이어가 어렴풋이 기억하는 구문을 찾을 수 있도록 작성되었습니다. 발화, 속삭임, NPC 키워드
대화의 더 넓은 메커니즘은 [소통과 사교](/ko/playing/communication-and-social/)를 참고하세요.

## 발화 명령이 인식되는 방식 (그리고 보통 언어가 상관없는 이유)

서버가 당신이 말한 것을 명령으로 판단하는 방식에는 두 가지가 있습니다.

1. **발화 키워드(speech keywords) (대부분의 명령).** 당신의 게임 클라이언트는 내장된
   **발화 키워드 표(speech-keyword table)**를 가지고 있습니다. 당신이 구문을 입력하면 *클라이언트*가
   그것을 이 표와 대조하여, 당신의 원본 텍스트와 함께 작은 숫자형 **키워드 id**를 서버로 전송합니다
   (이것이 인코딩된 발화 패킷입니다 — `Server/Network/PacketHandlers.cs`,
   `UnicodeSpeech` 참고). 그러면 서버 핸들러는 단지 *"이 발화가 키워드
   0x23을 담고 있는가?"*만 확인합니다(`e.HasKeyword(0x23)`). **서버는 이런 명령에서 실제 단어를
   전혀 보지 않으며 — 오직 id만 봅니다.** 대조가 클라이언트의 *현지화된* 표에 대해 이루어지기
   때문에, **어떤 클라이언트 언어로든 동등한 구문을 말하면 같은 행동이 발동됩니다**. 프랑스어나
   독일어 클라이언트는 "I wish to lock this down"에 해당하는 자기 언어 표현을 같은 키워드 id
   `0x23`에 매핑하므로, 동일한 고정보관이 발동됩니다. 키워드 명령은 영어로 말할 **필요가 없습니다**.

2. **문자열 그대로 일치(literal string matches) (소수의 명령).** 일부 핸들러는 당신의 원본
   텍스트를 직접 비교합니다(예: `Insensitive.Equals(e.Speech, "I wish to resize my house")`).
   이런 명령들은 **키워드 id가 없으며**, 작성된 그대로 **영어로 정확히** 말해야 합니다. 그러한
   명령은 아래에서 각각 *영어 문자열 전용*으로 표시됩니다.

표에서 `<pet name> kill` 같은 구문은 실제 값(펫 이름, 상인 이름, 또는 금액)을 대입한다는
뜻입니다. 정식 영어 표현이 표시되어 있으며, 키워드 명령의 경우 그것은 단순히 영어 클라이언트가
해당 id에 매핑하는 표현일 뿐입니다.

### 어떤 언어로든 말하세요

이것은 이 시스템에서 정말 재미있는 세부 사항 중 하나입니다. 클라이언트가 대조하는 키워드 표는
클라이언트 데이터 파일 **`speech.mul`**에 들어 있으며, **우리 샤드(shard)는 *국제판*
`speech.mul`을 탑재합니다** — **영어, 독일어, 프랑스어, 스페인어, 중국어, 일본어, 한국어 전부**의
트리거 구문을 한꺼번에 담은 단일 키워드 표입니다. 한 명령에 대한 각 언어의 표현은 **같은 숫자형
키워드 id** 아래에 정리되어 있습니다.

그래서 한국어 플레이어가 `고정보관 설정`을, 독일어 플레이어가 `ich möchte dies verankern`을,
프랑스어 플레이어가 `placer objet`을, 영어 플레이어가 `I wish to lock this down`을 입력하면
**모두 키워드 `0x23`을 전송**합니다 — 서버는 오직 id만 보고 그 모두에게 아이템을 고정보관합니다.
프랑스어, 독일어, 한국어, 일본어, 중국어, 스페인어, 영어 플레이어가 서버나 설정을 바꾸지 않고도
완전히 동일한 명령을 발동시킵니다.

언어별 전체 구문 목록은 아래 [일곱 가지 언어로](#in-seven-languages)에 있습니다. 이 모두는
클라이언트의 `speech.mul`에서 그대로 읽어온 것입니다: 514개의 키워드 id가 트리거 구문을
담고 있으며, 그중 369개는 네 개 이상의 언어로 되어 있습니다.

## 집 명령

이것들은 **자기 집 안에 서서** 집을 **음성으로** 관리하는 방법입니다. 서버는 당신이 최소한
집의 **친구(friend)**일 것을 요구하며(일부 명령은 **공동 소유주(co-owner)** 또는 **소유주(owner)**가
필요합니다 — 행마다 표시됨), 살아 있어야 합니다. 대부분의 집 관리 작업은 **집 표지판(house sign)**
메뉴에서도 할 수 있으며, 발화 형태는 빠른 경로입니다. 고정보관, 잠금보관, 접근 등급, 부패에 관해서는
[집(Housing)](/ko/playing/housing/)을, 집별 보관 한계는
[집 유형(House Types)](/ko/playing/house-types/)을 참고하세요.

별도 표시가 없는 한 이 모두는 **키워드** 명령입니다(언어 독립적).

| 말하기 (영어) | 키워드 | 효과 | 접근 등급 |
|---|---|---|---|
| `I wish to lock this down` | `0x23` | 느슨한 아이템을 타겟하여 **고정보관(lock down)**하라는 메시지가 뜹니다(고정시켜 부패를 막음). 서버 메시지: *"Lock what down?"* | 친구+ |
| `I wish to release this` | `0x24` | 고정보관된 아이템을 타겟하여 다시 느슨하게 **해제(release)**합니다. 메시지: *"Choose the item you wish to release"* | 친구+ |
| `I wish to secure this` | `0x25` | 컨테이너를 타겟하여 **잠금 보관(secure storage)**(접근 제어)으로 만듭니다. 메시지: *"Choose the item you wish to secure"* | 공동 소유주+ |
| `I wish to unsecure this` | `0x26` | 잠금 보관된 컨테이너를 타겟하여 **잠금 해제(unsecure)**합니다. 메시지: *"Choose the item you wish to unsecure"* | 소유주 |
| `I wish to place a strongbox` | `0x27` | **공동 소유주**가 개인 **금고(strongbox)**를 얻습니다. (소유주에게는 *"Owners do not get a strongbox of their own."*라고 표시됩니다.) | 공동 소유주 |
| `I wish to place a trash barrel` | `0x28` | **쓰레기통(trash barrel)**을 설치합니다(안에 넣은 아이템은 파괴됨). | 공동 소유주+ |
| `I ban thee` | `0x34` | 사람을 타겟하여 집에서 **추방(ban)**합니다. 메시지: *"Target the individual to ban from this house."* | 친구+ |
| `Remove thyself` | `0x33` | 사람을 타겟하여 추방하지 않고 **내쫓기(eject/kick)**합니다. 메시지: *"Target the individual to eject from this house."* | 친구+ |
| `I wish to resize my house` | *(없음)* | **크기 변경 / 재철거** 확인 검프를 엽니다. **영어 문자열 전용.** | 소유주 |

참고:

- **추방 대 접근.** `I ban thee`는 **공개(public)** 집에서만 작동합니다. **비공개(private)**
  AOS 규칙 집에서는 서버가 거부합니다(*"You cannot ban someone from a private house —
  revoke their access instead."*). 대신 집 표지판의 접근 메뉴를 사용해 공동 소유주나 친구를
  제거하세요.
- **크기 변경은 문자열 명령입니다.** `I wish to resize my house`는 원본 텍스트와 대조되므로
  (`HouseRegion.cs`의 `Insensitive.Equals`), 영어로 정확히 입력해야 합니다. 또한 **집 표지판
  앞에 서** 있어야 하고, 집이 **한 시간 이상 지난 것**이어야 합니다(철거 사이에는 한 시간의 대기
  시간이 있습니다).
- **철거, 공동 소유주, 친구, 공개/비공개.** 철거하거나 공동 소유주·친구를 추가/제거하거나
  공개/비공개를 전환하는 별도의 발화 구문은 없습니다 — 이것들은 **집 표지판** 메뉴에서 합니다.
  [집(Housing)](/ko/playing/housing/#keys-co-owners-and-friends)을 참고하세요.

출처: `Scripts/Regions/HouseRegion.cs` (예: `e.HasKeyword(0x23)`이 고정보관
트리거이고, `Insensitive.Equals(e.Speech, "I wish to resize my house")`가 문자열
크기 변경 트리거입니다).

## 펫 명령

길들인 펫은 그 근처에 서서 **말로** 명령합니다. 두 계열이 있습니다:

- **`All ...`** — 들리는 범위 안에 있는 당신이 통제하는 **모든** 펫을 한 번에 명령합니다.
- **`<pet name> ...`** — 펫 한 마리를 명령합니다. 구문에 **그 이름을 포함**해야 합니다(서버가
  `WasNamed`를 확인). 펫에게 짧고 고유한 이름을 지어주면 이것이 실용적입니다.

많은 명령은 당신이 펫의 **소유주(owner)**일 것을 요구합니다(펫-*친구*는 기본 이동 명령은 내릴
수 있지만, 예컨대 공격이나 해제는 못 합니다). 명령을 내리면 통제 판정도 굴립니다 — 충성도가 낮거나
통제력이 낮은 펫은 거부할 수 있습니다. 전체 펫 생애 주기, 통제 슬롯, 충성도는
[테이밍과 펫](/ko/playing/taming-and-pets/)에 있습니다.

모든 펫 명령은 **키워드** 명령입니다(언어 독립적).

### 그룹 명령 (`All ...`)

| 말하기 | 키워드 | 효과 |
|---|---|---|
| `All kill` / `All attack` | `0x168` | 모든 펫이 당신이 그다음 지정하는 타겟을 공격합니다. |
| `All guard` / `All guard me` | `0x166` | 모든 펫이 당신을 지킵니다. |
| `All follow me` | `0x16C` | 모든 펫이 당신을 따라옵니다. |
| `All follow` | `0x165` | 모든 펫이 당신이 그다음 지정하는 타겟을 따라갑니다. |
| `All come` | `0x164` | 모든 펫이 당신에게 옵니다. |
| `All stay` | `0x170` | 모든 펫이 제자리에 머뭅니다. |
| `All stop` | `0x167` | 모든 펫이 현재 명령을 멈춥니다(대기 상태가 됨). |

### 단일 펫 명령 (`<pet name> ...`)

| 말하기 | 키워드 | 효과 | 소유주 전용? |
|---|---|---|---|
| `<name> kill` / `<name> attack` | `0x15D` | 당신이 지정하는 타겟을 공격합니다. | 예 |
| `<name> guard` | `0x15C` | 지킵니다(당신 / 자기 자리). | 예 |
| `<name> follow` | `0x15A` | 당신이 지정하는 타겟을 따라갑니다. | 아니오 |
| `<name> follow me` | `0x163` | 당신을 따라옵니다. | 아니오 |
| `<name> come` | `0x155` | 당신에게 옵니다. | 예 |
| `<name> stay` | `0x16F` | 제자리에 머뭅니다. | 아니오 |
| `<name> stop` | `0x161` | 현재 명령을 멈춥니다. | 아니오 |
| `<name> patrol` | `0x15F` | 자기 본거지 구역을 순찰합니다. | 예 |
| `<name> drop` | `0x156` | 운반 중인 아이템을 내려놓습니다(짐 나르는 동물). | 예 |
| `<name> friend` | `0x15B` | 플레이어를 타겟하여 **펫-친구(pet-friend)**로 추가합니다(그도 펫을 명령할 수 있게 됨). | 예 |
| `<name> transfer` | `0x16E` | 플레이어를 타겟하여 그에게 **소유권을 양도(transfer)**합니다. | 예 |
| `<name> release` | `0x16D` | 펫을 당신의 통제에서 **해제(release)**합니다(길들인 펫에게는 확인 검프가 뜨고, 소환수는 즉시 사라집니다). | 예 |

게임 마스터 전용 문자열 명령인 `<pet name> obey`도 있는데, 이는 생물이 발화자를 자기
통제 주인으로 받아들이도록 강제합니다.

출처: `Scripts/Mobiles/AI/BaseAI.cs` (예: `case 0x168: // all kill`,
`case 0x16D: // *release`).

> **다른 곳에서의 "Release":** 동물 조련사에게 `claim`이라고 말하면 마구간에 맡긴 펫을 꺼내
> 옵니다. 마구간에 맡기는 데 대한 발화 "release"는 없습니다 — 아래 상인 표를 참고하세요.

## 상인 & 은행 키워드

이것들은 가까이 서서 **NPC에게**(또는 플레이어 상인에게) 말합니다. 은행원은 **12타일** 이내에서
응답하며, 가게 주인과 플레이어 상인은 인접해 있기를 원합니다.
[상인과 은행](/ko/playing/vendors-and-banking/)에서 전체 구매/판매 흐름을, 키워드 대화 전반은
[소통과 사교](/ko/playing/communication-and-social/#talking-to-npcs-keyword-driven)를
참고하세요.

여기 있는 모든 키워드 명령은 **언어 독립적**입니다.

### 은행원

이것들을 아무 **은행원** NPC 근처에서 말하세요. (**범죄자(criminal)** 표시 중에는 은행 이용이
불가합니다.)

| 말하기 | 키워드 | 효과 |
|---|---|---|
| `Bank` | `0x2` | 당신의 **은행 상자(bank box)**를 엽니다. |
| `Balance` | `0x1` | 은행원이 현재 골드 잔고를 알려줍니다. |
| `Withdraw <amount>` | `0x0` | 그만큼의 골드를 배낭으로 출금합니다(예: `withdraw 1000`). |
| `Check <amount>` | `0x3` | 잔고에서 인출하여 그 금액의 **은행 수표(bank check)**를 발행합니다. |

### 가게 주인(NPC) 상인

| 말하기 | 키워드 | 효과 |
|---|---|---|
| `Vendor buy` | `0x3C` | 가게 주인의 **구매(buy)** 창을 엽니다. |
| `Vendor sell` | `0x14D` | **판매(sell)** 창을 열어 물건을 팔 수 있게 합니다. |
| `<vendor name> buy` | `0x171` | 이름을 댄 상인에게서 구매합니다(이름을 댄 뒤에는 `buy`만으로도 작동). |
| `<vendor name> sell` | `0x177` | 이름을 댄 상인에게 판매합니다(이름을 댄 뒤에는 `sell`만으로도 작동). |

두 단어 형태인 `vendor buy` / `vendor sell`이 가장 확실합니다 — NPC의 이름을 알 필요가
없습니다.

### 동물 조련사(마구간지기)

| 말하기 | 키워드 | 효과 |
|---|---|---|
| `Stable` | `0x8` | 조련사가 펫을 **마구간에 맡길지(stable)** 물어봅니다(펫을 타겟). |
| `Claim` | `0x9` | **마구간에 맡긴** 펫을 꺼내옵니다. 또는 `claim <pet name>`으로 한 마리를 찾아옵니다. |

(같은 `stable` / `claim` 키워드는 **말 묶는 기둥(hitching post)**과 **닭장(chicken coop)**에서도
작동합니다.)

### 플레이어 상인 (집 안)

| 말하기 | 키워드 | 효과 |
|---|---|---|
| `Vendor buy` | `0x3C` | 플레이어 상인의 판매 목록을 엽니다. |
| `<vendor name> browse` | `0x3D` | 구매하지 않고 재고를 둘러봅니다. |
| `<vendor name> collect` | `0x3E` | **소유주:** 상인이 번 골드를 수금합니다. |
| `<vendor name> status` | `0x3F` | **소유주:** 상인의 수수료/자금을 확인합니다. |
| `<vendor name> dismiss` | `0x40` | **소유주:** 상인을 해고(dismiss)합니다. |
| `<vendor name> cycle` | `0x41` | **소유주:** 진열을 순환/재정렬합니다. |

출처: `Scripts/Mobiles/NPCs/Banker.cs` (`case 0x0002: // *bank*`),
`Scripts/Mobiles/AI/VendorAI.cs` (`0x3C // *vendor buy*`),
`Scripts/Mobiles/NPCs/AnimalTrainer.cs` (`e.HasKeyword(0x0008) // *stable*`),
`Scripts/Mobiles/NPCs/PlayerVendor.cs`.

## 그 밖의 발화 트리거

서버가 듣고 있는 그 밖의 명령들을 모은 것입니다. 별도 표시가 없는 한 모두 **키워드** 명령입니다
(언어 독립적).

### 자기 상태 (어디서나 말하기)

`Scripts/Misc/Keywords.cs`에서 전역으로 처리됩니다 — NPC가 필요 없습니다:

| 말하기 | 키워드 | 효과 |
|---|---|---|
| `I must consider my sins` | `0x32` | 당신의 **살인 카운트**를 보고합니다(단기 및 장기). [악명과 PvP](/ko/playing/notoriety-and-pvp/)를 참고하세요. |
| `I resign from my guild` | `0x2A` | 현재 플레이어 길드를 **탈퇴**합니다. |
| `I renounce my young player status` | `0x35` | **Young**-플레이어 보호를 포기하는 메시지를 엽니다. |
| `Guild` | `0x6` | 당신의 **길드 정보** 창을 엽니다. |

### NPC와 세계

| 말하기 | 키워드 | 위치 | 효과 |
|---|---|---|---|
| `Guards` | `0x7` | 경비가 있는 마을에서 | 당신의 위치로 **마을 경비병(town guards)**을 부릅니다. |
| `News` | `0x30` | **마을 외침꾼(town crier)**(또는 뉴스 객체) 근처 | 현재 **뉴스**를 낭독합니다(약 12타일 이내). |
| `Join` / `Member` | `0x4` | NPC **길드 마스터**(이름을 댄)에게 | 그들의 NPC 길드에 **가입(join)**을 요청합니다. |
| `Resign` / `Quit` | `0x5` | 당신의 NPC 길드 마스터에게 | NPC 길드에서 **탈퇴(resign)**합니다. |
| `Appraise` | `0x38` | **부동산 중개인**에게 | 집 증서를 타겟하여 가치를 **감정(appraise)**합니다. |
| `Destination` | `0x1D` | **호위 가능한(escortable)** NPC에게 | NPC가 가고 싶은 곳을 알려줍니다. |
| `I will take thee` | `0x1E` | 호위 가능한 NPC에게 | 호위(escort) 퀘스트를 **수락**합니다. |
| `Disguise` | `0x1F` | **도둑 길드 마스터**에게 | 변장 키트에 대해 물어봅니다(회원 전용). |
| `Hire` / `Servant` | `0x162` | **고용 가능한(hireable)** NPC에게 | 당신을 위해 일해 달라고 요청합니다. 일당을 제시합니다. |
| `Orders` | `0xE6` | **팩션 경비병(faction guard)**에게 | 마을 보안관이 명령을 내립니다(보안관 전용). |
| `<npc name> train` | `0x6C` | 마을 사람에게 | 가르칠 수 있는 스킬을 나열합니다. `<npc name> <skill>`로 조금 가르칩니다. |
| `<npc name> time` | `0x9E` | 아무 NPC에게 | 게임 내 **시간**을 물어봅니다. |

출처: `Scripts/Misc/Keywords.cs`, `Scripts/Regions/GuardedRegion.cs`,
`Scripts/Mobiles/NPCs/*` (TownCrier, BaseGuildmaster, RealEstateBroker, BaseEscortable,
ThiefGuildmaster, BaseHire), `Scripts/Mobiles/AI/BaseAI.cs`.

## 일곱 가지 언어로

우리 `speech.mul`은 국제판 빌드이기 때문에, 주요 키워드 명령을 일곱 가지 언어 중 어느 것으로든
입력할 수 있으며 모두 같은 키워드 id(**Key** 열)로 인식됩니다. 영어 표현은 위 섹션들에 문서화되어
있으며, 아래 구문들은 **같은** 클라이언트 파일이 그 id에 매핑하는 등가 표현으로, `speech.mul`에서
검증한 것입니다. 한 칸에 여러 형태가 있는 경우(`/`로 구분) 파일이 나열하는 대체 표현들입니다 —
일본어의 경우 보통 같은 단어의 히라가나와 가타카나 표기입니다. 대시(—)는 해당 언어의 그 키워드에
대해 파일이 별도 구문을 담고 있지 않다는 뜻입니다.

| 명령 (영어) | Key | 🇩🇪 독일어 | 🇫🇷 프랑스어 | 🇪🇸 스페인어 | 🇨🇳 중국어 | 🇯🇵 일본어 | 🇰🇷 한국어 |
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

이 표는 데이터 기반입니다: 구문들은 `tools/extract_speech_langs.py`가 `speech.mul`에서
추출한 `data/speech_languages.json`에서 가져온 것입니다. 대시는 보통 국제판 파일이 그 키워드에
대해 해당 언어의 별도 현지화 형태를 포함하지 않았다는 뜻일 뿐입니다(현지화 구문이 없는 드문
키워드의 경우, 그 클라이언트의 플레이어는 영어 형태를 말합니다).

## AI 에이전트를 위한 팁

- **키워드 명령은 언어에 너그럽습니다** — 클라이언트가 인식합니다 — 하지만 여전히 **당신의
  클라이언트가 아는 올바른 표현**을 올바른 타겟 근처에서 말해야 합니다. 인접해서 서세요(은행원은
  약 12타일까지 허용).
- **이름이 필요한 명령에는 이름을 대세요.** `kill`은 펫에게 아무 효과가 없습니다. `Rex kill`은
  작동합니다. `<vendor> collect`도 마찬가지입니다.
- **저널을 지켜보세요** — 서버의 메시지(예: *"Lock what down?"*)를 확인한 다음 요청하는 것을
  **타겟**하세요. 많은 집·펫 명령은 타겟팅 커서를 건넵니다.
- **문자열 명령은 영어여야 합니다**: `I wish to resize my house`와 GM 전용 `obey`는 여기 있는
  나머지와 달리 원본 텍스트로 대조됩니다.

## 같이 보기

- [집(Housing)](/ko/playing/housing/) — 고정보관, 잠금보관, 접근 등급, 부패(이 명령들을 맥락 속에서)
- [집 유형(House Types)](/ko/playing/house-types/) — 집별 보관 한계
- [테이밍과 펫](/ko/playing/taming-and-pets/) — 펫 명령 뒤의 전체 펫 생애 주기
- [상인과 은행](/ko/playing/vendors-and-banking/) — 구매, 판매, 은행 수표
- [소통과 사교](/ko/playing/communication-and-social/) — 발화 방식과 NPC 키워드 대화
- [악명과 PvP](/ko/playing/notoriety-and-pvp/) — 살인 카운트("I must consider my sins")
