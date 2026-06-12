---
title: UO 확장팩
description: 울티마 온라인의 모든 확장팩을 연대순으로 정리한 역사 — 각각이 추가한 땅, 종족, 스킬, 시스템 — 그리고 그것이 Endless Journey 룰셋을 돌리는 이 샤드에 어떻게 맞물리는지.
status: unverified
sources:
  - "general Ultima Online history; ultimaonline.fandom.com"
  - "servuo: Config/Expansion.cfg, Server/ExpansionInfo.cs"
last_verified: 2026-06-12
generated: false
---

울티마 온라인은 20년 넘게 확장되어 왔습니다. 각 **확장팩(expansion)**은 기존 게임에 새 콘텐츠를
덧대는 이름 붙은 릴리스입니다 — 새 땅과 *패싯(facets)*(평행 지도), 새 플레이 가능 **종족(races)**,
새 **스킬(skills)**과 주문 학파, 그리고 새 **시스템(systems)**(전투 연산, 제작, 주거, 항해).
**시대(era)**는 주어진 확장팩이 정의하는 기간입니다: 누군가 무언가를 "AOS 시대(AOS-era)"라고 할
때, 그것이 *Age of Shadows*와 함께 도착했거나 그에 의해 재편되었다는 뜻입니다.

이것이 문서화에 중요한 이유는 UO가 누적적이기 때문입니다. 서버는 기능을 메뉴에서 골라 담지 않습니다;
단일 확장팩 레벨을 선언하고 그것을 포함해 그 이하의 모든 것을 물려받습니다. **이 샤드는 Endless
Journey(EJ)를 돌립니다** — ServUO 서버 에뮬레이터의 가장 최신 레벨 — 그래서 아래의 *모든* 확장팩이
여기 존재합니다. Lost Lands, 모든 패싯, 모든 종족과 스킬 학파, 커스텀 주거, 항해, Eodon — 전부
가동 중입니다. (`Config/Expansion.cfg` 참고: `CurrentExpansion=EJ`.)

확장팩의 목록과 순서는 서버의 확장팩 enum(`Server/ExpansionInfo.cs`)에서 곧장 나옵니다: None →
T2A → UOR → UOTD → LBR → AOS → SE → ML → SA → HS → TOL → EJ. 각각의 대표 추가 사항은
아래에 있습니다.

## 연표

| Expansion | Year | Headline additions |
|-----------|------|---------------------|
| Launch | 1997 | 원래의 Britannia(Felucca 지도) |
| The Second Age (T2A) | 1998 | Lost Lands; 첫 대규모 땅 확장 |
| Renaissance (UOR) | 2000 | Trammel/Felucca 패싯 분리; 합의제 vs 개방형 PvP |
| Third Dawn (UOTD) | 2001 | Ilshenar 패싯; 첫 3D 클라이언트 |
| Lord Blackthorn's Revenge (LBR) | 2002 | 세계 전반의 새 아트와 생물 |
| Age of Shadows (AOS) | 2003 | Malas; 저항; 아이템 속성 + 보험; Necromancy, Chivalry; 커스텀 주거 |
| Samurai Empire (SE) | 2004 | Tokuno Islands; Bushido, Ninjitsu; 사무라이와 닌자 |
| Mondain's Legacy (ML) | 2005 | 엘프; Spellweaving; Heartwood; peerless 보스 |
| Stygian Abyss (SA) | 2009 | 가고일; Ter Mur; Mysticism, Imbuing, Throwing; the Abyss |
| High Seas (HS) | 2010 | 선박과 해상 전투; 낚시 개편 |
| Time of Legends (TOL) | 2015 | Valley of Eodon; Myrmidex; 스킬 마스터리 |
| Endless Journey (EJ) | 2018 | 무료 접근 등급 — **이 샤드가 돌리는 룰셋** |

## Launch (1997)

울티마 온라인은 단일한 땅으로 출시되었습니다: **Britannia**, 나중에 **Felucca**로 알려진 지도.
패싯도, 두 번째 지도도 없었고, 세계는 단일한 개방형 룰셋이었습니다 — 누구든, 어디서든, 누구든
공격할 수 있었습니다. 뒤따르는 모든 것은 이 원래의 세계 위에 지어집니다.

## The Second Age (T2A, 1998)

첫 대규모 땅 확장. T2A는 **Lost Lands**를 추가했습니다 — 동굴 통로와 던전을 통해 닿는 드넓은
야외 지역으로, 새 마을, 지형, 생물을 갖춰 탐험 가능한 표면을 대략 두 배로 늘렸습니다. 또한 더
강한 몬스터와 그 변경의 상징적인 던전들을 가져왔습니다.

이 샤드에서 Lost Lands는 완전히 존재합니다. 그 변경 마을 둘이 우리 월드 섹션에 문서화되어 있습니다:
**Delucia**와 **Papua**.

