# C013 — Shortest Path with an Optional Free Edge

## Metadata

- Category: Coding
- Tags: Dijkstra, Augmented State, Nonnegative Weights
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q1

Source and assessment: [2026-10-11 Q1](../../DailyTests/2026-10-11.md#q1--cheapest-trip-with-an-optional-free-edge). The reference material below does not change that attempt’s recorded result.

### Question

Implement runnable Python 3 `cheapest_trip(n, edges, s, t)` on a directed graph with nonnegative integer costs, using at most one free edge traversal. Return -1 if unreachable. Up to 100,000 nodes and 200,000 edges; parallel edges, self-loops and zero costs allowed. Explain correctness/complexity and test unreachable routes. For edges `[(0,1,5),(1,2,5),(0,2,20)]`, the cheapest trip from 0 to 2 costs 0.

### Key solution

Run Dijkstra on `(node, free_edge_used)`. A paid transition preserves the flag; a free transition changes unused to used. Keep distances and stale-heap checks for the exact state, not just the node. Nonnegative costs justify settling the cheapest state first.

For at most $`k`$ free traversals, use $`L=k+1`$ state layers. A lazy heap gives:

```math
T=O\!\left(LV+LE\log(LE+1)\right),\qquad S=O(LV+LE).
```

## Assessment history

- [2026-10-11 Q1 — assessment](../../DailyTests/2026-10-11.md#q1--cheapest-trip-with-an-optional-free-edge)

## Related questions and knowledge

- [C019 — Shortest Grid Route with One Blocked Entry](C019_Shortest_Grid_Route_with_One_Blocked_Entry.md) — Resource-augmented shortest paths; weighted Dijkstra versus unit-cost BFS.
