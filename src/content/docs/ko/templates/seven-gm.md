---
title: "7x GM 템플릿"
description: 고전 Ultima Online 엔드게임 — 700.0 총합 한계 안에서 일곱 스킬을 그랜드마스터(각 100.0)로, 목적별로 정리하고 강점, 약점, 스탯 메모를 곁들임.
status: unverified
sources:
  - "servuo: Config/PlayerCaps.cfg (700 total cap)"
  - "reference: classic UO template conventions"
  - "general UO community build knowledge"
last_verified: 2026-06-11
generated: false
---

:::note[커뮤니티 빌드 지혜]
여기 인용된 스킬 메커니즘(700.0 한계, 스킬당 100.0 한계, 성장 거동)은 이 샤드의
[설정](/ko/shard/)과 [스킬 성장](/ko/mechanics/skill-gain/)에 대해 소스 검증되었습니다. *템플릿
자체*는 이 서버에 맞춰 적응된 고전 UO 커뮤니티 관례입니다 — 검증된 형태이지, 필드 검증된 경로는
아닙니다. [위키 규약](/ko/guides/wiki-conventions/)에 따라 불일치를 신고하세요.
:::

## 700.0 한계와 "7x GM"의 의미

이 샤드에서 당신의 캐릭터는 **700.0 총 스킬 한계**를 가지며 개별 스킬은 각각 **100.0**에서
한계에 달합니다 — [샤드 요약](/ko/shard/)과 [스킬 성장](/ko/mechanics/skill-gain/) 참고.
"그랜드마스터"(GM)는 어떤 스킬에서 100.0에 이르면 얻는 칭호입니다. 일곱 스킬 × 100.0 = **700.0**,
정확히 총 한계입니다. 이것이 **7x GM**(또는 **7-GM**으로도 표기) 템플릿의 핵심 아이디어 전부입니다:
천장에 올리고 싶은 일곱 스킬을 고르면, 스킬 예산 전체를 쓴 것입니다. 여덟 번째 스킬을 밀어 올리면
서버가 어딘가에서 같은 양만큼 *강제로 내립니다* — 한계는 제안이 아니라 단단한 벽입니다.

일곱 슬롯밖에 없으니, 스킬을 무작위로 고르지 않습니다 — **목적**을 위한 템플릿을 고릅니다: 당신이
*할 수* 있고 싶은 것. 흔한 목적들:

- **근접(Melee)** — 무기로 때리고 살아남기("덱서").
- **시전(Cast)** — 데미지와 유틸리티를 위해 주문을 던지기(메이지).
- **길들이기(Tame)** — 강력한 펫에게 명령해 대신 싸우게 하기.
- **지원 / 군중 제어** — 방 전체를 매혹, 진정, 약화시키는 음유시인.
- **스텔스(Stealth)** — 숨어서 치고 사라지기.
- **제작(Craft)** — 장비, 도구, 소모품을 생산하기.

스탯도 스킬만큼 중요합니다. 당신의 세 능력치(STR/DEX/INT)는 별도의 **225 총 한계**를 공유하며, 그
배분 방식이 같은 일곱 스킬을 아주 다른 캐릭터로 빚어냅니다 — [캐릭터 & 스탯](/ko/playing/character-and-stats/)
참고. 아래 각 템플릿은 권장 스탯 성향을 포함합니다.

## 템플릿 읽는 법

아래 모든 빌드는 다음을 나열합니다:

- **7 스킬** — 각각 정확한 메커니즘을 위해 해당 [스킬 페이지](/ko/skills/)로 링크됨.
- **목적 / 하는 일** — 역할과 승리 조건(빌드가 실제로 어떻게 싸움에서 이기거나 일을 해내는지).
- **강점 / 약점** — 무엇에 뛰어나고 어디서 무너지는지.
- **권장 스탯** — 225 한계 안의 STR/DEX/INT 성향.

읽으면서 플레이 방법 가이드를 교차 참조하세요: [전투 기초](/ko/playing/combat-basics/),
[주문 시전](/ko/playing/spellcasting/), [명상 & 마나](/ko/playing/meditation-and-mana/),
[길들이기 & 펫](/ko/playing/taming-and-pets/), [제작](/ko/playing/crafting/),
[은신 & 스텔스](/ko/playing/hiding-and-stealth/), 그리고
[악명 & PvP](/ko/playing/notoriety-and-pvp/). 이 원형들 중 여럿은 전용 공략 페이지도 있습니다:
[전사(Warrior)](/ko/templates/warrior/), [메이지(Mage)](/ko/templates/mage/),
[동물 조련사(Animal Tamer)](/ko/templates/animal-tamer/), [대장장이(Blacksmith)](/ko/templates/blacksmith/),
그리고 [벌목꾼(Lumberjack)](/ko/templates/lumberjack/).

