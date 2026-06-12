---
title: "템플릿: 대장장이(Blacksmith)"
description: 채광 + 대장기술 입문 빌드와 완전한 성장 스토리라인 — 이 샤드의 실제 제작 수치를 사용한 생성 선택, 훈련 표, 금전 루프, 결정 지점.
status: unverified
sources:
  - "external: UOSA Beginners Guide (wiki.uosecondage.com/Beginners_Guide)"
  - "external: UOSA Blacksmithy guide (wiki.uosecondage.com/Blacksmithy)"
  - "external: UOSA smith training discussion (forums.uosecondage.com/viewtopic.php?t=389)"
  - "wiki: /crafting/blacksmithy/, /crafting/tinkering/, /skills/mining/, /items/resources/, /mechanics/character-creation/"
  - "servuo: Scripts/Items/Resource/Ore.cs (smelting skill check)"
  - "servuo: Scripts/Services/Craft/Core/Resmelt.cs (66% ingot recovery)"
  - "servuo: Scripts/VendorInfo/SBBlacksmith.cs, SBMiner.cs, SBAnimalTrainer.cs (NPC prices)"
  - "servuo: Scripts/Services/BulkOrders/BulkOrderSystem.cs (BOD timing)"
last_verified: 2026-06-11
generated: false
---

> **상태: unverified.** 이 스토리라인은 고전 시대 커뮤니티 지혜를 우리 샤드에 적응시킨 것입니다.
> 아래의 모든 스킬 범위와 NPC 가격은 서버 소스와 대조 확인되었지만, 페이싱과 금전 추산은 플레이를
> 통한 필드 검증을 기다리고 있습니다.

