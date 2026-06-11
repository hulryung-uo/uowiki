---
title: 독 & 상태 효과
description: 독의 단계와 치료, 그리고 마비, 출혈, 필살 일격, 허기, 저주 — 각각이 어떻게 작동하고 어떻게 제거하는지.
status: unverified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (bandage cure thresholds and poison-level scaling)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

이 페이지는 캐릭터에게 영향을 주는 해로운 상태와 각각을 해소하는 방법을 다룹니다.
치료 방법은 [치료(Healing)](/ko/playing/healing/)에서 자세히 다루며, 전투로 인해 적용되는
효과는 [전투(고급)](/ko/playing/combat-advanced/)에 있습니다.

## 독 (Poison)

**독(Poison)**은 시간에 따라 지속 피해를 입힙니다: 한 번 중독되면 치료하거나 효과가 사라질
때까지 작은 **틱(tick)** 단위의 피해를 반복적으로 받습니다. 독의 단계가 높을수록 틱 피해가
강하고 치료에 더 저항합니다.

### 독의 단계

독은 약한 것부터 강한 것까지 단계가 점점 높아집니다:

1. **Lesser(약한 독)**
2. **Regular(일반 독)**
3. **Greater(강한 독)**
4. **Deadly(치명적인 독)**
5. **Lethal(치사 독)** (크리처/특수 — 가장 강함; 입수 가능 여부는 샤드에 따라 다름, 미검증)

단계가 높을수록 틱당 피해가 크고 **치료하기가 더 어렵습니다** — 치료 확률은 `Bandage.cs`에서
명시적으로 독 단계로 나눠집니다.

### 중독되는 경로

- **몬스터** — 많은 크리처가 타격 시 또는 독 공격으로 중독시킵니다(어떤 몬스터가 어느 단계로
  중독시키는지는 [몬스터 도감(Bestiary)](/ko/bestiary/)을 참고하세요).
- **독이 묻은 무기** — [독 바르기(Poisoning)](/ko/skills/poisoning/)로 칼날에 독을 바른
  플레이어는 당신을 타격할 때 중독시킬 수 있습니다.
- **함정** — 독 함정이 걸린 상자/컨테이너(see [함정 해제(Remove Trap)](/ko/skills/remove-trap/)
  와 [자물쇠 따기(Lockpicking)](/ko/skills/lockpicking/)).
- **음식/음료** — 독이 든 무언가를 먹으면 중독될 수 있습니다
  ([음식 & 음료](/ko/items/catalog/food-drink/)).

### 독을 치료하는 방법

**독을 제거하려면 다음 중 하나를 사용하세요:**

- **붕대(Bandage)** — [치료(Healing)](/ko/skills/healing/) **≥ 60** 과
  [해부학(Anatomy)](/ko/skills/anatomy/) **≥ 60** 이 모두 필요합니다(검증됨, `Bandage.cs`);
  치료 확률 = `(Healing − 30)/50 − (PoisonLevel × 0.1) − (Slips × 0.02)`. 붕대를 더블클릭 →
  중독된 사람을 타겟합니다.
- **치료 주문(Cure spell)** — 2서클 [마법(Magery)](/ko/skills/magery/) 치료; 또는 영역을
  치료하려면 **Arch Cure(대치료)** (4서클).
- **치료 물약(Cure potion)** — 즉시 효과; 더 강한 물약일수록 더 높은 단계를 치료합니다(효과
  **미검증**). [물약(potions)](/ko/items/catalog/potions/)을 참고하세요.
- **Arch Cure / Chivalry Cleanse / Mysticism cure** — 스킬에 따라 사용할 수 있는 대체 치료
  수단(입수 가능 여부 미검증).

**중요:** 약한 **Heal/Greater Heal** 주문은 **중독된 대상의 HP를 치료하지 못합니다** —
반드시 **먼저 치료(cure)**한 다음 HP를 회복해야 합니다. 붕대로는 계속 적용할 수 있는데,
중독된 환자에게 쓴 붕대는 치료(HP 회복)에 앞서 해독을 먼저 시도합니다. 자세한 내용은
[치료(Healing)](/ko/playing/healing/)에 있습니다.

## 마비 (Paralysis)

**마비된(Paralyzed)** 캐릭터는 지속 시간 동안 움직이거나 행동할 수 없습니다.

- **원인:** **Paralyze(마비)** 주문([마법(Magery)](/ko/skills/magery/) 5서클),
  **Paralyze Field(마비 장판)**, **paralyzing blow(마비 일격)** 무기 특수, 그리고 일부
  크리처의 공격.

**마비를 푸는 방법:**

- **피해를 받기** — 타격을 받으면 보통 Paralyze 주문이 일찍 풀립니다(당신을 향한 적대 행동이
  마비를 종료시킵니다).