## 소드 덱서(Sword Dexxer)

**스킬:** [Swordsmanship](/ko/skills/swordsmanship/), [Tactics](/ko/skills/tactics/),
[Anatomy](/ko/skills/anatomy/), [Healing](/ko/skills/healing/),
[Resisting Spells](/ko/skills/resisting-spells/), [Magery](/ko/skills/magery/),
[Meditation](/ko/skills/meditation/).

**목적 / 하는 일:** 기본 중의 기본인 근접 빌드. Swordsmanship이 무기 스킬이고, Tactics와 Anatomy가
데미지를 곱하며, Healing이 붕대를 재생 가능한 체력 바로 바꿉니다(그리고 높은 Anatomy/Healing에서는
자가 부활). Resisting Spells가 적의 마법을 무디게 합니다. Magery와 Meditation은 데미지가 아니라
*유틸리티*입니다: 이동용 Recall과 Gate, 붕대를 받쳐주는 Greater Heal과 Cure, 그리고 마나를 환급하는
Meditation. 승리 조건은 소모전입니다 — 들어오는 데미지를 능가해 치유하며 대상을 갈아 넘어뜨리기.
[전투 기초](/ko/playing/combat-basics/) 참고.

**강점:** 운영이 저렴하고(시약이 아닌 붕대), 너그럽고, 자급자족하며, Recall 덕에 기동성 있음. 뛰어난
솔로 PvM.

**약점:** 제한된 순간 화력 — 천천히 이깁니다. 분산된 집중 탓에 Magery는 공격적으로 약하고, 군중
제어가 없습니다.

**권장 스탯:** ~100 STR / ~90 DEX / ~35 INT. STR은 체력과 데미지, DEX는 휘두르기와 붕대 속도; INT는
유틸리티 주문을 시전할 만큼만 높게.

**변형:**

- **메이스 / 펜싱 / 궁수 덱서** — [Swordsmanship](/ko/skills/swordsmanship/)을
  [Mace Fighting](/ko/skills/mace-fighting/), [Fencing](/ko/skills/fencing/),
  [Archery](/ko/skills/archery/)로 교체. 메이스는 일부 방어구를 무시하고 기절시킬 수 있고; 펜싱은
  빠르고 독을 묻힐 수 있으며; 궁수는 원거리에서 싸웁니다. 나머지 여섯 스킬은 그대로입니다.
- **패리 덱서** — 시전자 스킬 하나(보통 Meditation, 때로 Magery)를 [Parrying](/ko/skills/parrying/)으로
  버려 방패로 들어오는 타격의 일부를 막기. 자가 시전 유틸리티를 순수 방어와 맞바꿉니다.

## 퓨어 메이지(Pure Mage)

**스킬:** [Magery](/ko/skills/magery/), [Evaluating Intelligence](/ko/skills/evaluating-intelligence/),
[Meditation](/ko/skills/meditation/), [Wrestling](/ko/skills/wrestling/),
[Resisting Spells](/ko/skills/resisting-spells/), [Inscription](/ko/skills/inscription/), 그리고
**자유** 슬롯(흔히 [Anatomy](/ko/skills/anatomy/)나 음유시인 스킬).

**목적 / 하는 일:** 유리 대포 시전자. Magery가 당신이 하는 모든 것; Eval Int가 주문 데미지를
올리고; Meditation이 마나를 빠르게 채워 계속 시전하게 하며; Inscription이 주문 데미지 보너스를
더하고 직접 스크롤을 필사하게 합니다. Resisting Spells가 메이지 대 메이지 싸움에서 당신을
보호합니다. [Wrestling](/ko/skills/wrestling/)은 당신의 **맨손 방어**입니다 — 무기 스킬이 없으니,
GM Wrestling이 시전 중단을 막고 무장 해제나 마비 타격을 넣게 합니다. 승리 조건은 순간 화력입니다:
Eval로 강화된 주문(Explosion + Energy Bolt 콤보, Flamestrike)을 대상이 치유하는 것보다 빠르게
쌓기. [주문 시전](/ko/playing/spellcasting/)과 [명상 & 마나](/ko/playing/meditation-and-mana/) 참고.

