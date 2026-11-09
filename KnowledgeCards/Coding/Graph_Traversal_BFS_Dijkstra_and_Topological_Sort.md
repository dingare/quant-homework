# Graph Algorithms — BFS, Dijkstra, DAG, and Topological Sort

- Added: 2026-11-08
- Category: Coding / Knowledge Card
- Source: November 8 interview-drill Q1 and the subsequent graph-algorithm discussion.
- Status: Guided study reference. Q1 Partial / Hinted; both submitted edge-scanning implementations were tested and found flawed. The assistant supplied the BFS algorithm and verified reference; no independent corrected user submission has been received. K/R unresolved; implementation errors observed. Actual time Not recorded. Naming/typing clarifications are not conceptual errors. Filing this card does not establish mastery or add a canonical question.

## 1. Choose the algorithm by the question

| Question | Method | Next item to process |
| --- | --- | --- |
| Reachability, connected components, or two-group constraints in an undirected graph | BFS or DFS | BFS: oldest discovered node; DFS: most recently discovered unfinished node |
| Minimum number of edges when every edge has the same positive cost | BFS | FIFO queue |
| Minimum additive path cost with nonnegative edge weights | Dijkstra | Smallest tentative distance, using a min-heap |
| An order satisfying all directed dependencies | Topological sort, e.g. Kahn | A node with no remaining incoming prerequisites |
| Shortest/longest paths or path counts in a DAG | Topological order + DP | A node whose predecessors have all been processed |

DAG = Directed Acyclic Graph（有向无环图）. It is a graph property. Topological sort is an algorithmic task. A heap is a data structure, not a shortest-path algorithm by itself. Dijkstra generalizes the shortest-path use of BFS to nonnegative weighted edges; it does not replace BFS for every graph question.

## 2. Representation: edge list to adjacency list

`conflicts = [(0, 1), (2, 3), (0, 2)]` is an edge list. For an undirected graph, its adjacency list is:

```python
adj = [[1, 2], [0], [3, 0], [2]]
```

An adjacency list lets us find a node's neighbors without rescanning every edge. Build it once in linear time in nodes plus edges. For directed edges, append only the outgoing neighbor; for undirected edges, append both directions.

## 3. BFS: consistent two-group assignment

Each conflict edge requires opposite labels. Start one uncolored node with label 0, then propagate opposite labels throughout its entire connected component before choosing another root.

```python
from collections import deque


def assign_groups(n, conflicts):
    adj = [[] for _ in range(n)]
    for u, v in conflicts:
        adj[u].append(v)
        adj[v].append(u)

    res = [-1] * n
    for start in range(n):
        if res[start] != -1:
            continue
        res[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if res[v] == -1:
                    res[v] = 1 - res[u]
                    queue.append(v)
                elif res[v] == res[u]:
                    return None
    return res


assert assign_groups(4, [(0, 1), (2, 3), (0, 2)]) == [0, 1, 1, 0]
assert assign_groups(3, [(0, 1), (1, 2), (2, 0)]) is None
assert assign_groups(2, [(0, 1), (0, 1)]) == [0, 1]
assert assign_groups(1, [(0, 0)]) is None
assert assign_groups(3, []) == [0, 0, 0]
assert assign_groups(0, []) == []
```

**Invariant.** Every discovered node has one fixed label consistent with its discovery path from the root. A newly discovered neighbor receives the opposite label and is marked before enqueueing, so it enters the queue once. For an already labeled neighbor, check the edge instead of changing either label.

A same-color edge joins a discovery-tree path of even length to one additional edge, producing an odd cycle. Alternating two labels around an odd cycle is impossible. Conversely, if every edge passes the check, the returned assignment satisfies every constraint. An outer loop covers disconnected components and isolated nodes. A self-loop fails the same-color check; duplicate edges cause no problem.

If an explicit impossibility certificate is requested, retain discovery parents and depths, join the two tree paths to their common ancestor, then close the cycle with the conflicting edge. The implementation above returns only `None`.

### Why scanning the edge list once failed

- First submission: seeing an endpoint again was treated as failure, even when the new constraint was already satisfied. Changing a label could also invalidate an earlier edge.
- Second submission: unassigned and assigned states were distinguished correctly, but separately initialized groups could choose incompatible orientations. With edges `(0,1), (2,3), (0,2)`, the intermediate labels `[0,1,0,1]` can be repaired by flipping nodes 2 and 3 together. This is a valid graph, not proof of impossibility.
- Traversing an entire component from one root avoids independently choosing those orientations. Sorting endpoints by numeric ID does not establish a valid traversal order.

For n nodes and m input edges, time and auxiliary space including adjacency are both $`O(n+m)`$. Repeatedly scanning the full edge list for each processed node can take $`O(nm)`$ time.

## 4. Dijkstra + min-heap: nonnegative shortest paths

Applications include minimum travel time, network latency, weighted grids, and expanded-state path problems. Path cost must be the sum of edge costs; every edge weight must be nonnegative. Zero weights are allowed. The graph need not be acyclic.