- **함정 주머니(trapped pouch)** — 폭발 물약으로 함정을 건 주머니를
  ([세공(Tinkering)](/ko/skills/tinkering/)/[연금술(Alchemy)](/ko/skills/alchemy/)로 제작)
  소지하다가, 마비된 동안 더블클릭하면 즉시 풀려납니다. 이것이 표준적인 PvP 대응책입니다.
- **기다리기** — 지속 시간이 지나면 효과가 사라집니다.

[주문 저항(Resisting Spells)](/ko/skills/resisting-spells/)은 마법 마비의 지속 시간/확률을
낮춥니다(구체적 수치 미검증).

## 출혈과 필살 일격 (Bleeding and Mortal Strike)

이들은 **무기 특수 기술(special-move)** 효과입니다(see
[전투(고급)](/ko/playing/combat-advanced/#special-moves-primary-and-secondary)) — 정확한
수치는 **미검증**:

- **Bleed(출혈, Bleed Attack)** — 여러 초에 걸쳐 피해를 주는 상처를 입힙니다. **붕대**로
  상처를 싸매 출혈을 멈출 수 있습니다(`Bandage.cs`는 독/치료와 동일한 흐름에서 출혈을
  처리합니다).
- **Mortal Strike / Mortal Wound(필살 일격/치명상)** — 지속 시간 동안 대상은 일반적인
  수단으로 **치료받을 수 없습니다**; 기다리거나 특정 대응책을 써야 합니다. 치명상을 입은
  환자에게 쓴 붕대는 치료하는 대신 상처를 알려줍니다.

## 허기 (Hunger)

캐릭터는 시간이 지나면 **배가 고파집니다**. 음식을 무시하면:

- 허기는 재생을 줄이고 스탯/스태미나 회복을 저해할 수 있습니다(페널티 구체 수치 **미검증**).
- **먹는 법:** 배낭의 **[음식(food)](/ko/items/catalog/food-drink/)** — 과일, 빵, 익힌
  고기([요리(Cooking)](/ko/skills/cooking/)) — 을 배가 부를 때까지 더블클릭합니다("You are
  simply too full to eat any more.").

특히 긴 여행이나 반복 작업 중에는 음식을 좀 챙겨 두어, 허기가 조용히 회복을 늦추지 않게
하세요.

## 저주와 스탯 디버프 (Curses and stat debuffs)

다양한 주문/효과가 일시적으로 **스탯이나 저항을 낮춥니다:**

- **Curse(저주)** ([마법(Magery)](/ko/skills/magery/) 4서클) — 힘/민첩/지능을 낮춥니다(AOS에서는
  저항도 낮출 수 있음).
- **Clumsy / Weaken / Feeblemind** (1서클) — 각각 단일 스탯을 낮춥니다.
- **Mass Curse** — 영역 버전.
- 크리처의 **오라(aura)**와 **디버프(debuff)** 공격도 유사한 감소를 적용할 수 있습니다.

**저주/스탯 디버프를 제거하려면:**

- 가능한 경우 **Remove Curse(저주 해제)** ([기사도(Chivalry)](/ko/skills/chivalry/))를 시전하거나,
- **효과가 만료될 때까지 기다리거나**(대부분의 스탯 디버프는 시간제), 또는
- 스탯 버프 주문(Bless, Strength, Agility, Cunning)으로 감소를 상쇄합니다.

(정확한 지속 시간과 중첩 규칙은 **미검증** — [마법(Magery)](/ko/skills/magery/)와
[마법 색인](/ko/magic/)을 참고하세요.)

## 빠른 참고 — 무엇이 무엇을 제거하는가

- **독** → 붕대(Healing/Anatomy ≥ 60), Cure/Arch Cure 주문, Cure 물약.
- **마비** → 피해 받기, 또는 함정 주머니, 또는 기다리기.
- **출혈** → 붕대, 또는 기다리기.
- **필살 일격** → 기다리기(치료 차단); 특정 대응책만 유효.
- **허기** → 음식 먹기.
- **저주 / 스탯 디버프** → Remove Curse, 역버프, 또는 기다리기.

## 함께 보기

- [치료(Healing)](/ko/playing/healing/) — 해독 및 치료 절차
- [전투(고급)](/ko/playing/combat-advanced/) — 이러한 상태를 유발하는 특수 기술
- [독 바르기(Poisoning)](/ko/skills/poisoning/), [마법(Magery)](/ko/skills/magery/), [기사도(Chivalry)](/ko/skills/chivalry/)
- [몬스터 도감(Bestiary)](/ko/bestiary/) — 어떤 크리처가 중독시키거나 디버프를 거는지
- [물약(Potions)](/ko/items/catalog/potions/), [음식 & 음료](/ko/items/catalog/food-drink/)