**강점:** 최고의 순간 데미지, 완전한 기동성(Recall/Gate), 원거리, 유연한 유틸리티(Cure, Bless,
Reveal, Invisibility, 필드).

**약점:** 약함 — 낮은 체력, 근접 대상이 붙으면 빨리 죽음. 시약 비용이 쌓임. 주문이 "시전되는" 동안
취약.

**권장 스탯:** ~25 STR / ~10 DEX / ~100 INT (INT가 당신의 마나 풀). INT를 천장까지 펌프; 생존용 STR
약간.

## 탱크 메이지(Tank Mage)

**스킬:** [Magery](/ko/skills/magery/), [Evaluating Intelligence](/ko/skills/evaluating-intelligence/),
[Meditation](/ko/skills/meditation/), [Resisting Spells](/ko/skills/resisting-spells/),
[Wrestling](/ko/skills/wrestling/), [Tactics](/ko/skills/tactics/), [Anatomy](/ko/skills/anatomy/).

**목적 / 하는 일:** 고전적인 PvP 하이브리드 — **근접으로 싸우면서 동시에 시전**합니다. Wrestling,
Tactics, Anatomy가 당신의 주먹을 진짜 무기로 만들어, 무기를 뽑지 않고도 주먹질*과* 시전을 할 수
있습니다(재무장 위한 더듬거림 없음). Magery/Eval/Med가 핵과 치유를 전달하고; Resist가 시전자 결투에서
당신을 버티게 합니다. 승리 조건은 두 방향에서의 압박입니다: 근접 타격을 계속해 적을 중단시키면서
주문 콤보를 넣기. [악명 & PvP](/ko/playing/notoriety-and-pvp/) 참고.

**강점:** 중단시키기 어렵고, 시전자치고 내구력 있고, 모든 사거리에서 위험하며, 떨어뜨리거나 잃을
무기가 없음.

**약점:** 퓨어 메이지보다 낮은 주문 데미지(Inscription 보너스 없음), 덱서보다 낮은 근접 데미지.
수동적으로 플레이하면 어중간함 — 공격성에 보상합니다.

**권장 스탯:** ~75 STR / ~35 DEX / ~115 INT, 체력, 마나, 그리고 쓸 만한 주먹을 위해 균형 잡힘.

## 동물 조련사(Animal Tamer)

**스킬:** [Animal Taming](/ko/skills/animal-taming/), [Animal Lore](/ko/skills/animal-lore/),
[Veterinary](/ko/skills/veterinary/), [Magery](/ko/skills/magery/), [Meditation](/ko/skills/meditation/),
그리고 [Evaluating Intelligence](/ko/skills/evaluating-intelligence/) /
[Resisting Spells](/ko/skills/resisting-spells/) 중 둘(하나가 **자유** 슬롯).

**목적 / 하는 일:** 당신은 싸우지 않습니다 — 당신의 **펫**이 싸웁니다. Animal Taming이 강한 생물을
매혹하게 하고, Animal Lore가 그중 최고를 길들이고 명령하는 데 필요하며, Veterinary가 붕대와 해독으로
펫을 살려둡니다. Magery/Meditation이 Recall 기동성, Vet를 받쳐줄 치유, 그리고 펫에게 거는 Greater
Heal을 줍니다. 승리 조건은 당신이 뒤로 빠져 지원하는 동안 강력한 길들인 생물(드래곤, 최강 펫)이
죽이는 것입니다. 전체 공략은 [동물 조련사 템플릿](/ko/templates/animal-tamer/); 메커니즘은
[길들이기 & 펫](/ko/playing/taming-and-pets/).

**강점:** PvM에서 최고의 지속 살상력 — 최상위 펫은 대부분의 솔로 빌드를 데미지로 능가합니다. 안전한
플레이 스타일(뒤로 빠짐). 한 캐릭터에 둘(당신 + 펫).

**약점:** 펫 관리는 물류입니다 — 마구간, 먹이기, 컨트롤 확률, 그리고 비싼 펫을 잃을 위험. 펫이
죽거나 유인당하면 본인은 약함.

**권장 스탯:** ~30 STR / ~20 DEX / ~100+ INT — 당신은 사실상 지원 시전자이니, INT(마나)가 앞섭니다.

## 음유시인(Bard)

