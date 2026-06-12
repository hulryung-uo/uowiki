---
title: 무기
description: 울티마 온라인에서 무기가 작동하는 방식 — 피해, 휘두르기 속도, 단련하는 스킬, 힘 요구치, 한손 대 양손, 특수 기술 — 그리고 모든 무기 계열에 대한 소스 검증 스탯 표.
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/*.cs"
  - "servuo: Scripts/Abilities/WeaponAbility.cs"
  - "uo-resource: tiledata.mul (weapon layer)"
  - "uowiki: data/weapons.json (extracted via tools/extract_weapons.py)"
last_verified: 2026-06-11
generated: false
---

당신의 무기는 근접 또는 원거리 캐릭터가 실제로 어떻게 싸우는지를 결정합니다: 얼마나 세게 때리는지,
얼마나 빠르게 휘두르는지, 어떤 **전투 스킬(combat skill)**을 단련하는지, 그리고 어떤 두 **특수
기술(special moves)**을 풀어낼 수 있는지. 이 페이지는 스탯을 설명한 뒤, ServUO 소스에 있는
**무기 135종** 전부에 대한 소스 검증 스탯 표를 계열별로 묶어 제공합니다.

:::tip
아래 스탯은 우리 샤드(EJ)가 쓰는 **AOS 시대** 값으로, 각 무기의 `.cs` 클래스에서 그대로 읽어왔습니다.
휘두르기 속도는 **초(seconds)** 단위로 표시됩니다(ML/EJ의 `MlSpeed` 값 — *낮을수록 빠름*). 시대별로
모든 무기를 아트와 함께 둘러보려면 [무기 카탈로그](/ko/items/catalog/weapons/)를 보세요.
:::

## 무기가 작동하는 방식

장착 가능한 모든 무기는 똑같은 몇 가지 스탯을 공유합니다. 이것들을 이해하는 것이 무기 고르기의
전부입니다.

### 피해 범위

각 무기는 **최소 및 최대 기본 피해**를 표시합니다(예: 카타나는 10–14). 휘두를 때마다 그 범위에서
무작위 값을 굴리고, 그 기본값은 명중 전에 크게 보정됩니다 — 당신의
**[전술(Tactics)](/ko/skills/tactics/)**과 **[해부학(Anatomy)](/ko/skills/anatomy/)** 스킬,
**힘(Strength)**, 무기의 피해 증가 속성, 그리고 대상의 저항에 의해. 표의 값은 *기본* 범위뿐입니다.
높은 전술과 해부학을 가진 GM 전사는 훨씬 더 큰 피해를 줍니다. 전체 피해 파이프라인은
[전투 기초](/ko/playing/combat-basics/)를, 기저 공식은 [메커니즘(Mechanics)](/ko/mechanics/)을
보세요.

### 무기 속도 (휘두르기 지연)

**Speed**는 얼마나 자주 공격할 수 있는지입니다. 우리 ML/EJ 샤드에서 각 무기는 초 단위 `MlSpeed`를
가지며 — 표가 이를 직접 보여줍니다 — **낮을수록 빠릅니다**(2.0초 단검은 4.5초 헤비 크로스보우보다
두 배 넘게 자주 휘두릅니다). 휘두르기 사이의 *실제* 지연은 당신의 **스태미나**와 장비의 **Swing
Speed Increase** 속성으로 짧아집니다 — 스태미나가 많을수록 더 빠르게 휘두르고, 전투 중 스태미나를
잃으면 느려집니다. 빠른 무기는 더 많은 타격을 명중시키므로 명중 시 효과(독, 흡수, 특수)를 더 자주
적용하고, 느린 무기는 각 일격에 더 많은 순수 피해를 담습니다. 스태미나와 휘두르기 속도 보너스가
어떻게 결합되는지는 [전투 고급](/ko/playing/combat-advanced/)을 보세요.

### 지배 스킬

각 무기는 클래스에 따라 정확히 하나의 **전투 스킬(combat skill)**을 단련합니다. 네 가지 근접 스킬과
두 가지 원거리 스킬은 다음과 같습니다.

- [**검술(Swordsmanship)**](/ko/skills/swordsmanship/) — 검, 도끼, 폴암
- [**둔기술(Mace Fighting)**](/ko/skills/mace-fighting/) — 메이스, 해머, 지팡이, 완드
- [**펜싱(Fencing)**](/ko/skills/fencing/) — 단검, 크리스, 창, 포크
- [**궁술(Archery)**](/ko/skills/archery/) — 활과 석궁
- **투척(Throwing)** — 가고일 투척 무기

당신의 전투 스킬은 **명중 확률(chance to hit)**을 지배합니다. **[전술(Tactics)](/ko/skills/tactics/)**과
**[해부학(Anatomy)](/ko/skills/anatomy/)**은 그다음 당신의 **피해**를 끌어올리며 *모든* 무기에
적용되는데, 그래서 거의 모든 근접 템플릿이 이것들을 챙깁니다
([7×GM 전사 템플릿](/ko/templates/seven-gm/) 참고). 일부 무기는 한 계열의 골격 위에 만들어졌지만 다른
스킬을 단련합니다 — 그런 것들은 표에 표시됩니다(<sup>Sw</sup> 검술, <sup>Fe</sup> 펜싱,
<sup>Ma</sup> 둔기술).

### 힘 요구치

각 무기는 **힘 요구치(Strength requirement)**를 가집니다. 요구치보다 낮은 상태로 무기를 장착하면
페널티를 받으며 휘두릅니다. 무거운 양손 무기(할버드, 워 해머, 헤비 크로스보우)는 힘 80–95를
요구하고, 가벼운 단검과 완드는 5–10만큼만 필요합니다.

### 한손 대 양손

**한손(one-handed)** 무기는 다른 손을 **방패**(방어술)나 주문서를 위해 비워둡니다. **양손
(two-handed)** 무기는 양손을 모두 차지합니다: **방패 불가, 그리고 빈 손이 필요한 시전을 막습니다**.
양손 무기는 이를 보상하기 위해 일반적으로 더 세게 때립니다. Hands 열은 **1H** 또는 **2H**를
보여줍니다.

### 피해 유형

무기는 계열에 묶인 기본 **피해 유형**을 가합니다: 검과 칼은 **베기(slash)**, 창과 크리스는
**찌르기(pierce)**, 메이스와 지팡이는 **타격(bash)**입니다. 피해 유형은 대상의 저항에 대해 대조되며,
마법 무기는 피해를 화염/냉기/독/에너지로 나눌 수 있습니다.

## 특수 기술

모든 무기는 두 **특수 기술(special moves)** — **주(primary)** 무기 능력과 **부(secondary)** 무기
능력 — 을 부여합니다. 전투 책이나 전투 모드 버튼에서 하나를 장전하면, 다음 조건을 만족하는 타격이
**마나**(그리고 때때로 스태미나)를 소모해 발동시킵니다. **주** 능력은 무기의 전투 스킬 70 부근에서,
**부** 능력은 90 부근에서 잠금 해제됩니다. 무기가 제공하는 두 능력은 클래스에 의해 고정되어
있습니다 — 무기를 고르는 것은 부분적으로 그 특수 기술을 고르는 일입니다. 발동, 마나 비용, 타이밍은
[전투 고급](/ko/playing/combat-advanced/)을 보세요.

흔한 능력들(`Scripts/Abilities/WeaponAbility.cs` 기준):

| Ability | 하는 일 |
|---|---|
| **Armor Ignore** | 대상의 방어구를 우회 — 피해는 낮지만 거의 온전히 명중. |
| **Bleed Attack** | 시간에 걸쳐 피해를 주는 출혈을 입힘. |
| **Concussion Blow** | 대상의 현재 마나에 비례하는 폭발 피해. |
| **Crushing Blow** | 대략 +50% 피해의 강한 일격. |
| **Disarm** | 대상의 손에서 무기를 떨어뜨림(빈 손이 필요). |
| **Dismount** | 탈것에 탄 대상을 떨어뜨림 — PvP의 필수 기술. |
| **Double Strike** | 한 동작에 두 번 휘두름. |
| **Infectious Strike** | 모든 충전을 소모하지 않고 무기의 독을 전달. |
| **Mortal Strike** | 대상에 상처를 입혀 몇 초간 치유가 실패하게 함. |
| **Moving Shot** | (원거리) 이동하면서 발사할 수 있게 함. |
| **Paralyzing Blow** | 대상을 잠시 제자리에 얼림. |
| **Shadow Strike** | 공격자를 잠깐 은신/스텔스시키는 타격. |
| **Whirlwind Attack** | 당신에게 인접한 *모든* 적을 한 번에 타격. |
| **Frenzied Whirlwind** | 주변 적을 반복적으로 타격하는 광역 공격. |
| **Riding Swipe** | 대상을 낙마시키고 탈것을 절뚝거리게 할 수 있음. |
| **Block / Defense Mastery** | 피해 감소를 올리는 방어 특수기. |
| **Feint** | 대상이 당신에게 주는 피해를 몇 초간 줄임. |
| **Dual Wield / Double Shot** | 특정 토쿠노 및 원거리 무기의 추가 휘두르기/추가 발사 특수기. |
| **Armor Pierce** | 명중 시 대상의 물리 저항을 낮춤. |
| **Bladeweave** | 명중 시 여러 능력 중 하나를 무작위로 발동. |
| **Force Arrow / Lightning Arrow / Serpent Arrow** | 원소 또는 마법 효과를 더하는 엘프 활 특수기. |
| **Psychic Attack** | 대상의 마나 비용을 올리고 피해 출력을 낮춤. |
| **Mystic Arc / Infused Throw** | 가고일 투척 특수기(곡선/다중 대상 투척). |

:::note
일부 무기(예: **Thin Longsword**)는 특수 기술을 정의하지 않아 엔진 기본값인 *없음*으로 떨어집니다 —
그런 무기는 Primary/Secondary 열에 "—"로 표시됩니다.
:::

## 무기 계열

아래 각 섹션은 그 계열의 전투 스킬, 플레이 스타일, 그리고 ServUO 소스에서 그대로 만든 스탯 표를
제공합니다. 표 범례: **Damage** = 기본 최소–최대; **Speed** = 휘두르기당 초(낮을수록 빠름);
**Hands** = 1H/2H; **Str** = 힘 요구치; 무기 이름 뒤의 표시는 <sup>G</sup> = 가고일 전용,
<sup>Sw/Fe/Ma</sup> = 계열 기본과 다른 스킬을 단련함을 뜻합니다.

제작 무기는 [대장기술(Blacksmithy)](/ko/crafting/blacksmithy/)(금속 무기)과
[활 제작(Bowfletching)](/ko/crafting/bowfletching/)(활, 석궁, 탄약)에서 나옵니다. 전체 아트 및
시대별 색인은 [무기 카탈로그](/ko/items/catalog/weapons/)를 보세요.

### Swords

**스킬:** [검술(Swordsmanship)](/ko/skills/swordsmanship/) · **무기 수:** 33

**검술(Swordsmanship)** 계열은 게임에서 가장 폭넓습니다: 빠른 한손 DPS를 위한 카타나와 롱소드,
양손 베기 무기, 그리고 깊은 사무라이(토쿠노)와 가고일 검 라인업. 대부분은 방패와 짝을 이루는 베기
피해 한손 무기입니다. 검으로 선언된 소수(크리스와 랜스 — <sup>Fe</sup> 표시)는 실제로는 **펜싱**을
단련합니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x08FE.png" class="uo-sprite" alt="" width="40" /> | Blood Blade <sup>G·Fe</sup> | 10–12 | 2s | 1H | 10 | Bleed Attack | Paralyzing Blow |
| <img src="/img/items/0x27A8.png" class="uo-sprite" alt="" width="40" /> | Bokuto | 10–12 | 2s | 1H | 20 | Feint | Nerve Strike |
| <img src="/img/items/0x26BB.png" class="uo-sprite" alt="" width="40" /> | Bone Harvester | 12–16 | 3s | 1H | 25 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x2D35.png" class="uo-sprite" alt="" width="40" /> | Bone Machete | 11–15 | 2.75s | 1H | 20 | Defense Mastery | Bladeweave |
| <img src="/img/items/0x0F5E.png" class="uo-sprite" alt="" width="40" /> | Broadsword | 13–17 | 3.25s | 1H | 30 | Crushing Blow | Armor Ignore |
| <img src="/img/items/0x26C1.png" class="uo-sprite" alt="" width="40" /> | Crescent Blade | 12–15 | 2.5s | 2H | 55 | Double Strike | Mortal Strike |
| <img src="/img/items/0x1441.png" class="uo-sprite" alt="" width="40" /> | Cutlass | 10–14 | 2.5s | 1H | 25 | Bleed Attack | Shadow Strike |
| <img src="/img/items/0x27A9.png" class="uo-sprite" alt="" width="40" /> | Daisho | 13–16 | 2.75s | 2H | 40 | Feint | Double Strike |
| <img src="/img/items/0x090B.png" class="uo-sprite" alt="" width="40" /> | Dread Sword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Crushing Blow | Concussion Blow |
| <img src="/img/items/0x2D35.png" class="uo-sprite" alt="" width="40" /> | Elven Machete | 11–15 | 2.75s | 1H | 20 | Defense Mastery | Bladeweave |
| <img src="/img/items/0x48C6.png" class="uo-sprite" alt="" width="40" /> | Gargish Bone Harvester <sup>G</sup> | 12–16 | 3s | 1H | 25 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x48D0.png" class="uo-sprite" alt="" width="40" /> | Gargish Daisho <sup>G</sup> | 13–16 | 2.75s | 2H | 40 | Feint | Double Strike |
| <img src="/img/items/0x48BA.png" class="uo-sprite" alt="" width="40" /> | Gargish Katana <sup>G</sup> | 10–14 | 2.5s | 1H | 25 | Double Strike | Armor Ignore |
| <img src="/img/items/0x48BC.png" class="uo-sprite" alt="" width="40" /> | Gargish Kryss <sup>G·Fe</sup> | 10–12 | 2s | 1H | 10 | Armor Ignore | Infectious Strike |
| <img src="/img/items/0x48CA.png" class="uo-sprite" alt="" width="40" /> | Gargish Lance <sup>G·Fe</sup> | 18–22 | 4.25s | 1H | 95 | Dismount | Concussion Blow |
| <img src="/img/items/0xA345.png" class="uo-sprite" alt="" width="40" /> | Gargish Skull Longsword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x0908.png" class="uo-sprite" alt="" width="40" /> | Gargish Talwar <sup>G</sup> | 16–19 | 3.5s | 2H | 40 | Whirlwind Attack | Dismount |
| <img src="/img/items/0x090C.png" class="uo-sprite" alt="" width="40" /> | Glass Sword <sup>G</sup> | 11–15 | 2.75s | 1H | 20 | Bleed Attack | Mortal Strike |
| <img src="/img/items/0x13FF.png" class="uo-sprite" alt="" width="40" /> | Katana | 10–14 | 2.5s | 1H | 25 | Double Strike | Armor Ignore |
| <img src="/img/items/0x1401.png" class="uo-sprite" alt="" width="40" /> | Kryss <sup>Fe</sup> | 10–12 | 2s | 1H | 10 | Armor Ignore | Infectious Strike |
| <img src="/img/items/0x26C0.png" class="uo-sprite" alt="" width="40" /> | Lance <sup>Fe</sup> | 18–22 | 4.25s | 1H | 95 | Dismount | Concussion Blow |
| <img src="/img/items/0x0F61.png" class="uo-sprite" alt="" width="40" /> | Longsword | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x27A2.png" class="uo-sprite" alt="" width="40" /> | No Dachi | 16–19 | 3.5s | 2H | 40 | Crushing Blow | Riding Swipe |
| <img src="/img/items/0x26CE.png" class="uo-sprite" alt="" width="40" /> | Paladin Sword | 20–24 | 5s | 1H | 85 | Whirlwind Attack | Disarm |
| <img src="/img/items/0x2D33.png" class="uo-sprite" alt="" width="40" /> | Radiant Scimitar | 10–14 | 2.5s | 1H | 20 | Whirlwind Attack | Bladeweave |
| <img src="/img/items/0x2D32.png" class="uo-sprite" alt="" width="40" /> | Rune Blade | 14–17 | 3s | 2H | 30 | Disarm | Bladeweave |
| <img src="/img/items/0x13B6.png" class="uo-sprite" alt="" width="40" /> | Scimitar | 12–16 | 3s | 1H | 25 | Double Strike | Paralyzing Blow |
| <img src="/img/items/0x0907.png" class="uo-sprite" alt="" width="40" /> | Shortblade <sup>G·Fe</sup> | 10–13 | 2.25s | 1H | 45 | Armor Ignore | Mortal Strike |
| <img src="/img/items/0xA341.png" class="uo-sprite" alt="" width="40" /> | Skull Longsword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x0900.png" class="uo-sprite" alt="" width="40" /> | Stone War Sword <sup>G</sup> | 15–19 | 3.75s | 1H | 40 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x13B8.png" class="uo-sprite" alt="" width="40" /> | Thin Longsword | 15–16 | 3.5s | 1H | 35 | — | — |
| <img src="/img/items/0x13B9.png" class="uo-sprite" alt="" width="40" /> | Viking Sword | 15–19 | 3.75s | 1H | 40 | Crushing Blow | Paralyzing Blow |
| <img src="/img/items/0x27A4.png" class="uo-sprite" alt="" width="40" /> | Wakizashi | 10–14 | 2.5s | 1H | 20 | Frenzied Whirlwind | Double Strike |


### Axes

**스킬:** [검술(Swordsmanship)](/ko/skills/swordsmanship/) · **무기 수:** 14

도끼도 **검술(Swordsmanship)**을 단련하지만 높은 피해와 힘 요구치를 가진 무거운 양손 무기로
기웁니다. 다수가 **벌목** 도구로도 쓰이며(hatchet, two-handed axe, large battle axe), 벌목꾼은 도끼
피해에 보너스를 받습니다. 워 액스(<sup>Ma</sup>)는 예외 — 둔기술을 단련합니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0F49.png" class="uo-sprite" alt="" width="40" /> | Axe | 14–17 | 3s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x0F47.png" class="uo-sprite" alt="" width="40" /> | Battle Axe | 16–19 | 3.5s | 2H | 35 | Bleed Attack | Concussion Blow |
| <img src="/img/items/0x0F4B.png" class="uo-sprite" alt="" width="40" /> | Double Axe | 15–18 | 3.25s | 2H | 45 | Double Strike | Whirlwind Attack |
| <img src="/img/items/0x08FD.png" class="uo-sprite" alt="" width="40" /> | Dual Short Axes <sup>G</sup> | 14–17 | 3s | 2H | 35 | Double Strike | Infectious Strike |
| <img src="/img/items/0x0F45.png" class="uo-sprite" alt="" width="40" /> | Executioners Axe | 15–18 | 3.25s | 2H | 40 | Bleed Attack | Mortal Strike |
| <img src="/img/items/0x48B2.png" class="uo-sprite" alt="" width="40" /> | Gargish Axe <sup>G</sup> | 14–17 | 3s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x48B0.png" class="uo-sprite" alt="" width="40" /> | Gargish Battle Axe <sup>G</sup> | 16–19 | 3.5s | 2H | 35 | Bleed Attack | Concussion Blow |
| <img src="/img/items/0x0F43.png" class="uo-sprite" alt="" width="40" /> | Hatchet | 13–16 | 2.75s | 2H | 20 | Armor Ignore | Disarm |
| <img src="/img/items/0x2D28.png" class="uo-sprite" alt="" width="40" /> | Heavy Ornate Axe | 17–20 | 3.75s | 2H | 45 | Disarm | Crushing Blow |
| <img src="/img/items/0x13FB.png" class="uo-sprite" alt="" width="40" /> | Large Battle Axe | 17–20 | 3.75s | 2H | 80 | Whirlwind Attack | Bleed Attack |
| <img src="/img/items/0x2D28.png" class="uo-sprite" alt="" width="40" /> | Ornate Axe | 17–20 | 3.75s | 2H | 45 | Disarm | Crushing Blow |
| <img src="/img/items/0x0E86.png" class="uo-sprite" alt="" width="40" /> | Pickaxe | 12–16 | 3s | 1H | 50 | Double Strike | Disarm |
| <img src="/img/items/0x1443.png" class="uo-sprite" alt="" width="40" /> | Two Handed Axe | 16–19 | 3.5s | 2H | 40 | Double Strike | Shadow Strike |
| <img src="/img/items/0x13B0.png" class="uo-sprite" alt="" width="40" /> | War Axe <sup>Ma</sup> | 12–16 | 3s | 1H | 35 | Armor Ignore | Bleed Attack |


### Maces & Hammers

**스킬:** [둔기술(Mace Fighting)](/ko/skills/mace-fighting/) · **무기 수:** 20

메이스는 **둔기술(Mace Fighting)**을 단련하며 타격 피해를 줍니다. 그 특징적인 성질: 플레이어를
상대로 메이스 무기는 스태미나에 피해를 주고 (구버전 규칙에서는) 방어구의 일부를 무시할 수 있습니다.
가벼운 클럽부터 잔혹한 양손 워 해머까지 다양합니다. 몇몇 장식용 "완드" 아이템(매직 완드 / 폭죽
완드)은 실제로는 타격 무기여서 완드 계열이 아니라 여기에 있습니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | A Fireworks Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x13B4.png" class="uo-sprite" alt="" width="40" /> | Club | 10–14 | 2.5s | 1H | 40 | Crushing Blow | Dismount |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Diamond Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x0903.png" class="uo-sprite" alt="" width="40" /> | Disc Mace <sup>G</sup> | 11–15 | 2.75s | 1H | 45 | Armor Ignore | Disarm |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Emerald Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x48C2.png" class="uo-sprite" alt="" width="40" /> | Gargish Maul <sup>G</sup> | 14–18 | 3.5s | 1H | 45 | Double Strike | Concussion Blow |
| <img src="/img/items/0x48CC.png" class="uo-sprite" alt="" width="40" /> | Gargish Tessen <sup>G</sup> | 10–13 | 2s | 2H | 10 | Feint | Dual Wield |
| <img src="/img/items/0x48C0.png" class="uo-sprite" alt="" width="40" /> | Gargish War Hammer <sup>G</sup> | 17–20 | 3.75s | 2H | 95 | Whirlwind Attack | Crushing Blow |
| <img src="/img/items/0x143D.png" class="uo-sprite" alt="" width="40" /> | Hammer Pick | 13–17 | 3.25s | 1H | 45 | Armor Ignore | Mortal Strike |
| <img src="/img/items/0x0F5C.png" class="uo-sprite" alt="" width="40" /> | Mace | 11–15 | 2.75s | 1H | 45 | Concussion Blow | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Magic Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x143B.png" class="uo-sprite" alt="" width="40" /> | Maul | 14–18 | 3.5s | 1H | 45 | Double Strike | Concussion Blow |
| <img src="/img/items/0x27AE.png" class="uo-sprite" alt="" width="40" /> | Nunchaku | 12–15 | 2.5s | 2H | 15 | Block | Double Strike |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Ruby Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x26BC.png" class="uo-sprite" alt="" width="40" /> | Scepter | 14–18 | 3.5s | 1H | 40 | Crushing Blow | Mortal Strike |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Silver-Etched Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x27A3.png" class="uo-sprite" alt="" width="40" /> | Tessen | 10–13 | 2s | 2H | 10 | Feint | Dual Wield |
| <img src="/img/items/0x27A6.png" class="uo-sprite" alt="" width="40" /> | Tetsubo | 12–15 | 2.5s | 2H | 35 | Frenzied Whirlwind | Crushing Blow |
| <img src="/img/items/0x1439.png" class="uo-sprite" alt="" width="40" /> | War Hammer | 17–20 | 3.75s | 2H | 95 | Whirlwind Attack | Crushing Blow |
| <img src="/img/items/0x1407.png" class="uo-sprite" alt="" width="40" /> | War Mace | 16–20 | 4s | 1H | 80 | Crushing Blow | Mortal Strike |


### Staves

**스킬:** [둔기술(Mace Fighting)](/ko/skills/mace-fighting/) · **무기 수:** 10

쿼터스태프, 그날드 스태프, 블랙 스태프는 양손 **둔기술(Mace Fighting)** 무기입니다. 양손 지팡이
아트가 특정 시전자 빌드를 여전히 허용하기 때문에 메이지와 테이머에게 인기가 있고, 여러 그날드
스태프는 가고일의 *Force of Nature* 특수기를 가집니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF0.png" class="uo-sprite" alt="" width="40" /> | Black Staff | 13–16 | 2.75s | 2H | 35 | Whirlwind Attack | Paralyzing Blow |
| <img src="/img/items/0x48B8.png" class="uo-sprite" alt="" width="40" /> | Gargish Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0xA347.png" class="uo-sprite" alt="" width="40" /> | Gargish Skull Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x0905.png" class="uo-sprite" alt="" width="40" /> | Glass Staff <sup>G</sup> | 11–14 | 2.25s | 2H | 20 | Double Strike | Mortal Strike |
| <img src="/img/items/0x13F8.png" class="uo-sprite" alt="" width="40" /> | Gnarled Staff | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x0E89.png" class="uo-sprite" alt="" width="40" /> | Quarter Staff | 11–14 | 2.25s | 2H | 30 | Double Strike | Concussion Blow |
| <img src="/img/items/0x0906.png" class="uo-sprite" alt="" width="40" /> | Serpent Stone Staff <sup>G</sup> | 16–19 | 3.5s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x0E81.png" class="uo-sprite" alt="" width="40" /> | Shepherds Crook | 13–16 | 2.75s | 2H | 20 | Crushing Blow | Disarm |
| <img src="/img/items/0xA343.png" class="uo-sprite" alt="" width="40" /> | Skull Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x2D25.png" class="uo-sprite" alt="" width="40" /> | Wild Staff | 10–13 | 2.25s | 1H | 15 | Block | Force of Nature |


### Daggers & Knives

**스킬:** [펜싱(Fencing)](/ko/skills/fencing/) · **무기 수:** 17

가볍고 매우 빠른 **펜싱(Fencing)** 무기. 단검은 게임에서 무엇과도 견줄 만큼 빠르게 휘둘러지며 독과
Infectious Strike 특수기를 적용하는 데 뛰어납니다. 도축용 칼(butcher knife, cleaver, skinning knife
— <sup>Sw</sup> 표시)은 칼 모양이지만 **검술**을 단련하며 가죽 벗기기 도구로도 쓰입니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x2D21.png" class="uo-sprite" alt="" width="40" /> | Assassin Spike | 10–12 | 2s | 1H | 15 | Infectious Strike | Shadow Strike |
| <img src="/img/items/0x13F6.png" class="uo-sprite" alt="" width="40" /> | Butcher Knife <sup>Sw</sup> | 10–13 | 2.25s | 1H | 10 | Infectious Strike | Disarm |
| <img src="/img/items/0x0EC3.png" class="uo-sprite" alt="" width="40" /> | Cleaver <sup>Sw</sup> | 10–14 | 2.5s | 1H | 10 | Bleed Attack | Infectious Strike |
| <img src="/img/items/0x0F52.png" class="uo-sprite" alt="" width="40" /> | Dagger | 10–12 | 2s | 1H | 10 | Shadow Strike | Infectious Strike |
| <img src="/img/items/0x2D20.png" class="uo-sprite" alt="" width="40" /> | Elven Spellblade | 12–15 | 2.5s | 2H | 35 | Psychic Attack | Bleed Attack |
| <img src="/img/items/0x48B6.png" class="uo-sprite" alt="" width="40" /> | Gargish Butcher Knife <sup>G·Sw</sup> | 10–13 | 2.25s | 1H | 10 | Infectious Strike | Disarm |
| <img src="/img/items/0x48AE.png" class="uo-sprite" alt="" width="40" /> | Gargish Cleaver <sup>G·Sw</sup> | 10–14 | 2.5s | 1H | 10 | Bleed Attack | Infectious Strike |
| <img src="/img/items/0x0902.png" class="uo-sprite" alt="" width="40" /> | Gargish Dagger <sup>G</sup> | 10–12 | 2s | 1H | 10 | Shadow Strike | Infectious Strike |
| <img src="/img/items/0x48CE.png" class="uo-sprite" alt="" width="40" /> | Gargish Tekagi <sup>G</sup> | 10–13 | 2s | 2H | 10 | Dual Wield | Talon Strike |
| <img src="/img/items/0x27AD.png" class="uo-sprite" alt="" width="40" /> | Kama | 10–13 | 2s | 2H | 15 | Whirlwind Attack | Defense Mastery |
| <img src="/img/items/0x27A7.png" class="uo-sprite" alt="" width="40" /> | Lajatang | 16–19 | 3.5s | 2H | 65 | Defense Mastery | Frenzied Whirlwind |
| <img src="/img/items/0x2D22.png" class="uo-sprite" alt="" width="40" /> | Leafblade | 11–15 | 2.75s | 1H | 20 | Feint | Armor Ignore |
| <img src="/img/items/0x27AF.png" class="uo-sprite" alt="" width="40" /> | Sai | 10–13 | 2s | 2H | 15 | Dual Wield | Armor Pierce |
| <img src="/img/items/0x2D2F.png" class="uo-sprite" alt="" width="40" /> | Serrated War Cleaver | 10–13 | 2.25s | 2H | 15 | Disarm | Bladeweave |
| <img src="/img/items/0x0EC4.png" class="uo-sprite" alt="" width="40" /> | Skinning Knife <sup>Sw</sup> | 10–13 | 2.25s | 1H | 5 | Shadow Strike | Bleed Attack |
| <img src="/img/items/0x27AB.png" class="uo-sprite" alt="" width="40" /> | Tekagi | 10–13 | 2s | 2H | 10 | Dual Wield | Talon Strike |
| <img src="/img/items/0x2D2F.png" class="uo-sprite" alt="" width="40" /> | War Cleaver | 10–13 | 2.25s | 2H | 15 | Disarm | Bladeweave |


### Spears & Forks

**스킬:** [펜싱(Fencing)](/ko/skills/fencing/) · **무기 수:** 11

창, 파이크, 워 포크는 찌르기 **펜싱(Fencing)** 무기로, 대부분 양손이며 사거리형 피해가 좋습니다.
블레이디드 스태프(<sup>Sw</sup>)는 창 골격 위에 만들어졌지만 검술을 단련합니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x26BD.png" class="uo-sprite" alt="" width="40" /> | Bladed Staff <sup>Sw</sup> | 14–17 | 3s | 2H | 40 | Armor Ignore | Dismount |
| <img src="/img/items/0x26BF.png" class="uo-sprite" alt="" width="40" /> | Double Bladed Staff | 11–14 | 2.25s | 2H | 50 | Double Strike | Infectious Strike |
| <img src="/img/items/0x0904.png" class="uo-sprite" alt="" width="40" /> | Dual Pointed Spear <sup>G</sup> | 11–14 | 2.25s | 2H | 50 | Double Strike | Disarm |
| <img src="/img/items/0x48C8.png" class="uo-sprite" alt="" width="40" /> | Gargish Pike <sup>G</sup> | 14–17 | 3s | 2H | 50 | Paralyzing Blow | Infectious Strike |
| <img src="/img/items/0x48BE.png" class="uo-sprite" alt="" width="40" /> | Gargish War Fork <sup>G</sup> | 10–14 | 2.5s | 1H | 45 | Bleed Attack | Disarm |
| <img src="/img/items/0x26BE.png" class="uo-sprite" alt="" width="40" /> | Pike | 14–17 | 3s | 2H | 50 | Paralyzing Blow | Infectious Strike |
| <img src="/img/items/0x0E87.png" class="uo-sprite" alt="" width="40" /> | Pitchfork | 12–15 | 2.5s | 2H | 55 | Bleed Attack | Dismount |
| <img src="/img/items/0x1403.png" class="uo-sprite" alt="" width="40" /> | Short Spear | 10–13 | 2s | 2H | 40 | Shadow Strike | Mortal Strike |
| <img src="/img/items/0x0F62.png" class="uo-sprite" alt="" width="40" /> | Spear | 13–16 | 2.75s | 2H | 50 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x0F62.png" class="uo-sprite" alt="" width="40" /> | Tribal Spear | 13–15 | 2.75s | 2H | 50 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x1405.png" class="uo-sprite" alt="" width="40" /> | War Fork | 10–14 | 2.5s | 1H | 45 | Bleed Attack | Disarm |


### Polearms

**스킬:** [검술(Swordsmanship)](/ko/skills/swordsmanship/) · **무기 수:** 5

바르디슈, 할버드, 사이드는 거대한 양손 **검술(Swordsmanship)** 폴암입니다 — 근접에서 가장 높은 기본
피해와 힘 요구치를 가지며, 느린 휘두르기 속도와 맞바꿉니다. 휘둘러치기/광역 피해의 핵심 무기입니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0F4D.png" class="uo-sprite" alt="" width="40" /> | Bardiche | 17–20 | 3.75s | 2H | 45 | Paralyzing Blow | Dismount |
| <img src="/img/items/0x48B4.png" class="uo-sprite" alt="" width="40" /> | Gargish Bardiche <sup>G</sup> | 17–20 | 3.75s | 2H | 45 | Paralyzing Blow | Dismount |
| <img src="/img/items/0x48C4.png" class="uo-sprite" alt="" width="40" /> | Gargish Scythe <sup>G</sup> | 16–19 | 3.5s | 2H | 45 | Bleed Attack | Paralyzing Blow |
| <img src="/img/items/0x143E.png" class="uo-sprite" alt="" width="40" /> | Halberd | 18–21 | 4s | 2H | 95 | Whirlwind Attack | Concussion Blow |
| <img src="/img/items/0x26BA.png" class="uo-sprite" alt="" width="40" /> | Scythe | 16–19 | 3.5s | 2H | 45 | Bleed Attack | Paralyzing Blow |


### Bows & Crossbows

**스킬:** [궁술(Archery)](/ko/skills/archery/) · **무기 수:** 11

원거리 **궁술(Archery)** 무기. 모든 활과 석궁은 양손이고, 빈 손이 필요하며(방패 불가), 탄약을
소모합니다 — 활에는 화살, 석궁에는 볼트. 무거운 석궁은 더 세게 때리지만 느리게 휘두르고, 연발
석궁과 단궁은 피해를 속도와 맞바꿉니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | An Orcish Bow | 17–21 | 4.25s | 2H | 30 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | Bow | 17–21 | 4.25s | 2H | 30 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x26C2.png" class="uo-sprite" alt="" width="40" /> | Composite Bow | 16–20 | 4s | 2H | 45 | Armor Ignore | Moving Shot |
| <img src="/img/items/0x0F50.png" class="uo-sprite" alt="" width="40" /> | Crossbow | 18–22 | 4.5s | 2H | 35 | Concussion Blow | Mortal Strike |
| <img src="/img/items/0x2D1E.png" class="uo-sprite" alt="" width="40" /> | Elven Composite Longbow | 15–19 | 3.75s | 2H | 45 | Force Arrow | Serpent Arrow |
| <img src="/img/items/0x13FD.png" class="uo-sprite" alt="" width="40" /> | Heavy Crossbow | 20–24 | 5s | 2H | 80 | Moving Shot | Dismount |
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | Juka Bow | 17–21 | 4.25s | 2H | 100 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x2D2B.png" class="uo-sprite" alt="" width="40" /> | Lightweight Shortbow | 12–16 | 3s | 2H | 45 | Lightning Arrow | Psychic Attack |
| <img src="/img/items/0x2D2B.png" class="uo-sprite" alt="" width="40" /> | Magical Shortbow | 12–16 | 3s | 2H | 45 | Lightning Arrow | Psychic Attack |
| <img src="/img/items/0x26C3.png" class="uo-sprite" alt="" width="40" /> | Repeating Crossbow | 11–15 | 2.75s | 2H | 30 | Double Strike | Moving Shot |
| <img src="/img/items/0x27A5.png" class="uo-sprite" alt="" width="40" /> | Yumi | 13–17 | 3.25s | 2H | 35 | Armor Pierce | Double Shot |


### Thrown

**스킬:** [투척(Throwing)](/ko/skills/throwing/) · **무기 수:** 3

가고일 전용 **투척(Throwing)** 무기(부메랑, 사이클론, 소울 글레이브). 궁술처럼 원거리로 던지지만
투척 스킬의 지배를 받으며 추가 사거리를 위해 힘의 도움을 받습니다. 한손.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x08FF.png" class="uo-sprite" alt="" width="40" /> | Boomerang <sup>G</sup> | 11–15 | 2.75s | 1H | 25 | Mystic Arc | Concussion Blow |
| <img src="/img/items/0x0901.png" class="uo-sprite" alt="" width="40" /> | Cyclone <sup>G</sup> | 13–17 | 3.25s | 1H | 40 | Moving Shot | Infused Throw |
| <img src="/img/items/0x090A.png" class="uo-sprite" alt="" width="40" /> | Soul Glaive <sup>G</sup> | 16–20 | 4s | 1H | 60 | Armor Ignore | Mortal Strike |


### Wands

**스킬:** [둔기술(Mace Fighting)](/ko/skills/mace-fighting/) · **무기 수:** 11

완드는 마법 충전(Heal, Harm, Fireball 등)도 담는 한손 **둔기술(Mace Fighting)** 무기입니다. 근접
무기로서는 한결같이 약하며(9–11 피해, 낮은 힘 요구치) `BaseWand`에서 상속받은 Dismount/Disarm 특수기
세트를 가집니다. 그 가치는 휘두르기가 아니라 주문 충전에 있습니다.

| Icon | Weapon | Damage | Speed | Hands | Str | Primary | Secondary |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Clumsy Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Feeble Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Fireball Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Greater Heal Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Harm Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Heal Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Id Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Lightning Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Magic Arrow Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Mana Drain Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Weakness Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |


## 함께 보기

- [전투 기초](/ko/playing/combat-basics/)와 [전투 고급](/ko/playing/combat-advanced/) — 휘두르기, 명중 확률, 피해, 특수기가 어떻게 결정되는지
- [검술(Swordsmanship)](/ko/skills/swordsmanship/) · [둔기술(Mace Fighting)](/ko/skills/mace-fighting/) · [펜싱(Fencing)](/ko/skills/fencing/) · [궁술(Archery)](/ko/skills/archery/) — 전투 스킬들
- [전술(Tactics)](/ko/skills/tactics/)과 [해부학(Anatomy)](/ko/skills/anatomy/) — 모든 전사가 챙기는 보편적 피해 스킬
- [7×GM 전사 템플릿](/ko/templates/seven-gm/) — 완성된 근접 빌드
- [대장기술(Blacksmithy)](/ko/crafting/blacksmithy/)과 [활 제작(Bowfletching)](/ko/crafting/bowfletching/) — 자신의 무기 제작하기
- [무기 카탈로그](/ko/items/catalog/weapons/) — 시대별 모든 무기와 아트, 아이템 ID
