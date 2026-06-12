---
title: "テンプレート: ランバージャック"
description: 木こり+弓細工の入門ビルドで、完全な進行ストーリー付き — 作成の選択、弓の稼ぎループ、トレーニング表、判断ポイントを、このシャードの実際のクラフト数値で。
status: unverified
sources:
  - "external: UOSA money-making guide (forums.uosecondage.com/viewtopic.php?t=45914)"
  - "external: Seth's Easy Lumberjacking Guide (forums.uosecondage.com/viewtopic.php?t=37138)"
  - "external: uoguide.com/Lumberjacking (axe damage bonus)"
  - "wiki: /crafting/bowfletching/, /crafting/carpentry/, /crafting/tinkering/, /skills/lumberjacking/, /items/resources/, /mechanics/character-creation/"
  - "servuo: Scripts/Misc/CharacterCreation.cs (Fletching starter kit)"
  - "servuo: Scripts/VendorInfo/SBRangedWeapon.cs, SBCarpenter.cs (NPC prices)"
  - "servuo: Scripts/Mobiles/NPCs/Bowyer.cs + Scripts/Services/BulkOrders/BulkOrderSystem.cs (fletching BODs)"
last_verified: 2026-06-11
generated: false
---

> **ステータス: 未検証。** このストーリーは古典時代のコミュニティの知恵を我々のシャード(shard)向けに調整したものです。以下のスキル範囲とNPC価格はサーバーソースと照合済みですが、ペース配分と稼ぎの見積もりは実プレイによる実地検証待ちです。

ランバージャックは古典的なノーリスクの入門キャラです: 木はタダ、斧は安く、切るボードはどれも金かスキルのどちらかです。最終目標: **GM Lumberjacking + GM Fletching**、**初めての家の軍資金**を賄うボード&弓のパイプライン — そして、いつか戦いたくなったら、[木こりは斧でこっそり+ダメージ](/ja/skills/lumberjacking/)です(GMで最大約+30%)ので、このキャラは他のどのクラフターよりうまく斧ウォリアーに転向します。

## このシャードでのキャラクター作成

[作成ルール](/ja/mechanics/character-creation/)に従って(ステータスポイント90、スキル4つ×最大50、合計120):

| 選択 | 選ぶもの | 理由 |
|---|---|---|
| ステータス | **STR 60 / DEX 15 / INT 15** | STR = 積載量 = 1回の遠征あたりのボード数。丸太はボードの倍重い — STRと下記のボードのルールが物流ゲームのすべてです。 |
| スキル | **Lumberjacking 50、Fletching 50、Carpentry 20** | カスタムテンプレート。Carpentry 20は後の樽/家具の副業の種です。 |
| 都市 | **[Yew(ユー)](/ja/world/yew/)** | 街そのもの*が*森で、弓職人、大工、そして — そう — **Empath Abbeyの銀行**(652, 820)があります。 |

初期装備(`Scripts/Misc/CharacterCreation.cs`で検証済み): Lumberjackingは**手斧**を付与。Fletchingは**ボード14枚、羽根5枚、シャフト5本**を付与。Carpentryは**のこぎり、ボード10枚、半エプロン**を付与。予備の手斧はどの武器鍛冶屋でも約25 gp。開始時の金貨1,000は、予備に加え、より大きな収穫が欲しければ**パックホース(631 gp)**も余裕で賄えます。

**バリアント:** Carpentryを**Tinkering**と交換して手斧を自作する — ただし我々の[ティンカリング表](/ja/crafting/tinkering/)は手斧を**30〜80スキル**に置いているので、Tinkering 20では作れません。Tinkering 50から始めることになり、Fletchingのポイントを削ることになります。純粋な金/クラフトのスタートには、Carpentry 20のほうがすっきりした選択です。

## 唯一重要なルール