**스킬:** [Musicianship](/ko/skills/musicianship/)에 더해
[Provocation](/ko/skills/provocation/) / [Peacemaking](/ko/skills/peacemaking/) /
[Discordance](/ko/skills/discordance/) 중 둘 또는 셋, 그리고 [Magery](/ko/skills/magery/),
[Meditation](/ko/skills/meditation/), [Resisting Spells](/ko/skills/resisting-spells/)로 마무리.

**목적 / 하는 일:** 군중 제어와 지원. **Musicianship**이 관문입니다 — 모든 음유시인 능력은 악기와
성공한 Musicianship 판정을 요구합니다. 세 노래 스킬은 각각 다른 일을 합니다:

- **[Provocation](/ko/skills/provocation/)** — 두 몬스터가 서로 등을 돌리게 해 당신을 *위해* 싸우게
  하기. 도발자는 한 대도 안 맞고 방을 비울 수 있습니다.
- **[Peacemaking](/ko/skills/peacemaking/)** — 대상(또는 영역)을 진정시켜 싸움을 멈추게 해, 나쁜
  풀을 리셋하거나 탈출하게 하기.
- **[Discordance](/ko/skills/discordance/)** — 대상의 스킬과 스탯을 디버프해, 다른 모든 것(당신 펫,
  당신 파티, 당신 자신의 공격)이 더 세게 맞게 하기.

Magery/Med/Resist가 음유시인에게 기동성, 치유, 시전자 방어를 줍니다. 승리 조건은 **제어**입니다:
누가 누구와 싸울지, 누가 싸우기는 할지, 그리고 그동안 그들이 얼마나 약한지를 당신이 결정합니다. 많은
음유시인은 노래를 무기나 펫과 짝지어 실제 처치를 합니다.

**강점:** 비할 데 없는 군중 제어, 솔로 덱서를 압도하는 무리를 다룰 수 있음, 그룹에서 강하며, 어떤
파티든 전력 증폭.

**약점:** 낮은 개인 데미지 — 순수 음유시인은 천천히 죽입니다. 노래는 고레벨이나 "노래 면역" 생물에게
실패할 수 있고, 악기는 닳습니다.

**권장 스탯:** ~25 STR / ~10 DEX / ~100 INT, 노래 사이에 시전하고 명상하니 시전자 쪽으로 기움.

## 스텔스 궁수 / 스카우트

**스킬:** [Archery](/ko/skills/archery/), [Tactics](/ko/skills/tactics/),
[Anatomy](/ko/skills/anatomy/), [Healing](/ko/skills/healing/), [Hiding](/ko/skills/hiding/),
[Stealth](/ko/skills/stealth/), 그리고 **자유** 슬롯(흔히
[Resisting Spells](/ko/skills/resisting-spells/)나 [Magery](/ko/skills/magery/)).

**목적 / 하는 일:** 치고 사라지기. Archery가 원거리 데미지를 전달하고; Tactics와 Anatomy가 그것을
올리며; Healing이 당신을 수습합니다. 시그니처는 스텔스 한 쌍입니다: [Hiding](/ko/skills/hiding/)이
당신을 화면에서 지우고 [Stealth](/ko/skills/stealth/)가 *숨은 채 이동*하게 합니다. 살금살금 다가가,
강한 원거리 일격으로 열고, 대상이 닿기 전에 다시 은신으로 빠집니다. 승리 조건은 선제와 위치
선정입니다 — 싸움이 언제 시작할지 당신이 고르고 언제나 이탈할 수 있습니다.
[은신 & 스텔스](/ko/playing/hiding-and-stealth/) 참고.

**강점:** 교전 거리 제어, 정찰과 매복에 탁월, 강한 탈출 도구, 치명적인 개막 화력.

**약점:** 정면 근접에서 약함, 지형과 시야선에 의존, 탄약 물류(화살), 그리고 적이 가까우면 재은신이
실패할 수 있음.

**권장 스탯:** ~90 STR / ~100 DEX / ~35 INT. DEX가 활 속도를 좌우; STR은 생존용.

## 도둑 / 로그(Thief / Rogue)

**스킬:** [Stealing](/ko/skills/stealing/), [Snooping](/ko/skills/snooping/),
[Hiding](/ko/skills/hiding/), [Stealth](/ko/skills/stealth/), [Lockpicking](/ko/skills/lockpicking/),
그리고 **유틸리티** 스킬 둘(흔히 [Detecting Hidden](/ko/skills/detecting-hidden/),
백업 무기용 [Tactics](/ko/skills/tactics/), [Magery](/ko/skills/magery/), 또는
[Resisting Spells](/ko/skills/resisting-spells/)).

