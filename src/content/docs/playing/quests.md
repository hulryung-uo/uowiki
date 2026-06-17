---
title: Quests
description: How quests work — finding quest NPCs, accepting and tracking objectives, and turning them in for gold, items, and titles. Covers escort quests, Mondain's Legacy chains, bard-mastery quests, and more.
status: source-verified
sources:
  - "servuo: Scripts/Quests/BaseQuest.cs (objectives, rewards, titles), Scripts/Engines/Quests/QuestSystem.cs"
  - "servuo: Scripts/Services/MondainsLegacyQuests/ (questers, regions, rewards)"
last_verified: 2026-06-17
generated: false
---

Beyond grinding monsters, Britannia is full of **quests** — tasks handed out by NPCs that send
you to kill, fetch, escort, or deliver, and pay out **gold, items, and titles** when you
finish. They range from one-off favors to multi-part story chains.

## The basic loop

1. **Find a quest NPC** (a "quester"). Many stand in towns and camps; some are tied to a
   specific region or dungeon. Double-click or hail them.
2. **Accept the quest.** A quest gump lays out the **objectives** and the **rewards** on offer
   (`BaseQuest` shows objectives and a reward list).
3. **Complete the objectives** (`BaseObjective`) — e.g. *slay N of a creature*, *collect/deliver
   an item*, *escort an NPC*, or *reach a place*. Progress is tracked in your **quest log**.
4. **Turn it in** to the giver for the reward — gold, an item, and sometimes a wearable
   **title**.

## Kinds of quests you'll meet

- **Escort quests** — guide a wandering NPC safely to a destination. These also build the
  **[Compassion virtue](/playing/virtues/)**, so they're worth repeating.
- **Mondain's Legacy quests** — the large ML quest framework (apprentice/region questers,
  collection and crafting chains) with its own rewards (`MondainsLegacyQuests`).
- **Bard-mastery quests** — the quest line that teaches **[bard skill masteries](/playing/skill-masteries/)**
  (the knights Berran, Felean, and Hareus).
- **Crafting & gathering quests** — make or gather specific goods for a reward.
- **Story / dungeon chains** — longer arcs (e.g. the Eodon / Time of Legends content) that
  unlock access, recipes, or mastery primers.

## Tips

- **Read the reward before committing** — most quest gumps show the payout up front; some
  rewards (titles, recipes, access) matter more than the gold.
- **Escorts feed Compassion** — if you want the Compassion virtue, escort quests are the
  intended path.
- Keep an eye on **quest items** in your pack — some are flagged as quest-only and can't be
  sold or dropped normally until the quest resolves.

## See also

- [Virtues](/playing/virtues/) — escorts build Compassion; quests can advance others
- [Skill Masteries](/playing/skill-masteries/) — bard masteries come from a quest line
- [Communication & social](/playing/communication-and-social/) — hailing and talking to NPCs
- [The world & its towns](/world/) — where quest-givers gather