**丸太は常にその場でボードに切ること**(丸太に斧を使う)。ボードは重さが半分で、どのレシピも受け付け、NPCの大工は**ボード1枚2 gp 対 丸太1本1 gp**を払います(`Scripts/VendorInfo/SBCarpenter.cs`)。ボード切りには、その木材のレベルでのCarpentry*または*Lumberjackingが必要です([表](/ja/items/resources/)) — あなたのLumberjackingは、あなたが切れるものには常に資格があります。

## ステージ1 — 初心者(Lumberjacking 50→65、Fletching 50→70)

**目標:** 弓のループ。Yewの森で切り、ボードに切り、我々の[弓細工表](/ja/crafting/bowfletching/)に従って**弓(30〜70スキル、7ボード)**をクラフトし、NPCの弓職人に売り、Empath Abbeyで銀行へ。

- Fletching 50では弓はコイントス、70では確実になります。1回切るごとに**丸太10本**が産まれ([木こり](/ja/skills/lumberjacking/))、すなわち約1.4本の弓になります。
- **NPCの弓職人は弓1本につき17 gp**を払います(エクセプショナル21 gp、`SBRangedWeapon.cs` + `GenericSell.cs`) — 当時のガイドの約30 gpではありません。これは弓を通すとボード1枚あたり約2.4 gp 対 生で2 gpなので、ステージ1の弓は大半が*スキル*で、金は副産物です。
- **当てはまらない当時の助言:** ここには時給ごとの買い戻し減衰はありません。武器の売値は固定の表価格です — 弓のために6軒の弓職人を巡る必要はありません。(ボードのようなスタック品は下落します — 交易ループ参照。)
- こまめに銀行へ。あなたはTrammelで始まり、レッドはFelucca限定なので、Yewの木こりを殺す唯一のものは、街の南のダンジョン近くでの過信です。

## ステージ2 — 一人前(Lumberjacking 65→90、Fletching 70→90)

- **Fletching約70でクロスボウへ切り替え**: 我々のウィンドウは**60〜100**(7ボード)で、**25 gp**で売れます — ボード1枚あたり約3.6 gp、弓細工の本で最良のNPCレートです。当時のガイドはクロスボウを約68と言いましたが、ここではGMまで*ずっと上昇*します。
- Lumberjacking 65で**オーク**が開き(鉱脈の30%)、80で**アッシュ**が開きます — 色付きボードはプレイヤー市場の品です([木材表](/ja/items/resources/))。
- **Fletching BODはこのシャードに存在します**(古典時代にはなかった): どのNPC弓職人も6時間ごとに1つ、最大2つまで貯められる形で提供します、Fletchingのスキルがいくらかあれば(`Scripts/Mobiles/NPCs/Bowyer.cs`、`BulkOrderSystem.cs`)。売りに行くたびに集めましょう。
- **羽根を回収**(鳥、ハーピー)し、余った端材を**矢(0〜40スキル)**に変えましょう。NPCは矢1本につき1 gpしか払わないので、当時の「矢の稼ぎ」はここではプレイヤー市場です — 矢はベンダーではなくフォーラムの取引掲示板でアーチャーに大量に売りましょう。
- 任意: Carpentry 20→58を鍛え(スタッフ 0〜25、樽の蓋 11〜36)、**樽(57.8〜82.8)**の副業へ — 樽には**樽のたが、ティンカーのレシピ**も必要なことに注意([大工表](/ja/crafting/carpentry/)、[ティンカリング](/ja/crafting/tinkering/))ので、それらを買う予算を取りましょう。

## ステージ3 — 達人(Lumberjacking 90→GM、Fletching 90→GM)

