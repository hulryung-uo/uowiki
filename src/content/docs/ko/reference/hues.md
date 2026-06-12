---
title: 휴(Hue) 참조
description: UO 휴 값이 색상으로 매핑되는 방식 — hues.mul 팔레트, 주목할 만한 제작 자원 휴, 그리고 위키가 휴를 PNG에 구워 넣는 이유.
status: source-verified
sources:
  - "client: hues.mul"
  - "servuo: Scripts/Misc/ResourceInfo.cs"
last_verified: 2026-06-11
generated: false
---

울티마 온라인에서 **휴(hue)**는 클라이언트의 `hues.mul` 파일에 대한 1-기반 인덱스입니다. 색이
입혀진 모든 아이템, 생물, 의류는 휴 번호를 지니며; 클라이언트는 그 번호를 조회해 스프라이트를 어떻게
다시 칠할지 결정합니다.

이해해야 할 중요한 점은 휴가 **평평한 색조가 아니라는** 것입니다. 각 휴는 32단계 그라디언트입니다 —
그림자에서 하이라이트까지의 램프. 클라이언트가 휴가 적용된 스프라이트를 그릴 때, 스프라이트 자체의
회색조 그림자→하이라이트 램프를 따라가며 각 회색 단계를 휴 그라디언트의 대응하는 단계로 **재매핑**합니다.
거의 검은 픽셀은 휴의 가장 어두운 단계가 되고; 거의 흰 픽셀은 가장 밝은 단계가 됩니다. 그래서 하나의
회색조 주괴 스프라이트가 모든 음영과 깊이를 유지한 채 눈에 띄게 다른 아홉 가지 금속이 될 수 있는
것입니다.

이 재매핑은 또한 이 위키가 CSS `filter`나 색상 오버레이를 쓰는 대신 **휴를 PNG에 직접 구워 넣는**
이유이기도 합니다: CSS 색조는 평평한 색을 이미지 전체에 곱해 음영을 평탄화하는데, 이는 32단계 팔레트
재매핑을 재현할 수 없습니다. 우리는 `hues.mul`에서 그라디언트를 읽어 내, 클라이언트가 하는 것과
정확히 똑같이 스프라이트를 픽셀 단위로 다시 칠합니다.

(휴 `0`은 특수한 "휴 없음" 값입니다 — "스프라이트를 있는 그대로 그리라"는 뜻이므로, 자체 그라디언트
항목이 없습니다.)

## 전체 팔레트

아래는 `hues.mul`의 모든 휴를 작은 견본의 격자로 그린 것입니다. 각 견본은 그 휴의 32단계
그라디언트에서 대표적인 중간 톤을 보여 줍니다. 격자선은 방향 잡기를 위해 8열과 8행마다 표시됩니다.
왼쪽에서 오른쪽으로, 위에서 아래로 읽으면, 첫 견본이 게임 휴 `1`입니다.

![Grid of all UO hue swatches from hues.mul](/img/hues/chart.png)

*`hues.mul`의 3000개 휴 전부, 각각 하나의 중간 톤 견본(행당 40개).*

## 주목할 만한 휴

