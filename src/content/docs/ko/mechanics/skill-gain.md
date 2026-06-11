---
title: 스킬 상승
description: 이 서버에서 스킬 상승이 실제로 어떻게 작동하는지 — 상승 확률 공식, GGS 보장 상승, 한계 동작, 그리고 안티 매크로 상태.
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs"
  - "servuo: Server/Skills.cs (SkillInfo.GainFactor)"
  - "servuo: Config/PlayerCaps.cfg (EnableAntiMacro, caps)"
last_verified: 2026-06-11
generated: false
---

모든 휘두름, 파기, 주문 영창은 같은 주사위를 굴립니다. 이 페이지는 `Scripts/Misc/SkillCheck.cs` —
서버가 구동하는 파일 — 의 실제 로직을 문서화합니다.

## 기본 흐름

스킬을 사용하면, 서버는 난이도 창(`minSkill`–`maxSkill`, 또는 직접 `chance`)에 대해 **스킬
검사**를 합니다:

- `minSkill` 미만: 자동 실패, **상승 불가능**("too difficult").
- `maxSkill` 이상: 자동 성공, **상승 불가능**("no challenge").
- 그 사이: 성공 확률 = `(value − minSkill) / (maxSkill − minSkill)`, 그리고 시도의 성공 여부와
  무관하게 **상승 굴림**이 일어납니다.

그래서 단련의 스위트 스폿은 *어렵지만 가능한* 작업입니다 — 일단 작업이 사소해지면, 더 이상
당신에게 아무것도 가르쳐 주지 않습니다.

## 상승 확률 (`CheckSkill` → `GetGainChance`)

각 적격 사용에 대해, 0.1 스킬을 얻을 확률은 다음과 같이 계산됩니다:

```
gc = ( (TotalCap − TotalSkills) / TotalCap        // room left under the 700.0 cap
     + (SkillCap − SkillBase) / SkillCap ) / 2    // room left in this skill
gc = ( gc + (1 − difficultyChance) × bonus ) / 2  // harder tasks gain more
gc × = GainFactor                                  // per-skill factor (1.0 for all skills here)
gc = max(gc, 0.01)                                 // never below 1%
```

여기서 `bonus`는 **성공한 시도에서 0.5**이고 **실패에서 0.0**입니다(post-AOS 규칙, 이 EJ
샤드에 적용됨). 제어된 펫은 100% 보너스를 받습니다(확률 2배). 결과는 100%에서 한계입니다.

실용적 결과:

- **낮은 스킬은 빠르게 오르고, 높은 스킬은 느리게 오릅니다** — 총합과 개별 스킬 둘 다 차오를수록
  `gc`를 줄입니다.
- **10.0 미만의 어떤 스킬도 매 사용마다 오릅니다**(`skill.Base < 10.0`은 굴림을 우회), 그리고
  10.0 미만의 각 상승은 무작위 0.1–0.4 점프입니다.
- 99.9 스킬에서도, 바닥은 적격 사용당 1%입니다.

## GGS — 보장 상승 시스템

GGS는 **이 샤드에서 활성**입니다(`GGSActive = !Siege.SiegeShard`, 이것은 Siege 샤드가 아님).
각 스킬은 `NextGGSGain` 시간을 추적합니다; 그 타이머가 만료된 후 스킬을 사용하면, **무작위 굴림이
실패해도** 상승합니다.

타이머 길이는 `GGSTable`에서 오며, 스킬의 레벨(5.0 스킬 단위 행)과 당신의 총 스킬(열: 총 350.0
미만 / 350.0–699.9 / 700.0)로 인덱싱됩니다. 예시(분 단위):

| 스킬 레벨 | 총합 < 350 | 총합 350–699.9 | 총합 700 |
|------------|------------|-----------------|-----------|
| 0–4.9 | 1 | 3 | 5 |
| 50–54.9 | 27 | 72 | 138 |
| 95–99.9 | 540 | 1440 | 2580 |
| 110–114.9 | 618 | 1662 | 3060 |

요컨대: 막힌 스킬을 계속 사용하면 시스템이 결국 보상합니다 — 하지만 높은 스킬에서는 그
"결국"이 며칠로 늘어납니다.

## 스킬 한계 동작

- 개별 한계는 **100.0**이고 총 한계는 **700.0**입니다(`Config/PlayerCaps.cfg`;
  [샤드 신분증](/ko/shard/) 참고).
- 스킬은 그 잠금이 **올림**으로 설정되어 있고 한계 미만일 때만 상승합니다.
- 총 한계에서(또는 근처에서), `CheckReduceSkill`은 당신이 **내림**으로 설정한 스킬을 당신이
  얻는 양만큼 낮춥니다. 내림 플래그된 스킬이 없으면, 상승도 없습니다. 스킬 화살표를 의도적으로
  설정하세요.
- 감옥에서는 스킬 상승이 완전히 비활성화됩니다.

## 상승량과 가속기

- 일반 상승은 **0.1**입니다(지역 `SkillGain`으로 보정, 보통 ×1).
- 스킬에 대한 **민첩 스크롤(Scroll of Alacrity)**: 활성화된 동안 각 상승이 0.2–0.5가 됩니다.
- Mondain's Legacy 퀘스트 스킬 보너스: 플래그된 동안 상승 ×2–4.

## 안티 매크로: 비활성화

`SkillCheck.cs`는 고전적인 안티 매크로 시스템(플래그된 스킬에 대해 5분당 위치/대상당 최대 3회
상승)을 담고 있지만, `PlayerCaps.EnableAntiMacro`가 true일 때만 실행됩니다 — 그리고 이 샤드는
**`EnableAntiMacro=False`**(`Config/PlayerCaps.cfg`)입니다. 서버가 모르는 척하지 않고 한 곳에서
단련할 수 있습니다.

## 관련

- [스탯 상승](/ko/mechanics/stat-gain/) — 모든 스킬 상승은 스탯 상승도 굴림
- [스킬 색인](/ko/skills/) — 스킬별 단련 가이드
