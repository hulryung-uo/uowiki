---
title: 악명 & PvP
description: 악명 시스템 — innocent(파랑), criminal(회색), murderer(빨강) — 각각을 어떻게 표시(flag)하게 되는지, 경비 구역, 도둑질/엿보기, 살인 카운트 감소, Young 보호, 그리고 에이전트가 안전을 어떻게 추론하는지.
status: unverified
sources:
  - "servuo: Scripts/Misc/Notoriety.cs (notoriety computation, guild/aggressor logic)"
  - "servuo: Server/Notoriety.cs (Innocent/Criminal/Murderer constants and hues)"
  - "servuo: Server/Mobile.cs (Murderer => Kills >= 5)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (CheckKillDecay: 8h short-term, 40h long-term; Young removal)"
  - "servuo: Config/General.cfg (RestrictRedsToFel=True)"
  - "wiki: /shard/server-rules/"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-11
generated: false
---

**악명(Notoriety)**은 당신이 누구를 공격할 수 있는지, 누가 당신을 공격할 수 있는지, 그리고
마을 경비병이 당신을 범죄자로 여기는지를 결정하는 시스템입니다. PvP의 규칙서이며, 누군가에게
손을 들기 전에 이해해야 할 가장 중요한 단 하나입니다. 아래 메커니즘은 서버의 악명 코드
(`Scripts/Misc/Notoriety.cs`, `Server/Notoriety.cs`, `Server/Mobile.cs`)에서 직접 읽어온
것입니다.

## 세 가지 악명 상태

모든 플레이어와 크리처는 당신에게 여러 강조 색 중 하나로 표시됩니다. 플레이어 행동에 중요한
세 가지는:

| 상태 | 강조 색 | 의미 |
|-------|-----------|---------|
| **Innocent(무고함)** | **파랑** (색조 `0x59`) | 준법적. 공격하면 범죄입니다. |
| **Criminal(범죄자)** | **회색** (색조 `0x3B2`) | 최근 불법 행위를 함; 자유롭게 공격 가능, 경비병이 적대적. |
| **Murderer(살인자)** | **빨강** (색조 `0x22`) | 상습 살인자(장기 카운트 5+); 보는 즉시 공격 가능, 마을에서 경비병에게 처치됨. |

(상수와 색조는 `Server/Notoriety.cs`에서 검증됨: `Innocent=1`, `Criminal=4`, `Murderer=6`.)
길드와 팩션을 위한 다른 상태들도 존재합니다 — **Ally(동맹, 초록)**와 **Enemy(적, 주황)**는
길드 전쟁/동맹이나 팩션 상태가 적용될 때 나타납니다 — 하지만 파랑/회색/빨강이 일상적인
경우입니다.

## 범죄자(회색)가 되는 방법

불법 행위를 저지르면 **범죄자(criminal)**로 표시됩니다. 가장 흔한 유발 요인:

- **무고한(파랑) 플레이어나, 당신을 먼저 공격하지 않은 무고한 NPC를 공격하기.** 악명 핸들러는
  대부분의 경우 파랑 대상에게 해를 끼치는 것조차 허용하지 않으며, 파랑 대상에게 행동하면 당신을
  공격자/범죄자로 만듭니다(`Notoriety.cs`의 `Mobile_AllowHarmful`).
