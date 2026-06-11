---
title: 치유
description: 완전한 치유 참조 — 붕대(타이밍, 해독, 부활), 마법술 치유/해독 주문, 치유 물약, 그리고 펫을 위한 수의학.
status: unverified
sources:
  - "servuo: Scripts/Items/Resource/Bandage.cs (delay formula, range, cure/res skill thresholds, heal amount)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

이것은 모든 방법으로 체력을 회복하고 독을 제거하는 핵심 참조입니다: **붕대**(
[치유(Healing)](/ko/skills/healing/) / [수의학(Veterinary)](/ko/skills/veterinary/)),
**주문**([마법술(Magery)](/ko/skills/magery/)), 그리고 **물약**(
[물약 카탈로그](/ko/items/catalog/potions/)). 독 자체에 대해서는
[독과 상태이상](/ko/playing/poison-and-status/)을 참고하고, 죽음과 다시 일어서기에 대해서는
[죽음과 부활](/ko/playing/death-and-resurrection/)을 참고하세요.

## 붕대 — 사용법

**상처에 붕대를 감으려면:**

1. 배낭에 **붕대**가 있는지 확인하세요([재봉](/ko/playing/crafting/)으로 천을 제작하거나,
   치유사/벤더에게서 구입).
2. 가방의 붕대를 **더블클릭**하세요 — 대상 커서가 나타납니다.
3. 자신, 다친 아군, 또는 펫을 **대상으로 지정**하세요. 사정거리 안에 있어야 합니다(이 AOS
   샤드에서는 `Bandage.cs`의 `Range`에 따라 **2타일**).
4. 타이머가 끝나기를 기다리세요. 성공 시: "You finish applying the bandages." 그리고 HP가
   회복됩니다.

적용당 붕대 하나가 소모됩니다. 높은 민첩은 각 적용을 더 빠르게 하고, 높은
[치유](/ko/skills/healing/)와 [해부학](/ko/skills/anatomy/)은 **더 많은 HP**를 치유하고
성공/해독/부활 확률을 높입니다. 붕대 사용은 당신의 치유(또는 수의학)와 짝을 이루는 보조 스킬을
**120** 스킬까지 단련합니다(`Bandage.cs`의 `CheckSkill` 한계).

## 붕대 타이밍 (검증됨)

`Scripts/Items/Resource/Bandage.cs`의 `GetDelay`(AOS 경로)에서. 시간 단위는 **초**이며,
`Dex`는 치유자의 민첩입니다:

- **자가 치유:** `max(4, min(8, ceil(11 − Dex/20)))`. 즉 매우 높은 민첩에서 4초, 낮은
  민첩에서 최대 8초.
- **다른 사람 치유:** `max(2, ceil(4 − Dex/60))`. 최대 2초까지 빨라집니다.
- **펫에 [수의학](/ko/skills/veterinary/):** 고정 **2초**.
- **붕대를 통한 부활:** non-AOS dex 분기는 죽은 대상에 대해 **+5초**를 더합니다
  (`resDelay = 5.0`); 부활 붕대는 치유보다 눈에 띄게 더 오래 걸리는 것으로 보세요.

한 번에 **하나의 붕대 타이머**만 돌릴 수 있습니다 — 새 타이머를 시작하면 이전 것이 취소됩니다.

## 미끄러짐, 방해, 그리고 이동

