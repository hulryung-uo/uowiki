# Pre-AOS wrestling stun punch does not function on an EJ shard

- page: src/content/docs/templates/stun-mage.md
- observed: This shard runs expansion **EJ** (`Config/Expansion.cfg` → `CurrentExpansion=EJ`;
  loaded via `Scripts/Misc/CurrentExpansion.cs` into `Core.Expansion`). `Core.AOS` is
  `Expansion >= Expansion.AOS` (`Server/Main.cs:147`), and EJ is far past AOS in the enum, so
  **`Core.AOS == true`**. In `Scripts/Items/Equipment/Weapons/Fists.cs` the pre-AOS stun/disarm
  code is gated OFF when AOS is active:
  - `EventSink_StunRequest` and `EventSink_DisarmRequest` both begin with `if (Core.AOS) return;`
    (lines 324, 352) — the StunReady/DisarmReady toggles can never be set by a player.
  - `OnSwing` only calls `CheckPreAOSMoves` when `!Core.AOS` (line 265), so the
    `Anatomy >= 80.0 && Wrestling >= 80.0` stun (lines 162-201, 4s `Freeze` at line 183) is
    never reached.
  On EJ the Fists weapon instead exposes AOS **WeaponAbility** special moves —
  `PrimaryAbility = Disarm`, `SecondaryAbility = ParalyzingBlow` (Fists.cs lines 16-29) — which
  are gated by weapon skill + mana via `WeaponAbility.CheckSkills`/`CheckMana`
  (`Scripts/Abilities/WeaponAbility.cs`), NOT by the Anatomy-80/Wrestling-80 threshold or a
  StunReady toggle.
- expected-per-wiki: The page states "This shard implements the pre-AOS stun punch" and builds
  its entire thesis on "readying a stun requires Anatomy >= 80.0 AND Wrestling >= 80.0" with a
  StunReady punch that Freezes the target. That mechanic is real ServUO code but is
  pre-AOS-only and unreachable on this EJ shard.
- evidence: claude 2026-06-22; servuo Server/Main.cs:147, Config/Expansion.cfg,
  Scripts/Misc/CurrentExpansion.cs:13, Scripts/Items/Equipment/Weapons/Fists.cs:162-201,263-376,
  Scripts/Abilities/WeaponAbility.cs:212-262
- resolution applied: Page corrected in-place (status left `unverified`) to explain that the
  classic 80/80 stun punch is the pre-AOS mechanic and is NOT active on this EJ shard, replacing
  the false "this shard implements" claim with the actual EJ behavior (AOS ParalyzingBlow weapon
  special on Fists). Filed for librarian audit of any pages that cross-link the stun mechanic.

---
## RESOLVED 2026-06-23 (claude, librarian triage)
Confirmed against `Scripts/Items/Equipment/Weapons/Fists.cs` + `Server/Main.cs` + `Config/Expansion.cfg`:
on EJ (Core.AOS true) the pre-AOS 80/80 stun punch is gated off; Fists exposes AOS Disarm/ParalyzingBlow
specials instead. stun-mage.md was already corrected in-place (danger banner + accurate sources, status
kept `unverified` as a documented era variant). No further page change needed; closing.
