# C011 — Incremental Connectivity and Connected Pairs

## Metadata

- Category: Coding
- Tags: Disjoint Sets, Root Invariants, Amortized Complexity
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10, 2026-10-14
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q1

Source and assessment: [2026-10-10 Q1](../../DailyTests/2026-10-10.md#q1--incremental-connectivity). The reference material below does not change that attempt’s recorded result.

### Question

Start with up to 200,000 isolated machines and process up to 200,000 undirected edges. After each edge, return the total number of unordered connected pairs. Duplicate edges and self-loops are allowed. Implement runnable Python 3 `connected_pairs(n, edges)`; justify correctness, complexity and tests. For `n=4`, `[(0,1),(1,2),(2,3),(0,3)]` gives `[1,3,6,6]`.

### Key solution

Maintain one global total. Joining distinct components of sizes $`a,b`$ creates exactly the cross-component pairs:

```math
\binom{a+b}{2}-\binom a2-\binom b2=ab.
```

```python
def connected_pairs(n, edges):
    parent = list(range(n))
    size = [1] * n
    total = 0
    result = []

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        a, b = find(u), find(v)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            total += size[a] * size[b]
            parent[b] = a
            size[a] += size[b]
        result.append(total)
    return result
```

For $`m`$ edges: time $`O(n+m\alpha(n))`$, auxiliary space $`O(n)`$, output $`O(m)`$. Union by size keeps tree height logarithmic; path halving makes lookup amortized nearly constant.

## Interview drill — 2026-10-14 Q1

Source and assessment: [2026-10-14 Q1](../../DailyTests/2026-10-14.md#q1--connected-pairs). The reference material below does not change that attempt’s recorded result.

### Question

Implement runnable Python 3 `connected_pairs(n, edges)`: starting with isolated nodes, return the number of unordered connected pairs after every edge. Up to 200,000 nodes and edges; duplicate/self edges allowed. Explain correctness and complexity, and test disconnected groups. For `n=4`, `[(0,1),(2,3),(1,2),(0,3)]` returns `[1,2,6,6]`.

### Key solution

Use the [DSU reference](../../DailyTests/2026-10-10.md#q1--incremental-connectivity): path halving, union by size, and a global count. Link roots using `root[rv] = ru`.

```math
\Delta C=\binom{a+b}{2}-\binom a2-\binom b2=ab,\qquad
T(n,M)=O(n+M\alpha(n)).
```

Auxiliary space is $`O(n)`$, or $`O(n+M)`$ including output. A single find is at worst $`O(\log n)`$; amortized cost is $`O(\alpha(n))`$.

## Assessment history

- [2026-10-10 Q1 — assessment](../../DailyTests/2026-10-10.md#q1--incremental-connectivity)
- [2026-10-14 Q1 — assessment](../../DailyTests/2026-10-14.md#q1--connected-pairs)

## Related questions and knowledge

- [C008 — Dependency Ordering and DAG Scheduling](C008_Dependency_Ordering_and_DAG_Scheduling.md) — Undirected component connectivity versus directed dependency ordering.
