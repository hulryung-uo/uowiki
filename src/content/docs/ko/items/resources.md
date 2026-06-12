---
title: 자원
description: 채집 산출량과 스킬 요구치 — 광석과 주괴, 통나무와 판자, 가죽, 그리고 천.
status: source-verified
sources:
  - "servuo: Scripts/Services/Harvest/Mining.cs"
  - "servuo: Scripts/Services/Harvest/Lumberjacking.cs"
  - "servuo: Scripts/Items/Resource/Log.cs"
  - "servuo: Scripts/Misc/ResourceInfo.cs"
last_verified: 2026-06-11
generated: false
---

모든 제국은 누군가가 돌을 나르는 데서 시작합니다. 이것들이 브리타니아 경제의 원자재이며,
스킬 수치는 서버 소스의 채집 정의에서 가져왔습니다.

## 광석과 주괴 ([채광(Mining)](/ko/skills/mining/))

산과 동굴에서 광석을 캐고, 대장간에서 같은 금속의 주괴로 제련합니다. 스킬 요구치와 광맥 희귀도는
`Scripts/Services/Harvest/Mining.cs`에서, 광석→주괴 종류 매핑은
`Scripts/Misc/ResourceInfo.cs`에서 가져왔습니다.

| | Ore → Ingot | 채광 요구치 | 광맥 확률 | 가공에 필요한 대장 스킬 |
|---|-------------|-----------------|-------------|---------------------|
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Iron | 0 | 49.6% | 0 |
| <img src="/img/items/0x1BF2-h0973.png" class="uo-sprite" alt="" width="56" /> | Dull Copper | 65.0 | 11.2% | 65.0 |
| <img src="/img/items/0x1BF2-h0966.png" class="uo-sprite" alt="" width="56" /> | Shadow Iron | 70.0 | 9.8% | 70.0 |
| <img src="/img/items/0x1BF2-h096D.png" class="uo-sprite" alt="" width="56" /> | Copper | 75.0 | 8.4% | 75.0 |
| <img src="/img/items/0x1BF2-h0972.png" class="uo-sprite" alt="" width="56" /> | Bronze | 80.0 | 7.0% | 80.0 |
| <img src="/img/items/0x1BF2-h08A5.png" class="uo-sprite" alt="" width="56" /> | Gold | 85.0 | 5.6% | 85.0 |
| <img src="/img/items/0x1BF2-h0979.png" class="uo-sprite" alt="" width="56" /> | Agapite | 90.0 | 4.2% | 90.0 |
| <img src="/img/items/0x1BF2-h089F.png" class="uo-sprite" alt="" width="56" /> | Verite | 95.0 | 2.8% | 95.0 |
| <img src="/img/items/0x1BF2-h08AB.png" class="uo-sprite" alt="" width="56" /> | Valorite | 99.0 | 1.4% | 99.0 |

채광으로는 그 외에도 짝이 맞는 **화강암(granite)**(석공용), 70+ 스킬에서 **모래(sand)**(유리 세공용),
그리고 100.0에서 희귀 보석과 blackrock을 보너스로 얻을 수 있습니다.

## 통나무와 판자 ([벌목(Lumberjacking)](/ko/skills/lumberjacking/))

나무를 베어 통나무를 얻고(타격당 10개), 도끼로 통나무를 판자로 자릅니다. 벌목 요구치는
`Lumberjacking.cs`에서 가져왔으며, 판자 절단은 표에 적힌 스킬에서 **목공(Carpentry) 또는 벌목**을
인정합니다(`Log.cs`).

| Log | Board | 벌목 요구치 | 광맥 확률 | 판자 절단에 필요한 스킬 |
|---|---|---|---|---|
| <img src="/img/items/0x1BD7.png" class="uo-sprite" alt="" width="56" /> | Ordinary | 0 | 49% | 0 |
| <img src="/img/items/0x1BD7-h07DA.png" class="uo-sprite" alt="" width="56" /> | Oak | 65.0 | 30% | 65 |
| <img src="/img/items/0x1BD7-h04A7.png" class="uo-sprite" alt="" width="56" /> | Ash | 80.0 | 10% | 80 |
| <img src="/img/items/0x1BD7-h04A8.png" class="uo-sprite" alt="" width="56" /> | Yew | 95.0 | 5% | 95 |
| <img src="/img/items/0x1BD7-h04A9.png" class="uo-sprite" alt="" width="56" /> | Heartwood | 100.0 | 3% | 100 |
| <img src="/img/items/0x1BD7-h04AA.png" class="uo-sprite" alt="" width="56" /> | Bloodwood | 100.0 | 2% | 100 |
| <img src="/img/items/0x1BD7-h047F.png" class="uo-sprite" alt="" width="56" /> | Frostwood | 100.0 | 1% | 100 |