- [월드 아틀라스(World atlas)](/ko/world/) · [Delucia](/ko/world/delucia/) · [Papua](/ko/world/papua/)

## Renaissance (UOR, 2000)

Renaissance는 지리보다 *사회적* 게임을 더 많이 재편했습니다. 세계를 두 개의 평행 **패싯**으로
나누었습니다: **Trammel**, 플레이어가 동의 없이 서로를 해칠 수 없는 곳, 그리고 **Felucca**, 원래의
개방형 PvP, 풀 루팅 룰셋을 유지한 곳. 같은 도시가 양쪽에 존재하지만, 교전 규칙이 다릅니다. 이
"Tram/Fel" 분리는 PvP와 악명이 작동하는 방식에 대한 가장 중대한 변경이며, 오늘날까지 게임에
지속됩니다.

- [악명과 PvP(Notoriety and PvP)](/ko/playing/notoriety-and-pvp/)

## Third Dawn (UOTD, 2001)

Third Dawn은 **Ilshenar** 패싯을 도입했습니다 — 플레이어 주거도, 다른 지도와의 문게이트 연결도
없는, 가고일과 Ophidian을 테마로 한, 설화가 풍부한 큰 땅덩이. 그 또 다른 대표는 기술적이었습니다:
고전 2D 클라이언트와 나란한 대체 렌더러, UO의 첫 **3D 클라이언트**.

## Lord Blackthorn's Revenge (LBR, 2002)

LBR은 지리에서는 가볍고 연출에서는 무거웠습니다. 게임의 **아트와 생물** 상당수를 정비했고 — 많은
몬스터 스프라이트가 다시 그려졌습니다 — 타락한 Lord Blackthorn을 둘러싼 줄거리를 엮어 넣었습니다.
또한 한 해 전 도입된 더 새로운 3D 에셋에 대한 클라이언트 지원을 강화했습니다.

## Age of Shadows (AOS, 2003)

대형. *Age of Shadows*는 이전이나 이후 어떤 확장팩보다 장비와 전투의 규칙을 다시 썼습니다. 그
추가 사항:

- **Malas** — Luna, Umbra 도시와 Doom 던전의 본거지인 새 패싯.
- **저항 시스템(resistance system)**: 방어구가 더 이상 단일 Armor Rating을 쓰지 않고 다섯 개의
  별도 저항을 썼습니다 — Physical, Fire, Cold, Poison, Energy — 각각 70에서 캡. 데미지 타입이
  중요하며; 다섯을 균형 잡도록 슈트를 빌드합니다.
- **아이템 속성과 강도(intensity)**: 마법 장비가 수십 가지 누적 가능 속성(Faster Casting,
  Hit Chance Increase, Damage Increase, Lower Reagent Cost 등)을 얻어, 전리품과 제작을
  민맥싱 게임으로 만들었습니다.
- **아이템 보험(insurance)**, 죽음이 더 이상 장착 슈트를 잃는 것을 뜻하지 않도록.
- **커스텀 주거(custom housing)** — 고정된 증서에서 고르는 대신 플레이어가 자신만의 평면도를
  그릴 수 있게 한 게임 내 집 디자이너.
- 두 가지 새 주문 학파와 그 위에 지어진 템플릿: **Necromancy**(네크로맨서)와 **Chivalry**(팔라딘).

- [네크로맨서(Necromancer)](/ko/professions/necromancer/) · [팔라딘(Paladin)](/ko/professions/paladin/)
- [방어구와 저항(Armor and resistances)](/ko/items/armor/) · [주거 유형(House types)](/ko/playing/house-types/)

## Samurai Empire (SE, 2004)

**Tokuno Islands**를 중심으로 한 아시아 테마 확장팩으로, 자체 마을, 던전, 장식 양식을 갖춘 세 섬
패싯입니다. 두 가지 스킬과 그 주위에 지어진 클래스를 추가했습니다: **Bushido**(사무라이, 자세
기술을 지닌 근접/방어 전사)와 **Ninjitsu**(닌자, 은신, 동물 변신, 분신을 지님).

- [사무라이(Samurai)](/ko/professions/samurai/) · [닌자(Ninja)](/ko/professions/ninja/)

## Mondain's Legacy (ML, 2005)

Mondain's Legacy는 출시 이후 첫 새 **플레이 가능 종족**을 추가했습니다 — **엘프(elves)** — 자체
시작 스탯과 종족 특성을 지닙니다. 그 다른 기둥들:

- **Spellweaving**, 그룹으로 시전할 때 위력이 스케일링되는 비전 학파, 그 위에 지어진 Arcanist
  템플릿과 함께.
