---
title: ミスティック
description: 神秘術のキャスター — フォーカスまたはインビューイングで威力を発揮する、強烈な属性ダメージとデバフのスクール。スキル、ビルド、戦い方、装備、稼ぎ方。
status: unverified
sources:
  - "wiki cross-references; general UO play"
  - "servuo: Scripts/Spells/Mysticism/ (MysticSpell.cs power-skill = max(Imbuing, Focus); SpellDefinitions/: NetherBoltSpell.cs, EagleStrikeSpell.cs, SpellPlague.cs, CleansingWindsSpell.cs, RisingColossusSpell.cs, HealingStoneSpell.cs, NetherCycloneSpell.cs, StoneForm.cs)"
last_verified: 2026-06-11
generated: false
---

## このプロフェッションとは

ミスティック(Mystic)は[神秘術(Mysticism)](/ja/skills/mysticism/)を基盤としたキャスターです。
神秘術はスティジアン・アビス時代のスクールで、属性ダメージ、デバフ、回復、そして強力な召喚を
扱います。このシャードでは神秘術は実装済みです(EJ 拡張スタックには SA スキルが含まれます)。
単独でも強力なキャスターであり、[魔術(Magery)](/ja/skills/magery/)や
[呪文織り(Spellweaving)](/ja/skills/spellweaving/)と組み合わせて複数スクールのキャスターにも
よく合います。

## コアスキル

- [神秘術(Mysticism)](/ja/skills/mysticism/) — 詠唱スキル。使える呪文と基礎成功率を決めます。
- [フォーカス(Focus)](/ja/skills/focus/) **またはインビューイング(Imbuing)** — 神秘術のダメージと効果の強さをスケールさせる**パワースキル**です。サーバーエミュレーターは高い方を採用します。`MysticSpell.cs` は `max(Imbuing, Focus)` を取ります(`servuo: Scripts/Spells/Mysticism/MysticSpell.cs`)。フォーカスは軽い選択肢で、インビューイングはクラフトスキルも兼ねます。
- 第二の詠唱スクール — [魔術(Magery)](/ja/skills/magery/) + [知性評価(Evaluating Intelligence)](/ja/skills/evaluating-intelligence/)、または[呪文織り(Spellweaving)](/ja/skills/spellweaving/)。
- 燃料と生存のための[瞑想(Meditation)](/ja/skills/meditation/)と[魔法抵抗(Resisting Spells)](/ja/skills/resisting-spells/)。

## リージェント

神秘術の呪文はリージェント(メイジ系・降霊術系といくつか共有します)とマナを消費します。
リージェントポーチは在庫を切らさないようにしましょう。ただし詠唱の威力は依然としてリージェントでは
なくフォーカス/インビューイングから来ます。

## ビルド

まだ**専用のミスティック・テンプレートページはありません**。[メイジ・テンプレート](/ja/templates/mage/)から
組みましょう。キャスターのステータス配分(高い知力、潤沢なマナ)を保ち、スクール枠を神秘術 +
フォーカス(またはインビューイング)に入れ替え、それと並べて魔術/評価 + 瞑想 + 抵抗を配置します。
700 ポイント上限内への収め方については[7x GM テンプレート](/ja/templates/seven-gm/)を参照してください。

## プレイの仕方

[魔法スクール](/ja/playing/magic-schools/)は神秘術を各スクールの中に位置づけ、[呪文詠唱](/ja/playing/spellcasting/)は
詠唱の仕組みを、[瞑想とマナ](/ja/playing/meditation-and-mana/)は回復を扱います。

ツールキット(すべて `servuo: Scripts/Spells/Mysticism/SpellDefinitions/` 配下で確認済み):

- **ネザーボルト(Nether Bolt)** / **イーグルストライク(Eagle Strike)** — 信頼できる単体ダメージの直接攻撃です。
- **スペルプレイグ(Spell Plague)** — ターゲットが打撃を受け続けると追加ダメージを爆発させるデバフです。
- **クレンジングウィンズ(Cleansing Winds)** — 範囲回復と解毒です。
- **ヒーリングストーン(Healing Stone)** — 自分で生み出して携帯する自己回復アイテムです。
- **ライジングコロッサス(Rising Colossus)** — 強力な召喚戦闘の味方です。**ストーンフォーム(Stone Form)**は防御的な自己変身です。
- **ネザーサイクロン(Nether Cyclone)** / **ヘイルストーム(Hail Storm)** — 群れを一掃する範囲攻撃です。

## 装備

- [マジックアイテムの特性](/ja/magic/) — **Spell Damage Increase**、**Lower Mana Cost**、**Lower Reagent Cost**、**Faster Casting** を優先しましょう。可能なら神秘術のフォーカス/詠唱モッドも。
- [防具(Armor)](/ja/items/armor/) — メイジ向け(瞑想ペナルティなし)でバランスの取れた抵抗値。
- 十分な**リージェント**の在庫と、そのスクール用の[呪文書](/ja/items/)を持ちましょう。

## 生計の立て方

ミスティックはキャスターとしてダンジョンで稼ぎます。デバフ(スペルプレイグ)で口火を切り、
ネザーボルト/イーグルストライクで攻撃し、手強い相手にはライジングコロッサスを出し、
クレンジングウィンズ/ヒーリングストーンで回復します。強力な範囲呪文は群れの一掃を利益にします。
戦利品は[ベンダーと銀行](/ja/playing/vendors-and-banking/)を通じて売りましょう。

## 関連項目

- [メイジ](/ja/professions/mage/) — このビルドが借りるキャスターの基盤
- [スペルウィーバー](/ja/professions/spellweaver/) — 組み合わせる相補的な支援スクール
- [神秘術スキル](/ja/skills/mysticism/) · [フォーカス(Focus)](/ja/skills/focus/) · [魔法スクール](/ja/playing/magic-schools/)
