---
title: 플레이 방법 — 보물 사냥
description: 우리 샤드의 보물 사냥꾼 플레이 스타일 — 보물 지도를 찾거나 사고, 지도 제작으로 해독하고, 채광으로 상자를 파내고, 수호자와 싸우고, 함정 상자를 따 금화, 보석, 마법 장비, 파워 스크롤, 특수 스크롤을 얻기. 다섯 가지 Forgotten-Treasures 지도 단계(Stash, Supply, Cache, Hoard, Trove), 다섯 가지 전리품 패키지, 관련 스킬, 그리고 상자가 묻힌 곳을 다룬다.
status: source-verified
sources:
  - "servuo: Scripts/Services/TreasureMaps/TreasureMap.cs (decode, dig, dig range, guardians, spawn tables, location randomization)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapInfo.cs (levels, packages, decode difficulty, chest skills, loot tables)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapChest.cs (chest, trap, artifacts)"
  - "servuo: Scripts/Items/Tools/MapItem.cs (decoded-map gump 0x139D)"
  - "servuo: Config/TreasureMaps.cfg (Enabled=True, LootChance=.01, ResetTime=30.0)"
  - "servuo: Config/Expansion.cfg (CurrentExpansion=EJ -> modern system live)"
  - "servuo: Data/treasure.cfg (193 classic dig sites)"
  - "client art: gumpartLegacyMUL.uop gump 0x139D (map-window parchment)"
last_verified: 2026-06-11
generated: false
---

**보물 사냥**은 탐험가의 직업입니다: 보물 지도를 구하고, 해독하여 상자가 묻힌 곳을 드러내고,
그곳으로 여행하고, 파내고, 땅에서 솟아오르는 몬스터와 싸운 뒤, 상자의 잠금을 풀고 함정을 해제해
전리품을 얻습니다. 다재다능한 캐릭터에게 보상하며 금화, 보석, 마법 장비로, 그리고 최상위
등급에서는 파워 스크롤과 특수 스킬 스크롤로 보답합니다.

> **여기서 어떤 시스템이 돌아가는가.** 우리 샤드는 확장팩 **EJ**(`Config/Expansion.cfg` →
> `CurrentExpansion=EJ`)를 구동하므로, `TreasureMapInfo.NewSystem`이 **true**이며 현대적인
> **Forgotten Treasures** 보물 지도 시스템이 가동 중입니다. 지도는 더 오래된 "1–7단계" 번호가
> 아니라 다섯 단계 **Stash, Supply, Cache, Hoard, Trove**와 전리품 **패키지**를 가집니다. 이
> 페이지의 수치와 표는 EJ 코드 경로와 대조해 소스 검증되었습니다.

## 보물 사냥이란

전체 루프, 순서대로:

1. **지도를 구하세요.** 보물 지도는 몬스터에게서 드롭되거나(아래 참고) 다른 플레이어에게서
   사고/거래됩니다.
2. **해독하세요.** 지도를 더블클릭하면 [지도 제작(Cartography)](/ko/skills/cartography/) 스킬
   검사가 해독하여 빨간 핀으로 파는 지점을 표시합니다(`TreasureMap.Decode`, `DisplayTo`).
3. **그 지점으로 여행하세요.** 해독된 지도는 작은 지역 풍경을 보여 줍니다; 그 실제 위치로 항해하거나
   말을 탑니다.
4. **파세요.** 굴착 도구([채광(Mining)](/ko/skills/mining/) 도구)를 들고 핀 근처에 서서 파세요.
   당신의 스킬이 얼마나 가까이 있어야 하는지 정합니다(`DigTarget`).
5. **수호자와 싸우세요.** 파기를 마치면 지도 단계에 맞춰진 몬스터 넷이 스폰됩니다(`DigTimer`).
   그것들을 살아남으세요.
6. **상자를 여세요.** 상자는 **잠겨 있고 함정이 설치**되어 있습니다 —
   [자물쇠 따기(Lockpicking)](/ko/skills/lockpicking/)로 잠금을 따고
   [함정 해제(Remove Trap)](/ko/skills/remove-trap/)로 해제(또는 폭발을 감수)한 뒤,
   약탈하세요.

사람들이 보물을 사냥하는 것은 보상 때문입니다: 상자당 수만 금화, 보석 한 자루, 무작위 마법
무기/갑옷/장신구, 그리고 더 높은 등급에서는 **파워 스크롤**, **초월 스크롤(scrolls of
transcendence)**, **민첩 스크롤(scrolls of alacrity)**.

