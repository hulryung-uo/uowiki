---
title: 遊び方 — クラフト
description: 普遍的なクラフトの流れ — ツールからメニュー、カテゴリ、アイテム、製作へ — に加えて、各トレードの入り口、材料、エクセプショナル品質と製作者の刻印、失敗と材料喪失、修理、ルーニックツール、強化、バルクオーダーディード。
status: unverified
sources:
  - "servuo: Scripts/Services/Craft/Core/CraftGump.cs, CraftItem.cs (craft menu flow, exceptional chance, maker's mark)"
  - "servuo: Scripts/Services/Craft/Core/CraftItem.cs (failed skill check consumes the FULL listed resources for standard recipes — ConsumeType.All)"
  - "servuo: Scripts/Services/Craft/Core/QueryMakersMarkGump.cs, Repair.cs, Enhance.cs, Resmelt.cs (mark/repair/enhance/smelt features)"
  - "servuo: Scripts/Services/Craft/Def*.cs (per-trade craft definitions: Blacksmithy, Tailoring, Tinkering, Carpentry, BowFletching, Inscription, Cooking, Alchemy, Cartography, Masonry, Glassblowing)"
  - "in-game: foundry blacksmith evals 2026-06-12 (run c16f4 cycles 1-4 — 12 consecutive failed weapon crafts each burned the full 10-ingot cost; agent logs data/eval_logs/agent-evoc16f4c1s*/c3s*/c4s*)"
  - "general UO operation, pending in-game field verification"
last_verified: 2026-06-12
generated: false
---

このガイドは、**クラフト**が一般的にどう機能するか — すべてのトレードスキルが共有する流れ — を
説明し、それから各トレードの正しいツール、スキルページ、レシピ一覧へと案内します。クラフトは生の
材料（採取または購入したもの）を完成品 — 武器、防具、衣服、家具、ツール、食品、巻物、ポーション
など — に変えます。生の材料がどこから来るかについては、
[資源の採取](/ja/playing/gathering-resources/)と[資源リファレンス](/ja/items/resources/)を
参照してください。実践的な初期ビルドについては、
[鍛冶屋テンプレート](/ja/templates/blacksmith/)を参照してください。

**このページで使われる定義：**
- **トレードツール（Trade tool）** — クラフトのためにダブルクリックするアイテム（鍛冶のハンマー、
  裁縫キット、細工師の道具など）。各トレードには独自のツールがあります。
- **クラフトメニュー／クラフトガンプ** — トレードツールを使うと開くウィンドウ。アイテムの
  **カテゴリ**と、各カテゴリ内の**アイテム**を列挙します。
- **エクセプショナル（Exceptional）** — 最高品質の結果で、より良いステータスと、アイテムに名前を
  刻む選択肢を与えます。
- **資源／材料** — クラフト時に消費される素材（インゴット、板、革、布、リージェントなど）。

## 普遍的なクラフトの流れ

すべてのトレードは同じ5つのステップに従います（`Scripts/Services/Craft/Core/`のクラフトシステムに
対して検証済み）：

1. **ツールと材料を持つ。** トレードツールと必要な生の材料を**バックパック**に入れます。一部の
   レシピは、設備の近くにいることも必要とします（鍛冶には**炉と金床**、焼成には**オーブン**、布には
   **織機**など）。
2. **トレードツールをダブルクリックする。** これで**クラフトメニュー**（`CraftGump`）が開きます。
3. **カテゴリを選ぶ。** メニューはアイテムをカテゴリにまとめます（鍛冶屋なら：武器、防具、盾…）。
   カテゴリをクリックしてそのアイテムを見ます。カテゴリのレイアウトは**時代依存**であることに
   注意してください：このシャード（Endless Journey時代）では、鍛冶メニューはリング、チェーン、
   プレートを単一の**金属防具（Metal Armor）**カテゴリに統合し、時代制限のあるアイテムがあらゆる
   一覧に現れます — そのためアイテムの位置はクラシック時代の参照とは異なります。
4. **アイテムを選ぶ。** 各アイテムは**必要スキル**と**消費する材料**を示します。スキルや材料が
   足りないアイテムには印が付きます。
5. **作る。** *Make Now*（今すぐ作る）をクリックします（または数量を設定して一括製作）。あなたの
   キャラクターがしばらく作業し、それから**成功**（アイテムがパックに現れる）または**失敗**します。

メニューを開いたまま繰り返しクラフトできます。各試行は対応するスキルを鍛えます
（[スキル上昇](/ja/mechanics/skill-gain/)を参照）。

## 各トレードの入り口

各トレードは異なるスキル、ツール、メニューを使います。スキル範囲と完全なレシピ一覧はリンク先の
ページにあります — この表は単なる**入り口**です：

