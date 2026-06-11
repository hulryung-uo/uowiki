---
title: 音声コマンド
description: Ultima Onlineで行動を引き起こす特別な発話フレーズ — 家のコマンド(ロックダウン、セキュア、バン、ゴミ箱)、ペットの命令、銀行員とベンダーのキーワード、その他の発話トリガー — を、正確なフレーズ、効果、どこで言うか、そしてServUOのソースとともに。
status: source-verified
sources:
  - "servuo: Scripts/Regions/HouseRegion.cs (house command keywords + 'I wish to resize my house')"
  - "servuo: Scripts/Mobiles/AI/BaseAI.cs (pet command keywords)"
  - "servuo: Scripts/Mobiles/NPCs/Banker.cs (bank/balance/withdraw/check)"
  - "servuo: Scripts/Mobiles/AI/VendorAI.cs (vendor buy/sell)"
  - "servuo: Scripts/Mobiles/NPCs/AnimalTrainer.cs (stable/claim)"
  - "servuo: Scripts/Mobiles/NPCs/PlayerVendor.cs (player-vendor keywords)"
  - "servuo: Scripts/Misc/Keywords.cs (self-status keywords)"
  - "servuo: Server/Network/PacketHandlers.cs (UnicodeSpeech keyword decode — the localization mechanic)"
  - "data: data/speech_commands.json (extracted by tools/extract_speech.py)"
  - "client: speech.mul (keyword phrases, all languages)"
  - "data: data/speech_languages.json (extracted by tools/extract_speech_langs.py — per-language keyword phrases from speech.mul)"
last_verified: 2026-06-11
generated: false
---

Ultima Onlineの一部のことは、メニューをクリックするのではなく、**フレーズを声に出して言う**
ことで行います — それをスピーチバーに入力すると、サーバーが反応します。椅子をロックダウン
する、トラブルメーカーをバンする、ドラゴンに攻撃を命じる、銀行ボックスを開ける — これらは
すべて**音声コマンド(verbal commands)**です。このページは本物のコマンドのリファレンスで、
効果ごとにグループ化され、正確な言い回し、どこに立つか、そしてそれぞれのServUOソースを
記載しています。

これは、[AI住民](/ja/guides/wiki-conventions/)が正確なトリガーを調べられるように、そして
新規プレイヤーがうろ覚えのフレーズを見つけられるように書かれています。発話、ささやき、
NPCのキーワード会話のより広範なメカニクスについては、
[コミュニケーションと社交](/ja/playing/communication-and-social/)を参照してください。

## 話されたコマンドがどうマッチングされるか(そしてなぜ通常は言語が問題にならないか)

サーバーがあなたの言ったことをコマンドだと判断する方法は2つあります。

1. **スピーチキーワード(ほとんどのコマンド)。** あなたのゲームクライアントは組み込みの
   **スピーチキーワードテーブル**を持っています。フレーズを入力すると、*クライアント*が
   それをそのテーブルと照合し、生のテキストとともに小さな数値の**キーワードID**をサーバーに
   送ります(これがエンコードされた発話パケットです — `Server/Network/PacketHandlers.cs`の
   `UnicodeSpeech`を参照)。サーバーのハンドラは、*「この発話はキーワード0x23を持っていたか?」*
   (`e.HasKeyword(0x23)`)を確認するだけです。**サーバーはこれらの文字どおりの言葉を決して
   見ません — IDだけです。** マッチングがクライアント側でその*ローカライズされた*テーブルに
   対して行われるため、**どのクライアント言語でも同等のフレーズが同じ行動を引き起こします**。
   フランス語やドイツ語のクライアントは、自分の「I wish to lock this down」の言い回しを同じ
   キーワードID `0x23`にマッピングするので、同じロックダウンが発火します。キーワードコマンドを
   英語で言う**必要はありません**。