## 보물 지도 아이템

모든 지도는 **단계(level)**와 **패키지(package)**를 가집니다. 단계는 난이도와 전리품 예산을
정하고, 패키지는 장비와 스크롤을 한 플레이 스타일로 테마화합니다.

**단계**(enum `TreasureLevel`), 쉬운 것부터 어려운 것까지:

| 단계 | 해독 난이도 | 상자 요구 스킬 | 마법 아이템 | 금화 범위 |
|---|---|---|---|---|
| **Stash** | 100 | 5 | 6 | 10,000–40,000 |
| **Supply** | 200 | 45 | 8 | 20,000–50,000 |
| **Cache** | 300 | 75 | 12 (Assassin은 24) | 30,000–60,000 |
| **Hoard** | 400 | 80 | 18 | 40,000–70,000 |
| **Trove** | 500 | 80 | 36 | 50,000–70,000 |

*해독 난이도*는 `AssignChestQuality`/해독 표입니다(`Utility.Random(difficulty)`를 당신의 지도
제작과 비교). *상자 요구 스킬*, *마법 아이템 수*, *금화 범위*는 `TreasureMapInfo.Fill`,
`GetEquipmentAmount`, `GetGoldCount`에서 나옵니다.

**패키지**(enum `TreasurePackage`) — 전리품 테마:

- **Artisan** — 제작 도구/자원, 레시피, 지도 제작자/제작자 보상품.
- **Assassin** — 단검, 경갑, 은신/독 풍미 전리품(그리고 Cache에서 더 많은 마법 아이템).
- **Mage** — 지팡이, 로브/가죽, 시약(Stash에서), 시전자 스크롤.
- **Ranger** — 활, 가죽/스터드 갑옷, 궁술/조련 풍미.
- **Warrior** — 중무기, 플레이트 갑옷과 방패, 근접 스크롤.

**지도는 어디서 오는가.** 지도는 기본 확률 **`LootChance = .01`**(1%)로 몬스터 전리품으로
드롭되며, 생물별로 재정의 가능합니다(`Config/TreasureMaps.cfg`, `TreasureMap.LootChance`). 파낸
상자 자체가 다음 단계 지도를 담을 수 있습니다: Trove 미만 단계에서는 상자가 한 단계 높은 지도를
드롭할 10% 확률이 있습니다(`TreasureMapInfo.Fill`). 해독된 지도는 **축복(blessed)**되어 당신에게
남습니다.

## 보물 사냥꾼의 스킬

보물 사냥은 넓은 캐릭터를 만드는 정석적 이유입니다 — 끝에서 끝까지 여러 스킬을 건드리며, 그래서
[7-GM 템플릿](/ko/templates/seven-gm/)과 자연스럽게 어울립니다.

- **[지도 제작](/ko/skills/cartography/)** — 지도를 **해독**합니다. 단계가 높을수록 더 많은 지도
  제작이 필요합니다(위의 해독 난이도 표). 이 현대 시스템에서 지도 제작은 *또한* 파기 범위(아래)와
  상자의 품질 굴림(`AssignChestQuality`)을 좌우합니다.
- **[채광](/ko/skills/mining/)** — 상자를 파내려면 **굴착 도구**(아무 채광 채집 도구, 예: 삽이나
  곡괭이)를 들고 있어야 합니다(`TreasureMap.HasDiggingTool`).
- **[자물쇠 따기](/ko/skills/lockpicking/)** — 상자는 잠겨 있습니다; 그 잠금 레벨은 상자의
  *요구 스킬 − 10*이고 최대 잠금 레벨은 *요구 스킬 + 40*입니다(`TreasureMapInfo.Fill`).
- **[함정 해제](/ko/skills/remove-trap/)** — 모든 상자에는 **폭발 함정**(`TrapType.ExplosionTrap`)이
  설치되어 있습니다; 터지기 전에 해제하세요.
- **전투 / [마법술](/ko/magic/) / [조련](/ko/playing/taming-and-pets/)** — 파기에서 스폰되는
  수호자를 처리하기 위해. [전투 기초](/ko/playing/combat-basics/)를 참고하세요.

### 파기 범위

