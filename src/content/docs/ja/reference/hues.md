---
title: 色相（Hue）リファレンス
description: UO の色相値がどう色に対応するか —— hues.mul パレット、注目すべきクラフト資源の色相、そしてなぜ wiki が色相を PNG に焼き込むのか。
status: source-verified
sources:
  - "client: hues.mul"
  - "servuo: Scripts/Misc/ResourceInfo.cs"
last_verified: 2026-06-11
generated: false
---

Ultima Online における**色相（hue）**は、クライアントの `hues.mul` ファイルへの 1 始まりのインデックスだ。
色のついたあらゆるアイテム、クリーチャー、衣類は色相番号を持ち、クライアントはその番号を引いてスプライトを
どう再着色するかを決める。

理解すべき重要な点は、色相が**単一の平坦な色合いではない**ことだ。各色相は 32 段階のグラデーション —— 影から
ハイライトへのランプ —— である。クライアントが色相のついたスプライトを描くとき、スプライト自身のグレースケールの
影→ハイライトのランプをたどり、各グレーレベルを色相のグラデーションの対応する段階へ**再マッピング**する。
ほぼ黒のピクセルは色相の最も暗い段階に、ほぼ白のピクセルは最も明るい段階になる。だからこそ、一枚のグレースケールの
インゴットスプライトが、陰影と奥行きをすべて保ちながら、視覚的に異なる九種類の金属になれるのだ。

この再マッピングはまた、この wiki が CSS の `filter` やカラーオーバーレイを使うのではなく、色相を**直接 PNG に
焼き込む**理由でもある。CSS の色合いは平坦な色を画像全体に乗算して陰影を潰してしまい、32 段階のパレット
再マッピングを再現できない。我々は `hues.mul` からグラデーションを読み出し、クライアントとまったく同じように
スプライトをピクセル単位で再着色する。

（色相 `0` は特別な「色相なし」の値だ —— 「スプライトをそのまま描く」を意味するので、自身のグラデーション
エントリを持たない。）

## 完全なパレット

以下は `hues.mul` のすべての色相を、小さなスウォッチのグリッドとして描いたものだ。各スウォッチは、その色相の
32 段階グラデーションから代表的な中間色を示している。グリッド線は方向の目安として 8 列・8 行ごとに引かれている。
左から右、上から下へ読むと、最初のスウォッチがゲーム色相 `1` だ。

![Grid of all UO hue swatches from hues.mul](/img/hues/chart.png)

*`hues.mul` の全 3000 色相、それぞれ中間色スウォッチ一つずつ（1 行あたり 40 個）。*

## 注目すべき色相