**목적 / 하는 일:** 절도와 잠입. **Snooping**이 다른 플레이어의 가방 안을 엿봐 무엇이 가져갈 가치가
있는지 알려주고; **Stealing**이 그것을 들어 올립니다. Hiding과 Stealth가 안 보이게 드나들게 하고;
Lockpicking이 상자를 엽니다(그리고 전리품으로 가는 길을 무력화). 승리 조건은 처치가 아니라
한탕입니다 — 남이 번 것을 가져가 사라지기. 이것은 PvP/상호작용 주도 플레이 스타일이니, 먼저
[악명 & PvP](/ko/playing/notoriety-and-pvp/)에서 규칙을 이해하세요.

**강점:** 독특한 플레이 스타일, 싸움을 이기지 않고도 이득을 봄, 강한 스텔스와 탈출 키트, 잠긴
콘텐츠를 엶.

**약점:** 자체 전투력이 거의 또는 전혀 없음, 고위험(잡히면 표적이 됨), 그리고 효과가 샤드의 절도
규칙에 크게 좌우됨.

**권장 스탯:** ~40 STR / ~80 DEX / ~25 INT — 절도/탈출 속도용 DEX와, 휴대한다면 가벼운 무기.

## 제작자(Smith / Tailor)

**스킬:** [Blacksmithy](/ko/skills/blacksmithy/), [Mining](/ko/skills/mining/),
[Tinkering](/ko/skills/tinkering/), [Tailoring](/ko/skills/tailoring/),
[Carpentry](/ko/skills/carpentry/), [Arms Lore](/ko/skills/arms-lore/), 그리고 **자유** 슬롯
(흔히 이동용 [Magery](/ko/skills/magery/), 또는 재료용
[Lumberjacking](/ko/skills/lumberjacking/) / [Fishing](/ko/skills/fishing/)).

**목적 / 하는 일:** 생산. 이 빌드는 다른 모두가 사는 장비를 *만듭니다* — 무기와 방어구(Blacksmithy),
의류와 가죽 방어구(Tailoring), 가구, 활, 집(Carpentry), 도구와 유용한 장치(Tinkering). Mining이
화로에 광석을 먹이고; Arms Lore가 제작 무기와 방어구의 품질을 올립니다. 승리 조건은 경제적입니다:
GM 제작자는 곧 상점입니다. [제작](/ko/playing/crafting/)과
[자원 채집](/ko/playing/gathering-resources/) 참고; 전체 경로는
[대장장이 템플릿](/ko/templates/blacksmith/).

**강점:** 무한정 돈과 장비를 만듦, 소모품이 떨어지지 않음, 길드에 귀중, 낮은 전투 리스크.

**약점:** **전투 능력이 거의 없음.** 이것이 700 한계가 강제 기능으로 작용하는 가장 명확한
예입니다: 7x 제작자는 일곱 슬롯 전부를 생산에 썼으니, *동시에* 7x 전사일 수는 없습니다. 대부분의
플레이어는 제작자를 **별도 캐릭터**로 운영합니다.

**권장 스탯:** ~100 STR / ~25 DEX / ~100 INT. STR이 채광 수율과 일부 레시피의 제작 성공을 올리고;
INT가 Magery 자유 슬롯을 받쳐줍니다.

## 네크로 메이지 / 스펠위버 / 미스틱

**스킬:** 현대 시전자 학파 —
[Necromancy](/ko/skills/necromancy/) (+[Spirit Speak](/ko/skills/spirit-speak/)),
[Spellweaving](/ko/skills/spellweaving/) (+[Focus](/ko/skills/focus/)), 또는
[Mysticism](/ko/skills/mysticism/) (+[Focus](/ko/skills/focus/)) — 와 결합된
[Magery](/ko/skills/magery/), [Evaluating Intelligence](/ko/skills/evaluating-intelligence/),
[Meditation](/ko/skills/meditation/), [Resisting Spells](/ko/skills/resisting-spells/), 그리고
[Wrestling](/ko/skills/wrestling/).

