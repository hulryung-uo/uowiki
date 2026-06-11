---
title: 遊び方 — トレジャーハンティング
description: このシャードでのトレジャーハンターのプレイスタイル — トレジャーマップを見つけるか買い、地図作製で解読し、採掘で宝箱を掘り出し、守護者と戦い、罠付きの宝箱を解錠してゴールド、宝石、魔法装備、パワースクロール、特殊スクロールを得る。5つのForgotten-Treasuresマップレベル（Stash、Supply、Cache、Hoard、Trove）、5つの戦利品パッケージ、関わるスキル、そして宝箱が埋まっている場所を扱う。
status: source-verified
sources:
  - "servuo: Scripts/Services/TreasureMaps/TreasureMap.cs (decode, dig, dig range, guardians, spawn tables, location randomization)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapInfo.cs (levels, packages, decode difficulty, chest skills, loot tables)"
  - "servuo: Scripts/Services/TreasureMaps/TreasureMapChest.cs (chest, trap, artifacts)"
  - "servuo: Scripts/Items/Tools/MapItem.cs (decoded-map gump 0x139D)"
  - "servuo: Config/TreasureMaps.cfg (Enabled=True, LootChance=.01, ResetTime=30.0)"
  - "servuo: Config/Expansion.cfg (CurrentExpansion=EJ -> modern system live)"
  - "servuo: Data/treasure.cfg (193 classic dig sites)"
  - "client art: gumpartLegacyMUL.uop gump 0x139D (map-window parchment)"
last_verified: 2026-06-11
generated: false
---

**トレジャーハンティング**は探検家の職業です：トレジャーマップを入手し、それを解読して宝箱が
埋まっている場所を明らかにし、その地点へ旅し、掘り出し、地面から噴き出すモンスターと戦い、
それから宝箱を解錠して罠を解除し、戦利品を得ます。バランスの取れたキャラクターに報い、ゴールド、
宝石、魔法装備、そして — 最上位の階層では — パワースクロールと特殊スキルスクロールで支払います。

> **ここで動いているシステム。** このシャードは拡張**EJ**を動かしており
> （`Config/Expansion.cfg` → `CurrentExpansion=EJ`）、`TreasureMapInfo.NewSystem`が
> **true**で、現代の**Forgotten Treasures**トレジャーマップシステムが有効です。マップには
> 5つのレベル**Stash、Supply、Cache、Hoard、Trove**と戦利品**パッケージ**があり、古い
> 「レベル1〜7」の番号付けではありません。このページの数字と表はEJのコード経路に対して
> ソース検証済みです。

## トレジャーハンティングとは

完全な流れを順に：

1. **マップを入手する。** トレジャーマップはモンスターから落ちる（下記参照）か、他のプレイヤー
   から購入／取引します。
2. **解読する。** マップをダブルクリックします。[地図作製（Cartography）](/ja/skills/cartography/)の
   スキルチェックがそれを解読し、赤いピンで掘削地点を記します
   （`TreasureMap.Decode`、`DisplayTo`）。
3. **地点へ旅する。** 解読されたマップは小さな地域の眺めを示します。あなたはその現実世界の場所へ
   航海するか騎乗します。
4. **掘る。** 掘削ツール（[採掘（Mining）](/ja/skills/mining/)ツール）を持ってピンの近くに立ち、
   掘ります。スキルがどれだけ近づく必要があるかを決めます（`DigTarget`）。
5. **守護者と戦う。** 掘削を終えると、マップレベルに応じてスケールされた4体のモンスターが沸きます
   （`DigTimer`）。生き延びてください。
6. **宝箱を開ける。** 宝箱は**施錠され罠が仕掛けられています** — [開錠（Lockpicking）](/ja/skills/lockpicking/)
   でロックを開け、[トラップ解除（Remove Trap）](/ja/skills/remove-trap/)で罠を解除し（または爆発を
   覚悟し）、それから略奪します。

人々がトレジャーハントをするのは見返りのためです：宝箱1つあたり数万ゴールド、宝石の袋、
ランダムに魔法のかかった武器／防具／装飾品、そして — より高い階層では — **パワースクロール**、
**超越の巻物（Scrolls of Transcendence）**、**俊敏の巻物（Scrolls of Alacrity）**です。