- 적용 도중 타격을 받거나 방해받으면 **손가락이 미끄러질** 수 있습니다("Your fingers
  slip!"). 각 미끄러짐은 치유되는 HP를 줄이고(AOS에서는 미끄러짐당 약 35%) 해독/부활 확률을
  낮춥니다.
- 타이머가 끝나기 전에 **사정거리를 벗어나면**(환자로부터 2타일 초과), "You did not stay
  close enough to heal your target."가 뜨고 치유가 실패합니다.
- 끝나기 전에 **당신이 죽으면**: "You were unable to finish your work before you died."가
  뜨고 실패합니다.

**모범 사례:** 붕대가 끝날 때까지, 특히 다른 사람을 치유할 때는 정지해 인접한 상태를
유지하세요.

## 붕대가 치유하는 양

치유량은 **치유**와 **해부학**에 비례합니다(AOS 경로, `Bandage.cs`):

- `min = Anatomy/8 + Healing/5 + 4`
- `max = Anatomy/6 + Healing/2.5 + 4`
- 실제 치유량은 `min`과 `max` 사이의 무작위 값이며, 미끄러짐으로 감소하고, 같은 적용에서 동시에
  독/출혈을 해독했다면 감소합니다.

요컨대: **해부학과 치유가 높을수록 = 더 큰 치유.** 둘 다 최대로 올리면
([치유](/ko/skills/healing/) 100, [해부학](/ko/skills/anatomy/) 100) 가장 크고 가장
안정적인 붕대 치유를 얻습니다.

## 붕대로 독 해독하기

**중독된** 환자에게 붕대를 감으면 HP 치유 대신(또는 그에 앞서) 독을 해독하려 시도합니다.

- **스킬 요구치 (검증됨):** **치유 ≥ 60**과 **해부학 ≥ 60** 모두
  (`checkSkills = healing >= 60.0 && anatomy >= 60.0`).
- **해독 확률** = `(Healing − 30)/50 − (PoisonLevel × 0.1) − (Slips × 0.02)`. 높은 독
  단계(치명적 > 더 강한 > 일반 > 약한)는 해독하기 더 어렵고, 미끄러짐은 해가 됩니다.
- 성공 시: "You have been cured of all poisons." 실패 시: "You have failed to cure your
  target!" — 붕대를 한 번 더 적용해 다시 시도하세요.

독 단계와 다른 해독법은 [독과 상태이상](/ko/playing/poison-and-status/)을 참고하세요.

## 붕대로 부활시키기

**죽은** 플레이어(또는 수의학을 통해 죽은 펫)에게 붕대를 적용하면 그들을 되살릴 수 있습니다.

- **스킬 요구치 (검증됨):** **치유 ≥ 80**과 **해부학 ≥ 80** 모두
  (`checkSkills = healing >= 80.0 && anatomy >= 80.0`). 펫의 경우 수의학/동물 지식 등가가
  적용됩니다.
- **성공 확률** = `(Healing − 68)/50 − (Slips × 0.02)`.
- 성공 시 환자는 수락할 **부활 gump**를 받습니다. 죽은 펫을 부활시키면 펫에게 약간의 스킬
  손실(스킬당 0.1)이 발생합니다.
- 일반 붕대보다 오래 걸립니다(위의 **+5초** 부활 지연). 환자의 시체는 시신이 "들어맞는" 자리에
  있어야 하며, 일부 지역(예: Khaldun)은 부활을 막습니다.

전체 죽음/유령 절차: [죽음과 부활](/ko/playing/death-and-resurrection/).

## 마법술 치유 주문

[마법술](/ko/skills/magery/)과 주문서 + 시약이 있다면(
[주문 시전](/ko/playing/spellcasting/)과 [마법 색인](/ko/magic/) 참고):

- **Heal** (1서클) — 적당한 양의 HP를 회복합니다. **중독된 대상에는 작동하지 않습니다** —
  먼저 독을 해독해야 합니다.
- **Greater Heal** (4서클) — 더 많은 HP를 회복합니다. 마찬가지로 하위 치유는 독에 의해
  막히므로, 먼저 해독하세요.
- **Cure** (2서클) — 독을 제거합니다; 높은 독 단계에 대한 성공은 마법술에 비례합니다(임계값
  unverified).
- **Arch Cure** (4서클) — 여러 대상에서 독을 제거하는 광역 해독.

주문 시전은 **방해 가능**합니다: 타격을 받으면 치유가 피즐할 수 있습니다(
[전투 심화](/ko/playing/combat-advanced/#주문-및-무기-방해-피즐fizzle) 참고). 메이지는 보통
거리를 벌린 뒤 치유/해독합니다.

## 치유 물약

물약은 **즉시** 효과(시전/붕대 타이머 없음)이지만 물약 사용 사이에 **쿨다운**을
공유합니다(연달아 들이켤 수 없으며 지연이 있습니다 — 정확한 쿨다운 **unverified**). 비상
버튼으로 들고 다니세요. [물약 카탈로그](/ko/items/catalog/potions/)를 참고하세요:

- **Heal potion** — 소량의 즉시 HP.
- **Greater Heal potion** — 더 많은 즉시 HP.
- **Cure potion** — 독을 제거합니다(효과는 물약 강도 대 독 단계에 비례 — **unverified**).

**물약을 사용하려면:** 가방에서 더블클릭하세요. 물약은 [연금술](/ko/skills/alchemy/)로
만듭니다.

## 펫 치유 — 수의학

동물과 길들인 생물의 치유는 치유가 아니라 **[수의학](/ko/skills/veterinary/)**(보조로
[동물 지식(Animal Lore)](/ko/skills/animal-lore/))을 사용합니다. 붕대 절차는 동일합니다 —
붕대를 더블클릭하고, 펫을 대상으로 지정 — 펫에 대한 수의 붕대는 고정 **2초**입니다(`Bandage.cs`).
수의학은 가까이에 있는 주인/친구가 정화해 줄 수 있다면 **죽은 펫**도 부활시킬 수 있습니다.
[조련과 펫](/ko/playing/taming-and-pets/)을 참고하세요.

## 어떤 것을 언제 쓸까

- **붕대** — 지속 가능하고 마나가 들지 않는 주력 치유. 최고의 자원 대비 HP 효율; 스킬을
  단련하지만; 몇 초가 걸리고 미끄러질 수 있습니다. 전투 중과 전투 밖에서 기본으로 사용하세요.
- **Heal/Greater Heal 주문** — 마나가 있으면 빠른 폭발 치유이지만, 시약을 소모하고 피격 시
  피즐할 수 있으며 독에 막힙니다.
- **Cure (주문/물약/붕대) / Arch Cure** — 하위 치유를 효과적으로 쓰기 전에 독을 제거하기 위해.
- **Heal/Greater Heal 물약** — 붕대 타이머나 피즐을 감당할 수 없을 때 쿨다운을 감수한 즉시
  비상 치유.
- **수의학 붕대** — 펫을 치유/부활시키는 방법.

흔한 생존 패턴: **먼저 독 해독**(붕대/Cure), 그다음 **붕대나 주문으로 HP 치유**, 그리고
죽기 직전의 순간을 위해 **치유 물약**을 예비로 두세요.

## 함께 보기

- [치유 스킬](/ko/skills/healing/), [해부학](/ko/skills/anatomy/), [수의학](/ko/skills/veterinary/)
- [독과 상태이상](/ko/playing/poison-and-status/)
- [죽음과 부활](/ko/playing/death-and-resurrection/)
- [주문 시전](/ko/playing/spellcasting/), [마법술](/ko/skills/magery/), [마법 색인](/ko/magic/)
- [물약 카탈로그](/ko/items/catalog/potions/), [연금술](/ko/skills/alchemy/)
- [명상과 마나](/ko/playing/meditation-and-mana/) — 치유 주문을 위한 마나 충당
