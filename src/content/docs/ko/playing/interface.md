---
title: 사용자 인터페이스 (Gumps)
description: UO 클라이언트의 화면 창들 — 상태 바, 컴팩트 체력 바, 종이인형, 배낭과 컨테이너, 주문서와 스킬 목록 — 각 항목이 무엇을 뜻하고 각 창이 어떻게 동작하는지.
status: unverified
sources:
  - "client: gumpartLegacyMUL.uop (UI gump art)"
  - "classicuo: Game/UI/Gumps/StatusGump.cs (StatusGumpOld, gump 0x0802 field layout)"
  - "classicuo: Game/UI/Gumps/HealthBarGump.cs (self bar gump 0x0803, bar lines 0x0805/0x0806/0x0808)"
  - "classicuo: Game/UI/Gumps/ContainerGump.cs (default backpack 0x003C)"
  - "classicuo: Game/UI/Gumps/SpellbookGump.cs (magery spellbook 0x08AC)"
  - "classicuo: Game/UI/Gumps/StandardSkillsGump.cs + Controls/ExpandableScroll.cs (skill scroll 0x1F40..)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

Ultima Online에서 하는 거의 모든 일은 **gump**라 불리는 작은 화면 창을 통해 일어납니다.
gump는 클라이언트가 게임의 *gump 아트*로 그리는 모든 UI 패널입니다 — 상태 바, 체력 바,
종이인형, 열린 컨테이너, 주문서, 스킬 목록, 상점 주인의 재고, 읽는 표지판 등. 이 페이지는
신규 플레이어가 가장 많이 쓰게 될 창들과 그 위의 각 항목이 무엇을 뜻하는지에 대한 둘러보기
입니다.

아래 그림들은 클라이언트 자체의 gump 아트에 예시 값을 덧입혀 만든 것이라, 게임 안에서 보는
것과 같은 외형(chrome)을 보여줍니다.

## "gump"란 무엇인가?

**gump**는 드래그할 수 있는 클라이언트 창입니다. 공통된 동작을 공유합니다:

- **열기** — 대부분의 gump는 그것이 속한 대상을 **더블클릭**하여 엽니다(종이인형은 자기
  자신을, 배낭 내용물은 배낭을, 주문서를 읽으려면 주문서를 더블클릭) 또는 단축키/메뉴로 엽니다.
- **이동** — gump를 그 프레임으로 끌어 위치를 바꿉니다. 클라이언트는 영구적인 것들(상태 바,
  종이인형)을 어디에 두었는지 세션 간에 기억합니다.
- **닫기** — gump를 우클릭하여 닫습니다. 컨테이너는 사거리 밖으로 걸어 나가도 닫힙니다.
- **겹치기** — 한 번에 여러 gump를 열어 둘 수 있습니다; 하나를 클릭하면 맨 앞으로 옵니다.

몇몇 gump는 고정된 그림이 아니라 *상호작용하는 표면(interactive surface)*입니다 — 종이인형은
당신의 몸과 착용한 각 아이템으로 합성되고, 스킬 목록은 더 길게 늘릴 수 있는 양피지 두루마리
입니다. 이것들은 아래에 표시되어 있습니다.

## 상태 바

<img src="/img/ui/status-bar.png" alt="UO status window showing name, Str/Dex/Int, Hits/Mana/Stam, gold and weight" width="282" />

**상태 바(status bar)**는 캐릭터의 생체 신호 패널입니다. 컴팩트한 클래식 창(gump `0x0802`,
위 그림)은 항목들을 두 열로 배치합니다:

**왼쪽 열**

- **Name(이름)** — 캐릭터의 이름.
- **STR (Strength, 힘)** — 최대 Hit Points와 운반 가능 무게를 올리고, 무거운 무기와 방어구를
  사용할 수 있게 합니다.
- **DEX (Dexterity, 민첩)** — 최대 Stamina와 공격 속도를 올립니다.
- **INT (Intelligence, 지능)** — 최대 Mana를 올립니다.
- **Sex(성별)** — 캐릭터의 성별(Male/Female); 확장 보기에서는 종족 옆에 위치합니다.
- **AR (Armor Rating, 방어 등급)** — 착용한 방어구로부터의 물리 피해 저항. 확장/현대 상태
  창에서는 이것이 **다섯 가지 저항(five resistances)**(Physical, Fire, Cold, Poison, Energy)
  중 첫 번째이며, 각각 *현재/최대*로 표시됩니다.

