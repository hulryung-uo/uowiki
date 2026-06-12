---
title: 도구
description: 직업 및 유틸리티 도구 — 각 땜장이, 대장, 재단, 목공, 필경, 채집 도구가 무엇을 하는지, 어느 스킬에 쓰이는지, 사용 횟수는 얼마이고 어디서 구하는지.
status: source-verified
sources:
  - "servuo: Scripts/Items/Tools/BaseTool.cs"
  - "servuo: Scripts/Items/Tools/BaseHarvestTool.cs"
  - "servuo: Scripts/Items/Tools (TinkerTools, SmithHammer, Tongs, SewingKit, Scissors, Saw, DovetailSaw, MouldingPlane, JointingPlane, DrawKnife, Froe, Inshave, FletcherTools, ScribesPen, MortarPestle, Skillet, FlourSifter, RollingPin, MapmakersPen, Shovel, FishingPole)"
  - "servuo: Scripts/Items/Equipment/Weapons/Pickaxe.cs, Hatchet.cs, Axe.cs"
  - "servuo: Scripts/Items/Consumables/LockPick.cs"
  - "servuo: Scripts/Services/Craft/DefTinkering.cs (craft recipes + skill ranges)"
  - "client: artLegacyMUL.uop"
last_verified: 2026-06-11
generated: false
---

도구는 제한된 **사용 횟수(uses)**를 가진 소모 아이템입니다. 대부분의 도구는 더블 클릭하면 **제작
메뉴**(현재 스킬로 그 도구가 만들 수 있는 모든 것을 나열하는 gump)를 엽니다. 다른 도구들은 더블
클릭하면 일회성 동작을 발동한 뒤 월드를 타게팅합니다 — 곡괭이는 바위를, 낚싯대는 물을 겨눕니다.
어느 쪽이든 성공할 때마다 도구의 내구도가 깎이고, **남은 사용 횟수**가 0이 되면 도구는 부서지고
다음 것을 꺼내야 합니다.

이 목록의 거의 모든 금속 도구는 땜장이가 만듭니다 — [땜질(Tinkering)](/ko/skills/tinkering/)은 철
주괴(그리고 몇몇 목제 도구의 경우 판자)를 브리타니아의 도구 전체로 바꿉니다. 나머지는 마을 상인에게
삽니다. 제작 gump가 어떻게 작동하는지는 [제작(Crafting)](/ko/playing/crafting/)을, 채집 도구가
사용하는 클릭-타게팅 단계는 [타게팅(Targeting)](/ko/playing/targeting/)을 보세요.

도구 일가 전체에 적용되는 몇 가지 사실을 `Scripts/Items/Tools/BaseTool.cs`에서 그대로 가져왔습니다.

- 갓 **땜장이가 만든** 금속 도구는 *무작위로* 25–75회 사용으로 시작합니다
  (`BaseTool(int itemID) : this(Utility.RandomMinMax(25, 75), itemID)`) — 뛰어난 솜씨와
  고등급 주괴는 그 수치를 더 끌어올립니다.
- 도구의 품질과 사용 횟수는 메뉴가 아니라 제작자에 달려 있습니다 — 더 나은 땜장이가 더 오래가는
  도구를 만듭니다.
- 도구는 **영혼 귀속(soulbound)이 아닙니다** — 비축하거나 팔거나, 세션 중에 새 재봉 키트를
  길드원에게 건넬 수 있습니다.

## 제작 도구

이것들은 해당 직업의 제작 gump를 엽니다. 따로 명시하지 않는 한, 각각은 땜장이가 철 주괴로 만듭니다.
괄호 안의 스킬 범위는 레시피를 *처음* 시도할 수 있는 땜질 스킬부터 *마지막으로* 보장되는 지점까지의
구간입니다(`DefTinkering.cs`). 해당 NPC 상인에게서 그냥 살 수도 있습니다 —
[상인 & 은행](/ko/playing/vendors-and-banking/)을 보세요.

### Tinker's Tools — [땜질(Tinkering)](/ko/skills/tinkering/)

<img src="/img/items/0x1EB8.png" class="uo-sprite" alt="" width="56" />

