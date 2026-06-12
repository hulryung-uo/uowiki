---
title: 武器
description: Ultima Online における武器の仕組み — ダメージ、振り速度、鍛えるスキル、必要筋力、片手・両手、特殊技 — そしてすべての武器系統を網羅したソース検証済みのステータス表。
status: source-verified
sources:
  - "servuo: Scripts/Items/Equipment/Weapons/*.cs"
  - "servuo: Scripts/Abilities/WeaponAbility.cs"
  - "uo-resource: tiledata.mul (weapon layer)"
  - "uowiki: data/weapons.json (extracted via tools/extract_weapons.py)"
last_verified: 2026-06-11
generated: false
---

武器は、近接・遠隔キャラクターが実際にどう戦うかを決定します。どれだけ強く当たるか、
どれだけ速く振るか、どの**戦闘スキル (combat skill)** を鍛えるか、そしてどの2つの**特殊技 (special moves)** を
繰り出せるか、です。このページではまずステータスを解説し、続いて ServUO ソースに存在する
**135種の武器 (weapons)** すべてを系統別にまとめたソース検証済みステータス表を示します。

:::tip
以下のステータスは、当シャード (EJ) が使用する **AOS時代** の値で、各武器の `.cs` クラスから
直接読み取ったものです。振り速度は**秒**で表示しています (ML/EJ の `MlSpeed` 値 —
*低いほど速い*)。時代ごとにアート豊富な武器索引を閲覧したい場合は、
[武器カタログ](/ja/items/catalog/weapons/) を参照してください。
:::

## 武器の仕組み

装備可能な武器はすべて、同じ少数のステータスを共有します。それらを理解することが、
武器選びの全てと言ってよいでしょう。

### ダメージ範囲

各武器には**最小・最大の基礎ダメージ**が記載されています (例: katana は 10–14)。振るたびに
その範囲内のランダム値が振られ、命中する前にその基礎値は大きく補正されます — あなたの
**[Tactics](/ja/skills/tactics/)** と **[Anatomy](/ja/skills/anatomy/)** スキル、
**Strength**、武器のダメージ増加プロパティ、そして対象の抵抗値によってです。表の値は
*基礎*範囲のみで、Tactics と Anatomy の高い GM 戦士ははるかに大きなダメージを与えます。
ダメージ計算の全パイプラインは [戦闘の基礎](/ja/playing/combat-basics/) を、根底にある公式は
[メカニクス](/ja/mechanics/) を参照してください。

### 武器速度 (振りディレイ)

**速度 (Speed)** は、どれだけ頻繁に攻撃できるかを示します。当 ML/EJ シャードでは、各武器が秒単位の
`MlSpeed` を持ちます — 表はこれを直接表示しており、**低いほど速い**です (2.0秒の dagger は
4.5秒の heavy crossbow の2倍以上の頻度で振れます)。振りと振りの*実際の*ディレイは、あなたの
**Stamina** と装備の **Swing Speed Increase** プロパティによって短縮されます。スタミナが多いほど
振りが速くなり、戦闘でスタミナを失うと遅くなります。速い武器はより多く命中するため、
命中時効果 (毒、リーチ、特殊技) をより頻繁に発動させ、遅い武器は1撃ごとに大きな生ダメージを
込めます。スタミナと振り速度ボーナスがどう組み合わさるかは
[戦闘上級](/ja/playing/combat-advanced/) を参照してください。

### 統括スキル

各武器は、そのクラスによって正確に1つの**戦闘スキル**を鍛えます。4つの近接スキルと
2つの遠隔スキルは以下の通りです:

- [**Swordsmanship**](/ja/skills/swordsmanship/) — 剣、斧、長柄武器
- [**Mace Fighting**](/ja/skills/mace-fighting/) — メイス、ハンマー、杖、ワンド
- [**Fencing**](/ja/skills/fencing/) — ダガー、クリス、スピア、フォーク
- [**Archery**](/ja/skills/archery/) — 弓とクロスボウ
- **Throwing** — ガーゴイルの投擲武器

戦闘スキルは**命中率**を統括します。**[Tactics](/ja/skills/tactics/)** と
**[Anatomy](/ja/skills/anatomy/)** はその後**ダメージ**を底上げし、*すべての*武器に適用されます。
これが、ほぼ全ての近接テンプレートがこれらを携える理由です (
[7×GM 戦士テンプレート](/ja/templates/seven-gm/) 参照)。一部の武器は、ある系統の土台の上に
作られながら異なるスキルを鍛えます — それらは表で印を付けています (<sup>Sw</sup> Swordsmanship、
<sup>Fe</sup> Fencing、<sup>Ma</sup> Mace Fighting)。

### 必要筋力

各武器には**必要筋力 (Strength requirement)** があります。要件を下回った状態で武器を装備すると、
ペナルティを受けて振ることになります。重い両手武器 (halberd、war hammer、heavy crossbow) は
80–95 の Strength を要求し、軽い dagger やワンドは 5–10 ほどしか必要としません。

