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
  - "data: data/armor.json (gallery — 148 piece sprites grouped by material)"
last_verified: 2026-06-15
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


## 방어구 갤러리

이 샤드에서 제작 가능한 모든 방어구 조각을 재료별로(투구 → 고짓 → 가슴 → 팔 → 장갑 → 다리) 정리했습니다. 스프라이트는 기본 클라이언트 아트이며, 실제 플레이에서는 제작 재료(광석 또는 가죽)가 각 조각의 색과 수치를 바꿉니다. 스탯과 아이템 ID는 [방어구 카탈로그](/ko/items/catalog/armor/)에서 볼 수 있습니다.

### Leather

<div class="uo-gallery">
  <figure><img src="/img/items/0x782D.png" alt="Dragon Turtle Hide Helm" loading="lazy" /><figcaption>Dragon Turtle Hide Helm</figcaption></figure>
  <figure><img src="/img/items/0x7828.png" alt="Tiger Pelt Helm" loading="lazy" /><figcaption>Tiger Pelt Helm</figcaption></figure>
  <figure><img src="/img/items/0x1DB9.png" alt="leather cap" loading="lazy" /><figcaption>leather cap</figcaption></figure>
  <figure><img src="/img/items/0x2776.png" alt="leather jingasa" loading="lazy" /><figcaption>leather jingasa</figcaption></figure>
  <figure><img src="/img/items/0x278E.png" alt="leather ninja hood" loading="lazy" /><figcaption>leather ninja hood</figcaption></figure>
  <figure><img src="/img/items/0x7829.png" alt="Tiger Pelt Collar" loading="lazy" /><figcaption>Tiger Pelt Collar</figcaption></figure>
  <figure><img src="/img/items/0xA40F.png" alt="elegant collar" loading="lazy" /><figcaption>elegant collar</figcaption></figure>
  <figure><img src="/img/items/0xA40F.png" alt="elegant collar of fortune" loading="lazy" /><figcaption>elegant collar of fortune</figcaption></figure>
  <figure><img src="/img/items/0x2FC7.png" alt="leaf gorget" loading="lazy" /><figcaption>leaf gorget</figcaption></figure>
  <figure><img src="/img/items/0x13C7.png" alt="leather gorget" loading="lazy" /><figcaption>leather gorget</figcaption></figure>
  <figure><img src="/img/items/0x277A.png" alt="leather mempo" loading="lazy" /><figcaption>leather mempo</figcaption></figure>
  <figure><img src="/img/items/0x782B.png" alt="Dragon Turtle Hide Bustier" loading="lazy" /><figcaption>Dragon Turtle Hide Bustier</figcaption></figure>
  <figure><img src="/img/items/0x782A.png" alt="Dragon Turtle Hide Chest" loading="lazy" /><figcaption>Dragon Turtle Hide Chest</figcaption></figure>
  <figure><img src="/img/items/0x7823.png" alt="Tiger Pelt Bustier" loading="lazy" /><figcaption>Tiger Pelt Bustier</figcaption></figure>
  <figure><img src="/img/items/0x7822.png" alt="Tiger Pelt Chest" loading="lazy" /><figcaption>Tiger Pelt Chest</figcaption></figure>
  <figure><img src="/img/items/0x0405.png" alt="female gargish cloth chest armor" loading="lazy" /><figcaption>female gargish cloth chest armor</figcaption></figure>
  <figure><img src="/img/items/0x0303.png" alt="female gargish leather chest" loading="lazy" /><figcaption>female gargish leather chest</figcaption></figure>
  <figure><img src="/img/items/0x2FCB.png" alt="female leaf chest" loading="lazy" /><figcaption>female leaf chest</figcaption></figure>
  <figure><img src="/img/items/0x1C06.png" alt="female leather chest" loading="lazy" /><figcaption>female leather chest</figcaption></figure>
  <figure><img src="/img/items/0x0406.png" alt="gargish cloth chest armor" loading="lazy" /><figcaption>gargish cloth chest armor</figcaption></figure>
  <figure><img src="/img/items/0x0304.png" alt="gargish leather chest" loading="lazy" /><figcaption>gargish leather chest</figcaption></figure>
  <figure><img src="/img/items/0x2FC5.png" alt="leaf chest" loading="lazy" /><figcaption>leaf chest</figcaption></figure>
  <figure><img src="/img/items/0x13CC.png" alt="leather chest" loading="lazy" /><figcaption>leather chest</figcaption></figure>
  <figure><img src="/img/items/0x2793.png" alt="leather ninja jacket" loading="lazy" /><figcaption>leather ninja jacket</figcaption></figure>
  <figure><img src="/img/items/0x782E.png" alt="Dragon Turtle Hide Arms" loading="lazy" /><figcaption>Dragon Turtle Hide Arms</figcaption></figure>
  <figure><img src="/img/items/0x0403.png" alt="female gargish cloth arms armor" loading="lazy" /><figcaption>female gargish cloth arms armor</figcaption></figure>
  <figure><img src="/img/items/0x0301.png" alt="female gargish leather arms" loading="lazy" /><figcaption>female gargish leather arms</figcaption></figure>
  <figure><img src="/img/items/0x0404.png" alt="gargish cloth arms armor" loading="lazy" /><figcaption>gargish cloth arms armor</figcaption></figure>
  <figure><img src="/img/items/0x0302.png" alt="gargish leather arms" loading="lazy" /><figcaption>gargish leather arms</figcaption></figure>
  <figure><img src="/img/items/0x457E.png" alt="gargish leather wing armor" loading="lazy" /><figcaption>gargish leather wing armor</figcaption></figure>
  <figure><img src="/img/items/0x2FC8.png" alt="leaf arms" loading="lazy" /><figcaption>leaf arms</figcaption></figure>
  <figure><img src="/img/items/0x13CD.png" alt="leather arms" loading="lazy" /><figcaption>leather arms</figcaption></figure>
  <figure><img src="/img/items/0x1C0A.png" alt="leather bustier arms" loading="lazy" /><figcaption>leather bustier arms</figcaption></figure>
  <figure><img src="/img/items/0x277E.png" alt="leather hiro sode" loading="lazy" /><figcaption>leather hiro sode</figcaption></figure>
  <figure><img src="/img/items/0x2FC6.png" alt="leaf gloves" loading="lazy" /><figcaption>leaf gloves</figcaption></figure>
  <figure><img src="/img/items/0x13C6.png" alt="leather gloves" loading="lazy" /><figcaption>leather gloves</figcaption></figure>
  <figure><img src="/img/items/0x2792.png" alt="leather ninja mitts" loading="lazy" /><figcaption>leather ninja mitts</figcaption></figure>
  <figure><img src="/img/items/0x782C.png" alt="Dragon Turtle Hide Leggings" loading="lazy" /><figcaption>Dragon Turtle Hide Leggings</figcaption></figure>
  <figure><img src="/img/items/0x7824.png" alt="Tiger Pelt Leggings" loading="lazy" /><figcaption>Tiger Pelt Leggings</figcaption></figure>
  <figure><img src="/img/items/0x7826.png" alt="Tiger Pelt Long Skirt" loading="lazy" /><figcaption>Tiger Pelt Long Skirt</figcaption></figure>
  <figure><img src="/img/items/0x7825.png" alt="Tiger Pelt Shorts" loading="lazy" /><figcaption>Tiger Pelt Shorts</figcaption></figure>
  <figure><img src="/img/items/0x7827.png" alt="Tiger Pelt Skirt" loading="lazy" /><figcaption>Tiger Pelt Skirt</figcaption></figure>
  <figure><img src="/img/items/0x0407.png" alt="female gargish cloth kilt armor" loading="lazy" /><figcaption>female gargish cloth kilt armor</figcaption></figure>
  <figure><img src="/img/items/0x0409.png" alt="female gargish cloth legs armor" loading="lazy" /><figcaption>female gargish cloth legs armor</figcaption></figure>
  <figure><img src="/img/items/0x0310.png" alt="female gargish leather kilt" loading="lazy" /><figcaption>female gargish leather kilt</figcaption></figure>
  <figure><img src="/img/items/0x0305.png" alt="female gargish leather legs" loading="lazy" /><figcaption>female gargish leather legs</figcaption></figure>
  <figure><img src="/img/items/0x0408.png" alt="gargish cloth kilt armor" loading="lazy" /><figcaption>gargish cloth kilt armor</figcaption></figure>
  <figure><img src="/img/items/0x040A.png" alt="gargish cloth legs armor" loading="lazy" /><figcaption>gargish cloth legs armor</figcaption></figure>
  <figure><img src="/img/items/0x0311.png" alt="gargish leather kilt" loading="lazy" /><figcaption>gargish leather kilt</figcaption></figure>
  <figure><img src="/img/items/0x0305.png" alt="gargish leather legs" loading="lazy" /><figcaption>gargish leather legs</figcaption></figure>
  <figure><img src="/img/items/0x2FC9.png" alt="leaf legs" loading="lazy" /><figcaption>leaf legs</figcaption></figure>
  <figure><img src="/img/items/0x2FCA.png" alt="leaf tonlet" loading="lazy" /><figcaption>leaf tonlet</figcaption></figure>
  <figure><img src="/img/items/0x27C6.png" alt="leather do" loading="lazy" /><figcaption>leather do</figcaption></figure>
  <figure><img src="/img/items/0x278A.png" alt="leather haidate" loading="lazy" /><figcaption>leather haidate</figcaption></figure>
  <figure><img src="/img/items/0x13CB.png" alt="leather legs" loading="lazy" /><figcaption>leather legs</figcaption></figure>
  <figure><img src="/img/items/0x2791.png" alt="leather ninja pants" loading="lazy" /><figcaption>leather ninja pants</figcaption></figure>
  <figure><img src="/img/items/0x1C00.png" alt="leather shorts" loading="lazy" /><figcaption>leather shorts</figcaption></figure>
  <figure><img src="/img/items/0x1C08.png" alt="leather skirt" loading="lazy" /><figcaption>leather skirt</figcaption></figure>
  <figure><img src="/img/items/0x2786.png" alt="leather suneate" loading="lazy" /><figcaption>leather suneate</figcaption></figure>
