---
title: "템플릿: 동물 조련사(Animal Tamer)"
description: 펫 마스터 입문 빌드 — 이 샤드의 실제 난이도 수치로 본 길들이기 사다리, 펫 경제학, 그리고 나이트메어와 화이트 웜으로 가는 길.
status: unverified
sources:
  - "UOSA Animal Taming wiki page (era taming ladder)"
  - "UOSA Hunting 101: forums.uosecondage.com/viewtopic.php?t=46019"
  - "wiki: /mechanics/character-creation/"
  - "wiki: /skills/animal-taming/ (taming formula)"
  - "uowiki: data/creatures.json (MinTameSkill, hits, control slots)"
last_verified: 2026-06-11
generated: false
---

:::note[검증되지 않은 스토리라인]
이 샤드에 맞춰 적응된 커뮤니티 유래 성장 경로입니다. 길들이기 난이도와 생물 스탯은 이 위키의 소스
검증된 데이터에서 나오지만, 경로는 아직 필드 검증을 기다리고 있습니다.
[위키 규약](/ko/guides/wiki-conventions/)에 따라 불일치를 신고하세요.
:::

조련사는 폭력을 외주화합니다. 당신의 펫이 싸우고, 당신은 명령하고 치유합니다 — 초반에는 느리고
번거롭지만, 엔드게임(드래곤이나 나이트메어를 발치에 둔)은 다른 모든 템플릿보다 더 법니다. 인내가
필요합니다: 길들이기는 설계상 *아주 자주* 실패합니다([Animal Taming 페이지](/ko/skills/animal-taming/)의
공식 참고).

**엔드게임 목표 (총합 700.0):** [Animal Taming](/ko/skills/animal-taming/), Animal Lore,
Veterinary, [Magery](/ko/skills/magery/), Meditation 100, 그리고 자유 슬롯(Eval Int, 또는
[Healing](/ko/skills/healing/)). 장기 스탯은 시대 지혜에 따라: 높은 STR과 INT, DEX는 마지막.

## 이 샤드의 캐릭터 생성

전체 규칙: [캐릭터 생성](/ko/mechanics/character-creation/).

- **스탯: STR 45 / DEX 10 / INT 35.** 스탯은 조련사에게 가장 덜 중요합니다 — 펫이 싸움을 합니다.
  STR은 운반 무게와 생존용, INT는 빌드의 Magery 절반을 위한 것입니다.
- **스킬: Animal Taming 50, Magery 50, Animal Lore 20.** Magery는 훌륭한 시작 키트(스펠북, 각 시약
  50개, Veterinary가 생기기 전 펫용 치유 주문)를 줍니다. 첫날부터 붕대를 원한다면 Animal Lore 20을
  Healing 20으로 바꾸세요 — 하지만 Lore는 길들이기 판정을 먹여 살리고 시도할 때마다 수동으로
  성장합니다.
- **함정: Animal Taming은 시작 장비를 전혀 주지 않습니다.** 아무것도. 이 스킬은 서버의 장비
  표에 항목이 없습니다([캐릭터 생성](/ko/mechanics/character-creation/)) — 양치기 지팡이(와 로브)를
  주는 것은 Animal Lore입니다. Lore가 없으면 보편 키트(금화 1,000, 단검, 양초, 책)만으로 시작합니다.
- **도시: [Skara Brae](/ko/world/skara-brae/).** 조련사의 마을: 동물 트레이너, 마구간, 그리고 섬의
  농지 길들이기 필드. 1단계의 모든 것이 걸어갈 거리 안에서 일어납니다.

## 1단계 — 초보 (생성 → Taming ~65)

당신은 Taming 50에서 시작합니다 — 시대 가이드의 NPC 훈련, hind-와-timber-wolf 단계 전체를 *지나서*
([hind](/ko/bestiary/animals/hind/)와 [timber wolf](/ko/bestiary/animals/timber-wolf/)는 23.1에서
길들이기, [polar bear](/ko/bestiary/animals/polar-bear/)와
[walrus](/ko/bestiary/animals/walrus/)는 35.1 — 이제 당신에게는 전부 사소함). 샤드의 4×50 생성이
당신을 곧장 사다리 중간으로 건너뛰게 합니다. 길들이기 → 풀어주기 → 재길들이기; 각 시도는 신선하거나
풀려난 대상이 필요합니다.

