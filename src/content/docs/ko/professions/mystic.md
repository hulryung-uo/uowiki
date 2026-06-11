---
title: 미스틱 (Mystic)
description: Mysticism 캐스터 — Focus나 Imbuing로 구동되는 강력한 원소·디버프 학파. 스킬, 빌드, 전투 방법, 장비, 수입.
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Mysticism/ (MysticSpell.cs power-skill = max(Imbuing, Focus); SpellDefinitions/: NetherBoltSpell.cs, EagleStrikeSpell.cs, SpellPlague.cs, CleansingWindsSpell.cs, RisingColossusSpell.cs, HealingStoneSpell.cs, NetherCycloneSpell.cs, StoneForm.cs)"
last_verified: 2026-06-11
generated: false
---

## 이 직업은 무엇인가

미스틱은 [Mysticism](/ko/skills/mysticism/)(미스티시즘)을 기반으로 한 캐스터로, 원소
피해·디버프·치유·강력한 소환을 갖춘 Stygian-Abyss 시대의 학파다. 이 샤드(shard)에서
Mysticism은 실제로 작동한다(EJ 익스팬션 스택에는 SA 스킬이 포함된다). 강력한 단독
캐스터이며, [Magery](/ko/skills/magery/)(마법)나 [Spellweaving](/ko/skills/spellweaving/)(주문직조)과
결합해 다중 학파 캐스터로 잘 어울린다.

## 핵심 스킬

- [Mysticism](/ko/skills/mysticism/)(미스티시즘) — 시전 스킬. 사용 가능한 주문과 기본 성공률을 결정한다.
- [Focus](/ko/skills/focus/)(집중) **또는 Imbuing**(인부잉) — Mysticism의 피해와 효과 강도를 스케일링하는 **파워 스킬**. 에뮬레이터는 둘 중 높은 쪽을 사용한다: `MysticSpell.cs`는 `max(Imbuing, Focus)`를 취한다(`servuo: Scripts/Spells/Mysticism/MysticSpell.cs`). Focus는 더 가벼운 선택이고, Imbuing은 제작 스킬도 겸한다.
- 보조 캐스터 학파 — [Magery](/ko/skills/magery/)(마법) + [Evaluating Intelligence](/ko/skills/evaluating-intelligence/)(지능 평가), 또는 [Spellweaving](/ko/skills/spellweaving/)(주문직조).
- 마나 공급과 생존을 위한 [Meditation](/ko/skills/meditation/)(명상)과 [Resisting Spells](/ko/skills/resisting-spells/)(마법 저항).

## 리에이전트

Mysticism 주문은 리에이전트(메이지·네크로 계열과 여럿을 공유한다)와 마나를 소모한다.
리에이전트 주머니를 가득 채워 두되, 시전의 위력은 여전히 리에이전트가 아니라 Focus/Imbuing에서
나온다.

## 빌드

아직 **전용 미스틱 템플릿 페이지는 없다**. [메이지 템플릿](/ko/templates/mage/)에서 빌드하라:
캐스터 스탯 분배(높은 Int, 넉넉한 마나)를 유지하고 학파 슬롯을 Mysticism + Focus(또는 Imbuing)와
Magery/Eval + Meditation + Resist로 바꾼다. 700포인트 상한에 맞추는 방법은 [7x GM 템플릿](/ko/templates/seven-gm/)을
참고하라.

## 플레이 방법

[매직 스쿨](/ko/playing/magic-schools/)은 Mysticism을 여러 학파 가운데 자리매김하고,
[주문 시전](/ko/playing/spellcasting/)은 시전 메커니즘을, [명상 & 마나](/ko/playing/meditation-and-mana/)는
회복을 다룬다.

도구 모음(모두 `servuo: Scripts/Spells/Mysticism/SpellDefinitions/`에서 확인됨):

- **Nether Bolt** / **Eagle Strike** — 안정적인 단일 대상 피해 누크.
- **Spell Plague** — 대상이 계속 피격되면 추가 피해를 터뜨리는 디버프.
- **Cleansing Winds** — 광역 치유 및 해독.
- **Healing Stone** — 소환해서 들고 다니는 자가 치유 아이템.
- **Rising Colossus** — 강력한 소환 전투 동료. **Stone Form**은 방어형 자가 변신이다.
- **Nether Cyclone** / **Hail Storm** — 무리를 정리하는 광역 누크.

## 장비

- [매직 아이템 속성](/ko/magic/) — **Spell Damage Increase**, **Lower Mana Cost**, **Lower Reagent Cost**, **Faster Casting**를 우선하라. 가능하면 Mysticism Focus/Casting 모드도.
- [방어구](/ko/items/armor/) — 메이지 친화적(명상 페널티 없음)으로 균형 잡힌 저항.
- 가득 채운 **리에이전트** 재고와 해당 학파용 [스펠북](/ko/items/)을 챙겨라.

## 돈 버는 법

미스틱은 캐스터로서 던전을 파밍한다: 디버프(Spell Plague)로 열고, Nether Bolt/Eagle
Strike로 누크하고, 까다로운 대상에는 Rising Colossus를 소환하고, Cleansing Winds /
Healing Stone으로 치유한다. 강력한 광역 주문은 무리 정리를 수지맞게 만든다. 전리품은
[상점 & 은행 이용](/ko/playing/vendors-and-banking/)을 통해 팔아라.

## 함께 보기

- [메이지](/ko/professions/mage/) — 이 빌드가 빌려 오는 캐스터 기반
- [주문직조사](/ko/professions/spellweaver/) — 함께 짝지을 보완적 지원 학파
- [Mysticism 스킬](/ko/skills/mysticism/) · [Focus](/ko/skills/focus/) · [매직 스쿨](/ko/playing/magic-schools/)
