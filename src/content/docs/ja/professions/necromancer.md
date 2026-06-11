---
title: ネクロマンサー
description: 闇のキャスター — 特殊リージェントと降霊術(Spirit Speak)を燃料に、呪い、アンデッド召喚、自己変身を操る。スキル、ビルド、プレイ、装備、収入。
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Necromancy/ (WraithForm.cs, LichForm.cs, HorrificBeast.cs, VampiricEmbrace.cs, CorpseSkin.cs, BloodOath.cs, AnimateDeadSpell.cs, SummonFamiliar.cs, Strangle.cs, PainSpike.cs, Wither.cs); special reagent use confirmed in spell files"
last_verified: 2026-06-11
generated: false
---

## このプロフェッションとは

ネクロマンサー(Necromancer)は闇のキャスターです。敵を呪い、死者を起こして従え、戦闘上の
優位のために自らの肉体を変身させます。このシャードの死霊術(Necromancy)は本物で(EJ
エクスパンション構成には Age of Shadows 期のスキルが含まれます)。メイジ(ユーティリティ用の
[魔術(Magery)](/ja/skills/magery/))や、武器と武士道(Bushido)と自然に組み合わさります —
後者があの有名な[サンパイア](/ja/professions/sampire/)です。

## コアスキル

- [死霊術(Necromancy)](/ja/skills/necromancy/) — 詠唱スキル。呪文の威力、成功率、そして使える呪文を決めます。
- [降霊術(Spirit Speak)](/ja/skills/spirit-speak/) — 死霊術の効果を高め、**さらに**近くの死体から生命を吸って自己回復できます。降霊術なしのネクロマンサーは威力が半減します。
- 二次スキル:フルキャスターなら[魔術(Magery)](/ja/skills/magery/) + [知力評価(Evaluating Intelligence)](/ja/skills/evaluating-intelligence/)、**または**デクサーハイブリッドなら武器スキル([剣術(Swordsmanship)](/ja/skills/swordsmanship/)など) + [戦術(Tactics)](/ja/skills/tactics/)/[解剖学(Anatomy)](/ja/skills/anatomy/)。
- [瞑想(Meditation)](/ja/skills/meditation/)(キャスタービルド)と[魔法抵抗(Resisting Spells)](/ja/skills/resisting-spells/)が仕上げです。

## 8種ではなく特殊リージェント

死霊術はメイジの8種のリージェントを**使いません**。独自のセットを消費します — **バットウィング、
グレイブダスト、ディーモンブラッド、ノックスクリスタル、ピッグアイアン**。メイジ/リージェント
ベンダーから買い、深い在庫を保ちましょう — 各呪文がそれぞれの組み合わせを指定します。
(`servuo: Scripts/Spells/Necromancy/` 配下の呪文ファイルで確認済み。)詠唱にはリージェントに
加え、献金ではなくマナを支払います。

## ビルド

専用のネクロマンサー・テンプレートページはまだ**ありません**。キャスターネクロには、
[メイジ・テンプレート](/ja/templates/mage/)から始め、魔術 + 知力評価 + 瞑想 + 魔法抵抗とともに
死霊術 + 降霊術を組み込みます。近接ネクロには、[ウォリアー・テンプレート](/ja/templates/warrior/)から
始め、武器の核の周りに死霊術 + 降霊術を収めます。いずれにせよ、すべてを700ポイント上限内へ
押し込む方法については[7x GM テンプレート](/ja/templates/seven-gm/)を参照してください。

## プレイの仕方

詠唱モデルについては[魔法スクール](/ja/playing/magic-schools/)と[呪文詠唱](/ja/playing/spellcasting/)を、
マナ回復については[瞑想とマナ](/ja/playing/meditation-and-mana/)を読んでください。近接ハイブリッドは
[戦闘応用](/ja/playing/combat-advanced/)も読むべきです。

ツールキット(すべて `servuo: Scripts/Spells/Necromancy/` 配下で確認済み):

- **変身** — *レイス・フォーム*(マナリーチ、レイスの肉体)、*リッチ・フォーム*(マナ回復、火への弱点)、*ホリフィック・ビースト*(近接向けの肉体)。*ヴァンピリック・エンブレイス*は**一撃ごとにライフリーチ**を与え — サンパイアの礎です。
- **呪い** — *コープス・スキン*、*ブラッド・オース*、*ストラングル*、*ペイン・スパイク*、*ウィザー*(範囲)が対象を弱体化させ、出血させます。
- **アンデッド** — *アニメイト・デッド*は死体を起こして従者にし、*サモン・ファミリア*は専用ペットを与えます。
- **回復** — 戦いの合間に[降霊術(Spirit Speak)](/ja/skills/spirit-speak/)で死体から生命を吸い取ります。

## 装備

- [マジックアイテムプロパティ](/ja/magic/) — キャスターネクロは**ロウワー・リージェント・コスト**、**ロウワー・マナ・コスト**、**スペル・ダメージ・インクリース**、**高速詠唱(Faster Casting)**を求め、近接ネクロは代わりにヒットリーチとスイング速度を求めます。
- [防具(Armor)](/ja/items/armor/) — バランスの取れた抵抗。一部の変身は外見とステータスを上書きします。
- ハイブリッドビルド向けの[武器(Weapons)](/ja/items/weapons/)。5種の特殊リージェントを一式携帯しましょう。

## 生計の立て方

ネクロマンサーはダンジョンをソロで稼ぎます。対象を呪って撃ち、残した死体から回復し、死体を
漁ります。アンデッドの多い高ティアのコンテンツは、この呪いキットによく報いてくれます。余りは
[ベンダー&銀行](/ja/playing/vendors-and-banking/)で売りましょう。

## 関連項目

- [サンパイア](/ja/professions/sampire/) — 死霊術 + 武士道の近接リーチビルド
- [メイジ](/ja/professions/mage/) — 詠唱ネクロが借りるキャスターの基盤
- [死霊術スキル(Necromancy)](/ja/skills/necromancy/) · [降霊術(Spirit Speak)](/ja/skills/spirit-speak/) · [魔法スクール](/ja/playing/magic-schools/)
