---
title: 식물 & 정원 가꾸기
description: ServUO 식물 시스템 작동 방식 — 흙 그릇에 씨앗을 심어 장식용·실용 식물을 기르고, 성장 단계(씨앗, 묘목, 식물, 완전 성장, 장식용)에 걸쳐 매일 물을 주며, 해충·곰팡이·독·질병으로부터 건강하게 유지하고, 교배 수분으로 희귀한 색을 내고, 씨앗·꺾꽂이·자원·식물 색소를 수확하기.
status: source-verified
sources:
  - "servuo: Scripts/Services/Plants/PlantItem.cs (PlantStatus growth stages, watering, planting, decorative)"
  - "servuo: Scripts/Services/Plants/PlantSystem.cs (growth check, water, maladies, potions, fertile dirt, pollination)"
  - "servuo: Scripts/Services/Plants/PlantType.cs (44 plant types, categories, crossable/reproduces)"
  - "servuo: Scripts/Services/Plants/PlantHue.cs (19 plant hues, bright/rare, cross-breeding rules)"
  - "servuo: Scripts/Services/Plants/PlantResources.cs (plant resource yields)"
  - "servuo: Scripts/Services/Plants/MainPlantGump.cs (gardening UI gump)"
  - "servuo: Scripts/Services/BasketWeaving/PlantPigment.cs (plant pigments)"
  - "servuo: Scripts/Mobiles/NPCs/Naturalist.cs (Study of Solen seed reward)"
  - "client art: artLegacyMUL.uop (plant item sprites)"
last_verified: 2026-06-11
generated: false
---

**정원 가꾸기(Gardening)**는 Ultima Online 안의 독립적인 미니게임입니다: 흙 그릇에 씨앗을
심고, 하루에 한 번 물을 주면, 약 일주일에 걸쳐 장식으로 둘 수도 있고 유용한 재료를 수확할
수도 있는 식물로 자랍니다. 스킬 포인트나 전투가 필요 없고 — 인내심과 관심만 있으면 됩니다.
사람들은 **희귀한 색의 변종**을 ([주택 장식(decorating)](/ko/playing/decorating/)과 되팔이로
귀하게 여겨집니다) 얻기 위해, 제작에 쓰이는 **식물 자원**을 위해, 아이템을 염색하는 **식물
색소(plant pigments)**를 위해, 그리고 단순히 느긋한 수집 게임으로서 식물을 기릅니다: 44가지
식물 종류와 19가지 색이 있으며, 그중 다수는 세심한 **교배 수분(cross-pollination)**으로만
얻을 수 있습니다.

아래의 모든 수치와 동작은 ServUO 서버 에뮬레이터의 식물 스크립트(`Scripts/Services/Plants/`
아래, 섹션별로 인용)에서 나옵니다. 구조화된 데이터는 `tools/extract_plants.py`로 추출되어
`data/plants.json`에 들어 있습니다.

## 식물을 기르는 방법

성장 루프는 다음과 같습니다:

