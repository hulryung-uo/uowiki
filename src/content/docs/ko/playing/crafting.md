---
title: 플레이 방법 — 제작
description: 보편적인 제작 루프 — 도구에서 메뉴, 범주, 아이템, 만들기까지 — 와 직종별 진입점, 재료, 예외적 품질과 제작자 각인, 실패와 재료 손실, 수리, 룬 도구, 강화, 그리고 대량 주문 증서.
status: unverified
sources:
  - "servuo: Scripts/Services/Craft/Core/CraftGump.cs, CraftItem.cs (craft menu flow, exceptional chance, maker's mark)"
  - "servuo: Scripts/Services/Craft/Core/CraftItem.cs (failed skill check consumes the FULL listed resources for standard recipes — ConsumeType.All)"
  - "servuo: Scripts/Services/Craft/Core/QueryMakersMarkGump.cs, Repair.cs, Enhance.cs, Resmelt.cs (mark/repair/enhance/smelt features)"
  - "servuo: Scripts/Services/Craft/Def*.cs (per-trade craft definitions: Blacksmithy, Tailoring, Tinkering, Carpentry, BowFletching, Inscription, Cooking, Alchemy, Cartography, Masonry, Glassblowing)"
  - "in-game: foundry blacksmith evals 2026-06-12 (run c16f4 cycles 1-4 — 12 consecutive failed weapon crafts each burned the full 10-ingot cost; agent logs data/eval_logs/agent-evoc16f4c1s*/c3s*/c4s*)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-12
generated: false
---

이 가이드는 **제작**이 일반적으로 어떻게 작동하는지 — 모든 직종 스킬이 공유하는 루프 — 를
설명한 뒤, 각 직종에 맞는 도구, 스킬 페이지, 레시피 목록으로 안내합니다. 제작은 원자재(채집하거나
구입한)를 완성품으로 바꿉니다: 무기, 갑옷, 의복, 가구, 도구, 음식, 두루마리, 물약 등. 원자재가
어디서 오는지는 [자원 채집](/ko/playing/gathering-resources/)과
[자원 참조](/ko/items/resources/)를 참고하세요. 정리된 입문 빌드는
[대장장이 템플릿](/ko/templates/blacksmith/)을 참고하세요.

**이 페이지에서 사용하는 정의:**
- **직종 도구(Trade tool)** — 제작을 위해 더블클릭하는 아이템(대장장이 망치, 재봉 키트, 땜장이
  도구 등). 각 직종에는 자체 도구가 있습니다.
- **제작 메뉴 / 제작 gump** — 직종 도구를 사용할 때 열리는 창. **범주**와 각 범주 안의
  **아이템**을 나열합니다.
- **예외적(Exceptional)** — 더 나은 스탯과 아이템에 이름을 새길 옵션을 주는 최고 품질 결과.
- **자원 / 재료(Resource / material)** — 제작 시 소모되는 재료(잉곳, 보드, 가죽, 천, 시약 등).

## 보편적인 제작 루프

모든 직종은 같은 다섯 단계를 따릅니다(`Scripts/Services/Craft/Core/`의 제작 시스템과 대조해
검증됨):

1. **도구와 재료를 갖추세요.** 직종 도구와 필요한 원자재를 **배낭**에 넣으세요. 일부 레시피는
   스테이션 근처에 있어야 합니다(대장기술의 **화로와 모루**, 제빵의 **오븐**, 천의 **직조기**
   등).
2. **직종 도구를 더블클릭하세요.** 이것이 **제작 메뉴**(`CraftGump`)를 엽니다.
3. **범주를 고르세요.** 메뉴는 아이템을 범주로 묶습니다(대장장이의 경우: 무기, 갑옷, 방패…).
   범주를 클릭해 그 아이템을 보세요. 범주 배치는 **시대 의존적**입니다: 이 샤드(Endless Journey
   시대)에서 대장장이 메뉴는 링, 체인, 플레이트를 단일 **금속 갑옷(Metal Armor)** 범주로 합치며,
   시대 제한 아이템이 모든 목록에 나타납니다 — 그래서 아이템의 위치가 고전 시대 참조와 다릅니다.