이것들은 [ServUO의 `ResourceInfo.cs`](https://github.com/ServUO/ServUO)에 정의된 제작 자원
휴입니다 — 제작 시스템이 금속, 가죽, 드래곤 비늘, 목재에 적용하는 색상. 각 견본은 전체 32단계
그라디언트를 보여 줍니다(맨 위가 그림자, 맨 아래가 하이라이트).

### 금속

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x0973.png" class="uo-sprite" alt="Dull Copper hue ramp" width="48" height="48" /> | `0x0973` | 2419 | Dull Copper |
| <img src="/img/hues/h-0x0966.png" class="uo-sprite" alt="Shadow Iron hue ramp" width="48" height="48" /> | `0x0966` | 2406 | Shadow Iron |
| <img src="/img/hues/h-0x096D.png" class="uo-sprite" alt="Copper hue ramp" width="48" height="48" /> | `0x096D` | 2413 | Copper |
| <img src="/img/hues/h-0x0972.png" class="uo-sprite" alt="Bronze hue ramp" width="48" height="48" /> | `0x0972` | 2418 | Bronze |
| <img src="/img/hues/h-0x08A5.png" class="uo-sprite" alt="Gold hue ramp" width="48" height="48" /> | `0x08A5` | 2213 | Gold |
| <img src="/img/hues/h-0x0979.png" class="uo-sprite" alt="Agapite hue ramp" width="48" height="48" /> | `0x0979` | 2425 | Agapite |
| <img src="/img/hues/h-0x089F.png" class="uo-sprite" alt="Verite hue ramp" width="48" height="48" /> | `0x089F` | 2207 | Verite |
| <img src="/img/hues/h-0x08AB.png" class="uo-sprite" alt="Valorite hue ramp" width="48" height="48" /> | `0x08AB` | 2219 | Valorite |

### 가죽

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x0283.png" class="uo-sprite" alt="Spined leather hue ramp" width="48" height="48" /> | `0x0283` | 643 | Spined |
| <img src="/img/hues/h-0x0227.png" class="uo-sprite" alt="Horned leather hue ramp" width="48" height="48" /> | `0x0227` | 551 | Horned |
| <img src="/img/hues/h-0x01C1.png" class="uo-sprite" alt="Barbed leather hue ramp" width="48" height="48" /> | `0x01C1` | 449 | Barbed |

### 드래곤 비늘

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x066D.png" class="uo-sprite" alt="Red Scales hue ramp" width="48" height="48" /> | `0x066D` | 1645 | Red Scales |
| <img src="/img/hues/h-0x08A8.png" class="uo-sprite" alt="Yellow Scales hue ramp" width="48" height="48" /> | `0x08A8` | 2216 | Yellow Scales |
| <img src="/img/hues/h-0x0455.png" class="uo-sprite" alt="Black Scales hue ramp" width="48" height="48" /> | `0x0455` | 1109 | Black Scales |
| <img src="/img/hues/h-0x0851.png" class="uo-sprite" alt="Green Scales hue ramp" width="48" height="48" /> | `0x0851` | 2129 | Green Scales |
| <img src="/img/hues/h-0x08FD.png" class="uo-sprite" alt="White Scales hue ramp" width="48" height="48" /> | `0x08FD` | 2301 | White Scales |
| <img src="/img/hues/h-0x08B0.png" class="uo-sprite" alt="Blue Scales hue ramp" width="48" height="48" /> | `0x08B0` | 2224 | Blue Scales |

### 목재

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x07DA.png" class="uo-sprite" alt="Oak hue ramp" width="48" height="48" /> | `0x07DA` | 2010 | Oak |
| <img src="/img/hues/h-0x04A7.png" class="uo-sprite" alt="Ash hue ramp" width="48" height="48" /> | `0x04A7` | 1191 | Ash |
| <img src="/img/hues/h-0x04A8.png" class="uo-sprite" alt="Yew hue ramp" width="48" height="48" /> | `0x04A8` | 1192 | Yew |
| <img src="/img/hues/h-0x04A9.png" class="uo-sprite" alt="Heartwood hue ramp" width="48" height="48" /> | `0x04A9` | 1193 | Heartwood |
| <img src="/img/hues/h-0x04AA.png" class="uo-sprite" alt="Bloodwood hue ramp" width="48" height="48" /> | `0x04AA` | 1194 | Bloodwood |
| <img src="/img/hues/h-0x047F.png" class="uo-sprite" alt="Frostwood hue ramp" width="48" height="48" /> | `0x047F` | 1151 | Frostwood |

## 같은 스프라이트, 모든 금속

모든 주괴 색상은 **같은** 회색조 아트(아이템 `0x1BF2`)를 사용합니다. 바뀌는 것은 휴뿐입니다.
아래는 그 하나의 스프라이트를 아홉 번 그린 것입니다 — 평범한 Iron에 더해 여덟 가지 색 금속 — 재매핑이
어떻게 하나의 아트를 아홉 개의 뚜렷한 주괴로 바꾸는지 보여 주기 위해:

<img src="/img/items/0x1BF2.png" class="uo-sprite" alt="Iron ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0973.png" class="uo-sprite" alt="Dull Copper ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0966.png" class="uo-sprite" alt="Shadow Iron ingot" width="44" height="44" />
<img src="/img/hues/demo-0x096D.png" class="uo-sprite" alt="Copper ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0972.png" class="uo-sprite" alt="Bronze ingot" width="44" height="44" />
<img src="/img/hues/demo-0x08A5.png" class="uo-sprite" alt="Gold ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0979.png" class="uo-sprite" alt="Agapite ingot" width="44" height="44" />
<img src="/img/hues/demo-0x089F.png" class="uo-sprite" alt="Verite ingot" width="44" height="44" />
<img src="/img/hues/demo-0x08AB.png" class="uo-sprite" alt="Valorite ingot" width="44" height="44" />

*Iron, Dull Copper, Shadow Iron, Copper, Bronze, Gold, Agapite, Verite, Valorite —
하나의 스프라이트, 아홉 가지 휴.*

이 자원들이 어디서 오고 어떻게 쓰이는지 보려면, [자원 채집 가이드(Resources gathering
guide)](/ko/items/resources/)와 [자원 아이템 카탈로그(Resources item
catalog)](/ko/items/catalog/resources/)를 방문하세요.