## トレジャーマップというアイテム

すべてのマップには**レベル**と**パッケージ**があります。レベルは難易度と戦利品の予算を設定し、
パッケージは装備とスクロールをあるプレイスタイルへとテーマ付けします。

**レベル**（enum `TreasureLevel`）、易しい順から難しい順へ：

| レベル | 解読難易度 | 宝箱の必要スキル | 魔法アイテム | ゴールド範囲 |
|---|---|---|---|---|
| **Stash** | 100 | 5 | 6 | 10,000〜40,000 |
| **Supply** | 200 | 45 | 8 | 20,000〜50,000 |
| **Cache** | 300 | 75 | 12（Assassinは24） | 30,000〜60,000 |
| **Hoard** | 400 | 80 | 18 | 40,000〜70,000 |
| **Trove** | 500 | 80 | 36 | 50,000〜70,000 |

*解読難易度*は`AssignChestQuality`／解読テーブル（`Utility.Random(difficulty)`をあなたの
地図作製と比較）です。*宝箱の必要スキル*、*魔法アイテム数*、*ゴールド範囲*は
`TreasureMapInfo.Fill`、`GetEquipmentAmount`、`GetGoldCount`から来ています。

**パッケージ**（enum `TreasurePackage`） — 戦利品のテーマ：

- **Artisan** — クラフトツール／資源、レシピ、地図師／クラフター向けの逸品。
- **Assassin** — ダガー、軽装防具、隠密／毒系統の戦利品（そしてCacheではより多くの魔法アイテム）。
- **Mage** — 杖、ローブ／革、リージェント（Stashにて）、術者向けスクロール。
- **Ranger** — 弓、皮／スタッド防具、弓術／調教系統。
- **Warrior** — 重武器、プレート防具と盾、近接スクロール。

**マップの出どころ。** マップは基本確率**`LootChance = .01`**（1%）でモンスターの戦利品として
落ち、生物ごとに上書き可能です（`Config/TreasureMaps.cfg`、`TreasureMap.LootChance`）。掘り出した
宝箱自体が次の上のマップを含むことがあります：Trove未満のレベルでは、宝箱が1レベル上のマップを
落とす確率が10%あります（`TreasureMapInfo.Fill`）。解読されたマップは**ブレス**されるので、
あなたの手元に残ります。

## トレジャーハンターのスキル

トレジャーハンティングは、幅広いキャラクターを作る典型的な理由です — 端から端まで複数のスキルに
触れるため、[セブンGMテンプレート](/ja/templates/seven-gm/)と自然に組み合わさります。

- **[地図作製（Cartography）](/ja/skills/cartography/)** — マップを**解読**します。レベルが
  高いほど、より多くの地図作製が必要です（上記の解読難易度テーブル）。この現代システムでは、
  地図作製は掘削範囲（下記）と宝箱の品質ロール（`AssignChestQuality`）も*同時に*支配します。
- **[採掘（Mining）](/ja/skills/mining/)** — 宝箱を掘り出すには**掘削ツール**（任意の採掘採取
  ツール、例：シャベルやつるはし）を持ち運ぶ必要があります（`TreasureMap.HasDiggingTool`）。
- **[開錠（Lockpicking）](/ja/skills/lockpicking/)** — 宝箱は施錠されています。そのロックレベルは
  宝箱の*必要スキル − 10*、最大ロックレベルは*必要スキル + 40*です（`TreasureMapInfo.Fill`）。
- **[トラップ解除（Remove Trap）](/ja/skills/remove-trap/)** — すべての宝箱には**爆発の罠**
  （`TrapType.ExplosionTrap`）が仕掛けられています。爆発する前に解除してください。
- **戦闘 / [魔法（Magery）](/ja/magic/) / [調教](/ja/playing/taming-and-pets/)** — 掘削で沸く
  守護者を捌くために。[戦闘の基本](/ja/playing/combat-basics/)を参照。

### 掘削範囲

掘るためにピンへどれだけ近く対象指定する必要があるかは、あなたの**地図作製**に依存します
（現代システムは範囲に採掘ではなく地図作製を使います — `DigTarget.OnTarget`）：