땜장이 자신의 키트. 더블 클릭하면 땜질 메뉴를 열어 시계, 함정, 열쇠, 도구(추가 땜장이 도구 포함),
장신구, 그리고 다양한 소형 금속 제품을 만듭니다. 철 주괴 2개로 **땜질 10.0–60.0**에서 땜장이가
제작. 땜장이 NPC가 판매. 사용 횟수는 기본 25–75 범위.

### Smith's Hammer & Tongs — [대장기술(Blacksmithy)](/ko/skills/blacksmithy/)

<img src="/img/items/0x13E3.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0FBB.png" class="uo-sprite" alt="" width="56" />

**smith's hammer**는 대장간에서 대장기술 메뉴를 열어 주괴를 무기와 방어구로 두드립니다
(`CraftSystem => DefBlacksmithy.CraftSystem`). **tongs(집게)**는 같은 직업에 속하며 광석을 손에 든
상태로 변환하고 대장간 작업을 처리하는 도구입니다. 땜장이가 제작 — 해머는 주괴 4개로 **땜질
40.0–90.0**, 집게는 주괴 1개로 **35.0–85.0** — 또는 대장장이와 땜장이 상인에게서 구매. (AOS에서
제작 가능한 해머 클래스는 `SmithyHammer`이고, 구버전 `SmithHammer` 아트는 `0x13E3`입니다.)

### Sewing Kit & Scissors — [재봉(Tailoring)](/ko/skills/tailoring/)

<img src="/img/items/0x0F9D.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F9F.png" class="uo-sprite" alt="" width="56" />

**sewing kit(재봉 키트)**는 재봉 메뉴를 열어 천과 가죽을 의류와 가벼운 방어구로 꿰맵니다
(`DefTailoring.CraftSystem`). **scissors(가위)**는 재봉 도구이자 만능 절단 도구로 두 역할을 합니다.
**옷감 한 필을 천으로, 천을 붕대로, 생가죽을 가죽으로** 자릅니다([자원(Resources)](/ko/items/resources/)
참고). 가위는 특수 처리되어 무작위 25–75 기본값이 아닌 고정 **50회 사용**
(`Scissors.cs`의 `m_UsesRemaining = 50`)을 가집니다. 둘 다 땜장이가 제작(재봉 키트: 주괴 2개로
**10.0–70.0**; 가위: 주괴 2개로 **5.0–55.0**)하거나 재단사와 잡화상 상인에게서 구매합니다.

### 목공 도구 — [목공(Carpentry)](/ko/skills/carpentry/)

<img src="/img/items/0x1034.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1028.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x102C.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1030.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E4.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E5.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E6.png" class="uo-sprite" alt="" width="56" />

목수는 작은 무기고를 들고 다니며, **그중 어느 하나든 같은 목공 메뉴를 엽니다**(모든 클래스가
`DefCarpentry.CraftSystem`을 반환): **saw**, **dovetail saw**, **moulding plane**, **jointing
plane**, **smoothing plane**, **draw knife**, **froe**, **inshave**. 이들은 아트와 레시피 비용만
다릅니다 — 땜장이가 건네준 아무거나 골라 판자로 가구, 악기, 활, 하우스 애드온을 만드세요. 금속 날이
달린 것들(saw, dovetail saw, draw knife, froe, inshave)은 철로 **땜질 30.0–80.0**에서 땜장이가
제작하고, 목제 플레인과 jointing/moulding 플레인은 **판자**로 **0.0–50.0**에서 땜장이가 제작합니다.
모두 목수와 땜장이 NPC가 판매합니다.

### Fletcher's Tools — [활 제작 & 화살 제작(Bowcraft & Fletching)](/ko/skills/bowcraft-fletching/)

<img src="/img/items/0x1022.png" class="uo-sprite" alt="" width="56" />

활 제작 메뉴(`DefBowFletching.CraftSystem`)를 열어 판자와 깃털로 활, 석궁, 화살, 볼트를 만듭니다.
주괴 3개로 **땜질 35.0–85.0**에서 땜장이가 제작하거나, 활장인/화살장인 상인에게서 구매합니다.

### Scribe's Pen — [필사(Inscription)](/ko/skills/inscription/)

<img src="/img/items/0x0FBF.png" class="uo-sprite" alt="" width="56" />

