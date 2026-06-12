---
title: 마을 서비스 범례
description: 각 마을 서비스 아이콘의 의미 — 모든 도시 페이지에 표시되는 상점과 훈련사.
status: source-verified
sources:
  - "anima: data/map_pois.json (npc_vendor types)"
  - "reference: uo.com cities & towns"
last_verified: 2026-06-12
generated: false
---

모든 [도시 페이지](/ko/world/)는 마을이 제공하는 서비스를 작은 아이콘으로 표시합니다. 이 페이지는
그 아이콘들의 열쇠입니다 — 각각이 무엇을 뜻하고 어떤 인게임 상인을 가리키는지 알려줍니다. 서비스
아이콘은 **[uo.com](https://uo.com/)** 제공입니다.

## 아이콘

| 아이콘 | 서비스 | 거기서 찾을 수 있는 것 |
|------|---------|------------------------|
| <img src="/img/services/bank.gif" alt="Bank" width="28" /> | **은행(Bank)** | 은행원(보통 주조인 포함). 도시 간 공유 보관소이자 사실상 거래의 중심지. [상인 & 은행](/ko/playing/vendors-and-banking/) 참고. |
| <img src="/img/services/blacksmith.gif" alt="Blacksmith" width="28" /> | **대장장이(Blacksmith / Smithy)** | 대장장이, 갑옷장인, 무기장인 — 금속 무기와 방어구를 사고팔며, 주괴와 대장 도구를 판매. [대장장이(Blacksmith)](/ko/professions/blacksmith/) 참고. |
| <img src="/img/services/tinker.gif" alt="Tinker" width="28" /> | **땜장이(Tinker)** | 도구, 부품, 태엽 장치. [땜장이(Tinker)](/ko/professions/tinker/) 참고. |
| <img src="/img/services/carpenter.gif" alt="Carpenter" width="28" /> | **목수(Carpenter)** | 판자, 목공 도구, 완성 가구. [목수 & 활장인(Carpenter & Bowyer)](/ko/professions/carpenter-bowyer/) 참고. |
| <img src="/img/services/bowyer.gif" alt="Bowyer" width="28" /> | **활장인(Bowyer / Fletcher)** | 활, 석궁, 화살, 볼트. [목수 & 활장인(Carpenter & Bowyer)](/ko/professions/carpenter-bowyer/) 참고. |
| <img src="/img/services/tailor.gif" alt="Tailor" width="28" /> | **재단사(Tailor / Leatherworker)** | 천, 가죽, 재봉 키트, 의류; 모피상과 무두장이가 생가죽을 공급. [재단사(Tailor)](/ko/professions/tailor/) 참고. |
| <img src="/img/services/jeweler.gif" alt="Jeweler" width="28" /> | **보석상(Jeweler)** | 보석, 반지, 목걸이. |
| <img src="/img/services/mage.gif" alt="Mage shop" width="28" /> | **메이지 상점(Mage shop)** | 주문 두루마리, 주문서, 완드, 지팡이. [메이지(Mage)](/ko/professions/mage/)와 [마법술(Magery)](/ko/skills/magery/) 참고. |
| <img src="/img/services/reagents.gif" alt="Reagents" width="28" /> | **시약 / 연금술사(Reagents / Alchemist)** | 여덟 가지 시약과 물약을 파는 연금술사 또는 약초상. [시약(Reagents)](/ko/items/reagents/)과 [연금술사(Alchemist)](/ko/professions/alchemist/) 참고. |
| <img src="/img/services/eye.gif" alt="Scribe / library" width="28" /> | **필경사 / 도서관(Scribe / Library)** | 필사 용품과 빈 두루마리를 파는 필경사; 학문의 도시에서는 지식의 도서관. [필경사(Scribe)](/ko/professions/scribe/) 참고. |
| <img src="/img/services/healer.gif" alt="Healer" width="28" /> | **치료사(Healer)** | 치유 서비스, 붕대, 그리고 신전이나 치료사에게 도달한 유령의 부활. [치유(Healing)](/ko/skills/healing/) 참고. |
| <img src="/img/services/provisioner.gif" alt="Provisioner" width="28" /> | **잡화상(Provisioner)** | 일반 상점 — 횃불, 음식, 기본 보급품, 그리고 근처에 신발을 파는 제화공. |
| <img src="/img/services/baker.gif" alt="Baker" width="28" /> | **제빵사(Baker)** | 빵, 반죽, 제빵 재료; 종종 음식거리를 위한 정육점과 농부가 근처에. |
| <img src="/img/services/stables.gif" alt="Stables" width="28" /> | **마구간 / 동물 조련사(Stables / Animal trainer)** | 동물 조련사와 수의사 — 펫을 맡기고 탈것을 구매. [조련사(Tamer)](/ko/professions/tamer/)와 [동물 조련(Animal Taming)](/ko/skills/animal-taming/) 참고. |
| <img src="/img/services/inn.gif" alt="Inn" width="28" /> | **여관(Inn)** | 안전하게 로그아웃할 장소를 제공하는 여관 주인, 역사적으로는 임대 객실도. |
| <img src="/img/services/tavern.gif" alt="Tavern" width="28" /> | **선술집(Tavern)** | 술집 주인, 요리사, 선술집 지기 — 음식, 술, 그리고 동네 소문. |

## 참고

- 마을에 표시된 서비스는 지도 데이터(`data/map_pois.json`)에 그 도시 근처로 기록된 **실제 NPC 상인
  스폰**에서 가져온 것이므로, 아이콘은 단순한 설정이 아니라 우리 샤드의 월드에 실제로 존재하는 것을
  반영합니다.
- 일부 상인은 한 건물을 공유하며(예를 들어 한 상점 주인이 "제화공, 잡화상"일 수 있음), 일부 전문
  훈련사(음유시인, 어부, 지도 제작자, 조선공)는 전용 아이콘 없이 마을에 나타납니다 — 도시 페이지가
  그런 경우를 본문에서 별도로 언급합니다.

## 관련 문서

- [월드 개요](/ko/world/) · [상인 & 은행](/ko/playing/vendors-and-banking/)
- [직업(Professions)](/ko/professions/) — 모든 제작과 전투 경로
