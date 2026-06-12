#!/usr/bin/env python3
"""Shared UI-string label dictionary for the locale-aware page generators.

The generators (gen_bestiary.py, gen_items.py, gen_spells.py, gen_crafting.py)
write English pages to src/content/docs/<section>/ and Korean/Japanese copies to
src/content/docs/ko/<section>/ and .../ja/<section>/. Only *UI chrome* is
translated — section headings, table column headers, group names and intro/
description prose. Proper nouns stay English: creature names, item names, spell
names and mantras, weapon-family subcategory names, and all numbers/IDs/art.

Korean & Japanese terms follow tools/i18n_glossary.md (the official UO client
terms) wherever skills/stats/reagents appear.

Public API:
    LOCALES                       — ['en', 'ko', 'ja']
    L(locale, key, **fmt)         — localized string for `key`, English fallback.
                                    If kwargs are given, the result is .format()ed.
    SKILL(locale, english_name)   — official localized skill name (English fallback).
    locale_prefix(locale)         — '' for en, '/ko' or '/ja' otherwise. Prefix
                                    internal links with this.
"""

LOCALES = ["en", "ko", "ja"]


def locale_prefix(locale):
    """Internal-link prefix for a locale ('' for the default English locale)."""
    return "" if locale == "en" else "/" + locale


# ---------------------------------------------------------------------------
# Official skill names (from tools/i18n_glossary.md — Cliloc.kor / Cliloc.jpn).
# Keyed by the English skill name as it appears in the generators/data.
# ---------------------------------------------------------------------------
SKILLS = {
    "Alchemy": {"ko": "연금술", "ja": "錬金術"},
    "Anatomy": {"ko": "해부학", "ja": "解剖学"},
    "Animal Lore": {"ko": "동물학", "ja": "動物学"},
    "Item Identification": {"ko": "물건 감정", "ja": "鑑定"},
    "Arms Lore": {"ko": "병기학", "ja": "武器学"},
    "Parrying": {"ko": "방패술", "ja": "受け流し"},
    "Begging": {"ko": "구걸술", "ja": "物乞い"},
    "Blacksmithing": {"ko": "대장술", "ja": "鍛冶"},
    "Blacksmith": {"ko": "대장술", "ja": "鍛冶"},
    "Blacksmithy": {"ko": "대장술", "ja": "鍛冶"},
    "Fletching": {"ko": "궁시 제작술", "ja": "弓矢工"},
    "Bow Fletching": {"ko": "궁시 제작술", "ja": "弓矢工"},
    "Bowcraft/Fletching": {"ko": "궁시 제작술", "ja": "弓矢工"},
    "Peacemaking": {"ko": "평화 유지", "ja": "沈静化"},
    "Camping": {"ko": "야영술", "ja": "野営"},
    "Carpentry": {"ko": "목공술", "ja": "大工"},
    "Cartography": {"ko": "지도 제작술", "ja": "測量"},
    "Cooking": {"ko": "요리술", "ja": "調理"},
    "Detecting Hidden": {"ko": "은신 감지", "ja": "探知"},
    "Discordance": {"ko": "불협화음", "ja": "不調和"},
    "Eval Intelligence": {"ko": "지능 평가", "ja": "評価"},
    "Healing": {"ko": "치료술", "ja": "治療"},
    "Fishing": {"ko": "낚시", "ja": "釣り"},
    "Forensics": {"ko": "법의학", "ja": "検死"},
    "Forensic Evaluation": {"ko": "법의학", "ja": "検死"},
    "Herding": {"ko": "목동술", "ja": "牧羊"},
    "Hiding": {"ko": "은신술", "ja": "隠蔽"},
    "Provocation": {"ko": "연주 도발", "ja": "扇動"},
    "Inscription": {"ko": "기록술", "ja": "書写"},
    "Inscribe": {"ko": "기록술", "ja": "書写"},
    "Lock Picking": {"ko": "자물쇠 따기", "ja": "開錠"},
    "Lockpicking": {"ko": "자물쇠 따기", "ja": "開錠"},
    "Magery": {"ko": "마법학", "ja": "魔法"},
    "Resisting Spells": {"ko": "마법 저항", "ja": "耐性"},
    "MagicResist": {"ko": "마법 저항", "ja": "耐性"},
    "Tactics": {"ko": "전술", "ja": "戦術"},
    "Snooping": {"ko": "훔쳐보기", "ja": "詮索"},
    "Musicianship": {"ko": "음악 연주", "ja": "音楽"},
    "Poisoning": {"ko": "중독술", "ja": "毒"},
    "Archery": {"ko": "궁술", "ja": "弓術"},
    "Spirit Speak": {"ko": "심령술", "ja": "霊話"},
    "SpiritSpeak": {"ko": "심령술", "ja": "霊話"},
    "Stealing": {"ko": "훔치기", "ja": "窃盗"},
    "Tailoring": {"ko": "재봉술", "ja": "裁縫"},
    "Animal Taming": {"ko": "동물 조련술", "ja": "調教"},
    "AnimalTaming": {"ko": "동물 조련술", "ja": "調教"},
    "Taming": {"ko": "동물 조련술", "ja": "調教"},
    "Taste Identification": {"ko": "맛 감정", "ja": "味見"},
    "TasteID": {"ko": "맛 감정", "ja": "味見"},
    "Tinkering": {"ko": "기계공학", "ja": "細工"},
    "Tracking": {"ko": "추적술", "ja": "追跡"},
    "Veterinary": {"ko": "수의학", "ja": "獣医学"},
    "Swordsmanship": {"ko": "검술", "ja": "剣術"},
    "Swords": {"ko": "검술", "ja": "剣術"},
    "Mace Fighting": {"ko": "곤봉술", "ja": "棍術"},
    "Macing": {"ko": "곤봉술", "ja": "棍術"},
    "Fencing": {"ko": "펜싱", "ja": "槍術"},
    "Wrestling": {"ko": "레슬링", "ja": "格闘"},
    "Lumberjacking": {"ko": "벌목술", "ja": "伐採"},
    "Mining": {"ko": "채광", "ja": "採掘"},
    "Meditation": {"ko": "명상", "ja": "瞑想"},
    "Stealth": {"ko": "잠행", "ja": "隠密"},
    "Remove Trap": {"ko": "함정 해제", "ja": "罠解除"},
    "RemoveTrap": {"ko": "함정 해제", "ja": "罠解除"},
    "Necromancy": {"ko": "강령술", "ja": "霊媒"},
    "Focus": {"ko": "집중", "ja": "集中"},
    "Chivalry": {"ko": "기사도", "ja": "騎士道"},
    "Bushido": {"ko": "무사도", "ja": "武士道"},
    "Ninjitsu": {"ko": "인술", "ja": "忍術"},
    "Spellweaving": {"ko": "주문조합", "ja": "織成呪文"},
    "Mysticism": {"ko": "신비술", "ja": "神秘"},
    "Throwing": {"ko": "투척술", "ja": "投擲"},
}