필사 메뉴(`DefInscription.CraftSystem`)를 열어 주문 두루마리와 책(시약 + 빈 두루마리)을 적습니다.
주괴 1개로 **땜질 25.0–75.0**에서 땜장이가 제작하거나, 필경사와 메이지 상인에게서 구매합니다. 지도
제작자의 펜과 아트 `0x0FBF`를 공유합니다.

### Mortar & Pestle — [연금술(Alchemy)](/ko/skills/alchemy/)

<img src="/img/items/0x0E9B.png" class="uo-sprite" alt="" width="56" />

연금술 메뉴(`DefAlchemy.CraftSystem`)를 열어 시약을 물약으로 빻습니다. 주괴 3개로 **땜질
20.0–70.0**에서 땜장이가 제작하거나, 연금술사와 메이지 상인에게서 구매합니다. (일부 퀘스트 단계에서
시약을 빻는 타게팅 도구로도 쓰입니다.) [연금술(Alchemy)](/ko/skills/alchemy/)을 보세요.

### 요리 도구 — [요리(Cooking)](/ko/skills/cooking/)

<img src="/img/items/0x097F.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x103E.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1043.png" class="uo-sprite" alt="" width="56" />

**skillet(프라이팬)**, **flour sifter(체)**, **rolling pin(밀대)**은 각각 요리 메뉴
(`DefCooking.CraftSystem`)를 엽니다 — 실제로는 요리에 필요한 레시피(밀가루 체질, 반죽 밀기, 굽기)에
맞는 것을 꺼내 씁니다. 땜장이가 제작: 프라이팬(주괴 4개, **30.0–80.0**), 체(주괴 3개,
**50.0–100.0**), 밀대(**판자** 5개, **0.0–50.0**). 요리사, 제빵사, 잡화상 상인에게서 구매.

### Mapmaker's Pen — [지도 제작(Cartography)](/ko/skills/cartography/)

<img src="/img/items/0x0FBF.png" class="uo-sprite" alt="" width="56" />

지도 제작 메뉴(`DefCartography.CraftSystem`)를 열어 빈 지도를 그리고 보물 지도 위치를 정밀하게
찍습니다. 주괴 1개로 **땜질 25.0–75.0**에서 땜장이가 제작하거나, 지도 제작자/필경사 상인에게서
구매합니다. 필경사의 펜과 같은 아트(`0x0FBF`)입니다.

## 채집 도구

이것들은 메뉴를 열지 않습니다 — 더블 클릭한 뒤 자원 노드를 **타게팅**합니다
([자원 채집(Gathering resources)](/ko/playing/gathering-resources/) 참고). 제작 시스템이 아니라
채집 스킬에 쓰입니다.

### Pickaxe & Shovel — [채광(Mining)](/ko/skills/mining/)

<img src="/img/items/0x0E86.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F39.png" class="uo-sprite" alt="" width="56" />

둘 다 채광 채집(`HarvestSystem => Mining.System`)을 실행합니다. **pickaxe(곡괭이)**는 다재다능한
광부의 도구입니다 — 광맥을 작업하고 동굴과 산비탈에서 광석을 캐며, `BaseAxe`에서 파생되므로 (약한)
무기로도 쓸 수 있고, 고정 **50회 사용**(`Pickaxe.cs`의 `UsesRemaining = 50`)으로 시작합니다.
**shovel(삽)**은 광석을 파며 "땅을 파는" 더 깔끔한 작업 방식에 적합한 도구로, 역시 기본 **50회
사용**(`Shovel() : this(50)`)입니다. 바위에서 뽑아내는 것 — 철부터 valorite, 그리고 화강암, 모래,
보석 — 은 [자원(Resources)](/ko/items/resources/) 페이지에 있습니다. 곡괭이는 땜장이/대장장이
제품이고, 삽은 주괴 4개로 **땜질 40.0–90.0**에서 땜장이가 제작하며 광부와 잡화상이 판매합니다.

### Hatchet & Axe — [벌목(Lumberjacking)](/ko/skills/lumberjacking/)

<img src="/img/items/0x0F43.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F49.png" class="uo-sprite" alt="" width="56" />

