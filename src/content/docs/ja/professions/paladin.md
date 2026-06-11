---
title: パラディン
description: 聖なる戦士 — 騎士道(Chivalry)を献金ポイントで唱えるデクサー。コアスキル、ビルド、戦い方、装備、収入をひとつにまとめて。
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Chivalry/ (PaladinSpell.cs tithing cost; ConsecrateWeapon.cs, EnemyOfOne.cs, DivineFury.cs, CloseWounds.cs, CleanseByFire.cs, HolyLight.cs, DispelEvil.cs, RemoveCurse.cs, SacredJourney.cs)"
last_verified: 2026-06-11
generated: false
---

## このプロフェッションとは

パラディン(Paladin)は、聖なるスペルブックを取り付けた近接戦闘職です。その核はあくまで
[ウォリアー](/ja/professions/warrior/) — 武器、戦術、包帯 — ですが、[騎士道(Chivalry)](/ja/skills/chivalry/)が
自己バフ、軽度の回復、呪い解除、無料の移動を上乗せします。このシャードの騎士道は本物で
(エクスパンション構成に AOS 期のスキルが含まれます)、マナを消費しません。その力は
**献金ポイント(tithing points)**で動きます。

## コアスキル

- [騎士道(Chivalry)](/ja/skills/chivalry/) — 聖なる魔法体系。騎士道が高いほど、呪文効果は強力で確実になり、バフの持続時間も長くなります。
- **武器スキル** — [剣術(Swordsmanship)](/ja/skills/swordsmanship/)、[フェンシング(Fencing)](/ja/skills/fencing/)、または[メイス戦闘(Mace Fighting)](/ja/skills/mace-fighting/)。騎士道は支援役で、敵を倒すのは武器です。
- [戦術(Tactics)](/ja/skills/tactics/)と[解剖学(Anatomy)](/ja/skills/anatomy/) — ウォリアーとまったく同じ2つのダメージ倍率。解剖学は包帯回復の威力も底上げします。
- [治療(Healing)](/ja/skills/healing/) — 包帯は依然として定番の回復手段で、クローズ・ウーンズはそれを補うだけです。
- 任意で[集中(Focus)](/ja/skills/focus/)または[魔法抵抗(Resisting Spells)](/ja/skills/resisting-spells/)を、敵キャスターへの生存力のために。

## マナではなく献金ポイント

騎士道の呪文はマナではなく**献金ポイント**で支払われます。祭壇(shrine)でゴールドを寄付して
獲得します(祭壇を使い、献金を選びます)。詠唱のたびにそのプールからポイントを消費し、空に
なったら再び献金します。これはサーバーエミュレーターで確認済みで — `PaladinSpell.cs` はマナでは
なく `Caster.TithingPoints` を確認・控除します(`servuo: Scripts/Spells/Chivalry/PaladinSpell.cs`)。
数千ゴールドを献金しておけば、バフは常に利用可能です。

## ビルド

ウィキにはまだ**専用のパラディン・テンプレートページ**はありません。騎士道の枠を持つデクサーと
して組みましょう。ステータス、武器スキルの順序、狩りルートは[ウォリアー・テンプレート](/ja/templates/warrior/)から
始め、ユーティリティ枠のひとつを[騎士道(Chivalry)](/ja/skills/chivalry/)に差し替えます。典型的な
最終構成は、武器 + 戦術 + 解剖学 + 治療 + 騎士道 + 受け流し + もうひとつです。7つのスキルを
700ポイント上限内に収める方法については[7x GM テンプレート](/ja/templates/seven-gm/)を参照して
ください。(闇の魔法とライフリーチも欲しいなら、騎士道に死霊術(Necromancy)と武士道(Bushido)を
融合させた[サンパイア](/ja/professions/sampire/)を見てください。)

## プレイの仕方

詠唱体系の中で騎士道がどこに位置するかは[魔法スクール](/ja/playing/magic-schools/)を、詠唱の
仕組みは[呪文詠唱](/ja/playing/spellcasting/)を読んでください。近接の側面については、
[戦闘の基礎](/ja/playing/combat-basics/)に続いて[戦闘応用](/ja/playing/combat-advanced/)が
スイングのループと武器の特殊技を扱い、[治療](/ja/playing/healing/)が包帯のタイミングを扱います。

ループは次の通り。まずゴールドを献金します。戦闘前に**コンセクレート・ウェポン**(自分のダメージ
タイプを対象の最も弱い抵抗に合わせる)と**エネミー・オブ・ワン**(単一の種族に対する大きな
ダメージボーナス — ただし他のすべてから余分にダメージを受けます)を唱えます。**ディヴァイン・
フューリー**は防御と引き換えにスイング速度を上げます。窮地では**クローズ・ウーンズ**が回復し、
**クレンズ・バイ・ファイア** / **リムーブ・カース**が毒と呪いを取り除きます。**ホーリー・ライト**は
範囲攻撃、**ディスペル・イーヴル**は召喚を散らし、**セイクリッド・ジャーニー**はパラディンの
リコールとゲートです。これらはすべて `servuo: Scripts/Spells/Chivalry/` 配下に確認済みのファイル
です。

## 装備

- [武器(Weapons)](/ja/items/weapons/)と[武器カタログ](/ja/items/catalog/weapons/) — 武器スキルに合わせて選びます。デクサーに役立つ修正(ヒットリーチ、スイング速度)は通常通り適用されます。
- [防具(Armor)](/ja/items/armor/) — バランスの取れた抵抗を優先。盾は[受け流し(Parrying)](/ja/skills/parrying/)を可能にします。
- [マジックアイテムプロパティ](/ja/magic/) — ここでは高速詠唱(Faster Casting)はほとんど重要ではない(詠唱が少ない)ため、近接と生存系の修正を優先します。**包帯**を携帯しましょう。

## 生計の立て方

パラディンはウォリアーと同様に稼ぎます。ダンジョンの部屋を一掃し、死体を漁ります。騎士道の
キットは**アンデッドや「悪」のコンテンツ**を特に儲けやすくします — コンセクレートとエネミー・
オブ・ワンが墓地やアンデッドダンジョンを切り裂き、聖なるバフは献金したゴールドしか消費しません。
余った戦利品は[ベンダー&銀行](/ja/playing/vendors-and-banking/)で売りましょう。

## 関連項目

- [ウォリアー](/ja/professions/warrior/) — このビルドが乗るデクサーの基盤
- [サンパイア](/ja/professions/sampire/) — 少しの騎士道も使うリーチ近接ハイブリッド
- [騎士道スキル(Chivalry)](/ja/skills/chivalry/) · [魔法スクール](/ja/playing/magic-schools/)
