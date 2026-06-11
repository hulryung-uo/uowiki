---
title: アイテム
description: アイテムカテゴリの概観 — リソース、触媒、そして残りのアイテム解説がどこにあるか。
status: source-verified
sources:
  - "servuo: Scripts/Misc/ResourceInfo.cs"
last_verified: 2026-06-11
generated: false
---

ブリタニアでバックパックに入るものすべてを整理しました。このセクションでは、キュレーション済みのウィキが直接解説するアイテムカテゴリを扱い、残りを所有するセクションへ案内します。

## このセクションのページ

- **[リソース](/ja/items/resources/)** — 採取の産物：9種の鉱石/インゴットとその採掘要件、7種の木材、革、そして布。
- **[触媒（リエージェント）](/ja/items/reagents/)** — 8種のメイジ用触媒：どこで買えるか、どのサークルがどれを消費するか。
- **[武器](/ja/items/weapons/)** — ダメージ、速度、スキル、スペシャルムーブの仕組みと、全武器系統のステータス表。
- **[防具](/ja/items/armor/)** — 抵抗値、素材（革 → プレート → ドラゴン）、スロット、スーツ、そしてメイジアーマーのトレードオフ。
- **[道具](/ja/items/tools/)** — あらゆる製作・採取道具（ティンカー道具、シャベル、裁縫キット、のこぎり…）、どのスキルに役立つか、どこで手に入るか。

## アイテム全カタログ

**[アイテムカタログ](/ja/items/catalog/)** は、ServUO ソース内の*あらゆる*アイテムを網羅した自動生成・画像豊富なインデックスです — 3,600点超のアイテムを、クライアントアート、アイテムID、重量とともに、**ゲームプレイ上の種別**（系統別の武器、素材別の防具など）で分類し、サブカテゴリでグループ化しています。カテゴリ別に閲覧：

- [武器](/ja/items/catalog/weapons/) — 剣、斧、ポールアーム、メイス、杖、短剣、槍、弓、投擲武器、ワンド。それぞれ鍛えるスキル付き
- [防具](/ja/items/catalog/armor/) — 素材別、布や革からプレート、ドラゴンスケイルまで
- [盾](/ja/items/catalog/shields/) と [装身具](/ja/items/catalog/jewelry/)（指輪、腕輪、首飾り、イヤリング）
- [衣服](/ja/items/catalog/clothing/) — 帽子、ローブ、履物、シャツ、ズボン
- [楽器](/ja/items/catalog/instruments/)、
  [スペルブック & タリスマン](/ja/items/catalog/spellbooks-talismans/)
- [ポーション](/ja/items/catalog/potions/)、[巻物](/ja/items/catalog/scrolls/)、
  [触媒](/ja/items/catalog/reagents/)、[食料 & 飲料](/ja/items/catalog/food-drink/)
- [リソース](/ja/items/catalog/resources/)、[道具](/ja/items/catalog/tools/)、
  [照明](/ja/items/catalog/lighting/)、[容器](/ja/items/catalog/containers/)、
  [書物](/ja/items/catalog/books/)
- [装飾品](/ja/items/catalog/decorations/)、
  [アドオン & 家具](/ja/items/catalog/addons-furniture/)、
  [アーティファクト](/ja/items/catalog/artifacts/)、[機能アイテム](/ja/items/catalog/functional/)、
  [クエストアイテム](/ja/items/catalog/quest-items/)、[その他](/ja/items/catalog/miscellaneous/)

## アイテムカテゴリ一覧

| カテゴリ | 何が入っているか | 解説場所 |
|----------|--------------|---------------|
| 原材料 | 鉱石、インゴット、丸太、板、獣皮、革、布 | [リソース](/ja/items/resources/) |
| 触媒 | 8種のメイジ用触媒（ネクロマンシー用触媒は別枠） | [触媒](/ja/items/reagents/), [魔法](/ja/magic/) |
| 武器 & 防具 | 製作品・ドロップ品の装備、有色金属の装備 | [Blacksmithy](/ja/skills/blacksmithy/), [製作](/ja/crafting/) |
| 消耗品 | 包帯、ポーション、食料、巻物 | [Healing](/ja/skills/healing/), [魔法](/ja/magic/) |
| 道具 | つるはし、シャベル、斧、鍛冶ハンマー、裁縫キット | [スキル](/ja/skills/) 内の各スキルページ |
| 宝物 | 魔法のドロップ品、宝の地図の箱 | ドロップ予算については [サーバールール](/ja/shard/server-rules/) |

## アイテムに影響するシャード固有の事項

- 地面に放置されたアイテムは **60分** で消滅します（`Config/General.cfg`） — 銀行に預けるか、失うかだ。
- ドロップ品質はフェルッカ補正付きの予算システムを使用します — [サーバールール](/ja/shard/server-rules/)を参照。
- ベンダーの在庫は1時間ごとに補充され、価格は需給に応じて変動します
  （`Config/Vendors.cfg`）。