모든 도끼류 무기(**hatchet**, **axe**, battle axe 등 — 전부 `BaseAxe`에서 파생)는 이중 역할을
합니다: 나무를 향해 휘둘러 [벌목(Lumberjacking)](/ko/skills/lumberjacking/)용 **통나무**를 베고,
그것으로 통나무를 **판자**로 자르며, 진짜 근접 무기로도 들고 다닙니다. 대장장이가 만들고
무기/잡화상 상인이 판매합니다. 산출량과 통나무→판자 표는 [자원(Resources)](/ko/items/resources/)에
있습니다.

### Fishing Pole — [낚시(Fishing)](/ko/skills/fishing/)

<img src="/img/items/0x0DC0.png" class="uo-sprite" alt="" width="56" />

더블 클릭하고 물을 타게팅해 낚시합니다(`FishingPole`이 낚시 채집을 실행). 장착 가능한 한손 아이템
이기도 하며, 그 자체로 제작 가능합니다(나무로 활 제작/목공). 표준 낚싯대는 **150회 사용**
(`FishingPole.cs`의 `UsesRemaining = 150`)으로 시작합니다 — 낚시가 긴 노가다인 만큼 금속 도구보다
훨씬 많습니다. 어물상과 잡화상 상인이 판매합니다. [낚시(Fishing)](/ko/skills/fishing/)를 보세요.

## 유틸리티 도구

제작 gump에 묶이지 않은 작은 단일 용도 아이템:

- **Lockpicks(자물쇠 따개)** <img src="/img/items/0x14FC.png" class="uo-sprite" alt="" width="56" /> —
  더블 클릭하고 잠긴 상자나 문을 타게팅해
  [자물쇠 따기(Lockpicking)](/ko/skills/lockpicking/) 스킬을 자물쇠 레벨과 겨룹니다. 어려운 자물쇠를
  실패하면 따개가 부러질 수 있습니다. 메뉴 도구와 달리 자물쇠 따개는 **쌓이는 소모품**입니다(개별
  도구 사용 횟수가 아니라 `Amount` — `LockPick.cs`). 주괴 1개로 **땜질 45.0–95.0**에서 땜장이가
  제작하거나, 도둑/땜장이 상인에게서 구매합니다.
- **Keys & key rings(열쇠 & 열쇠고리)** — 땜장이는 상자와 집을 위한 열쇠(와 그에 맞는 자물쇠)를
  만들고, 열쇠고리는 그것들을 한 묶음 담습니다. 땜질 메뉴에서 제작(`Key`는 주괴 3개,
  **20.0–70.0**).
- **Tinker traps(땜장이 함정)** — 땜질 메뉴는 전리품을 지키기 위한 함정 설치형 컨테이너(다트, 독,
  폭발 함정)도 만듭니다. [땜질(Tinkering)](/ko/skills/tinkering/)과
  [제작 → 땜질(Tinkering)](/ko/crafting/tinkering/)을 보세요.
- **Dye tubs(염색통)** <img src="/img/items/0x0FAB.png" class="uo-sprite" alt="" width="56" /> —
  제작 도구가 아니라 채색 유틸리티: 천이나 아이템을 넣고 색조를 골라 염색합니다. 색 공간은
  [색조 참조(Hue Reference)](/ko/reference/hues/)에 있습니다.

## 빠른 참조

스킬 범위는 레시피를 처음 시도할 → 마지막으로 보장되는 땜질 스킬입니다(`DefTinkering.cs`).
"Random 25–75"는 땜장이가 만든 도구의 `BaseTool` 기본값입니다.