1. **씨앗을 구하세요.** 씨앗은 이미 소유한 완전 성장 식물에서
   (see [식물이 주는 것](#what-plants-give-you)), 몬스터/보물 드롭에서, 그리고 **Naturalist
   (박물학자)**의 퀘스트 보상(아래 참고)으로 나옵니다. 씨앗은 식물의 **종류(type)**와
   **색(hue)**을 기록합니다.
2. **흙 그릇을 준비하세요.** 새 식물 그릇은 `BowlOfDirt` 단계에서 시작합니다
   (`Scripts/Services/Plants/PlantItem.cs`). 흙이 부드러워질 때까지 **물(water)**을 부으세요 —
   씨앗이 자리 잡으려면 흙이 최소한 살짝 적셔져 있어야 합니다(`Water >= 2`). 그렇지 않으면
   *"The dirt needs to be softened first."* 가 뜹니다.
3. 준비된 토양에 **씨앗을 심으세요.** 그릇은 `Seed` 단계로 넘어가고, 이제 당신이 고른 종류와
   색을 가집니다.
4. **매일 물을 주세요.** **물(water)**이 든 음료를 부으세요. 물 수치는 **0–4** 범위이고
   식물은 정확히 **2**에 있기를 원합니다(`PlantSystem.cs`). 매일의 성장 검사마다 토양이 1씩
   마르므로, 하루에 한 번 물을 끼얹으면 건강이 유지됩니다. 물이 너무 많거나 *또는* 너무
   적어도 식물이 손상됩니다.
5. **자라게 하세요.** 하루에 한 번(성장 검사는 **23시간** 타이머로 실행됩니다.
   `PlantSystem.CheckDelay`. 로그인하거나 월드가 저장될 때도 다시 검사됩니다), 건강한 식물은
   한 단계 나아갑니다.

성장 검사가 카운트되려면 식물이 당신의 **배낭, 은행 상자, 또는 집에 잠금 고정(locked down)**
되어 있어야 합니다(`PlantItem.cs`의 `ValidGrowthLocation`). 식물을 **더블클릭**하여
상호작용하면 정원 gump가 열립니다.

### 성장 단계

식물은 이 단계들을 거쳐 올라갑니다(`enum PlantStatus`, `PlantItem.cs`). 내부적으로 성장
검사는 단계 1–9를 셉니다; 클라이언트가 표시하는 라벨 상태는 다음과 같습니다:

| 단계 | `PlantStatus` | 생김새 |
|------:|---------------|--------------------|
| 0 | `BowlOfDirt` | 빈 그릇. 물로 부드럽게 한 뒤 씨앗을 심으세요. |
| 1 | `Seed` | 씨앗이 흙에 있음; 곧 싹틉니다. |
| 2–3 | `Sapling` | 어린 묘목, 아직 매일 자라는 중. |
| 4–6 | `Plant` | 알아볼 수 있는 식물; 그릇이 초록으로 변합니다. |
| 7–9 | `FullGrownPlant` | 완전히 자람 — 종류와 색을 보이고, 수분이 가능하며, 씨앗/자원을 산출합니다. |
| 10 | `DecorativePlant` | "장식용으로 설정됨": 완성된 화분 식물. 더 이상 물 줄 필요 없음. |
| 11 | `DeadTwigs` | 방치되어 죽음 — 잔가지만 남음. |

식물이 **완전 성장**에 도달하면 씨앗/자원을 생산하도록 두거나, **장식용으로 설정(set it to
decorative)**할 수 있습니다(`SetToDecorativeGump.cs`) — 더 이상 돌봄이 필요 없고 집에
배치할 수 있는 영구 장식물로 바꾸는 일방향 단계입니다.

### 정원 gump

자라는 식물을 더블클릭하면 메인 정원 인터페이스가 열립니다(`MainPlantGump.cs`). 중앙에 식물의
아트가 보이고, 컨트롤 패널이 있습니다: **번식(reproduction)** 메뉴, 현재 수치가 표시된 네 가지
**병해(maladies)**(해충, 곰팡이, 독, 질병), **물(water)** 수치, 네 개의 **물약(potion)**
슬롯(독/치료/회복/힘), 성장 단계 표시기, 도움말 버튼, 그리고 "그릇 비우기" 버튼. 이 패널은 하나의
맞춤 그림이 아니라 범용 다크 프레임(gump `0xE10`)에 아이템 아트 타일을 더해 구성됩니다.

아래의 식물 스프라이트는 `data/plants.json`의 아이템 ID에 대해 클라이언트 아트에서 직접
렌더링한 것입니다:

![A montage of example plant types: campion flowers, poppies, lilies, fern, ponytail palm, century plant, barrel and tribarrel cactus, bonsai, cocoa tree and sugar canes](/img/plants/montage.png)

## 건강하게 유지하기

식물에는 **hits(체력 풀)**과 **Dying / Wilted / Healthy / Vibrant**의 `Health` 등급이
있습니다. 식물은 적어도 **Healthy** 이상일 때만 *자랍니다*(`PlantSystem.Grow`). 따라서 잘
유지하는 것이 일의 전부입니다. 건강은 네 가지 **병해(maladies)**와 잘못된 물 주기에 의해
위협받습니다(모두 `Scripts/Services/Plants/PlantSystem.cs`에 있음):

| 위험 요소 | 원인 | 치료법 |
|--------|----------------|------------------|
| **해충(Infestation)** | 매일 무작위(**꽃이 핀** 식물과 **밝은** 색조 식물에서, 그리고 과습 시 더 잘 발생). | 식물에 **greater poison potion(강한 독 물약)**을 부으세요. |
| **곰팡이(Fungus)** | 매일 무작위(과습 시 더 잘 발생). | **greater cure potion(강한 치료 물약)**을 부으세요. |
| **독(Poison)** | 독 물약을 과다 적용하여 발생(넘쳐 남음). | **greater heal potion(강한 회복 물약)**을 부으세요. |
| **질병(Disease)** | 치료 물약을 과다 적용하여 발생(넘쳐 남음). | **greater heal potion(강한 회복 물약)**을 부으세요. |

각 병해는 **0–2** 범위입니다. 오직 **greater(강한)** 물약만 효과가 있습니다 — 약한/일반 물약은
*"This potion is not powerful enough"* 을 띄웁니다(`PlantItem.ApplyPotion`). 물약은 그릇에
**2** 충전까지 쌓이며 다음 성장 검사에서 소모되는데, 이때 남은 체력을 회복하기 전에 먼저 해당
병해를 상쇄합니다.

**물 주기는 병해만큼 중요합니다.** 물은 **0–4**에 머무르며 식물은 **2**를 원합니다. 각 성장
검사마다 2에서 벗어난 물의 매 1점이 `3–6` 피해를 주며, 활성화된 각 병해의 매 단계도 마찬가지로
피해를 줍니다(`ApplyMaladiesEffects`). hits를 0까지 떨어뜨리면 식물은 **죽습니다**: 완전 성장
식물은 **dead twigs(잔가지)**로 무너지고, 덜 자란 식물은 빈 흙 그릇으로 되돌아갑니다
(`PlantItem.Die`).

**이로운 돌봄.** 식물에 **병해가 없고** 물이 적절하면, 천천히 회복합니다(검사당 `+2` hits,
또는 **greater heal potion** 충전당 `+7`). **greater strength potion(강한 힘 물약)**은 다음
검사의 해충/곰팡이 확률을 충전당 `0.075` 낮춥니다. 그리고 **fertile dirt(비옥한 흙)**(*bag of
bones* / 비옥한 흙 그릇)에 심으면 **10% 확률로 이중 성장(double-grow)** — 한 단계를 건너뜀 —
을 단계 5까지 얻습니다(`Grow`).

> **방치는 한 가지 면에서는 너그럽습니다:** 성장 검사는 대략 하루에 한 번과 로그인/월드 저장
> 시에만 발동하므로, 식물은 진행 없이 가만히 있을 수 있습니다. 하지만 물이 나쁘거나 병해가
> 방치된 상태에서 검사가 도는 순간 피해를 입습니다 — 그래서 아픈 식물을 두고 오래 자리를
> 비우면 치명적입니다.

## 식물 종류 & 색

**기를 수 있는 식물 종류 44가지**와 **식물 색조 19가지**가 있습니다(`PlantType.cs`,
`PlantHue.cs`). 종류는 카테고리로 나뉩니다:

- **Default(기본, 17종)** — 일상적인 정원 식물: campion flowers, poppies, snowdrops,
  bulrushes, lilies, pampas grass, rushes, elephant-ear plant, fern, ponytail palm, small
  palm, century plant, water plant, snake plant, prickly-pear / barrel / tribarrel cactus.
  이들만이 **교배(cross-bred)**할 수 있고 **번식(reproduce)**(씨앗 생성)할 수 있습니다.
- **Bonsai(분재, 8종)** — common, uncommon, rare, exceptional, exotic **분재 나무**(하위
  등급에는 초록과 분홍 변종). 이들은 특수 드롭이며, 교배도 번식도 하지 않습니다.
- **Peculiar(특이, 18종)** — 장식 전용 기이한 것들: cactus, flax flowers, foxglove, hops,
  orfluer flowers, twisted/straight cypress, short/tall hedge, juniper bush, snowdrop &
  poppy patches, cattails, spider tree, water lily, sugar canes(대나무 아트), 그리고 vanilla.
- **Fragrant(향기, 1종)** — **cocoa tree(코코아 나무)**(옛 아트에서는 *o'hii tree*), 코코아의
  공급원.

### 색조와 교배 수분

씨앗은 **색조(hue)**를 지닙니다. 자연의 시작 색은 **Plain, Red, Blue, Yellow**입니다
(`RandomFirstGeneration` 집합). 이들로부터 세 가지 파생 색이 원색을 섞어 나옵니다 —
**Purple**(red+blue), **Green**(blue+yellow), **Orange**(red+yellow) — 그리고 각 색에는
**Bright(밝은)** 변종이 있습니다. 또한 일반적 혼합으로는 나오지 않는 다섯 가지 **희귀(rare)**
색조가 있습니다: **Black, White, Pink, Magenta, Aqua, Fire Red**(`PlantHue.cs`).

색은 **교배 수분(cross-pollination)**으로 만들어집니다(`PlantHue.Cross`, `PlantType.Cross`):

1. 완전 성장한 **교배 가능(crossable)** 식물은 **꽃가루 생성(PollenProducing)** 상태가 됩니다.
2. gump의 번식/수분 타겟(`PollinateTarget.cs`, `ReproductionGump.cs`)을 사용해 한 식물을 다른
   식물로 수분시킵니다. 그러면 그 씨앗은 자신의 것이 아니라 **교배된(crossed)** 종류와 색을
   지니게 됩니다.
3. 색조 교배 규칙: **같은 색 → 그 색을 Bright로**; **두 원색 → 그 혼합**(red+blue = purple
   등); 원색을 비원색과 교배하면 원색을 유지; 그 외에는 공유 성분. 모든 교배에는 또한 **1%
   확률로 Black 또는 White가 나옵니다** — "우연한" 희귀 식물이 나타나는 고전적 방식입니다.
4. 종류 교배는 표에서 두 종류의 **평균** 쪽으로 밀어붙이므로, 여러 세대에 걸쳐 씨앗을 목표
   식물 쪽으로 끌고 갈 수 있습니다.

**교배 가능(crossable)**한 색조/종류만 교배될 수 있고, **번식하는(reproducing)** 것만 애초에
씨앗을 만듭니다(`IsCrossable`, `Reproduces`). 희귀 색조(Black, White, Pink, Magenta, Aqua,
Fire Red)와 Peculiar/Bonsai 종류는 교배가 **불가능**합니다 — 길러내는 것이 아니라 수집하는
것입니다.

모든 종류와 색조의 기계 판독 가능한 전체 목록(아이템 ID, 카테고리,
crossable/reproduces/bright 플래그 포함)은 `data/plants.json`에 있습니다.

## 식물이 주는 것

완전 성장한 식물은 재생 가능한 작은 공장입니다. 완전한 크기에서 각 성장 검사마다 다음을 생산할
수 있습니다(`PlantSystem.Grow`):

- **씨앗(Seeds)** — 수분되고 번식하는 식물은 교배된 종류/색을 지닌 씨앗을 산출합니다(일생에 걸쳐
  최대 8개). 이것이 색을 번식시키고 거래하는 방식입니다. 낱개 씨앗과 **씨앗 상자(seed box)**
  (`Scripts/Items/Functional/SeedBox/`)로 수집품을 보관하고 정리할 수 있습니다.
- **식물 꺾꽂이 / 자원(Plant clippings / resources)** — 특정 **종류 + 색조** 조합은 제작
  재료를 드롭합니다(일생에 걸쳐 최대 8개). `PlantResources.cs`에서:

  | 자원 | 식물 + 필요한 색조 |
  |----------|----------------------|
  | Red leaves | Elephant-ear plant, ponytail palm, 또는 century plant — **Bright Red** |
  | Orange petals | Poppies, bulrushes, 또는 pampas grass — **Bright Orange** |
  | Green thorns | Snake plant 또는 barrel cactus — **Bright Green** |
  | Cocoa pulp | Cocoa tree — **Plain** |
  | Sack of sugar | Sugar canes — **Plain** |
  | Flax | Flax flowers — **Plain** |
  | Bark fragment | Straight 또는 twisted cypress — **Plain** |
  | Vanilla | Vanilla — **Plain** |
  | Poppies dust | Poppy patch — **Plain** |

  이것이 바로 색조가 외양 이상으로 중요한 이유입니다: 잎/꽃잎/가시 식물은 **bright(밝은)** 색만이
  그 시약을 산출합니다. **Cocoa pulp**, **sack of sugar**, **vanilla**는
  [요리(Cooking)](/ko/skills/cooking/) 계통(초콜릿과 제빵 레시피)에 들어갑니다.
- **식물 색소(Plant pigments)** — 완전 성장 및 장식용 식물의 색은 **식물 색소(plant pigments)**
  로 바꿀 수 있으며(`Scripts/Services/BasketWeaving/PlantPigment.cs`), 식물 색 팔레트로 아이템을
  염색하는 데 쓰입니다. 이 샤드에서 염색 색이 어떻게 작동하는지는
  [색조 참고(Hues reference)](/ko/reference/hues/)를 보세요.
- **장식용 식물(Decorative plants)** — 완성된 식물을 장식용으로 설정하면
  [주택 장식(house decorating)](/ko/playing/decorating/)을 위한 영구 화분 식물이 됩니다.

### Naturalist (박물학자)

**Naturalist(박물학자)** NPC(`Scripts/Mobiles/NPCs/Naturalist.cs`)는 **Study of Solen** 퀘스트와
연결되어 있습니다. 이를 완료하면 **무작위 식물 씨앗**을 보상으로 받습니다. 평범한 둥지를
연구하면 준희귀 색조 셋(**Pink, Magenta, Aqua**) 중 하나가 나오고; *특별한* 둥지를 연구하면
진정한 희귀 색조(**Fire Red, White, 또는 Black**)가 나옵니다 — 단순히 교배할 수 없는 색으로
수집을 시작하기에 믿을 만한 방법입니다. *(이 샤드의 Naturalist는 퀘스트 제공자이며, 식물
감정사/상인이 아닙니다.)*

## 함께 보기

- [장식(Decorating)](/ko/playing/decorating/) — 화분 식물과 장식용 나무를 집에 배치하기.
- [주택 종류(House Types)](/ko/playing/house-types/) — 식물을 잠금 고정할 집 형태.
- [색조(Hues)](/ko/reference/hues/) — 식물 색과 식물 색소가 염색 팔레트에 어떻게 들어맞는지.
- [자원(Resources)](/ko/items/resources/) — 식물로 기른 재료가 채집 자원 중 어디에 위치하는지.
- [요리(Cooking)](/ko/skills/cooking/) — 정원의 코코아, 설탕, 바닐라가 제빵 레시피에 들어갑니다.
- [직업(Professions)](/ko/professions/) — 전업 정원사는 재미있고 평화로운 틈새 직업입니다.