| 地図作製 | 最大掘削範囲 |
|---|---|
| 100+ | 4タイル |
| 81〜99 | 3タイル |
| 51〜80 | 2タイル |
| 51未満 | 1タイル |

遠すぎる場所を対象指定すると、マップはどの方向へ移動すべきかを教えてくれます。8タイル以内では
「とても近い」と言います。

## マップを読む（ガンプ）

解読されたトレジャーマップはまさに文字通り — **世界の一区画を地図作製で描いた地図に、埋まった
宝箱の場所に1本のピンが刺さったもの**です。座標の一覧ではありません。あなたが見分けなければ
ならない地形の絵です。

メカニクス上（`servuo: Scripts/Services/TreasureMaps/TreasureMap.cs`）、マップが作られるとき、
宝箱の周りのブリタニア（フェルッカ／トランメル）の**600 × 600タイルの地域**を捉えます — 他の
ファセットではより小さく（300 × 300、またはTer Murでは200 × 200） — そしてそれを小さな羊皮紙の
ガンプとして表示します（解読されたマップアイテムはグラフィック`0x14EC`）。マップは次に
`AddWorldPin(ChestLocation)`を呼び出して、その地点に**1本のピン**を落とします。

決定的に重要なのは、宝箱は**中央にない**ことです：捉えられたウィンドウはオフセットされており、
掘削地点はマップの4分の1から4分の3のあたりに来ます
（`x1 = ChestLocation.X − RandomMinMax(width/4, 3·width/4)`）。だから単に中央へ航海すること
はできません — ピンの周りの**海岸線、川、道、ランドマークを読み**、それらを現実世界と照合し、
そこへ騎乗するか航海し、その正確な地点の範囲内で掘らなければなりません。

![解読されたトレジャーマップの例：羊皮紙の巻物にインクで描かれた海岸線と、掘削地点に番号付きのピンが中央からずれて刺さっている](/img/treasure/example-map.png)

*解読されたマップの一例で、クライアントが表示するとおりに描かれています — 手描きのインクの海岸線の
輪郭（古典的なハッチのティック付き）が羊皮紙の巻物に描かれ、本物のクライアントガンプアートで
縁取られています：「Plot Course」のタイトルバー（ガンプ`0x1398`）、木の棒の巻物フレーム
（`0x1432`）、そしてコンパスローズ（`0x139D`）。番号付きのピンは掘削地点に中央からずれて刺さって
いるので、周囲の海岸線を読んで世界の中の一致する場所を見つけます。*

## 掘削地点

宝箱の地点が選ばれる方法は2通りあり、どこで掘ることになるかに影響します：

- **古典的な固定地点（伝統的な「掘削スポット」）。** `Data/treasure.cfg`は**193のハードコード
  された**ブリタニア（フェルッカ／トランメル）の座標 — プレイヤーが*あの*掘削地点として思い浮かべる
  有名なトレジャースポット — を列挙しています。これらは、ランダム化された場所が**オフ**のときに
  `GetRandomClassicLocation()`によって使われます。
- **このシャードの現代のランダム化マップ。** `Config/TreasureMaps.cfg`が**`Enabled=True`**である
  ため（`TreasureMap.NewChestLocations`）、稼働中のマップは代わりに**各ファセットの掘削可能な
  地域内で宝箱をランダム化します**（`TreasureMap.GetRandomLocation`）。フェルッカとトランメルでは
  その地域は**マップ全体**です（`0,0 → 5119,4095`）。Tokuno、Malas、Ilshenar、Ter Mur、Eodonは
  特定の矩形を使います。選ばれたタイルは次に`ValidateLocation`によって検証されます — 町、家、
  ダンジョン、チャンピオンスポーン地域、道、そして歩行不可または非自然のタイルを拒否します
  （土／草／ジャングル／森／雪のみが許可されます）。そのため宝箱は常に開けた荒野に落ちます。

下の地図は**193の古典的地点**をフェルッカ上にプロットしており、ブリタニア全土の伝統的な広がりを
見ることができます。このシャードでは、今日のマップが指す正確な一覧というより、トレジャーが好む
*種類*の地形のガイドとして扱ってください。