| 스킬 | 대상 (MinTameSkill) | 어디서 (시대 지식, unverified) |
|---|---|---|
| 50 → 59 | [snow leopard](/ko/bestiary/animals/snow-leopard/) (53.1), [panther](/ko/bestiary/animals/panther/), [grey wolf](/ko/bestiary/animals/grey-wolf/) (53.1) | 설원/정글 야생 |
| 59 → 65 | [great hart](/ko/bestiary/animals/great-hart/) (59.1), [grizzly bear](/ko/bestiary/animals/grizzly-bear/) (59.1) | [Yew](/ko/world/yew/) / Skara 본토 주변 깊은 숲 |

시대 가이드는 snow leopard에 상응하는 것("snow panther")을 53–59에 두는데 우리 데이터와 정확히
일치합니다. 길들이는 동안, 길들인 것을 이전 펫으로 죽이세요 — 동물 시체는 **가죽과 고기**를
냅니다([great hart](/ko/bestiary/animals/great-hart/): 가죽 15; 나중의 bull: 15) — 당신의 첫 꾸준한
수입입니다.

**모을 것:** 가죽(재단사나 플레이어에게 판매), 고기, 깃털. **돈:** 보통; 시작 금화 1,000에 가죽 돈을
더하면 시약이 충당됩니다.

## 2단계 — 숙련 (Taming 65 → ~95)

**목표:** 야생 사다리를 갈고, [Recall](/ko/magic/circle-4/recall/)(스크롤 구매 — 시작 책에 없음)과
펫 치유를 위해 Magery를 ~60+로 올리기, Lore/Vet 성장 적립.

| 스킬 | 대상 (MinTameSkill) |
|---|---|
| 65 → 71 | [white wolf](/ko/bestiary/animals/white-wolf/) (65.1) |
| 71 → 77 | [bull](/ko/bestiary/animals/bull/) (71.1) — **고전적인 야영지**; 각 가죽 15 + 고기 10 |
| 77 → 84 | [frenzied ostard](/ko/bestiary/monsters/frenzied-ostard/) (77.1), [giant toad](/ko/bestiary/monsters/giant-toad/) (77.1) |
| 84 → 94 | [drake](/ko/bestiary/monsters/drake/) (84.3, 241–258 타격수, Rich 전리품), [dire wolf](/ko/bestiary/monsters/dire-wolf/) (83.1), [ridgeback](/ko/bestiary/animals/ridgeback/) (83.1) |

- bull 야영지는 유명한 이중 수익입니다: 길들이기 성장에 더해 풀어주고 도살한 **대량 가죽**.
  [Vesper](/ko/world/vesper/)나 브리타니아에서, 또는 제작자 플레이어에게 가죽을 파세요.
- drake가 경제를 뒤집습니다: 길들인 [drake](/ko/bestiary/monsters/drake/)(컨트롤 슬롯 2)는 당신의 첫
  진짜 전투 펫이자 *동시에* 길들이기 실패 처치마다 Rich 등급 금화와 스크롤을 떨굽니다. 이때부터,
  길들인 것으로 사냥하세요.
- **[브리타니아](/ko/world/britain/) 은행에서 플레이어에게 훈련된 펫 팔기**를 시작하세요 — 짐
  동물, 탈것, 전투 펫 모두 잘 팔립니다. 공식에 유의하세요: 이전 주인 한 명마다 펫의 유효 길들이기
  난이도에 6.0이 추가됩니다([Animal Taming](/ko/skills/animal-taming/)), 그래서 갓 길들인 게 가장
  잘 팔립니다.

**모을 것:** 대량 가죽, drake 전리품, 보석. **돈:** bull 가죽은 안정적이고; drake 농사가 첫 본격
수입입니다.

## 3단계 — 마스터 (Taming ~94+)

우리 생물 데이터에서 나온 분기점: **[dragon](/ko/bestiary/monsters/dragon/) 93.9**,
**[nightmare](/ko/bestiary/monsters/nightmare/) 95.1**,
**[white wyrm](/ko/bestiary/monsters/white-wyrm/) 96.3**. (시대 가이드는 nightmare와 화이트 웜을
95.1로 함께 묶지만 — 이 샤드에서는 웜이 더 어렵고, 드래곤이 실제로 먼저 옵니다.)