</div>

### Studded

<div class="uo-gallery">
  <figure><img src="/img/items/0x2B76.png" alt="hide gorget" loading="lazy" /><figcaption>hide gorget</figcaption></figure>
  <figure><img src="/img/items/0x13D6.png" alt="studded gorget" loading="lazy" /><figcaption>studded gorget</figcaption></figure>
  <figure><img src="/img/items/0x279D.png" alt="studded mempo" loading="lazy" /><figcaption>studded mempo</figcaption></figure>
  <figure><img src="/img/items/0x1C02.png" alt="female studded chest" loading="lazy" /><figcaption>female studded chest</figcaption></figure>
  <figure><img src="/img/items/0x2B74.png" alt="hide chest" loading="lazy" /><figcaption>hide chest</figcaption></figure>
  <figure><img src="/img/items/0x2B79.png" alt="hide female chest" loading="lazy" /><figcaption>hide female chest</figcaption></figure>
  <figure><img src="/img/items/0x13DB.png" alt="studded chest" loading="lazy" /><figcaption>studded chest</figcaption></figure>
  <figure><img src="/img/items/0x2B77.png" alt="hide pauldrons" loading="lazy" /><figcaption>hide pauldrons</figcaption></figure>
  <figure><img src="/img/items/0x13DC.png" alt="studded arms" loading="lazy" /><figcaption>studded arms</figcaption></figure>
  <figure><img src="/img/items/0x1C0C.png" alt="studded bustier arms" loading="lazy" /><figcaption>studded bustier arms</figcaption></figure>
  <figure><img src="/img/items/0x277F.png" alt="studded hiro sode" loading="lazy" /><figcaption>studded hiro sode</figcaption></figure>
  <figure><img src="/img/items/0x2B75.png" alt="hide gloves" loading="lazy" /><figcaption>hide gloves</figcaption></figure>
  <figure><img src="/img/items/0x13D5.png" alt="studded gloves" loading="lazy" /><figcaption>studded gloves</figcaption></figure>
  <figure><img src="/img/items/0x2B78.png" alt="hide pants" loading="lazy" /><figcaption>hide pants</figcaption></figure>
  <figure><img src="/img/items/0x27C7.png" alt="studded do" loading="lazy" /><figcaption>studded do</figcaption></figure>
  <figure><img src="/img/items/0x278B.png" alt="studded haidate" loading="lazy" /><figcaption>studded haidate</figcaption></figure>
  <figure><img src="/img/items/0x13DA.png" alt="studded legs" loading="lazy" /><figcaption>studded legs</figcaption></figure>
  <figure><img src="/img/items/0x27D2.png" alt="studded suneate" loading="lazy" /><figcaption>studded suneate</figcaption></figure>