**목적 / 하는 일:** Magery 코어에 두 번째 주문 학파를 볼트로 결합한 확장 시대 하이브리드 시전자.
**네크로 메이지**는 저주, 소환, 생명력 흡수를 더하고(Spirit Speak가 네크로 효과를 증폭); **스펠위버**는
비전 포커스, 소환, 영역 버프를 더하며; **미스틱**은 자체 원소와 소환 계열을 더합니다(Focus가
Spellweaving과 Mysticism 둘 다에 힘을 줌). 승리 조건은 메이지의 순간 화력과 같지만 — 저항을 우회할
추가 디버프, 소환, 데미지 타입과 함께. 이것들은 **확장 시대** 콘텐츠이기에 여기서 더 간략합니다;
이 샤드가 어떤 학파를 운영하고 그것들이 어떻게 상호작용하는지는
[마법 학파](/ko/playing/magic-schools/)를 참고하세요.

**강점:** 다양한 데미지 타입과 디버프, 소모용 아군으로서의 소환, 강한 PvM과 PvP 유연성.

**약점:** 시약과 자원을 많이 먹음, 플레이가 더 복잡함, 그리고 가용성이 전적으로 샤드의
[확장](/ko/shard/) 설정에 달림 — 헌신하기 전에 이 학파가 여기 존재하는지 확인하세요.

**권장 스탯:** ~30 STR / ~10 DEX / ~110 INT — 퓨어 메이지처럼 순수 시전자 성향.

## 강제 기능으로서의 700 한계

한계는 맞서 싸울 제약이 아니라 게임의 설계입니다. **모든 것을 할 수는 없습니다.** 일곱 슬롯은 모든
빌드가 의도적인 트레이드오프의 집합임을 뜻합니다:

- **하이브리드는 깊이를 폭과 맞바꿉니다.** 탱크 메이지는 싸우고 *동시에* 시전하지만, 퓨어 메이지보다
  핵이 약하고 덱서보다 타격이 약합니다. 패리 덱서는 자가 시전 유틸리티를 포기해 방패를 얻습니다.
  당신이 더하는 모든 "그리고"는 "그뿐 아니라"의 비용이 듭니다.
- **어떤 목적들은 그저 한 캐릭터를 공유하지 않습니다.** 7x 제작자와 7x 전사는 둘 다 일곱 슬롯 전부를
  원합니다 — 둘 다일 수는 없습니다. 이것이 대부분의 플레이어가 **여러 캐릭터**를 유지하는 이유입니다:
  전투 본캐와 제작자(그리고 어쩌면 조련사, 음유시인, 도둑)를 같은 계정에.
- **한계는 역할 안에서의 선택도 강제합니다.** Inscription의 데미지 보너스를 원하는 메이지는 음유시인
  스킬이나 Anatomy가 쓸 수 있었던 슬롯을 포기합니다. 언제나 기회비용이 있습니다.

:::caution[스킬 스크롤 / 파워 스크롤 — 이 샤드에서 unverified]
일부 샤드에서는 **파워 스크롤**(과 유사한 스킬 스크롤)이 *개별* 스킬의 한계를 100.0 위로 올리고 —
일부에서는 총 예산도 올려, 7×100 셈 전체를 바꿉니다. **그런 아이템이 이 샤드에 존재하는지, 그리고
무엇을 하는지는 여기서 unverified입니다.** 위의 700.0 총합 / 스킬당 100.0 모델을, 이 서버의
[설정](/ko/shard/)과 [스킬 성장](/ko/mechanics/skill-gain/) 규칙에 대해 확인될 때까지 기준선으로
취급하세요.
:::

## 함께 보기

- [스킬 성장 메커니즘](/ko/mechanics/skill-gain/) — 스킬이 어떻게 오르고 700에서 한계가 무엇을 하는지.
- [캐릭터 & 스탯](/ko/playing/character-and-stats/) — 별도의 225 스탯 한계.
- [샤드 요약](/ko/shard/) — 이 서버의 한계와 확장을 한눈에.
- 공략 템플릿: [전사(Warrior)](/ko/templates/warrior/), [메이지(Mage)](/ko/templates/mage/),
  [동물 조련사(Animal Tamer)](/ko/templates/animal-tamer/), [대장장이(Blacksmith)](/ko/templates/blacksmith/),
  [벌목꾼(Lumberjack)](/ko/templates/lumberjack/).
- [모든 스킬](/ko/skills/) — 각 템플릿이 의존하는 정확한 메커니즘을 갖춘 모든 스킬.