**오른쪽 열**

- **HITS** — 현재 / 최대 **Hit Points**. 0에 도달하면 죽습니다. 최대치는 Strength에 따라
  커집니다.
- **MANA** — 현재 / 최대 **Mana**, 주문과 일부 특수 기술의 연료. 최대치는 Intelligence에 따라
  커지며; 명상 중에는 마나가 더 빠르게 재생됩니다.
- **STAM** — 현재 / 최대 **Stamina**. 행동하고 달리면 소모됩니다; 0이면 달릴 수 없고 더 느리게
  휘두릅니다. 최대치는 Dexterity에 따라 커집니다.
- **GOLD** — 배낭에 든 금화.
- **WGHT (Weight, 무게)** — 현재 / 최대 운반 무게. 최대치를 넘으면 **과적(overweight)** 상태가
  됩니다: 느려지고 결국 움직일 수 없게 됩니다.

STR/DEX/INT 옆의 작은 자물쇠 아이콘은 **스탯 잠금(stat locks)**입니다 — 클릭하면 각 스탯을
*올림*(↑), *내림*(↓), *잠금*(—) 사이로 순환시키며, 훈련 시 어떤 스탯이 바뀔 수 있는지를
제어합니다.

확장 상태 창에는 더 많은 것이 추가됩니다: 다섯 가지 저항, **Followers**(펫 제어 슬롯의 사용/
최대), Luck, 무기 Damage, Stat Cap, 그리고 전투 등급. 각 수치가 무엇을 하고 이 샤드에서 어떻게
성장하는지는 **[캐릭터 & 스탯](/ko/playing/character-and-stats/)**을 보세요.

## 체력 바

<img src="/img/ui/health-bar.png" alt="Compact UO health bar with name and filled health, stamina and mana bars" width="154" />

**체력 바(health bar)**는 크리처의 Hits, Stamina, Mana를 숫자가 아니라 막대로 보여주는 작은
3줄 gump(자기 자신 바 = gump `0x0803`)입니다. 다음에 대해 열 수 있습니다:

- **자기 자신** — 화면 어디에나 둘 수 있는 이동 가능한 표시기.
- **펫** — 길들인 각 크리처마다 바를 열어 전투 중 체력을 지켜보고 명령을 내립니다.
  **[길들이기 & 펫](/ko/playing/taming-and-pets/)**을 보세요.
- **다른 플레이어와 몬스터** — 대상을 싱글클릭하고 드래그하여 그 바를 띄웁니다.

바는 *현재 ÷ 최대*에 비례하여 채워집니다. 색이 상태를 알립니다:

- **초록 / 파랑** — 건강함; 채워진 부분이 남은 양입니다.
- **회색(회색 처리됨)** — 크리처가 죽었거나, 사거리 밖이거나, 숨어 있어 표시가 오래된
  것입니다.
- **노랑** — 무적/축복(harm 불가).
- **중독됨(Poisoned)** — 대상이 독 피해를 받고 있음을 경고하기 위해 바가 독 색으로 변합니다.

다른 플레이어의 바는 또한 **악명(notoriety)**(innocent, criminal, enemy 등)에 따라 색이
입혀집니다. 그것이 전투를 어떻게 좌우하는지는 **[전투 기초](/ko/playing/combat-basics/)**를
보세요.

## 종이인형

**종이인형(paperdoll)**은 자기 자신을 더블클릭하면 열리는 머리부터 발끝까지의 캐릭터 초상입니다.
장비 화면도 겸합니다: 착용한 모든 아이템이 입은 상태로 표시되며, 아이템을 끌어 입고 벗을 수
있습니다. 이는 하나의 그림이 아니라 — 클라이언트가 나체 몸에 장착된 아이템마다 하나씩의 gump를
더해, 슬롯 순서로 그리고 각 아이템의 색조로 입혀 합성합니다.

종이인형이 어떻게 조립되는지에 대한 전체 설명(과 복장 갤러리)은
**[종이인형 참고(Paperdoll reference)](/ko/reference/paperdoll/)**를 보세요.

## 배낭 & 컨테이너

<img src="/img/ui/backpack.png" alt="UO default backpack container window" width="230" />

