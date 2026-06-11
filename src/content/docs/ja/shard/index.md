---
title: シャードアイデンティティカード
description: このシャードを一目で — 拡張、スキルとステータスのキャップ、そして主要レートを、サーバー設定から直接。
status: source-verified
sources:
  - "servuo: Config/Expansion.cfg"
  - "servuo: Config/PlayerCaps.cfg"
  - "servuo: Config/General.cfg"
  - "servuo: Config/TestCenter.cfg"
last_verified: 2026-06-11
generated: false
---

:::note[ここでの「ServUO」の意味]
**シャード（shard）** とは、稼働中のウルティマオンラインのゲームワールド（サーバーインスタンス）のことである。この
シャードは **[ServUO](https://www.servuo.com/)** 上で動いている — オープンソースのウルティマオンライン
**サーバーエミュレーター**で、コミュニティが自前のワールドをホストできるようUOサーバーを再実装した
ソフトウェアだ。したがって、この wiki 全体で言う「ServUO」とは、（ルールと数値が定義されている）その
エミュレーターのソースコードを指しており、稼働中のサーバーそのものを指すわけではない。
:::

ひとつのシャード、ひとそろいのルール — これらは、ServUOエミュレーターの設定 `Config/*.cfg` から直接読み取った、
このシャードが実際に稼働している数値である。

## 拡張

| 設定 | 値 | ソース |
|---------|-------|--------|
| 拡張 | **EJ（Endless Journey）** | `Config/Expansion.cfg`（`CurrentExpansion=EJ`） |
| テストセンターモード | 無効 | `Config/TestCenter.cfg`（`Enabled=False`） |

EJはServUOエミュレーターが提供する中で最も現代的なルールセットである。AOSの戦闘計算、ML時代のステータス上昇、SAの種族と
スキルがすべて有効になっている。この wiki が「AOS時代」または「ML時代」の挙動と言う場合、それはここに適用される。

## スキルキャップ（`Config/PlayerCaps.cfg`）

| 設定 | 値 | 備考 |
|---------|-------|-------|
| 個別スキルキャップ | **100.0**（`SkillCap=1000`） | 該当する場合、パワースクロールによってスキルごとに引き上げ可能。 |
| 合計スキルキャップ | **700.0**（`TotalSkillCap=7000`） | キャップに達すると、新たな上昇には別のスキルを下げる設定（矢印ダウン）が必要。 |
| アンチマクロコード | **無効**（`EnableAntiMacro=False`） | 同一地点・同一対象による上昇の抑制はなし。[スキル上昇](/ja/mechanics/skill-gain/)を参照。 |

## ステータスキャップ（`Config/PlayerCaps.cfg`）

| 設定 | 値 |
|---------|-------|
| 合計ステータスキャップ | **225**（`TotalStatCap=225`） |
| 力 / 敏捷 / 知力のキャップ | **各125**（`StrCap`/`DexCap`/`IntCap=125`） |
| ステータスごとの強化最大値 | **各150**（`StrMaxCap`/`DexMaxCap`/`IntMaxCap=150`） |
| ステータス上昇確率 | 条件を満たすスキル使用ごとに **5%**（`PlayerChanceToGainStats=5.0`） |
| ステータス上昇の時間遅延 | **無効**（`EnablePlayerStatTimeDelay=False`） |
| ペットのステータス上昇確率 / 遅延 | 5% / 無効（`PetChanceToGainStats=5.0`、`EnablePetStatTimeDelay=False`） |

これらがどう相互作用するかの詳細：[ステータス上昇メカニクス](/ja/mechanics/stat-gain/)。

## ワールドの挙動（`Config/General.cfg`）

| 設定 | 値 |
|---------|-------|
| 地面のアイテム消滅 | **60分**（`DefaultItemDecayTime=60`） |
| 殺人者（レッド） | **フェルッカ（Felucca）のみ**（`RestrictRedsToFel=True`） |

## さらに

- [サーバールールとレート](/ja/shard/server-rules/) — 住居、戦利品予算、トレジャーマップ、
  ベンダー、セーブと再起動
- [はじめに](/ja/guides/getting-started/) — これがどんなシャードで、誰が暮らしているのか
