---
title: 試薬
description: 8つの magery 試薬の購入者向け概要 — 各々が何を支え、どの circle が最も消費し、どこで買うか。
status: source-verified
sources:
  - "servuo: Scripts/Spells/First..Eighth (reagent usage counts, surveyed 2026-06-11)"
  - "anima: data/world_knowledge.yaml (mage_shop city features)"
last_verified: 2026-06-11
generated: false
---

メイジの力は、雑草、灰、蜘蛛の部位を詰めた肩掛け袋に宿ります。これはその買い物ガイドです。
呪文ごとのレシピは [Magic セクション](/ja/magic/) にあります。

## 8つの試薬

使用数は、64 の magery 呪文のうち何個が各試薬を消費するかで、呪文ソース
(`Scripts/Spells/First` から `Eighth`) を調査したものです:

| | 試薬 | 使用する呪文数 | 最も重い circle | 代表的な呪文 |
|---|---------|-----------------|------------------|------------------|
| <img src="/img/items/0x0F86.png" class="uo-sprite" alt="" width="56" /> | Mandrake Root | 35 | 4th, 7th, 8th | Recall, Greater Heal, Gate Travel |
| <img src="/img/items/0x0F7B.png" class="uo-sprite" alt="" width="56" /> | Bloodmoss | 27 | 3rd, 8th | Recall, Teleport, the 8th-circle summons |
| <img src="/img/items/0x0F8C.png" class="uo-sprite" alt="" width="56" /> | Sulfurous Ash | 25 | 7th, 4th | Flamestrike, Gate Travel, Fireball line |
| <img src="/img/items/0x0F8D.png" class="uo-sprite" alt="" width="56" /> | Spider's Silk | 22 | 7th, 8th | Heal, Greater Heal, Flamestrike, summons |
| <img src="/img/items/0x0F84.png" class="uo-sprite" alt="" width="56" /> | Garlic | 20 | 4th, 1st–3rd | Heal, Greater Heal, Cure, protection line |
| <img src="/img/items/0x0F7A.png" class="uo-sprite" alt="" width="56" /> | Black Pearl | 17 | 7th, 5th | Recall, Energy Bolt, Gate Travel |
| <img src="/img/items/0x0F88.png" class="uo-sprite" alt="" width="56" /> | Nightshade | 16 | 5th, 2nd | Energy Bolt, curse/poison line |
| <img src="/img/items/0x0F85.png" class="uo-sprite" alt="" width="56" /> | Ginseng | 11 | 1st, 4th | Heal, Greater Heal, Cure |

表から導かれる購入アドバイス:

- **Mandrake、bloodmoss、black pearl** — 移動魔法 (Recall/Gate) はこれらを絶え間なく燃やします。
  どのメイジも溜め込みます。
- **Garlic、ginseng、spider's silk** — 回復セット。サポートメイジはこれらを真っ先に空にします。
- **Sulfurous ash、spider's silk、black pearl、nightshade** — 戦闘セット (Flamestrike と
  Energy Bolt が主力のダメージ呪文)。

## どこで買うか

mage shop は8つすべてを揃えます。`world_knowledge.yaml` による mage shop のある都市:

- **[Moonglow](/ja/world/moonglow/)** — メイジの都市。島自体に試薬畑がある
- **[Britain](/ja/world/britain/)** — 中心近くに複数の mage ベンダー
- **Nujel'm** — 宮殿都市の mage shop
- **Papua** — 試薬のための Lost Lands の立ち寄り先
- **Wind** — メイジ専用の隠し都市 (入れるならすでに詠唱できる)

正確なベンダーの戸口は [インタラクティブマップ](https://uomap.vercel.app) で見つけてください
(NPC Vendors を切り替えて "Mage" を検索)。ベンダーの在庫は 60 分ごとに更新され、価格は大量
購入に反応します (`Config/Vendors.cfg` — [サーバールール](/ja/shard/server-rules/) 参照)。
そのため試薬の調達は、1つのベンダーを叩き続けるより、2〜3 都市を巡る方が勝ります。

## 注記

- Necromancy は別の試薬セット (bat wings、grave dust など) を使います — [Magic](/ja/magic/)
  セクションで文書化されています。
- 呪文ごとの試薬コストは circle が上がるほど増えます。8th-circle の summon は1回の詠唱で
  4 種類の試薬を食うことがあります。数十ではなく数百単位で在庫してください。

## 関連

- [Magery](/ja/skills/magery/) — circle、詠唱成功率、マナ
- [Magic](/ja/magic/) — 呪文ごとの試薬レシピ
