---
title: "템플릿: 스턴 메이지(스턴 마사)"
description: 봉쇄 시전자 — 레슬링 스턴 펀치(해부학 80 + 레슬링 80)를 준비해 대상을 얼리고, 주문 콤보를 꽂는 마법학 메이지.
status: unverified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/Fists.cs (stun requires Anatomy >= 80.0 AND Wrestling >= 80.0; disarm requires Arms Lore >= 80 + Wrestling >= 80)"
  - "servuo: Config/PlayerCaps.cfg (700 total / 100 per-skill / 225 stat caps)"
  - "community/era UO build knowledge — adapted to this shard"
last_verified: 2026-06-12
generated: false
---

:::note[검증되지 않음 — 커뮤니티/시대 빌드, 적응됨]
이 샤드에 적응된 고전 한국 커뮤니티 메이지 변형입니다. **80/80 스턴 요구치**와 **700/225 한계**는
ServUO에 대해 소스 검증되었으며; 빌드 형태와 PvP 콤보 전술은 시대 지혜입니다. **정확한 PvP
타이밍은 검증되지 않았고** — 필드 검증은 보류 중입니다. [위키 규약](/ko/guides/wiki-conventions/)에
따라 불일치를 신고하세요.
:::

한국 UO 커뮤니티에서 메이지는 **마사**(*masa*, 마법사 *mabeopsa* "magus/mage"에서 유래)라고 불렸습니다.
**스턴 메이지**(**스턴 마사**)는 AOS 이전의 **스턴 펀치**를 중심으로 세워진 마사 변형입니다: 대상을
잠깐 **얼리는** 레슬링 동작으로, 적이 행동할 수 없는 동안 주문 콤보를 꽂을 공짜 창을 줍니다.

이것은 여기 세 마사 템플릿 중 하나로, [연금술 메이지](/ko/templates/alchemy-mage/)와
[무기/할버드 메이지](/ko/templates/weapon-mage/)와 함께합니다. 셋 모두의 고수준 PvP 그림은
[PvP 빌드](/ko/professions/pvp/)를; 처음부터의 시전자 스토리라인은 [메이지 템플릿](/ko/templates/mage/)을
참고하세요.

## 아이디어: 스턴, 그다음 폭격 (소스 검증된 요구치)

이 샤드는 AOS 이전 스턴 펀치를 구현합니다. `servuo: Scripts/Items/Equipment/Weapons/Fists.cs`에
따르면, **스턴을 준비하려면 요구됩니다**:

> **해부학 ≥ 80.0 AND 레슬링 ≥ 80.0**

(관련된 무장 해제 동작은 대신 **병기학 ≥ 80 AND 레슬링 ≥ 80**을 요구합니다.) 이 두 스킬이 있으면, 스턴을
준비하고 다음번 성공한 레슬링 타격이 대상을 잠깐 묶습니다 — 스턴 메이지는 그 창을 사용해 적이 반응하거나
치유하기 전에 평가로 강화된 주문 콤보를 꽂습니다. 묶고, 그다음 쏟아붓기.

요구치가 100이 아니라 **80**이므로, 스턴을 *사용*하는 데 해부학과 레슬링이 엄격히 GM일 필요는 없습니다 —
하지만 GM 레슬링은 당신의 비무장 방어이기도 하고 명중/스턴 확률을 높이므로, 이 템플릿은 둘 다 100으로
챙깁니다.

## 7개 스킬 (≈총 700)

일곱 개의 그랜드마스터(100.0) 스킬은 **700.0**을 합산합니다 — 이 샤드의 총 스킬 한계
(`Config/PlayerCaps.cfg`):

- **[마법학](/ko/skills/magery/)** — 당신의 주문 콤보와 기동성.
- **[지능 평가](/ko/skills/evaluating-intelligence/)** — 주문 데미지를 높임.
- **[마법 저항](/ko/skills/resisting-spells/)** — 적의 마법을 버팀.
- **[레슬링](/ko/skills/wrestling/)** — 스턴(≥80 필요)과 당신의 비무장 방어.
- **[해부학](/ko/skills/anatomy/)** — 스턴(≥80 필요); 근접/치유도 강화.
- **[명상](/ko/skills/meditation/)** — 콤보 사이 마나를 다시 채움.
- **유연: [기록술](/ko/skills/inscription/)**(주문 데미지 보너스 + 필사) 또는 다른 유틸리티 스킬.

:::tip[120은 파워 스크롤에서 옵니다]
7-GM(100.0) 천장은 *기본* 한계입니다. 개별 스킬은 **파워 스크롤**로 **120**까지 가며, 이 샤드에서는
**챔피언 스폰과 보물**에서 드롭됩니다 — [보물 사냥](/ko/playing/treasure-hunting/)을 참고하세요.
:::

**권장 스탯 (225 한계):** STR ~75 / DEX ~35 / INT ~115 (225 스탯 총합은 샤드 한계,
`Config/PlayerCaps.cfg`) — STR과 스턴을 위한 쓸만한 펀치, 마나를 위해 INT가 앞섭니다.

## 어떻게 플레이하는가

- **스턴을 준비**하고(해부학 80 + 레슬링 80 필요, `Fists.cs`에 따름), 레슬링 사거리로 붙어, 펀치를 꽂아
  대상을 묶으세요.
- **창 안에 쏟아붓기:** 대상이 스턴된 동안, 평가로 강화된 주문 콤보(고전적인 익스플로전 → 에너지 볼트
  식 버스트)를 이어가 적이 회복하기 전에 떨어지게 하세요.
- GM 레슬링으로 **끊김 없이 유지**해서 적 근접이 *당신*의 시전을 봉쇄하지 못하게 하세요.
- **정확한 스턴 지속 시간과 스턴→콤보 창의 PvP 타이밍은 이 샤드에서 검증되지 않았습니다** — 라이브
  대상에 테스트하고 신고하세요. 이것은 플레이어 전투 빌드이니, 먼저 [심화 전투](/ko/playing/combat-advanced/)와
  [PvP 빌드](/ko/professions/pvp/)를 읽으세요.

## 돈

PvM에서는 [메이지 템플릿](/ko/templates/mage/)처럼 플레이합니다 — 리콜로 들어가, 버스트하고, 리콜로
나오기 — 근접이 빠른 스폰에 대한 추가 컨트롤 도구로 스턴을 곁들여서. 진짜 우위는 **PvP**입니다:
플레이어를 묶어 보장된 콤보 창을 여는 것이 이 빌드의 목적입니다.

## 같이 보기

- [메이지 템플릿](/ko/templates/mage/) — 밑바탕이 되는 시전자 스토리라인.
- [PvP 빌드](/ko/professions/pvp/) — 탱크/녹스/스턴 메이지 개요.
- [레슬링](/ko/skills/wrestling/), [해부학](/ko/skills/anatomy/),
  [심화 전투](/ko/playing/combat-advanced/).
- 형제 빌드: [연금술 메이지](/ko/templates/alchemy-mage/), [무기/할버드 메이지](/ko/templates/weapon-mage/).
