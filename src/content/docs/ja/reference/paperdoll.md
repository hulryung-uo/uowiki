---
title: ペーパードール（Paperdoll）
description: キャラクターのペーパードールがどう組み立てられるか —— 裸の身体ガンプに装備ガンプを重ね、スロット順に描画し、アイテムの色相で着色する。
status: source-verified
sources:
  - "client: gumpartLegacyMUL.uop, tiledata.mul"
  - "classicuo: PaperDollInteractable.cs"
last_verified: 2026-06-11
generated: false
---

**ペーパードール（paperdoll）**は、自分をダブルクリックしたときに現れる、キャラクターの頭からつま先までの
肖像だ。これは一枚の画像ではない。クライアントが、裸の身体の絵に装備アイテム一つにつき一枚の絵を加えて、
その場で*合成*する。だから身につけたものは何でも、身につけた姿で表示される。このページはその合成がどう
機能するかを説明し、さまざまな防具と衣類についての結果を示す。

## ペーパードールはどう組み立てられるか

クライアントは固定された手順に従う（ClassicUO の `PaperDollInteractable.cs` と `Game/Constants.cs` で検証済み）。

1. **身体を描く。** 半裸の身体ガンプが最初に左上の角に置かれる。人間男性は ガンプ `0x000C`、人間女性は
   `0x000D`。
2. **各アイテムのガンプを見つける。** すべての装備可能品はクライアントの `tiledata.mul` に **AnimID** を持つ。
   そのペーパードール用の絵は、男性ドールでは id が `AnimID + 50000`、女性ドールでは `AnimID + 60000` の
   ガンプだ。女性専用のガンプが存在しない場合、クライアントは男性用にフォールバックする。
3. **装備を身体の上に重ねる。** 各装備ガンプは同じ左上の角に描かれ —— アート自体がドール上の正しい位置を
   すでに保持している —— 透過で合成される。それらは固定された**レイヤー順**で奥から手前へ描かれる。

   > Cloak, Shirt, Pants, Shoes, Legs, Arms, Torso, Tunic, Ring, Bracelet, Face,
   > Gloves, Skirt, Robe, Waist, Necklace, Hair, Beard, Earrings, Helmet,
   > One-Handed, Two-Handed, Talisman

   この順序こそが、ブレストプレートがその下のレザーを覆い、ヘルメットが髪の上に描かれる理由だ。
4. **色相で着色する。** 防具と衣類のアートはグレースケールだ。アイテムの**色相**が最後に適用され、その
   グレーのランプを[色相パレット](/ja/reference/hues/)を通して再マッピングする。こうして染められたローブや
   色つき金属のスーツが、その色を見せる。

以下の画像はそれらの正確なガンプを合成して生成したものなので、ゲーム内のペーパードールが描画するものと一致する。

## 裸の身体

これらは、すべてのペーパードールが起点とする基礎の身体ガンプだ。アートはグレースケールで、クライアントは
それをキャラクターの**肌の色相**で着色する（ServUO は `RandomSkinHue` の範囲、ゲーム色相 1002〜1058 から一つを
ロールする）。下の図は、ガンプの生のグレーではなく肌として読めるよう、代表的な人間の肌色（色相 1024）で
着色されている。

<img src="/img/paperdoll/body-male.png" width="220" alt="Skin-toned male human body paperdoll (gump 0x000C)" />
<img src="/img/paperdoll/body-female.png" width="220" alt="Skin-toned female human body paperdoll (gump 0x000D)" />

*男性の身体 `0x000C`（左）と女性の身体 `0x000D`（右）、肌の色相 1024 で着色。*

## 素材別の防具

下の各スーツは、肌色の男性の身体に、その素材の標準的なパーツ（胸当て、腕、脚、手袋、ゴーゲット／兜 ——
その素材が持つもの）を重ね、スロット順に描画し、各パーツ自身の色相で着色したものだ。フルセットは
[防具カタログ](/ja/items/catalog/armor/)で閲覧できる。盾には独自の[盾カタログ](/ja/items/catalog/shields/)がある。

### レザー

<img src="/img/paperdoll/suit-leather.png" width="220" alt="Full leather armor worn on a male body" />

*胸当て、腕、脚、手袋、ゴーゲット、キャップ。*

### スタッドレザー

<img src="/img/paperdoll/suit-studded.png" width="220" alt="Full studded leather armor worn on a male body" />

*胸当て、腕、脚、手袋、ゴーゲット。*

### ボーン

<img src="/img/paperdoll/suit-bone.png" width="220" alt="Full bone armor worn on a male body" />