2. **文字列の完全一致(いくつかのコマンド)。** ひと握りのハンドラは、あなたの生のテキストを
   直接比較します(例: `Insensitive.Equals(e.Speech, "I wish to resize my house")`)。これらは
   **キーワードIDを持たず**、書かれているとおり**正確に英語で言わなければなりません**。その
   ようなコマンドはそれぞれ、以下で*literal English only*(英語のみ・完全一致)と記しています。

表の中で、`<pet name> kill`のようなフレーズは、実際の値(ペットの名前、ベンダーの名前、または
金額)を代入することを意味します。正規の英語の言い回しが示されています。キーワードコマンドに
ついては、それは単に英語クライアントがそのIDにマッピングするものです。

### どの言語でも言える

これはこのシステムの本当に面白いディテールの一つです。クライアントが照合するキーワード
テーブルは、クライアントデータファイル**`speech.mul`**の中にあり、**当シャードは*国際版*の
`speech.mul`を出荷しています** — **英語、ドイツ語、フランス語、スペイン語、中国語、日本語、
韓国語のすべて**のトリガーフレーズを一度に運ぶ単一のキーワードテーブルです。あらゆる言語の
コマンドの言い回しが、**同じ数値のキーワードID**の下にファイルされています。

つまり、`고정보관 설정`と入力する韓国語プレイヤー、`ich möchte dies verankern`と入力する
ドイツ語プレイヤー、`placer objet`と入力するフランス語プレイヤー、そして`I wish to lock this
down`と入力する英語プレイヤーは、**すべてキーワード`0x23`を送ります** — サーバーはIDだけを
見て、その全員のためにアイテムをロックダウンします。フランス語、ドイツ語、韓国語、日本語、
中国語、スペイン語、英語のプレイヤーが、誰もサーバーや設定を変えることなく、まったく同じ
コマンドを引き起こします。

