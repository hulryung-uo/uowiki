---
title: "템플릿: 벌목꾼(Lumberjack)"
description: 벌목 + 활제작 입문 빌드와 완전한 성장 스토리라인 — 이 샤드의 실제 제작 수치를 사용한 생성 선택, 활 금전 루프, 훈련 표, 결정 지점.
status: unverified
sources:
  - "external: UOSA money-making guide (forums.uosecondage.com/viewtopic.php?t=45914)"
  - "external: Seth's Easy Lumberjacking Guide (forums.uosecondage.com/viewtopic.php?t=37138)"
  - "external: uoguide.com/Lumberjacking (axe damage bonus)"
  - "wiki: /crafting/bowfletching/, /crafting/carpentry/, /crafting/tinkering/, /skills/lumberjacking/, /items/resources/, /mechanics/character-creation/"
  - "servuo: Scripts/Misc/CharacterCreation.cs (Fletching starter kit)"
  - "servuo: Scripts/VendorInfo/SBRangedWeapon.cs, SBCarpenter.cs (NPC prices)"
  - "servuo: Scripts/Mobiles/NPCs/Bowyer.cs + Scripts/Services/BulkOrders/BulkOrderSystem.cs (fletching BODs)"
last_verified: 2026-06-11
generated: false
---

> **상태: unverified.** 이 스토리라인은 고전 시대 커뮤니티 지혜를 우리 샤드에 적응시킨 것입니다.
> 아래의 스킬 범위와 NPC 가격은 서버 소스와 대조 확인되었지만; 페이싱과 수입 추산은 플레이를 통한
> 필드 검증을 기다리고 있습니다.

벌목꾼은 고전적인 무위험 입문자입니다: 나무는 공짜고, 도끼는 싸며, 당신이 베는 모든 판자는 금화이거나
스킬입니다. 엔드게임 목표: **GM Lumberjacking + GM Fletching**, 당신의 **첫 집 종잣돈**을 대는
판자-와-활 파이프라인 — 그리고, 혹시라도 싸우고 싶어진다면
[Lumberjacking은 은밀히 도끼 +데미지](/ko/skills/lumberjacking/)이니(GM에서 ~+30%까지), 이 캐릭터는
다른 어떤 제작자보다 도끼 전사로 전환이 잘 됩니다.

## 이 샤드의 캐릭터 생성

[생성 규칙](/ko/mechanics/character-creation/)(스탯 90포인트, 스킬 4개 × 최대 50, 합계 120)에 따라:

| 선택 | 고를 것 | 이유 |
|---|---|---|
| 스탯 | **STR 60 / DEX 15 / INT 15** | STR = 운반 무게 = 트립당 판자. 통나무는 판자의 두 배 무게이니 — STR과 아래의 판자 규칙이 물류 게임의 전부입니다. |
| 스킬 | **Lumberjacking 50, Fletching 50, Carpentry 20** | 커스텀 템플릿. Carpentry 20은 나중의 통/가구 부업의 씨앗입니다. |
| 도시 | **[Yew](/ko/world/yew/)** | 마을 자체*가* 숲이며, 활제작자, 목수, 그리고 — 그렇습니다 — **Empath Abbey의 은행** (652, 820)이 있습니다. |

시작 장비(`Scripts/Misc/CharacterCreation.cs`에서 검증됨): Lumberjacking은 **손도끼**를 주고;
Fletching은 **판자 14, 깃털 5, 화살대 5**를 주고; Carpentry는 **톱, 판자 10, 반쪽 앞치마**를 줍니다.
예비 손도끼는 어떤 무기제작자에게든 ~25 gp입니다. 시작 금화 1,000은 예비품에 더해, 더 큰 운반량을
원하면 **짐 말 (631 gp)**까지 쉽게 충당합니다.

**변형:** Carpentry를 **Tinkering**으로 바꿔 손도끼를 직접 만들 수 있지만 — 우리
[땜질 표](/ko/crafting/tinkering/)는 손도끼를 **30–80 스킬**에 두니, Tinkering 20으로는 못 만듭니다;
Tinkering 50에서 시작하며 Fletching 포인트를 깎아야 합니다. 순수 금전/제작 시작에는 Carpentry 20이
더 깔끔한 선택입니다.

## 가장 중요한 한 가지 규칙

