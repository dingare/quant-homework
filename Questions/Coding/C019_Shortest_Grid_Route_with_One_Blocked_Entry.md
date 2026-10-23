# C019 — Shortest Grid Route with One Blocked Entry

## Metadata

- Category: Coding
- Tags: BFS, Resource State, FIFO, Discovery Invariant
- Date Added: 2026-10-22
- Original drill dates: 2026-10-20
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-20 Q1

Source and assessment: [2026-10-20 Q1](../../DailyTests/2026-10-20.md#q1--shortest-route-with-one-blocked-entry). The reference material below does not change that attempt’s recorded result.

### Question

Implement runnable Python 3:

```python
def shortest_route(grid: list[list[int]]) -> int:
    ...
```

A nonempty rectangular grid contains open cells (0) and blocked cells (1). Start at the top-left cell and reach the bottom-right cell. Both endpoints are open. Each move goes up, down, left or right and costs one step. **At most one move during the entire route may enter a blocked cell.** Every other move must enter an open cell.

Return the minimum number of steps, or -1 if reaching the destination is impossible. There are at most 200,000 cells. Do not modify the input. Examples: `[[0,1],[1,0]]` returns 2; `[[0,1,1,0]]` returns -1; `[[0]]` returns 0.

Derive an $`O(RC)`$-time approach. Explain what information the algorithm retains, correctness and auxiliary space. Include runnable tests covering zero blocked entries, a necessary blocked entry, an unreachable destination and a single cell.

### Key solution

Use states `(row, column, used)`, where used is zero or one. Every move costs one, including a blocked-cell entry; unlike a free-edge coupon, the allowance does not remove the step's cost. FIFO BFS processes states by distance. A cell reached with the allowance unused is a different state from the same cell reached after using it. Mark each state discovered on enqueue.

Reference supplied on request, not a corrected user submission:

```python
from collections import deque


def shortest_route(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dist = [[[-1, -1] for _ in range(n)] for _ in range(m)]
    dist[0][0][0] = 0
    nodes = deque([(0, 0, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while nodes:
        i, j, used = nodes.popleft()
        cost = dist[i][j][used]
        if i == m - 1 and j == n - 1:
            return cost
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if not (0 <= ni < m and 0 <= nj < n):
                continue
            new_used = used + grid[ni][nj]
            if new_used > 1:
                continue
            if dist[ni][nj][new_used] != -1:
                continue
            dist[ni][nj][new_used] = cost + 1
            nodes.append((ni, nj, new_used))
    return -1


assert shortest_route([[0]]) == 0
assert shortest_route([[0, 0], [0, 0]]) == 2
assert shortest_route([[0, 1], [1, 0]]) == 2
assert shortest_route([[0, 1, 1, 0]]) == -1
```

There are at most two states per cell and four outgoing moves per state. BFS first dequeues a destination state at the minimum valid distance. Time and auxiliary space are both $`O(RC)`$; input is unchanged. A heap-based shortest-path algorithm can also solve the problem but does not meet the requested linear-time bound.

During recording, this reference passed its four original assertions, all 171 endpoint-open grids with dimensions 1–3 by 1–3, 1,000 seeded random grids against an independent remove-one-obstacle / ordinary-BFS oracle, input-preservation checks, and a 200,000-cell open chain. These checks validate the assistant reference only, not an independent user implementation.

## Assessment history

- [2026-10-20 Q1 — assessment](../../DailyTests/2026-10-20.md#q1--shortest-route-with-one-blocked-entry)

## Related questions and knowledge

- [C013 — Shortest Path with an Optional Free Edge](C013_Shortest_Path_with_an_Optional_Free_Edge.md) — Resource-augmented shortest paths; weighted Dijkstra versus unit-cost BFS.