これらは [ServUO の `ResourceInfo.cs`](https://github.com/ServUO/ServUO) で定義されたクラフト資源の色相だ ——
クラフトシステムが金属、レザー、ドラゴンスケール、木材に適用する色である。各スウォッチは 32 段階の完全な
グラデーションを示している（上が影、下がハイライト）。

### 金属

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x0973.png" class="uo-sprite" alt="Dull Copper hue ramp" width="48" height="48" /> | `0x0973` | 2419 | Dull Copper |
| <img src="/img/hues/h-0x0966.png" class="uo-sprite" alt="Shadow Iron hue ramp" width="48" height="48" /> | `0x0966` | 2406 | Shadow Iron |
| <img src="/img/hues/h-0x096D.png" class="uo-sprite" alt="Copper hue ramp" width="48" height="48" /> | `0x096D` | 2413 | Copper |
| <img src="/img/hues/h-0x0972.png" class="uo-sprite" alt="Bronze hue ramp" width="48" height="48" /> | `0x0972` | 2418 | Bronze |
| <img src="/img/hues/h-0x08A5.png" class="uo-sprite" alt="Gold hue ramp" width="48" height="48" /> | `0x08A5` | 2213 | Gold |
| <img src="/img/hues/h-0x0979.png" class="uo-sprite" alt="Agapite hue ramp" width="48" height="48" /> | `0x0979` | 2425 | Agapite |
| <img src="/img/hues/h-0x089F.png" class="uo-sprite" alt="Verite hue ramp" width="48" height="48" /> | `0x089F` | 2207 | Verite |
| <img src="/img/hues/h-0x08AB.png" class="uo-sprite" alt="Valorite hue ramp" width="48" height="48" /> | `0x08AB` | 2219 | Valorite |

### レザー

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x0283.png" class="uo-sprite" alt="Spined leather hue ramp" width="48" height="48" /> | `0x0283` | 643 | Spined |
| <img src="/img/hues/h-0x0227.png" class="uo-sprite" alt="Horned leather hue ramp" width="48" height="48" /> | `0x0227` | 551 | Horned |
| <img src="/img/hues/h-0x01C1.png" class="uo-sprite" alt="Barbed leather hue ramp" width="48" height="48" /> | `0x01C1` | 449 | Barbed |

### ドラゴンスケール

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x066D.png" class="uo-sprite" alt="Red Scales hue ramp" width="48" height="48" /> | `0x066D` | 1645 | Red Scales |
| <img src="/img/hues/h-0x08A8.png" class="uo-sprite" alt="Yellow Scales hue ramp" width="48" height="48" /> | `0x08A8` | 2216 | Yellow Scales |
| <img src="/img/hues/h-0x0455.png" class="uo-sprite" alt="Black Scales hue ramp" width="48" height="48" /> | `0x0455` | 1109 | Black Scales |
| <img src="/img/hues/h-0x0851.png" class="uo-sprite" alt="Green Scales hue ramp" width="48" height="48" /> | `0x0851` | 2129 | Green Scales |
| <img src="/img/hues/h-0x08FD.png" class="uo-sprite" alt="White Scales hue ramp" width="48" height="48" /> | `0x08FD` | 2301 | White Scales |
| <img src="/img/hues/h-0x08B0.png" class="uo-sprite" alt="Blue Scales hue ramp" width="48" height="48" /> | `0x08B0` | 2224 | Blue Scales |

### 木材

| Swatch | Hue (hex) | Hue (dec) | Name |
| --- | --- | --- | --- |
| <img src="/img/hues/h-0x07DA.png" class="uo-sprite" alt="Oak hue ramp" width="48" height="48" /> | `0x07DA` | 2010 | Oak |
| <img src="/img/hues/h-0x04A7.png" class="uo-sprite" alt="Ash hue ramp" width="48" height="48" /> | `0x04A7` | 1191 | Ash |
| <img src="/img/hues/h-0x04A8.png" class="uo-sprite" alt="Yew hue ramp" width="48" height="48" /> | `0x04A8` | 1192 | Yew |
| <img src="/img/hues/h-0x04A9.png" class="uo-sprite" alt="Heartwood hue ramp" width="48" height="48" /> | `0x04A9` | 1193 | Heartwood |
| <img src="/img/hues/h-0x04AA.png" class="uo-sprite" alt="Bloodwood hue ramp" width="48" height="48" /> | `0x04AA` | 1194 | Bloodwood |
| <img src="/img/hues/h-0x047F.png" class="uo-sprite" alt="Frostwood hue ramp" width="48" height="48" /> | `0x047F` | 1151 | Frostwood |

## 同じスプライト、すべての金属

すべてのインゴットの色は**同じ**グレースケールアート（アイテム `0x1BF2`）を使う。変わるのは色相だけだ。以下は
その一枚のスプライトを九回描いたものだ —— 素の Iron に八つの色つき金属を加えて —— 再マッピングがいかに一枚の
アートを九種類の異なるインゴットに変えるかを示している。

<img src="/img/items/0x1BF2.png" class="uo-sprite" alt="Iron ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0973.png" class="uo-sprite" alt="Dull Copper ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0966.png" class="uo-sprite" alt="Shadow Iron ingot" width="44" height="44" />
<img src="/img/hues/demo-0x096D.png" class="uo-sprite" alt="Copper ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0972.png" class="uo-sprite" alt="Bronze ingot" width="44" height="44" />
<img src="/img/hues/demo-0x08A5.png" class="uo-sprite" alt="Gold ingot" width="44" height="44" />
<img src="/img/hues/demo-0x0979.png" class="uo-sprite" alt="Agapite ingot" width="44" height="44" />
<img src="/img/hues/demo-0x089F.png" class="uo-sprite" alt="Verite ingot" width="44" height="44" />
<img src="/img/hues/demo-0x08AB.png" class="uo-sprite" alt="Valorite ingot" width="44" height="44" />

*Iron、Dull Copper、Shadow Iron、Copper、Bronze、Gold、Agapite、Verite、Valorite —— 一枚のスプライト、九つの色相。*

これらの資源がどこから来てどう使われるかを見るには、[資源採集ガイド](/ja/items/resources/)と
[資源アイテムカタログ](/ja/items/catalog/resources/)を訪れてほしい。