</div>

### Bone

<div class="uo-gallery">
  <figure><img src="/img/items/0x1F0B.png" alt="an evil orc helm" loading="lazy" /><figcaption>an evil orc helm</figcaption></figure>
  <figure><img src="/img/items/0x1451.png" alt="bone helm" loading="lazy" /><figcaption>bone helm</figcaption></figure>
  <figure><img src="/img/items/0x1F0B.png" alt="orc helm" loading="lazy" /><figcaption>orc helm</figcaption></figure>
  <figure><img src="/img/items/0x144F.png" alt="bone chest" loading="lazy" /><figcaption>bone chest</figcaption></figure>
  <figure><img src="/img/items/0x144E.png" alt="bone arms" loading="lazy" /><figcaption>bone arms</figcaption></figure>
  <figure><img src="/img/items/0x1450.png" alt="bone gloves" loading="lazy" /><figcaption>bone gloves</figcaption></figure>
  <figure><img src="/img/items/0x1452.png" alt="bone legs" loading="lazy" /><figcaption>bone legs</figcaption></figure>
</div>

### Ringmail

<div class="uo-gallery">
  <figure><img src="/img/items/0x13EC.png" alt="ringmail chest" loading="lazy" /><figcaption>ringmail chest</figcaption></figure>
  <figure><img src="/img/items/0x13EE.png" alt="ringmail arms" loading="lazy" /><figcaption>ringmail arms</figcaption></figure>
  <figure><img src="/img/items/0x13EB.png" alt="ringmail gloves" loading="lazy" /><figcaption>ringmail gloves</figcaption></figure>
  <figure><img src="/img/items/0x13F0.png" alt="ringmail legs" loading="lazy" /><figcaption>ringmail legs</figcaption></figure>