![193の古典的なトレジャー掘削地点すべてが金色のXマーカーとしてプロットされたブリタニアの地図](/img/treasure/locations.png)

*`Data/treasure.cfg`からの193の古典的掘削地点すべてを、フェルッカの地図上にプロットしたもの。*

**正確な座標が欲しいですか？** 各地点の絶対（X, Y） — 最寄りの都市とマップへのジャンプリンク
付き — は**[トレジャーマップ掘削地点](/ja/playing/treasure-locations/)**に列挙されています。

## 宝箱と戦利品

**守護者。** 掘削を終えると、宝箱のところに**4**体のモンスターが沸きます（`DigTimer.OnTick`）。
現代システムでは各スポーンに**70%**の確率で`(Guardian)`のタグが付きます。それらはマップレベルと
ファセットに応じてスケールします（`TreasureMap.Spawn`テーブル） — フェルッカ／トランメルでは、
おおよそ：

- **Stash** — モングバット、ラットマン、スケルトン、ゾンビ、ヘッドレス。
- **Supply** — オークの魔法使い、ガーゴイル、ゲイザー、ヘルハウンド、アースエレメンタル。
- **Cache** — リッチ、オーガロード、ドレッドスパイダー、エレメンタル、リッチロード、デーモン、エルダーゲイザー。
- **Hoard** — エンシェントワーム、バルロン、ブラッド／ポイズンエレメンタル、タイタン。
- **Trove** — ブラッド／ポイズンエレメンタル、コールドドレイク、フロストドラゴン／ドレイク、グレータードラゴン。

**開ける。** 宝箱は施錠され**爆発の罠**を備えています。[開錠](/ja/skills/lockpicking/)でロックを
開け、[トラップ解除](/ja/skills/remove-trap/)で解除します。宝箱の**品質**
（Rusty / Standard / Gold）は掘削時にあなたの地図作製からロールされ、宝石、リージェント、材料の
数を増やします。

**戦利品**（`TreasureMapInfo.Fill`）、中身ごとに：

- **ゴールド** — レベルに応じてスケールしたゴールドの袋（上記の表を参照）、加えて宝箱の品質と
  レベルとともに数が増える**宝石の袋**。
- **魔法装備** — マップの**パッケージ**によってテーマ付けされた、ランダムに魔法のかかった武器、
  防具、装飾品。レベル表の数（Stash → Troveで6 → 36アイテム）。
- **リージェント** — **Stash + Mage**マップでのみ（宝箱の品質に応じて20/40/60）。
- **クラフト資源と特殊材料** — **Artisan**マップで（インゴット、板、革。Ter Murではインビューイング
  材料など）。
- **特殊／マイナーアーティファクトの戦利品と装飾品** — Supplyから上は確率が増します。
- **パワースクロール** — **フェルッカのみ**、**Cache以上**で、パッケージのスキルで**+110**
  （`GetPowerScrollList`）。
- **超越の巻物（Scrolls of Transcendence）** — Supply/Cacheを除くほとんどのレベルで
  （`GetTranscendenceList`）。
- **俊敏の巻物（Scrolls of Alacrity）** — Stashを除くほとんどのレベルで（そしてフェルッカでは
  Cacheでも除く）（`GetAlacrityList`）。

魔法装備と特殊アイテムはパッケージによってテーマ付けされ、レベルごとの予算内で
`RunicReforging.GenerateRandomItem`によって作られます。個々のドロップが何であるかについては
[アイテムリファレンス](/ja/items/)を参照してください。

## 関連項目

- [地図作製](/ja/skills/cartography/) · [採掘](/ja/skills/mining/) ·
  [開錠](/ja/skills/lockpicking/) · [トラップ解除](/ja/skills/remove-trap/)
- [セブンGMテンプレート](/ja/templates/seven-gm/) · [戦闘の基本](/ja/playing/combat-basics/) ·
  [調教とペット](/ja/playing/taming-and-pets/)
- [資源の採取](/ja/playing/gathering-resources/) · [アイテムリファレンス](/ja/items/)

地点は`Data/treasure.cfg`からプロットされています。地図アートと解読されたマップの羊皮紙は
クライアント自身の著作権上問題のないアセットです。