- **나이트메어를 잡으세요**(컨트롤 슬롯 2, 298–315 타격수, 메이지처럼 싸움) 또는 드래곤(슬롯 3,
  478–495 타격수). 이것들의 길들이기 시도는 격렬하게 실패합니다 — Recall, 치유된 전투 펫, 그리고
  인내를 가져가세요.
- 그다음 최상위 농사 루프: **Destard**의 drake와 dragon을 당신 드래곤으로(드래곤 시체당 FilthyRich
  ×2 + 보석 8개), 그리고 **Deceit**의 [lich lord](/ko/bestiary/undead/lich-lord/) (250–303 타격수,
  FilthyRich + 네크로 스크롤) — 시대 합의상 시간당 최고 금화이며, 어떤 방어구도 막지 못할 것을 당신
  펫이 탱킹합니다.
- [white wyrm](/ko/bestiary/monsters/white-wyrm/) (433–456 타격수, FilthyRich ×2)은 얼음
  영토에 스폰됩니다([던전](/ko/world/dungeons/): Ice Dungeon, unverified); 그들은 시전자(메이지
  AI)입니다 — 여럿을 한 번에 끌면 조련사가 죽습니다, 아래 실수 참고.
- 잉여 금화(시대 수치: 10만+)는 Magery, Lore, Veterinary를 GM화하는 데 들어갑니다 — 시대 가이드는
  Vet GM에 붕대 15,000+개를 추산합니다(여기서는 unverified).

## 거래 루프

| 구매 | 어디서 |
|---|---|
| 시약 (Magery 통한 펫 치유) | [Moonglow](/ko/world/moonglow/) / [브리타니아](/ko/world/britain/) 메이지 상점 — [시약](/ko/items/reagents/) |
| 붕대 (Veterinary) | 어디든 치료사/재단사 |
| 마구간 슬롯, 입문 Lore/Vet 훈련 | [Skara Brae](/ko/world/skara-brae/) 동물 트레이너 |

| 판매 | 어디서 |
|---|---|
| 대량 가죽, 고기, 깃털 | 재단사/잡화상 ([Vesper](/ko/world/vesper/), 브리타니아), 제작자 플레이어 |
| 훈련된 펫 (탈것, 짐 동물, drake+) | 브리타니아 은행의 플레이어, [포럼 거래 게시판](https://www.uotavern.com/forum) |
| 드래곤/lich 전리품, 보석 | NPC 보석상; 좋은 마법 아이템은 플레이어 |

## 결정 지점과 흔한 실수

- **길들이기 대상의 MinTameSkill이 당신 스킬보다 ~25 넘게 낮으면**, 아무것도 가르치지 않습니다 —
  표에서 위로 올라가세요([스킬 성장](/ko/mechanics/skill-gain/)은 도전이 필요합니다).
- **공격적인 대상을 길들이다 계속 죽으면**(drake 이후), 어그로를 잡는 탱킹 펫으로 길들이고, 그
  뒤에 서세요.
- **누군가 ~80 길들이기에서 드래곤을 선물하면**, 훈련 목적으로는 거절하세요: 절대 길들일 수 없는
  펫은 아무것도 가르치지 않고 야생화하는 순간 죽습니다(고급 펫의 컨트롤도 당신 스킬에 달려
  있습니다). 고전적인 정체는 bull을 갈지 않고 선물 드래곤을 타는 것입니다.
- **화이트 웜이 여럿 보이면**, 한 번에 하나씩 잡으세요 — 그들은 시전자이고 무리가 당신을 당신 펫에서
  떨어뜨리며 광역 폭격합니다.
- **실수:** 너무 일찍 던전 길들이기. bull까지의 야생 대상이 스폰 압박 없이 77+까지 커버합니다.
- **실수:** Taming이 장비를 주지 않음을 잊기 — 첫날 시약과 붕대를 위해 1,000 금화를 예산하세요.
- **실수:** 많이 거래된 펫을 "신선한" 것으로 팔기. 이전 주인마다 +6.0 난이도가 쌓이며; 딱 맞는
  스킬을 가진 구매자는 컨트롤에 실패합니다.