### 片手 vs 両手

**片手 (one-handed)** 武器は、もう一方の手を**盾** (Parrying) や呪文書のために空けておけます。
**両手 (two-handed)** 武器は両手を占有します。**盾は持てず、片手を必要とする詠唱も妨げます**。
両手武器はそれを補うために概してより強く命中します。Hands 列は **1H** または **2H** を示します。

### ダメージタイプ

武器はその系統に結びついた基礎**ダメージタイプ**を与えます。剣やナイフは**斬撃 (slash)**、
スピアやクリスは**刺突 (pierce)**、メイスや杖は**打撃 (bash)** です。ダメージタイプは対象の
抵抗値と照合され、魔法武器はダメージを fire/cold/poison/energy に分割できます。

## 特殊技

すべての武器は2つの**特殊技 (special moves)** を付与します — **一次 (primary)** と
**二次 (secondary)** の武器アビリティです。戦闘書または戦闘モードのボタンから1つを構え、
次の有効な命中で**マナ** (時にはスタミナ) を消費して発動します。**一次**アビリティは武器の
戦闘スキルが約70で解放され、**二次**は約90で解放されます。武器が提供する2つのアビリティは
クラスによって固定されています — 武器を選ぶことは、部分的にその特殊技を選ぶことです。発動、
マナコスト、タイミングについては [戦闘上級](/ja/playing/combat-advanced/) を参照してください。

一般的なアビリティ (`Scripts/Abilities/WeaponAbility.cs` より):

| アビリティ | 効果 |
|---|---|
| **Armor Ignore** | 対象の防具を無視 — ダメージは低いが、ほぼ全量が通る。 |
| **Bleed Attack** | 継続ダメージを与える出血を付与する。 |
| **Concussion Blow** | 対象の現在マナに比例したバーストダメージ。 |
| **Crushing Blow** | およそ +50% ダメージの重い一撃。 |
| **Disarm** | 対象の手から武器を叩き落とす (空いた手が必要)。 |
| **Dismount** | 騎乗中の対象を乗騎から叩き落とす — PvP の定番。 |
| **Double Strike** | 1アクションで2回振る。 |
| **Infectious Strike** | チャージを使い切らずに武器の毒を付与する。 |
| **Mortal Strike** | 対象を負傷させ、数秒間ヒーリングを失敗させる。 |
| **Moving Shot** | (遠隔) 移動しながら射撃できる。 |
| **Paralyzing Blow** | 対象を短時間その場に固定する。 |
| **Shadow Strike** | 攻撃者を一時的に隠す/ステルスさせる一撃。 |
| **Whirlwind Attack** | 隣接する*すべての*敵を一度に攻撃する。 |
| **Frenzied Whirlwind** | 近くの敵を繰り返し攻撃する範囲攻撃。 |
| **Riding Swipe** | 対象を下馬させ、乗騎を負傷させることがある。 |
| **Block / Defense Mastery** | 被ダメージ軽減を高める防御特殊技。 |
| **Feint** | 数秒間、対象が与えてくるダメージを軽減する。 |
| **Dual Wield / Double Shot** | 特定の Tokuno・遠隔武器の追加振り/追加射撃の特殊技。 |
| **Armor Pierce** | 命中時に対象の物理抵抗を下げる。 |
| **Bladeweave** | 命中時にいくつかのアビリティのうち1つをランダムに発動する。 |
| **Force Arrow / Lightning Arrow / Serpent Arrow** | 属性または魔法効果を加えるエルフ弓の特殊技。 |
| **Psychic Attack** | 対象のマナコストを上げ、ダメージ出力を下げる。 |
| **Mystic Arc / Infused Throw** | ガーゴイルの投擲特殊技 (アーク/多対象投擲)。 |

:::note
一部の武器 (例: **Thin Longsword**) は特殊技を定義しておらず、エンジン既定の*なし*に戻ります —
それらは Primary/Secondary 列に「—」と表示されます。
:::

## 武器系統

以下の各セクションでは、系統の戦闘スキル、プレイスタイル、そして ServUO ソースから直接
構築したステータス表を示します。表の凡例: **Damage** = 基礎の最小–最大、**Speed** = 振り
あたりの秒数 (低いほど速い)、**Hands** = 1H/2H、**Str** = 必要筋力。武器名の後の印は
<sup>G</sup> = ガーゴイル専用、<sup>Sw/Fe/Ma</sup> = その系統の既定とは異なるスキルを鍛える、
を意味します。

クラフト武器は [Blacksmithy](/ja/crafting/blacksmithy/) (金属武器) と
[Bowfletching](/ja/crafting/bowfletching/) (弓、クロスボウ、矢弾) から作られます。アートと時代の
完全な索引は [武器カタログ](/ja/items/catalog/weapons/) を参照してください。

### Swords