4. **아이템을 고르세요.** 각 아이템은 **필요한 스킬**과 **소모하는 재료**를 보여 줍니다. 스킬이나
   재료가 부족한 아이템은 표시됩니다.
5. **만드세요.** *Make Now*를 클릭하세요(또는 수량을 설정해 일괄 제작). 캐릭터가 잠시 작업한 뒤,
   **성공**(아이템이 가방에 나타남)하거나 **실패**합니다.

메뉴를 열어 둔 채 반복적으로 제작할 수 있습니다. 각 시도는 해당 스킬을 단련합니다(
[스킬 상승](/ko/mechanics/skill-gain/) 참고).

## 직종별 진입점

각 직종은 다른 스킬, 도구, 메뉴를 사용합니다. 스킬 범위와 전체 레시피 목록은 링크된 페이지에
있습니다 — 이 표는 그저 **진입점**입니다:

| 직종 | 스킬 | 도구 (더블클릭) | 레시피 |
| --- | --- | --- | --- |
| 대장기술 | [대장기술(Blacksmithy)](/ko/skills/blacksmithy/) | 대장장이 망치 (**화로와 모루**에서) | [/ko/crafting/blacksmithy/](/ko/crafting/blacksmithy/) |
| 재봉 | [재봉(Tailoring)](/ko/skills/tailoring/) | 재봉 키트 | [/ko/crafting/tailoring/](/ko/crafting/tailoring/) |
| 땜장이 | [땜장이(Tinkering)](/ko/skills/tinkering/) | 땜장이 도구 | [/ko/crafting/tinkering/](/ko/crafting/tinkering/) |
| 목공 | [목공(Carpentry)](/ko/skills/carpentry/) | 톱 / 더브테일 톱 | [/ko/crafting/carpentry/](/ko/crafting/carpentry/) |
| 활 제작 | [활 제작/궁시(Bowcraft/Fletching)](/ko/skills/bowcraft-fletching/) | 활 제작 도구 | [/ko/crafting/bowfletching/](/ko/crafting/bowfletching/) |
| 필사 | [필사(Inscription)](/ko/skills/inscription/) | 필경사의 펜 | [/ko/crafting/inscription/](/ko/crafting/inscription/) |
| 요리 | [요리(Cooking)](/ko/skills/cooking/) | 프라이팬 / **오븐**에서 | [/ko/crafting/cooking/](/ko/crafting/cooking/) |
| 연금술 | 연금술(Alchemy) | 막자와 막자사발 | [/ko/crafting/alchemy/](/ko/crafting/alchemy/) |
| 지도 제작 | 지도 제작(Cartography) | 지도 제작자의 펜 | [/ko/crafting/cartography/](/ko/crafting/cartography/) |
| 석공 | (스킬 + 도구) | 망치와 끌 | [/ko/crafting/masonry/](/ko/crafting/masonry/) |
| 유리 세공 | (스킬 + 도구) | 취관 (화로/용광로에서) | [/ko/crafting/glassblowing/](/ko/crafting/glassblowing/) |

모든 직종은 [제작 개요](/ko/crafting/)에서 둘러보세요. 도구 자체는
[도구 카탈로그](/ko/items/catalog/tools/)에 있습니다.

## 재료와 구할 곳

레시피는 가방에 있어야 하는 **원자재**를 소모합니다:

- 대장기술용 **잉곳** — 화로에서 캔 광석을 제련. [채광(Mining)](/ko/skills/mining/)과
  [자원 채집](/ko/playing/gathering-resources/)을 참고하세요.
- 목공과 활 제작용 **보드** — 통나무를 보드로 자름.
  [벌목(Lumberjacking)](/ko/skills/lumberjacking/)을 참고하세요.
