---
title: サンパイア
description: 伝説のハイブリッド — 一撃ごとに生命を吸収し(ヴァンパイリックエンブレイス)、武士道で群れをなぎ払う近接キャラクター。名高いソロ PvM のモンスター狩り。
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Necromancy/VampiricEmbrace.cs; Scripts/Spells/Bushido/ (HonorableExecution.cs, LightningStrike.cs, MomentumStrike.cs, Confidence.cs); Scripts/Spells/Chivalry/ (ConsecrateWeapon.cs, EnemyOfOne.cs)"
last_verified: 2026-06-11
generated: false
---

## このプロフェッションとは

サンパイア(Sampire、「サムライ + ヴァンパイア」)は、Ultima Online で最も名高い PvM テンプレートです。
**一撃ごとに生命を吸収する**近接キャラクターであり、通常のデクサーなら踏み潰されるモンスターの群れを
意に介しません。このシャードでは構成要素はすべて実装済みです(EJ 拡張スタックには AOS、SE、ML
スキルが含まれます)。これは独自のスキルではなく融合ビルドであり — 3つのスクールを組み合わせます。

- [降霊術(Necromancy)](/ja/professions/necromancer/) → **ヴァンパイリックエンブレイス(Vampiric Embrace)**(生命吸収のフォーム)
- [武士道(Bushido)](/ja/professions/samurai/) → 名誉、ライトニングストライク、そして武器のワールウィンド相乗効果
- 少量の[騎士道(Chivalry)](/ja/professions/paladin/) → コンセクレイトウェポンとエネミーオブワン

## コアスキル

- [降霊術(Necromancy)](/ja/skills/necromancy/) — このビルドを定義する吸収フォーム、**ヴァンパイリックエンブレイス**を唱えるのにちょうど足りるだけ(必要なスキルは控えめ)。
- [武士道(Bushido)](/ja/skills/bushido/) — **名誉(Honorable Execution)**、**ライトニングストライク**、**コンフィデンス**、そして両手武器での受け流し向上のため。
- [騎士道(Chivalry)](/ja/skills/chivalry/) — **コンセクレイトウェポン(Consecrate Weapon)**(相手の最も低い抵抗を突く)と**エネミーオブワン(Enemy of One)**(単一タイプへの大ダメージ)のための小さな投資。ティッシングポイントで支払います([パラディン](/ja/professions/paladin/)を参照)。
- 武器スキル — 多くは[剣術(Swordsmanship)](/ja/skills/swordsmanship/)(**ワールウィンド**特殊技と内蔵リーチを持つ両手武器)。
- [戦術(Tactics)](/ja/skills/tactics/)と[解剖学(Anatomy)](/ja/skills/anatomy/) — ダメージ倍率。必須です。
- [受け流し(Parrying)](/ja/skills/parrying/)はよく採用されます。リーチが包帯の代わりになるため、[治療(Healing)](/ja/skills/healing/)は任意です。

## ビルド

まだ**専用のサンパイア・テンプレートページはありません**。3つのスクールから借りるデクサーとして
組みましょう。武器 + 戦術 + 解剖学の核については[ウォリアー・テンプレート](/ja/templates/warrior/)から
始め、その周りに降霊術、武士道、少量の騎士道を収めます。これは厳しい収まり具合です —
700 ポイントの予算については[7x GM テンプレート](/ja/templates/seven-gm/)を参照してください。
サンパイアは多くの場合、降霊術と騎士道を GM 未満(主要呪文に必要な分だけ)で運用し、
戦闘の核にポイントを回します。

## プレイの仕方 — ループ

特殊技と武器速度については[戦闘応用](/ja/playing/combat-advanced/)を読みましょう。このビルドは
それらに生死を懸けています。代名詞的なループはこうです。

1. **ヴァンパイリックエンブレイス**を有効化(唱えてフォームを維持) — これで一撃ごとに回復します。
2. 手強い相手を**名誉(Honor)**で名誉付け(武士道)し、交戦前に**コンセクレイトウェポン** + **エネミーオブワン**(騎士道)を行います。
3. 群れへ**ワールウィンド** — 多数の敵を同時に当てるということは、多くの生命吸収が同時に起こるということです。つまり群れはあなたを傷つける速さより速く*回復させて*くれます。
4. 重要な一撃の命中のために**ライトニングストライク**を散りばめ、集中攻撃を受けたときは**コンフィデンス**/**イベイジョン**と受け流しに頼ります。

吸収は当てている対象の数に応じてスケールするため、サンパイアはモンスターの群れに対してソロでほぼ
無敵です — これが、定番の PvM ファーマーとして名高い理由です。(仕組みは確認済み:
`servuo: Scripts/Spells/Necromancy/VampiricEmbrace.cs`、武士道のファイル群、そして
`Scripts/Spells/Chivalry/ConsecrateWeapon.cs` / `EnemyOfOne.cs`。)

## 装備

- [武器(Weapons)](/ja/items/weapons/)と[武器カタログ](/ja/items/catalog/weapons/) — **ワールウィンド**特殊技と**Hit Life Leech**を持つ両手武器。多くのプレイヤーは野太刀やダブルアックスを好みます。
- [マジックアイテムの特性](/ja/magic/) — **Hit Life Leech**、**Hit Lower Defense**、**Swing Speed Increase**、**スタミナ/マナ**の持続力、そして抵抗キャップを積み重ねます。Faster Casting は数少ないバフ詠唱にしか役立ちません。
- [防具(Armor)](/ja/items/armor/) — ヴァンパイリックエンブレイスには既知の属性弱点があるため、それがさらす抵抗をキャップで埋めましょう。

## 生計の立て方

サンパイアは最高の**ソロ PvM ファーマー**です。他のソロテンプレートでは生き残れない高ティアの
ダンジョンの群れやボスを一掃し、すべてを略奪します。騎士道用に金貨をティッシングし、フォームの
再詠唱用に降霊術のリージェントを切らさず、戦果は[ベンダーと銀行](/ja/playing/vendors-and-banking/)を
通じて売りましょう。

## 関連項目

- [ネクロマンサー](/ja/professions/necromancer/) · [サムライ](/ja/professions/samurai/) · [パラディン](/ja/professions/paladin/) — 融合する3つのスクール
- [ウォリアー](/ja/professions/warrior/) — デクサーの基盤
- [戦闘応用](/ja/playing/combat-advanced/) · [7x GM テンプレート](/ja/templates/seven-gm/)
