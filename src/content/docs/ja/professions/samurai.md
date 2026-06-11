---
title: サムライ
description: 武士道の剣士 — 規律によって一振りをバーストダメージとカウンター防御に変えるデクサー。スキル、ビルド、戦い方、装備、稼ぎ方。
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Bushido/ (Confidence.cs, Evasion.cs, CounterAttack.cs, LightningStrike.cs, MomentumStrike.cs, HonorableExecution.cs)"
last_verified: 2026-06-11
generated: false
---

## このプロフェッションとは

サムライ(Samurai)は、[武士道(Bushido)](/ja/skills/bushido/)を用いてウォリアーの技を増幅させる
近接戦闘職です。名誉を基盤としたバーストダメージ、反応型の防御、そしてより緻密な武器特殊技の
立ち回りを実現します。このシャードでは武士道は実装済みです(EJ 拡張スタックには
サムライ・エンパイア時代のスキルが含まれます)。本質的には依然として[ウォリアー](/ja/professions/warrior/)
であり — 武士道は味付け、武器が本体です。

## コアスキル

- [武士道(Bushido)](/ja/skills/bushido/) — 規律のスキル。その能力の威力と成功率を決め、両手武器での受け流しを向上させます。
- 武器スキル — 多くは[剣術(Swordsmanship)](/ja/skills/swordsmanship/)(刀、野太刀、両刃刀)ですが、[フェンシング(Fencing)](/ja/skills/fencing/)や[メイス戦闘(Mace Fighting)](/ja/skills/mace-fighting/)でも機能します。
- [戦術(Tactics)](/ja/skills/tactics/)と[解剖学(Anatomy)](/ja/skills/anatomy/) — ダメージ倍率。
- [受け流し(Parrying)](/ja/skills/parrying/) — 武士道と相乗効果を持ちます。サムライは両手武器でも効果的に受け流せます。
- 包帯用の[治療(Healing)](/ja/skills/healing/)、任意で[魔法抵抗(Resisting Spells)](/ja/skills/resisting-spells/)。

## ビルド

まだ**専用のサムライ・テンプレートページはありません**。武士道枠を持つデクサーとして組みましょう。
ステータス、武器の習得順序、狩りルートについては[ウォリアー・テンプレート](/ja/templates/warrior/)から
始め、そこに[武士道(Bushido)](/ja/skills/bushido/)を加えます。よくある構成は、武器 + 戦術 + 解剖学 +
武士道 + 受け流し + 治療 + もうひとつです。700 ポイントの計算については[7x GM テンプレート](/ja/templates/seven-gm/)を
参照してください。武士道は[サンパイア](/ja/professions/sampire/)の柱でもあります。

## プレイの仕方

[戦闘の基礎](/ja/playing/combat-basics/)はスイングのループを解説し、[戦闘応用](/ja/playing/combat-advanced/)は
武器特殊技と速度を扱います — 武士道はそれらを軸に組まれているため、これは必須です。
[魔法スクール](/ja/playing/magic-schools/)は武士道を各スクールの中に位置づけます。

ツールキット(すべて `servuo: Scripts/Spells/Bushido/` 配下で確認済み):

- **名誉(Honorable Execution)** — ターゲットに名誉を捧げ、ダメージ/回復の見返りを得ます。大きな戦いの口火を切る一手です。
- **コンフィデンス(Confidence)** — 受け流しの成功に報いる防御的な継続回復(heal-over-time)です。
- **イベイジョン(Evasion)** — ブロック性能が大幅に向上する短い時間枠です。
- **カウンターアタック(Counter Attack)** — 受け流したときに自動で反撃します。
- **ライトニングストライク(Lightning Strike)** — 速くて安価な特殊技で、次の一撃の命中率/クリティカルを高めます。
- **モメンタムストライク(Momentum Strike)** — ターゲットとその周囲にも当たります。集団戦と相性が良いです。

これらは武器自体の一次/二次特殊技の上に重なります — 武器の項目を読み、武士道の能力と連携させましょう。

## 装備

- [武器(Weapons)](/ja/items/weapons/)と[武器カタログ](/ja/items/catalog/weapons/) — 両手の剣術武器(野太刀)は武士道の受け流し相乗効果に合います。リーチとスイング速度のモッドを選びましょう。
- [防具(Armor)](/ja/items/armor/) — バランスの取れた抵抗値。両手受け流しのおかげで盾は任意です。
- [マジックアイテムの特性](/ja/magic/) — Hit Lower Defense、Hit Leech、Swing Speed Increase がサムライに映えます。**包帯**を携帯しましょう。

## 生計の立て方

サムライは他のデクサーと同様にダンジョンで稼ぎますが、武士道によって単体相手のバースト
(名誉 + ライトニングストライク)と集団制御(モメンタムストライク)が向上します。部屋を一掃し、
死体を漁り、余剰は[ベンダーと銀行](/ja/playing/vendors-and-banking/)を通じて売りましょう。

## 関連項目

- [ウォリアー](/ja/professions/warrior/) — デクサーの基盤
- [サンパイア](/ja/professions/sampire/) — 武士道 + 降霊術リーチのハイブリッド
- [ニンジャ](/ja/professions/ninja/) — もうひとつのトクノの規律。ステルスを基盤とします
- [武士道スキル](/ja/skills/bushido/) · [戦闘応用](/ja/playing/combat-advanced/)
