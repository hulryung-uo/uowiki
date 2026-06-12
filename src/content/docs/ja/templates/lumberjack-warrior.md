---
title: "テンプレート: ランバージャックウォリアー（斧使い）"
description: 斧デクサー —— 伐採を取り、グランドマスターで斧を +20% ダメージで振るう近接ウォリアーを、7-GM 構成として提示。
status: unverified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs (lumberBonus = GetBonus(Lumberjacking, 0.200, 100.0, 10.00))"
  - "servuo: Scripts/Items/Equipment/Weapons/BaseAxe.cs (axes use Lumberjacking.System; DefSkill = Swords)"
  - "servuo: Config/PlayerCaps.cfg (700 total / 100 per-skill / 225 stat caps)"
  - "community/era UO build knowledge — adapted to this shard"
last_verified: 2026-06-12
generated: false
---

:::note[未検証 —— コミュニティ／時代の構成、調整済み]
これはクラシック時代のコミュニティ構成（「ランバージャックデクサー」／「斧使い」）をこのシャードに調整したものです。
**+20% 斧ボーナス**と **700/225 上限**は ServUO に対してソース検証済みですが、構成の形とお金の助言は
時代の知恵です。**実地検証は保留中**です —— 遊んだら[wiki の規約](/ja/guides/wiki-conventions/)に従って
相違を報告してください。
:::

ランバージャックウォリアーは、素の剣デクサーより強く殴れる一つの捻りを加えた[ウォリアー](/ja/templates/warrior/)です:
**[伐採](/ja/skills/lumberjacking/)**を取り、**斧**で戦います。このシャードでは斧系の武器が伐採スキルに応じた
固定ダメージボーナスを得るので、グランドマスターのランバージャックは、同じキャラクターがカタナを持つよりも
明らかに強く振るいます。

## 斧がより強く殴る理由（ソース検証済み）

`servuo: Scripts/Items/Equipment/Weapons/BaseWeapon.cs` によれば、武器の総ダメージに**lumber ボーナス**が加わります:

```
lumberBonus = GetBonus(Lumberjacking, 0.200, 100.0, 10.00)
```

この式は **100.0 の伐採で +20% ダメージ**に達します（`BaseAxe.cs` は斧を `Lumberjacking.System` で登録するので、
ボーナスは斧を装備しているときにのみ適用され、斧以外の武器ではこの行はゼロになります）。斧はまた
[剣術](/ja/skills/swordsmanship/)を訓練・使用するので（`BaseAxe.cs`: `DefSkill = Swords`）、
ランバージャックウォリアーは**斧に特化した剣士**です —— カタナではなく [War Axe](/ja/items/catalog/weapons/)、
Large Battle Axe、Two-Handed Axe を使います。

この +20% はあなたの STR、解剖学、戦術のボーナスの上に乗るので、素のデクサーが決して得られない本物の無料の
ダメージ層です。代償は、7 つのスキル枠の一つを、たとえば魔法ではなく伐採に費やすことです。

## 7 スキル（合計約 700）

7 つのグランドマスター（100.0）スキルの合計は **700.0** —— このシャードの総スキル上限
（`Config/PlayerCaps.cfg`）です。一つの妥当な配分:

- **[剣術](/ja/skills/swordsmanship/)** —— あなたの武器スキル; 斧はこれを訓練・使用します。
- **[戦術](/ja/skills/tactics/)** —— 核となるダメージ倍率。
- **[解剖学](/ja/skills/anatomy/)** —— さらなるダメージ、そして包帯回復を養います。
- **[治療](/ja/skills/healing/)** —— 包帯; 治療＋解剖学が 80/80 で自己蘇生。
- **[伐採](/ja/skills/lumberjacking/)** —— +20% 斧ボーナス（と無料の木材; 後述）。
- **[耐性](/ja/skills/resisting-spells/)** —— 敵の魔法を鈍らせる。
- **フレックス: [受け流し](/ja/skills/parrying/)**（盾による防御の一部 —— ただし両手斧は盾を持つ手が
  残らないので、受け流しは片手の [War Axe](/ja/items/catalog/weapons/)と組み合わせること）、または
  **[騎士道](/ja/skills/chivalry/)／[魔法](/ja/skills/magery/)**（回復、キュア、移動などのユーティリティ）。

:::tip[120 はパワースクロールから]
上記の 7-GM（100.0）の天井は*基本*上限です。個々のスキルは**パワースクロール**で **120** まで押し上げられ、
このシャードでは**チャンピオンスポーンと宝**から落ちます —— [トレジャーハンティング](/ja/playing/treasure-hunting/)を参照。
120 剣術／120 戦術の斧使いが、このテンプレートの最終形態です。
:::

**推奨ステータス（225 上限）:** 約 100 STR / 約 90 DEX / 約 35 INT。STR はヒットポイントとダメージ、
DEX は振りと包帯の速度を駆動します。INT は低く保ちましょう（ユーティリティのフレックスに足りる程度）。
合計 225 のステータスはシャードの上限です（`Config/PlayerCaps.cfg`）。

## 立ち回り

[ウォリアー](/ja/templates/warrior/)のように遊びます —— 接近、振る、包帯、戦利品 —— ただし手には斧を、
そしてそれに伴うダメージの優位を携えて。勝利条件は同じ消耗戦です: 飛んでくるダメージを回復で上回り、
対象を削り切る、ただしより速く。

- **両手斧で口火を切る**。盾を諦められるときの最大の一撃のために。受け流しの防御が欲しいときは片手の
  [War Axe](/ja/items/catalog/weapons/) ＋ 盾に切り替えましょう。
- **伐採を GM に保つ** —— 100 を下回る 1 ポイントごとにダメージを失うので、「今のところ」90 に置いておかないこと。
- **自給自足の木こり。** 伐採は単なるダメージのステータスではありません: 木から**木材を採集**できるので、
  剣デクサーを上回って殴る同じキャラクターが、売るための、あるいは弓職／大工の燃料となる丸太を切れます。
  多くのプレイヤーは斧使いを、自分で元を取る戦士として運用します。

武器のスペシャルとタイミングについては[上級戦闘](/ja/playing/combat-advanced/)を参照。

## お金

斧使いは素のウォリアーと同じ[ダンジョン](/ja/world/dungeons/)ラダーを狩りますが、+20% のダメージ優位は、
どの段でもより速い撃破と時間あたりのより多いゴールドを意味します。それに加えて:

- **木材収入。** ダンジョンへの行き帰りに丸太を切りましょう。板は大工や弓職に売れ、あるいは自分の生産ミュールの
  燃料になります。
- **ダンジョン狩り。** アースエレメンタル、オーガ、リッチ、そしてラダーを登っていく —— ダメージボーナスが
  あらゆる戦いを短くします。Felucca のスポーンは PvP のリスクを受け入れればより多く払います。

## 関連項目

- [ウォリアーテンプレート](/ja/templates/warrior/) —— この構成が重ねる、初心者→達人の完全なストーリー。
- [7x GM テンプレート](/ja/templates/seven-gm/) —— これが終盤構成のどこに位置するか。
- [伐採](/ja/skills/lumberjacking/)、[剣術](/ja/skills/swordsmanship/)、
  [戦術](/ja/skills/tactics/)。
- [ウォリアー職業](/ja/professions/warrior/)、[上級戦闘](/ja/playing/combat-advanced/)。