</div>

### Chainmail

<div class="uo-gallery">
  <figure><img src="/img/items/0x13BB.png" alt="chain coif" loading="lazy" /><figcaption>chain coif</figcaption></figure>
  <figure><img src="/img/items/0x2774.png" alt="chain hatsuburi" loading="lazy" /><figcaption>chain hatsuburi</figcaption></figure>
  <figure><img src="/img/items/0x13BF.png" alt="chain chest" loading="lazy" /><figcaption>chain chest</figcaption></figure>
  <figure><img src="/img/items/0x13BE.png" alt="chain legs" loading="lazy" /><figcaption>chain legs</figcaption></figure>
</div>

### Plate

<div class="uo-gallery">
  <figure><img src="/img/items/0x140C.png" alt="bascinet" loading="lazy" /><figcaption>bascinet</figcaption></figure>
  <figure><img src="/img/items/0x2B6E.png" alt="circlet" loading="lazy" /><figcaption>circlet</figcaption></figure>
  <figure><img src="/img/items/0x1408.png" alt="close helm" loading="lazy" /><figcaption>close helm</figcaption></figure>
  <figure><img src="/img/items/0x2778.png" alt="decorative plate kabuto" loading="lazy" /><figcaption>decorative plate kabuto</figcaption></figure>
  <figure><img src="/img/items/0x2B70.png" alt="gemmed circlet" loading="lazy" /><figcaption>gemmed circlet</figcaption></figure>
  <figure><img src="/img/items/0x2777.png" alt="heavy plate jingasa" loading="lazy" /><figcaption>heavy plate jingasa</figcaption></figure>
  <figure><img src="/img/items/0x140A.png" alt="helmet" loading="lazy" /><figcaption>helmet</figcaption></figure>
  <figure><img src="/img/items/0x2781.png" alt="light plate jingasa" loading="lazy" /><figcaption>light plate jingasa</figcaption></figure>
  <figure><img src="/img/items/0x140E.png" alt="norse helm" loading="lazy" /><figcaption>norse helm</figcaption></figure>
  <figure><img src="/img/items/0x2785.png" alt="plate battle kabuto" loading="lazy" /><figcaption>plate battle kabuto</figcaption></figure>
  <figure><img src="/img/items/0x2775.png" alt="plate hatsuburi" loading="lazy" /><figcaption>plate hatsuburi</figcaption></figure>
  <figure><img src="/img/items/0x1412.png" alt="plate helm" loading="lazy" /><figcaption>plate helm</figcaption></figure>
  <figure><img src="/img/items/0x2B71.png" alt="raven helm" loading="lazy" /><figcaption>raven helm</figcaption></figure>
  <figure><img src="/img/items/0x2B6F.png" alt="royal circlet" loading="lazy" /><figcaption>royal circlet</figcaption></figure>
  <figure><img src="/img/items/0x2784.png" alt="small plate jingasa" loading="lazy" /><figcaption>small plate jingasa</figcaption></figure>
  <figure><img src="/img/items/0x2789.png" alt="standard plate kabuto" loading="lazy" /><figcaption>standard plate kabuto</figcaption></figure>
  <figure><img src="/img/items/0x2B72.png" alt="vulture helm" loading="lazy" /><figcaption>vulture helm</figcaption></figure>
  <figure><img src="/img/items/0x2B73.png" alt="winged helm" loading="lazy" /><figcaption>winged helm</figcaption></figure>
  <figure><img src="/img/items/0x1413.png" alt="plate gorget" loading="lazy" /><figcaption>plate gorget</figcaption></figure>
  <figure><img src="/img/items/0x2779.png" alt="plate mempo" loading="lazy" /><figcaption>plate mempo</figcaption></figure>
  <figure><img src="/img/items/0x0309.png" alt="female gargish plate chest" loading="lazy" /><figcaption>female gargish plate chest</figcaption></figure>
  <figure><img src="/img/items/0x1C04.png" alt="female plate chest" loading="lazy" /><figcaption>female plate chest</figcaption></figure>
  <figure><img src="/img/items/0x030A.png" alt="gargish plate chest" loading="lazy" /><figcaption>gargish plate chest</figcaption></figure>
  <figure><img src="/img/items/0x1415.png" alt="plate chest" loading="lazy" /><figcaption>plate chest</figcaption></figure>
  <figure><img src="/img/items/0x0307.png" alt="female gargish plate arms" loading="lazy" /><figcaption>female gargish plate arms</figcaption></figure>
  <figure><img src="/img/items/0x0308.png" alt="gargish plate arms" loading="lazy" /><figcaption>gargish plate arms</figcaption></figure>
  <figure><img src="/img/items/0x1410.png" alt="plate arms" loading="lazy" /><figcaption>plate arms</figcaption></figure>
  <figure><img src="/img/items/0x2780.png" alt="plate hiro sode" loading="lazy" /><figcaption>plate hiro sode</figcaption></figure>
  <figure><img src="/img/items/0x1414.png" alt="plate gloves" loading="lazy" /><figcaption>plate gloves</figcaption></figure>
  <figure><img src="/img/items/0x030B.png" alt="female gargish plate kilt" loading="lazy" /><figcaption>female gargish plate kilt</figcaption></figure>
  <figure><img src="/img/items/0x030D.png" alt="female gargish plate legs" loading="lazy" /><figcaption>female gargish plate legs</figcaption></figure>
  <figure><img src="/img/items/0x030C.png" alt="gargish plate kilt" loading="lazy" /><figcaption>gargish plate kilt</figcaption></figure>
  <figure><img src="/img/items/0x030E.png" alt="gargish plate legs" loading="lazy" /><figcaption>gargish plate legs</figcaption></figure>
  <figure><img src="/img/items/0x277D.png" alt="plate do" loading="lazy" /><figcaption>plate do</figcaption></figure>
  <figure><img src="/img/items/0x278D.png" alt="plate haidate" loading="lazy" /><figcaption>plate haidate</figcaption></figure>
  <figure><img src="/img/items/0x1411.png" alt="plate legs" loading="lazy" /><figcaption>plate legs</figcaption></figure>
  <figure><img src="/img/items/0x2788.png" alt="plate suneate" loading="lazy" /><figcaption>plate suneate</figcaption></figure>