**スキル:** [Swordsmanship](/ja/skills/swordsmanship/) · **武器数:** 33

**Swordsmanship** 系統はゲーム内で最も幅広い系統です。高速な片手 DPS の katana や longsword、
両手の斬撃武器、そして深みのある侍 (Tokuno) とガーゴイルの刀剣群が揃います。多くは斬撃ダメージの
片手武器で、盾と組み合わせます。剣として宣言されていながら実際には **Fencing** を鍛えるものも
少数あります (kryss と lance — <sup>Fe</sup> で印付け)。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x08FE.png" class="uo-sprite" alt="" width="40" /> | Blood Blade <sup>G·Fe</sup> | 10–12 | 2s | 1H | 10 | Bleed Attack | Paralyzing Blow |
| <img src="/img/items/0x27A8.png" class="uo-sprite" alt="" width="40" /> | Bokuto | 10–12 | 2s | 1H | 20 | Feint | Nerve Strike |
| <img src="/img/items/0x26BB.png" class="uo-sprite" alt="" width="40" /> | Bone Harvester | 12–16 | 3s | 1H | 25 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x2D35.png" class="uo-sprite" alt="" width="40" /> | Bone Machete | 11–15 | 2.75s | 1H | 20 | Defense Mastery | Bladeweave |
| <img src="/img/items/0x0F5E.png" class="uo-sprite" alt="" width="40" /> | Broadsword | 13–17 | 3.25s | 1H | 30 | Crushing Blow | Armor Ignore |
| <img src="/img/items/0x26C1.png" class="uo-sprite" alt="" width="40" /> | Crescent Blade | 12–15 | 2.5s | 2H | 55 | Double Strike | Mortal Strike |
| <img src="/img/items/0x1441.png" class="uo-sprite" alt="" width="40" /> | Cutlass | 10–14 | 2.5s | 1H | 25 | Bleed Attack | Shadow Strike |
| <img src="/img/items/0x27A9.png" class="uo-sprite" alt="" width="40" /> | Daisho | 13–16 | 2.75s | 2H | 40 | Feint | Double Strike |
| <img src="/img/items/0x090B.png" class="uo-sprite" alt="" width="40" /> | Dread Sword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Crushing Blow | Concussion Blow |
| <img src="/img/items/0x2D35.png" class="uo-sprite" alt="" width="40" /> | Elven Machete | 11–15 | 2.75s | 1H | 20 | Defense Mastery | Bladeweave |
| <img src="/img/items/0x48C6.png" class="uo-sprite" alt="" width="40" /> | Gargish Bone Harvester <sup>G</sup> | 12–16 | 3s | 1H | 25 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x48D0.png" class="uo-sprite" alt="" width="40" /> | Gargish Daisho <sup>G</sup> | 13–16 | 2.75s | 2H | 40 | Feint | Double Strike |
| <img src="/img/items/0x48BA.png" class="uo-sprite" alt="" width="40" /> | Gargish Katana <sup>G</sup> | 10–14 | 2.5s | 1H | 25 | Double Strike | Armor Ignore |
| <img src="/img/items/0x48BC.png" class="uo-sprite" alt="" width="40" /> | Gargish Kryss <sup>G·Fe</sup> | 10–12 | 2s | 1H | 10 | Armor Ignore | Infectious Strike |
| <img src="/img/items/0x48CA.png" class="uo-sprite" alt="" width="40" /> | Gargish Lance <sup>G·Fe</sup> | 18–22 | 4.25s | 1H | 95 | Dismount | Concussion Blow |
| <img src="/img/items/0xA345.png" class="uo-sprite" alt="" width="40" /> | Gargish Skull Longsword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x0908.png" class="uo-sprite" alt="" width="40" /> | Gargish Talwar <sup>G</sup> | 16–19 | 3.5s | 2H | 40 | Whirlwind Attack | Dismount |
| <img src="/img/items/0x090C.png" class="uo-sprite" alt="" width="40" /> | Glass Sword <sup>G</sup> | 11–15 | 2.75s | 1H | 20 | Bleed Attack | Mortal Strike |
| <img src="/img/items/0x13FF.png" class="uo-sprite" alt="" width="40" /> | Katana | 10–14 | 2.5s | 1H | 25 | Double Strike | Armor Ignore |
| <img src="/img/items/0x1401.png" class="uo-sprite" alt="" width="40" /> | Kryss <sup>Fe</sup> | 10–12 | 2s | 1H | 10 | Armor Ignore | Infectious Strike |
| <img src="/img/items/0x26C0.png" class="uo-sprite" alt="" width="40" /> | Lance <sup>Fe</sup> | 18–22 | 4.25s | 1H | 95 | Dismount | Concussion Blow |
| <img src="/img/items/0x0F61.png" class="uo-sprite" alt="" width="40" /> | Longsword | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x27A2.png" class="uo-sprite" alt="" width="40" /> | No Dachi | 16–19 | 3.5s | 2H | 40 | Crushing Blow | Riding Swipe |
| <img src="/img/items/0x26CE.png" class="uo-sprite" alt="" width="40" /> | Paladin Sword | 20–24 | 5s | 1H | 85 | Whirlwind Attack | Disarm |
| <img src="/img/items/0x2D33.png" class="uo-sprite" alt="" width="40" /> | Radiant Scimitar | 10–14 | 2.5s | 1H | 20 | Whirlwind Attack | Bladeweave |
| <img src="/img/items/0x2D32.png" class="uo-sprite" alt="" width="40" /> | Rune Blade | 14–17 | 3s | 2H | 30 | Disarm | Bladeweave |
| <img src="/img/items/0x13B6.png" class="uo-sprite" alt="" width="40" /> | Scimitar | 12–16 | 3s | 1H | 25 | Double Strike | Paralyzing Blow |
| <img src="/img/items/0x0907.png" class="uo-sprite" alt="" width="40" /> | Shortblade <sup>G·Fe</sup> | 10–13 | 2.25s | 1H | 45 | Armor Ignore | Mortal Strike |
| <img src="/img/items/0xA341.png" class="uo-sprite" alt="" width="40" /> | Skull Longsword <sup>G</sup> | 14–18 | 3.5s | 1H | 35 | Armor Ignore | Concussion Blow |
| <img src="/img/items/0x0900.png" class="uo-sprite" alt="" width="40" /> | Stone War Sword <sup>G</sup> | 15–19 | 3.75s | 1H | 40 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x13B8.png" class="uo-sprite" alt="" width="40" /> | Thin Longsword | 15–16 | 3.5s | 1H | 35 | — | — |
| <img src="/img/items/0x13B9.png" class="uo-sprite" alt="" width="40" /> | Viking Sword | 15–19 | 3.75s | 1H | 40 | Crushing Blow | Paralyzing Blow |
| <img src="/img/items/0x27A4.png" class="uo-sprite" alt="" width="40" /> | Wakizashi | 10–14 | 2.5s | 1H | 20 | Frenzied Whirlwind | Double Strike |


