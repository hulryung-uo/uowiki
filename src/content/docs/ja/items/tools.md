---
title: 道具
description: 製作・実用道具 — tinker、smith、tailor、carpenter、scribe、採集の各道具が何をするか、どのスキルに仕えるか、使用回数はいくつか、どこで入手するか。
status: source-verified
sources:
  - "servuo: Scripts/Items/Tools/BaseTool.cs"
  - "servuo: Scripts/Items/Tools/BaseHarvestTool.cs"
  - "servuo: Scripts/Items/Tools (TinkerTools, SmithHammer, Tongs, SewingKit, Scissors, Saw, DovetailSaw, MouldingPlane, JointingPlane, DrawKnife, Froe, Inshave, FletcherTools, ScribesPen, MortarPestle, Skillet, FlourSifter, RollingPin, MapmakersPen, Shovel, FishingPole)"
  - "servuo: Scripts/Items/Equipment/Weapons/Pickaxe.cs, Hatchet.cs, Axe.cs"
  - "servuo: Scripts/Items/Consumables/LockPick.cs"
  - "servuo: Scripts/Services/Craft/DefTinkering.cs (craft recipes + skill ranges)"
  - "client: artLegacyMUL.uop"
last_verified: 2026-06-11
generated: false
---

道具とは、限られた数の**使用回数 (uses)** を持つ消耗品です。ほとんどの道具はダブルクリックで
**製作メニュー** (そのスキルでその道具が作れるものすべてを並べた gump) を開きます。他の道具は
ダブルクリックすると一回限りのアクションを発し、世界を対象にします — pickaxe なら岩を、
fishing pole なら水を。いずれにせよ、使用に成功するたびに道具の耐久が削られ、**残り使用回数**が
ゼロになると道具は崩れ、あなたは次の1本に手を伸ばします。

このリストのほぼすべての金属道具は tinker が作ります — [Tinkering](/ja/skills/tinkering/) は
鉄インゴット (そして一部の木製道具には板) を Britannia のあらゆる工具一式に変えます。残りは
町のベンダーから購入します。製作 gump の仕組みは [Crafting](/ja/playing/crafting/) を、採集
道具が使うポイント＆クリックの手順は [Targeting](/ja/playing/targeting/) を参照してください。

一族全体に当てはまるいくつかの事実を、`Scripts/Items/Tools/BaseTool.cs` から直接:

- 出来たての **tinker 製**金属道具は、*ランダム*な 25–75 回の使用回数で始まります
  (`BaseTool(int itemID) : this(Utility.RandomMinMax(25, 75), itemID)`) — exceptional な
  職人技と高品位のインゴットがその数を引き上げます。
- 道具の品質と使用回数は、メニューではなく作り手に乗ります: 優れた tinker ほど長持ちする道具を
  作ります。
- 道具は魂縛りでは**ありません** — 備蓄したり、売ったり、セッション中にギルドメイトへ新品の
  sewing kit を手渡したりできます。

## 製作道具

これらはそれぞれの職のための製作 gump を開きます。特記なき限り、各々は tinker が鉄インゴット
から鍛えます。括弧内のスキル範囲は、レシピを*最初に*試行できる Tinkering スキルから*最後に*
保証されるところまで (`DefTinkering.cs` より) です。対応する NPC ベンダーから単に購入する
こともできます — [ベンダーと銀行](/ja/playing/vendors-and-banking/) 参照。

### Tinker's Tools — [Tinkering](/ja/skills/tinkering/)

<img src="/img/items/0x1EB8.png" class="uo-sprite" alt="" width="56" />

