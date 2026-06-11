# Page lists main dig area near (2560,540); a better-documented training spot exists at (2567,493)
- page: src/content/docs/world/minoc.md
- observed: Map-data scan + live mining evals: tile (2567,493,z~22) is walkable with ~19 mineable mountain tiles within reach 2, on the east face minutes from Minoc forge/bank. Dozens of 10-min AI mining sessions trained Mining there without relocating beyond bank-hopping. Calibration: anima foundry/kernel/gm.py FIXED_START_PROFILES; evals eval-evob826c*, eval-evobc201c2*
- expected-per-wiki: Mention (2567,493) east-face spot in the Minoc mining section alongside the (2560,540) area
- evidence: anima map scan (MapReader + MINEABLE_LAND_TILES) and foundry evals 2026-06-10/11
