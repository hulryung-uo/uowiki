---
title: 샘파이어 (Sampire)
description: 전설의 하이브리드 — 매 타격마다 생명을 흡수하고(Vampiric Embrace) Bushido로 무리를 휩쓰는 근접 캐릭터. 유명한 솔로 PvM 몬스터 학살자.
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Necromancy/VampiricEmbrace.cs; Scripts/Spells/Bushido/ (HonorableExecution.cs, LightningStrike.cs, MomentumStrike.cs, Confidence.cs); Scripts/Spells/Chivalry/ (ConsecrateWeapon.cs, EnemyOfOne.cs)"
last_verified: 2026-06-11
generated: false
---

## 이 직업은 무엇인가

샘파이어("samurai + vampire")는 Ultima Online에서 가장 유명한 PvM 템플릿이다: **매 타격마다
생명을 흡수하며** 보통 덱서라면 짓눌릴 몬스터 무리를 가볍게 떨쳐낸다. 이 샤드(shard)에서는
모든 구성 요소가 실제로 작동한다(EJ 익스팬션 스택에는 AOS, SE, ML 스킬이 포함된다). 이것은
자체 스킬이 아닌 융합 빌드로, 세 학파를 결합한다:

- [Necromancy](/ko/professions/necromancer/) → **Vampiric Embrace**(생명 흡수 형태)
- [Bushido](/ko/professions/samurai/) → Honor, Lightning Strike, 그리고 무기 Whirlwind 시너지
- 약간의 [Chivalry](/ko/professions/paladin/) → Consecrate Weapon과 Enemy of One

## 핵심 스킬

- [Necromancy](/ko/skills/necromancy/)(강령술) — 빌드를 정의하는 흡수 형태인 **Vampiric Embrace**를 시전할 만큼만(요구 스킬은 적당한 수준).
- [Bushido](/ko/skills/bushido/)(부시도) — **Honor**(Honorable Execution), **Lightning Strike**, **Confidence**, 그리고 양손 무기로 향상된 막기를 위해.
- [Chivalry](/ko/skills/chivalry/)(기사도) — **Consecrate Weapon**(대상의 가장 약한 저항을 노림)과 **Enemy of One**(단일 유형 대상에게 큰 피해)을 위한 소규모 투자로, 티딩 포인트로 지불한다([팔라딘](/ko/professions/paladin/) 참고).
- 무기 스킬 — 보통 [Swordsmanship](/ko/skills/swordsmanship/)(검술, **Whirlwind** 특수 공격과 내장 리치를 가진 양손 무기).
- [Tactics](/ko/skills/tactics/)(전술)와 [Anatomy](/ko/skills/anatomy/)(해부학) — 피해 배수, 필수.
- [Parrying](/ko/skills/parrying/)(막기)는 흔하다. [Healing](/ko/skills/healing/)(치유)은 흡수가 붕대를 대신하므로 선택 사항이다.

## 빌드

아직 **전용 샘파이어 템플릿 페이지는 없다**. 세 학파에서 빌려 오는 덱서로 빌드하라:
무기 + Tactics + Anatomy 핵심은 [워리어 템플릿](/ko/templates/warrior/)에서 시작한 뒤
Necromancy, Bushido, 약간의 Chivalry를 그 주위에 끼워 넣는다. 빡빡한 조합이다 —
700포인트 예산은 [7x GM 템플릿](/ko/templates/seven-gm/)을 참고하라. 샘파이어는 흔히
Necromancy와 Chivalry를 GM 미만(핵심 주문이 요구하는 만큼만)으로 운용해 전투 핵심에
포인트를 확보한다.

## 플레이 방법 — 루프

특수 공격과 무기 속도는 [전투 심화](/ko/playing/combat-advanced/)를 읽어라. 이 빌드는
그것에 따라 살고 죽는다. 상징적인 루프:

1. **Vampiric Embrace** 활성화(시전 후 형태 유지) — 이제 모든 일격이 당신을 치유한다.
2. 까다로운 대상을 **Honor**(Bushido)한 뒤, 교전 전에 **Consecrate Weapon** + **Enemy of One**(Chivalry).
3. 무리 속으로 **Whirlwind** — 여러 적을 동시에 때리는 것은 여러 동시 생명 흡수를 뜻하므로, 무리가 오히려 당신을 더 빨리 *치유*한다.
4. 핵심 휘두름의 명중을 위해 **Lightning Strike**를 끼우고, 집중 공격을 받을 때는 **Confidence**/**Evasion**과 Parrying에 기대라.

흡수가 때리는 대상 수에 따라 스케일링하므로, 샘파이어는 몬스터 무리를 상대로 솔로에서
거의 죽지 않는다 — 전설적인 PvM 파머로 통하는 이유다. (메커니즘 확인됨:
`servuo: Scripts/Spells/Necromancy/VampiricEmbrace.cs`, Bushido 파일들, 그리고
`Scripts/Spells/Chivalry/ConsecrateWeapon.cs` / `EnemyOfOne.cs`.)

## 장비

- [무기](/ko/items/weapons/)와 [무기 카탈로그](/ko/items/catalog/weapons/) — **Whirlwind** 특수 공격과 **Hit Life Leech**를 가진 양손 무기. 많은 플레이어가 노다치나 더블 액스를 선호한다.
- [매직 아이템 속성](/ko/magic/) — **Hit Life Leech**, **Hit Lower Defense**, **Swing Speed Increase**, **스태미나/마나** 지속, 그리고 저항 상한을 쌓아라. Faster Casting은 소수의 버프 시전에만 도움이 된다.
- [방어구](/ko/items/armor/) — Vampiric Embrace는 알려진 원소 약점을 동반하므로, 그것이 노출시키는 저항을 상한까지 메워라.

## 돈 버는 법

샘파이어는 최고의 **솔로 PvM 파머**다: 다른 솔로 템플릿이 버티지 못하는 고티어 던전
무리와 보스를 정리하며 모든 것을 줍는다. Chivalry용으로 금화를 티딩하고, 형태 재시전을
위한 Necromancy 리에이전트를 챙기고, 수확물은 [상점 & 은행 이용](/ko/playing/vendors-and-banking/)을
통해 팔아라.

## 함께 보기

- [네크로맨서](/ko/professions/necromancer/) · [사무라이](/ko/professions/samurai/) · [팔라딘](/ko/professions/paladin/) — 융합되는 세 학파
- [워리어](/ko/professions/warrior/) — 덱서의 기반
- [전투 심화](/ko/playing/combat-advanced/) · [7x GM 템플릿](/ko/templates/seven-gm/)
