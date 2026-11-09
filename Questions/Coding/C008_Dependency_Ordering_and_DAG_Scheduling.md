# C008 — Dependency Ordering and DAG Scheduling

## Metadata

- Category: Coding
- Tags: Graphs, Topological Sort, DAG DP, Cycle Detection
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08, 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-08 Q1

Source and assessment: [2026-10-08 Q1](../../DailyTests/2026-10-08.md#q1--dependency-ordering). The reference material below does not change that attempt’s recorded result.

### Question

There are n jobs numbered 0 through n-1. Each dependency [a,b] means a must finish before b starts. Write Python 3 returning any valid execution order, or an empty list if impossible. Explain cycle detection and time / space complexity.

### Recorded solution

Use edges a → b. Kahn's algorithm stores adjacency lists and indegrees, queues all zero-indegree jobs, then removes their outgoing edges. Each removed job satisfies all prerequisites. If fewer than n jobs are processed, the remaining graph contains a cycle. Time and space: $`O(V+E)`$. This is feedback, not an independently completed solution.

### Related Notes

- [New graph / topological-sort gap](../../Backlog.md#october-8-interview-knowledge-gaps): historical gap record from before this canonical note was filed.

## Interview drill — 2026-10-09 Q1

Source and assessment: [2026-10-09 Q1](../../DailyTests/2026-10-09.md#q1--dag-scheduling-with-durations). The reference material below does not change that attempt’s recorded result.

### Question

Given task durations and dependencies `(u, v)`, with unlimited workers and independent tasks allowed to run simultaneously, find the minimum completion time or return -1 for a cycle. Example: `durations = [3,2,5,4]`, `dependencies = [(0,2),(1,2),(2,3)]`.

### Recorded solution

Initialize `finish = durations[:]`. Kahn BFS guarantees all parents have been processed when a node's indegree reaches zero. Count processed nodes to detect a cycle. The answer is `max(finish)`; for the example it is 12. Time and space are `O(V+E)`.

## Algorithm to Implementation

### Dependency order

`indegree[v]` counts prerequisites not yet removed. Initially enqueue every zero-indegree node, including isolated jobs. Removing u decreases each outgoing neighbor's count; enqueue a neighbor exactly when its count becomes zero. If the queue empties before all nodes are removed, a cycle blocks the remaining jobs.

```python
from collections import deque


def execution_order(n: int, dependencies: list[tuple[int, int]]) -> list[int]:
    adjacency = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in dependencies:
        adjacency[u].append(v)
        indegree[v] += 1

    ready = deque(u for u in range(n) if indegree[u] == 0)
    order = []
    while ready:
        u = ready.popleft()
        order.append(u)
        for v in adjacency[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)
    return order if len(order) == n else []


assert execution_order(3, [(0, 1), (1, 2)]) == [0, 1, 2]
assert execution_order(2, [(0, 1), (1, 0)]) == []
assert execution_order(3, []) == [0, 1, 2]
assert execution_order(0, []) == []
```

### Durations with unlimited workers

Task v starts only after its latest-finishing prerequisite. Before processing an edge u → v, `finish[u]` is final. Update `finish[v]` with `finish[u] + durations[v]`; taking the maximum across all parents accounts for parallel work. When v enters the queue, all its parent contributions have arrived. An empty task set takes zero time; durations are assumed nonnegative.

```python
def minimum_completion_time(durations, dependencies):
    n = len(durations)
    adjacency = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in dependencies:
        adjacency[u].append(v)
        indegree[v] += 1

    finish = list(durations)
    ready = deque(u for u in range(n) if indegree[u] == 0)
    processed = 0
    while ready:
        u = ready.popleft()
        processed += 1
        for v in adjacency[u]:
            finish[v] = max(finish[v], finish[u] + durations[v])
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)
    return max(finish, default=0) if processed == n else -1


assert minimum_completion_time([3, 2, 5, 4], [(0, 2), (1, 2), (2, 3)]) == 12
assert minimum_completion_time([3, 7], []) == 7
assert minimum_completion_time([1, 1], [(0, 1), (1, 0)]) == -1
assert minimum_completion_time([], []) == 0
```

Both functions use O(V+E) time and auxiliary space, including the graph copy. Dependencies use valid node IDs; neither function modifies its inputs. Run both blocks in order; the second shares the deque import.

Reference added during the code-completion review; historical assessment results are unchanged.

## Assessment history

- [2026-10-08 Q1 — assessment](../../DailyTests/2026-10-08.md#q1--dependency-ordering)
- [2026-10-09 Q1 — assessment](../../DailyTests/2026-10-09.md#q1--dag-scheduling-with-durations)

## Related questions and knowledge

- [C018 — Maximum-Sum Path in a Tree](C018_Maximum_Sum_Path_in_a_Tree.md) — Dependency order and propagation of dynamic-programming states.
- [C011 — Incremental Connectivity and Connected Pairs](C011_Incremental_Connectivity_and_Connected_Pairs.md) — Undirected component connectivity versus directed dependency ordering.