*胸当て、腕、脚、手袋、兜 —— その淡いボーン色で。*

### リングメイル

<img src="/img/paperdoll/suit-ringmail.png" width="220" alt="Full ringmail armor worn on a male body" />

*胸当て、腕、脚、手袋。*

### チェインメイル

<img src="/img/paperdoll/suit-chainmail.png" width="220" alt="Full chainmail armor worn on a male body" />

*胸当て、脚、コイフ。*

### プレートメイル

<img src="/img/paperdoll/suit-plate.png" width="220" alt="Full plate armor worn on a male body" />

*胸当て、腕、脚、手袋、ゴーゲット、兜 —— 古典的なフルプレート。*

### ドラゴンスケール

<img src="/img/paperdoll/suit-dragon.png" width="220" alt="Full dragon-scale armor worn on a male body" />

*胸当て、腕、脚、手袋、兜 —— ドラゴンスケールの焼き込まれた色相を帯びて。*

### ハイド

<img src="/img/paperdoll/suit-hide.png" width="220" alt="Full hide armor worn on a male body" />

*胸当て、肩当て（腕）、ズボン、手袋、ゴーゲット。*

### ウッドランド

<img src="/img/paperdoll/suit-woodland.png" width="220" alt="Full woodland armor worn on a male body" />

*胸当て、腕、脚、手袋、ゴーゲット —— エルフのハートウッドセット。*

### ガーゴイルレザー

<img src="/img/paperdoll/suit-gargish-leather.png" width="220" alt="Full gargish leather armor worn on a male body" />

*胸当て、腕、脚、キルト。*

### ガーゴイルプレート

<img src="/img/paperdoll/suit-gargish-plate.png" width="220" alt="Full gargish plate armor worn on a male body" />

*胸当て、腕、脚、キルト。*

### ガーゴイルストーン

<img src="/img/paperdoll/suit-gargish-stone.png" width="220" alt="Full gargish stone armor worn on a male body" />

*胸当て、腕、脚、キルト —— その彫り出された石の色合いで。*

### サムライプレート

<img src="/img/paperdoll/suit-samurai-plate.png" width="220" alt="Full samurai plate armor worn on a male body" />

*胴（胸当て）、佩楯（腿当て）、臑当（脚当て）、面頬（顔）、そしてプレートの兜。*

### プレートと盾

<img src="/img/paperdoll/suit-shield.png" width="220" alt="Full plate armor with a metal shield worn on a male body" />

*金属の盾を利き手と逆の手に持つフルプレートのスーツ —— 盾は片手レイヤーに描かれる。*

## 衣装

布のパーツは同じ合成を使う —— ここでは素のローブ、ロングパンツ付きの上等なシャツ、そしてローブと帽子の
ウィザードの装いだ。フルレンジは[衣類カタログ](/ja/items/catalog/clothing/)を参照。

<img src="/img/paperdoll/suit-robe.png" width="220" alt="A robe worn on a male body" />
<img src="/img/paperdoll/suit-fancy-shirt-and-pants.png" width="220" alt="A fancy shirt and long pants worn on a male body" />
<img src="/img/paperdoll/suit-wizard.png" width="220" alt="A robe and wizard's hat worn on a male body" />

*ローブ、上等なシャツ＋ロングパンツ、そしてウィザードの装い（ローブ＋ウィザードハット）。*

## 単一の装備アイテム

一度に一つのパーツを見るために、ここでは単一のアイテムを装備した身体を示す。最後の三つは、同じ基礎アートを
異なる[色相](/ja/reference/hues/)で着色したものだ。

<img src="/img/paperdoll/item-plate-chest.png" width="220" alt="A plate chest worn on a male body" />
<img src="/img/paperdoll/item-dragon-helm.png" width="220" alt="A dragon helm worn on a male body" />
<img src="/img/paperdoll/item-bone-chest.png" width="220" alt="A bone chest worn on a male body" />

*プレートの胸当て、ドラゴンの兜、ボーンの胸当て。*

<img src="/img/paperdoll/item-robe-blue.png" width="220" alt="A blue-dyed robe worn on a male body" />
<img src="/img/paperdoll/item-robe-red.png" width="220" alt="A red-dyed robe worn on a male body" />
<img src="/img/paperdoll/item-wizards-hat-green.png" width="220" alt="A green-dyed wizard's hat worn on a male body" />

*同じローブの青と赤、そして緑のウィザードハット —— 一枚のグレースケールガンプが色相を通じてどんな色にも
なる様子を示している。*