파기 위해 핀에 얼마나 가까이 대상 지정해야 하는지는 당신의 **지도 제작**에 달려 있습니다(현대
시스템은 범위에 채광이 아니라 지도 제작을 사용 — `DigTarget.OnTarget`):

| 지도 제작 | 최대 파기 범위 |
|---|---|
| 100+ | 4타일 |
| 81–99 | 3타일 |
| 51–80 | 2타일 |
| 51 미만 | 1타일 |

너무 멀리 대상 지정하면 지도가 어느 방향으로 움직일지 알려 주고; 8타일 안에서는 "very
close"라고 말합니다.

## 지도 읽기 (gump)

해독된 보물 지도는 정확히 그것입니다 — **묻힌 상자에 핀 하나가 꽂힌, 세계 한 조각을 지도 제작으로
그린 지도**. 좌표 목록이 아니라, 당신이 알아봐야 할 지형의 그림입니다.

기계적으로(`servuo: Scripts/Services/TreasureMaps/TreasureMap.cs`), 지도가 만들어질 때 상자
주변 브리타니아(Felucca/Trammel)의 **600 × 600타일 지역**을 포착하며 — 다른 페이싯에서는 더
작습니다(300 × 300, 또는 Ter Mur에서는 200 × 200) — 작은 양피지 gump로 보여 줍니다(해독된 지도
아이템은 그래픽 `0x14EC`). 그런 다음 지도는 `AddWorldPin(ChestLocation)`을 호출해 그 지점에
**핀 하나**를 떨굽니다.

결정적으로, 상자는 **중앙에 있지 않습니다**: 포착된 창이 오프셋되어 파는 지점이 지도를 가로질러
4분의 1과 4분의 3 사이 어딘가에 놓입니다
(`x1 = ChestLocation.X − RandomMinMax(width/4, 3·width/4)`). 그래서 그냥 가운데로 항해할 수
없습니다 — 핀 주변의 **해안선, 강, 도로, 랜드마크를 읽고**, 실제 세계와 맞추고, 그곳으로
말을 타거나 항해해, 그 정확한 지점의 범위 안에서 파야 합니다.

![해독된 보물 지도의 예: 양피지 두루마리에 잉크로 그린 해안선과, 파는 지점에 중앙에서 벗어나 꽂힌 번호 매겨진 핀](/img/treasure/example-map.png)

*해독된 지도의 예로, 클라이언트가 보여 주는 방식대로 그려진 것 — 양피지 두루마리에 손으로 잉크로
그린 해안선 윤곽(고전적인 해치 틱과 함께)을, 실제 클라이언트 gump 아트로 틀을 두름: "Plot
Course" 제목 바(gump `0x1398`), 나무 막대 두루마리 틀(`0x1432`), 그리고 나침반 장미(`0x139D`).
번호 매겨진 핀이 파는 지점에서 중앙을 벗어나 앉아 있어, 세계에서 일치하는 지점을 찾기 위해 주변
해안선을 읽습니다.*

## 파기 위치

상자의 지점이 선택되는 방식에는 두 가지가 있고, 어디서 파게 되는지에 영향을 줍니다:

- **고전 고정 장소("파는 지점").** `Data/treasure.cfg`는 **193개의 하드코딩된**
  브리타니아(Felucca/Trammel) 좌표를 나열합니다 — 플레이어가 *그* 파기 위치로 여기는 잘 알려진
  보물 지점들. 무작위 위치가 **꺼져** 있을 때 `GetRandomClassicLocation()`이 이를 사용합니다.
- **우리 샤드의 현대적 무작위 지도.** `Config/TreasureMaps.cfg`가 **`Enabled=True`**
  (`TreasureMap.NewChestLocations`)이므로, 라이브 지도는 대신 **각 페이싯의 팔 수 있는 지역 안에서
  상자를 무작위화**합니다(`TreasureMap.GetRandomLocation`). Felucca와 Trammel의 경우 그 지역은
  **지도 전체**(`0,0 → 5119,4095`)입니다; Tokuno, Malas, Ilshenar, Ter Mur, Eodon은 특정
  사각형을 사용합니다. 선택된 타일은 `ValidateLocation`으로 검증됩니다 — 마을, 주택, 던전,
  챔피언 스폰 지역, 도로, 그리고 걷거나 자연스럽지 않은 타일을 거부하여(흙/풀/정글/숲/눈만 허용),
  상자는 항상 열린 황야에 놓입니다.

