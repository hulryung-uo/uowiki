---
title: スペルウィーバー(アルカニスト)
description: アルカニスト — 近くに織り手が多いほどアーケインサークルが強まる、支援とユーティリティのキャスター。スキル、ビルド、戦い方、装備、稼ぎ方。
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Spellweaving/ (ArcaneCircle.cs, ArcaneEmpowerment.cs, GiftOfRenewal.cs, GiftOfLife.cs, Wildfire.cs, WordOfDeath.cs, SummonFey.cs, SummonFiend.cs, NatureFury.cs, Thunderstorm.cs, ReaperForm.cs)"
last_verified: 2026-06-11
generated: false
---

## このプロフェッションとは

スペルウィーバー(Spellweaver、アルカニスト/Arcanist)は、[呪文織り(Spellweaving)](/ja/skills/spellweaving/)を
基盤とした支援とユーティリティのキャスターです。呪文織りはモンディンズ・レガシー時代のスクールです。
このシャードでは呪文織りは実装済みです(EJ 拡張スタックには ML スキルが含まれます)。キャラクターの
唯一のスクールであることはまれで — [メイジ](/ja/professions/mage/)、[ミスティック](/ja/professions/mystic/)、
[テイマー](/ja/professions/tamer/)に重ねて、回復、バフ、召喚、範囲ダメージを加えます。

## コアスキル

- [呪文織り(Spellweaving)](/ja/skills/spellweaving/) — 詠唱スキル。呪文の威力と、保持できるアーケインフォーカスの強さを決めます。
- 軸となる主要スクール — [魔術(Magery)](/ja/skills/magery/) + [知性評価(Evaluating Intelligence)](/ja/skills/evaluating-intelligence/)、[神秘術(Mysticism)](/ja/skills/mysticism/) + [フォーカス(Focus)](/ja/skills/focus/)、または[テイマー](/ja/professions/tamer/)向けのペットスキル。
- 燃料と生存のための[瞑想(Meditation)](/ja/skills/meditation/)と[魔法抵抗(Resisting Spells)](/ja/skills/resisting-spells/)。

## アーケインサークルの仕組み

呪文織りの代名詞は**アーケインサークル(Arcane Circle)**です。その中に立つ(他の織り手が集まる場所で
詠唱する)と、織りの呪文を強化する**アーケインフォーカス(Arcane Focus)**を得られます — そして
**近くにいるスペルウィーバーが多いほどフォーカスは強くなる**ため、グループ向きのスクールです。
*アーケインエンパワーメント(Arcane Empowerment)*は、次の織りの強さ/持続時間をさらに高めます。
どちらも確認済みです: `servuo: Scripts/Spells/Spellweaving/ArcaneCircle.cs` と `ArcaneEmpowerment.cs`。
ソロでも、アイテム(アーケインローブ/ジェム)からフォーカスを得られますが、より弱いものになります。

## ビルド

まだ**専用のスペルウィーバー・テンプレートページはありません**。呪文織りはキャスターに加える1枠と
して扱いましょう。[メイジ・テンプレート](/ja/templates/mage/)(またはテイマー/ミスティックの構成)から
始め、高い知力のキャスターステータスを保ち、[呪文織り(Spellweaving)](/ja/skills/spellweaving/)を
収めます。700 ポイントの計算については[7x GM テンプレート](/ja/templates/seven-gm/)を参照してください。

## プレイの仕方

[魔法スクール](/ja/playing/magic-schools/)は呪文織りを各スクールの中に位置づけ、[呪文詠唱](/ja/playing/spellcasting/)は
詠唱を、[瞑想とマナ](/ja/playing/meditation-and-mana/)はマナを扱います。

ツールキット(すべて `servuo: Scripts/Spells/Spellweaving/` 配下で確認済み):

- **ギフトオブリニューアル(Gift of Renewal)** — 継続回復(heal-over-time)のバフです。**ギフトオブライフ(Gift of Life)**は遅延型の自分/味方の蘇生保険です。
- **アーケインエンパワーメント(Arcane Empowerment)** — 次の織りを強化します。**アチューンウェポン(Attune Weapon)**は受けるダメージを吸収します。
- **サモンフェイ(Summon Fey)** / **サモンフィーンド(Summon Fiend)** — 召喚戦闘の味方です。**ネイチャーズフューリー(Nature's Fury)**は攻撃的な群れを召喚します。
- **ワイルドファイア(Wildfire)** / **サンダーストーム(Thunderstorm)** — 群れを一掃する持続的な範囲ダメージです。
- **ワードオブデス(Word of Death)** — 弱った相手への大ダメージです。
- **リーパーフォーム(Reaper Form)** — 速度と引き換えに呪文の威力を得る自己変身です。

## 装備

- [マジックアイテムの特性](/ja/magic/) — ソロのフォーカスを与える**アーケインローブ/フォーカス**アイテム。加えて呪文用の**Spell Damage**、**Lower Mana Cost**、**Faster Casting**。
- [防具(Armor)](/ja/items/armor/) — メイジ向けでバランスの取れた抵抗値。
- 呪文織りは多くの呪文で、8つのメイジリージェントではなく**アーケインフォーカス**のチャージを使います。フォーカスアイテムを携帯しましょう。

## 生計の立て方

スペルウィーバーが呪文織り単独でソロ狩りをすることはまれです — それはあなたの主スクールやペットが
すでに行うことを増幅します。自分を回復・バフし、群れにワイルドファイアを落とし、ワードオブデスで
仕留めます。グループでは、アーケインサークルが全員の織りを強くします。戦利品は
[ベンダーと銀行](/ja/playing/vendors-and-banking/)を通じて売りましょう。

## 関連項目

- [メイジ](/ja/professions/mage/)と[ミスティック](/ja/professions/mystic/) — 重ねる対象として一般的な主要スクール
- [テイマー](/ja/professions/tamer/) — 呪文織りの回復/召喚をペットと組み合わせます
- [呪文織りスキル](/ja/skills/spellweaving/) · [魔法スクール](/ja/playing/magic-schools/)
