---
title: 방어구
description: 방어구와 다섯 가지 저항이 어떻게 작동하는지, 천부터 드래곤 비늘까지의 모든 재료, 신체 슬롯, 방패, 그리고 균형 잡힌 한 벌을 맞추는 법.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Armor/BaseArmor.cs"
  - "servuo: Scripts/Items/Equipment/Armor/ArmorEnums.cs"
  - "servuo: Scripts/Items/Equipment/Armor/*.cs (per-piece base resists, str req, material)"
  - "servuo: Server/Mobile.cs (MaxPlayerResistance = 70)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (GetMinResistance — Magic Resist floor)"
  - "servuo: Scripts/Misc/RegenRates.cs (GetArmorMeditationValue — meditation/mana penalty)"
  - "client art: static art for piece sprites"
last_verified: 2026-06-11
generated: false
---

방어구는 당신의 체력과 드래곤의 숨결 사이를 막아 서는 것입니다. 우리 샤드(서버 에뮬레이터,
Endless Journey / AOS 규칙)에서는 착용하는 모든 부위가 각 피해 유형의 일부를 흡수하는
**저항(resistances)**을 기여합니다. 좋은 한 벌은 무거운 가슴판 하나가 아니라 — 여섯 신체 슬롯을
모두 덮고 강력한 상한선 아래에서 다섯 저항 수치의 균형을 맞추는 것입니다.