tinker 自身の道具一式。ダブルクリックで Tinkering メニューを開き、時計、罠、鍵、道具
(さらなる tinker's tools を含む)、宝飾品、そして幅広い小型金属製品を作ります。**Tinkering
10.0–60.0** で 2 個の鉄インゴットから tinker 製。tinker NPC が販売。使用回数は既定の 25–75
範囲です。

### Smith's Hammer & Tongs — [Blacksmithy](/ja/skills/blacksmithy/)

<img src="/img/items/0x13E3.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0FBB.png" class="uo-sprite" alt="" width="56" />

**smith's hammer** は forge で Blacksmithy メニューを開き、インゴットを武器と防具に叩き上げます
(`CraftSystem => DefBlacksmithy.CraftSystem`)。**tongs** は同じ職に属し、鉱石を手持ちの状態に
変換して forge 作業を扱うための道具です。tinker 製 — hammer は **Tinkering 40.0–90.0** で 4 個の
インゴットから、tongs は **35.0–85.0** で 1 個のインゴットから — または blacksmith と tinker の
ベンダーから購入。(AOS では製作可能な hammer クラスは `SmithyHammer`、古い `SmithHammer` の
アートは `0x13E3` です。)

### Sewing Kit & Scissors — [Tailoring](/ja/skills/tailoring/)

<img src="/img/items/0x0F9D.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F9F.png" class="uo-sprite" alt="" width="56" />

**sewing kit** は Tailoring メニューを開き、cloth と leather を衣類と軽防具に縫い上げます
(`DefTailoring.CraftSystem`)。**scissors** は仕立て道具を兼ねる*と同時に*、万能の裁断具です:
**bolt of cloth を cloth に、cloth を bandages に、hides を leather に**裁断します
([Resources](/ja/items/resources/) 参照)。scissors は特例として固定の **50 回使用**に設定されて
おり (`Scissors.cs` の `m_UsesRemaining = 50`)、ランダムな 25–75 の既定ではありません。両方とも
tinker 製 (sewing kit: **10.0–70.0** で 2 個のインゴット、scissors: **5.0–55.0** で 2 個の
インゴット) または tailor と provisioner のベンダーから購入。

### Carpentry tools — [Carpentry](/ja/skills/carpentry/)

<img src="/img/items/0x1034.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1028.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x102C.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1030.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E4.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E5.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x10E6.png" class="uo-sprite" alt="" width="56" />

carpenter は小さな武器庫を持ち歩き、**そのいずれもが同じ Carpentry メニューを開きます**
(どのクラスも `DefCarpentry.CraftSystem` を返します): **saw**、**dovetail saw**、**moulding
plane**、**jointing plane**、**smoothing plane**、**draw knife**、**froe**、**inshave** です。
これらはアートとレシピコストだけが異なります — tinker から渡されたものを選び、板から家具、
楽器、弓、家のアドオンを作りましょう。金属刃のもの (saw、dovetail saw、draw knife、froe、
inshave) は **Tinkering 30.0–80.0** で鉄から tinker 製。木製の plane と jointing/moulding plane
は **0.0–50.0** で**板**から tinker 製。すべて carpenter と tinker の NPC が販売します。

### Fletcher's Tools — [Bowcraft & Fletching](/ja/skills/bowcraft-fletching/)

<img src="/img/items/0x1022.png" class="uo-sprite" alt="" width="56" />

Bowcraft メニュー (`DefBowFletching.CraftSystem`) を開き、板と羽から弓、クロスボウ、矢、ボルトを
仕立てます。**Tinkering 35.0–85.0** で 3 個のインゴットから tinker 製、または bowyer/fletcher の
ベンダーから購入。

### Scribe's Pen — [Inscription](/ja/skills/inscription/)

<img src="/img/items/0x0FBF.png" class="uo-sprite" alt="" width="56" />

Inscription メニュー (`DefInscription.CraftSystem`) を開き、呪文スクロールと書物を書写します
(reagents + 空白スクロール)。**Tinkering 25.0–75.0** で 1 個のインゴットから tinker 製、または
scribe と mage のベンダーから購入。mapmaker's pen とアート `0x0FBF` を共有します。

### Mortar & Pestle — [Alchemy](/ja/skills/alchemy/)

<img src="/img/items/0x0E9B.png" class="uo-sprite" alt="" width="56" />

Alchemy メニュー (`DefAlchemy.CraftSystem`) を開き、reagents をすり潰してポーションにします。
**Tinkering 20.0–70.0** で 3 個のインゴットから tinker 製、または alchemist と mage のベンダーから
購入。(一部のクエスト手順で reagents を砕くための対象指定道具としても使われます。)
[Alchemy](/ja/skills/alchemy/) を参照してください。

### Cooking tools — [Cooking](/ja/skills/cooking/)

<img src="/img/items/0x097F.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x103E.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x1043.png" class="uo-sprite" alt="" width="56" />

**skillet**、**flour sifter**、**rolling pin** はそれぞれ Cooking メニュー
(`DefCooking.CraftSystem`) を開きます — 実際には料理が必要とするレシピに応じて、いずれか
(小麦粉をふるう、生地をのばす、揚げる) に手を伸ばします。tinker 製: skillet (4 個のインゴット、
**30.0–80.0**)、flour sifter (3 個のインゴット、**50.0–100.0**)、rolling pin (5 個の**板**、
**0.0–50.0**)。cook、baker、provisioner のベンダーから購入。

### Mapmaker's Pen — [Cartography](/ja/skills/cartography/)

<img src="/img/items/0x0FBF.png" class="uo-sprite" alt="" width="56" />

Cartography メニュー (`DefCartography.CraftSystem`) を開き、空白の地図を描き、宝の地図の場所を
特定します。**Tinkering 25.0–75.0** で 1 個のインゴットから tinker 製、または mapmaker/scribe の
ベンダーから購入。scribe's pen と同じアート (`0x0FBF`)。

## 採集道具

これらはメニューを開きません — ダブルクリックして、それから資源ノードを**対象指定**します
([資源の採集](/ja/playing/gathering-resources/) 参照)。製作システムではなく採集スキルに仕えます。

### Pickaxe & Shovel — [Mining](/ja/skills/mining/)

<img src="/img/items/0x0E86.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F39.png" class="uo-sprite" alt="" width="56" />

両方とも Mining 採集 (`HarvestSystem => Mining.System`) を実行します。**pickaxe** は万能の採掘
道具です — 鉱脈を掘り、洞窟内や山肌で鉱石を採取し、`BaseAxe` から派生するため使用可能な (弱い)
武器でもあります。固定の **50 回使用**で始まります (`Pickaxe.cs` の `UsesRemaining = 50`)。
**shovel** は鉱石を掘り、よりすっきりした「地面を掘る」ワークフローに最適な道具です。これも
既定で **50 回使用** (`Shovel() : this(50)`)。岩から引き出すもの — iron から valorite、加えて
granite、sand、宝石 — は [Resources](/ja/items/resources/) ページにあります。pickaxe は
tinker/blacksmith の品。shovel は **Tinkering 40.0–90.0** で 4 個のインゴットから tinker 製で、
miner や provisioner が販売します。

### Hatchet & Axe — [Lumberjacking](/ja/skills/lumberjacking/)

<img src="/img/items/0x0F43.png" class="uo-sprite" alt="" width="56" />
<img src="/img/items/0x0F49.png" class="uo-sprite" alt="" width="56" />

任意の斧型武器 (**hatchet**、**axe**、battle axe など — すべて `BaseAxe` から派生) は二役を
こなします: 木に振るって [Lumberjacking](/ja/skills/lumberjacking/) のために**丸太**を切り、
それから丸太を**板**に切り、さらに本物の近接武器として携えます。blacksmith が作り、
weapon/provisioner のベンダーが販売します。収量と丸太→板の表は
[Resources](/ja/items/resources/) にあります。

### Fishing Pole — [Fishing](/ja/skills/fishing/)

<img src="/img/items/0x0DC0.png" class="uo-sprite" alt="" width="56" />

ダブルクリックして水を対象指定し釣ります (`FishingPole` が Fishing 採集を実行)。装備可能な
片手アイテムでもあり、それ自体が製作可能です (Bowcraft/Carpentry で木材から)。標準の pole は
**150 回使用**で始まります (`FishingPole.cs` の `UsesRemaining = 150`) — 釣りは長い修行なので、
金属道具よりはるかに多いです。fishmonger と provisioner のベンダーが販売します。
[Fishing](/ja/skills/fishing/) を参照してください。

## 実用道具

製作 gump に紐づかない、より小さな一仕事のアイテム:

- **Lockpicks** <img src="/img/items/0x14FC.png" class="uo-sprite" alt="" width="56" /> —
  ダブルクリックして施錠された箱や扉を対象指定し、あなたの
  [Lockpicking](/ja/skills/lockpicking/) スキルを錠のレベルにぶつけます。難しい錠での解錠失敗は
  破損することがあります。メニュー道具と違い、lockpick は**スタック可能な消耗品**です (`Amount`、
  道具ごとの使用回数ではない — `LockPick.cs`)。**Tinkering 45.0–95.0** で 1 個のインゴットから
  tinker 製、または thief/tinker のベンダーから購入。
- **Keys & key rings** — tinker は箱や家のための鍵 (とそれに合う錠) を製作します。key ring は
  その束を保持します。Tinkering メニューで作ります (`Key` は 3 個のインゴット、**20.0–70.0**)。
- **Tinker traps** — Tinkering メニューは戦利品を守るための罠付き容器 (dart、poison、explosion の
  罠) も作ります。[Tinkering](/ja/skills/tinkering/) と
  [Crafting → Tinkering](/ja/crafting/tinkering/) を参照してください。
- **Dye tubs** <img src="/img/items/0x0FAB.png" class="uo-sprite" alt="" width="56" /> —
  製作道具ではなく染色用具です: cloth やアイテムを入れ、色相を選んで染めます。色空間は
  [色相リファレンス](/ja/reference/hues/) です。

## クイックリファレンス

スキル範囲は、レシピを最初に試行→最後に保証する Tinkering スキルです (`DefTinkering.cs`)。
「Random 25–75」は tinker 製道具の `BaseTool` 既定です。

| 道具 | 仕えるスキル | 機能 | 使用回数 | 入手方法 |
|------|--------------|--------------|------|------------|
| Tinker's Tools | [Tinkering](/ja/skills/tinkering/) | Tinkering メニューを開く | random 25–75 | Tinker (10–60) または tinker ベンダー |
| Smith's Hammer | [Blacksmithy](/ja/skills/blacksmithy/) | forge で武器と防具を鍛える | random 25–75 | Tinker (40–90) または smith ベンダー |
| Tongs | [Blacksmithy](/ja/skills/blacksmithy/) | forge / 鉱石の扱い | random 25–75 | Tinker (35–85) または smith ベンダー |
| Sewing Kit | [Tailoring](/ja/skills/tailoring/) | Tailoring メニューを開く | random 25–75 | Tinker (10–70) または tailor ベンダー |
| Scissors | [Tailoring](/ja/skills/tailoring/) | Tailoring メニュー; cloth/bolt/hide を裁断 | **50** | Tinker (5–55) または tailor ベンダー |
| Saw / Dovetail Saw | [Carpentry](/ja/skills/carpentry/) | Carpentry メニューを開く | random 25–75 | Tinker (30–80) または carpenter ベンダー |
| Moulding/Jointing/Smoothing Plane | [Carpentry](/ja/skills/carpentry/) | Carpentry メニューを開く | random 25–75 | Tinker が**板**から (0–50) または carpenter ベンダー |
| Draw Knife / Froe / Inshave | [Carpentry](/ja/skills/carpentry/) | Carpentry メニューを開く | random 25–75 | Tinker (30–80) または carpenter ベンダー |
| Fletcher's Tools | [Bowcraft](/ja/skills/bowcraft-fletching/) | Bowcraft メニューを開く | random 25–75 | Tinker (35–85) または bowyer ベンダー |
| Scribe's Pen | [Inscription](/ja/skills/inscription/) | Inscription メニューを開く | random 25–75 | Tinker (25–75) または scribe ベンダー |
| Mortar & Pestle | [Alchemy](/ja/skills/alchemy/) | Alchemy メニューを開く | random 25–75 | Tinker (20–70) または alchemist ベンダー |
| Skillet / Flour Sifter / Rolling Pin | [Cooking](/ja/skills/cooking/) | Cooking メニューを開く | random 25–75 | Tinker (skillet 30–80、sifter 50–100、pin boards 0–50) または cook ベンダー |
| Mapmaker's Pen | [Cartography](/ja/skills/cartography/) | Cartography メニューを開く | random 25–75 | Tinker (25–75) または mapmaker ベンダー |
| Pickaxe | [Mining](/ja/skills/mining/) | 鉱石を採掘 (弱い斧武器でもある) | **50** | Tinker/smith または provisioner |
| Shovel | [Mining](/ja/skills/mining/) | 鉱石を掘る | **50** | Tinker (40–90) または provisioner |
| Hatchet / Axe | [Lumberjacking](/ja/skills/lumberjacking/) | 丸太を切る、板を裁つ (武器でもある) | 武器耐久 | Smith または weapon ベンダー |
| Fishing Pole | [Fishing](/ja/skills/fishing/) | 釣り (水を対象指定) | **150** | Fisher/provisioner ベンダーまたは製作 |
| Lockpicks | [Lockpicking](/ja/skills/lockpicking/) | 施錠された箱/扉を解錠 | スタック可 (消耗) | Tinker (45–95) または thief ベンダー |
| Keys / Key Rings | — | 箱や家を施錠/解錠 | 該当なし | Tinker (key 20–70) |
| Dye Tub | — | cloth/アイテムを[色相](/ja/reference/hues/)で再着色 | 再利用可 | Tinker ベンダー / 報酬 |

## 関連項目

- [Tinkering](/ja/skills/tinkering/) — これらの大半を作るスキル · [Crafting 概要](/ja/crafting/) · [製作メニューの仕組み](/ja/playing/crafting/)
- [資源の採集](/ja/playing/gathering-resources/) · [Resources](/ja/items/resources/) — 採集道具が世界から引き出すもの
- [ベンダーと銀行](/ja/playing/vendors-and-banking/) — 道具を買う場所 · [Targeting](/ja/playing/targeting/)
- [道具カタログ](/ja/items/catalog/tools/) — ソースの全道具アイテム、アートとアイテム ID 付き · [アイテム概要](/ja/items/)
