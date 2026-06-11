---
title: 은신과 잠행
description: 숨는 법, 잠행(Stealth)으로 숨은 채 이동하는 법, 다른 이를 탐지하고 추적하는 법, 무엇이 당신을 드러내는지, 그리고 은신을 도주·정찰·도둑/암살자 플레이에 활용하는 법.
status: unverified
sources:
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

이 페이지는 들키지 않고 머무는 법을 다룹니다. 사라지는 [은신(Hiding)](/ko/skills/hiding/),
숨은 채 움직이는 [잠행(Stealth)](/ko/skills/stealth/), 다른 이를 찾아내는
[은신 탐지(Detecting Hidden)](/ko/skills/detecting-hidden/)와 [추적(Tracking)](/ko/skills/tracking/),
그리고 무엇이 당신을 드러내는지를 설명합니다. 도주를 위한 전투 활용은
[전투 기초 → 도주](/ko/playing/combat-basics/#fleeing)에 있습니다.

## 은신 — 그 자리에서 사라지기

**숨으려면:**

1. **가만히 서 있으세요** (이동 중에는 숨을 수 없습니다 — 그건 잠행이 필요합니다).
2. **[은신(Hiding)](/ko/skills/hiding/)** 스킬을 발동하세요(스킬 목록을 열어 은신을 사용하거나,
   은신 단축키/매크로를 사용).
3. 성공하면 다른 플레이어와 대부분의 생물에게 **보이지 않게** 됩니다: "You have
   hidden yourself well."; 실패하면: "You can't seem to hide here."

**성공 확률은 은신 스킬에 비례**합니다 — 스킬이 높을수록 더 안정적으로, 더 위험한 상황(적 근처)
에서도 숨을 수 있습니다. 가만히 서 있고 관찰자에게서 떨어져 있으면 도움이 됩니다. 일부
클라이언트/상황은 보정치를 더합니다(세부 사항 미확인).

숨어 있는 동안에는 다른 이의 화면에 나타나지 않으며 많은 자동 타기팅 공격에서도 건너뛰어집니다 —
무언가가 당신을 드러낼 때까지(아래 참고).

## 잠행 — 숨은 채 이동하기

단순한 은신은 한 걸음을 떼는 순간 풀립니다. **[잠행(Stealth)](/ko/skills/stealth/)**은
**숨은 상태를 깨지 않고 이동**하게 해 줍니다:

**잠행하려면:**

1. **먼저 숨으세요**(잠행을 시작하려면 이미 숨어 있어야 합니다).
2. 한 번에 한 칸씩 이동하세요. 매 걸음마다 [잠행(Stealth)](/ko/skills/stealth/) 스킬이 판정됩니다.

- 다시 판정하거나 드러날 위험을 감수하기 전까지 **제한된 걸음 수**만 잠행할 수 있으며,
  **안전한 걸음 수는 잠행 스킬에 비례**합니다(스킬이 높을수록 = 더 많은 걸음). 정확한 걸음 수는
  **미확인** — [잠행(Stealth)](/ko/skills/stealth/) 참고.
- 잠행은 일반적으로 대놓고 달리는 것보다 **느리며**, 갑옷을 입지 않거나 가벼운 갑옷일 때 가장
  잘 작동합니다(무거운 갑옷은 잠행에 페널티를 줍니다 — 세부 사항 미확인).
- 잠행 판정에 실패하면 **드러나게** 됩니다. 다시 숨고 계속하세요.

## 은신 탐지 — 다른 이를 드러내기

**[은신 탐지(Detecting Hidden)](/ko/skills/detecting-hidden/)**는 근처에 숨은 플레이어와
생물을 찾아냅니다.

**탐지하려면:**

1. **은신 탐지** 스킬을 사용하세요.
2. 숨은 캐릭터가 있다고 의심되는 **영역/지점을 지정**하세요.
3. 성공하면 사거리 안의 숨은 대상이 드러납니다.

높은 은신 탐지가 숨은 자의 은신/잠행을 능가하면 그를 찾아낼 수 있습니다. 이는 잠행자에 대한
능동적 대응책으로, 경비병·도둑 차단자·PvP 플레이어가 이를 훈련합니다.

## 추적 — 생물과 플레이어 찾기

**[추적(Tracking)](/ko/skills/tracking/)**은 시야에 없는 모빌(mobile)이라도 근처에 있으면
위치를 찾아냅니다.

**추적하려면:**

1. **추적** 스킬을 사용하세요.
2. 메뉴에서 **분류**(동물, 몬스터, 인간형/사람 등)를 고르세요.
3. 사거리 안에서 가장 가까운 일치 대상 쪽으로 목록/화살표를 얻습니다.

높은 추적은 더 먼 사거리의 대상을 보여 주며 잠행자를 **드러내거나** 적어도 **위치를 파악**하는 데
도움이 됩니다(추적은 숨은 이동자의 존재/방향을 감지할 수 있습니다 — 은신 탐지와 조합해 그들을
못 박으세요). 사냥, 정찰, 도둑 잡기에 유용합니다.

## 무엇이 당신을 드러내는가

다음을 하면 숨은 상태를 잃습니다:

- **공격**하거나 적대 행동을 취할 때.
- **주문을 시전**할 때(시전은 당신을 드러냅니다 — `RevealingAction`).
- **붕대를 사용**하거나 많은 스킬/아이템을 사용할 때(붕대 코드는 사용 시 `RevealingAction`을
  호출합니다 — [치료](/ko/playing/healing/) 참고).
- **피해를 입거나** 적중당할 때.
- 특정 생물에 **인접**하거나 너무 가까이 너무 오래 서 있을 때(근접 드러남 —
  세부 사항 미확인).
- **은신 탐지**나 **드러내기(Reveal)** 주문([마법술](/ko/skills/magery/) 6서클)에 걸릴 때 —
  이는 영역 내 모두를 강제로 드러냅니다.

요약하면: **행동하면 드러납니다.** 은신/잠행은 이동하고 관찰하기 위한 것이지, 보이지 않는 채
행동하기 위한 것이 아닙니다.

## 은신과 잠행의 용도

- **도주** — [시야 선](/ko/playing/combat-basics/#range-melee-adjacency-vs-ranged-line-of-sight)을
  끊은 뒤 은신해 추격자를 떨치고 회복하거나 [소환(Recall)](/ko/playing/movement-and-travel/)으로
  벗어나세요.
- **정찰** — 던전이나 PvP 구역으로 잠행해 들어가 적을 발견하고, 수를 세고, 들키지 않고 전리품을
  찾으세요.
- **도둑 플레이** — [절도(Stealing)](/ko/skills/stealing/)와 [엿보기(Snooping)](/ko/skills/snooping/)는
  은신/잠행과 짝을 이뤄 물건을 훔치고 빠져나갑니다. 이것이 유발하는 범죄 플래그는
  [악명과 PvP](/ko/playing/notoriety-and-pvp/) 참고.
- **암살자 플레이** — 잠행으로 위치를 잡고 강한 일격이나
  [인술(Ninjitsu)](/ko/skills/ninjitsu/) 동작으로 시작하세요. 단, 공격하는 즉시 드러납니다.

## 함께 보기

- [은신(Hiding)](/ko/skills/hiding/), [잠행(Stealth)](/ko/skills/stealth/), [은신 탐지(Detecting Hidden)](/ko/skills/detecting-hidden/), [추적(Tracking)](/ko/skills/tracking/)
- [전투 기초 → 도주](/ko/playing/combat-basics/#fleeing)
- [이동과 여행](/ko/playing/movement-and-travel/)
- [절도(Stealing)](/ko/skills/stealing/), [엿보기(Snooping)](/ko/skills/snooping/), [인술(Ninjitsu)](/ko/skills/ninjitsu/)
- [악명과 PvP](/ko/playing/notoriety-and-pvp/) — 도둑/암살자 행동에서 생기는 플래그
