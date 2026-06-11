---
title: 샤드 신분증
description: 이 샤드를 한눈에 — 확장팩, 스킬과 스탯 한계, 그리고 핵심 비율을, 서버 설정에서 직접.
status: source-verified
sources:
  - "servuo: Config/Expansion.cfg"
  - "servuo: Config/PlayerCaps.cfg"
  - "servuo: Config/General.cfg"
  - "servuo: Config/TestCenter.cfg"
last_verified: 2026-06-11
generated: false
---

:::note[여기서 "ServUO"가 의미하는 것]
**샤드**는 구동 중인 울티마 온라인 게임 세계(서버 인스턴스)입니다. 이 샤드는
**[ServUO](https://www.servuo.com/)** — 오픈소스 울티마 온라인 **서버 에뮬레이터** — 위에서
구동됩니다: 커뮤니티가 자체 세계를 호스팅할 수 있도록 UO 서버를 재구현하는 소프트웨어입니다.
그래서 이 위키 전체에서 "ServUO"는 (규칙과 수치가 정의된) 그 에뮬레이터의 소스 코드를 가리키며,
라이브 서버 자체가 아닙니다.
:::

하나의 샤드, 하나의 규칙 집합 — 이것들은 이 샤드가 실제로 구동 중인 수치이며, ServUO
에뮬레이터의 설정 `Config/*.cfg`에서 직접 읽은 것입니다.

## 확장팩

| 설정 | 값 | 출처 |
|---------|-------|--------|
| 확장팩 | **EJ (Endless Journey)** | `Config/Expansion.cfg` (`CurrentExpansion=EJ`) |
| 테스트 센터 모드 | 비활성화 | `Config/TestCenter.cfg` (`Enabled=False`) |

EJ는 ServUO 에뮬레이터가 제공하는 가장 현대적인 룰셋입니다: AOS 전투 계산, ML 시대 스탯 상승,
SA 종족과 스킬이 모두 적용됩니다. 이 위키가 "AOS 시대" 또는 "ML 시대" 동작이라고 말하는 곳은,
여기에 적용됩니다.

## 스킬 한계 (`Config/PlayerCaps.cfg`)

| 설정 | 값 | 메모 |
|---------|-------|-------|
| 개별 스킬 한계 | **100.0** (`SkillCap=1000`) | 해당되는 경우 파워 스크롤로 스킬별 상향 가능. |
| 총 스킬 한계 | **700.0** (`TotalSkillCap=7000`) | 한계에서, 새 상승은 다른 스킬을 내림(아래 화살표)으로 설정해야 함. |
| 안티 매크로 코드 | **비활성화** (`EnableAntiMacro=False`) | 동일 위치/동일 대상 상승 제한 없음. [스킬 상승](/ko/mechanics/skill-gain/) 참고. |

## 스탯 한계 (`Config/PlayerCaps.cfg`)

| 설정 | 값 |
|---------|-------|
| 총 스탯 한계 | **225** (`TotalStatCap=225`) |
| 힘 / 민첩 / 지능 한계 | 각 **125** (`StrCap`/`DexCap`/`IntCap=125`) |
| 강화 스탯별 최대치 | 각 **150** (`StrMaxCap`/`DexMaxCap`/`IntMaxCap=150`) |
| 스탯 상승 확률 | 적격 스킬 사용당 **5%** (`PlayerChanceToGainStats=5.0`) |
| 스탯 상승 시간 지연 | **비활성화** (`EnablePlayerStatTimeDelay=False`) |
| 펫 스탯 상승 확률 / 지연 | 5% / 비활성화 (`PetChanceToGainStats=5.0`, `EnablePetStatTimeDelay=False`) |

이것들이 어떻게 상호작용하는지의 세부 사항: [스탯 상승 메커니즘](/ko/mechanics/stat-gain/).

## 세계 동작 (`Config/General.cfg`)

| 설정 | 값 |
|---------|-------|
| 땅 아이템 부패 | **60분** (`DefaultItemDecayTime=60`) |
| 살인자(레드) | **Felucca 전용** (`RestrictRedsToFel=True`) |

## 더 보기

- [서버 규칙과 비율](/ko/shard/server-rules/) — 주택, 전리품 예산, 보물 지도, 벤더, 저장과
  재시작
- [시작하기](/ko/guides/getting-started/) — 이것이 어떤 종류의 샤드이고 누가 사는지
