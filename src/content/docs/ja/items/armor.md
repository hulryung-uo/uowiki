---
title: 防具
description: 防具と5つの抵抗値の仕組み、cloth から dragon scale までの全素材、装備スロット、盾、そしてバランスの取れたスーツの組み立て方。
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Armor/BaseArmor.cs"
  - "servuo: Scripts/Items/Equipment/Armor/ArmorEnums.cs"
  - "servuo: Scripts/Items/Equipment/Armor/*.cs (per-piece base resists, str req, material)"
  - "servuo: Server/Mobile.cs (MaxPlayerResistance = 70)"
  - "servuo: Scripts/Mobiles/PlayerMobile.cs (GetMinResistance — Magic Resist floor)"
  - "servuo: Scripts/Misc/RegenRates.cs (GetArmorMeditationValue — meditation/mana penalty)"
  - "client art: static art for piece sprites"
last_verified: 2026-06-11
generated: false
---

防具は、あなたのヒットポイントとドラゴンのブレスとの間に立ちはだかるものです。当シャード
(ServUO、Endless Journey / AOS ルール) では、身につける各部位が**抵抗値 (resistances)** に
寄与し、各ダメージタイプの一部を吸収します。優れたスーツは、1枚の重い胸当てで決まるものでは
ありません — 6つの装備スロットすべてをカバーし、5つの抵抗値を厳しい上限の下でバランスさせる
ことが肝心です。