- **Heartwood**, 숲에 숨겨진 엘프 정착지로, 자체 퀘스트 주도 제작 보상을 갖춤.
- **Peerless 보스** — 인스턴스화된, 열쇠로 잠긴 조우(Travesty, Dreadhorn, Lady Melisande
  등)로, 엔드게임 전투의 틀이 되었습니다.
- *Imbuing*이 나중에 공식화할 자원·속성 제작을 향한 초기 토대.

- [Spellweaver](/ko/professions/spellweaver/) · [Spellweaving 스킬](/ko/skills/spellweaving/)

## Stygian Abyss (SA, 2009)

Stygian Abyss는 두 번째 새 종족을 추가했습니다 — 날 수 있는 **가고일(gargoyles)** — 그리고
**Ter Mur** 패싯, 위대한 **Stygian Abyss** 던전 자체를 통해 닿는 가고일 고향. 세 가지 스킬을
한꺼번에 가져왔습니다:

- **Mysticism**, 비전/신성 하이브리드 학파(미스틱).
- **Imbuing**, 마법 속성을 통제된 강도로 아이템에 빌드할 수 있게 하는 제작 스킬 — ML 토대의
  공식화.
- **Throwing**, 가고일 전용 원거리 전투 스킬.

- [미스틱(Mystic)](/ko/professions/mystic/) · [Mysticism](/ko/skills/mysticism/)
- [Imbuing](/ko/skills/imbuing/) · [Throwing](/ko/skills/throwing/)

## High Seas (HS, 2010)

High Seas는 바다를 중요하게 만들었습니다. 완전한 **항해와 해상 전투** 시스템을 추가했고 — 대포가
달린 다중 타일 선박, 선박 대 선박 전투, merfolk와 Corgul 보스 같은 해상 적 — **낚시(fishing)**를
새 어획물, 큰 물고기, 병에 든 메시지(message-in-a-bottle) 보물을 갖춘 더 깊은 직업으로 개편했습니다.

- [어부(Fisher)](/ko/professions/fisher/) · [보물 사냥(Treasure hunting)](/ko/playing/treasure-hunting/) (병에 든 메시지 / SOS)

## Time of Legends (TOL, 2015)

Time of Legends는 **Valley of Eodon**을 열었습니다 — 공룡, 곤충형 **Myrmidex**, 그리고 Zhah와
Sakkhra 부족이 사는 선사시대 정글 땅. 그 시스템 추가는 **스킬 마스터리(skill masteries)**였습니다 —
확립된 캐릭터에게 새로운 전문화 층과 능동 능력을 주는 스킬별 마스터리 능력.

## Endless Journey (EJ, 2018)

Endless Journey는 콘텐츠 투하라기보다 **접근 등급(access tier)**입니다: 활성 구독 없이 계정이
로그인해 게임의 넓은 부분을 플레이하게 해 주는 무료 룰셋으로, 저장 공간과 최신 콘텐츠에 일부 제한이
있습니다. ServUO 서버 에뮬레이터에서 EJ는 **가장 높은 확장팩 레벨**이며, 이는 그 위 모든 확장팩의
전체 콘텐츠 스택을 물려받는다는 뜻입니다.

**이것이 우리 샤드가 돌리는 룰셋입니다.** 이 위키 다른 곳에서 어떤 스킬, 주문, 아이템이 여기
존재한다고 읽는다면, 그것은 EJ가 그 아래의 모든 역사를 앞으로 실어 나르기 때문입니다.

- [우리 샤드(Our shard)](/ko/shard/)

## 이것이 우리 샤드에 의미하는 바

샤드가 **EJ**를 돌리므로, 이 역사 중 무엇도 가정이 아닙니다 — 전부 당신이 딛고 선 땅입니다. 모든
패싯(Felucca, Trammel, Ilshenar, Malas, Tokuno, Ter Mur, Eodon), 두 추가 종족(엘프, 가고일),
모든 주문 학파(Necromancy, Chivalry, Bushido, Ninjitsu, Spellweaving, Mysticism), 그리고 모든
시스템(저항, 아이템 속성, 보험, 커스텀 주거, 항해, imbuing, 마스터리)이 여기 캐릭터들에게
이용 가능합니다.

또한 그래서 이 위키 전반의 페이지가 콘텐츠를 **시대(era)**별로 태그합니다. 아이템과 제작 카탈로그는
각 재질, 아이템, 레시피가 언제 도입되었는지 표시합니다 — 그 태그는 이 페이지의 역사에서 곧장
나오므로, 무언가가 출시 시대의 주력인지 후속 확장팩과 함께 도착했는지 한눈에 알 수 있습니다. 아이템별
시대 태그는 [아이템 카탈로그(item catalogs)](/ko/items/)를, 이 EJ 기준선 위에 얹히는 캡, 레이트,
하우스 룰은 [샤드 페이지(shard pages)](/ko/shard/)를 보세요.
