---
title: 페이퍼돌(Paperdoll)
description: 캐릭터의 페이퍼돌이 어떻게 구성되는가 — 슬롯 순서대로 그려지고 아이템 휴로 색이 입혀지는, 장비 검프가 겹쳐진 나체 몸체 검프.
status: source-verified
sources:
  - "client: gumpartLegacyMUL.uop, tiledata.mul"
  - "classicuo: PaperDollInteractable.cs"
last_verified: 2026-06-11
generated: false
---

**페이퍼돌(paperdoll)**은 자신을 더블클릭할 때 나타나는, 머리부터 발끝까지의 캐릭터 초상입니다.
이것은 단일 이미지가 아닙니다: 클라이언트가 나체 몸체 그림에 장착 아이템마다 그림 하나씩을 더해 즉석에서
*합성*하므로, 당신이 무엇을 입든 입은 채로 나타납니다. 이 페이지는 그 합성이 어떻게 작동하는지
설명하고 다양한 방어구와 의류에 대한 결과를 보여 줍니다.

## 페이퍼돌이 어떻게 구성되는가

클라이언트는 고정된 레시피를 따릅니다(ClassicUO의 `PaperDollInteractable.cs`와
`Game/Constants.cs`에서 검증됨):

1. **몸체를 그립니다.** 반나체 몸체 검프가 먼저 왼쪽 위 모서리에 깔립니다: 인간 남성은 검프
   `0x000C`, 인간 여성은 `0x000D`.
2. **각 아이템의 검프를 찾습니다.** 모든 착용 가능 아이템은 클라이언트의 `tiledata.mul`에
   **AnimID**를 지닙니다. 그 페이퍼돌 그림은 남성 돌의 경우 id가 `AnimID + 50000`인 검프,
   여성 돌의 경우 `AnimID + 60000`인 검프입니다. 여성 전용 검프가 존재하지 않으면, 클라이언트는
   남성 것으로 대체합니다.
3. **장비를 몸체 위에 겹칩니다.** 각 장비 검프는 같은 왼쪽 위 모서리에 그려지며 — 아트 자체가 이미
   돌 위의 올바른 위치를 담고 있습니다 — 투명도를 적용해 합성됩니다. 고정된 **레이어 순서(layer
   order)**로 뒤에서 앞으로 그려집니다:

   > Cloak, Shirt, Pants, Shoes, Legs, Arms, Torso, Tunic, Ring, Bracelet, Face,
   > Gloves, Skirt, Robe, Waist, Necklace, Hair, Beard, Earrings, Helmet,
   > One-Handed, Two-Handed, Talisman

   이 순서가 흉갑(breastplate)이 그 아래의 가죽을 덮는 이유이고, 투구가 머리카락 위에 그려지는
   이유입니다.
4. **휴로 색을 입힙니다.** 방어구와 의류 아트는 회색조입니다; 아이템의 **휴(hue)**가 마지막에
   적용되어, 그 회색 램프를 [휴 팔레트(hue palette)](/ko/reference/hues/)를 통해 재매핑함으로써
   염색된 로브나 색 금속 슈트가 그 색을 보이게 합니다.

아래 이미지들은 바로 그 검프들을 합성해 생성한 것이므로, 게임 속 페이퍼돌이 렌더링하는 것과
일치합니다.

## 나체 몸체

이것들은 모든 페이퍼돌이 시작하는 기본 몸체 검프입니다. 아트는 회색조입니다; 클라이언트는 캐릭터의
**피부 휴(skin hue)**로 색을 입힙니다(ServUO는 `RandomSkinHue` 범위, 게임 휴 1002–1058에서
하나를 굴립니다). 아래 인물들은 검프의 날것 그대로의 회색이 아니라 살로 읽히도록 대표적인 인간 피부
톤(휴 1024)으로 색이 입혀졌습니다.

<img src="/img/paperdoll/body-male.png" width="220" alt="Skin-toned male human body paperdoll (gump 0x000C)" />
<img src="/img/paperdoll/body-female.png" width="220" alt="Skin-toned female human body paperdoll (gump 0x000D)" />

*남성 몸체 `0x000C`(왼쪽)와 여성 몸체 `0x000D`(오른쪽), 피부 휴 1024로 색 입힘.*

## 재질별 방어구

아래 각 슈트는 그 재질의 표준 부위(가슴, 팔, 다리, 장갑, 목가리개/투구 — 재질이 가진 것 무엇이든)로
겹친 피부톤 남성 몸체이며, 슬롯 순서로 그려지고 각 부위 자체의 휴로 색이 입혀졌습니다. 전체 세트는
[방어구 카탈로그(armor catalog)](/ko/items/catalog/armor/)에서 둘러보세요; 방패는 자체
[방패 카탈로그(shield catalog)](/ko/items/catalog/shields/)가 있습니다.

### 가죽(Leather)

<img src="/img/paperdoll/suit-leather.png" width="220" alt="Full leather armor worn on a male body" />

*가슴, 팔, 다리, 장갑, 목가리개, 모자.*

### 스터디드 레더(Studded leather)

<img src="/img/paperdoll/suit-studded.png" width="220" alt="Full studded leather armor worn on a male body" />