</div>

### Dragon scale

<div class="uo-gallery">
  <figure><img src="/img/items/0x2645.png" alt="dragon helm" loading="lazy" /><figcaption>dragon helm</figcaption></figure>
  <figure><img src="/img/items/0x2641.png" alt="dragon chest" loading="lazy" /><figcaption>dragon chest</figcaption></figure>
  <figure><img src="/img/items/0x2657.png" alt="dragon arms" loading="lazy" /><figcaption>dragon arms</figcaption></figure>
  <figure><img src="/img/items/0x2643.png" alt="dragon gloves" loading="lazy" /><figcaption>dragon gloves</figcaption></figure>
  <figure><img src="/img/items/0x2647.png" alt="dragon legs" loading="lazy" /><figcaption>dragon legs</figcaption></figure>
</div>

### Woodland (elven)

<div class="uo-gallery">
  <figure><img src="/img/items/0x2B69.png" alt="woodland gorget" loading="lazy" /><figcaption>woodland gorget</figcaption></figure>
  <figure><img src="/img/items/0x2B6D.png" alt="female elven plate chest" loading="lazy" /><figcaption>female elven plate chest</figcaption></figure>
  <figure><img src="/img/items/0x2B67.png" alt="woodland chest" loading="lazy" /><figcaption>woodland chest</figcaption></figure>
  <figure><img src="/img/items/0x2B6C.png" alt="woodland arms" loading="lazy" /><figcaption>woodland arms</figcaption></figure>
  <figure><img src="/img/items/0x2B6A.png" alt="woodland gloves" loading="lazy" /><figcaption>woodland gloves</figcaption></figure>
  <figure><img src="/img/items/0x2B6B.png" alt="woodland legs" loading="lazy" /><figcaption>woodland legs</figcaption></figure>
