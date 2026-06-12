---
title: 資源
description: 採集の収量とスキル要件 — 鉱石とインゴット、丸太と板、革、そして cloth。
status: source-verified
sources:
  - "servuo: Scripts/Services/Harvest/Mining.cs"
  - "servuo: Scripts/Services/Harvest/Lumberjacking.cs"
  - "servuo: Scripts/Items/Resource/Log.cs"
  - "servuo: Scripts/Misc/ResourceInfo.cs"
last_verified: 2026-06-11
generated: false
---

すべての帝国は、誰かが岩を運ぶことで築かれます。これらは Britannia 経済の原材料で、サーバー
ソースの採集定義から得たスキル数値を添えています。

## 鉱石とインゴット ([Mining](/ja/skills/mining/))

山や洞窟から鉱石を掘り、forge で同じ金属のインゴットに精錬します。スキル要件と鉱脈の希少度は
`Scripts/Services/Harvest/Mining.cs` から、鉱石→インゴットのタイプ対応は
`Scripts/Misc/ResourceInfo.cs` から:

| | 鉱石 → インゴット | 必要 Mining | 鉱脈出現率 | 加工に必要な Smith スキル |
|---|-------------|-----------------|-------------|---------------------|
| <img src="/img/items/0x1BF2.png" class="uo-sprite" alt="" width="56" /> | Iron | 0 | 49.6% | 0 |
| <img src="/img/items/0x1BF2-h0973.png" class="uo-sprite" alt="" width="56" /> | Dull Copper | 65.0 | 11.2% | 65.0 |
| <img src="/img/items/0x1BF2-h0966.png" class="uo-sprite" alt="" width="56" /> | Shadow Iron | 70.0 | 9.8% | 70.0 |
| <img src="/img/items/0x1BF2-h096D.png" class="uo-sprite" alt="" width="56" /> | Copper | 75.0 | 8.4% | 75.0 |
| <img src="/img/items/0x1BF2-h0972.png" class="uo-sprite" alt="" width="56" /> | Bronze | 80.0 | 7.0% | 80.0 |
| <img src="/img/items/0x1BF2-h08A5.png" class="uo-sprite" alt="" width="56" /> | Gold | 85.0 | 5.6% | 85.0 |
| <img src="/img/items/0x1BF2-h0979.png" class="uo-sprite" alt="" width="56" /> | Agapite | 90.0 | 4.2% | 90.0 |
| <img src="/img/items/0x1BF2-h089F.png" class="uo-sprite" alt="" width="56" /> | Verite | 95.0 | 2.8% | 95.0 |
| <img src="/img/items/0x1BF2-h08AB.png" class="uo-sprite" alt="" width="56" /> | Valorite | 99.0 | 1.4% | 99.0 |

Mining はまた、対応する**granite** (石工用)、70+ スキルで **sand** (ガラス吹き用)、そして —
100.0 で — ボーナスとしての希少な宝石や blackrock も産出します。

## 丸太と板 ([Lumberjacking](/ja/skills/lumberjacking/))

木を伐って丸太を得 (1振りにつき 10 本)、斧で丸太を板に切ります。伐採要件は `Lumberjacking.cs`
から。板への裁断は記載スキルで **Carpentry または Lumberjacking** を受け付けます (`Log.cs`):

| 丸太 | 板 | 伐採に必要な Lumberjacking | 鉱脈出現率 | 板に切るのに必要なスキル |
|---|---|---|---|---|
| <img src="/img/items/0x1BD7.png" class="uo-sprite" alt="" width="56" /> | Ordinary | 0 | 49% | 0 |
| <img src="/img/items/0x1BD7-h07DA.png" class="uo-sprite" alt="" width="56" /> | Oak | 65.0 | 30% | 65 |
| <img src="/img/items/0x1BD7-h04A7.png" class="uo-sprite" alt="" width="56" /> | Ash | 80.0 | 10% | 80 |
| <img src="/img/items/0x1BD7-h04A8.png" class="uo-sprite" alt="" width="56" /> | Yew | 95.0 | 5% | 95 |
| <img src="/img/items/0x1BD7-h04A9.png" class="uo-sprite" alt="" width="56" /> | Heartwood | 100.0 | 3% | 100 |
| <img src="/img/items/0x1BD7-h04AA.png" class="uo-sprite" alt="" width="56" /> | Bloodwood | 100.0 | 2% | 100 |
| <img src="/img/items/0x1BD7-h047F.png" class="uo-sprite" alt="" width="56" /> | Frostwood | 100.0 | 1% | 100 |