### Axes

**スキル:** [Swordsmanship](/ja/skills/swordsmanship/) · **武器数:** 14

斧も **Swordsmanship** を鍛えますが、高ダメージと高い必要筋力を持つ重い両手武器に偏ります。
多くは**伐採 (lumberjacking)** 道具を兼ね (hatchet、two-handed axe、large battle axe)、
lumberjack は斧ダメージにボーナスを得ます。war axe (<sup>Ma</sup>) は例外で、Mace Fighting を
鍛えます。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0F49.png" class="uo-sprite" alt="" width="40" /> | Axe | 14–17 | 3s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x0F47.png" class="uo-sprite" alt="" width="40" /> | Battle Axe | 16–19 | 3.5s | 2H | 35 | Bleed Attack | Concussion Blow |
| <img src="/img/items/0x0F4B.png" class="uo-sprite" alt="" width="40" /> | Double Axe | 15–18 | 3.25s | 2H | 45 | Double Strike | Whirlwind Attack |
| <img src="/img/items/0x08FD.png" class="uo-sprite" alt="" width="40" /> | Dual Short Axes <sup>G</sup> | 14–17 | 3s | 2H | 35 | Double Strike | Infectious Strike |
| <img src="/img/items/0x0F45.png" class="uo-sprite" alt="" width="40" /> | Executioners Axe | 15–18 | 3.25s | 2H | 40 | Bleed Attack | Mortal Strike |
| <img src="/img/items/0x48B2.png" class="uo-sprite" alt="" width="40" /> | Gargish Axe <sup>G</sup> | 14–17 | 3s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x48B0.png" class="uo-sprite" alt="" width="40" /> | Gargish Battle Axe <sup>G</sup> | 16–19 | 3.5s | 2H | 35 | Bleed Attack | Concussion Blow |
| <img src="/img/items/0x0F43.png" class="uo-sprite" alt="" width="40" /> | Hatchet | 13–16 | 2.75s | 2H | 20 | Armor Ignore | Disarm |
| <img src="/img/items/0x2D28.png" class="uo-sprite" alt="" width="40" /> | Heavy Ornate Axe | 17–20 | 3.75s | 2H | 45 | Disarm | Crushing Blow |
| <img src="/img/items/0x13FB.png" class="uo-sprite" alt="" width="40" /> | Large Battle Axe | 17–20 | 3.75s | 2H | 80 | Whirlwind Attack | Bleed Attack |
| <img src="/img/items/0x2D28.png" class="uo-sprite" alt="" width="40" /> | Ornate Axe | 17–20 | 3.75s | 2H | 45 | Disarm | Crushing Blow |
| <img src="/img/items/0x0E86.png" class="uo-sprite" alt="" width="40" /> | Pickaxe | 12–16 | 3s | 1H | 50 | Double Strike | Disarm |
| <img src="/img/items/0x1443.png" class="uo-sprite" alt="" width="40" /> | Two Handed Axe | 16–19 | 3.5s | 2H | 40 | Double Strike | Shadow Strike |
| <img src="/img/items/0x13B0.png" class="uo-sprite" alt="" width="40" /> | War Axe <sup>Ma</sup> | 12–16 | 3s | 1H | 35 | Armor Ignore | Bleed Attack |