아래 표의 수치는 서버 소스에 부위별로 정의된 **기본(base)** 값입니다. 페이퍼돌에 실제로 표시되는
값은 제작 **재료**(광석 또는 가죽 종류), **명품(exceptional)** 품질, 그리고 마법 속성의 보너스를
더한 것입니다 — [재료](#materials)와 [한 벌 & 전략](#suits--strategy)을 보세요.

## 방어구가 작동하는 방식 (AOS / EJ)

### 다섯 가지 저항

현대 방어구는 각각 한 피해 유형을 줄이는 다섯 **저항(resistances)**으로 평가됩니다.

- **Physical(물리)** — 검, 화살, 대부분의 근접 및 물리 주문
- **Fire(화염)** — Fireball, Flamestrike, 불을 뿜는 생물
- **Cold(냉기)** — 서리 주문과 냉기 기반 생물
- **Poison(독)** — Poison 주문, 독 묻은 무기, 독성 생물
- **Energy(에너지)** — Energy Bolt, Lightning, 그리고 에너지 공격

저항 *N*은 해당 피해 유형이 *N* 퍼센트만큼 줄어든다는 뜻입니다. 착용하는 각 방어구 부위가 자신의
저항을 당신의 총합에 더하며, 페이퍼돌은 착용한 모든 부위의 합을 보여줍니다. 피해는 들어오는 유형에
맞는 저항에 대해 적용되므로, 화염에 치우친 한 벌은 에너지 메이지 앞에서 녹아내립니다.

### 70% 저항 상한

플레이어 저항에는 상한이 있습니다. 서버 에뮬레이터의 `Server/Mobile.cs`는
`MaxPlayerResistance = 70`으로 설정합니다 — **어떤 저항도 70%를 넘을 수 없습니다**. 방어구를 아무리
많이 쌓거나 보너스를 아무리 많이 쌓아도 마찬가지입니다. 따라서 한 벌 맞추기는 넘치는 부분을
낭비하지 않으면서 신경 쓰는 유형에서 70에 도달하는 게임입니다. (일부 몬스터와 특수 효과는 당신의
실효 상한을 낮출 수 있습니다. 70 천장은 정상적인 플레이어 최대치입니다.)

높은 **마법 저항(Magic Resistance)** 스킬은 *반대로* 작동합니다 — 당신의 저항 *하한*을
(`PlayerMobile.GetMinResistance`) 끌어올려, GM 저항에서 낮은 저항들을 최소치 쪽으로 당겨 올립니다.
그래서 저항 메이지는 어떤 원소에도 완전히 무방비가 되지 않습니다.
[전투(고급)](/ko/playing/combat-advanced/)를 보세요.

### 힘 요구치

모든 부위에는 **힘 요구치(Strength requirement)**가 있습니다 — 무거운 재료일수록 더 많이 요구합니다.
플레이트 가슴판은 **힘 95**가 필요하고, 가죽 가슴판은 **25**면 됩니다(AOS 값). 요구치보다 낮은
부위를 착용하면 그 대가를 치르게 되며, 그래서 힘이 낮은 시전자는 가죽 쪽으로 기웁니다. 일부 방어구
모드와 재료는 요구치를 낮춥니다. [캐릭터 & 스탯](/ko/playing/character-and-stats/)을 보세요.

### 명상 페널티 (마나 재생)

무겁고 금속인 방어구는 **마나 재생을 옥죕니다**. 서버 에뮬레이터의
`RegenRates.GetArmorMeditationValue`는 착용한 각 부위의 **명상 허용치(meditation allowance)**를
확인합니다.

- **All**(명상 가능) — 페널티 없음(가죽, 천, 그리고 대부분의 메이지 친화적 방어구)
- **Half** — 마나 재생에서 그 부위의 보정된 방어 등급의 절반을 차감(스터디드)
- **None**(명상 불가) — 보정된 방어 등급 전체를 차감(본, 링, 체인, 플레이트, 드래곤, 스톤)

착용한 모든 부위의 페널티가 합산되고 나뉘어 마나 재생을 끌어내립니다. 빠져나갈 길은 두 가지입니다:
**Mage Armor** 속성(과 **Spell Channeling**)은 이 계산에서 어떤 부위든 완전히 명상 가능한 것으로
취급하게 하고, Stygian Abyss / EJ 규칙에서 명상 불가 **금속** 방어구는 대신 고유한 **Lower Mana
Cost**를 부여합니다(근접 시전자에게 도움이 되는 작은 절충). 전체 메커니즘 — 메이지가 왜 가죽을
선호하는지 포함 — 은 [명상 & 마나](/ko/playing/meditation-and-mana/)에 있습니다.

### 신체 슬롯과 "한 벌"

방어구는 여섯 신체 슬롯을 덮고, 방패는 보조 손을 차지합니다.

| Slot | Pieces |
|---|---|
| Helm | helmet, cap, coif, circlet, kabuto |
| Gorget / Neck | gorget, collar, mempo |
| Chest | chest, tunic, bustier |
| Arms | arms, sleeves, sode, pauldrons |
| Gloves | gloves, mitts |
| Legs | legs, leggings, kilt, skirt |

완전한 **한 벌**은 슬롯당 한 부위씩입니다. 저항은 슬롯에 걸쳐 *더해지므로*, 평범한 재료의 완전한
한 벌이 혼자 입은 무거운 가슴판 하나를 손쉽게 능가합니다. 가슴은 방어 등급에 가장 많이 기여하지만
(그 계수가 가장 큼 — 아래 참고), 비어 있는 슬롯은 모두 그냥 버려지는 저항입니다.

서버 에뮬레이터는 각 슬롯의 AOS 이전 방어 등급 기여를 고정 표(`BaseArmor.ArmorScalars`)로
보정합니다: Gorget `0.07`, Gloves `0.07`, Helmet `0.14`, Arms `0.15`, Legs `0.22`, Chest `0.35`.
가슴이 대략 한 벌 등급의 절반입니다.

### 옛 방어 등급(Armor Rating)에 관하여

AOS 이전에는 방어구가 다섯 저항이 아니라 단일 **방어 등급(Armor Rating, AR)** 수치를 썼습니다.
우리 샤드는 AOS/EJ 규칙으로 돌아가므로 플레이에서 중요한 것은 저항이지만, 기저의 `ArmorBase` 값
(아래 표의 `ar=` 열)은 여전히 AOS 이전 방어 등급과 명상 페널티 계산에 들어갑니다. 그래서 AR이 높은
플레이트 부위가 AR이 낮은 가죽 부위보다 마나 재생을 더 크게 깎습니다.

## 재료

재료는 부드러운 천과 가죽부터 금속 메일과 플레이트를 거쳐 이국적인 드래곤 비늘과 가고일 돌에까지
이릅니다. 아래 각 행은 **그 재료의 가슴 부위 기본 저항 프로필**과 힘 요구치, 기본 방어 등급, 명상
허용치이며, 부위별 소스에서 그대로 가져왔습니다. 같은 재료의 다른 슬롯은 저항 프로필을 공유하지만
더 낮은 힘 요구치와 방어 등급을 가집니다.

| | Material | Phys | Fire | Cold | Poison | Energy | Str (chest) | AR | Medable | 제작 직업 |
|---|---|---|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x13CC.png" class="uo-sprite" alt="" width="48" /> | **Leather** | 2 | 4 | 3 | 3 | 3 | 25 | 13 | **All** | [재봉(Tailoring)](/ko/crafting/tailoring/) |
| <img src="/img/items/0x13DB.png" class="uo-sprite" alt="" width="48" /> | **Studded** | 2 | 4 | 3 | 3 | 4 | 35 | 16 | Half | [재봉(Tailoring)](/ko/crafting/tailoring/) |
| <img src="/img/items/0x144F.png" class="uo-sprite" alt="" width="48" /> | **Bone** | 3 | 3 | 4 | 2 | 4 | 60 | 30 | None | [재봉(Tailoring)](/ko/crafting/tailoring/) |
| <img src="/img/items/0x13EC.png" class="uo-sprite" alt="" width="48" /> | **Ringmail** | 3 | 3 | 1 | 5 | 3 | 40 | 22 | None | [대장기술(Blacksmithy)](/ko/crafting/blacksmithy/) |
| <img src="/img/items/0x13BF.png" class="uo-sprite" alt="" width="48" /> | **Chainmail** | 4 | 4 | 4 | 1 | 2 | 60 | 28 | None | [대장기술(Blacksmithy)](/ko/crafting/blacksmithy/) |
| <img src="/img/items/0x1415.png" class="uo-sprite" alt="" width="48" /> | **Plate** | 5 | 3 | 2 | 3 | 2 | 95 | 40 | None | [대장기술(Blacksmithy)](/ko/crafting/blacksmithy/) |
| <img src="/img/items/0x2641.png" class="uo-sprite" alt="" width="48" /> | **Dragon scale** | 3 | 3 | 3 | 3 | 3 | 75 | 40 | None | [대장기술(Blacksmithy)](/ko/crafting/blacksmithy/) |
| <img src="/img/items/0x2B67.png" class="uo-sprite" alt="" width="48" /> | **Woodland** | 5 | 3 | 2 | 3 | 2 | 95 | 40 | None | [재봉(Tailoring)](/ko/crafting/tailoring/) |
| <img src="/img/items/0x0286.png" class="uo-sprite" alt="" width="48" /> | **Stone (gargish)** | 6 | 6 | 4 | 8 | 6 | 40 | — | None | [재봉(Tailoring)](/ko/crafting/tailoring/) |

*출처: `Scripts/Items/Equipment/Armor/*.cs`, 재료별 가슴 부위. 수치는 재료, 품질, 마법 보너스 이전의
기본 저항입니다.*

표 읽는 법:

- **Cloth(천)**는 엄밀히는 가장 가벼운 "방어구"이지만 표준 천은 의류 레이어(BaseArmor가 아니라
  BaseClothing)에 속하며 그 자체로는 거의 아무것도 기여하지 않습니다 — 메이지에게의 가치는 완전히
  명상 가능하고 염색 가능하다는 점입니다. 가고일 "천" 방어구 부위는 특수한 경우로, 천처럼 보이지만
  소스에서는 기계적으로 **Leather** 재료입니다.
- **Leather(가죽)**는 메이지와 궁수의 친구입니다 — 완전히 **명상 가능**(마나 재생 페널티 없음),
  가장 낮은 힘 요구치, 균형 잡힌 낮은 저항. Barbed/horned/spined 생가죽(아래 참고)은 그 저항을
  크게 끌어올립니다.
- **Studded(스터디드)**는 마나 재생의 절반을 약간 더 나은 물리/에너지 방어와 맞바꿉니다.
- **Bone(본)**은 (뼈로 제작하는) 재봉 중간 방어구로, 고른 중간 범위 저항과 묵직한 힘 비용을
  가집니다.
- **Ringmail → Chainmail → Plate**는 대장장이의 금속 계열입니다: 방어 등급과 힘 요구치가 올라가고
  명상이 허용되지 않습니다. 플레이트는 전사의 표준입니다 — 가장 높은 기본 물리와 방어 등급.
- **Dragon scale(드래곤 비늘)**은 이국적인 예외입니다. 기본 저항은 평탄한 **3/3/3/3/3**이지만, 비늘
  방어구의 매력은 위에 덧입히는 **색 있는 드래곤 비늘**이 주는 높은 저항과, 약점 원소가 없는 고른
  분포에 있습니다.
- **Woodland(우드랜드, 엘프)**는 플레이트의 프로필을 따르지만 나무/가죽으로 **재봉**합니다.
- **Stone(스톤)**은 가고일의 중장갑입니다: 이 목록에서 가장 높은 기본 저항(그리고 특히 높은 독
  저항)으로, 엔드게임 재료의 지위를 반영합니다.

### 제작과 생가죽

- **재봉(Tailoring)**은 가죽, 스터디드, 본, 우드랜드, 가고일 방어구를 제작합니다. 가죽 계열은 쓰인
  생가죽에 따라 스케일됩니다: 일반 가죽 → **spined** → **horned** → **barbed**, 각각 점점 더 나은
  저항과 방어 등급을 가진 별개의 `ArmorMaterialType`입니다.
  [재봉(Tailoring)](/ko/crafting/tailoring/)과 [자원(Resources)](/ko/items/resources/)을 보세요.
- **대장기술(Blacksmithy)**은 링메일, 체인메일, 플레이트, 드래곤 비늘 방어구를 단조합니다. 쓰인
  광석(dull copper → valorite)은 저항과 방어 보너스, 그리고 색 있는 **색조(hue)**를 더합니다.

## 방패

방패는 보조 손(양손) 슬롯을 차지하며 [방어술(Parrying)](/ko/skills/parrying/) 스킬의 지배를 받습니다.
이 스킬은 들어오는 근접 또는 원거리 타격을 **통째로 막을** 확률을 줍니다. 막기 확률은 방어술 스킬과
장착한 방패에 따라 스케일됩니다 — 무거운 방패는 더 많이 막지만 더 무겁고 더 많은 힘을 요구합니다.

방패 종류는 가벼운 **버클러**부터 목재와 청동 방패를 거쳐 **무거운 금속**과 **카이트** 방패에까지
이르며, 오더/카오스와 가고일 변형도 있습니다. 모든 금속 방패는 기본적으로 **Plate** 재료이며,
플레이트 방어구처럼 **명상 불가**로 취급됩니다 — 다만 AOS/EJ 규칙에서 방패는 명상/마나 페널티에
더해지지 **않습니다**(여섯 신체 슬롯만 더해집니다; `RegenRates.GetArmorOffset`은 AOS에서 방패를
건너뜀). 방어술을 쓰려는 메이지는 시전을 유지하기 위해 여전히 **Spell Channeling** 방패를
선호합니다.

아트와 함께 모든 방패를 보려면 [방패 카탈로그](/ko/items/catalog/shields/)를, 막기 확률 세부사항은
[방어술(Parrying)](/ko/skills/parrying/)을 보세요.

## 한 벌 & 전략

한 벌을 맞추는 일은 캐릭터가 감당할 수 있는 방어와 마나 재생 프로필 위에서, 다섯 유형 전부에 대해
**70% 상한 아래 저항을 최대화**하는 것입니다.

- **균형 잡힌 한 벌** — 한 유형을 뾰족하게 올리기보다 최저 저항을 가장 높게 끌어올리는 것을
  목표로 하세요. 몬스터의 피해 유형이 어느 저항이 중요한지를 결정하므로, 전반적으로 60대인 균형
  잡힌 한 벌이 물리 70 / 에너지 20인 한 벌보다 더 많은 교전에서 살아남습니다. 저항은 슬롯에 걸쳐
  더해지므로, 부위별 수치를 더 높이려 하기 전에 **모든 슬롯**을 채우세요.
- **메이지의 절충** — 금속 방어구는 명상을 막으므로, 시전자는 역사적으로 가죽/천으로 도배하고 낮은
  물리 저항을 감수했습니다. **Mage Armor** 속성이 이 규칙을 깹니다 — 메이지가 마나 재생 페널티
  없이 고저항 명상 불가 방어구(심지어 플레이트)를 입게 해줍니다. 당신의 템플릿에 맞춰 저항 방어,
  힘 요구치, 마나 재생을 저울질하세요 — [명상 & 마나](/ko/playing/meditation-and-mana/)와
  [7 GM 템플릿](/ko/templates/seven-gm/)의 7 GM 메이지 빌드를 보세요.
- **재료로 만든 색 있는 방어구** — 더 나은 광석이나 생가죽으로 제작하면 저항이 오르고 *동시에*
  방어구의 색이 바뀝니다. 색조가 모두에게 재료를 한눈에 알려줍니다. Dull copper, shadow iron,
  copper, bronze, gold, agapite, verite, valorite는 각각 방어를 점점 더하고 뚜렷한 색을 줍니다
  ([색조 참조(Hue Reference)](/ko/reference/hues/) 참고). 숙련된 제작자의 명품 품질은 추가
  내구도와 저항을 더합니다.
- **가고일 & 엘프 변형** — 가고일 캐릭터는 **가고일** 플레이트/스톤/가죽 부위를 사용하며(사람
  모양의 투구는 착용 불가), 엘프는 **우드랜드** 방어구를 사용합니다. 기저 재료 메커니즘은
  공유하지만 종족 제한이 있으므로, 플레이하는 종족에 맞춰 한 벌을 맞추세요.

한 벌을 입을 가치가 있게 만드는 스킬을 키우려면 [전술(Tactics)](/ko/skills/tactics/),
[방어술(Parrying)](/ko/skills/parrying/), 그리고 [7 GM 템플릿](/ko/templates/seven-gm/)을 보세요.
아트와 아이템 ID와 함께 특정 부위를 보려면 [방어구 카탈로그](/ko/items/catalog/armor/)와
[방패 카탈로그](/ko/items/catalog/shields/)를 보세요.