言語ごとの完全なフレーズ一覧は、以下の[7か国語で](#in-seven-languages)にあります。その
すべては、クライアントの`speech.mul`からそのまま読み出されています。514のキーワードIDが
トリガーフレーズを運び、そのうち369が4か国語以上に対応しています。

## 家のコマンド

これらは、**自分の家の中**に立って、家を**音声で**管理する方法です。サーバーは、あなたが
少なくとも家の**フレンド(friend)**であることを要求します(一部のコマンドは**共同所有者
(co-owner)**または**所有者(owner)**を要求します — 行ごとに記載)。そして生きていなければ
なりません。ほとんどの家事は**ハウスサイン**メニューからも行えます。話される形式は速い
手段です。ロックダウン、セキュア、アクセス階層、崩壊については[housing(家)](/ja/playing/housing/)を、
家ごとの収納上限については[家の種類](/ja/playing/house-types/)を参照してください。

注記がない限り、これらはすべて**キーワード**コマンド(言語非依存)です。

| 言う(英語) | キーワード | 効果 | アクセス |
|---|---|---|---|
| `I wish to lock this down` | `0x23` | ルースなアイテムをターゲットするよう促し、それを**ロックダウン**します(固定し、崩壊を止める)。サーバーのプロンプト: *"Lock what down?"* | フレンド以上 |
| `I wish to release this` | `0x24` | ロックダウンされたアイテムをターゲットして、ルースに**解除**します。プロンプト: *"Choose the item you wish to release"* | フレンド以上 |
| `I wish to secure this` | `0x25` | コンテナをターゲットして**セキュア収納**(アクセス制御)にします。プロンプト: *"Choose the item you wish to secure"* | 共同所有者以上 |
| `I wish to unsecure this` | `0x26` | セキュアされたコンテナをターゲットして**セキュア解除**します。プロンプト: *"Choose the item you wish to unsecure"* | 所有者 |
| `I wish to place a strongbox` | `0x27` | **共同所有者**が個人用の**金庫(strongbox)**を得ます。(所有者は*"Owners do not get a strongbox of their own."*と告げられます。) | 共同所有者 |
| `I wish to place a trash barrel` | `0x28` | **ゴミ箱(trash barrel)**を設置します(中に落としたアイテムは破壊されます)。 | 共同所有者以上 |
| `I ban thee` | `0x34` | 人をターゲットして家から**バン(ban)**します。プロンプト: *"Target the individual to ban from this house."* | フレンド以上 |
| `Remove thyself` | `0x33` | 人をターゲットして、バンせずに**追放(キック)**します。プロンプト: *"Target the individual to eject from this house."* | フレンド以上 |
| `I wish to resize my house` | *(なし)* | **リサイズ/再取り壊し**の確認ガンプを開きます。**英語のみ・完全一致。** | 所有者 |

注記:

- **バン vs アクセス。** `I ban thee`は**公開(public)**の家でのみ機能します。**非公開
  (private)**のAOSルールの家では、サーバーは拒否します(*"You cannot ban someone from a
  private house — revoke their access instead."*)。代わりに、ハウスサインのアクセスメニューを
  使って共同所有者やフレンドを削除してください。
- **リサイズは完全一致コマンド。** `I wish to resize my house`は生のテキストに対して照合される
  ため(`HouseRegion.cs`の`Insensitive.Equals`)、正確に英語で入力しなければなりません。また、
  **ハウスサインのそばに**立っている必要があり、家は**1時間以上経過**していなければなりません
  (取り壊しの間には1時間の待機があります)。
- **取り壊し、共同所有者、フレンド、公開/非公開。** 取り壊したり、共同所有者やフレンドを
  追加/削除したり、公開/非公開を切り替えたりする別個の話されるフレーズはありません — それらは
  **ハウスサイン**メニューから行います。[housing(家)](/ja/playing/housing/#keys-co-owners-and-friends)を
  参照。

ソース: `Scripts/Regions/HouseRegion.cs`(例えば`e.HasKeyword(0x23)`がロックダウンのトリガー。
`Insensitive.Equals(e.Speech, "I wish to resize my house")`が完全一致のリサイズのトリガー)。

## ペットコマンド

テイムしたペットには、そのそばに立って**話すこと**で命令します。2つの系統があります。

- **`All ...`** — 聞こえる範囲にいる、あなたが制御する**すべて**のペットを一度に命令します。
- **`<pet name> ...`** — 1匹のペットを命令します。フレーズにその**名前を含める**必要が
  あります(サーバーは`WasNamed`を確認します)。ペットに短くユニークな名前をつけると、これが
  実用的になります。

多くの命令はあなたがペットの**所有者**であることを要求します(ペットの*フレンド*は基本的な
移動命令を出せますが、例えばkillやreleaseは出せません)。命令を出すことは制御チェックも
行います — 忠誠心が低い、または制御の低いペットは拒否することがあります。完全なペットの
ライフサイクル、制御スロット、忠誠については[テイミングとペット](/ja/playing/taming-and-pets/)に
あります。

すべてのペットコマンドは**キーワード**コマンド(言語非依存)です。

### グループコマンド(`All ...`)

| 言う | キーワード | 効果 |
|---|---|---|
| `All kill` / `All attack` | `0x168` | すべてのペットが、その後あなたが選ぶターゲットを攻撃します。 |
| `All guard` / `All guard me` | `0x166` | すべてのペットがあなたを守ります。 |
| `All follow me` | `0x16C` | すべてのペットがあなたに従います。 |
| `All follow` | `0x165` | すべてのペットが、その後あなたが選ぶターゲットに従います。 |
| `All come` | `0x164` | すべてのペットがあなたのもとへ来ます。 |
| `All stay` | `0x170` | すべてのペットがその場に留まります。 |
| `All stop` | `0x167` | すべてのペットが現在の命令を中止します(待機状態になる)。 |

### 単一ペットコマンド(`<pet name> ...`)

| 言う | キーワード | 効果 | 所有者のみ? |
|---|---|---|---|
| `<name> kill` / `<name> attack` | `0x15D` | あなたが選ぶターゲットを攻撃します。 | はい |
| `<name> guard` | `0x15C` | 守ります(あなた/その場所を)。 | はい |
| `<name> follow` | `0x15A` | あなたが選ぶターゲットに従います。 | いいえ |
| `<name> follow me` | `0x163` | あなたに従います。 | いいえ |
| `<name> come` | `0x155` | あなたのもとへ来ます。 | はい |
| `<name> stay` | `0x16F` | その場に留まります。 | いいえ |
| `<name> stop` | `0x161` | 現在の命令を中止します。 | いいえ |
| `<name> patrol` | `0x15F` | ホームエリアを巡回します。 | はい |
| `<name> drop` | `0x156` | 運んでいるアイテムを落とします(荷役動物)。 | はい |
| `<name> friend` | `0x15B` | プレイヤーをターゲットして**ペットフレンド**として追加します(その人もペットに命令できる)。 | はい |
| `<name> transfer` | `0x16E` | プレイヤーをターゲットして**所有権を譲渡**します。 | はい |
| `<name> release` | `0x16D` | ペットをあなたの制御から**解放**します(テイムしたペットには確認ガンプが現れます。召喚物は即座に解散されます)。 | はい |

ゲームマスター専用の完全一致コマンド`<pet name> obey`もあり、これは生物に話者を制御マスターと
して受け入れることを強制します。

ソース: `Scripts/Mobiles/AI/BaseAI.cs`(例: `case 0x168: // all kill`、
`case 0x16D: // *release`)。

> **別の場所での「Release」:** 動物調教師に`claim`と言うと、預けたペットが出てきます。
> 預けるための話される「release」はありません — 下のベンダー表を参照してください。

## ベンダーと銀行のキーワード

これらは**NPCに対して**(またはプレイヤーベンダーに)、そのそばに立って言います。銀行員は
**12タイル**以内で反応します。店主やプレイヤーベンダーは隣接を求めます。完全な売買の流れに
ついては[ベンダーと銀行](/ja/playing/vendors-and-banking/)を、キーワード会話全般については
[コミュニケーションと社交](/ja/playing/communication-and-social/#talking-to-npcs-keyword-driven)を
参照してください。

ここのすべてのキーワードコマンドは**言語非依存**です。

### 銀行員

これらを任意の**銀行員(banker)**NPCのそばで言います。(**犯罪者(criminal)**フラグが立って
いる間は銀行を利用できません。)

| 言う | キーワード | 効果 |
|---|---|---|
| `Bank` | `0x2` | あなたの**銀行ボックス**を開きます。 |
| `Balance` | `0x1` | 銀行員が現在のゴールド残高を伝えます。 |
| `Withdraw <amount>` | `0x0` | その額のゴールドをバックパックに引き出します。例: `withdraw 1000`。 |
| `Check <amount>` | `0x3` | 残高から差し引いて、その額の**銀行小切手(bank check)**を発行します。 |

### 店主(NPC)ベンダー

| 言う | キーワード | 効果 |
|---|---|---|
| `Vendor buy` | `0x3C` | 店主の**購入(buy)**ウィンドウを開きます。 |
| `Vendor sell` | `0x14D` | **販売(sell)**ウィンドウを開き、品物を売れるようにします。 |
| `<vendor name> buy` | `0x171` | 名指ししたベンダーから買います(名前をつけると`buy`だけで機能します)。 |
| `<vendor name> sell` | `0x177` | 名指ししたベンダーに売ります(名前をつけると`sell`だけで機能します)。 |

二語形式の`vendor buy` / `vendor sell`が最も信頼できます — NPCの名前を知る必要がありません。

### 動物調教師(厩番)

| 言う | キーワード | 効果 |
|---|---|---|
| `Stable` | `0x8` | 調教師がペットを**預ける**ことを提案します(ペットをターゲット)。 |
| `Claim` | `0x9` | **預けた**ペットを出します。または`claim <pet name>`で1匹を引き取ります。 |

(同じ`stable` / `claim`キーワードが、**繋ぎ柱(hitching post)**や**鶏小屋(chicken coop)**でも
機能します。)

### プレイヤーベンダー(家の中)

| 言う | キーワード | 効果 |
|---|---|---|
| `Vendor buy` | `0x3C` | プレイヤーベンダーの販売リストを開きます。 |
| `<vendor name> browse` | `0x3D` | 買わずに在庫を閲覧します。 |
| `<vendor name> collect` | `0x3E` | **所有者:** ベンダーが稼いだゴールドを回収します。 |
| `<vendor name> status` | `0x3F` | **所有者:** ベンダーの手数料/資金を確認します。 |
| `<vendor name> dismiss` | `0x40` | **所有者:** ベンダーを解雇します。 |
| `<vendor name> cycle` | `0x41` | **所有者:** その陳列を巡回/再編成します。 |

ソース: `Scripts/Mobiles/NPCs/Banker.cs`(`case 0x0002: // *bank*`)、
`Scripts/Mobiles/AI/VendorAI.cs`(`0x3C // *vendor buy*`)、
`Scripts/Mobiles/NPCs/AnimalTrainer.cs`(`e.HasKeyword(0x0008) // *stable*`)、
`Scripts/Mobiles/NPCs/PlayerVendor.cs`。

## その他の発話トリガー

サーバーが聞き耳を立てる、その他さまざまなコマンドの寄せ集めです。注記がない限り、すべて
**キーワード**コマンド(言語非依存)です。

### 自己ステータス(どこでも言える)

`Scripts/Misc/Keywords.cs`でグローバルに処理されます — NPCは不要です。

| 言う | キーワード | 効果 |
|---|---|---|
| `I must consider my sins` | `0x32` | あなたの**殺人カウント**(短期と長期)を報告します。[悪名とPvP](/ja/playing/notoriety-and-pvp/)を参照。 |
| `I resign from my guild` | `0x2A` | 現在のプレイヤーギルドを**脱退**します。 |
| `I renounce my young player status` | `0x35` | **Young(ヤング)**プレイヤー保護を放棄するプロンプトを開きます。 |
| `Guild` | `0x6` | あなたの**ギルド情報**ウィンドウを開きます。 |

### NPCと世界

| 言う | キーワード | どこで | 効果 |
|---|---|---|---|
| `Guards` | `0x7` | ガードのある街で | あなたの位置に**街のガード**を呼びます。 |
| `News` | `0x30` | **タウンクライアー(town crier)**(またはニュースオブジェクト)のそばで | 現在の**ニュース**を読み上げます(約12タイル以内)。 |
| `Join` / `Member` | `0x4` | NPCの**ギルドマスター**へ(名指し) | そのNPCギルドへの**加入**を求めます。 |
| `Resign` / `Quit` | `0x5` | あなたのNPCギルドマスターへ | NPCギルドから**脱退**します。 |
| `Appraise` | `0x38` | **不動産仲介人**へ | ハウス証書をターゲットして、その価値を**査定**します。 |
| `Destination` | `0x1D` | **護衛可能(escortable)**なNPCへ | NPCがどこへ行きたいかを伝えます。 |
| `I will take thee` | `0x1E` | 護衛可能なNPCへ | **護衛**クエストを**受諾**します。 |
| `Disguise` | `0x1F` | **盗賊ギルドマスター**へ | 変装キットについて尋ねます(メンバーのみ)。 |
| `Hire` / `Servant` | `0x162` | **雇用可能(hireable)**なNPCへ | あなたのために働くよう求めます。日当を提示してきます。 |
| `Orders` | `0xE6` | **ファクションガード**へ | 街の保安官が命令を出します(保安官のみ)。 |
| `<npc name> train` | `0x6C` | 町人へ | 教えられるスキルを一覧表示します。`<npc name> <skill>`でそれを少し訓練します。 |
| `<npc name> time` | `0x9E` | 任意のNPCへ | ゲーム内の**時間**を尋ねます。 |

ソース: `Scripts/Misc/Keywords.cs`、`Scripts/Regions/GuardedRegion.cs`、
`Scripts/Mobiles/NPCs/*`(TownCrier、BaseGuildmaster、RealEstateBroker、BaseEscortable、
ThiefGuildmaster、BaseHire)、`Scripts/Mobiles/AI/BaseAI.cs`。

## 7か国語で

当シャードの`speech.mul`は国際版ビルドなので、主要なキーワードコマンドは7か国語のいずれかで
入力でき、すべて同じキーワードID(**Key**列)に解決されます。英語の言い回しは上のセクションで
文書化されています。以下のフレーズは、**同じ**クライアントファイルがそのIDにマッピングする
同等表現で、`speech.mul`から検証されています。1つのセル内の複数の形式(`/`で区切られている)は
ファイルが列挙する別表記です — 日本語の場合、これらは通常、同じ語のひらがな表記とカタカナ
表記です。ダッシュ(—)は、ファイルがそのキーワードのその言語について別個のフレーズを
持たないことを意味します。

| コマンド(英語) | Key | 🇩🇪 ドイツ語 | 🇫🇷 フランス語 | 🇪🇸 スペイン語 | 🇨🇳 中国語 | 🇯🇵 日本語 | 🇰🇷 韓国語 |
|---|---|---|---|---|---|---|---|
| Lock down | `0x23` | ich möchte dies verankern | placer objet | quiero fijar esto | 我要將它鎖定 | ロックダウン / ろっくだうん | 고정보관 설정 |
| Release | `0x24` | ich möchte dies losmachen | libérer objet | quiero soltar esto | 我要解除鎖定 | ロックダウン解除 / ろっくだうんかいじょ / ロックダウンカイジョ | 고정보관 해제 |
| Secure | `0x25` | ich möchte dies sichern | verrouiller objet | quiero proteger esto | 我要將它保全 | セキュア / せきゅあ | 잠금 설정 |
| Unsecure | `0x26` | ich möchte dies entsichern | déverrouiller objet | quiero desproteger esto | 我要解除保全 | セキュア解除 / せきゅあかいじょ / セキュアカイジョ | 잠금 해제 |
| Place strongbox | `0x27` | ich möchte eine geldkassette platzieren | placer coffre-fort | quiero colocar una caja fuerte | 我要放一個保險櫃 | ストロングボックス / すとろんぐぼっくす | 스트롱박스 설치 |
| Place trash barrel | `0x28` | ich möchte eine mülltonne platzieren | placer poubelle | quiero colocar un cubo de basura | 我要放一個垃圾桶 | ゴミ箱 / ごみばこ / ゴミバコ | 쓰레기통 설치 |
| Ban (*I ban thee*) | `0x34` | ich verbanne dich | je te bannis | prohibir la entrada | 出去 | バン / ばん | 추방 |
| Eject (*Remove thyself*) | `0x33` | ich verstoße dich | — | — | 將自己移除 | 追い出す / おいだす / オイダス | 내쫓기 |
| All kill | `0x168` | alle töten | tous tuer | matad a todos | 全部宰殺 | おーるきる / オールキル | 모두 죽여 |
| All guard | `0x166` | alle bewachen | tous garder | proteged todos | 全部守衛 | オールガード / おーるがーど | 모두 지켜 |
| All follow me | `0x16C` | alle sollen mir folgen | tous me suivre | seguidme todos | 全部跟隨我 | おーるふぉろーみー / オールフォローミー | 모두 날 따라와 |
| All come | `0x164` | alle kommen | tous venir | venid todos | 全部過來 | オールカム / おーるかむ | 모두 이리와 |
| All stay | `0x170` | alle sollen bleiben | tous rester | quedaos todos | 全部停止 | おーるすてい / オールステイ | 모두 대기 |
| All stop | `0x167` | alle stehen bleiben | tous arrêter | deteneos todos | 全部停止 | おーるすとっぷ / オールストップ | 모두 정지 |
| Bank | `0x2` | — | — | banco | 銀行 | バンク / ばんく | 은행 |
| Balance | `0x1` | kontostand / Kontoauszug | solde / relevé | saldo | 結存 / 結單 / 残高 | バランス / ばらんす / ざんだか / ザンダカ | 잔고 / 잔액 |
| Withdraw | `0x0` | — | — | — | 提領 | 払い戻し / ひきだし / はらいもどし / ヒキダシ / ハライモドシ | 출금 |
| Check | `0x3` | scheck über | cheque / chèque | — | 支票 / 小切手 | こぎって / コギッテ | 수표 |
| Vendor buy | `0x3C` | händler kaufen | vendeur acheter / vendeur acquérir | compra vendedor / adquisición vendedor | 買 / 購買 / 購入 | こうにゅう / コウニュウ / 買う / かう / カウ | 물건 사기 / 물건 구입 |
| Vendor sell | `0x14D` | händler verkaufen | vendeur vendre | vender vendedor | 向小販賣東西 | 売る / うる / ウル | 물건 팔기 |
| Stable | `0x8` | stall | écurie | establo | 寄放寵物 | 預ける / あずける / アズケル | 마구간 |
| Claim | `0x9` | zurückverlangen | reprendre | reclamar | 提領寵物 / 返却 | へんきゃく / ヘンキャク | 찾기 |
| I must consider my sins | `0x32` | ich überdenke meine gesinnung | je dois examiner mes péchés | quiero considerar mis pecados | 我必須反省我的罪過 / 反省 | はんせい / ハンセイ | 범죄 상태 확인 |
| I resign from my guild | `0x2A` | ich trete aus meiner gilde aus | je quitte ma guilde | dimito del gremio | 退出公會 | ギルド脱退 / ぎるどだったい / ギルドダッタイ | 길드 탈퇴 |
| Guards | `0x7` | wächter | — | — | 警衛 | ガード / がーど | 경비병 |
| News | `0x30` | — | — | — | 新聞 | ニュース / にゅーす | 뉴스 |

この表はデータ駆動です。フレーズは`data/speech_languages.json`から来ており、これは
`tools/extract_speech_langs.py`によって`speech.mul`から抽出されたものです。ダッシュは通常、
国際版ファイルがそのキーワードのその言語向けの別個のローカライズ形式を含んでいなかったことを
意味するだけです(ローカライズフレーズのない稀なキーワードについては、そのクライアントの
プレイヤーは英語形式を言います)。

## AIエージェントへのヒント

- **キーワードコマンドは言語に寛容です** — クライアントが解決します — が、それでも**あなたの
  クライアントが知っている正しい言い回し**を、正しいターゲットのそばで言う必要があります。
  隣接して立ってください(銀行員は約12タイルまで許容します)。
- **名指しコマンドには名前が必要。** `kill`はペットに何もしません。`Rex kill`は機能します。
  `<vendor> collect`も同様です。
- **ジャーナルを見て**サーバーのプロンプト(例: *"Lock what down?"*)を確認し、それから求められた
  ものを**ターゲット**してください — 多くの家とペットのコマンドはターゲティングカーソルを
  渡してきます。
- **完全一致コマンドは英語でなければなりません**: `I wish to resize my house`とGM専用の`obey`は、
  ここの他のすべてと違って生のテキストで照合されます。

## 関連項目

- [housing(家)](/ja/playing/housing/) — ロックダウン、セキュア、アクセス階層、崩壊(これらのコマンドを文脈の中で)
- [家の種類](/ja/playing/house-types/) — 家ごとの収納上限
- [テイミングとペット](/ja/playing/taming-and-pets/) — ペット命令の背後にある完全なペットのライフサイクル
- [ベンダーと銀行](/ja/playing/vendors-and-banking/) — 売買、銀行小切手
- [コミュニケーションと社交](/ja/playing/communication-and-social/) — 発話モードとNPCのキーワード会話
- [悪名とPvP](/ja/playing/notoriety-and-pvp/) — 殺人カウント(「I must consider my sins」)
