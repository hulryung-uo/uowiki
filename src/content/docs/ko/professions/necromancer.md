---
title: 네크로맨서 (Necromancer)
description: 다크 캐스터 — 특수 리에이전트와 Spirit Speak로 굴러가는 저주, 언데드 소환, 자기 변신. 스킬, 빌드, 플레이, 장비, 수입.
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Necromancy/ (WraithForm.cs, LichForm.cs, HorrificBeast.cs, VampiricEmbrace.cs, CorpseSkin.cs, BloodOath.cs, AnimateDeadSpell.cs, SummonFamiliar.cs, Strangle.cs, PainSpike.cs, Wither.cs); special reagent use confirmed in spell files"
last_verified: 2026-06-11
generated: false
---

## 이 직업은 무엇인가

네크로맨서(necromancer)는 다크 캐스터다: 적을 저주하고, 죽은 자를 일으켜 부리며, 전투
이점을 위해 자신의 몸을 변형시킨다. 이 샤드에서 Necromancy(강령술)는 실재한다(EJ 확장
스택에 Age-of-Shadows 시대 스킬이 포함됨). 메이지([Magery](/ko/magic/) 유틸리티를 위해)나
무기 + Bushido와 자연스럽게 짝지어지며 — 후자가 그 유명한
[샘파이어](/ko/professions/sampire/)다.

## 핵심 스킬

- [Necromancy](/ko/skills/necromancy/)(강령술) — 캐스팅 스킬. 주문 위력, 성공률, 사용할 수 있는 주문을 결정한다.
- [Spirit Speak](/ko/skills/spirit-speak/)(영혼 대화) — Necromancy 효과를 강화하고 **또한** 근처 시체에서 생명력을 빨아들여 스스로를 치유하게 해준다. Spirit Speak 없는 네크로맨서는 반쪽짜리다.
- 보조: 완전한 캐스터를 위한 [Magery](/ko/skills/magery/) + [Evaluating Intelligence](/ko/skills/evaluating-intelligence/), **또는** 덱서 하이브리드를 위한 무기 스킬([Swordsmanship](/ko/skills/swordsmanship/) 등) + [Tactics](/ko/skills/tactics/)/[Anatomy](/ko/skills/anatomy/).
- [Meditation](/ko/skills/meditation/)(명상, 캐스터 빌드)과 [Resisting Spells](/ko/skills/resisting-spells/)가 마무리를 짓는다.

## 여덟 가지가 아닌 특수 리에이전트

Necromancy는 여덟 가지 메이지 리에이전트를 **사용하지 않는다**. 고유한 세트를 소비한다:
**배트 윙(bat wing), 그레이브 더스트(grave dust), 데몬 블러드(daemon blood), 녹스
크리스탈(nox crystal), 피그 아이언(pig iron)**. 메이지/리에이전트 벤더에게서 사서 두툼하게
비축해 두어라 — 각 주문이 고유한 조합을 명시한다. (`servuo: Scripts/Spells/Necromancy/`
아래의 주문 파일들에서 확인됨.) 리에이전트 위에, 시전 비용은 십일조가 아니라 마나로 낸다.

## 빌드

아직 **전용 네크로맨서 템플릿 페이지가 없다**. 캐스터 네크로맨서라면
[메이지 템플릿](/ko/templates/mage/)에서 시작해 Magery + Eval + Meditation + Resist와 함께
Necromancy + Spirit Speak를 끼워 넣어라. 근접 네크로맨서라면
[워리어 템플릿](/ko/templates/warrior/)에서 시작해 무기 코어 주위에 Necromancy + Spirit
Speak를 맞춰라. 어느 쪽이든, 이 모두를 700포인트 상한 아래에 욱여넣는 법은
[7x GM 템플릿](/ko/templates/seven-gm/)을 참고하라.

## 플레이 방법

캐스팅 모델은 [마법 학파](/ko/playing/magic-schools/)와 [주문 시전](/ko/playing/spellcasting/)을,
마나 회복은 [명상 & 마나](/ko/playing/meditation-and-mana/)를 읽어라. 근접 하이브리드는
[전투 심화](/ko/playing/combat-advanced/)도 읽어야 한다.

툴킷(모두 `servuo: Scripts/Spells/Necromancy/` 아래에서 확인됨):

- **변신** — *Wraith Form*(마나 흡수, 망령 몸), *Lich Form*(마나 재생, 화염 약점), *Horrific Beast*(근접 몸). *Vampiric Embrace*는 **모든 타격에 생명력 흡수**를 부여한다 — 샘파이어의 초석이다.
- **저주** — *Corpse Skin*, *Blood Oath*, *Strangle*, *Pain Spike*, *Wither*(광역)는 대상을 약화시키고 출혈시킨다.
- **언데드** — *Animate Dead*는 시체를 하인으로 일으키고, *Summon Familiar*는 개인 펫을 준다.
- **치유** — 전투 사이 [Spirit Speak](/ko/skills/spirit-speak/)로 시체에서 생명력을 빨아들인다.

## 장비

- [마법 아이템 속성](/ko/magic/) — 캐스터 네크로는 **Lower Reagent Cost**, **Lower Mana Cost**, **Spell Damage Increase**, **Faster Casting**을 원하고, 근접 네크로는 대신 흡수와 스윙 속도를 원한다.
- [방어구](/ko/items/armor/) — 균형 잡힌 저항. 일부 변신은 외형과 스탯을 덮어쓴다.
- 하이브리드 빌드를 위한 [무기](/ko/items/weapons/). 다섯 가지 특수 리에이전트를 한 세트 가득 챙겨라.

## 돈 버는 법

네크로맨서는 던전을 솔로로 파밍한다: 대상을 저주하고 누크하며, 그것이 남긴 시체에서
치유하고, 시체를 약탈한다. 언데드가 많은 고티어 콘텐츠는 저주 키트에 잘 보답한다. 남는 것은
[상점 & 은행 이용](/ko/playing/vendors-and-banking/)을 통해 팔아라.

## 함께 보기

- [샘파이어](/ko/professions/sampire/) — Necromancy + Bushido 근접 흡수 빌드
- [메이지](/ko/professions/mage/) — 캐스팅 네크로가 빌려 오는 캐스터 기반
- [Necromancy 스킬](/ko/skills/necromancy/) · [Spirit Speak](/ko/skills/spirit-speak/) · [마법 학파](/ko/playing/magic-schools/)