*가슴, 팔, 다리, 장갑, 목가리개.*

### 본(Bone)

<img src="/img/paperdoll/suit-bone.png" width="220" alt="Full bone armor worn on a male body" />

*가슴, 팔, 다리, 장갑, 투구 — 창백한 뼈 색조로.*

### 링메일(Ringmail)

<img src="/img/paperdoll/suit-ringmail.png" width="220" alt="Full ringmail armor worn on a male body" />

*가슴, 팔, 다리, 장갑.*

### 체인메일(Chainmail)

<img src="/img/paperdoll/suit-chainmail.png" width="220" alt="Full chainmail armor worn on a male body" />

*가슴, 다리, 코이프(coif).*

### 플레이트메일(Platemail)

<img src="/img/paperdoll/suit-plate.png" width="220" alt="Full plate armor worn on a male body" />

*가슴, 팔, 다리, 장갑, 목가리개, 투구 — 고전적인 풀 플레이트.*

### 드래곤 스케일(Dragon scale)

<img src="/img/paperdoll/suit-dragon.png" width="220" alt="Full dragon-scale armor worn on a male body" />

*가슴, 팔, 다리, 장갑, 투구 — 드래곤 비늘의 구워진 휴를 지님.*

### 하이드(Hide)

<img src="/img/paperdoll/suit-hide.png" width="220" alt="Full hide armor worn on a male body" />

*가슴, 폴드론(어깨, 팔), 바지, 장갑, 목가리개.*

### 우드랜드(Woodland)

<img src="/img/paperdoll/suit-woodland.png" width="220" alt="Full woodland armor worn on a male body" />

*가슴, 팔, 다리, 장갑, 목가리개 — 엘프의 heartwood 세트.*

### 가고일 가죽(Gargish leather)

<img src="/img/paperdoll/suit-gargish-leather.png" width="220" alt="Full gargish leather armor worn on a male body" />

*가슴, 팔, 다리, 킬트(kilt).*

### 가고일 플레이트(Gargish plate)

<img src="/img/paperdoll/suit-gargish-plate.png" width="220" alt="Full gargish plate armor worn on a male body" />

*가슴, 팔, 다리, 킬트.*

### 가고일 스톤(Gargish stone)

<img src="/img/paperdoll/suit-gargish-stone.png" width="220" alt="Full gargish stone armor worn on a male body" />

*가슴, 팔, 다리, 킬트 — 깎은 돌 색조로.*

### 사무라이 플레이트(Samurai plate)

<img src="/img/paperdoll/suit-samurai-plate.png" width="220" alt="Full samurai plate armor worn on a male body" />

*도(do, 가슴), 하이다테(haidate, 허벅지 보호구), 스네아테(suneate, 다리 보호구), 멘포(mempo,
얼굴), 그리고 플레이트 가부토(kabuto) 투구.*

### 방패를 든 플레이트(Plate with a shield)

<img src="/img/paperdoll/suit-shield.png" width="220" alt="Full plate armor with a metal shield worn on a male body" />

*보조 손에 금속 방패를 든 풀 플레이트 슈트 — 방패는 한손(one-handed) 레이어에 그려집니다.*

## 의류 차림새

천 부위는 같은 합성을 사용합니다 — 여기서는 평범한 로브, 긴 바지에 멋진 셔츠, 그리고 로브와 모자의
마법사 룩. 전체 범위는 [의류 카탈로그(clothing catalog)](/ko/items/catalog/clothing/)를
보세요.

<img src="/img/paperdoll/suit-robe.png" width="220" alt="A robe worn on a male body" />
<img src="/img/paperdoll/suit-fancy-shirt-and-pants.png" width="220" alt="A fancy shirt and long pants worn on a male body" />
<img src="/img/paperdoll/suit-wizard.png" width="220" alt="A robe and wizard's hat worn on a male body" />

*로브, 멋진 셔츠 + 긴 바지, 그리고 마법사 룩(로브 + 위저드 햇).*

## 단일 장착 아이템

한 번에 한 부위씩 보기 위해, 여기 단일 아이템을 장착한 몸체가 있습니다. 마지막 셋은 같은 기본
아트를 서로 다른 [휴(hues)](/ko/reference/hues/)로 색 입힌 것을 보여 줍니다.

<img src="/img/paperdoll/item-plate-chest.png" width="220" alt="A plate chest worn on a male body" />
<img src="/img/paperdoll/item-dragon-helm.png" width="220" alt="A dragon helm worn on a male body" />
<img src="/img/paperdoll/item-bone-chest.png" width="220" alt="A bone chest worn on a male body" />

*플레이트 가슴, 드래곤 투구, 본 가슴.*

<img src="/img/paperdoll/item-robe-blue.png" width="220" alt="A blue-dyed robe worn on a male body" />
<img src="/img/paperdoll/item-robe-red.png" width="220" alt="A red-dyed robe worn on a male body" />
<img src="/img/paperdoll/item-wizards-hat-green.png" width="220" alt="A green-dyed wizard's hat worn on a male body" />

*같은 로브를 파랑과 빨강으로, 그리고 초록 위저드 햇 — 하나의 회색조 검프가 그 휴를 통해 어떻게 어떤
색이든 되는지 보여 줌.*