```python
import heapq


def dijkstra(n, edges, source):
    # Directed graph; valid node IDs and nonnegative weights assumed.
    adj = [[] for _ in range(n)]
    for u, v, weight in edges:
        adj[u].append((v, weight))

    dist = [float("inf")] * n
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, weight in adj[u]:
            new_dist = d + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    return dist


edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
assert dijkstra(4, edges, 0) == [0, 3, 1, 4]
assert dijkstra(3, [(0, 1, 0)], 0) == [0, 0, float("inf")]
assert dijkstra(2, [(0, 1, 8), (0, 1, 0)], 0) == [0, 0]
```

**Invariant.** Tentative distances are costs of discovered paths. When the smallest nonstale heap entry is popped, its distance is final: any supposedly shorter undiscovered path would have a frontier node with a smaller tentative distance. Nonnegative remaining edges supply that guarantee.

Do not mark a node final on its first insertion. In the example, node 1 first enters at distance 4, then at distance 3. Leave the old `(4, 1)` entry in the heap and skip it when popped. Use strict improvement when pushing, so equal-distance routes and zero-weight cycles do not keep adding entries. Unreachable nodes retain infinity. To stop at one target, stop when its nonstale entry is popped, not when it is first discovered.

For this lazy-heap implementation, including adjacency, time is $`O(n+m\log(m+1))`$ and auxiliary space is $`O(n+m)`$. For a simple graph this gives the familiar $`O((n+m)\log(n+1))`$ bound. Parallel edges can make the lazy heap larger than n, so a blanket claim of heap space linear only in nodes is inaccurate.

For a nonnegative weighted route with one free-edge opportunity, use the state `(node, opportunity_used)` and keep separate distances for each state. See C013 below. Negative weights invalidate the standard settling guarantee; general directed graphs may require Bellman–Ford, whereas DAGs permit the topological method below.

## 5. Topological sort: satisfy prerequisites

For a directed edge `u -> v`, u must occur before v. Common uses: task scheduling, prerequisite courses, and calculation dependencies. A complete topological order exists exactly when the directed graph is acyclic; the order need not be unique.

Kahn's algorithm keeps the remaining incoming-edge count for each node. Enqueue every zero-indegree node. After processing a node, remove its outgoing edges; enqueue a neighbor exactly when its indegree becomes zero.

```python
from collections import deque


def topological_sort(n, edges):
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    queue = deque(u for u in range(n) if indegree[u] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return order if len(order) == n else None


assert topological_sort(4, [(0, 2), (1, 2), (2, 3)]) == [0, 1, 2, 3]
assert topological_sort(2, [(0, 1), (1, 0)]) is None
assert topological_sort(1, [(0, 0)]) is None
assert topological_sort(2, [(0, 1), (0, 1)]) == [0, 1]
assert topological_sort(0, []) == []
```

**Invariant.** A node is ready only after all its incoming prerequisites have been removed. A finite nonempty DAG always has a zero-indegree node, so if processing stalls with nodes remaining, a directed cycle exists. Some remaining nodes may merely depend on a cycle rather than lie on it. This card uses `None` for a cycle, distinguishing failure from a valid empty graph's `[]`; the existing C008 question uses its original empty-list failure convention.

Time and auxiliary space including adjacency are $`O(n+m)`$. The queue resembles BFS's queue, but eligibility comes from zero remaining indegree, not from being newly discovered by a neighbor. Repeated edges work because both the initial count and the later decrements include each occurrence.

## 6. DAG + dynamic programming

In topological order, every predecessor has been processed before its successor. For shortest paths, initialize the source distance to zero and the rest to infinity, then relax outgoing edges from each reachable node:

```math
d[v]\leftarrow\min\{d[v],\ d[u]+w(u,v)\}.
```

This works with negative edge weights too: the dependency order is valid regardless of weights. It takes $`O(n+m)`$ time including topological sorting. No heap is necessary. For longest paths, use negative infinity for unreachable states and maximize instead.

For task durations with unlimited parallel workers, a task starts after its latest-finishing prerequisite. Completion time therefore follows a longest-path recurrence, not the sum of all task durations. See C008 for the existing implementation.

## Connections and verification

- [C008 — Dependency Ordering and DAG Scheduling](../../Questions/Coding/C008_Dependency_Ordering_and_DAG_Scheduling.md): Kahn's algorithm and critical-path completion time.
- [C013 — Shortest Path with an Optional Free Edge](../../Questions/Coding/C013_Shortest_Path_with_an_Optional_Free_Edge.md): Dijkstra over augmented states.
- [C019 — Shortest Grid Route with One Blocked Entry](../../Questions/Coding/C019_Shortest_Grid_Route_with_One_Blocked_Entry.md): unit-cost BFS with resource states.
- [C011 — Incremental Connectivity](../../Questions/Coding/C011_Incremental_Connectivity_and_Connected_Pairs.md): component maintenance; plain connectivity alone does not maintain opposite-color constraints.

The assistant's BFS reference in the conversation passed 8 edge cases, 2,000 random-graph comparisons against exhaustive assignments, input-preservation checks, and a 200,000-node path. These validate the reference, not an independent user implementation. At filing, all Python blocks in this card executed successfully, including all three algorithms' assertions and additional regression cases. Group validity was checked independently of global label orientation. All seven changed Markdown files passed the repository's math/Markdown checker. No user elapsed time is inferred.
