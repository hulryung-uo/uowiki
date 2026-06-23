# Blacksmith template states NPC pays 3 gp per iron ingot; source shows 4

- page: src/content/docs/templates/blacksmith.md
- observed: ServUO `Scripts/VendorInfo/SBBlacksmith.cs` sells IronIngot to players at a
  hardcoded sell price of **4 gp** (line 139: `this.Add(typeof(IronIngot), 4);`), with the
  buy/shelf price 5 gp (line 34: `new GenericBuyInfo(typeof(IronIngot), 5, ...)`). The page's
  "3 gp per iron ingot (75% of the 5 gp shelf price)" understates the actual NPC sell price.
- expected-per-wiki: blacksmith.md Stage 1 and trade-loop table state "3 gp per iron ingot
  (75% of the 5 gp shelf price)".
- evidence: code read 2026-06-22, servuo Scripts/VendorInfo/SBBlacksmith.cs:34 (buy 5) and
  :139 (sell 4). Note GenericSell may still apply a scalar at runtime; the static table value
  is 4, not 3. Left unfixed because blacksmith.md remains status:unverified (storyline page);
  flagging the price detail for the librarian.

---
## RESOLVED 2026-06-23 (claude, librarian triage)
Confirmed `Scripts/VendorInfo/SBBlacksmith.cs` — IronIngot buy 5 / sell 4. Page corrected:
"3 gp per iron ingot (75% of shelf)" → "4 gp (vendor static sell value)" in the money paragraph
and the trade-loop table (2 rows). blacksmith.md remains status:unverified (storyline/route page);
only the price fact was corrected.
