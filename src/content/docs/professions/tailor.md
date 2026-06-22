---
title: Tailor
description: Turn cloth and leather into clothing and leather armor. Skills, the build, the sewing loop, what you make, and how a tailor earns.
status: source-verified
sources:
  - "servuo: Scripts/Services/Craft/DefTailoring.cs (MainSkill = Tailoring; cloth & leather/hide resources)"
  - "servuo: Scripts/Services/Craft/Core/CraftItem.cs (success & exceptional chance from main skill only; Arms Lore not referenced)"
  - "servuo: Scripts/Items/Equipment/Armor/BaseArmor.cs DistributeExceptionalBonuses (exceptional leather/studded armor: +ArmsLore/20 random resist)"
  - "servuo: Scripts/Items/Equipment/Clothing/BaseClothing.cs (exceptional clothing: +ArmsLore/20 resist, capped +4)"
  - "servuo: Scripts/Skills/ArmsLore.cs (active skill is item identification only)"
  - "servuo: Scripts/Mobiles/NPCs/Tailor.cs (BODType.Tailor; SupportsBulkOrders needs Tailoring skill > 0)"
  - "servuo: Scripts/Services/BulkOrders/ (banked points; Rewards/ runic sewing kits, power scrolls, cloth)"
  - "servuo: Config/Expansion.cfg (EJ)"
last_verified: 2026-06-22
generated: false
---

## What this profession is

The tailor works in cloth and leather, sewing everything from shirts and dyed robes to full
suits of leather and studded armor. It is one of the cheapest crafts to start — a sewing kit
and a bolt of cloth are all you need — and it pairs naturally with almost any other build,
since both fighters and crafters always need wearables. Tailoring also supplies the bandages
every healer and tamer burns through.

## Core skills

- [Tailoring](/skills/tailoring/) — the headline skill: cut and sew cloth and leather into clothing and armor.
- [Arms Lore](/skills/arms-lore/) — does **not** raise the chance to produce **exceptional** items (the craft engine never checks it), but on this shard it adds **+Arms Lore/20 random resist points** to leather and studded armor that comes out exceptional (+5 at GM), and a smaller resist bonus to clothing (capped at +4). It matters most for leather armor, where those extra resists mean real defense.

## The build

There is no dedicated tailor template yet — tailoring is most often picked up as a second
craft alongside another profession. For a pure crafter, slot Tailoring into a multi-skill
spread and see [7x GM Templates](/templates/seven-gm/) for fitting it under the 700-point
cap (a common pairing is tailor + alchemist/cook, or tailor on a smith for a full
crafting character).

## How to craft

Read [Crafting](/playing/crafting/) for the craft menu and exceptional mechanics. The
[Tailoring crafting](/crafting/tailoring/) page lists the full recipe catalog and the
material each item needs.

The loop: stock raw material, open the sewing kit, and pick items from the craft menu.
**Cloth** comes from the farming chain — cotton or flax spun into thread on a spinning wheel,
woven into cloth on a loom — or bought in bolts; **leather** is cut from hides looted off
animals and tanned. Higher Tailoring is what raises your exceptional chance; Arms Lore then
adds extra resists to each exceptional armor piece. Cut cloth
with scissors to make bandages, and cut hides into leather before sewing armor.

## What you make / tools

- [Tools](/items/tools/) — a **sewing kit** to craft and **scissors** to cut cloth into bandages and hides into leather.
- [Resources](/items/resources/) — **leather and cloth**; the cotton/flax → thread → cloth chain and the hide → leather chain feed every recipe.
- [Clothing catalog](/items/catalog/clothing/) — shirts, robes, hats, and dyeable wearables.
- [Armor catalog](/items/catalog/armor/) — **leather and studded armor** suits, the tailor's high-value output.

## Making a living

Tailors earn by selling **leather armor suits** to fighters who want light, no-skill-penalty
protection, and by turning out **bandages** in bulk (cut cloth) for healers, tamers, and
warriors who go through hundreds. Sewn **bags and pouches** and dyed clothing round out the
stock. Tailor bulk order deeds, like the smith's, reward materials and rare tools for filled
orders. Move goods through [Vendors & Banking](/playing/vendors-and-banking/).

## See also

- [7x GM Templates](/templates/seven-gm/) — fitting tailoring into a crafting build
- [Blacksmith](/professions/blacksmith/) — the metal-armor counterpart; many crafters do both
- [Warrior](/professions/warrior/) · [Tamer](/professions/tamer/) — buyers of leather armor and bandages
- [Tailoring](/skills/tailoring/) · [Tailoring crafting](/crafting/tailoring/) · [Resources](/items/resources/)