**언제나 통나무를 그 자리에서 판자로 쪼개세요**(통나무에 도끼 사용). 판자는 절반 무게이고, 모든
레시피가 받으며, NPC 목수는 **통나무당 1 gp 대비 판자당 2 gp**를 지불합니다
(`Scripts/VendorInfo/SBCarpenter.cs`). 판자 자르기는 그 나무 수준의 Carpentry *또는* Lumberjacking이
필요합니다([표](/ko/items/resources/)) — 당신이 쪼갤 수 있는 것에는 Lumberjacking이 항상 자격이
됩니다.

## 1단계 — 초보 (Lumberjacking 50→65, Fletching 50→70)

**목표:** 활 루프. Yew 숲에서 쪼개고, 판자를 자르고, 우리 [활제작 표](/ko/crafting/bowfletching/)에
따라 **활(30–70 스킬, 판자 7개)**을 제작하고, NPC 활제작자에게 팔고, Empath Abbey에서 은행에
맡기세요.

- Fletching 50에서 활은 동전 던지기이고; 70이면 보장됩니다. 각 쪼개기는 **통나무 10개**를
  냅니다([벌목](/ko/skills/lumberjacking/)), 즉 ~1.4개의 활.
- **NPC 활제작자는 활당 17 gp를 지불합니다**(익셉셔널 21 gp, `SBRangedWeapon.cs` +
  `GenericSell.cs`) — 시대 가이드의 ~30 gp가 *아닙니다*. 활을 통하면 판자당 ~2.4 gp 대 원료 2 gp이니,
  1단계 활은 대부분 *스킬*이고 금화는 부산물입니다.
- **적용되지 않는 시대 조언:** 여기엔 시간당 되사기 가격 하락이 없습니다. 무기 판매 가격은 고정 표
  가격입니다 — 활을 위해 활제작자 여섯 곳 순회를 돌 필요가 없습니다. (판자 같은 누적 가능 품목은
  하락합니다 — 거래 루프 참고.)
- 자주 은행에 맡기세요; 당신은 Trammel에서 시작하고 적색은 Felucca 전용이니, Yew 벌목꾼을 죽이는
  유일한 것은 마을 남쪽 던전 근처에서의 자만뿐입니다.

## 2단계 — 숙련 (Lumberjacking 65→90, Fletching 70→90)

- **Fletching ~70에서 석궁으로 전환**: 우리 구간은 **60–100**(판자 7개)이고, **25 gp**에 팔립니다 —
  판자당 ~3.6 gp, 활제작 책에서 최고의 NPC 비율. 시대 가이드는 석궁을 ~68에 두었고; 여기서는 GM까지
  *내내 성장*합니다.
- Lumberjacking 65는 **oak**(광맥의 30%)를, 80은 **ash**를 엽니다 — 유색 판자는 플레이어 시장
  상품입니다([목재 표](/ko/items/resources/)).
- **Fletching BOD가 이 샤드에 존재합니다**(고전 시대에는 없었습니다): 어떤 NPC 활제작자든 Fletching
  스킬이 조금이라도 있으면 6시간마다 하나, 최대 2개까지 적립해 제공합니다
  (`Scripts/Mobiles/NPCs/Bowyer.cs`, `BulkOrderSystem.cs`). 판매하러 갈 때마다 수거하세요.
- **깃털을 모으고**(새, harpy) 남는 자투리를 **화살(0–40 스킬)**로 바꾸세요. NPC는 화살당 1 gp밖에
  안 주니, 시대의 "화살 돈"은 여기서 플레이어 시장입니다 — 화살은 벤더가 아니라 포럼 거래 게시판의
  궁수에게 대량으로 파세요.
- 선택: **통(57.8–82.8)** 부업을 향해 Carpentry 20→58(지팡이 0–25, 통 뚜껑 11–36)을 훈련하세요 —
  통은 **통 테(barrel hoop), 즉 땜장이 레시피**도 필요하니([목공 표](/ko/crafting/carpentry/),
  [땜질](/ko/crafting/tinkering/)), 그것들을 살 예산을 잡으세요.

## 3단계 — 마스터 (Lumberjacking 90→GM, Fletching 90→GM)

- **헤비 석궁(80–120, 판자 10개)**이 ~90 이후의 성장 아이템입니다 — Fletching 95에서 석궁은 87%
  성공(느린 성장)인 반면 헤비는 ~37% 근처에 있습니다. 27 gp에 팔리는데, 석궁보다 *나쁜* 판자당
  gp이니 — 헤비는 스킬용으로, 석궁은 금화용으로 제작하세요.
