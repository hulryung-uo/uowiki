---
title: UO 拡張（Expansions）
description: Ultima Online のすべての拡張の年代記 —— 各拡張が追加した土地、種族、スキル、システム —— と、Endless Journey ルールセットで動くこのシャードへの対応。
status: unverified
sources:
  - "general Ultima Online history; ultimaonline.fandom.com"
  - "servuo: Config/Expansion.cfg, Server/ExpansionInfo.cs"
last_verified: 2026-06-12
generated: false
---

Ultima Online は二十年以上にわたって拡張されてきた。各**拡張（expansion）**は、既存のゲームに新しいコンテンツを
ボルト留めする名前付きのリリースだ —— 新たな土地と*ファセット（facet、並行マップ）*、新たなプレイ可能**種族**、
新たな**スキル**と魔法体系、そして新たな**システム**（戦闘計算、クラフト、住居、航海）。**時代（era）**とは、
ある拡張が定義する期間だ。何かが「AOS 時代の」ものだと言うとき、それは *Age of Shadows* とともに登場した、
あるいはそれによって作り変えられたという意味である。

これは文書化において重要だ。UO は累積的だからである。サーバーは機能をアラカルトで選ぶのではない。単一の拡張
レベルを宣言し、それを含むそこまでのすべてを継承する。**このシャードは Endless Journey（EJ）で動く** ——
サーバーエミュレーターにおける最新のレベル —— ので、以下の*すべての*拡張がここに存在する。ロストランド、
すべてのファセット、あらゆる種族と魔法体系、カスタム住居、航海、Eodon —— すべて稼働中だ。（`Config/Expansion.cfg`
を参照: `CurrentExpansion=EJ`。）

拡張のリストと順序は、サーバーの拡張 enum（`Server/ExpansionInfo.cs`）からそのまま来ている: None → T2A → UOR →
UOTD → LBR → AOS → SE → ML → SA → HS → TOL → EJ。それぞれの目玉となる追加要素を以下に示す。

## タイムライン

| Expansion | Year | Headline additions |
|-----------|------|---------------------|
| Launch | 1997 | 元祖ブリタニア（Felucca マップ） |
| The Second Age (T2A) | 1998 | ロストランド；最初の大規模な土地拡張 |
| Renaissance (UOR) | 2000 | Trammel/Felucca のファセット分割；合意制 vs オープン PvP |
| Third Dawn (UOTD) | 2001 | Ilshenar ファセット；初の 3D クライアント |
| Lord Blackthorn's Revenge (LBR) | 2002 | 世界中の新しいアートとクリーチャー |
| Age of Shadows (AOS) | 2003 | Malas；抵抗値；アイテム特性＋保険；Necromancy、Chivalry；カスタム住居 |
| Samurai Empire (SE) | 2004 | Tokuno 諸島；Bushido、Ninjitsu；サムライとニンジャ |
| Mondain's Legacy (ML) | 2005 | エルフ；Spellweaving；Heartwood；ピアレスボス |
| Stygian Abyss (SA) | 2009 | ガーゴイル；Ter Mur；Mysticism、Imbuing、Throwing；Abyss |
| High Seas (HS) | 2010 | 船と海戦；釣りの刷新 |
| Time of Legends (TOL) | 2015 | Valley of Eodon；Myrmidex；スキルマスタリー |
| Endless Journey (EJ) | 2018 | 無料アクセス層 —— **このシャードが動かすルールセット** |

## Launch（1997）

Ultima Online は単一の土地で出荷された: **ブリタニア（Britannia）**、後に **Felucca** として知られるマップだ。
ファセットはなく、第二のマップもなく、世界は単一のオープンなルールセットだった —— 誰でも、どこでも、誰でも
攻撃できた。続くすべては、この元祖の世界の上に築かれている。

## The Second Age（T2A、1998）

最初の大規模な土地拡張。T2A は**ロストランド（Lost Lands）**を追加した —— 洞窟の通路とダンジョンを通じて
到達する広大な屋外地域で、新たな町、地形、クリーチャーを伴い、探索可能な地表をおよそ倍にした。より手強い
モンスターと、あのフロンティアの象徴的なダンジョンももたらした。

