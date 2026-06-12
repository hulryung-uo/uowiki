---
title: "템플릿: 벌목 전사(도끼꾼)"
description: 도끼 덱서 — 벌목술을 익혀 그랜드마스터에서 도끼를 +20% 데미지로 휘두르는 근접 전사, 7-GM 빌드로 제시.
status: unverified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (lumberBonus = GetBonus(Lumberjacking, 0.200, 100.0, 10.00))"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseAxe.cs (axes use Lumberjacking.System; DefSkill = Swords)"
  - "servuo: Config/PlayerCaps.cfg (700 total / 100 per-skill / 225 stat caps)"
  - "community/era UO build knowledge — adapted to this shard"
last_verified: 2026-06-12
generated: false
---

:::note[검증되지 않음 — 커뮤니티/시대 빌드, 적응됨]
이것은 이 샤드에 적응된 고전 시대 커뮤니티 빌드("벌목 덱서" / "도끼꾼")입니다. **+20% 도끼 보너스**와
**700/225 한계**는 ServUO에 대해 소스 검증되었으며; 빌드 형태와 금전 조언은 시대 지혜입니다. **필드
검증은 보류 중**입니다 — 플레이하면서 [위키 규약](/ko/guides/wiki-conventions/)에 따라 불일치를
신고하세요.
:::

벌목 전사는 평범한 검 덱서보다 더 세게 때리게 만드는 한 가지 비틀기를 가진 [전사](/ko/templates/warrior/)입니다:
**[벌목술](/ko/skills/lumberjacking/)**을 익히고 **도끼**로 싸웁니다. 이 샤드에서 도끼류 무기는 당신의
벌목술 스킬에 비례한 고정 데미지 보너스를 받으므로, 그랜드마스터 벌목꾼은 같은 캐릭터가 카타나를 든
것보다 눈에 띄게 더 세게 휘두릅니다.

## 도끼가 더 세게 때리는 이유 (소스 검증됨)

`servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs`에 따르면, 총 무기 데미지에 **벌목 보너스**가
더해집니다:

```
lumberBonus = GetBonus(Lumberjacking, 0.200, 100.0, 10.00)
```

그 공식은 **100.0 벌목술에서 +20% 데미지**에 도달합니다(`BaseAxe.cs`가 도끼를 `Lumberjacking.System`으로
등록하므로, 보너스는 도끼를 들고 있을 때만 적용되고; 도끼가 아닌 무기에는 그 항이 0이 됩니다). 도끼는
또한 [검술](/ko/skills/swordsmanship/)을 훈련하고 사용하므로(`BaseAxe.cs`: `DefSkill = Swords`), 벌목
전사는 **도끼를 전문으로 하는 검사**입니다 — 카타나가 아니라 [워 액스](/ko/items/catalog/weapons/),
라지 배틀 액스, 또는 투핸디드 액스.

+20%는 당신의 STR, 해부학, 전술 보너스 위에 쌓이므로, 평범한 덱서가 결코 얻지 못하는 진짜 공짜 데미지
구간입니다. 대가는 일곱 스킬 슬롯 중 하나를 마법학 같은 것 대신 벌목술에 쓰는 것입니다.

## 7개 스킬 (≈총 700)

일곱 개의 그랜드마스터(100.0) 스킬은 **700.0**을 합산합니다 — 이 샤드의 총 스킬 한계
(`Config/PlayerCaps.cfg`). 합리적인 한 가지 배분:

- **[검술](/ko/skills/swordsmanship/)** — 당신의 무기 스킬; 도끼가 이것을 훈련하고 사용함.
- **[전술](/ko/skills/tactics/)** — 핵심 데미지 배율.
- **[해부학](/ko/skills/anatomy/)** — 추가 데미지, 그리고 붕대 치유를 뒷받침.
- **[치료술](/ko/skills/healing/)** — 붕대; 치료술+해부학 80/80에서 자가 부활.
- **[벌목술](/ko/skills/lumberjacking/)** — +20% 도끼 보너스(그리고 공짜 나무; 아래 참조).
- **[마법 저항](/ko/skills/resisting-spells/)** — 적의 마법을 무디게 함.
- **유연: [방패술](/ko/skills/parrying/)**(방어의 방패 몫 — 단, 투핸디드 도끼는 방패를 들 손이 없으니,
  방패술은 한손 [워 액스](/ko/items/catalog/weapons/)와 짝지으세요), 또는 유틸리티(치유, 해독, 이동)를
  위한 **[기사도](/ko/skills/chivalry/)/[마법학](/ko/skills/magery/)**.

