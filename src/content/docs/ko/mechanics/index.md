---
title: 게임 메커니즘
description: 메커니즘 페이지 색인 — 이 샤드에서 내부의 수치가 실제로 어떻게 작동하는지.
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs"
last_verified: 2026-06-11
generated: false
---

브리타니아는 주사위로 돌아가지만, 그 주사위는 공개되어 있습니다 — 이 샤드의 서버 소스는 열려
있으며, 이 페이지들은 서버가 실제로 굴리는 것을 문서화합니다.

## 페이지

- **[스킬 상승](/ko/mechanics/skill-gain/)** — 상승 확률 공식, 보장 상승 시스템(GGS), 스킬
  한계에서의 동작, 그리고 안티 매크로 검사가 여기서 꺼져 있는 이유.
- **[스탯 상승](/ko/mechanics/stat-gain/)** — 힘, 민첩성, 지능이 스킬 사용에서 어떻게 자라는지,
  그리고 225 스탯 한계에서 무슨 일이 일어나는지.

## 관련 참조

- [샤드 신분증](/ko/shard/) — 이 메커니즘들이 읽어 들이는 설정된 한계와 비율
- [스킬](/ko/skills/) — 전체 스킬 표와 스킬별 단련 가이드
- [마법](/ko/magic/) — 주문 메커니즘은 자체 섹션에 있음

## 검증에 관한 메모

메커니즘 페이지는 ServUO 소스의 정확한 파일을 인용하며(경로는 `../servuo` 기준), 주로
`Scripts/Misc/SkillCheck.cs`와 `Server/Skills.cs`입니다. 인게임 동작이 여기의 공식과 다르다면,
그것은 페이지나 서버의 버그입니다 — 어느 쪽이든,
[신고서를 제출하세요](/ko/guides/wiki-conventions/).