| Tool | 쓰이는 스킬 | 하는 일 | 사용 횟수 | 구하는 법 |
|------|--------------|--------------|------|------------|
| Tinker's Tools | [땜질(Tinkering)](/ko/skills/tinkering/) | 땜질 메뉴를 엶 | random 25–75 | 땜장이(10–60) 또는 땜장이 상인 |
| Smith's Hammer | [대장기술(Blacksmithy)](/ko/skills/blacksmithy/) | 대장간에서 무기 & 방어구 제작 | random 25–75 | 땜장이(40–90) 또는 대장 상인 |
| Tongs | [대장기술(Blacksmithy)](/ko/skills/blacksmithy/) | 대장간 / 광석 취급 | random 25–75 | 땜장이(35–85) 또는 대장 상인 |
| Sewing Kit | [재봉(Tailoring)](/ko/skills/tailoring/) | 재봉 메뉴를 엶 | random 25–75 | 땜장이(10–70) 또는 재단사 상인 |
| Scissors | [재봉(Tailoring)](/ko/skills/tailoring/) | 재봉 메뉴; 천/필/생가죽 절단 | **50** | 땜장이(5–55) 또는 재단사 상인 |
| Saw / Dovetail Saw | [목공(Carpentry)](/ko/skills/carpentry/) | 목공 메뉴를 엶 | random 25–75 | 땜장이(30–80) 또는 목수 상인 |
| Moulding/Jointing/Smoothing Plane | [목공(Carpentry)](/ko/skills/carpentry/) | 목공 메뉴를 엶 | random 25–75 | **판자**로 땜장이(0–50) 또는 목수 상인 |
| Draw Knife / Froe / Inshave | [목공(Carpentry)](/ko/skills/carpentry/) | 목공 메뉴를 엶 | random 25–75 | 땜장이(30–80) 또는 목수 상인 |
| Fletcher's Tools | [활 제작(Bowcraft)](/ko/skills/bowcraft-fletching/) | 활 제작 메뉴를 엶 | random 25–75 | 땜장이(35–85) 또는 활장인 상인 |
| Scribe's Pen | [필사(Inscription)](/ko/skills/inscription/) | 필사 메뉴를 엶 | random 25–75 | 땜장이(25–75) 또는 필경사 상인 |
| Mortar & Pestle | [연금술(Alchemy)](/ko/skills/alchemy/) | 연금술 메뉴를 엶 | random 25–75 | 땜장이(20–70) 또는 연금술사 상인 |
| Skillet / Flour Sifter / Rolling Pin | [요리(Cooking)](/ko/skills/cooking/) | 요리 메뉴를 엶 | random 25–75 | 땜장이(프라이팬 30–80, 체 50–100, 밀대 판자 0–50) 또는 요리사 상인 |
| Mapmaker's Pen | [지도 제작(Cartography)](/ko/skills/cartography/) | 지도 제작 메뉴를 엶 | random 25–75 | 땜장이(25–75) 또는 지도 제작자 상인 |
| Pickaxe | [채광(Mining)](/ko/skills/mining/) | 광석 채굴(약한 도끼 무기이기도 함) | **50** | 땜장이/대장 또는 잡화상 |
| Shovel | [채광(Mining)](/ko/skills/mining/) | 광석 파기 | **50** | 땜장이(40–90) 또는 잡화상 |
| Hatchet / Axe | [벌목(Lumberjacking)](/ko/skills/lumberjacking/) | 통나무 베기, 판자 자르기(무기이기도 함) | 무기 내구도 | 대장 또는 무기 상인 |
| Fishing Pole | [낚시(Fishing)](/ko/skills/fishing/) | 낚시(물 타게팅) | **150** | 어부/잡화상 상인 또는 제작 |
| Lockpicks | [자물쇠 따기(Lockpicking)](/ko/skills/lockpicking/) | 잠긴 상자/문 따기 | 쌓임(소모) | 땜장이(45–95) 또는 도둑 상인 |
| Keys / Key Rings | — | 상자 & 집 잠금/해제 | 해당 없음 | 땜장이(열쇠 20–70) |
| Dye Tub | — | [색조](/ko/reference/hues/)로 천/아이템 재염색 | 재사용 가능 | 땜장이 상인 / 보상 |

## 함께 보기

- [땜질(Tinkering)](/ko/skills/tinkering/) — 이들 대부분을 만드는 스킬 · [제작 개요](/ko/crafting/) · [제작 메뉴 작동 방식](/ko/playing/crafting/)
- [자원 채집(Gathering resources)](/ko/playing/gathering-resources/) · [자원(Resources)](/ko/items/resources/) — 채집 도구가 월드에서 뽑아내는 것
- [상인 & 은행](/ko/playing/vendors-and-banking/) — 도구를 사는 곳 · [타게팅(Targeting)](/ko/playing/targeting/)
- [도구 카탈로그](/ko/items/catalog/tools/) — 소스에 있는 모든 도구 아이템과 아트, 아이템 ID · [아이템 개요](/ko/items/)
