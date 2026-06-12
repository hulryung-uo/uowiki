---
title: ゲームメカニクス
description: メカニクス関連ページの索引 — このシャードで内部的に数値が実際どう動いているか。
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs"
last_verified: 2026-06-11
generated: false
---

ブリタニアはダイス（サイコロ）の上で動いているが、そのダイスは公開されている — このシャードのサーバーソースは
オープンであり、これらのページは実際にどんな出目が振られているかを記録している。

## ページ

- **[スキル上昇](/ja/mechanics/skill-gain/)** — 上昇確率の計算式、保証上昇システム（Guaranteed Gain
  System, GGS）、スキルキャップでの挙動、そしてここでアンチマクロチェックがオフになっている理由。
- **[ステータス上昇](/ja/mechanics/stat-gain/)** — 筋力（STR）、敏捷（DEX）、知力（INT）が
  スキル使用によってどう伸びるか、そして225のステータスキャップに達したときに何が起こるか。

## 関連リファレンス

- [シャードアイデンティティカード](/ja/shard/) — これらのメカニクスが読み取る、設定済みのキャップとレート
- [スキル](/ja/skills/) — スキル一覧表とスキルごとのトレーニングガイド
- [魔法](/ja/magic/) — 呪文のメカニクスは独自のセクションにある

## 検証に関する注記

メカニクスページは、ServUOソース内の正確なファイル（パスは `../servuo` からの相対）を引用しており、主に
`Scripts/Misc/SkillCheck.cs` と `Server/Skills.cs` を参照している。ゲーム内の挙動がここの計算式と
食い違う場合、それはページかサーバーのバグであり、いずれにせよ
[レポートを提出](/ja/guides/wiki-conventions/)してほしい。