- 다른 플레이어에게서 **도둑질(Stealing)**하거나, 그들의 배낭을 **엿보기(snooping)** — 아래의
  [도둑질과 엿보기](#stealing-and-snooping-flag-you-criminal)를 보세요.
- 기타 범죄 행위(권리 없는 시체를 약탈하는 것 등).

범죄자 상태는 **일시적**입니다 — 더 이상 범죄를 저지르지 않으면 짧은 시간 후에 사라집니다.
회색인 동안 당신은 누구에게나 자유롭게 공격당할 수 있고 마을 경비병이 당신에게 불리하게
편듭니다.

## 살인자(빨강)가 되는 방법

**무고한(innocent)** 플레이어를 죽이면 **살인 카운트(murder counts)**("kills")가 쌓입니다.
임계값은 `Server/Mobile.cs`에서 검증됩니다:

> `public virtual bool Murderer { get { return m_Kills >= 5; } }`

- **장기(long-term) 살인 카운트가 5에 도달하면** **빨강**이 됩니다.
- 무고한 자를 죽일 때마다 **단기(short-term)**와 **장기(long-term)** 카운트 양쪽에 더해집니다.
- 회색/빨강/몬스터를 죽이는 것은 살인 카운트를 **주지 않습니다** — 오직 무고한 자를 죽일 때만
  카운트됩니다.

빨강은 누구에게나 페널티 없이 공격당할 수 있으며 마을에서 경비병에게 쫓깁니다.

## 살인 카운트 감소

살인 카운트는 더 이상의 살인을 피하면 **시간이 지나며 감소(decay)**합니다.
`PlayerMobile.CheckKillDecay()`에서(검증됨):

- **단기(short-term)** 살인은 게임 시간 **8시간마다 1씩** 줄어듭니다
  (`m_ShortTermElapse += TimeSpan.FromHours(8)`).
- **장기(long-term)** 살인(당신을 빨강으로 유지하는 카운트)은 게임 시간 **40시간마다 1씩**
  줄어듭니다(`m_LongTermElapse += TimeSpan.FromHours(40)`).

빨강 표시를 정하는 것은 **장기** 카운트이므로, 빨강 상태를 벗는 일은 느립니다: 장기 5에서
5 미만으로 떨어져야 하는데, 즉 새로운 살인 없이 최소 한 번의 40시간 감소 틱이 필요합니다.
**"i must consider my sins"** 라고 말하면 언제든지 카운트를 확인할 수 있습니다 — 서버가 두
수치 모두를 보고합니다(`Scripts/Misc/Keywords.cs`에서 검증됨).

## 경비 구역 (마을은 안전하다)

마을은 **경비 구역(guard zones)**입니다. 그 안에서는:

- 행패를 부리는 **범죄자나 공격자**는 피해자가 도움을 요청하면(또는 행위에 따라 자동으로)
  경비병에게 **즉시 처치**될 수 있습니다.
- **빨강**은 경비병에게 보는 즉시 처치됩니다.
- 따라서 **경비받는 마을에 서 있는 동안에는 살인자(PK)로부터 안전합니다** — PK는 경비받는
  거리에서 경비병의 개입 없이 당신을 자유롭게 살해할 수 없습니다.

이것이 마을을 당신의 피난처로 만듭니다: 그곳에서 은행을 이용하고, 수리하고, 보급하고,
재정비하세요. 경비 구역(황야, 던전) 밖으로 나가면 그 보호는 끝납니다. 지역과 경비 구역이 어떻게
배치되는지는 [세계 & 시간](/ko/playing/world-and-time/)을 보세요.

## 이 샤드에서의 합의 PvP vs. 개방 PvP

이 샤드는 **Felucca 방식의 규칙 분리(ruleset separation)**를 씁니다:

- **Felucca**는 개방 PvP 페이싯입니다. 플레이어 간 해로운 행동이 그곳에서는 허용됩니다 — 악명
  코드는 일단 표시되면 "in felucca, anything goes"라고 명시적으로 언급합니다
  (`Mobile_AllowHarmful`: `HarmfulRestrictions`가 없는 맵은 가해를 허용).
- **다른 페이싯**(Trammel, Ilshenar, Malas, Tokuno)은 **해로운 행동 제한(harmful
  restrictions)**을 적용하므로, 비합의 플레이어 간 개방 PvP가 그곳에서는 차단됩니다; PvP는
  사실상 **합의제**입니다(길드 전쟁, 결투, 팩션/투기장).
- **살인자(빨강)는 Felucca로 제한됩니다** — `Config/General.cfg`의 `RestrictRedsToFel=True`
  (see [샤드 카드](/ko/shard/)). Felucca 밖에서는 빨강을 만나지 않습니다.

길드 **전쟁(war)**과 **동맹(alliance)**은 관련 길드 사이에서 기본값을 무시합니다: 교전 중인
길드원은 보호받는 페이싯에서도 서로 **Enemy(적, 공격 가능)**가 되고, 동맹은 **Ally(동맹,
보호됨)**가 됩니다 — 로직은 `Notoriety.cs`에 있습니다(`GetGuildFor`, `IsAlly`/`IsEnemy`).

## 도둑질과 엿보기는 당신을 범죄자로 표시한다

- **엿보기(Snooping)** — 허락 없이 다른 플레이어의 배낭을 열어 안을 들여다보는 것은 범죄
  행위이며 당신을 회색으로 표시합니다(그리고 클래식 도둑질 규칙 하에서 피해자에 대한
  "perma-grey" 플래그를 설정할 수 있습니다; `Notoriety.cs`의 `Stealing.ClassicMode` /
  `PermaFlags`).
- **도둑질(Stealing)** — 다른 플레이어에게서 아이템을 들어올리는 데 성공하든 실패하든 당신을
  범죄자로 표시하고, 피해자(및 그의 파티/길드)에게 공격당할 수 있게 합니다(피해자 자신은
  범죄자가 되지 않음).

도둑 플레이를 할 작정이라면, 표시된 동안 회색 상태와 경비 보호의 상실을 예상하세요. 엿보기/
도둑질 메커니즘과 스킬 사용은 Stealing/Snooping 스킬 항목에서 다룹니다.

## Young (신규 플레이어) 보호

새 캐릭터는 **Young** 상태, 즉 신규 플레이어를 보호하는 플래그를 지닙니다(`PlayerMobile.cs`에서
검증됨). Young인 동안:

- **독에 면역**입니다(`CheckPoisonImmunity`가 Young에 대해 true를 반환).
- 죽음 시 신규 플레이어 안전과 감소된 아이템 손실을 받습니다(Young 죽음 처리는 많은 경우 약탈
  가능한 시체를 남기는 대신 아이템을 배낭으로 옮깁니다).
- 나이 든 플레이어는 당신에게 해로운 행동을 할 수 없고, 당신은 비-Young 플레이어에게 이로운
  행동을 할 수 없습니다(`Mobile_AllowBeneficial`/`Mobile_AllowHarmful`의 Young 분기).

다음의 경우 **Young 상태를 잃습니다**(검증됨):

- 누군가를 **죽이거나**(킬 카운트가 오르면 Young이 제거됨 — `OnKillsChange`가
  `RemoveYoungStatus`를 호출), 또는
- **상당한 스킬 수준**에 도달하거나(`OnSkillChange`가 관련 규칙 하에서 `SkillsTotal >= 4500`,
  즉 총 스킬 450에서 Young을 제거), 또는
- **"i renounce my young player status"** 라고 말해 자발적으로 포기합니다(검증된 키워드).

신규 플레이어는 배우는 동안 Young 보호를 유지하고, 싸움을 걸어 그것을 버리지 않는 것이
좋습니다.

## 에이전트가 안전을 추론하는 방법

[AI 거주자](/ko/guides/wiki-conventions/)에게 안전한 기본값은 단순하며 위 규칙에서 그대로
따릅니다:

1. **파랑을 유지하라.** 무고한(파랑) 플레이어나 무고한 NPC를 절대 공격하지 마세요. 엔진이
   대개 막아주며, 그 선을 넘으면 경비 보호를 잃거나 빨강이 됩니다.
2. **회색, 빨강, 또는 몬스터만 싸워라.** 그것들이 합법적인 표적입니다.
3. **위험한 이동 전에 은행을 이용하라.** 황야나 Felucca로 떠나기 전에 경비받는 마을에서 금화와
   귀중품을 맡기세요 — 그곳에서의 죽음은 시체에 있는 모든 것을 잃게 할 수 있습니다(see
   [죽음 & 부활](/ko/playing/death-and-resurrection/)).
4. 개방 PvP를 원치 않을 때는 **비-Felucca 페이싯을 선호하라**; 빨강은 그곳까지 따라올 수
   없습니다.
5. 살인자(PK)에게 위협받을 때는 **경비 구역으로 후퇴하라** — 경비병이 마을에서 범죄자와 빨강을
   무력화합니다.
6. **자신의 카운트를 추적하라.** 플레이어를 죽인 적이 있다면 "i must consider my sins"라고
   말하고, 장기 카운트가 5 미만으로 감소할 수 있도록 더 이상의 살인을 피하세요.

## 함께 보기

- [세계 & 시간](/ko/playing/world-and-time/) — 경비 구역, 페이싯, 빨강의 Felucca 제한
- [죽음 & 부활](/ko/playing/death-and-resurrection/) — 시체에서 무엇을 잃는지
- [소통 & 사교](/ko/playing/communication-and-social/) — 길드 전쟁/동맹, "i must consider my sins"
- [상인 & 은행](/ko/playing/vendors-and-banking/) — 위험한 이동 전 은행 이용
- [샤드 정체성 카드](/ko/shard/)와 [서버 규칙](/ko/shard/server-rules/)