def SKILL(locale, name):
    """Official localized skill name; falls back to the English `name`."""
    if locale == "en" or name is None:
        return name
    entry = SKILLS.get(name)
    if entry and locale in entry:
        return entry[locale]
    return name


# ---------------------------------------------------------------------------
# UI label dictionary. Keys are stable identifiers used by the generators; the
# English value is the canonical wording and the fallback. Phrases that take
# runtime values use {placeholders} resolved via L(locale, key, **fmt).
# ---------------------------------------------------------------------------
LABELS = {
    # --- Generic table column headers -------------------------------------
    "col.icon": {"en": "Icon", "ko": "아이콘", "ja": "アイコン"},
    "col.name": {"en": "Name", "ko": "이름", "ja": "名前"},
    "col.creature": {"en": "Creature", "ko": "크리처", "ja": "クリーチャー"},
    "col.group": {"en": "Group", "ko": "그룹", "ja": "グループ"},
    "col.creatures": {"en": "Creatures", "ko": "크리처 수", "ja": "クリーチャー数"},
    "col.hits": {"en": "Hits", "ko": "체력", "ja": "ヒットポイント"},
    "col.damage": {"en": "Damage", "ko": "데미지", "ja": "ダメージ"},
    "col.tamable": {"en": "Tamable", "ko": "테이밍 가능", "ja": "テイム可"},
    "col.min_taming": {"en": "Min taming", "ko": "최소 조련술", "ja": "最低調教"},
    "col.slots": {"en": "Slots", "ko": "슬롯", "ja": "スロット"},
    "col.item": {"en": "Item", "ko": "아이템", "ja": "アイテム"},
    "col.item_id": {"en": "Item ID", "ko": "아이템 ID", "ja": "アイテムID"},
    "col.weight": {"en": "Weight", "ko": "무게", "ja": "重量"},
    "col.skill": {"en": "Skill", "ko": "스킬", "ja": "スキル"},
    "col.materials": {"en": "Materials", "ko": "재료", "ja": "材料"},
    "col.era": {"en": "Era", "ko": "시대", "ja": "時代"},
    "col.category": {"en": "Category", "ko": "카테고리", "ja": "カテゴリ"},
    "col.items": {"en": "Items", "ko": "아이템 수", "ja": "アイテム数"},
    "col.slot": {"en": "Slot", "ko": "슬롯", "ja": "スロット"},
    "col.spell": {"en": "Spell", "ko": "주문", "ja": "呪文"},
    "col.circle": {"en": "Circle", "ko": "서클", "ja": "サークル"},
    "col.mana": {"en": "Mana", "ko": "마나", "ja": "マナ"},
    "col.reagents": {"en": "Reagents", "ko": "시약", "ja": "試薬"},
    "col.words_of_power": {"en": "Words of power", "ko": "마법 주문", "ja": "力の言葉"},
    "col.value": {"en": "Value", "ko": "수치", "ja": "値"},
    "col.stat": {"en": "Stat", "ko": "능력치", "ja": "ステータス"},
    "col.craft_system": {"en": "Craft system", "ko": "제작 시스템", "ja": "クラフトシステム"},
    "col.main_skill": {"en": "Main skill", "ko": "주요 스킬", "ja": "メインスキル"},
    "col.recipes": {"en": "Recipes", "ko": "레시피", "ja": "レシピ"},
    "col.total": {"en": "Total", "ko": "합계", "ja": "合計"},
    "cell.yes": {"en": "yes", "ko": "가능", "ja": "可"},

    # --- Bestiary group names ---------------------------------------------
    "group.animals": {"en": "Animals", "ko": "동물", "ja": "動物"},
    "group.monsters": {"en": "Monsters", "ko": "몬스터", "ja": "モンスター"},
    "group.humanoids": {"en": "Humanoids", "ko": "휴머노이드", "ja": "人型"},
    "group.undead": {"en": "Undead", "ko": "언데드", "ja": "アンデッド"},
    "group.elementals": {"en": "Elementals", "ko": "정령", "ja": "エレメンタル"},
    "group.sea": {"en": "Sea Creatures", "ko": "바다 생물", "ja": "海洋生物"},
    "group.bosses": {"en": "Bosses & Champions", "ko": "보스 & 챔피언", "ja": "ボス & チャンピオン"},

    # --- Monster sub-bucket names -----------------------------------------
    "bucket.Dragons & Wyrms": {"en": "Dragons & Wyrms", "ko": "드래곤 & 웜", "ja": "ドラゴン & ワーム"},
    "bucket.Daemons & Fiends": {"en": "Daemons & Fiends", "ko": "데몬 & 마물", "ja": "デーモン & 魔物"},
    "bucket.Reptiles & Serpents": {"en": "Reptiles & Serpents", "ko": "파충류 & 뱀", "ja": "爬虫類 & 蛇"},
    "bucket.Beasts & Hounds": {"en": "Beasts & Hounds", "ko": "야수 & 사냥개", "ja": "獣 & 猟犬"},
    "bucket.Insects & Arachnids": {"en": "Insects & Arachnids", "ko": "곤충 & 거미류", "ja": "昆虫 & クモ類"},
    "bucket.Magical & Fey": {"en": "Magical & Fey", "ko": "마법 생물 & 요정", "ja": "魔法生物 & 妖精"},
    "bucket.Goblins & Gremlins": {"en": "Goblins & Gremlins", "ko": "고블린 & 그렘린", "ja": "ゴブリン & グレムリン"},
    "bucket.Gazers & Aberrations": {"en": "Gazers & Aberrations", "ko": "게이저 & 기형 생물", "ja": "ゲイザー & 異形"},
    "bucket.Tokuno & Eastern": {"en": "Tokuno & Eastern", "ko": "토쿠노 & 동방", "ja": "トクノ & 東方"},
    "bucket.Birds & Harpies": {"en": "Birds & Harpies", "ko": "조류 & 하피", "ja": "鳥類 & ハーピー"},
    "bucket.Slimes & Oozes": {"en": "Slimes & Oozes", "ko": "슬라임 & 점액", "ja": "スライム & ウーズ"},
    "bucket.Plants & Fungi": {"en": "Plants & Fungi", "ko": "식물 & 균류", "ja": "植物 & 菌類"},
    "bucket.Giants & Brutes": {"en": "Giants & Brutes", "ko": "거인 & 흉포 생물", "ja": "巨人 & 凶暴生物"},
    "bucket.Other Monsters": {"en": "Other Monsters", "ko": "기타 몬스터", "ja": "その他のモンスター"},

    # --- Bestiary section headings & prose --------------------------------
    "bestiary.title": {"en": "Bestiary", "ko": "몬스터 도감", "ja": "モンスター図鑑"},
    "bestiary.index_desc": {
        "en": "Creature reference for our shard — {n} creatures extracted from ServUO source.",
        "ko": "우리 샤드의 크리처 레퍼런스 — ServUO 소스에서 추출한 {n}종의 크리처.",
        "ja": "本シャードのクリーチャーリファレンス — ServUO ソースから抽出した {n} 種のクリーチャー。",
    },
    "bestiary.intro": {
        # EN preserves the original hard line-wrapping (byte-identical output).
        "en": "Stats for **{n} creatures**, extracted directly from the ServUO scripts that\n"
              "run this shard (`Scripts/Mobiles/`). Every page is generated — to fix an error,\n"
              "file a discrepancy report; never hand-edit these pages.",
        "ko": "이 샤드를 구동하는 ServUO 스크립트(`Scripts/Mobiles/`)에서 직접 추출한 "
              "**{n}종 크리처**의 스탯입니다. 모든 페이지는 자동 생성됩니다 — 오류를 고치려면 "
              "불일치 보고서를 제출하세요. 이 페이지를 직접 수정하지 마세요.",
        "ja": "本シャードを動かす ServUO スクリプト(`Scripts/Mobiles/`)から直接抽出した "
              "**{n} 種のクリーチャー**のステータスです。すべてのページは自動生成されます — "
              "誤りを修正するには不一致レポートを提出してください。ページを直接編集しないでください。",
    },
    "bestiary.groups": {"en": "Groups", "ko": "그룹", "ja": "グループ"},
    "bestiary.notable_tamables": {"en": "Notable tamables", "ko": "주목할 만한 테이밍 대상", "ja": "注目のテイム可能クリーチャー"},
    "bestiary.tamables_intro": {
        "en": "The hardest tames on the shard, by minimum Animal Taming skill.",
        "ko": "최소 동물 조련술 기준으로, 이 샤드에서 가장 길들이기 어려운 크리처입니다.",
        "ja": "最低調教スキル順に、本シャードで最もテイムが難しいクリーチャーです。",
    },
    "bestiary.all_tamable": {
        # EN preserves the original two-line wrapping.
        "en": "All {n} tamable creatures have a\n**Taming** section on their page.",
        "ko": "{n}종의 테이밍 가능 크리처는 모두 페이지에 **테이밍** 섹션이 있습니다.",
        "ja": "{n} 種のテイム可能クリーチャーはすべてページに**テイム**セクションがあります。",
    },
    "bestiary.group_desc": {
        "en": "{group} — {n} creatures, stats from ServUO source.",
        "ko": "{group} — {n}종 크리처, ServUO 소스 기준 스탯.",
        "ja": "{group} — {n} 種のクリーチャー、ServUO ソース由来のステータス。",
    },
    "bestiary.grouped_by_type": {
        "en": "Grouped by creature type. ServUO doesn't tag creatures with an "
              "introduction era, so they're grouped by kind (dragons, daemons, "
              "beasts, …) rather than by expansion.",
        "ko": "크리처 종류별로 분류했습니다. ServUO는 크리처에 도입 시대를 표시하지 않으므로 "
              "확장팩이 아닌 종류(드래곤, 데몬, 야수 등)별로 묶었습니다.",
        "ja": "クリーチャーの種類別に分類しています。ServUO はクリーチャーに導入時代を付与しないため、"
              "拡張ではなく種類(ドラゴン、デーモン、獣など)別にまとめています。",
    },
    # creature-page sections
    "sect.stats": {"en": "Stats", "ko": "스탯", "ja": "ステータス"},
    "sect.resistances": {"en": "Resistances", "ko": "저항력", "ja": "耐性"},
    "sect.skills": {"en": "Skills", "ko": "스킬", "ja": "スキル"},
    "sect.appearance": {"en": "Appearance", "ko": "외형", "ja": "外見"},
    "sect.sounds": {"en": "Sounds", "ko": "사운드", "ja": "サウンド"},
    "sect.loot_resources": {"en": "Loot & resources", "ko": "전리품 & 자원", "ja": "戦利品 & 資源"},
    "sect.taming": {"en": "Taming", "ko": "테이밍", "ja": "テイム"},
    "row.strength": {"en": "Strength", "ko": "힘", "ja": "STR"},
    "row.dexterity": {"en": "Dexterity", "ko": "민첩성", "ja": "DEX"},
    "row.intelligence": {"en": "Intelligence", "ko": "지능", "ja": "INT"},
    "row.stamina": {"en": "Stamina", "ko": "기력", "ja": "スタミナ"},
    "row.mana": {"en": "Mana", "ko": "마나", "ja": "マナ"},
    "row.damage_type": {"en": "Damage type", "ko": "데미지 타입", "ja": "ダメージタイプ"},
    "res.physical": {"en": "Physical", "ko": "물리", "ja": "物理"},
    "res.fire": {"en": "Fire", "ko": "화염", "ja": "火"},
    "res.cold": {"en": "Cold", "ko": "냉기", "ja": "冷気"},
    "res.poison": {"en": "Poison", "ko": "독", "ja": "毒"},
    "res.energy": {"en": "Energy", "ko": "에너지", "ja": "エネルギー"},
    "fact.in_game_name": {"en": "In-game name", "ko": "게임 내 이름", "ja": "ゲーム内名称"},
    "fact.corpse": {"en": "Corpse", "ko": "시체", "ja": "死体"},
    "fact.body_id": {"en": "Body ID", "ko": "바디 ID", "ja": "ボディID"},
    "fact.base_sound_id": {"en": "Base sound ID", "ko": "기본 사운드 ID", "ja": "基本サウンドID"},
    "fact.ai": {"en": "AI", "ko": "AI", "ja": "AI"},
    "fact.fight_mode": {"en": "Fight mode", "ko": "전투 모드", "ja": "戦闘モード"},
    "fact.fame": {"en": "Fame", "ko": "명성", "ja": "名声"},
    "fact.karma": {"en": "Karma", "ko": "카르마", "ja": "カルマ"},
    "fact.virtual_armor": {"en": "Virtual armor", "ko": "가상 방어구", "ja": "仮想アーマー"},
    "fact.script": {"en": "Script", "ko": "스크립트", "ja": "スクリプト"},
    "fact.random_name": {
        "en": "random (`{list}` name list)",
        "ko": "무작위 (`{list}` 이름 목록)",
        "ja": "ランダム (`{list}` 名前リスト)",
    },
    "row.meat": {"en": "Meat", "ko": "고기", "ja": "肉"},
    "row.hides": {"en": "Hides", "ko": "가죽", "ja": "皮"},
    "row.feathers": {"en": "Feathers", "ko": "깃털", "ja": "羽根"},
    "row.wool": {"en": "Wool", "ko": "양모", "ja": "羊毛"},
    "row.loot_pack": {"en": "Loot pack", "ko": "전리품 팩", "ja": "戦利品パック"},
    "row.count": {"en": "Count", "ko": "개수", "ja": "数"},
    "appearance.carve": {"en": "Carve: {parts}.", "ko": "해체: {parts}.", "ja": "解体: {parts}。"},
    "appearance.gold": {"en": "Gold: {v}", "ko": "골드: {v}", "ja": "ゴールド: {v}"},
    "appearance.pack_items": {
        "en": "Pack items (some chance-based): {items}",
        "ko": "팩 아이템 (일부 확률 기반): {items}",
        "ja": "パックアイテム(一部は確率制): {items}",
    },
    "appearance.paperdoll_ref": {
        "en": "See the [paperdoll layer reference]({prefix}/reference/paperdoll/) for how "
              "equipment is composited.",
        "ko": "장비가 어떻게 합성되는지는 [페이퍼돌 레이어 레퍼런스]({prefix}/reference/paperdoll/)를 참고하세요.",
        "ja": "装備がどのように合成されるかは[ペーパードール レイヤー リファレンス]({prefix}/reference/paperdoll/)を参照してください。",
    },
    "appearance.note.random": {"en": "random", "ko": "무작위", "ja": "ランダム"},
    "appearance.note.dyed": {"en": "dyed", "ko": "염색", "ja": "染色"},
    "sound.anger": {"en": "Anger", "ko": "분노", "ja": "怒り"},
    "sound.idle": {"en": "Idle", "ko": "대기", "ja": "待機"},
    "sound.attack": {"en": "Attack", "ko": "공격", "ja": "攻撃"},
    "sound.hurt": {"en": "Hurt", "ko": "피격", "ja": "被弾"},
    "sound.death": {"en": "Death", "ko": "죽음", "ja": "死亡"},
    "taming.min_skill": {"en": "Min taming skill", "ko": "최소 조련술", "ja": "最低調教スキル"},
    "taming.control_slots": {"en": "Control slots", "ko": "컨트롤 슬롯", "ja": "コントロールスロット"},

    # --- Item catalog -----------------------------------------------------
    "items.title": {"en": "Item Catalog", "ko": "아이템 도감", "ja": "アイテムカタログ"},
    "items.index_desc": {
        "en": "Image-rich catalog of every item in the ServUO source, grouped by gameplay type.",
        "ko": "ServUO 소스의 모든 아이템을 게임플레이 유형별로 분류한 이미지 위주의 도감입니다.",
        "ja": "ServUO ソースのすべてのアイテムをゲームプレイ種別ごとに分類した画像中心のカタログです。",
    },
    "items.index_intro": {
        "en": "A complete, auto-generated catalog of every concrete item class in the "
              "ServUO source — {total} items across {ncat} gameplay categories. Items are "
              "classified by gameplay type (weapons by family, armor by material, shields, "
              "jewelry, clothing, and so on) rather than by source directory. Each category "
              "page lists items with their client art, item ID and weight, grouped by "
              "subcategory.",
        "ko": "ServUO 소스의 모든 구체 아이템 클래스를 자동 생성한 완전한 도감입니다 — "
              "{ncat}개 게임플레이 카테고리에 걸친 {total}개 아이템. 아이템은 소스 디렉터리가 아닌 "
              "게임플레이 유형(무기는 계열별, 방어구는 재질별, 방패, 장신구, 의류 등)으로 분류됩니다. "
              "각 카테고리 페이지는 아이템을 클라이언트 아트, 아이템 ID, 무게와 함께 하위 카테고리별로 "
              "나열합니다.",
        "ja": "ServUO ソースのすべての具象アイテムクラスを自動生成した完全なカタログです — "
              "{ncat} のゲームプレイカテゴリにまたがる {total} アイテム。アイテムはソースディレクトリ"
              "ではなくゲームプレイ種別(武器は系統別、防具は素材別、盾、装身具、衣類など)で分類されます。"
              "各カテゴリページはアイテムをクライアントアート、アイテムID、重量とともにサブカテゴリ別に"
              "列挙します。",
    },
    "items.index_regen": {
        "en": "This catalog is regenerated from `data/items.json` by `tools/gen_items.py`; "
              "do not hand-edit the category pages.",
        "ko": "이 도감은 `tools/gen_items.py`가 `data/items.json`에서 재생성합니다. "
              "카테고리 페이지를 직접 수정하지 마세요.",
        "ja": "このカタログは `tools/gen_items.py` が `data/items.json` から再生成します。"
              "カテゴリページを直接編集しないでください。",
    },
    "items.cat_desc": {
        "en": "Every {category} item in the ServUO source ({n}) — {blurb} — grouped by the "
              "expansion era it was introduced in, with art, item IDs and weights.",
        "ko": "ServUO 소스의 모든 {category} 아이템({n}개) — {blurb} — 도입된 확장팩 시대별로 "
              "분류했으며, 아트, 아이템 ID, 무게가 포함됩니다.",
        "ja": "ServUO ソースのすべての {category} アイテム({n} 個) — {blurb} — 導入された拡張時代別に"
              "分類し、アート、アイテムID、重量を掲載しています。",
    },
    "items.cat_intro": {
        "en": "Auto-generated catalog of every {category} — {blurb} ({n} items), **grouped by "
              "the game era each was introduced in** (oldest first). Era is derived from the "
              "ServUO craft definitions; items with no determinable era are listed last. Icons "
              "are static client art.",
        "ko": "모든 {category}의 자동 생성 도감입니다 — {blurb} ({n}개 아이템), **각 아이템이 도입된 "
              "게임 시대별로 분류**(오래된 순). 시대는 ServUO 제작 정의에서 도출되며, 시대를 판별할 수 "
              "없는 아이템은 마지막에 나열됩니다. 아이콘은 정적 클라이언트 아트입니다.",
        "ja": "すべての {category} の自動生成カタログです — {blurb} ({n} アイテム)、**各アイテムが導入"
              "されたゲーム時代別に分類**(古い順)。時代は ServUO のクラフト定義から導出され、時代を判別"
              "できないアイテムは最後に列挙されます。アイコンは静的なクライアントアートです。",
    },
    "items.era_untagged": {"en": "Era not determined", "ko": "시대 미확정", "ja": "時代未確定"},
    "items.untagged_note": {
        "en": "Not craftable, so the source gives no introduction era (many are loot, "
              "artifacts, or world items).",
        "ko": "제작 불가능하여 소스에 도입 시대가 없습니다(상당수가 전리품, 아티팩트, 월드 아이템입니다).",
        "ja": "クラフト不可のためソースに導入時代がありません(多くは戦利品、アーティファクト、"
              "ワールドアイテムです)。",
    },
    "items.all_label": {"en": "All", "ko": "전체", "ja": "すべて"},
    # item subcategories translatable via glossary / generic terms
    "isub.Swords": {"en": "Swords", "ko": "검", "ja": "剣"},
    "isub.Axes": {"en": "Axes", "ko": "도끼", "ja": "斧"},
    "isub.Maces & Hammers": {"en": "Maces & Hammers", "ko": "철퇴 & 망치", "ja": "メイス & ハンマー"},
    "isub.Staves": {"en": "Staves", "ko": "지팡이", "ja": "杖"},
    "isub.Daggers & Knives": {"en": "Daggers & Knives", "ko": "단검 & 나이프", "ja": "短剣 & ナイフ"},
    "isub.Spears & Forks": {"en": "Spears & Forks", "ko": "창 & 포크", "ja": "槍 & フォーク"},
    "isub.Bows & Crossbows": {"en": "Bows & Crossbows", "ko": "활 & 석궁", "ja": "弓 & クロスボウ"},
    "isub.Wands": {"en": "Wands", "ko": "완드", "ja": "ワンド"},
    "isub.Helms": {"en": "Helms", "ko": "투구", "ja": "兜"},
    "isub.Rings": {"en": "Rings", "ko": "반지", "ja": "指輪"},
    "isub.Bracelets": {"en": "Bracelets", "ko": "팔찌", "ja": "ブレスレット"},
    "isub.Necklaces": {"en": "Necklaces", "ko": "목걸이", "ja": "ネックレス"},
    "isub.Earrings": {"en": "Earrings", "ko": "귀걸이", "ja": "イヤリング"},
    "isub.Hats": {"en": "Hats", "ko": "모자", "ja": "帽子"},
    "isub.Footwear": {"en": "Footwear", "ko": "신발", "ja": "履物"},
    "isub.Robes & Cloaks": {"en": "Robes & Cloaks", "ko": "로브 & 망토", "ja": "ローブ & マント"},
    "isub.Pants & Skirts": {"en": "Pants & Skirts", "ko": "바지 & 치마", "ja": "ズボン & スカート"},
    "isub.Shirts & Tops": {"en": "Shirts & Tops", "ko": "셔츠 & 상의", "ja": "シャツ & トップス"},
    "isub.Ingots": {"en": "Ingots", "ko": "주괴", "ja": "インゴット"},
    "isub.Ore": {"en": "Ore", "ko": "광석", "ja": "鉱石"},
    "isub.Wood": {"en": "Wood", "ko": "목재", "ja": "木材"},
    "isub.Leather & Hides": {"en": "Leather & Hides", "ko": "가죽 & 생가죽", "ja": "革 & 生皮"},
    "isub.Spellbooks": {"en": "Spellbooks", "ko": "마법서", "ja": "魔法書"},
    "isub.Runebooks": {"en": "Runebooks", "ko": "룬북", "ja": "ルーンブック"},
    "isub.Talismans": {"en": "Talismans", "ko": "탈리스만", "ja": "タリスマン"},
    "isub.Other": {"en": "Other", "ko": "기타", "ja": "その他"},
    # category names (for index table + page titles + intros)
    "cat.Weapons": {"en": "Weapons", "ko": "무기", "ja": "武器"},
    "cat.Armor": {"en": "Armor", "ko": "방어구", "ja": "防具"},
    "cat.Shields": {"en": "Shields", "ko": "방패", "ja": "盾"},
    "cat.Jewelry": {"en": "Jewelry", "ko": "장신구", "ja": "装身具"},
    "cat.Clothing": {"en": "Clothing", "ko": "의류", "ja": "衣類"},
    "cat.Instruments": {"en": "Instruments", "ko": "악기", "ja": "楽器"},
    "cat.Spellbooks & Talismans": {"en": "Spellbooks & Talismans", "ko": "마법서 & 탈리스만", "ja": "魔法書 & タリスマン"},
    "cat.Potions": {"en": "Potions", "ko": "물약", "ja": "ポーション"},
    "cat.Scrolls": {"en": "Scrolls", "ko": "스크롤", "ja": "スクロール"},
    "cat.Reagents": {"en": "Reagents", "ko": "시약", "ja": "試薬"},
    "cat.Food & Drink": {"en": "Food & Drink", "ko": "음식 & 음료", "ja": "食料 & 飲料"},
    "cat.Resources": {"en": "Resources", "ko": "자원", "ja": "資源"},
    "cat.Tools": {"en": "Tools", "ko": "도구", "ja": "道具"},
    "cat.Lighting": {"en": "Lighting", "ko": "조명", "ja": "照明"},
    "cat.Containers": {"en": "Containers", "ko": "용기", "ja": "コンテナ"},
    "cat.Books": {"en": "Books", "ko": "책", "ja": "本"},
    "cat.Decorations": {"en": "Decorations", "ko": "장식품", "ja": "装飾品"},
    "cat.Addons & Furniture": {"en": "Addons & Furniture", "ko": "애드온 & 가구", "ja": "アドオン & 家具"},
    "cat.Artifacts": {"en": "Artifacts", "ko": "아티팩트", "ja": "アーティファクト"},
    "cat.Functional": {"en": "Functional", "ko": "기능성 아이템", "ja": "機能アイテム"},
    "cat.Quest Items": {"en": "Quest Items", "ko": "퀘스트 아이템", "ja": "クエストアイテム"},
    "cat.Miscellaneous": {"en": "Miscellaneous", "ko": "기타", "ja": "その他"},
    # category blurbs (used in intro/desc prose)
    "blurb.Weapons": {
        "en": "melee, ranged and thrown weapons grouped by family and the combat skill they train",
        "ko": "근접·원거리·투척 무기를 계열과 훈련하는 전투 스킬별로 분류",
        "ja": "近接・遠隔・投擲武器を系統と訓練する戦闘スキル別に分類",
    },
    "blurb.Armor": {
        "en": "wearable armor grouped by material, from cloth to dragon scale",
        "ko": "천부터 드래곤 비늘까지 재질별로 분류한 착용 방어구",
        "ja": "布からドラゴンスケールまで素材別に分類した着用防具",
    },
    "blurb.Shields": {"en": "shields of every material", "ko": "모든 재질의 방패", "ja": "あらゆる素材の盾"},
    "blurb.Jewelry": {
        "en": "rings, bracelets, necklaces and earrings",
        "ko": "반지, 팔찌, 목걸이, 귀걸이",
        "ja": "指輪、ブレスレット、ネックレス、イヤリング",
    },
    "blurb.Clothing": {
        "en": "non-armor wearables — hats, robes, footwear and more",
        "ko": "방어구가 아닌 착용품 — 모자, 로브, 신발 등",
        "ja": "防具以外の着用品 — 帽子、ローブ、履物など",
    },
    "blurb.Instruments": {
        "en": "musical instruments used by the Musicianship skill",
        "ko": "음악 연주 스킬에 사용되는 악기",
        "ja": "音楽スキルで使用する楽器",
    },
    "blurb.Spellbooks & Talismans": {
        "en": "spellbooks, runebooks and talismans",
        "ko": "마법서, 룬북, 탈리스만",
        "ja": "魔法書、ルーンブック、タリスマン",
    },
    "blurb.Potions": {"en": "drinkable and thrown potions", "ko": "마시거나 투척하는 물약", "ja": "飲用および投擲ポーション"},
    "blurb.Scrolls": {"en": "spell and skill scrolls", "ko": "주문 및 스킬 스크롤", "ja": "呪文・スキルスクロール"},
    "blurb.Reagents": {"en": "spell-casting reagents", "ko": "주문 시전용 시약", "ja": "呪文詠唱用の試薬"},
    "blurb.Food & Drink": {
        "en": "food, ingredients and beverages",
        "ko": "음식, 재료, 음료",
        "ja": "食料、材料、飲料",
    },
    "blurb.Resources": {
        "en": "raw crafting materials — ingots, ore, wood, leather and hides",
        "ko": "원재료 제작 자원 — 주괴, 광석, 목재, 가죽, 생가죽",
        "ja": "未加工のクラフト素材 — インゴット、鉱石、木材、革、生皮",
    },
    "blurb.Tools": {"en": "crafting and harvesting tools", "ko": "제작 및 채집 도구", "ja": "クラフト・採取用の道具"},
    "blurb.Lighting": {
        "en": "lanterns, torches, candles and lamps",
        "ko": "랜턴, 횃불, 양초, 램프",
        "ja": "ランタン、松明、ろうそく、ランプ",
    },
    "blurb.Containers": {
        "en": "chests, bags, boxes and other containers",
        "ko": "상자, 가방, 박스 등의 용기",
        "ja": "チェスト、バッグ、ボックスなどのコンテナ",
    },
    "blurb.Books": {"en": "readable books", "ko": "읽을 수 있는 책", "ja": "読める本"},
    "blurb.Decorations": {
        "en": "statues, plants and decorative furnishings",
        "ko": "조각상, 식물, 장식용 가구",
        "ja": "彫像、植物、装飾用の調度品",
    },
    "blurb.Addons & Furniture": {
        "en": "multi-tile house deco and crafting stations",
        "ko": "멀티타일 하우스 장식 및 제작대",
        "ja": "マルチタイルのハウス装飾とクラフト台",
    },
    "blurb.Artifacts": {
        "en": "rare and event-reward items not covered by another family",
        "ko": "다른 계열에 포함되지 않는 희귀·이벤트 보상 아이템",
        "ja": "他の系統に含まれない希少・イベント報酬アイテム",
    },
    "blurb.Functional": {"en": "interactive functional items", "ko": "상호작용 가능한 기능성 아이템", "ja": "対話可能な機能アイテム"},
    "blurb.Quest Items": {"en": "items tied to quests", "ko": "퀘스트와 연계된 아이템", "ja": "クエストに紐づくアイテム"},
    "blurb.Miscellaneous": {"en": "everything else", "ko": "그 외 모든 것", "ja": "その他すべて"},

    # --- Magic / spells ---------------------------------------------------
    "magic.index_title": {"en": "Magery Spellbook", "ko": "마법학 주문서", "ja": "魔法スペルブック"},
    "magic.index_desc": {
        "en": "All 64 Magery spells by circle, with mana costs and skill requirements.",
        "ko": "서클별 마법학 주문 64종 전체와 마나 소비량 및 스킬 요구치.",
        "ja": "サークル別の魔法スペル全 64 種、マナ消費とスキル要件付き。",
    },
    "magic.index_intro": {
        "en": "The Magery spellbook holds 64 spells in 8 circles. Each circle has a fixed "
              "mana cost and a Magery skill band: below the minimum the cast always fails, at "
              "or above the maximum it never fizzles. Casting from a scroll counts as two "
              "circles lower for the skill check.",
        "ko": "마법학 주문서에는 8개 서클에 걸쳐 64개의 주문이 있습니다. 각 서클은 고정된 마나 "
              "소비량과 마법학 스킬 구간을 가집니다: 최소치 미만이면 시전이 항상 실패하고, 최대치 "
              "이상이면 절대 실패하지 않습니다. 스크롤로 시전하면 스킬 판정 시 두 서클 낮게 계산됩니다.",
        "ja": "魔法スペルブックには 8 サークルにわたり 64 の呪文があります。各サークルには固定の"
              "マナ消費と魔法スキル帯があります: 最低値未満では詠唱は必ず失敗し、最大値以上では"
              "決して失敗しません。スクロールからの詠唱はスキル判定で 2 サークル低く扱われます。",
    },
    "magic.circles": {"en": "Circles", "ko": "서클", "ja": "サークル"},
    "magic.min_magery_0": {"en": "Min Magery (0% success)", "ko": "최소 마법학 (성공률 0%)", "ja": "最低魔法 (成功率0%)"},
    "magic.magery_100": {"en": "Magery for 100%", "ko": "100% 마법학", "ja": "成功率100%の魔法"},
    "magic.skill_band_note": {
        "en": "Skill values come from `MagerySpell.GetCastSkills` (success chance ramps "
              "linearly across the 40-point band).",
        "ko": "스킬 수치는 `MagerySpell.GetCastSkills`에서 가져온 것입니다(성공 확률은 40포인트 "
              "구간에 걸쳐 선형으로 증가).",
        "ja": "スキル値は `MagerySpell.GetCastSkills` に由来します(成功率は 40 ポイントの帯で線形に"
              "上昇します)。",
    },
    "magic.circle_heading": {
        "en": "Circle {n} — {word}",
        "ko": "서클 {n} — {word}",
        "ja": "サークル {n} — {word}",
    },
    "magic.see_also": {"en": "See also", "ko": "함께 보기", "ja": "関連項目"},
    "magic.see_reagents": {"en": "See also: [Reagents]({prefix}/magic/reagents/)",
                           "ko": "함께 보기: [시약]({prefix}/magic/reagents/)",
                           "ja": "関連項目: [試薬]({prefix}/magic/reagents/)"},
    "magic.runic_note": {
        "en": "Each spell page shows its words of power in the <span class=\"uo-runic\">Britannian</span> "
              "runic alphabet — font *New Britannia Runic* (Carved) by Dame Lori, community "
              "free-use, via the [Ultima Codex Lycaeum](https://lycaeum.ultimacodex.com/new-britannia-runic-fonts-6-styles/).",
        "ko": "각 주문 페이지는 마법 주문을 <span class=\"uo-runic\">브리타니아</span> 룬 문자로 표시합니다 — "
              "폰트 *New Britannia Runic* (Carved), Dame Lori 제작, 커뮤니티 자유 사용, "
              "[Ultima Codex Lycaeum](https://lycaeum.ultimacodex.com/new-britannia-runic-fonts-6-styles/) 경유.",
        "ja": "各呪文ページは力の言葉を<span class=\"uo-runic\">ブリタニア</span>ルーン文字で表示します — "
              "フォント *New Britannia Runic* (Carved)、Dame Lori 制作、コミュニティ自由利用、"
              "[Ultima Codex Lycaeum](https://lycaeum.ultimacodex.com/new-britannia-runic-fonts-6-styles/) 経由。",
    },
    # spell circle ordinal words
    "circ.First": {"en": "First", "ko": "제1", "ja": "第1"},
    "circ.Second": {"en": "Second", "ko": "제2", "ja": "第2"},
    "circ.Third": {"en": "Third", "ko": "제3", "ja": "第3"},
    "circ.Fourth": {"en": "Fourth", "ko": "제4", "ja": "第4"},
    "circ.Fifth": {"en": "Fifth", "ko": "제5", "ja": "第5"},
    "circ.Sixth": {"en": "Sixth", "ko": "제6", "ja": "第6"},
    "circ.Seventh": {"en": "Seventh", "ko": "제7", "ja": "第7"},
    "circ.Eighth": {"en": "Eighth", "ko": "제8", "ja": "第8"},
    # spell page
    "spell.mantra_note": {
        "en": "the words of power, shown above in the Britannian runic alphabet and here in "
              "the Ultima Online game typeface. {word} Circle Magery.",
        "ko": "마법 주문으로, 위에는 브리타니아 룬 문자로, 여기에는 울티마 온라인 게임 서체로 "
              "표시됩니다. {word} 서클 마법학.",
        "ja": "力の言葉。上にブリタニアのルーン文字、ここにウルティマオンラインのゲーム書体で"
              "表示されています。{word}サークル魔法。",
    },
    "spell.casting_requirements": {"en": "Casting requirements", "ko": "시전 요구사항", "ja": "詠唱要件"},
    "spell.mana_cost": {"en": "Mana cost", "ko": "마나 소비", "ja": "マナ消費"},
    "spell.min_magery": {
        "en": "Minimum Magery",
        "ko": "최소 마법학",
        "ja": "最低魔法",
    },
    "spell.min_magery_note": {
        "en": "(0% success below this)",
        "ko": "(이 미만은 성공률 0%)",
        "ja": "(これ未満は成功率0%)",
    },
    "spell.magery_100": {"en": "Magery for 100% success", "ko": "성공률 100% 마법학", "ja": "成功率100%の魔法"},
    "spell.scroll_note": {
        # EN preserves the original hard line-wrapping.
        "en": "Casting from a scroll lowers the effective circle by two, reducing the skill\n"
              "requirement (mana cost is unchanged).",
        "ko": "스크롤로 시전하면 유효 서클이 둘 낮아져 스킬 요구치가 줄어듭니다(마나 소비는 동일).",
        "ja": "スクロールからの詠唱は有効サークルを 2 下げ、スキル要件を軽減します(マナ消費は変わりません)。",
    },
    "spell.see_overview": {
        "en": "[Spellbook overview]({prefix}/magic/)",
        "ko": "[주문서 개요]({prefix}/magic/)",
        "ja": "[スペルブック概要]({prefix}/magic/)",
    },
    "spell.see_reagents_li": {
        "en": "[Reagents]({prefix}/magic/reagents/)",
        "ko": "[시약]({prefix}/magic/reagents/)",
        "ja": "[試薬]({prefix}/magic/reagents/)",
    },
    # reagents page
    "reagents.title": {"en": "Reagents", "ko": "시약", "ja": "試薬"},
    "reagents.desc": {
        "en": "The eight Magery reagents and every spell that consumes each one.",
        "ko": "8가지 마법학 시약과 각 시약을 소비하는 모든 주문.",
        "ja": "8 種の魔法試薬と、それぞれを消費するすべての呪文。",
    },
    "reagents.intro": {
        "en": "Every Magery spell consumes one of each listed reagent per cast (unless the "
              "caster has Lower Reagent Cost or uses an arcane gem).",
        "ko": "모든 마법학 주문은 시전 시 나열된 각 시약을 하나씩 소비합니다(시전자가 시약 소비 감소를 "
              "갖거나 아케인 젬을 사용하는 경우는 제외).",
        "ja": "すべての魔法呪文は詠唱ごとに記載の各試薬を 1 つずつ消費します(詠唱者が試薬コスト軽減を"
              "持つか、アーケインジェムを使う場合を除く)。",
    },
    "reagents.used_by": {
        "en": "Used by {n} spells:",
        "ko": "{n}개 주문에서 사용:",
        "ja": "{n} の呪文で使用:",
    },
    "reagents.in_circle": {"en": "circle {n}", "ko": "서클 {n}", "ja": "サークル {n}"},
    "reagents.see_overview": {
        "en": "See also: [Spellbook overview]({prefix}/magic/)",
        "ko": "함께 보기: [주문서 개요]({prefix}/magic/)",
        "ja": "関連項目: [スペルブック概要]({prefix}/magic/)",
    },
    # reagent names (KO translates; JA keeps mostly English per glossary)
    "reag.Black Pearl": {"en": "Black Pearl", "ko": "흑진주", "ja": "Black Pearl"},
    "reag.Bloodmoss": {"en": "Bloodmoss", "ko": "피이끼", "ja": "Blood Moss"},
    "reag.Garlic": {"en": "Garlic", "ko": "마늘", "ja": "garlic"},
    "reag.Ginseng": {"en": "Ginseng", "ko": "인삼", "ja": "Ginseng"},
    "reag.Mandrake Root": {"en": "Mandrake Root", "ko": "만드레이크 뿌리", "ja": "Mandrake Root"},
    "reag.Nightshade": {"en": "Nightshade", "ko": "밤그늘풀", "ja": "nightshade"},
    "reag.Spiders' Silk": {"en": "Spiders' Silk", "ko": "거미줄", "ja": "Spiders' Silk"},
    "reag.Sulfurous Ash": {"en": "Sulfurous Ash", "ko": "유황 가루", "ja": "Sulfurous Ash"},
    # reagent blurbs
    "reagblurb.Black Pearl": {
        "en": "Associated with projection and force; common in energy and travel magic.",
        "ko": "투사와 힘에 관련됨; 에너지·이동 마법에 흔히 쓰입니다.",
        "ja": "投射と力に関連。エネルギーや移動の魔法でよく使われます。",
    },
    "reagblurb.Bloodmoss": {
        "en": "Associated with movement; common in travel, summoning and agility magic.",
        "ko": "이동에 관련됨; 이동·소환·민첩 마법에 흔히 쓰입니다.",
        "ja": "移動に関連。移動・召喚・敏捷の魔法でよく使われます。",
    },
    "reagblurb.Garlic": {
        "en": "Associated with warding; common in protective and curative magic.",
        "ko": "방호에 관련됨; 보호·치유 마법에 흔히 쓰입니다.",
        "ja": "防護に関連。保護・治癒の魔法でよく使われます。",
    },
    "reagblurb.Ginseng": {
        "en": "Associated with healing and restoration.",
        "ko": "치유와 회복에 관련됨.",
        "ja": "治癒と回復に関連。",
    },
    "reagblurb.Mandrake Root": {
        "en": "Associated with power; the workhorse reagent of high-circle magic.",
        "ko": "힘에 관련됨; 고서클 마법의 핵심 시약입니다.",
        "ja": "力に関連。高サークル魔法の主力試薬です。",
    },
    "reagblurb.Nightshade": {
        "en": "Associated with poison and curses.",
        "ko": "독과 저주에 관련됨.",
        "ja": "毒と呪いに関連。",
    },
    "reagblurb.Spiders' Silk": {
        "en": "Associated with binding and summoning.",
        "ko": "속박과 소환에 관련됨.",
        "ja": "束縛と召喚に関連。",
    },
    "reagblurb.Sulfurous Ash": {
        "en": "Associated with fire and energy.",
        "ko": "불과 에너지에 관련됨.",
        "ja": "火とエネルギーに関連。",
    },

    # --- Crafting ---------------------------------------------------------
    "craft.index_title": {"en": "Crafting", "ko": "제작", "ja": "クラフト"},
    "craft.index_desc": {
        "en": "Overview of all {n} craft systems on the shard, with recipe counts extracted from ServUO.",
        "ko": "이 샤드의 모든 {n}개 제작 시스템 개요와 ServUO에서 추출한 레시피 수.",
        "ja": "本シャードの全 {n} クラフトシステムの概要と、ServUO から抽出したレシピ数。",
    },
    "craft.index_intro": {
        "en": "The shard has **{n} craft systems** with **{total} craftable recipes**, extracted "
              "directly from the ServUO craft system definitions. Each page lists every recipe "
              "with its skill range and material costs.",
        "ko": "이 샤드에는 **{n}개 제작 시스템**과 **{total}개 제작 가능 레시피**가 있으며, ServUO "
              "제작 시스템 정의에서 직접 추출했습니다. 각 페이지는 모든 레시피를 스킬 범위와 재료 "
              "비용과 함께 나열합니다.",
        "ja": "本シャードには **{n} のクラフトシステム**と **{total} の製作可能レシピ**があり、ServUO の"
              "クラフトシステム定義から直接抽出しています。各ページはすべてのレシピをスキル範囲と材料"
              "コストとともに列挙します。",
    },
    "craft.system_desc": {
        "en": "All {n} {system} recipes ({skill} skill): skill ranges and material requirements, "
              "extracted from ServUO.",
        "ko": "{n}개의 {system} 레시피 전체({skill} 스킬): 스킬 범위와 재료 요구사항, ServUO에서 추출.",
        "ja": "{n} 件の {system} レシピすべて({skill} スキル): スキル範囲と材料要件、ServUO から抽出。",
    },
    "craft.main_recipes": {
        "en": "**Main skill:** {skill} · **Recipes:** {n}",
        "ko": "**주요 스킬:** {skill} · **레시피:** {n}",
        "ja": "**メインスキル:** {skill} · **レシピ:** {n}",
    },
    "craft.skill_range_note": {
        "en": "Skill range is the span from 0% success chance (min) to 100% success chance (max).",
        "ko": "스킬 범위는 성공 확률 0%(최소)부터 100%(최대)까지의 구간입니다.",
        "ja": "スキル範囲は成功率 0%(最低)から 100%(最高)までの幅です。",
    },
}


def L(locale, key, **fmt):
    """Localized UI string for `key` (English fallback). If kwargs are passed,
    .format(**kwargs) is applied to the chosen string."""
    entry = LABELS.get(key)
    if entry is None:
        raise KeyError("i18n_labels: unknown key %r" % key)
    s = entry.get(locale) or entry["en"]
    if fmt:
        s = s.format(**fmt)
    return s
