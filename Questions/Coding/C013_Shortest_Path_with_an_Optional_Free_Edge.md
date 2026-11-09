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

## Algorithm to Implementation

Store two distances per node: coupon unused (0) and used (1). For each directed edge, try its ordinary cost without changing the flag; from layer 0, also try cost zero into layer 1. The heap stores `(distance, node, flag)`. Ignore stale entries by comparing against that exact layer's distance. The first nonstale destination entry is optimal across both layers because every expanded edge has nonnegative cost.

```python
from heapq import heappop, heappush


def cheapest_trip(n, edges, s, t):
    adjacency = [[] for _ in range(n)]
    for u, v, cost in edges:
        adjacency[u].append((v, cost))

    distance = [[float("inf"), float("inf")] for _ in range(n)]
    distance[s][0] = 0
    heap = [(0, s, 0)]
    while heap:
        current, u, used = heappop(heap)
        if current != distance[u][used]:
            continue
        if u == t:
            return current
        for v, cost in adjacency[u]:
            paid = current + cost
            if paid < distance[v][used]:
                distance[v][used] = paid
                heappush(heap, (paid, v, used))
            if used == 0 and current < distance[v][1]:
                distance[v][1] = current
                heappush(heap, (current, v, 1))
    return -1


assert cheapest_trip(3, [(0, 1, 5), (1, 2, 5), (0, 2, 20)], 0, 2) == 0
assert cheapest_trip(3, [(0, 1, 5), (1, 2, 5)], 0, 2) == 5
assert cheapest_trip(3, [(0, 1, 0)], 0, 2) == -1
assert cheapest_trip(1, [(0, 0, 7)], 0, 0) == 0
assert cheapest_trip(2, [(0, 1, 8), (0, 1, 0)], 0, 1) == 0
```

For this two-layer lazy-heap implementation, time is O(V + E log(E+1)) and auxiliary space O(V+E), including adjacency and heap entries. Inputs are unchanged. Keeping just one distance per node can discard a more expensive arrival that still has its coupon, even when that arrival is the best route to a later destination.

Reference added during the code-completion review; historical assessment results are unchanged.

## Assessment history

- [2026-10-11 Q1 — assessment](../../DailyTests/2026-10-11.md#q1--cheapest-trip-with-an-optional-free-edge)

## Related questions and knowledge

- [C019 — Shortest Grid Route with One Blocked Entry](C019_Shortest_Grid_Route_with_One_Blocked_Entry.md) — Resource-augmented shortest paths; weighted Dijkstra versus unit-cost BFS.
