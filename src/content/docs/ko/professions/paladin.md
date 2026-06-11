---
title: 팔라딘 (Paladin)
description: 성스러운 전사 — 십일조 포인트로 Chivalry를 시전하는 덱서. 핵심 스킬, 빌드, 싸우는 법, 장비, 그리고 수입을 한곳에.
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Chivalry/ (PaladinSpell.cs tithing cost; ConsecrateWeapon.cs, EnemyOfOne.cs, DivineFury.cs, CloseWounds.cs, CleanseByFire.cs, HolyLight.cs, DispelEvil.cs, RemoveCurse.cs, SacredJourney.cs)"
last_verified: 2026-06-11
generated: false
---

## 이 직업은 무엇인가

팔라딘(paladin)은 성스러운 주문서를 장착한 근접 전사다. 그 핵심은
[워리어](/ko/professions/warrior/) — 무기, Tactics, 붕대 — 이지만,
[Chivalry](/ko/skills/chivalry/)(기사도)가 자기 버프, 가벼운 치유, 저주 제거, 무료 이동을
얹어준다. 이 샤드의 Chivalry는 실재한다(확장 스택에 AOS 시대 스킬이 포함됨), 그리고 마나가
들지 않는다: 그 힘은 **십일조 포인트(tithing points)**로 돌아간다.

## 핵심 스킬

- [Chivalry](/ko/skills/chivalry/)(기사도) — 성스러운 학파. Chivalry가 높을수록 주문 효과가 더 강하고 안정적이며 버프 지속 시간이 길어진다.
- **무기 스킬** — [Swordsmanship](/ko/skills/swordsmanship/), [Fencing](/ko/skills/fencing/), 또는 [Mace Fighting](/ko/skills/mace-fighting/). Chivalry는 보조이고, 죽이는 일은 무기가 한다.
- [Tactics](/ko/skills/tactics/)와 [Anatomy](/ko/skills/anatomy/) — 워리어와 똑같은 두 피해 배수. Anatomy는 붕대 치유의 동력이기도 하다.
- [Healing](/ko/skills/healing/)(치유) — 붕대가 여전히 기본 회복 수단이고, Close Wounds는 보충일 뿐이다.
- 적대적 캐스터에 대한 생존력을 위한 선택 [Focus](/ko/skills/focus/) 또는 [Resisting Spells](/ko/skills/resisting-spells/).

## 마나가 아니라 십일조 포인트

Chivalry 주문은 마나가 아니라 **십일조 포인트(tithing points)**로 지불된다. 사원에서 금화를
기부해 얻는다(사원을 사용해 십일조를 선택). 시전할 때마다 그 풀에서 포인트가 소모되며,
바닥나면 다시 십일조를 바친다. 이는 에뮬레이터에서 확인된다 — `PaladinSpell.cs`는 마나가
아니라 `Caster.TithingPoints`를 확인하고 차감한다
(`servuo: Scripts/Spells/Chivalry/PaladinSpell.cs`). 버프를 항상 쓸 수 있도록 수천 금화를
십일조로 바쳐 두어라.

## 빌드

위키에는 아직 **전용 팔라딘 템플릿 페이지가 없다**. Chivalry 슬롯을 가진 덱서로 빌드하라:
스탯, 무기 스킬 순서, 사냥 루트는 [워리어 템플릿](/ko/templates/warrior/)에서 시작한 다음,
유틸리티 슬롯 하나를 [Chivalry](/ko/skills/chivalry/)로 교체하라. 전형적인 엔드게임 구성은
무기 + Tactics + Anatomy + Healing + Chivalry + Parrying + 하나 더다. 일곱 스킬을 700포인트
상한 아래에 맞추는 법은 [7x GM 템플릿](/ko/templates/seven-gm/)을 참고하라. (다크 매직과
생명력 흡수도 원한다면, Chivalry를 Necromancy 및 Bushido와 융합한
[샘파이어](/ko/professions/sampire/)를 보라.)

## 플레이 방법

캐스팅 학파들 사이에서 Chivalry가 어디 위치하는지는 [마법 학파](/ko/playing/magic-schools/)를,
시전 메커니즘은 [주문 시전](/ko/playing/spellcasting/)을 읽어라. 근접 쪽은
[전투 기초](/ko/playing/combat-basics/)에 이어 [전투 심화](/ko/playing/combat-advanced/)가
스윙 루프와 무기 특수 기술을 다루고, [치유](/ko/playing/healing/)가 붕대 타이밍을 다룬다.

루프: 먼저 금화를 십일조로 바친다. 전투 전에 **Consecrate Weapon**(피해 타입을 대상의 가장
약한 저항에 맞춤)과 **Enemy of One**(단일 생물 종류에 대한 큰 피해 보너스 — 단, 그 외 모든
것에게서 추가 피해를 받음)을 시전한다. **Divine Fury**는 방어를 대가로 스윙 속도를 더한다.
위급할 때는 **Close Wounds**가 치유하고, **Cleanse by Fire** / **Remove Curse**가 독과 저주를
벗겨낸다. **Holy Light**는 광역 누크, **Dispel Evil**은 소환수를 흩뜨리고, **Sacred Journey**는
팔라딘의 Recall이자 게이트다. 이 모두는 `servuo: Scripts/Spells/Chivalry/` 아래의 확인된
파일이다.

## 장비

- [무기](/ko/items/weapons/)와 [무기 목록](/ko/items/catalog/weapons/) — 무기 스킬에 맞춰 고르고, 덱서를 돕는 모드(흡수, 스윙 속도)는 평소대로 적용된다.
- [방어구](/ko/items/armor/) — 균형 잡힌 저항을 선호하라. 방패는 [Parrying](/ko/skills/parrying/)을 가능하게 한다.
- [마법 아이템 속성](/ko/magic/) — Faster Casting은 여기서 거의 의미가 없으므로(시전이 적음), 근접과 생존 모드를 우선하라. **붕대**를 챙겨라.

## 돈 버는 법

팔라딘은 워리어처럼 파밍한다: 던전 방을 청소하고 시체를 약탈한다. Chivalry 키트는 **언데드와
"악한" 콘텐츠**를 특히 수익성 있게 만든다 — Consecrate에 Enemy of One을 더하면 묘지나 언데드
던전을 갈아버리고, 성스러운 버프는 십일조로 바친 금화만 든다. 남는 전리품은
[상점 & 은행 이용](/ko/playing/vendors-and-banking/)을 통해 팔아라.

## 함께 보기

- [워리어](/ko/professions/warrior/) — 이 빌드가 올라타는 덱서 기반
- [샘파이어](/ko/professions/sampire/) — Chivalry도 조금 쓰는 흡수-근접 하이브리드
- [Chivalry 스킬](/ko/skills/chivalry/) · [마법 학파](/ko/playing/magic-schools/)