このシャードではロストランドは完全に存在する。そのフロンティアの町のうち二つが我々のワールドセクションで
文書化されている: **Delucia** と **Papua**。

- [ワールドアトラス](/ja/world/) · [Delucia](/ja/world/delucia/) · [Papua](/ja/world/papua/)

## Renaissance（UOR、2000）

Renaissance は地理よりも*社会的な*ゲームを作り変えた。世界を二つの並行**ファセット**に分割した:
**Trammel**、プレイヤーが同意なしに互いを傷つけられない場所と、**Felucca**、元祖のオープン PvP・全ロストの
ルールセットを保った場所だ。同じ都市が両方に存在するが、交戦のルールが異なる。この「Tram/Fel」の分断は、
PvP と悪名がどう機能するかへの最も重大な変更であり、今日に至るまでゲームに残り続けている。

- [悪名と PvP](/ja/playing/notoriety-and-pvp/)

## Third Dawn（UOTD、2001）

Third Dawn は **Ilshenar** ファセットを導入した —— プレイヤー住居もなく、他のマップへのムーンゲートの接続も
ない、伝承の豊かな大きな陸塊で、ガーゴイルとオフィディアンをテーマにしている。もう一つの目玉は技術的なものだった:
UO 初の **3D クライアント**、古典的な 2D クライアントと並ぶ代替レンダラーだ。

## Lord Blackthorn's Revenge（LBR、2002）

LBR は地理が軽めで、演出が重めだった。ゲームの**アートとクリーチャー**の大部分を刷新し —— 多くのモンスター
スプライトが描き直された —— 堕落した Lord Blackthorn をめぐるストーリーラインを織り込んだ。前年に導入された
新しい 3D アセットへのクライアントのサポートも強化した。

## Age of Shadows（AOS、2003）

大物だ。*Age of Shadows* は、それ以前のどの拡張よりも装備と戦闘のルールを書き換えた。その追加要素:

- **Malas** —— 新たなファセットで、Luna、Umbra の街、そして Doom ダンジョンの本拠地。
- **抵抗システム**: 防具はもはや単一の Armor Rating を使わず、五つの個別の抵抗値を使う —— 物理、炎、冷気、毒、
  エネルギー —— それぞれ 70 が上限。ダメージタイプが重要になり、五つのバランスを取るようにスーツを組む。
- **アイテム特性と強度**: 魔法装備が数十の積み重ね可能な特性を得た（Faster Casting、Hit Chance Increase、
  Damage Increase、Lower Reagent Cost など）、戦利品とクラフトをミニマックスのゲームに変えた。
- **アイテム保険**、死がもはや装備したスーツを失うことを意味しなくなった。
- **カスタム住居** —— ゲーム内の家のデザイナー、プレイヤーが固定された証書から選ぶ代わりに自分の間取りを
  描けるようにした。
- 二つの新たな魔法体系と、それに基づくテンプレート: **Necromancy**（ネクロマンサー）と **Chivalry**
  （パラディン）。

- [ネクロマンサー](/ja/professions/necromancer/) · [パラディン](/ja/professions/paladin/)
- [防具と抵抗値](/ja/items/armor/) · [家のタイプ](/ja/playing/house-types/)

## Samurai Empire（SE、2004）

**Tokuno 諸島**を中心とするアジア風の拡張で、独自の町、ダンジョン、装飾様式を持つ三島のファセットだ。二つの
スキルと、それを中心に組まれたクラスを追加した: **Bushido**（サムライ、構えの能力を持つ近接／受け流しの
ウォリアー）と **Ninjitsu**（ニンジャ、ステルス、動物変化、分身を持つ）。

- [サムライ](/ja/professions/samurai/) · [ニンジャ](/ja/professions/ninja/)

## Mondain's Legacy（ML、2005）

Mondain's Legacy はローンチ以来初の新たな**プレイ可能種族** —— **エルフ** —— を、独自の開始ステータスと種族
特性とともに追加した。その他の柱:

- **Spellweaving**、グループで唱えると威力がスケールする秘術の体系、プラスそれに基づく Arcanist テンプレート。
- **Heartwood**、森に隠されたエルフの集落で、独自のクエスト駆動のクラフト報酬を持つ。
- **ピアレスボス（Peerless bosses）** —— インスタンス化された鍵で制限される遭遇（Travesty、Dreadhorn、
  Lady Melisande など）で、終盤の戦いのテンプレートになった。