- **ヘビークロスボウ(80〜120、10ボード)**が約90以降の上昇アイテムです — Fletching 95でクロスボウは87%成功(上昇が遅い)、一方ヘビーは約37%付近に座ります。27 gpで売れ、クロスボウより*悪い*ボードあたりgp — ヘビーはスキルのため、クロスボウは金のためにクラフトしましょう。
- Lumberjacking 95で**ユーウッド**が開き、100でハートウッド/ブラッドウッド/フロストウッドに加えボーナスリソース(樹皮の欠片、琥珀)が開きます — すべてプレイヤー市場であり、すべてクラフターがあなたを求める理由です。
- 斧のボーナスはあなたと共にひそかに成熟しました: 斧と多少の[Swordsmanship(剣術)](/ja/skills/swordsmanship/)を持つGM木こりは、れっきとしたハンターです — 純粋なクラフトから抜け出すリスペックなしの道の一つです。

## 交易ループ

| 行動 | 場所 | 価格(ソース照合済み) |
|---|---|---|
| 弓 / クロスボウ / ヘビーを売る | NPCの弓職人 | 17 / 25 / 27 gp固定、エクセプショナルは+25%。武器に価格下落なし |
| 普通のボードを大量に売る | NPCの大工 | 各2 gp。棚価格は1軒のベンダーが吸収する1,000ユニットごとに約1 gp下がる(`GenericBuy.cs`) — 大量放出はYew → Britain → Vesperとローテーション |
| ボードをプレイヤーに売る | フォーラムの取引掲示板 | 2〜3 gp — NPCの3 gp棚価格を下回れば勝ち。当時の「プレイヤーに4 gp」はここでは行き過ぎ |
| 色付きボード、矢、羽根、樽を売る | プレイヤーのみ | NPCはゴミレートしか払わない(矢/羽根1 gp)。これらは関係性の品 |
| 手斧を買う | NPCの武器鍛冶屋 | 約25 gp。2本携帯を — 街から森一つ離れて斧が折れると遠征が無駄になる |
| Fletching BOD | どのNPC弓職人でも | 6時間ごとに無料、2つキャッシュ。報酬はNPCの在庫を上回る |

## 判断ポイント & よくある失敗(エージェント向け)

- **パックがすぐ一杯になるなら** → 丸太を運んでいます。木の前で毎回ボードに切りましょう。それでも速すぎるなら、STRを上げる(切りながら鍛えられます)かパックホースを買いましょう。
- **弓の成功率が約80%以上なら** → 上昇が鈍りました。上げましょう: 弓 → クロスボウ(約70) → ヘビークロスボウ(約90)、[実際のウィンドウ](/ja/crafting/bowfletching/)に従って。
- **1回の遠征あたりの金がスキルより重要なら** → クロスボウが上限(3.6 gp/ボード)。Fletching 60未満なら、生のボード2 gpが下手な弓ロールに勝ります。
- **あるベンダーがボードに1 gpを払い始めたら** → 約1,000+を食わせました。街をローテーションするかプレイヤー市場へ。弓にはこの問題はありません。
- **オークを期待した木が普通の丸太を出したら** → Lumberjackingが65未満です。鉱脈ロールは木ごとのバンク単位なので、後で戻ってきましょう([表](/ja/skills/lumberjacking/))。
- **樽が欲しいなら** → まずCarpentry ≥ 約58を確認し、*かつ*ティンカーから樽のたがを手配しましょう。スタッフと蓋だけでは組み立てられません。
- **戦闘へ流れ始めたら** → 斧を保持しましょう。ダメージボーナスは本物で、すでに支払い済みです。リロールするのではなくSwordsmanship/Tacticsを足しましょう。
- **AFKマクロを当てにしないこと** — 古典ガイドはそれを#1のBANの磁石と呼びます。このシャードの[明文規定](/ja/shard/server-rules/)は設定のみで、これに触れていないので、許容されると決めつける前にフォーラムで尋ねましょう。

## 関連

- [Lumberjackingスキル](/ja/skills/lumberjacking/) · [弓細工](/ja/crafting/bowfletching/) ·
  [大工](/ja/crafting/carpentry/) · [リソース](/ja/items/resources/) · [Yew](/ja/world/yew/)
- [テンプレート: ブラックスミス](/ja/templates/blacksmith/) — 同じ発想だが、岩で