| トレード | スキル | ツール（ダブルクリック） | レシピ |
| --- | --- | --- | --- |
| 鍛冶 | [鍛冶（Blacksmithy）](/ja/skills/blacksmithy/) | 鍛冶のハンマー（**炉と金床**にて） | [/ja/crafting/blacksmithy/](/ja/crafting/blacksmithy/) |
| 裁縫 | [裁縫（Tailoring）](/ja/skills/tailoring/) | 裁縫キット | [/ja/crafting/tailoring/](/ja/crafting/tailoring/) |
| 細工 | [細工（Tinkering）](/ja/skills/tinkering/) | 細工師の道具 | [/ja/crafting/tinkering/](/ja/crafting/tinkering/) |
| 木工 | [木工（Carpentry）](/ja/skills/carpentry/) | のこぎり／ダブテイルソー | [/ja/crafting/carpentry/](/ja/crafting/carpentry/) |
| 弓作り | [弓矢作り（Bowcraft/Fletching）](/ja/skills/bowcraft-fletching/) | 弓師の道具 | [/ja/crafting/bowfletching/](/ja/crafting/bowfletching/) |
| 書写 | [書写（Inscription）](/ja/skills/inscription/) | 写字生のペン | [/ja/crafting/inscription/](/ja/crafting/inscription/) |
| 料理 | [料理（Cooking）](/ja/skills/cooking/) | フライパン／**オーブン**にて | [/ja/crafting/cooking/](/ja/crafting/cooking/) |
| 錬金術 | 錬金術（Alchemy） | 乳鉢と乳棒 | [/ja/crafting/alchemy/](/ja/crafting/alchemy/) |
| 地図作製 | 地図作製（Cartography） | 地図師のペン | [/ja/crafting/cartography/](/ja/crafting/cartography/) |
| 石工 | （スキル + ツール） | 木槌と鑿 | [/ja/crafting/masonry/](/ja/crafting/masonry/) |
| ガラス吹き | （スキル + ツール） | 吹き竿（炉／溶炉にて） | [/ja/crafting/glassblowing/](/ja/crafting/glassblowing/) |

すべてのトレードは[クラフト概要](/ja/crafting/)から閲覧できます。ツールそのものは
[ツールカタログ](/ja/items/catalog/tools/)にあります。

## 材料とその入手先

レシピは、パックに入っていなければならない**生の材料**を消費します：

- 鍛冶用の**インゴット** — 採掘した鉱石を炉で精錬します。[採掘](/ja/skills/mining/)と
  [資源の採取](/ja/playing/gathering-resources/)を参照。
- 木工と弓作り用の**板** — 丸太を板に切ります。[伐採](/ja/skills/lumberjacking/)を参照。
- 裁縫用の**革／皮**と**布** — 死体を剥いで革を得るか、布の連鎖を進めます。
  [資源の採取](/ja/playing/gathering-resources/)を参照。
- 書写／錬金術用の**リージェント** — NPCの魔法使い／錬金術師から買うか採取します。
  [リージェント](/ja/items/reagents/)を参照。
- 料理用の**食材** — 小麦粉、生の魚／肉など。

正確なスキル要件と、**色付き鉱石／革／木材の階層**（より高いスキルを要し、より良いアイテムを
産出する）は[資源リファレンス](/ja/items/resources/)に記載されています — 数字を暗記するよりそこへ
リンクしてください。

## 成功、エクセプショナル品質、製作者の刻印

クラフトすると、結果は次の3つのいずれかになります：

