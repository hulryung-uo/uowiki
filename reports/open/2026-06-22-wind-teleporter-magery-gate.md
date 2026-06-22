# Wind entrance teleporter + Magery gate unconfirmed in ServUO source

- page: src/content/docs/world/wind.md
- claim disputed: "hidden entrance near (1361, 895) in north-central Britannia" and
  "Magery-gated teleporter, ~70.0 skill required" to enter Wind.
- observed (source read):
  - `Data/Regions.xml` defines `TownRegion` "Wind" on both Felucca and Trammel facets,
    with rects in the Lost Lands coordinate block (x ~5132-5366, y ~3-204) and a region
    travel point `<go x="5223" y="190" z="5" />`. So the *city region* is verified, and it
    is a guarded town region (TownRegion : GuardedRegion in Scripts/Regions/TownRegion.cs),
    NOT a dungeon region.
  - `Scripts/Items/Functional/PublicMoongate.cs` has no Wind entry (no public gate) — verified.
  - A `SkillTeleporter : Teleporter` class exists (Scripts/Items/Internal/Teleporter.cs,
    line ~431) that supports a configurable SkillName + required value, so a Magery-gated
    teleporter is technically supported by the engine.
  - However, I could NOT locate the actual Wind entrance teleporter instance, its
    coordinates, the configured skill, or the required value. Teleporters are spawned from
    decoration / `Data/teleporters.csv`; the entries near the Wind/Lost Lands coordinate
    block in teleporters.csv are plain (non-skill) teleporters, and no Wind-specific
    SkillTeleporter placement was found in this pass.
- expected-per-wiki: surface entrance at (1361, 895); Magery 70.0 to pass the teleporter.
- needs: locate the Wind entrance teleporter placement (decoration data or a Gen* script)
  and confirm (a) its world coordinates, (b) whether it is a SkillTeleporter, (c) the
  SkillName (Magery?) and required value. Alternatively confirm in-game via an anima agent.
- evidence: Regions.xml lines 521-544 (Felucca) / 1595-1618 (Trammel);
  Scripts/Regions/TownRegion.cs:10; Scripts/Items/Functional/PublicMoongate.cs:314-330;
  Scripts/Items/Internal/Teleporter.cs:431 (SkillTeleporter).
