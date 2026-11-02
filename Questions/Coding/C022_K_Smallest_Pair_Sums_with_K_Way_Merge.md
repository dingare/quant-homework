# C022 — K Smallest Pair Sums with K-Way Merge

## Metadata

- Category: Coding
- Tags: Min-Heap, K-Way Merge, Sorted Arrays, Enumeration Invariant
- Date Added: 2026-11-01
- Original drill: November 1, 2026, Q1
- Status: Algorithm and assistant reference code supplied; independent user implementation unverified.

## Core Question

Implement runnable Python 3:

```python
def smallest_sums(a: list[int], b: list[int], k: int) -> list[int]:
    ...
```

Both arrays are sorted in nondecreasing order. Every index pair `(i, j)` contributes `a[i] + b[j]`. Return the smallest k sums in nondecreasing order, or all sums if fewer than k pairs exist. Different index pairs count separately, even when their sums coincide.

- Each array has at most 200,000 integers; negatives and duplicates are allowed.
- k is between 0 and 100,000 inclusive.
- Empty input or k = 0 returns an empty list.
- Do not modify either input.
- `[1,1,4]`, `[2,3]`, k = 4 returns `[3,3,4,4]`.
- `[-2,3]`, `[1]`, k = 5 returns `[-1,4]`.

Avoid generating the full Cartesian product; work should be driven primarily by the number of returned sums. Explain the invariant, why no index pair is duplicated or incorrectly skipped, and time and auxiliary-space complexity. Include runnable edge tests. Original budget: 20 minutes; actual time Not recorded.

## Intuition and Invariant

Fixing i gives a sorted row: `a[i] + b[0]`, `a[i] + b[1]`, and so on. Merge these sorted rows using a min-heap. Each heap entry `(sum, i, j)` is the next unreturned element of one included row. Pop the smallest head, output its sum, then insert only the next element from that same row. Every pair in an included row is generated once; equal sums from distinct pairs are retained.

Because a is sorted, only its first `min(len(a), k)` rows need to be included. The reference swaps the local array names when needed to make the row-defining array shorter; neither input is changed.

## Reference Implementation

This is the assistant code supplied at the user's request, not an independent user submission.

```python
from heapq import heapify, heappop, heappush


def smallest_sums(a: list[int], b: list[int], k: int) -> list[int]:
    if not a or not b or k <= 0:
        return []

    # Use the shorter array to define rows, keeping the heap smaller.
    if len(a) > len(b):
        a, b = b, a

    h = min(len(a), k)
    heap = [(a[i] + b[0], i, 0) for i in range(h)]
    heapify(heap)

    result = []

    while heap and len(result) < k:
        total, i, j = heappop(heap)
        result.append(total)

        # Advance only the row whose current element was removed.
        if j + 1 < len(b):
            heappush(heap, (a[i] + b[j + 1], i, j + 1))

    return result


assert smallest_sums([1, 1, 4], [2, 3], 4) == [3, 3, 4, 4]
assert smallest_sums([-2, 3], [1], 5) == [-1, 4]
assert smallest_sums([0, 0], [0, 0], 10) == [0, 0, 0, 0]
assert smallest_sums([], [1], 3) == []
assert smallest_sums([1], [2], 0) == []
```

For nonempty inputs and positive k, let h be the minimum of the two array lengths and k, and let r be the actual number of outputs. Heap initialization takes $`O(h)`$ time. Total time is $`O(h+r\log(h+1))`$ and auxiliary space is $`O(h)`$, excluding the output. Empty-input and zero-k returns take constant time.

## Connections

- [C017 — Minimum Units for Overlapping Tasks](C017_Minimum_Units_for_Overlapping_Tasks.md): both use heap entries with state, but resource availability and merging sorted streams have different invariants.
- [C010 — Kth Largest](C010_Kth_Largest_Heap_and_Quickselect.md): this question enumerates sorted pair sums rather than retaining the largest k values from one array.

## Assessment History

- [November 1 Q1](../../DailyTests/2026-11-01.md#q1--k-smallest-pair-sums): reported brute-force idea, then algorithm explanation and requested reference code; Partial / Hinted. No user code submitted, no observed I error, K/R unresolved. Verification of the assistant reference does not establish independent user implementation.