100.0에서의 보너스 채집: bark fragments, luminescent fungi, switches, parasitic plants,
brilliant amber.

## 가죽

날이 있는 도구로 동물 사체의 가죽을 벗겨 **생가죽(hides)**을 얻고, 가위로 잘라 **가죽(leather)**으로
만듭니다. `ResourceInfo.cs`(`m_AOSLeatherInfo`) 기준으로 네 종류가 있습니다.

| | Leather | 출처 |
|---|---------|-----------|
| <img src="/img/items/0x1081.png" class="uo-sprite" alt="" width="56" /> | Normal | 흔한 동물(소, 사슴 등) |
| <img src="/img/items/0x1081-h0283.png" class="uo-sprite" alt="" width="56" /> | Spined | 더 강한 짐승 |
| <img src="/img/items/0x1081-h0227.png" class="uo-sprite" alt="" width="56" /> | Horned | 위험한 몬스터 |
| <img src="/img/items/0x1081-h01C1.png" class="uo-sprite" alt="" width="56" /> | Barbed | 최상위 포식자(드래곤과 그 일족) |

어떤 생물이 어떤 가죽을 주는지는 도감의 영역입니다 —
[도감(Bestiary)](/ko/bestiary/)을 참고하세요. 각 가죽 등급은 고유한 제작 속성 묶음
(`CraftAttributeInfo`)을 갖습니다.

## 천 — 양과 밭에서 옷감 한 필까지

천은 스킬로 채집하는 것이 아니라, 물레와 베틀을 거쳐 원섬유에서 *제조*됩니다. 그 과정은
다음과 같습니다(`Scripts/Items/Resource/Cotton.cs`, `Wool.cs`, `Flax.cs`,
`YarnsAndThreads.cs`, `BoltOfCloth.cs` 기준).

| 단계 | 도구 | 산출물 |
|---|---|---|
| 원섬유 — <img src="/img/items/0x0DF9.png" class="uo-sprite" alt="" width="56" /> **cotton**(목화 식물에서 채집), <img src="/img/items/0x0DF8.png" class="uo-sprite" alt="" width="56" /> **wool**(양털 깎기), 또는 <img src="/img/items/0x1A9C.png" class="uo-sprite" alt="" width="56" /> **flax**(아마 식물 수확) | — | 섬유 그 자체 |
| 섬유를 **잣기** | 물레(Spinning wheel) | <img src="/img/items/0x0FA0.png" class="uo-sprite" alt="" width="56" /> **실타래/방적사**(사용당 6개) |
| 실을 **짜기** | 베틀(Loom) | <img src="/img/items/0x0F95.png" class="uo-sprite" alt="" width="56" /> **옷감 한 필(bolt of cloth)** |
| 옷감을 **자르기** | 가위(Scissors) | <img src="/img/items/0x1766.png" class="uo-sprite" alt="" width="56" /> **천(cloth)**(한 필당 50개) |
| 천을 **자르기** | 가위(Scissors) | <img src="/img/items/0x0E21.png" class="uo-sprite" alt="" width="56" /> **붕대(bandages)** — [치유(Healing)](/ko/skills/healing/)의 연료 |

물레와 베틀은 재단사 상점과 여러 가정집에 놓여 있습니다(둘 다 제작 가능한 하우스 애드온입니다).
잣기나 짜기에는 스킬 체크가 걸리지 않습니다 — 누구나 섬유를 천까지 가공할 수 있고, 스킬은 나중에,
재단사가 천을 의류와 방어구로 만들 때 필요해집니다.

또는 재단사와 잡화상 상인에게서 옷감 한 필, 양털, 목화를 **그냥 사서** 곧장 가위 단계로 건너뛸
수도 있습니다. 천은 어떤 염료든 받으므로, 색이 들어간 의류는 별도의 재료가 아니라 염색통 작업으로
처리합니다 — [색조 참조(Hue Reference)](/ko/reference/hues/)를 보세요.

재봉(Tailoring)은 천을 의류와 가벼운 방어구로 만듭니다 — [재봉(Tailoring)](/ko/crafting/tailoring/)과
[의류 카탈로그](/ko/items/catalog/clothing/)를 참고하세요.

## 관련 문서

- [아이템 개요](/ko/items/) · [대장기술(Blacksmithy)](/ko/skills/blacksmithy/) · [제작(Crafting)](/ko/crafting/)
- [인터랙티브 지도](https://uomap.vercel.app) — 상인과 지형 찾기
