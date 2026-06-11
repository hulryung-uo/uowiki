---
title: スキル上昇
description: このサーバーでスキル上昇が実際にどう機能するか — 上昇確率の計算式、GGSによる確定上昇、上限の挙動、アンチマクロの状態。
status: source-verified
sources:
  - "servuo: Scripts/Misc/SkillCheck.cs"
  - "servuo: Server/Skills.cs (SkillInfo.GainFactor)"
  - "servuo: Config/PlayerCaps.cfg (EnableAntiMacro, caps)"
last_verified: 2026-06-11
generated: false
---

一振り、一掘り、一詠唱のすべてが同じサイコロを振ります。このページは
`Scripts/Misc/SkillCheck.cs` — サーバーが実際に実行しているファイル — のロジックを文書化します。

## 基本的な流れ

スキルを使うと、サーバーは難易度ウィンドウ（`minSkill`〜`maxSkill`、または直接の`chance`）に対して
**スキルチェック**を行います。

- `minSkill`未満：自動的に失敗し、**上昇は不可能**（「難しすぎる」）。
- `maxSkill`以上：自動的に成功し、**上昇は不可能**（「歯ごたえがない」）。
- その間：成功確率 = `(value − minSkill) / (maxSkill − minSkill)`、そして試行が成功したかどうかに
  かかわらず**上昇判定**が発生します。

つまり鍛錬の最適点は、*難しいが可能*な作業です — そして作業が簡単になりすぎると、もう何も
教えてくれなくなります。

## 上昇確率（`CheckSkill` → `GetGainChance`）

適格な使用ごとに、0.1スキル上昇する確率は次のように計算されます：

```
gc = ( (TotalCap − TotalSkills) / TotalCap        // room left under the 700.0 cap
     + (SkillCap − SkillBase) / SkillCap ) / 2    // room left in this skill
gc = ( gc + (1 − difficultyChance) × bonus ) / 2  // harder tasks gain more
gc × = GainFactor                                  // per-skill factor (1.0 for all skills here)
gc = max(gc, 0.01)                                 // never below 1%
```

ここで`bonus`は**成功時に0.5**、**失敗時に0.0**です（post-AOSルール、これはこのEJシャードに
適用されます）。操作中のペットは100%のボーナスを得ます（確率2倍）。結果は100%で上限が
かかります。

実用上の帰結：

- **低いスキルは速く上昇し、高いスキルはゆっくり上昇する** — 合計値と個別スキルの両方が、
  満たされるにつれて`gc`を縮小します。
- **10.0未満のスキルはすべて使用のたびに上昇する**（`skill.Base < 10.0`は判定を回避）。そして
  10.0未満の各上昇はランダムに0.1〜0.4の跳ね上がりです。
- 下限は適格な使用ごとに1%で、99.9スキルでも同様です。

## GGS — 確定上昇システム（Guaranteed Gain System）

GGSは**このシャードで有効**です（`GGSActive = !Siege.SiegeShard`、そしてこれはSiegeシャードでは
ありません）。各スキルは`NextGGSGain`の時刻を追跡しており、そのタイマーが切れた後にスキルを使うと、
ランダム判定に失敗しても**上昇します**。

タイマーの長さは`GGSTable`から来ており、スキルのレベル（5.0スキルごとの行）と合計スキル（列：
合計350.0未満／350.0〜699.9／700.0）でインデックスされます。例（分単位）：

| スキルレベル | 合計 < 350 | 合計 350〜699.9 | 合計 700 |
|------------|------------|-----------------|-----------|
| 0〜4.9 | 1 | 3 | 5 |
| 50〜54.9 | 27 | 72 | 138 |
| 95〜99.9 | 540 | 1440 | 2580 |
| 110〜114.9 | 618 | 1662 | 3060 |

要するに：行き詰まったスキルを使い続ければシステムはいずれ報いてくれます — ただし高スキルでは
その「いずれ」が何日にも延びます。

## スキル上限の挙動

- 個別の上限は**100.0**、合計の上限は**700.0**です
  （`Config/PlayerCaps.cfg`、[シャードカード](/ja/shard/)を参照）。
- スキルは、そのロックが**up**に設定され、かつ上限未満のときにのみ上昇します。
- 合計上限に達した（または近い）とき、`CheckReduceSkill`は**down**に設定したスキルを、上昇した分と
  同じ量だけ下げます。down指定のスキルがなければ上昇もありません。スキルの矢印は意図的に設定して
  ください。
- 牢屋ではスキル上昇は完全に無効化されます。

## 上昇量とアクセラレーター

- 通常の上昇量は**0.1**です（地域の`SkillGain`で修正、通常は×1）。
- スキルへの**俊敏の巻物（Scroll of Alacrity）**：有効中は各上昇が0.2〜0.5になります。
- Mondain's Legacyのクエストスキルボーナス：フラグが立っている間は上昇が×2〜4。

## アンチマクロ：無効

`SkillCheck.cs`には古典的なアンチマクロシステム（フラグの立ったスキルで5分あたり1つの場所／対象に
つき最大3回の上昇）が含まれていますが、それは`PlayerCaps.EnableAntiMacro`がtrueのときにのみ
動作します — そしてこのシャードは**`EnableAntiMacro=False`**です（`Config/PlayerCaps.cfg`）。
サーバーがあなたに気づかないふりをすることなく、一箇所で鍛錬できます。

## 関連

- [ステータス上昇](/ja/mechanics/stat-gain/) — スキル上昇のたびにステータス上昇の判定も行われます
- [スキル一覧](/ja/skills/) — スキルごとの鍛錬ガイド