:::tip[120은 파워 스크롤에서 옵니다]
위의 7-GM(100.0) 천장은 *기본* 한계입니다. 개별 스킬은 **파워 스크롤**로 **120**까지 밀 수 있으며, 이
샤드에서는 **챔피언 스폰과 보물**에서 드롭됩니다 — [보물 사냥](/ko/playing/treasure-hunting/)을
참고하세요. 120 검술 / 120 전술 도끼꾼이 이 템플릿의 최종 상태입니다.
:::

**권장 스탯 (225 한계):** STR ~100 / DEX ~90 / INT ~35. STR은 체력과 데미지, DEX는 스윙과 붕대 속도를
좌우하고; INT는 낮게(유틸리티 유연 슬롯에 딱 필요한 만큼) 유지하세요. 225 스탯 총합은 샤드 한계입니다
(`Config/PlayerCaps.cfg`).

## 어떻게 플레이하는가

[전사](/ko/templates/warrior/)처럼 플레이합니다 — 붙고, 휘두르고, 붕대 감고, 약탈 — 단, 손에 도끼와
그에 따른 데미지 우위를 더해서. 승리 조건은 같은 소모전입니다: 들어오는 데미지를 치유로 능가하고 대상을
갈아내되, 더 빠르게.

- **방패를 포기할 여유가 있을 때 투핸디드 도끼로 시작**해 가장 큰 타격을 내고; 방패술의 방어를 원할 때
  한손 [워 액스](/ko/items/catalog/weapons/) + 방패로 내리세요.
- **벌목술을 GM으로 유지**하세요 — 100 미만의 매 포인트가 데미지 손해이니, "일단" 90에 두지 마세요.
- **자급자족 벌목꾼.** 벌목술은 데미지 스탯일 뿐 아니라: 나무에서 **목재를 채집**하게 해주므로, 검
  덱서를 능가하는 같은 캐릭터가 통나무도 베어 팔거나 궁시 제작자/목공에게 댈 수 있습니다. 많은
  플레이어가 도끼꾼을 제 값을 하는 전사로 운영합니다.

무기 스페셜과 타이밍은 [심화 전투](/ko/playing/combat-advanced/)를 참고하세요.

## 돈

도끼꾼은 평범한 전사와 같은 [던전](/ko/world/dungeons/) 사다리를 농사하지만, +20% 데미지 우위 덕에 매
구간에서 더 빠른 처치와 시간당 더 많은 골드를 냅니다. 그 위에:

- **나무 수입.** 던전을 오가는 길에 통나무를 베세요; 판자는 목공과 궁시 제작자에게 팔거나, 자신의 제작
  노새에 댑니다.
- **던전 농사.** 어스 엘리멘탈, 오거, 리치, 그리고 사다리 위로 — 데미지 보너스가 매 싸움을 단축합니다.
  Felucca 스폰은 PvP 위험을 감수하면 더 많이 줍니다.

## 같이 보기

- [전사 템플릿](/ko/templates/warrior/) — 이 빌드가 얹어지는 완전한 초보자→마스터 스토리라인.
- [7x GM 템플릿](/ko/templates/seven-gm/) — 엔드게임 빌드 가운데 이것의 위치.
- [벌목술](/ko/skills/lumberjacking/), [검술](/ko/skills/swordsmanship/), [전술](/ko/skills/tactics/).
- [전사 직업](/ko/professions/warrior/), [심화 전투](/ko/playing/combat-advanced/).
