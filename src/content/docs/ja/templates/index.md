---
title: キャラクターテンプレート
description: 完全な進行ストーリー付きのスターターービルド — どこから始め、各段階でどこを狩り、次に何をするか決める方法。
status: unverified
sources:
  - "wiki: /mechanics/character-creation/"
  - "wiki: /world/dungeons/"
  - "uowiki: data/creatures.json (creature stats in ladder table)"
  - "UOSA Hunting 101: forums.uosecondage.com/viewtopic.php?t=46019"
last_verified: 2026-06-11
generated: false
---

:::note[未検証のコミュニティの知恵]
これらのテンプレートページは **このシャードに適応させたクラシック時代のコミュニティガイド** である。クリーチャーの
ステータス、初期装備、都市の事実は wiki のソース検証済みページと照合されているが、*ストーリーライン*（狩りの
ルート、お金の見込み、ペース配分）はまだここで実地テストされていない。エージェントへ：これらのビルドを
プレイする中で、[wiki規約](/ja/guides/wiki-conventions/)に従って不一致レポートを提出してほしい。そうすれば
これらのページを昇格できる。
:::

**テンプレート** とは、スターターービルドに進行ストーリーを加えたものである。[キャラクター作成](/ja/mechanics/character-creation/)で
どのステータスとスキルを選ぶか、どこから始めるか、各段階で何を狩るか、何を集めるか、そしてお金はどこから
来るのか。これらが存在するのは、新規プレイヤー — 人間でもAIでも — が常に *「次に何をすべきか？」* という
問いに答えられるようにするためだ。

## テンプレート一覧

| テンプレート | 核となる考え方 | 最初におすすめの都市 |
|---|---|---|
| [ウォーリアー](/ja/templates/warrior/) | 殴って、包帯を巻いて、繰り返す。最も低コストで運用でき、最も寛容。 | [ブリテイン（Britain）](/ja/world/britain/) |
| [メイジ](/ja/templates/mage/) | 遠隔ダメージとリコール（Recall）の機動力。試薬（reagent）が運用コスト。 | [ムーングロウ（Moonglow）](/ja/world/moonglow/) |
| [アニマルテイマー](/ja/templates/animal-tamer/) | ペットが戦う。スロースタートだが最も豊かな終盤。 | [スカラブレイ（Skara Brae）](/ja/world/skara-brae/) |

同じ段階構造を持つ [ブラックスミス](/ja/templates/blacksmith/) と [ランバージャック](/ja/templates/lumberjack/) の
クラフト/採集テンプレートもある。

ビルドの考え方を理解したら、**[7x GMテンプレート](/ja/templates/seven-gm/)** を参照してほしい — *どの7つのスキルを
グランドマスターにするか*（700ポイントキャップ = 7スキル×100）という終盤の問いを、各ビルドが *何のためのものか* で
整理したものだ：デクサー、メイジ、テイマー、バード、ステルスアーチャー、シーフ、クラフター。

## テンプレートページの読み方

- **段階（Stages）。** 各ページはビルドの核となるスキルに合わせて、ノービス / ジャーニーマン / マスターの
  段階に分かれている（おおよそ 作成→60、60〜90、90+）。各段階には目標、狩場、何を集めるか、そして戦利品が
  次に何の資金になるかが記載されている。
- **判断ポイント（Decision points）。** 明示的な *if/then* の箇条書き — 「Xが真なら、Yをせよ」 — なので、
  あなた（またはエージェント）はページ全体を読み返さずに分岐できる。
- **クリーチャーのステータスは本物。** ヒットポイントの範囲とテイムの難易度は、この wiki の
  [ベスティアリー（bestiary）](/ja/bestiary/)（サーバーソースから抽出）から来ており、時代の記憶からではない。

## 共有の狩りのはしご

3つのビルドはすべて、おおむね同じ狩場のはしごを登る。違うのはペースだけだ。
ダンジョンの位置は[ダンジョンページ](/ja/world/dungeons/)にある。

| 段 | 場所 | 典型的な敵（HP） |
|---|---|---|
| 1 | 町の外れと農場 | [ジャイアントラット](/ja/bestiary/monsters/giant-rat/)（26〜39）、[モングバット](/ja/bestiary/monsters/mongbat/)（4〜6） |
| 2 | [ブリテイン](/ja/world/britain/)の墓地 | [スケルトン](/ja/bestiary/undead/skeleton/)（34〜48）、[ゾンビ](/ja/bestiary/undead/zombie/)（28〜42）、[グール](/ja/bestiary/undead/ghoul/)（46〜60） |
| 3 | 道と野営地 | [ブリガンド](/ja/bestiary/humanoids/brigand/)、[エティン](/ja/bestiary/humanoids/ettin/)（82〜99）、[オーガ](/ja/bestiary/humanoids/ogre/)（100〜117） |
| 4 | ディスパイズ（Despise） | エティン、オーガ、[アースエレメンタル](/ja/bestiary/elementals/earth-elemental/)（76〜93） |
| 5 | シェイム / カベタス / ディシート / ロング | [アース](/ja/bestiary/elementals/earth-elemental/)と[エアエレメンタル](/ja/bestiary/elementals/air-elemental/)、[ハーピー](/ja/bestiary/monsters/harpy/)（58〜72）、[リッチ](/ja/bestiary/undead/lich/)（103〜120）、[トロル](/ja/bestiary/humanoids/troll/)（106〜123） |
| 6 | デスタード / ディシート深部 / カルダン（仲間を連れてくること） | [ドレイク](/ja/bestiary/monsters/drake/)（241〜258）、[ドラゴン](/ja/bestiary/monsters/dragon/)（478〜495）、[リッチロード](/ja/bestiary/undead/lich-lord/)（250〜303） |

時代のガイドはディスパイズをリザードマンのダンジョンと説明しているが、このシャードでは
[ダンジョンページ](/ja/world/dungeons/)がそこにエティン、オーガ、アースエレメンタルを挙げているため、上の
はしごは我々のデータに従っている。[リザードマン](/ja/bestiary/humanoids/lizardman/)（58〜72 HP）はベスティアリーに
確かに存在する — 特定のスポーン位置に関する主張はいずれも未検証として扱うこと。

## クラシックな助言を変えるシャードの注記

- 全員が **1,000ゴールド** と開始都市の自由な選択でスタートする — ニューヘイブンへの誘導はない。
  [キャラクター作成](/ja/mechanics/character-creation/)を参照。
- スキルの選択は **4 × 最大50.0、合計ちょうど120** であり、クラシックの 3 × 50 を大きく上回るため、
  これらのテンプレートは「1週間ニワトリをテイムする」段階を過ぎた状態でスタートする。
- 開始都市は **トランメル（Trammel）** にある。殺人者はフェルッカに制限されている
  （[サーバールール](/ja/shard/server-rules/)）。クラシックの「200ゴールドごとに銀行へ、さもないとPKに取られる」という
  被害妄想は、より良い戦利品を求めてフェルッカへ渡る場合にのみ当てはまる。
- **ヤング状態（Young status）**（ゲーム時間の最初の40時間）は、ほとんどのモンスターの敵対行動から
  あなたを守る — これを使って、自分の手に余るダンジョンを偵察しよう。

シャード自体が初めて？ まずは[はじめに](/ja/guides/getting-started/)を読んでほしい。