대장장이는 경제 캐릭터입니다: 광석을 캐고, 제련하고, 두드려 물건을 만들고, 다른 플레이어의 모험을
당신의 수입으로 바꾸세요. 엔드게임 목표: **GM Blacksmithy + GM Mining**, 마크된 채광 지점들의 룬북,
꾸준한 [대량 주문](#bulk-order-deeds) 습관, 그리고 사람들이 부서진 플레이트를 들고 오는 대장장이라는
명성.

## 이 샤드의 캐릭터 생성

서버가 강제하는 [생성 규칙](/ko/mechanics/character-creation/)(스탯 90포인트, 스킬 4개 × 최대 50,
합계 120)에 따라:

| 선택 | 고를 것 | 이유 |
|---|---|---|
| 스탯 | **STR 60 / DEX 15 / INT 15** | STR은 운반 무게 — 광석은 무겁습니다. 서버 자체의 Blacksmith 직업 템플릿과 정확히 일치합니다. |
| 스킬 | **Blacksmithy 50, Mining 50, Tinkering 20** | 직업 버튼이 아니라 *커스텀* 템플릿을 쓰세요 — 커스텀 선택이 스킬별 시작 장비를 줍니다. |
| 도시 | **[Minoc](/ko/world/minoc/)** | 산, 화로, 모루, 그리고 은행이 한 짧은 루프 안에. |

시작 장비: Blacksmithy는 **집게, 곡괭이 2개, 철 주괴 50개, 반쪽 앞치마**를 주고; Mining은 세 번째
곡괭이를 추가하고; Tinkering은 **땜장이 도구 + 주괴 50개 더**를 추가합니다. 시작 금화 1,000에서,
Minoc 광부/땜장이에게서 사세요: 예비 **삽 (12 gp)**과 **곡괭이 (22–25 gp)**, 그리고 동물
트레이너에게서 **짐 말 (631 gp)**이나 **짐 라마 (565 gp)**를 고려하세요 — 트립당 운반량을 대략
두 배로 만듭니다(`Scripts/VendorInfo/SBMiner.cs`, `SBAnimalTrainer.cs`).

**여기 적용되지 않는 시대 조언:** 고전 가이드는 PK를 지나 광석을 나르는 것을 경고합니다. 당신은
**Trammel**에서 시작하고 이 샤드에서 적색은 Felucca로 제한됩니다(`Config/General.cfg`) — 더해 새
계정은 영(Young) 보호가 있습니다. 평화롭게 채광하세요.

## 1단계 — 초보 (Smithy 50→65, Mining 50→65)

**목표:** 자가 조달 루프. [Minoc 광산](/ko/world/minoc/)에서 철을 캐고, 화로에서 제련하고, 제작하고,
제품을 다시 제련하고, 잉여를 은행에 맡기세요.

- **제련은 Mining 판정입니다**(`Scripts/Items/Resource/Ore.cs`): 철광석은 25–75 구간에 맞춰
  제련되고, *실패한 제련은 목표 광석 더미의 절반을 태웁니다*. Mining 50에서는 제련의 약 절반이
  실패합니다 — Mining ~75까지는 **작은 더미로 제련하세요**, 거기서 철 제련이 실패 없이 됩니다.
- **커틀러스를 제작하세요** — 우리 샤드에서 커틀러스 구간은 **24.3–74.3**입니다
  ([제작 표](/ko/crafting/blacksmithy/)), 그래서 50(≈64% 성공)에서 ~65까지 데려가며, 시대 표준의
  "50–65 후 전환"이 아닙니다. 각 주괴 8개.
- 제작 굼프를 통해 **훈련 산출물을 제련하세요**: 회수율은 **주괴의 66%**입니다
  (`Scripts/Services/Craft/Core/Resmelt.cs`), 그래서 커틀러스 시도마다 주괴 ~3개를 잃습니다.
- **"전부 제작"** 묶음을 쓰세요 — 클릭당 여러 번의 성장 판정([스킬 성장](/ko/mechanics/skill-gain/)).

지금 돈: 솔직히 적습니다. NPC 대장장이는 **철 주괴당 3 gp**를 지불합니다(진열 가격 5 gp의 75%,
`SBBlacksmith.cs` + `Scripts/VendorInfo/GenericSell.cs`) — 원주괴 잉여를 파는 게 싸구려 무기를 파는
것보다 낫습니다(커틀러스는 12 gp밖에 못 받는데, 이는 원료인 주괴 8개*보다 적습니다*).

## 2단계 — 숙련 (Smithy 65→85, Mining 65→85)

- **훈련 표 (우리 수치, [/ko/crafting/blacksmithy/](/ko/crafting/blacksmithy/)에서):**
  ~65부터 **kryss 36.7–86.7** (주괴 8개), 그다음 ~75부터 **short spear 45.3–95.3** (주괴 6개).
- **Mining 65+는 유색 광맥을 엽니다** — 65에 dull copper, 70에 shadow, 75에 copper, 80에
  bronze([광석 표](/ko/items/resources/)). 유색 주괴는 NPC가 아니라 플레이어 대장장이에게 팔립니다.
- **Tinkering:** 시대 조언은 "Tinkering 20이면 삽을 만든다"고 하지만 — **여기서는 아닙니다**. 삽은
  **Tinkering 40–90**이 필요합니다([땜질 표](/ko/crafting/tinkering/)). **가위(5–55, 주괴 2개)**로
  20→40을 훈련한 뒤, 직접 삽을 만드세요. 그때까지는 12 gp NPC 삽이면 됩니다.
- Magery 친구가 있거나(또는 Recall 스크롤을 사서), **광산, 화로, 은행에 마크된 룬북**을 마련하세요 —
  운반 루프가 이 직업의 전부입니다.

## 3단계 — 마스터 (Smithy 85→GM, Mining 85→GM)

- **platemail gorget 56.4–106.4** (주괴 10개)이 ~80→95를 데려가고; **platemail gloves
  58.9–108.9** (주괴 12개)이 GM까지 데려갑니다 — 둘 다 구간이 GM 너머까지 가니 100.0*에서*도 성장을
  줍니다.
- **플레이트 차익거래:** NPC 방어구 상인은 **plate gorget당 52 gp**와 **plate gloves당 72 gp**를
  지불합니다(`SBBlacksmith.cs`), 익셉셔널이면 +25%. plate gloves는 주괴 12개를 72–90 gp로 바꿉니다 —
  **주괴당 6+ gp, 원주괴 비율의 두 배**. 당신의 GM 훈련이 스스로 비용을 댑니다; 시대 가이드는 대부분
  제련해 되돌리며 GM까지 주괴 40–55k를 예산했지만, 여기서는 고급품이 *팔립니다*.
- Mining 85→99는 gold/agapite/verite/**valorite (99)** 광맥을 엽니다 — 플레이어 전사들이 실제로 돈을
  내는 명품 주괴입니다.

## 대량 주문 증서

대장장이 BOD는 이 샤드에서 작동합니다(`Scripts/Services/BulkOrders/BulkOrderSystem.cs`, TOL 방식
시스템이 EJ 하에 활성): 어떤 NPC 대장장이든 **6시간마다 하나씩, 최대 2개까지 적립**해 제공합니다
(`Delay = 6`, `MaxCachedDeeds = 2`), Blacksmithy 스킬이 조금이라도 있으면. 훈련 산출물로 철 소형
BOD를 채우고 은행 갈 때마다 수거하세요 — 보상에는 NPC가 파는 어떤 것보다 나은 대장장이 도구와
재료가 포함됩니다.

## 거래 루프

| 행동 | 어디서 | 가격 (소스 확인) |
|---|---|---|
| 원철 주괴 판매 | NPC 대장장이, 어디든 | 각 3 gp; 진열 가격은 벤더가 흡수하는 1,000단위당 ~1 gp씩 떨어짐(경제 시스템, `GenericBuy.cs`) — 대량 처분은 여러 마을에 분산하세요 |
| 철 주괴 대량 판매 | 플레이어 제작자 (포럼 거래 게시판) | 3–5 gp — NPC의 5 gp 진열 가격 아래라면 대안을 깎아내림 |
| plate gorget / gloves 판매 | NPC 방어구 상인 | 52 / 72 gp 고정 (+25% 익셉셔널); 경제 아이템 아님, 가격 하락 없음 |
| 유색 주괴 & 익셉셔널 플레이트 판매 | 플레이어만 | NPC는 valorite를 철과 같은 값으로 지불 — 절대 유색을 NPC에 팔지 마세요 |
| 수리 | 붐비는 화로 (브리타니아, Minoc) | 팁; 수리는 나중에 당신 플레이트를 살 고객 명단을 만듭니다 |
| 삽/곡괭이 구매 | NPC 광부/땜장이 | 12 / 22–25 gp, Tinkering 40+까지 |

[브리타니아](/ko/world/britain/) 은행은 팔 만한 재고가 있을 때 현세의 시장입니다;
[Vesper](/ko/world/vesper/)는 Minoc의 작은 벤더 명단이 못 채우는 것을 커버합니다.

## 결정 지점과 흔한 실수 (에이전트용)

- **계속 과중량이면** → STR이 너무 낮거나 짐 동물이 없음; 걷기 전에 산비탈 화로 인접 지점에서
  제련하고, 주괴는 광석보다 훨씬 가볍다는 것을 기억하세요.
- **제련이 계속 광석을 파괴하면** → Mining이 ~75 미만; 작은 더미로 제련하거나, 손실을 Mining 훈련으로
  받아들이세요(판정이 스킬을 성장시킵니다).
- **제작 아이템 성공률이 ~80% 이상이면** → 성장이 느려졌습니다; 표에서 내려가세요(커틀러스 → kryss →
  short spear → plate gorget → plate gloves), [실제 구간](/ko/crafting/blacksmithy/)에 따라.
- **훈련 무기를 NPC에 팔고 싶다면** → 그러지 마세요; 제련은 주괴의 66%를 회수하니, 11–16 gp 판매보다
  가치 있습니다. 예외: plate gorget/gloves는 금속 가치보다 높게 팔립니다.
- **유색 광맥이 평범한 철을 내면** → Mining이 그 광석의 요건 미만([표](/ko/skills/mining/)); 광맥이
  낭비된 건 아니니, 나중에 다시 오세요.
- **한 벤더에서 주괴 가격이 붕괴하면** → ~1,000+ 단위를 먹였습니다; 마을을 돌리거나 플레이어 대량
  시장으로 전환하세요.
- **"Blacksmith" 직업 버튼을 골랐다면** → 고정된 30포인트 스킬과 커스텀 장비 없음을 받았습니다;
  여기서는 커스텀 템플릿이 엄밀히 더 낫습니다.
- **AFK 매크로에 의존하지 마세요** — 안티 매크로 *코드*는 꺼져
  있지만([스킬 성장](/ko/mechanics/skill-gain/)), 고전 가이드는 무인 플레이를 1위 밴 유발 요인으로
  부릅니다; 이 샤드의 성문 정책은 이를 다루지 않으니, 용인된다고 가정하기 전에 포럼에서 물어보세요.

## 관련

- [Blacksmithy 스킬](/ko/skills/blacksmithy/) · [Mining 스킬](/ko/skills/mining/) ·
  [자원](/ko/items/resources/) · [시작하기](/ko/guides/getting-started/)
- [템플릿: 벌목꾼(Lumberjack)](/ko/templates/lumberjack/) — 같은 아이디어, 다만 나무로
