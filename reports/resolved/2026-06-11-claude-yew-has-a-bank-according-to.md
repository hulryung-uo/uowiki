# Yew has a bank according to the interactive map
- page: src/content/docs/world/yew.md
- observed: uomap (js/data.js line 285) shows a Banker vendor at (652, 820), inside Yew bounds (92-756, 656-1261). If correct, the wiki page should list a bank in Yew.
- expected-per-wiki: The wiki page states Yew has no bank and advises planning banking around trips to Britain or Minoc.
- evidence: uomap js/data.js:285 { name: 'Banker', x: 652, y: 820 }; wiki sources cite anima world_knowledge.yaml which lists no bank for Yew