### Maces & Hammers

**スキル:** [Mace Fighting](/ja/skills/mace-fighting/) · **武器数:** 20

メイスは **Mace Fighting** を鍛え、打撃ダメージを与えます。その特徴: プレイヤーに対して、
メイス武器はスタミナを削り、(古いルールセットでは) 防具の一部を無視できます。軽い club から
凶悪な両手 war hammer まで幅広く揃います。装飾的な「ワンド」品 (magic wand / fireworks wand) は
実際には打撃武器で、Wands 系統ではなくここに属します。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | A Fireworks Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x13B4.png" class="uo-sprite" alt="" width="40" /> | Club | 10–14 | 2.5s | 1H | 40 | Crushing Blow | Dismount |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Diamond Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x0903.png" class="uo-sprite" alt="" width="40" /> | Disc Mace <sup>G</sup> | 11–15 | 2.75s | 1H | 45 | Armor Ignore | Disarm |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Emerald Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x48C2.png" class="uo-sprite" alt="" width="40" /> | Gargish Maul <sup>G</sup> | 14–18 | 3.5s | 1H | 45 | Double Strike | Concussion Blow |
| <img src="/img/items/0x48CC.png" class="uo-sprite" alt="" width="40" /> | Gargish Tessen <sup>G</sup> | 10–13 | 2s | 2H | 10 | Feint | Dual Wield |
| <img src="/img/items/0x48C0.png" class="uo-sprite" alt="" width="40" /> | Gargish War Hammer <sup>G</sup> | 17–20 | 3.75s | 2H | 95 | Whirlwind Attack | Crushing Blow |
| <img src="/img/items/0x143D.png" class="uo-sprite" alt="" width="40" /> | Hammer Pick | 13–17 | 3.25s | 1H | 45 | Armor Ignore | Mortal Strike |
| <img src="/img/items/0x0F5C.png" class="uo-sprite" alt="" width="40" /> | Mace | 11–15 | 2.75s | 1H | 45 | Concussion Blow | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Magic Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x143B.png" class="uo-sprite" alt="" width="40" /> | Maul | 14–18 | 3.5s | 1H | 45 | Double Strike | Concussion Blow |
| <img src="/img/items/0x27AE.png" class="uo-sprite" alt="" width="40" /> | Nunchaku | 12–15 | 2.5s | 2H | 15 | Block | Double Strike |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Ruby Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x26BC.png" class="uo-sprite" alt="" width="40" /> | Scepter | 14–18 | 3.5s | 1H | 40 | Crushing Blow | Mortal Strike |
| <img src="/img/items/0x2D24.png" class="uo-sprite" alt="" width="40" /> | Silver-Etched Mace | 13–17 | 3.25s | 1H | 35 | Concussion Blow | Crushing Blow |
| <img src="/img/items/0x27A3.png" class="uo-sprite" alt="" width="40" /> | Tessen | 10–13 | 2s | 2H | 10 | Feint | Dual Wield |
| <img src="/img/items/0x27A6.png" class="uo-sprite" alt="" width="40" /> | Tetsubo | 12–15 | 2.5s | 2H | 35 | Frenzied Whirlwind | Crushing Blow |
| <img src="/img/items/0x1439.png" class="uo-sprite" alt="" width="40" /> | War Hammer | 17–20 | 3.75s | 2H | 95 | Whirlwind Attack | Crushing Blow |
| <img src="/img/items/0x1407.png" class="uo-sprite" alt="" width="40" /> | War Mace | 16–20 | 4s | 1H | 80 | Crushing Blow | Mortal Strike |


### Staves

**スキル:** [Mace Fighting](/ja/skills/mace-fighting/) · **武器数:** 10