- **失敗** — 試行に失敗します（[失敗と材料喪失](#失敗と材料喪失)を参照）。
- **通常の成功** — 標準品質のアイテム。
- **エクセプショナル成功** — 最高品質で、ボーナスの耐久度／ステータスと、それに**刻印を入れる**
  選択肢があります。エクセプショナルの確率はレシピの要件を超えるスキルとともに上がります
  （`CraftItem.cs`の`GetExceptionalChance`で計算。一部のレシピは決してエクセプショナルにならず、
  特定のアイテム／タリスマンはボーナスを加えます）。

**製作者の刻印（Maker's mark）：** アイテムをエクセプショナルでクラフトすると、それに**キャラクターの
名前を刻む**かどうかを（`QueryMakersMarkGump`を通じて）尋ねられることがあります（「&lt;name&gt;
作」）。刻印されたエクセプショナル品は珍重され、より高く売れます。通常は一度好みを設定すると
メニューが記憶します。

したがって高いスキルは二重に重要です：より難しいアイテムをそもそもクラフトできるようにし、それらの
アイテムがエクセプショナルで仕上がる割合を高めます。

## 失敗と材料喪失

クラフトは失敗することがあり、**失敗は材料を破壊します**（鍛冶でフィールド検証済み）：

- 標準レシピでは、失敗したスキルチェックはそのアイテムの**記載された全資源**を消費し、一部では
  ありません（`CraftItem.cs`は通常レシピで`ConsumeType.All`で消費を振ります）。実地テストでは、
  12回連続で失敗した武器の試行がそれぞれ10インゴットのコストをまるごと焼きました — アイテム
  ゼロで120インゴットです。
- あなたの**成功確率は、レシピの最低スキルを超える50ポイントのウィンドウにわたって線形に
  スケールします**（例：最低スキルではほぼ必ず失敗、最低 + 50では決して失敗しません）。スキルが
  上がるにつれて失敗率は下がります — 希少な材料を賭ける前に安価なアイテムで鍛えてください。
- **あなたのスキルで鍛えられる最も安いレシピを選んでください。** 鍛冶屋にとっては**ダガー**
  （3インゴット、スキル0から製作可能）がずば抜けて最も安い練習用です。10インゴットのレシピを
  早すぎる段階で試みると、1振りあたり3倍以上の金属を無駄にします。

## アイテムの修理

使い込んだ武器、防具、ツールは**耐久度**を失い、やがて壊れます。それらを対応するトレードスキルで
**修理**できます（`Repair.cs`より）：

1. 関連する**トレードツール**をダブルクリックします（金属防具／武器には鍛冶のハンマー、革／布には
   裁縫キット、木製品にはのこぎりなど）。
2. クラフトメニューで**Repair（修理）**を選びます（または**修理ディード**を使います）。
3. 損傷したアイテムを対象指定します。

成功すると耐久度が回復します。修理の失敗は**アイテムの最大耐久度を下げる**ことがあるので、高い
スキルで修理してください。各トレードは、それが作れるアイテムの種類を修理します — 鍛冶は金属、裁縫は
革／布、木工／弓作りは木材、というように。

## ルーニックツールと強化（概要）

2つの上級機能が、ハイエンドのクラフターに魔法の装備を作らせます（メカニクスは拡張依存です —
詳細は検証なしとして扱ってください）：

- **ルーニックツール（Runic tools）** — 特殊で使用回数の限られたトレードツール（ルーニック
  ハンマー、裁縫キットなど。しばしば[バルクオーダー報酬](#バルクオーダーディードbods)から）で、
  **ランダムな魔法特性**を持つアイテムをクラフトします。ルーニックツールを持ったまま通常通りに
  クラフトします。
- **強化（Enhancing）** — 完成したアイテムを取り、**より良い資源で再鍛造する**ことで
  （`Enhance.cs`より）その資源のボーナスを加えます。強化は**失敗時にアイテムを破壊する**ことが
  あるので、危険です。

各トレードがどのルーニックツールと強化オプションをサポートするかについては、個別の
[/ja/crafting/](/ja/crafting/)トレードページを参照してください。

## 再精錬（金属の回収）

鍛冶屋は、クラフトまたは略奪した金属アイテムを炉でその一部のインゴットへと**再精錬**できます
（`Resmelt.cs`より） — 失敗した、または不要な金属品をリサイクルするのに便利です。鍛冶メニューの
精錬オプションを使い、炉の近くでアイテムを対象指定します。

## バルクオーダーディード（BODs）

**バルクオーダーディード（Bulk Order Deeds）**はクラフトの報酬ループです。トレードのNPC店主
（例：鍛冶屋や織工）は定期的に**BOD**を提供します：特定アイテムを一定数量（任意でエクセプショナル、
かつ特定の材料で）求めるディードです。

BODを使うには：
1. 関連するNPCからディードを入手します（バルクオーダーを求める／コンテキストメニューを使う）。
2. **要求されたアイテムをクラフトし**、それぞれをディードの上に落として満たします。
3. **完成したディードをNPCに納品**して**報酬** — ゴールド、希少材料、ルーニックツール、レシピ、
   そして複数の小ディードを組み合わせてより大きな賞品を得る**大BOD** — を受け取ります。

BODはルーニックツールやその他のクラフター専用報酬への主要な経路です。報酬表はトレードとシャード
設定によって異なります — そのトレードの[/ja/crafting/](/ja/crafting/)ページを確認してください。

## 関連項目

- [クラフト概要](/ja/crafting/)と[鍛冶クラフト](/ja/crafting/blacksmithy/)
- [鍛冶屋テンプレート](/ja/templates/blacksmith/) — 完全なクラフトビルド
- [資源の採取](/ja/playing/gathering-resources/) — 材料の出どころ
- [資源リファレンス](/ja/items/resources/) · [ツールカタログ](/ja/items/catalog/tools/) ·
  [資源カタログ](/ja/items/catalog/resources/)
- スキルページ：[鍛冶](/ja/skills/blacksmithy/) · [裁縫](/ja/skills/tailoring/) ·
  [細工](/ja/skills/tinkering/) · [木工](/ja/skills/carpentry/) ·
  [弓矢作り](/ja/skills/bowcraft-fletching/) · [書写](/ja/skills/inscription/) ·
  [料理](/ja/skills/cooking/)
- [スキル上昇](/ja/mechanics/skill-gain/) · [色相／カラーリファレンス](/ja/reference/hues/)
