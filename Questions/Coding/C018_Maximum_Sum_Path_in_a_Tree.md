# C018 — Maximum-Sum Path in a Tree

## Metadata

- Category: Coding
- Tags: Trees, Dynamic Programming, Iterative Traversal
- Date Added: 2026-10-22
- Original drill dates: 2026-10-18
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-18 Q1

Source and assessment: [2026-10-18 Q1](../../DailyTests/2026-10-18.md#q1--maximum-sum-path-in-a-tree). The reference material below does not change that attempt’s recorded result.

### Question

Implement runnable Python 3:

```python
def best_path_sum(
    values: list[int],
    edges: list[tuple[int, int]]
) -> int:
    ...
```

An undirected tree has nodes numbered 0 through n minus one, with integer node values that may be negative. Return the largest sum along any nonempty simple path. A path follows edges without revisiting a node, may start/end anywhere, and may consist of one node. There are 1–200,000 nodes; edges form a valid tree. Do not modify inputs. Handle a tree that is one long chain.

Example: values = [-10, 9, 20, 15, 7], edges = [(0,1), (0,2), (2,3), (2,4)] gives 42. Derive linear time, explain state invariants/correctness and auxiliary space, and include runnable single-node, all-negative and chain tests.

### Key solution

The adjacency list records undirected connections; choosing root 0 only establishes parent/child relationships. Record a parent-before-child traversal, then process it in reverse. No recursion is needed.

- down[u]: maximum sum of a downward path starting at u, including u; it can attach to the parent.
- best[u]: maximum nonempty path sum anywhere in u's subtree; it need not include u.

Let g1 and g2 be the two largest positive child down contributions, padded with zeros. Then:

```math
down[u]=values[u]+g_1,
```

```math
best[u]=\max\left(values[u]+g_1+g_2,\ \max_{v\text{ child of }u}best[v]\right).
```

For a leaf, both states equal its node value. Zero means omit a child branch, never choose an empty final path. A complete path through u can use two child directions; a path that also attaches to the parent can use only one. Never attach a child's best value as if it were its down value. For node 5 with children 4 and 6, best is 15 but down is 11.

Reference supplied during the discussion, not an exact user submission:

```python
def best_path_sum(
    values: list[int],
    edges: list[tuple[int, int]]
) -> int:
    n = len(values)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * n
    order = [0]
    i = 0
    while i < len(order):
        u = order[i]
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            order.append(v)
        i += 1

    down = [0] * n
    best = [0] * n
    for u in reversed(order):
        g1 = g2 = 0
        subtree_best = values[u]
        for v in adj[u]:
            if v == parent[u]:
                continue
            subtree_best = max(subtree_best, best[v])
            gain = down[v]
            if gain > g1:
                g2 = g1
                g1 = gain
            elif gain > g2:
                g2 = gain
        down[u] = values[u] + g1
        best[u] = max(subtree_best, values[u] + g1 + g2)
    return best[0]


assert best_path_sum(
    [-10, 9, 20, 15, 7],
    [(0, 1), (0, 2), (2, 3), (2, 4)]
) == 42
assert best_path_sum([-3], []) == -3
assert best_path_sum([-8, -2, -5], [(0, 1), (1, 2)]) == -2
assert best_path_sum([2, -1, 3, 4], [(0, 1), (1, 2), (2, 3)]) == 8
```

Every simple path has a highest node relative to the chosen root. At that node it uses at most two child branches, so its best possible sum is considered. The root's subtree is the entire tree; return best[0] because 0 is the chosen root's ID, not its value or a special maximum node. Time and auxiliary space are both linear in n.

During recording, the supplied reference passed its four assertions, 1,000 seeded random comparisons against an independent all-starts path oracle, input-preservation checks, and a 200,000-node chain. These checks validate the reference only, not the user's unsubmitted version.

## Assessment history

- [2026-10-18 Q1 — assessment](../../DailyTests/2026-10-18.md#q1--maximum-sum-path-in-a-tree)

## Related questions and knowledge

- [C008 — Dependency Ordering and DAG Scheduling](C008_Dependency_Ordering_and_DAG_Scheduling.md) — Dependency order and propagation of dynamic-programming states.
- [C015 — Arithmetic Expressions and Nested State](C015_Arithmetic_Expressions_and_Nested_State.md) — Nested state and iterative traversal without deep Python recursion.