- 재봉용 **가죽** 과 **천** — 시체에서 가죽을 벗기거나, 천 사슬을 돌립니다.
  [자원 채집](/ko/playing/gathering-resources/)을 참고하세요.
- 필사/연금술용 **시약** — NPC 메이지/연금술사에게서 구입하거나 채집. [시약](/ko/items/reagents/)을
  참고하세요.
- 요리용 **음식 재료** — 밀가루, 날생선/고기 등.

정확한 스킬 게이트와 **유색 광석 / 가죽 / 목재 등급**(더 높은 스킬을 요구하고 더 나은 아이템을
산출)은 [자원 참조](/ko/items/resources/)에 나열되어 있습니다 — 수치를 외우기보다 거기로
링크하세요.

## 성공, 예외적 품질, 그리고 제작자 각인

제작하면, 결과는 세 가지 중 하나입니다:

- **실패** — 시도에 실패합니다(아래 [실패와 재료 손실](#실패와-재료-손실) 참고).
- **일반 성공** — 표준 품질 아이템.
- **예외적 성공** — 보너스 내구도/스탯과 **각인** 옵션이 있는 최고 품질. 예외적 확률은 레시피
  요구치 위의 스킬에 따라 오릅니다(`CraftItem.cs`의 `GetExceptionalChance`로 계산됨; 일부
  레시피는 절대 예외적일 수 없고, 특정 아이템/탈리스만은 보너스를 더함).

**제작자 각인(Maker's mark):** 아이템을 예외적으로 제작하면, (`QueryMakersMarkGump`를 통해)
**캐릭터 이름을 새길지**("Crafted by &lt;name&gt;") 묻습니다. 각인된 예외적 상품은 귀하게
여겨지고 더 잘 팔립니다. 보통 한 번 선호도를 설정하면 메뉴가 그것을 기억합니다.

따라서 높은 스킬은 두 가지로 중요합니다: 더 어려운 아이템을 아예 제작하게 해 주고, 그 아이템들이
예외적으로 나오는 비율을 높입니다.

## 실패와 재료 손실

제작은 실패할 수 있고, **실패는 재료를 파괴합니다**(대장기술에 대해 필드 검증됨):

- 표준 레시피의 경우 실패한 스킬 검사는 그 아이템의 **나열된 전체 자원**을 소모하며, 일부가
  아닙니다(`CraftItem.cs`는 일반 레시피에 대해 `ConsumeType.All`로 소모를 굴림). 라이브
  테스트에서, 12회 연속 실패한 무기 시도는 각각 완전한 10잉곳 비용을 태웠습니다 — 0개 아이템에
  120잉곳.
- 당신의 **성공 확률은 레시피 최소 스킬 위로 50포인트 창에 걸쳐 선형으로 비례**합니다(예: 최소
  스킬에서는 거의 항상 실패하고; 최소 + 50에서는 절대 실패하지 않음). 스킬이 오르면 실패율이
  떨어집니다 — 희귀 재료를 걸기 전에 저렴한 아이템으로 단련하세요.
- **스킬로 단련할 수 있는 가장 저렴한 레시피를 고르세요.** 대장장이의 경우 **단검(Dagger)**(3잉곳,
  스킬 0부터 제작 가능)이 단연 가장 저렴한 단련용입니다; 10잉곳 레시피를 너무 일찍 시도하면 굴림당
  세 배가 넘는 금속을 낭비합니다.

## 아이템 수리

닳은 무기, 갑옷, 도구는 **내구도**를 잃고 결국 부서집니다. 맞는 직종 스킬로 그것들을
**수리**할 수 있습니다(`Repair.cs`에 따름):

1. 관련 **직종 도구**를 더블클릭하세요(예: 금속 갑옷/무기에는 대장장이 망치, 가죽/천에는 재봉
   키트, 나무 아이템에는 톱).
2. 제작 메뉴에서 **Repair**를 고르세요(또는 **수리 증서** 사용).
3. 손상된 아이템을 대상으로 지정하세요.

성공은 내구도를 회복하고; 실패한 수리는 **아이템의 최대 내구도를 낮출 수** 있으니, 높은 스킬로
수리하세요. 각 직종은 만들 수 있는 아이템 유형을 수리합니다 — 대장기술은 금속을, 재봉은 가죽/천을,
목공/활 제작은 나무를 수리하는 식입니다.

## 룬 도구와 강화 (간략)

두 가지 고급 기능은 최고급 제작자가 마법 장비를 만들게 해 줍니다(메커니즘은 확장팩 의존적 —
구체적 사항은 unverified로 보세요):

- **룬 도구(Runic tools)** — 특수하고 사용 횟수가 제한된 직종 도구(룬 망치, 재봉 키트 등, 종종
  [대량 주문 보상](#대량-주문-증서-bod)에서 나옴)로, **무작위 마법 속성**을 가진 아이템을
  제작합니다. 룬 도구를 든 채 평소처럼 제작합니다.
- **강화(Enhancing)** — 완성된 아이템을 가져와 **더 나은 자원으로 다시 단조**(`Enhance.cs`에
  따름)하여 그 자원의 보너스를 더합니다. 강화는 **실패 시 아이템을 파괴**할 수 있으니, 위험합니다.

각 직종이 어떤 룬 도구와 강화 옵션을 지원하는지는 개별 [/ko/crafting/](/ko/crafting/) 직종
페이지를 참고하세요.

## 재제련 (금속 회수)

대장장이는 제작하거나 약탈한 금속 아이템을 화로에서 그 잉곳의 일부로 **재제련**할 수
있습니다(`Resmelt.cs`에 따름) — 실패하거나 원치 않는 금속 상품을 재활용하는 데 유용합니다.
대장장이 메뉴의 재제련 옵션을 사용해 화로 근처에서 아이템을 대상으로 지정하세요.

## 대량 주문 증서(BOD)

**대량 주문 증서(Bulk Order Deeds)**는 제작 보상 루프입니다. 한 직종의 NPC 상점 주인(예:
대장장이나 직조공)이 주기적으로 **BOD**를 제공합니다: 특정 아이템의 수량(선택적으로 예외적이고,
특정 재료로)을 요청하는 증서입니다.

BOD를 사용하려면:
1. 관련 NPC에게서 증서를 받으세요(대량 주문을 요청하거나 / 컨텍스트 메뉴 사용).
2. **요청된 아이템을 제작**하고 각각을 증서 위로 떨궈 채우세요.
3. **완성된 증서를 NPC에게 제출**해 **보상**을 받으세요 — 금화, 희귀 재료, 룬 도구, 레시피,
   그리고 여러 소형을 결합해 더 큰 상을 주는 **대형 BOD**.

BOD는 룬 도구와 그 밖의 제작자 전용 보상으로 가는 주 경로입니다. 보상 표는 직종과 샤드 설정에
따라 다릅니다 — 그 직종의 [/ko/crafting/](/ko/crafting/) 페이지를 확인하세요.

## 함께 보기

- [제작 개요](/ko/crafting/)와 [대장기술 제작](/ko/crafting/blacksmithy/)
- [대장장이 템플릿](/ko/templates/blacksmith/) — 완전한 제작 빌드
- [자원 채집](/ko/playing/gathering-resources/) — 재료가 어디서 오는지
- [자원 참조](/ko/items/resources/) · [도구 카탈로그](/ko/items/catalog/tools/) ·
  [자원 카탈로그](/ko/items/catalog/resources/)
- 스킬 페이지: [대장기술](/ko/skills/blacksmithy/) · [재봉](/ko/skills/tailoring/) ·
  [땜장이](/ko/skills/tinkering/) · [목공](/ko/skills/carpentry/) ·
  [활 제작/궁시](/ko/skills/bowcraft-fletching/) · [필사](/ko/skills/inscription/) ·
  [요리](/ko/skills/cooking/)
- [스킬 상승](/ko/mechanics/skill-gain/) · [색조/색상 참조](/ko/reference/hues/)