- *Imbuing* が後に形式化することになる、資源と特性のクラフトへの初期の地ならし。

- [スペルウィーバー](/ja/professions/spellweaver/) · [Spellweaving スキル](/ja/skills/spellweaving/)

## Stygian Abyss（SA、2009）

Stygian Abyss は二つ目の新種族 —— 飛行できる**ガーゴイル** —— と、**Ter Mur** ファセット、ガーゴイルの故郷で
偉大な **Stygian Abyss** ダンジョンそのものを通じて到達する場所を追加した。三つのスキルを一度にもたらした:

- **Mysticism**、秘術／神聖のハイブリッド体系（ミスティック）。
- **Imbuing**、制御された強度でアイテムに魔法特性を組み込めるクラフトスキル —— ML の地ならしの形式化。
- **Throwing**、ガーゴイル専用の遠距離戦闘スキル。

- [ミスティック](/ja/professions/mystic/) · [Mysticism](/ja/skills/mysticism/)
- [Imbuing](/ja/skills/imbuing/) · [Throwing](/ja/skills/throwing/)

## High Seas（HS、2010）

High Seas は海を重要なものにした。完全な**航海と海戦**システムを追加し —— 大砲を備えた複数タイルの船、船対船の
戦い、マーフォークや Corgul ボスのような海の敵 —— そして**釣り**を、新たな獲物、大魚、ボトルメール（message-in-a-bottle）の
宝を伴うより奥深い職業へと刷新した。

- [漁師](/ja/professions/fisher/) · [トレジャーハンティング](/ja/playing/treasure-hunting/)（ボトルメール／SOS）

## Time of Legends（TOL、2015）

Time of Legends は **Valley of Eodon** を開いた —— 恐竜、昆虫型の **Myrmidex**、そして Zhah 族と Sakkhra 族の
いる先史時代のジャングルの土地だ。そのシステム的な追加は**スキルマスタリー** —— スキルごとのマスタリー能力で、
熟練したキャラクターに新たな特化の層と能動的な力を与える。

## Endless Journey（EJ、2018）

Endless Journey はコンテンツの追加というより**アクセス層**だ: アカウントがアクティブなサブスクリプションなしに
ログインしてゲームの広い範囲を遊べる無料プレイのルールセットで、ストレージと最新コンテンツにいくらかの制限が
ある。サーバーエミュレーターにおいて EJ は**最高の拡張レベル**であり、つまりその上のすべての拡張の完全な
コンテンツスタックを継承する。

**これが我々のシャードが動かすルールセットだ。** この wiki の他の場所で、あるスキル、呪文、アイテムがここに
存在すると読んだなら、それは EJ がその下の歴史全体を引き継いでいるからだ。

- [我々のシャード](/ja/shard/)

## これが我々のシャードにとって意味すること

シャードが **EJ** で動くので、この歴史のどれも仮定の話ではない —— すべてあなたが立っている地面だ。あらゆる
ファセット（Felucca、Trammel、Ilshenar、Malas、Tokuno、Ter Mur、Eodon）、追加の両種族（エルフ、ガーゴイル）、
あらゆる魔法体系（Necromancy、Chivalry、Bushido、Ninjitsu、Spellweaving、Mysticism）、そしてあらゆるシステム
（抵抗値、アイテム特性、保険、カスタム住居、航海、imbuing、マスタリー）が、ここのキャラクターに利用可能だ。

それがまた、この wiki 全体のページがコンテンツを**時代（era）**でタグ付けする理由でもある。アイテムとクラフトの
カタログは、各素材、アイテム、レシピがいつ導入されたかを記す —— それらのタグはこのページの歴史からそのまま来て
いるので、何かがローンチ時代の定番か、後の拡張で登場したかを一目で見分けられる。アイテムごとの時代タグは
[アイテムカタログ](/ja/items/)を、この EJ の基準線の上に乗る上限値、レート、ハウスルールは
[シャードページ](/ja/shard/)を参照してほしい。