**배낭(backpack)**을 더블클릭하면 컨테이너 gump가 열립니다(기본 배낭 = gump `0x003C`, 위 그림).
컨테이너는 UO가 모든 것을 저장하는 방식입니다:

- **아이템은 창 안의 자유 위치에 놓입니다** — 끌어서 집어 들고, 창에 떨어뜨려 도로 넣고, 다른
  컨테이너에 떨어뜨려 둘 사이로 옮깁니다.
- **중첩(Nesting)** — 컨테이너는 다른 컨테이너를 담을 수 있으며(배낭 속 주머니, 은행 상자 속
  궤짝), 각각 자체 gump로 열립니다.
- **무게(Weight)** — 모든 아이템에는 무게가 있고; 배낭의 내용물은 상태 바의 **WGHT** 수치에
  반영됩니다. Bag-of-holding과 은행 상자는 자체 아이템/무게 한도를 가집니다.
- **쌓기(Stacking)** — 동일한 상품(금화, 시약, 주괴)은 수량이 표시된 하나의 더미로 쌓입니다.

집어 들기, 장착, 은행 상자, 그리고 죽었을 때 무엇이 남는지는
**[아이템 & 소지품](/ko/playing/items-and-inventory/)**을 보세요.

## 주문서 & 스킬 목록

### 주문서

<img src="/img/ui/spellbook.png" alt="An open UO magery spellbook gump" width="406" />

**주문서(spellbook)**를 더블클릭하면 열립니다(마법 책은 gump `0x08AC`). 옮겨 적은 각 주문이
책의 페이지에 작은 아이콘으로 나타납니다; 책등을 따라 있는 원형 버튼이 주문 서클 사이를
넘깁니다. 시전하려면 **주문 아이콘을 더블클릭**(또는 주문 단축키 사용)한 뒤, 타겟 커서로
조준합니다. 시전에는 알맞은 **Magery** 스킬, 충분한 **Mana**, 그리고 배낭 안의 주문 **시약
(reagents)**이 필요합니다. 전체 시전 흐름, 실패(fizzle), 방해는
**[주문 시전](/ko/playing/spellcasting/)**을 보세요.

### 스킬 목록

<img src="/img/ui/skills.png" alt="UO skill list parchment scroll with example skills and values" width="345" />

**스킬 목록(skill list)**은 모든 스킬과 100.0 만점 중 현재 수치를 나열하는 양피지 두루마리
(확장 가능 두루마리 gump `0x1F40`–`0x1F43`로 구성)입니다. 여기서 할 수 있는 것:

- **활성 스킬 사용** — *사용 가능*으로 강조된 이름의 스킬(Hiding, Animal Lore, Anatomy,
  Detect Hidden 등)을 더블클릭하여 발동한 뒤, 요청하면 타겟합니다.
- **스킬을 끌어내기** — 화면에 원클릭 버튼으로 만듭니다.
- **스킬 잠금 설정** — 각 스킬 옆의 작은 화살표가 *올림*(↑) / *내림*(↓) / *잠금*(—)을
  순환하며, 총 스킬 상한에 가까워질 때 어떤 스킬이 포인트를 얻거나 내놓을지를 관장합니다.

두루마리의 아래 가장자리를 끌어 더 많은 행을 보이도록 길게 늘일 수 있습니다. 스킬이 사용으로
어떻게 오르는지와 이 샤드의 상한은 **[스킬 사용 & 훈련](/ko/playing/using-and-training-skills/)**
을 보세요.

## 일반적인 gump & 타게팅

많은 행동은 **2단계**입니다: 무언가를 발동하고(주문 시전, 스킬 사용, 제작 클릭, "looting"
선택), 클라이언트가 **타겟 커서(targeting cursor)**를 보여주면, 그 행동이 적용될 대상을
클릭합니다. 타겟 커서가 떠 있는 동안:

- 대상을 클릭하여 행동을 적용하고;
- **Escape**(또는 우클릭)를 눌러 취소하고;
- 단축키로 클릭 없이 **마지막 타겟(last target)**을 재사용하거나 **자기 자신(yourself)**을
  타겟합니다.

이 "발동 후 타겟" 패턴은 시전, 치료, 길들이기, 제작, 줍기 모두의 바탕이 됩니다. 커서,
마지막 타겟 / 자기 타겟 단축키, 사거리 규칙은 **[타게팅](/ko/playing/targeting/)**을 보세요.
