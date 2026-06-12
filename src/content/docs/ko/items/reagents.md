---
title: 시약
description: 여덟 가지 마법술 시약을 구매자 관점에서 정리 — 각 시약이 무엇을 시전하게 하는지, 어느 서클에서 가장 많이 소모되는지, 어디서 살 수 있는지.
status: source-verified
sources:
  - "servuo: Scripts/Spells/First..Eighth (reagent usage counts, surveyed 2026-06-11)"
  - "anima: data/world_knowledge.yaml (mage_shop city features)"
last_verified: 2026-06-11
generated: false
---

메이지의 힘은 잡초와 재, 거미 부속물이 담긴 어깨 가방에서 나옵니다. 이 글은 그 쇼핑 가이드이며,
주문별 시약 레시피는 [마법 섹션](/ko/magic/)에 있습니다.

## 여덟 가지 시약

사용 횟수는 64개 마법술 주문 중 각 시약을 소모하는 주문의 수로, 주문 소스
(`Scripts/Spells/First`부터 `Eighth`까지)를 조사해 집계했습니다.

| | Reagent | 사용하는 주문 수 | 가장 많이 쓰는 서클 | 대표 주문 |
|---|---------|-----------------|------------------|------------------|
| <img src="/img/items/0x0F86.png" class="uo-sprite" alt="" width="56" /> | Mandrake Root | 35 | 4th, 7th, 8th | Recall, Greater Heal, Gate Travel |
| <img src="/img/items/0x0F7B.png" class="uo-sprite" alt="" width="56" /> | Bloodmoss | 27 | 3rd, 8th | Recall, Teleport, 8서클 소환 주문들 |
| <img src="/img/items/0x0F8C.png" class="uo-sprite" alt="" width="56" /> | Sulfurous Ash | 25 | 7th, 4th | Flamestrike, Gate Travel, Fireball 계열 |
| <img src="/img/items/0x0F8D.png" class="uo-sprite" alt="" width="56" /> | Spider's Silk | 22 | 7th, 8th | Heal, Greater Heal, Flamestrike, 소환 주문 |
| <img src="/img/items/0x0F84.png" class="uo-sprite" alt="" width="56" /> | Garlic | 20 | 4th, 1st–3rd | Heal, Greater Heal, Cure, 보호 계열 |
| <img src="/img/items/0x0F7A.png" class="uo-sprite" alt="" width="56" /> | Black Pearl | 17 | 7th, 5th | Recall, Energy Bolt, Gate Travel |
| <img src="/img/items/0x0F88.png" class="uo-sprite" alt="" width="56" /> | Nightshade | 16 | 5th, 2nd | Energy Bolt, 저주/독 계열 |
| <img src="/img/items/0x0F85.png" class="uo-sprite" alt="" width="56" /> | Ginseng | 11 | 1st, 4th | Heal, Greater Heal, Cure |

표에서 도출되는 구매 요령:

- **Mandrake, bloodmoss, black pearl** — 이동 마법(Recall/Gate)이 이것들을 끊임없이 소모하므로
  모든 메이지가 잔뜩 비축합니다.
- **Garlic, ginseng, spider's silk** — 치유 세트. 서포트 메이지가 가장 먼저 바닥내는 시약입니다.
- **Sulfurous ash, spider's silk, black pearl, nightshade** — 전투 세트
  (Flamestrike와 Energy Bolt가 주력 피해 주문입니다).

## 구매처

메이지 상점은 여덟 가지를 모두 취급합니다. `world_knowledge.yaml` 기준으로 메이지 상점이 있는 도시:

- **[Moonglow](/ko/world/moonglow/)** — 메이지의 도시; 섬 자체에 시약 밭이 있음
- **[Britain](/ko/world/britain/)** — 중심부 근처에 여러 메이지 상인
- **Nujel'm** — 궁전 도시의 메이지 상점
- **Papua** — Lost Lands에서 시약을 살 수 있는 거점
- **Wind** — 메이지 전용 숨겨진 도시 (들어갈 수 있다면 이미 시전이 가능하다는 뜻)

정확한 상인 위치는 [인터랙티브 지도](https://uomap.vercel.app)에서 확인하세요(NPC Vendors를 켜고
"Mage"로 검색). 상인 재고는 60분마다 갱신되고 가격은 대량 구매에 반응하므로
(`Config/Vendors.cfg` — [서버 규칙](/ko/shard/server-rules/) 참고), 한 상인을 두드리기보다
두세 도시를 도는 시약 순회가 더 효율적입니다.

## 참고

- 강령술(Necromancy)은 별도의 시약 세트(박쥐 날개, 무덤 먼지 등)를 사용합니다 —
  [마법](/ko/magic/) 섹션에 정리되어 있습니다.
- 주문별 시약 비용은 서클이 올라갈수록 증가합니다. 8서클 소환은 한 번 시전에 네 종류의 시약을
  소모할 수 있습니다. 수십 개가 아니라 수백 개 단위로 비축하세요.

## 관련 문서

- [마법술(Magery)](/ko/skills/magery/) — 서클, 시전 확률, 마나
- [마법(Magic)](/ko/magic/) — 주문별 시약 레시피