아래 지도는 브리타니아 전역의 전통적 분포를 볼 수 있도록 Felucca의 **193개 고전 장소**를
표시합니다. 우리 샤드에서는, 오늘날 지도가 가리키는 정확한 목록이라기보다 보물이 선호하는 지형의
*종류*에 대한 안내로 보세요.

![193개의 모든 고전 보물 파기 장소가 금색 X 표시로 그려진 브리타니아 지도](/img/treasure/locations.png)

*`Data/treasure.cfg`의 193개 모든 고전 파기 장소를 Felucca 지도에 표시함.*

**정확한 좌표를 원하나요?** 모든 장소의 절대 (X, Y) — 가장 가까운 도시와 지도로 점프하는 링크와
함께 — 는 **[보물 지도 파기 장소](/ko/playing/treasure-locations/)**에 나열되어 있습니다.

## 상자와 전리품

**수호자.** 파기를 마치면 상자에 **4**마리의 몬스터가 스폰됩니다(`DigTimer.OnTick`). 현대
시스템에서 각 스폰은 `(Guardian)`으로 태그될 **70%** 확률을 가집니다. 지도 단계와 페이싯에 맞춰
비례합니다(`TreasureMap.Spawn` 표) — Felucca/Trammel의 경우, 대략:

- **Stash** — mongbat, ratman, skeleton, zombie, headless.
- **Supply** — orcish mage, gargoyle, gazer, hell hound, earth elemental.
- **Cache** — lich, ogre lord, dread spider, elemental, lich lord, daemon, elder gazer.
- **Hoard** — ancient wyrm, balron, blood/poison elemental, titan.
- **Trove** — blood/poison elemental, cold drake, frost dragon/drake, greater dragon.

**여는 법.** 상자는 잠겨 있고 **폭발 함정**을 지닙니다; [자물쇠 따기](/ko/skills/lockpicking/)로
잠금을 따고 [함정 해제](/ko/skills/remove-trap/)로 해제하세요. 상자 **품질**(Rusty / Standard /
Gold)은 파는 시점에 당신의 지도 제작에서 굴려지며 보석, 시약, 재료 수를 늘립니다.

**전리품**(`TreasureMapInfo.Fill`), 안에 든 것별로:

- **금화** — 단계에 맞춰진 금화 한 자루(위 표 참고)에 더해, 상자 품질과 단계에 따라 수가 늘어나는
  **보석 한 자루**.
- **마법 장비** — 지도의 **패키지**로 테마화된 무작위 마법 무기, 갑옷, 장신구, 단계 표의 수만큼
  (Stash → Trove에서 6 → 36개 아이템).
- **시약** — **Stash + Mage** 지도에서만(상자 품질에 따라 20/40/60).
- **제작 자원과 특수 재료** — **Artisan** 지도에서(잉곳, 보드, 가죽; Ter Mur에서는 임뷰 재료
  등).
- **특수 / 마이너 아티팩트 전리품과 장식품** — Supply부터 위로 확률 증가.
- **파워 스크롤** — **Felucca 전용**, **Cache 이상**에서, 패키지의 스킬로 **+110**
  (`GetPowerScrollList`).
- **초월 스크롤** — Supply/Cache를 제외한 대부분의 단계에서(`GetTranscendenceList`).
- **민첩 스크롤** — Stash를 제외한 대부분의 단계에서(그리고 Felucca의 Cache 제외)
  (`GetAlacrityList`).

마법 장비와 특수 아이템은 패키지로 테마화되고 단계별 예산 안에서
`RunicReforging.GenerateRandomItem`이 만듭니다. 개별 드롭이 무엇인지는
[아이템 참조](/ko/items/)를 참고하세요.

## 함께 보기

- [지도 제작](/ko/skills/cartography/) · [채광](/ko/skills/mining/) ·
  [자물쇠 따기](/ko/skills/lockpicking/) · [함정 해제](/ko/skills/remove-trap/)
- [7-GM 템플릿](/ko/templates/seven-gm/) · [전투 기초](/ko/playing/combat-basics/) ·
  [조련과 펫](/ko/playing/taming-and-pets/)
- [자원 채집](/ko/playing/gathering-resources/) · [아이템 참조](/ko/items/)

위치는 `Data/treasure.cfg`에서 표시함; 지도 아트와 해독된 지도 양피지는 클라이언트 자체의 저작권
문제 없는 에셋입니다.