quarterstaff、gnarled staff、black staff は両手の **Mace Fighting** 武器です。両手杖のアートでも
特定のキャスタービルドが成立するため、メイジやテイマーに人気があり、いくつかの gnarled staff は
ガーゴイルの *Force of Nature* 特殊技を備えています。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF0.png" class="uo-sprite" alt="" width="40" /> | Black Staff | 13–16 | 2.75s | 2H | 35 | Whirlwind Attack | Paralyzing Blow |
| <img src="/img/items/0x48B8.png" class="uo-sprite" alt="" width="40" /> | Gargish Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0xA347.png" class="uo-sprite" alt="" width="40" /> | Gargish Skull Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x0905.png" class="uo-sprite" alt="" width="40" /> | Glass Staff <sup>G</sup> | 11–14 | 2.25s | 2H | 20 | Double Strike | Mortal Strike |
| <img src="/img/items/0x13F8.png" class="uo-sprite" alt="" width="40" /> | Gnarled Staff | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x0E89.png" class="uo-sprite" alt="" width="40" /> | Quarter Staff | 11–14 | 2.25s | 2H | 30 | Double Strike | Concussion Blow |
| <img src="/img/items/0x0906.png" class="uo-sprite" alt="" width="40" /> | Serpent Stone Staff <sup>G</sup> | 16–19 | 3.5s | 2H | 35 | Crushing Blow | Dismount |
| <img src="/img/items/0x0E81.png" class="uo-sprite" alt="" width="40" /> | Shepherds Crook | 13–16 | 2.75s | 2H | 20 | Crushing Blow | Disarm |
| <img src="/img/items/0xA343.png" class="uo-sprite" alt="" width="40" /> | Skull Gnarled Staff <sup>G</sup> | 15–18 | 3.25s | 2H | 20 | Concussion Blow | Force of Nature |
| <img src="/img/items/0x2D25.png" class="uo-sprite" alt="" width="40" /> | Wild Staff | 10–13 | 2.25s | 1H | 15 | Block | Force of Nature |


### Daggers & Knives

**スキル:** [Fencing](/ja/skills/fencing/) · **武器数:** 17

軽量で非常に高速な **Fencing** 武器です。dagger はゲーム内のどの武器にも劣らない速さで振れ、
毒の付与と Infectious Strike 特殊技に優れます。解体ナイフ類 (butcher knife、cleaver、
skinning knife — <sup>Sw</sup> で印付け) はナイフ形ですが **Swordsmanship** を鍛え、皮剥ぎ道具を
兼ねます。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x2D21.png" class="uo-sprite" alt="" width="40" /> | Assassin Spike | 10–12 | 2s | 1H | 15 | Infectious Strike | Shadow Strike |
| <img src="/img/items/0x13F6.png" class="uo-sprite" alt="" width="40" /> | Butcher Knife <sup>Sw</sup> | 10–13 | 2.25s | 1H | 10 | Infectious Strike | Disarm |
| <img src="/img/items/0x0EC3.png" class="uo-sprite" alt="" width="40" /> | Cleaver <sup>Sw</sup> | 10–14 | 2.5s | 1H | 10 | Bleed Attack | Infectious Strike |
| <img src="/img/items/0x0F52.png" class="uo-sprite" alt="" width="40" /> | Dagger | 10–12 | 2s | 1H | 10 | Shadow Strike | Infectious Strike |
| <img src="/img/items/0x2D20.png" class="uo-sprite" alt="" width="40" /> | Elven Spellblade | 12–15 | 2.5s | 2H | 35 | Psychic Attack | Bleed Attack |
| <img src="/img/items/0x48B6.png" class="uo-sprite" alt="" width="40" /> | Gargish Butcher Knife <sup>G·Sw</sup> | 10–13 | 2.25s | 1H | 10 | Infectious Strike | Disarm |
| <img src="/img/items/0x48AE.png" class="uo-sprite" alt="" width="40" /> | Gargish Cleaver <sup>G·Sw</sup> | 10–14 | 2.5s | 1H | 10 | Bleed Attack | Infectious Strike |
| <img src="/img/items/0x0902.png" class="uo-sprite" alt="" width="40" /> | Gargish Dagger <sup>G</sup> | 10–12 | 2s | 1H | 10 | Shadow Strike | Infectious Strike |
| <img src="/img/items/0x48CE.png" class="uo-sprite" alt="" width="40" /> | Gargish Tekagi <sup>G</sup> | 10–13 | 2s | 2H | 10 | Dual Wield | Talon Strike |
| <img src="/img/items/0x27AD.png" class="uo-sprite" alt="" width="40" /> | Kama | 10–13 | 2s | 2H | 15 | Whirlwind Attack | Defense Mastery |
| <img src="/img/items/0x27A7.png" class="uo-sprite" alt="" width="40" /> | Lajatang | 16–19 | 3.5s | 2H | 65 | Defense Mastery | Frenzied Whirlwind |
| <img src="/img/items/0x2D22.png" class="uo-sprite" alt="" width="40" /> | Leafblade | 11–15 | 2.75s | 1H | 20 | Feint | Armor Ignore |
| <img src="/img/items/0x27AF.png" class="uo-sprite" alt="" width="40" /> | Sai | 10–13 | 2s | 2H | 15 | Dual Wield | Armor Pierce |
| <img src="/img/items/0x2D2F.png" class="uo-sprite" alt="" width="40" /> | Serrated War Cleaver | 10–13 | 2.25s | 2H | 15 | Disarm | Bladeweave |
| <img src="/img/items/0x0EC4.png" class="uo-sprite" alt="" width="40" /> | Skinning Knife <sup>Sw</sup> | 10–13 | 2.25s | 1H | 5 | Shadow Strike | Bleed Attack |
| <img src="/img/items/0x27AB.png" class="uo-sprite" alt="" width="40" /> | Tekagi | 10–13 | 2s | 2H | 10 | Dual Wield | Talon Strike |
| <img src="/img/items/0x2D2F.png" class="uo-sprite" alt="" width="40" /> | War Cleaver | 10–13 | 2.25s | 2H | 15 | Disarm | Bladeweave |


