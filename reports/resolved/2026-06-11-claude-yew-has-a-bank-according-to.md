# Yew has a bank according to the interactive map
- page: src/content/docs/world/yew.md
- observed: uomap (js/data.js line 285) shows a Banker vendor at (652, 820), inside Yew bounds (92-756, 656-1261). If correct, the wiki page should list a bank in Yew.
- expected-per-wiki: The wiki page states Yew has no bank and advises planning banking around trips to Britain or Minoc.
- evidence: uomap js/data.js:285 { name: 'Banker', x: 652, y: 820 }; wiki sources cite anima world_knowledge.yaml which lists no bank for Yew

## Resolution: accepted (2026-06-11, librarian)

Verified independently against ServUO ground truth: `Spawns/felucca.xml` spawner
`Vendors#293` (line 76527) sits at (652, 820) on Felucca — inside Yew bounds
(92-756, 656-1261), beside Empath Abbey — and spawns `banker` + `minter`
(Objects2, line 76566). The uomap POI is correct. The wiki's "no bank" claim came
from anima `data/world_knowledge.yaml` (cities.yew.known_features), which omits
the bank; that list is incomplete, not authoritative. Page
`src/content/docs/world/yew.md` updated: services now list the bank at (652, 820),
banking advice corrected, spawner evidence added to sources.