100.0 でのボーナス伐採: bark fragments、luminescent fungi、switches、parasitic plants、
brilliant amber。

## 革

動物の死体を刃物で皮剥ぎして**hides**を得、scissors で**leather**に切ります。`ResourceInfo.cs`
(`m_AOSLeatherInfo`) によると4種類:

| | 革 | 入手元 |
|---|---------|-----------|
| <img src="/img/items/0x1081.png" class="uo-sprite" alt="" width="56" /> | Normal | 一般的な動物 (牛、鹿など) |
| <img src="/img/items/0x1081-h0283.png" class="uo-sprite" alt="" width="56" /> | Spined | より頑丈な獣 |
| <img src="/img/items/0x1081-h0227.png" class="uo-sprite" alt="" width="56" /> | Horned | 危険なモンスター |
| <img src="/img/items/0x1081-h01C1.png" class="uo-sprite" alt="" width="56" /> | Barbed | 頂点捕食者 (ドラゴンとその同類) |

どの特定の生物がどの革を産出するかは bestiary の領域です — [Bestiary](/ja/bestiary/) を参照して
ください。各革の等級はそれぞれの製作属性束を持ちます (`CraftAttributeInfo`)。

## Cloth — 羊と畑から bolt まで

cloth はスキルで採集するものではなく、糸車と織機を通じて生の繊維から*製造*されます。その連鎖
(`Scripts/Items/Resource/Cotton.cs`、`Wool.cs`、`Flax.cs`、`YarnsAndThreads.cs`、
`BoltOfCloth.cs` より):

| 工程 | 道具 | 産出 |
|---|---|---|
| 生繊維 — <img src="/img/items/0x0DF9.png" class="uo-sprite" alt="" width="56" /> **cotton** (綿花の植物から摘む)、<img src="/img/items/0x0DF8.png" class="uo-sprite" alt="" width="56" /> **wool** (羊を刈る)、または <img src="/img/items/0x1A9C.png" class="uo-sprite" alt="" width="56" /> **flax** (亜麻の植物を収穫) | — | 繊維そのもの |
| 繊維を**紡ぐ** | 糸車 | <img src="/img/items/0x0FA0.png" class="uo-sprite" alt="" width="56" /> **糸/毛糸のスプール** (1回の使用につき 6) |
| 糸を**織る** | 織機 | <img src="/img/items/0x0F95.png" class="uo-sprite" alt="" width="56" /> **bolt of cloth** |
| bolt を**切る** | Scissors | <img src="/img/items/0x1766.png" class="uo-sprite" alt="" width="56" /> **cloth** (1 bolt につき 50) |
| cloth を**切る** | Scissors | <img src="/img/items/0x0E21.png" class="uo-sprite" alt="" width="56" /> **bandages** — [Healing](/ja/skills/healing/) の燃料 |

糸車と織機は tailor の店や多くの家に立っています (両方とも製作可能な家のアドオン)。紡ぎや
織りにスキルチェックはかかりません — 誰でも繊維を cloth まで通せます。スキルが要るのは後で、
tailor が cloth を衣類や防具に変えるときです。

bolt of cloth、wool、cotton を tailor や provisioner のベンダーから単に**購入**して、scissors に
直行することもできます。cloth はどんな染料も受け付けるため、色付きの衣類は別素材ではなく
dye-tub の仕事です — [色相リファレンス](/ja/reference/hues/) を参照してください。

Tailoring は cloth を衣類と軽防具に変えます — [Tailoring](/ja/crafting/tailoring/) と
[衣類カタログ](/ja/items/catalog/clothing/) を参照してください。

## 関連

- [アイテム概要](/ja/items/) · [Blacksmithy](/ja/skills/blacksmithy/) · [Crafting](/ja/crafting/)
- [インタラクティブマップ](https://uomap.vercel.app) — ベンダーと地形を探す