### Spears & Forks

**スキル:** [Fencing](/ja/skills/fencing/) · **武器数:** 11

spear、pike、war fork は刺突の **Fencing** 武器で、ほとんどが両手でリーチ型の良好なダメージを
持ちます。bladed staff (<sup>Sw</sup>) は spear の土台の上に作られますが Swordsmanship を
鍛えます。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x26BD.png" class="uo-sprite" alt="" width="40" /> | Bladed Staff <sup>Sw</sup> | 14–17 | 3s | 2H | 40 | Armor Ignore | Dismount |
| <img src="/img/items/0x26BF.png" class="uo-sprite" alt="" width="40" /> | Double Bladed Staff | 11–14 | 2.25s | 2H | 50 | Double Strike | Infectious Strike |
| <img src="/img/items/0x0904.png" class="uo-sprite" alt="" width="40" /> | Dual Pointed Spear <sup>G</sup> | 11–14 | 2.25s | 2H | 50 | Double Strike | Disarm |
| <img src="/img/items/0x48C8.png" class="uo-sprite" alt="" width="40" /> | Gargish Pike <sup>G</sup> | 14–17 | 3s | 2H | 50 | Paralyzing Blow | Infectious Strike |
| <img src="/img/items/0x48BE.png" class="uo-sprite" alt="" width="40" /> | Gargish War Fork <sup>G</sup> | 10–14 | 2.5s | 1H | 45 | Bleed Attack | Disarm |
| <img src="/img/items/0x26BE.png" class="uo-sprite" alt="" width="40" /> | Pike | 14–17 | 3s | 2H | 50 | Paralyzing Blow | Infectious Strike |
| <img src="/img/items/0x0E87.png" class="uo-sprite" alt="" width="40" /> | Pitchfork | 12–15 | 2.5s | 2H | 55 | Bleed Attack | Dismount |
| <img src="/img/items/0x1403.png" class="uo-sprite" alt="" width="40" /> | Short Spear | 10–13 | 2s | 2H | 40 | Shadow Strike | Mortal Strike |
| <img src="/img/items/0x0F62.png" class="uo-sprite" alt="" width="40" /> | Spear | 13–16 | 2.75s | 2H | 50 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x0F62.png" class="uo-sprite" alt="" width="40" /> | Tribal Spear | 13–15 | 2.75s | 2H | 50 | Armor Ignore | Paralyzing Blow |
| <img src="/img/items/0x1405.png" class="uo-sprite" alt="" width="40" /> | War Fork | 10–14 | 2.5s | 1H | 45 | Bleed Attack | Disarm |


### Polearms

**スキル:** [Swordsmanship](/ja/skills/swordsmanship/) · **武器数:** 5

bardiche、halberd、scythe は巨大な両手の **Swordsmanship** 長柄武器です — 近接で最高の基礎
ダメージと必要筋力を持つ代わりに、振り速度が遅いという代償があります。whirlwind/範囲ダメージの
定番です。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0F4D.png" class="uo-sprite" alt="" width="40" /> | Bardiche | 17–20 | 3.75s | 2H | 45 | Paralyzing Blow | Dismount |
| <img src="/img/items/0x48B4.png" class="uo-sprite" alt="" width="40" /> | Gargish Bardiche <sup>G</sup> | 17–20 | 3.75s | 2H | 45 | Paralyzing Blow | Dismount |
| <img src="/img/items/0x48C4.png" class="uo-sprite" alt="" width="40" /> | Gargish Scythe <sup>G</sup> | 16–19 | 3.5s | 2H | 45 | Bleed Attack | Paralyzing Blow |
| <img src="/img/items/0x143E.png" class="uo-sprite" alt="" width="40" /> | Halberd | 18–21 | 4s | 2H | 95 | Whirlwind Attack | Concussion Blow |
| <img src="/img/items/0x26BA.png" class="uo-sprite" alt="" width="40" /> | Scythe | 16–19 | 3.5s | 2H | 45 | Bleed Attack | Paralyzing Blow |


### Bows & Crossbows

**スキル:** [Archery](/ja/skills/archery/) · **武器数:** 11