以下の表の数値は、サーバーソース内で部位ごとに定義された**基礎 (base)** 値です。実際に
ペーパードールに表示される量には、製作**素材 (resource)** (鉱石や革の種類)、**exceptional**
品質、そして任意の魔法プロパティからのボーナスが加わります — [素材](#materials) と
[スーツと戦略](#suits--strategy) を参照してください。

## 防具の仕組み (AOS / EJ)

### 5つの抵抗値

現代の防具は5つの**抵抗値 (resistances)** で評価され、それぞれが1つのダメージタイプを
軽減します:

- **Physical** — 剣、矢、ほとんどの近接と物理呪文
- **Fire** — Fireball、Flamestrike、火を吐く生物
- **Cold** — 氷結呪文と冷気系の生物
- **Poison** — Poison 呪文、毒武器、毒を持つ生物
- **Energy** — Energy Bolt、Lightning、エネルギー攻撃

抵抗値が *N* なら、そのダメージタイプは *N* パーセント軽減されます。身につけた各部位は
その抵抗値を合計に加え、ペーパードールは身につけた全部位にわたる合計を表示します。ダメージは
入ってくるタイプに対応する抵抗値に対して適用されるため、火に偏ったスーツはエナジーメイジの
前で溶けてしまいます。

### 70% 抵抗上限

プレイヤーの抵抗値には上限があります。ServUO の `Server/Mobile.cs` は
`MaxPlayerResistance = 70` を設定しており — **どれだけ防具やボーナスを積み重ねても、単一の
抵抗値は 70% を超えられません**。したがってスーツ構築は、気にかけるタイプで余剰を無駄にせず
70 に到達させるゲームです。(一部のモンスターや特殊効果はあなたの実効上限を下げることが
できますが、70 という天井は通常のプレイヤー最大値です。)

高い **Magic Resistance** スキルは*逆*に働きます。抵抗値の*下限*を上げ
(`PlayerMobile.GetMinResistance`)、GM Resist では低い抵抗値を最低値まで引き上げるため、
Resist メイジはどの属性に対しても完全に無防備になることはありません。
[戦闘 (上級)](/ja/playing/combat-advanced/) を参照してください。

### 必要筋力

各部位には**必要筋力 (Strength requirement)** があります — 重い素材ほど多くを要求します。
plate chest は **95 Strength** を必要とし、leather chest はわずか **25** です (AOS 値)。要件を
下回って部位を装備すると代償を被るため、低筋力のキャスターは leather に傾きます。一部の防具
モッドや素材は要件を下げます。[キャラクターとステータス](/ja/playing/character-and-stats/) を
参照してください。

### Meditation ペナルティ (マナ回復)

重い金属防具は**マナ回復を阻害します**。ServUO の `RegenRates.GetArmorMeditationValue` は
身につけた各部位の **meditation 許容度**をチェックします:

- **All** (med 可能) — ペナルティなし (leather、cloth、ほとんどのメイジ向け防具)
- **Half** — 部位のスケール済み防御値の半分をマナ回復から差し引く (studded)
- **None** (med 不可) — スケール済み防御値の全量を差し引く (bone、ring、chain、plate、
  dragon、stone)

身につけた全部位からのペナルティが合計・分割され、マナ回復を引き下げます。逃げ道は2つ
あります: **Mage Armor** プロパティ (および **Spell Channeling**) はこの計算において任意の
部位を完全に med 可能として扱わせ、Stygian Abyss / EJ ルールでは med 不可の**金属**防具は
代わりに固有の **Lower Mana Cost** を付与します (近接キャスターを助ける小さな引き換え)。
完全なメカニクス — メイジが leather を好む理由を含む — は
[Meditation とマナ](/ja/playing/meditation-and-mana/) にあります。

### 装備スロットと「スーツ」

防具は6つの装備スロットをカバーし、加えて盾のための利き手とは逆の手があります:

| スロット | 部位 |
|---|---|
| Helm | helmet、cap、coif、circlet、kabuto |
| Gorget / Neck | gorget、collar、mempo |
| Chest | chest、tunic、bustier |
| Arms | arms、sleeves、sode、pauldrons |
| Gloves | gloves、mitts |
| Legs | legs、leggings、kilt、skirt |

完全な**スーツ**とは、各スロットに1部位ずつのことです。抵抗値はスロットをまたいで*加算*される
ため、控えめな素材の完全なスーツは、単体で装備した重量級の胸当て1枚を容易に上回る抵抗値を
持ちます。chest が最も多くの防御値に寄与しますが (そのスカラーが最大 — 後述)、空いた
スロットはすべて、あなたが取りこぼしている抵抗値です。

ServUO は各スロットの AOS 以前の防御値寄与を固定の表 (`BaseArmor.ArmorScalars`) でスケール
します: Gorget `0.07`、Gloves `0.07`、Helmet `0.14`、Arms `0.15`、Legs `0.22`、Chest `0.35`。
chest はスーツの防御値のおよそ半分です。

### 旧 Armor Rating についての注記

AOS 以前、防具は5つの抵抗値ではなく単一の **Armor Rating (AR)** 数値を用いていました。
当シャードは AOS/EJ ルールで動作するため、プレイ上は抵抗値が重要ですが、根底にある
`ArmorBase` 値 (下の表の `ar=` 列) は今も AOS 以前の防御値と meditation ペナルティ計算に
供給されています。これが、高 AR の plate 部位が低 AR の leather 部位よりマナ回復を厳しく
罰する理由です。

## 素材

素材は柔らかい cloth や leather から金属の mail や plate を経て、エキゾチックな dragon scale や
ガーゴイルの stone まで幅広く揃います。下表の各行は、その**素材の chest 部位の基礎抵抗
プロファイル**で、必要筋力、基礎防御値、meditation 許容度を、部位ごとのソースから直接
取得したものです。同素材の他スロットは抵抗プロファイルを共有しますが、より低い必要筋力と
防御値を持ちます。

| | 素材 | Phys | Fire | Cold | Poison | Energy | 筋力 (chest) | AR | Med 可否 | 製作元 |
|---|---|---|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x13CC.png" class="uo-sprite" alt="" width="48" /> | **Leather** | 2 | 4 | 3 | 3 | 3 | 25 | 13 | **All** | [Tailoring](/ja/crafting/tailoring/) |
| <img src="/img/items/0x13DB.png" class="uo-sprite" alt="" width="48" /> | **Studded** | 2 | 4 | 3 | 3 | 4 | 35 | 16 | Half | [Tailoring](/ja/crafting/tailoring/) |
| <img src="/img/items/0x144F.png" class="uo-sprite" alt="" width="48" /> | **Bone** | 3 | 3 | 4 | 2 | 4 | 60 | 30 | None | [Tailoring](/ja/crafting/tailoring/) |
| <img src="/img/items/0x13EC.png" class="uo-sprite" alt="" width="48" /> | **Ringmail** | 3 | 3 | 1 | 5 | 3 | 40 | 22 | None | [Blacksmithy](/ja/crafting/blacksmithy/) |
| <img src="/img/items/0x13BF.png" class="uo-sprite" alt="" width="48" /> | **Chainmail** | 4 | 4 | 4 | 1 | 2 | 60 | 28 | None | [Blacksmithy](/ja/crafting/blacksmithy/) |
| <img src="/img/items/0x1415.png" class="uo-sprite" alt="" width="48" /> | **Plate** | 5 | 3 | 2 | 3 | 2 | 95 | 40 | None | [Blacksmithy](/ja/crafting/blacksmithy/) |
| <img src="/img/items/0x2641.png" class="uo-sprite" alt="" width="48" /> | **Dragon scale** | 3 | 3 | 3 | 3 | 3 | 75 | 40 | None | [Blacksmithy](/ja/crafting/blacksmithy/) |
| <img src="/img/items/0x2B67.png" class="uo-sprite" alt="" width="48" /> | **Woodland** | 5 | 3 | 2 | 3 | 2 | 95 | 40 | None | [Tailoring](/ja/crafting/tailoring/) |
| <img src="/img/items/0x0286.png" class="uo-sprite" alt="" width="48" /> | **Stone (gargish)** | 6 | 6 | 4 | 8 | 6 | 40 | — | None | [Tailoring](/ja/crafting/tailoring/) |

*ソース: `Scripts/Items/Equipment/Armor/*.cs`、素材ごとの chest 部位。数値は素材・品質・魔法
ボーナス適用前の基礎抵抗値です。*

表の読み方:

- **Cloth** は技術的には最も軽い「防具」ですが、標準的な cloth は衣類レイヤー (BaseArmor では
  なく BaseClothing) に属し、それ自体ではほとんど何も寄与しません — メイジにとっての価値は、
  完全に med 可能で染色可能な点です。ガーゴイルの「cloth」防具部位は特殊例で、見た目は cloth
  ですがソース上は機械的に **Leather** 素材です。
- **Leather** はメイジとアーチャーの友です: 完全に **med 可能** (マナ回復ペナルティなし)、最も
  低い必要筋力、バランスの取れた低抵抗値。Barbed/horned/spined の革 (後述) はその抵抗値を
  大きく押し上げます。
- **Studded** はマナ回復の半分と引き換えに、わずかに優れた物理/エナジーのカバー範囲を得ます。
- **Bone** は (骨から製作する) 仕立て中量防具で、均等な中域の抵抗値とそれなりの筋力コストを
  持ちます。
- **Ringmail → Chainmail → Plate** は鍛冶の金属系統です: 防御値と必要筋力が上昇し、meditation は
  不可。Plate は戦士の標準 — 最高の基礎物理と防御値を持ちます。
- **Dragon scale** はエキゾチックな例外です。基礎抵抗値は一律 **3/3/3/3/3** ですが、scale
  防具の魅力は、上に重ねる**色付き dragon scale** が付与する高抵抗値と、均等な広がりにあります
  — 突かれる弱点属性がありません。
- **Woodland** (エルフ) は plate のプロファイルを映しますが、木/革から**仕立て**られます。
- **Stone** はガーゴイルの重量級です: このリストで最高の基礎抵抗値 (特に高い poison 抵抗) を
  持ち、エンドゲーム素材としての地位を反映しています。

### 製作と革

- **Tailoring** は leather、studded、bone、woodland、gargish 防具を製作します。leather 系統は
  使用する革に応じてスケールします: 通常の leather → **spined** → **horned** → **barbed** で、
  それぞれが異なる `ArmorMaterialType` であり、抵抗値と防御値が段階的に向上します。
  [Tailoring](/ja/crafting/tailoring/) と [Resources](/ja/items/resources/) を参照してください。
- **Blacksmithy** は ringmail、chainmail、plate、dragon-scale 防具を鍛造します。使用する鉱石
  (dull copper → valorite) は抵抗値と防御値のボーナス、そして色付きの**色相 (hue)** を加えます。

## 盾

盾は逆手 (両手) スロットを占め、[Parrying](/ja/skills/parrying/) スキルが統括します。これは
**入ってくる近接または遠隔の命中を丸ごと受け流す**チャンスを与えます。ブロック率は Parrying
スキルと装備した盾に応じてスケールします — 重い盾ほど多くブロックしますが、重く、より多くの
Strength を要求します。

盾の種類は、軽い **buckler** から wooden や bronze の盾を経て、**heavy metal** や **kite** の盾
まで、加えて order/chaos やガーゴイルの変種まで揃います。すべての金属盾は既定で **Plate** 素材で、
plate 防具と同様に **med 不可**とされます — ただし AOS/EJ ルールでは盾は meditation/マナ
ペナルティに加算され**ません** (6つの装備スロットのみが加算され、`RegenRates.GetArmorOffset` は
AOS 下で盾をスキップします)。受け流したいメイジは、それでも詠唱を維持するために
**Spell Channeling** の盾を好むでしょう。

すべての盾をアート付きで [盾カタログ](/ja/items/catalog/shields/) で閲覧でき、ブロック率の
詳細は [Parrying](/ja/skills/parrying/) を参照してください。

## スーツと戦略

スーツの組み立ては、キャラクターが許容できる防御値とマナ回復のプロファイルの上に、5つの
タイプすべてにわたって **70% 上限の下で抵抗値を最大化する**ことに尽きます。

- **バランス型スーツ** — 1つを尖らせるのではなく、最も低い抵抗値を高めることを狙います。
  モンスターのダメージタイプがどの抵抗値が重要かを決めるため、全体的に 60 台のバランス型
  スーツは、70-physical / 20-energy のスーツより多くの遭遇を生き延びます。抵抗値はスロットを
  またいで加算されるため、部位ごとの数値を追う前に**すべてのスロット**を埋めましょう。
- **メイジの引き換え** — 金属防具は meditation を妨げるため、キャスターは歴史的に全身
  leather/cloth を着て、低い物理抵抗を受け入れてきました。**Mage Armor** プロパティはこの
  ルールを破ります: メイジが高抵抗の med 不可防具 (plate さえも) をマナ回復ペナルティなしで
  着られるようにします。抵抗カバー範囲を、テンプレートの必要筋力とマナ回復と天秤にかけて
  ください — [Meditation とマナ](/ja/playing/meditation-and-mana/) と
  [Seven GM テンプレート](/ja/templates/seven-gm/) の seven-GM メイジビルドを参照してください。
- **素材による色付き防具** — より良い鉱石や革で製作すると抵抗値が上がる*と同時に*防具が
  染色され、その色相が一目で素材を伝えます。Dull copper、shadow iron、copper、bronze、gold、
  agapite、verite、valorite はそれぞれ増加する防御値と独特の色を加えます
  ([色相リファレンス](/ja/reference/hues/) 参照)。熟練クラフターによる exceptional 品質は、
  さらなる耐久と抵抗値を加えます。
- **ガーゴイル & エルフの変種** — ガーゴイルキャラクターは **gargish** の plate/stone/leather
  部位を使い (人間形の helm は着られません)、エルフは **woodland** 防具を使います。これらは
  根底の素材メカニクスを共有しますが種族制限があるため、プレイする種族に合わせてスーツを
  組んでください。

スーツを着る価値あるものにするスキルの訓練については、[Tactics](/ja/skills/tactics/)、
[Parrying](/ja/skills/parrying/)、そして [Seven-GM テンプレート](/ja/templates/seven-gm/) を
参照してください。アートとアイテム ID 付きで個別の部位を閲覧するには、
[防具カタログ](/ja/items/catalog/armor/) と [盾カタログ](/ja/items/catalog/shields/) を
参照してください。
