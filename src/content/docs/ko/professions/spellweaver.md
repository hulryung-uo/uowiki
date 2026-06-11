---
title: 주문직조사 (Spellweaver / Arcanist)
description: 아케이니스트 — 주변에 직조사가 많을수록 Arcane Circle이 강해지는 지원·유틸리티 캐스터. 스킬, 빌드, 전투 방법, 장비, 수입.
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Spellweaving/ (ArcaneCircle.cs, ArcaneEmpowerment.cs, GiftOfRenewal.cs, GiftOfLife.cs, Wildfire.cs, WordOfDeath.cs, SummonFey.cs, SummonFiend.cs, NatureFury.cs, Thunderstorm.cs, ReaperForm.cs)"
last_verified: 2026-06-11
generated: false
---

## 이 직업은 무엇인가

주문직조사(아케이니스트, Arcanist)는 [Spellweaving](/ko/skills/spellweaving/)(주문직조)을
기반으로 한 지원·유틸리티 캐스터로, Mondain's-Legacy 시대의 학파다. 이 샤드(shard)에서
Spellweaving은 실제로 작동한다(EJ 익스팬션 스택에는 ML 스킬이 포함된다). 한 캐릭터의
유일한 학파인 경우는 드물다 — [메이지](/ko/professions/mage/), [미스틱](/ko/professions/mystic/),
[테이머](/ko/professions/tamer/) 위에 얹어 치유·버프·소환·광역 피해를 더한다.

## 핵심 스킬

- [Spellweaving](/ko/skills/spellweaving/)(주문직조) — 시전 스킬. 주문 위력과 보유 가능한 Arcane Focus의 강도를 결정한다.
- 중심을 잡을 주 학파 — [Magery](/ko/skills/magery/)(마법) + [Evaluating Intelligence](/ko/skills/evaluating-intelligence/)(지능 평가), [Mysticism](/ko/skills/mysticism/)(미스티시즘) + [Focus](/ko/skills/focus/)(집중), 또는 [테이머](/ko/professions/tamer/)를 위한 펫 스킬.
- 마나 공급과 생존을 위한 [Meditation](/ko/skills/meditation/)(명상)과 [Resisting Spells](/ko/skills/resisting-spells/)(마법 저항).

## Arcane Circle 메커니즘

Spellweaving의 상징은 **Arcane Circle**이다. 그 안에 서면(다른 직조사들이 모이는 곳에서
시전) 직조 주문을 강화하는 **Arcane Focus**를 얻는다 — 그리고 **주변에 주문직조사가 많을수록
포커스가 강해진다**. 그래서 그룹 친화적인 학파다. *Arcane Empowerment*는 다음 직조의
강도/지속을 추가로 끌어올린다. 둘 다 확인됨: `servuo: Scripts/Spells/Spellweaving/ArcaneCircle.cs`와
`ArcaneEmpowerment.cs`. 솔로일 때도 아이템(아케인 로브/젬)으로 포커스를 얻지만, 더 약하다.

## 빌드

아직 **전용 주문직조사 템플릿 페이지는 없다**. Spellweaving을 캐스터에 추가하는 한
슬롯으로 취급하라: [메이지 템플릿](/ko/templates/mage/)(또는 테이머/미스틱 분배)에서 시작해
높은 Int 캐스터 스탯을 유지하고 [Spellweaving](/ko/skills/spellweaving/)을 끼워 넣는다.
700포인트 계산은 [7x GM 템플릿](/ko/templates/seven-gm/)을 참고하라.

## 플레이 방법

[매직 스쿨](/ko/playing/magic-schools/)은 Spellweaving을 여러 학파 가운데 자리매김하고,
[주문 시전](/ko/playing/spellcasting/)은 시전을, [명상 & 마나](/ko/playing/meditation-and-mana/)는
마나를 다룬다.

도구 모음(모두 `servuo: Scripts/Spells/Spellweaving/`에서 확인됨):

- **Gift of Renewal** — 지속 회복 버프. **Gift of Life**는 지연성 자가/아군 부활 보험이다.
- **Arcane Empowerment** — 다음 직조를 강화한다. **Attune Weapon**은 들어오는 피해를 흡수한다.
- **Summon Fey** / **Summon Fiend** — 소환 전투 동료. **Nature's Fury**는 공격적인 무리를 소환한다.
- **Wildfire** / **Thunderstorm** — 무리를 정리하는 지속 광역 피해.
- **Word of Death** — 약해진 대상에게 강력한 피해.
- **Reaper Form** — 속도를 주문 위력과 맞바꾸는 자가 변신.

## 장비

- [매직 아이템 속성](/ko/magic/) — 솔로 포커스를 주는 **아케인 로브/포커스** 아이템. 더해 주문용 **Spell Damage**, **Lower Mana Cost**, **Faster Casting**.
- [방어구](/ko/items/armor/) — 메이지 친화적으로 균형 잡힌 저항.
- Spellweaving은 많은 주문에서 여덟 가지 메이지 리에이전트 대신 **Arcane Focus** 충전을 사용한다. 포커스 아이템을 챙겨라.

## 돈 버는 법

주문직조사가 Spellweaving만으로 홀로 파밍하는 일은 드물다 — 그것은 당신의 주 학파나
펫이 이미 하는 일을 증폭한다: 자신을 치유·버프하고, 무리에 Wildfire를 떨어뜨리고,
Word of Death로 마무리한다. 그룹에서는 Arcane Circle이 모두의 직조를 강하게 만든다.
전리품은 [상점 & 은행 이용](/ko/playing/vendors-and-banking/)을 통해 팔아라.

## 함께 보기

- [메이지](/ko/professions/mage/)와 [미스틱](/ko/professions/mystic/) — 얹기 좋은 흔한 주 학파
- [테이머](/ko/professions/tamer/) — Spellweaving의 치유/소환을 펫과 짝짓는다
- [Spellweaving 스킬](/ko/skills/spellweaving/) · [매직 스쿨](/ko/playing/magic-schools/)