</div>

### Stone (gargish)

<div class="uo-gallery">
  <figure><img src="/img/items/0x0285.png" alt="female gargish stone chest" loading="lazy" /><figcaption>female gargish stone chest</figcaption></figure>
  <figure><img src="/img/items/0x0286.png" alt="gargish stone chest" loading="lazy" /><figcaption>gargish stone chest</figcaption></figure>
  <figure><img src="/img/items/0x0283.png" alt="female gargish stone arms" loading="lazy" /><figcaption>female gargish stone arms</figcaption></figure>
  <figure><img src="/img/items/0x0284.png" alt="gargish stone arms" loading="lazy" /><figcaption>gargish stone arms</figcaption></figure>
  <figure><img src="/img/items/0x0287.png" alt="female gargish stone kilt" loading="lazy" /><figcaption>female gargish stone kilt</figcaption></figure>
  <figure><img src="/img/items/0x0289.png" alt="female gargish stone legs" loading="lazy" /><figcaption>female gargish stone legs</figcaption></figure>
  <figure><img src="/img/items/0x0288.png" alt="gargish stone kilt" loading="lazy" /><figcaption>gargish stone kilt</figcaption></figure>
  <figure><img src="/img/items/0x028A.png" alt="gargish stone legs" loading="lazy" /><figcaption>gargish stone legs</figcaption></figure>
</div>

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