遠隔の **Archery** 武器です。すべての弓とクロスボウは両手で、空いた手を必要とし (盾は不可)、
弾薬を消費します — 弓には矢、クロスボウにはボルトです。重いクロスボウは強く命中しますが遅く
振り、repeating crossbow や shortbow はダメージと引き換えに速さを得ます。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | An Orcish Bow | 17–21 | 4.25s | 2H | 30 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | Bow | 17–21 | 4.25s | 2H | 30 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x26C2.png" class="uo-sprite" alt="" width="40" /> | Composite Bow | 16–20 | 4s | 2H | 45 | Armor Ignore | Moving Shot |
| <img src="/img/items/0x0F50.png" class="uo-sprite" alt="" width="40" /> | Crossbow | 18–22 | 4.5s | 2H | 35 | Concussion Blow | Mortal Strike |
| <img src="/img/items/0x2D1E.png" class="uo-sprite" alt="" width="40" /> | Elven Composite Longbow | 15–19 | 3.75s | 2H | 45 | Force Arrow | Serpent Arrow |
| <img src="/img/items/0x13FD.png" class="uo-sprite" alt="" width="40" /> | Heavy Crossbow | 20–24 | 5s | 2H | 80 | Moving Shot | Dismount |
| <img src="/img/items/0x13B2.png" class="uo-sprite" alt="" width="40" /> | Juka Bow | 17–21 | 4.25s | 2H | 100 | Paralyzing Blow | Mortal Strike |
| <img src="/img/items/0x2D2B.png" class="uo-sprite" alt="" width="40" /> | Lightweight Shortbow | 12–16 | 3s | 2H | 45 | Lightning Arrow | Psychic Attack |
| <img src="/img/items/0x2D2B.png" class="uo-sprite" alt="" width="40" /> | Magical Shortbow | 12–16 | 3s | 2H | 45 | Lightning Arrow | Psychic Attack |
| <img src="/img/items/0x26C3.png" class="uo-sprite" alt="" width="40" /> | Repeating Crossbow | 11–15 | 2.75s | 2H | 30 | Double Strike | Moving Shot |
| <img src="/img/items/0x27A5.png" class="uo-sprite" alt="" width="40" /> | Yumi | 13–17 | 3.25s | 2H | 35 | Armor Pierce | Double Shot |


### Thrown

**スキル:** [Throwing](/ja/skills/throwing/) · **武器数:** 3

ガーゴイル専用の **Throwing** 武器 (boomerang、cyclone、soul glaive)。archery のように遠隔で
投擲しますが Throwing スキルが統括し、Strength の高さで射程が伸びます。片手です。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x08FF.png" class="uo-sprite" alt="" width="40" /> | Boomerang <sup>G</sup> | 11–15 | 2.75s | 1H | 25 | Mystic Arc | Concussion Blow |
| <img src="/img/items/0x0901.png" class="uo-sprite" alt="" width="40" /> | Cyclone <sup>G</sup> | 13–17 | 3.25s | 1H | 40 | Moving Shot | Infused Throw |
| <img src="/img/items/0x090A.png" class="uo-sprite" alt="" width="40" /> | Soul Glaive <sup>G</sup> | 16–20 | 4s | 1H | 60 | Armor Ignore | Mortal Strike |


### Wands

**スキル:** [Mace Fighting](/ja/skills/mace-fighting/) · **武器数:** 11

ワンドは片手の **Mace Fighting** 武器で、魔法チャージ (Heal、Harm、Fireball など) も保持します。
近接武器としては一様に弱く (9–11 ダメージ、低い必要筋力)、`BaseWand` から受け継いだ
Dismount/Disarm の特殊技セットを持ちます。その価値は呪文チャージにあり、振りにはありません。

| アイコン | 武器 | ダメージ | 速度 | 手 | 筋力 | 一次 | 二次 |
|---|---|---|---|---|---|---|---|
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Clumsy Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Feeble Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Fireball Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Greater Heal Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Harm Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Heal Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Id Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Lightning Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Magic Arrow Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Mana Drain Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |
| <img src="/img/items/0x0DF2.png" class="uo-sprite" alt="" width="40" /> | Weakness Wand | 9–11 | 2.75s | 1H | 5 | Dismount | Disarm |


## 関連項目

- [戦闘の基礎](/ja/playing/combat-basics/) と [戦闘上級](/ja/playing/combat-advanced/) — 振り、命中率、ダメージ、特殊技がどう解決されるか
- [Swordsmanship](/ja/skills/swordsmanship/) · [Mace Fighting](/ja/skills/mace-fighting/) · [Fencing](/ja/skills/fencing/) · [Archery](/ja/skills/archery/) — 戦闘スキル
- [Tactics](/ja/skills/tactics/) と [Anatomy](/ja/skills/anatomy/) — すべての戦士が携える汎用ダメージスキル
- [7×GM 戦士テンプレート](/ja/templates/seven-gm/) — 完成された近接ビルド
- [Blacksmithy](/ja/crafting/blacksmithy/) と [Bowfletching](/ja/crafting/bowfletching/) — 自分の武器を作る
- [武器カタログ](/ja/items/catalog/weapons/) — 時代ごとの全武器、アートとアイテム ID 付き