- Lumberjacking 95는 **yew wood**를, 100은 heartwood/bloodwood/frostwood에 더해 보너스 자원(나무
  껍질 조각, 호박)을 엽니다 — 전부 플레이어 시장이며, 전부 제작자들이 당신을 찾는 이유입니다.
- 도끼 보너스는 당신과 함께 조용히 성숙했습니다: 도끼와 약간의
  [Swordsmanship](/ko/skills/swordsmanship/)을 든 GM 벌목꾼은 정당한 사냥꾼입니다 — 순수 제작에서
  나가는 리스펙 없는 경로 하나.

## 거래 루프

| 행동 | 어디서 | 가격 (소스 확인) |
|---|---|---|
| 활 / 석궁 / 헤비 판매 | NPC 활제작자 | 17 / 25 / 27 gp 고정, +25% 익셉셔널; 무기는 가격 하락 없음 |
| 평범한 판자 대량 판매 | NPC 목수 | 각 2 gp; 진열 가격은 한 벤더가 흡수하는 1,000단위당 ~1 gp씩 하락(`GenericBuy.cs`) — 큰 처분은 Yew → 브리타니아 → Vesper로 돌리세요 |
| 플레이어에게 판자 판매 | 포럼 거래 게시판 | 2–3 gp — NPC의 3 gp 진열 가격 아래라면 이김; 시대의 "플레이어에게 4 gp"는 여기선 과합니다 |
| 유색 판자, 화살, 깃털, 통 판매 | 플레이어만 | NPC는 잡템 비율 지불(화살/깃털 1 gp); 이것들은 관계 상품입니다 |
| 손도끼 구매 | NPC 무기제작자 | ~25 gp; 두 자루 휴대 — 마을에서 숲 하나 떨어진 곳에서 부서진 도끼는 헛걸음입니다 |
| Fletching BOD | 어떤 NPC 활제작자든 | 6시간마다 공짜, 캐시 2; 보상이 NPC 재고를 능가 |

## 결정 지점과 흔한 실수 (에이전트용)

- **가방이 너무 빨리 차면** → 통나무를 나르고 있습니다; 매번 나무에서 판자를 자르세요. 그래도 너무
  빠르면, STR을 올리거나(쪼개는 동안 성장) 짐 말을 사세요.
- **활 성공률 ≥ ~80%이면** → 성장이 느려졌습니다; 위로 올라가세요: 활 → 석궁(~70) → 헤비 석궁(~90),
  [실제 구간](/ko/crafting/bowfletching/)에 따라.
- **스킬보다 트립당 금화가 더 중요하면** → 석궁이 천장입니다(판자당 3.6 gp); Fletching 60 미만에서는
  2 gp 원판자가 나쁜 활 굴림을 이깁니다.
- **벤더가 판자에 1 gp를 주기 시작하면** → ~1,000+를 먹였습니다; 마을을 돌리거나 플레이어 시장으로
  전환하세요. 활은 이 문제가 없습니다.
- **oak를 기대한 나무가 평범한 통나무를 주면** → Lumberjacking이 65 미만; 광맥 굴림은 나무-뱅크
  단위이니, 나중에 다시 오세요([표](/ko/skills/lumberjacking/)).
- **통을 원하면** → 먼저 Carpentry ≥ ~58을 확인하고 *또한* 땜장이에게서 통 테를 마련하세요; 지팡이와
  뚜껑만으로는 조립되지 않습니다.
- **전투 쪽으로 흐르기 시작하면** → 도끼를 유지하세요; 데미지 보너스는 진짜이고 이미 값을 치렀습니다.
  리롤하지 말고 Swordsmanship/Tactics를 추가하세요.
- **AFK 매크로에 의존하지 마세요** — 고전 가이드는 이를 1위 밴 유발 요인으로 부릅니다; 이 샤드의
  [성문 규칙](/ko/shard/server-rules/)은 config 전용이고 이를 다루지 않으니, 용인된다고 가정하기 전에
  포럼에서 물어보세요.

## 관련

- [Lumberjacking 스킬](/ko/skills/lumberjacking/) · [Bow Fletching](/ko/crafting/bowfletching/) ·
  [Carpentry](/ko/crafting/carpentry/) · [자원](/ko/items/resources/) · [Yew](/ko/world/yew/)
- [템플릿: 대장장이(Blacksmith)](/ko/templates/blacksmith/) — 같은 아이디어, 다만 바위로
