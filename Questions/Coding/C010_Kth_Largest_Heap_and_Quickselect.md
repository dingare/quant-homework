# C010 — Kth Largest: Heap and Quickselect

## Metadata

- Category: Coding
- Tags: Heaps, Selection, Partitioning
- Date Added: 2026-10-22
- Original drill dates: 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-09 Q4

Source and assessment: [2026-10-09 Q4](../../DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement). The reference material below does not change that attempt’s recorded result.

### Question

Return the kth-largest array element without fully sorting. First give an `O(n log k)` method; then identify an expected-`O(n)` follow-up.

### Recorded answer details

Maintain a min-heap containing the largest k values seen so far. Push while `len(heap) < k`, then compare with its minimum. Time is `O(n log k)` and space `O(k)`. Quickselect partitions and continues only on the side containing index `n-k`; expected `O(n)`, worst-case `O(n^2)`.

## Algorithm to Implementation

### Size-k min-heap

The heap contains the largest k values in the processed prefix once at least k values have been read. Its root is the smallest retained value, hence the kth largest. A new value below that root cannot enter the top k; a larger value replaces the root. Equal values count separately.

```python
from heapq import heappush, heapreplace


def kth_largest_heap(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError("Require 1 <= k <= len(nums)")
    heap = []
    for value in nums:
        if len(heap) < k:
            heappush(heap, value)
        elif value > heap[0]:
            heapreplace(heap, value)
    return heap[0]


assert kth_largest_heap([3, 2, 1, 5, 6, 4], 2) == 5
assert kth_largest_heap([5, 5, 3], 2) == 5
assert kth_largest_heap([-4, -1, -2], 3) == -4
assert kth_largest_heap([7], 1) == 7
```

Time O(n log(k+1)), auxiliary space O(k), with no input mutation.

### Randomized three-way quickselect

Select ascending index `len(nums) - k`. Partition the active interval into values below, equal to, and above a random pivot. The equal band is already at its final range of sorted ranks. Return if the target falls there; otherwise retain only the side containing the target. Three-way partitioning handles repeated values without repeatedly selecting one equal element at a time.

```python
from random import randrange


def kth_largest_quickselect(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError("Require 1 <= k <= len(nums)")
    values = list(nums)  # Preserve the caller's input.
    target = len(values) - k
    low, high = 0, len(values) - 1
    while low <= high:
        pivot = values[randrange(low, high + 1)]
        lt, i, gt = low, low, high
        while i <= gt:
            if values[i] < pivot:
                values[lt], values[i] = values[i], values[lt]
                lt += 1
                i += 1
            elif values[i] > pivot:
                values[i], values[gt] = values[gt], values[i]
                gt -= 1  # Recheck the value just swapped into i.
            else:
                i += 1
        if target < lt:
            high = lt - 1
        elif target > gt:
            low = gt + 1
        else:
            return values[target]
    raise RuntimeError("Unreachable for valid k")


for values, k, expected in [([3, 2, 1, 5, 6, 4], 2, 5),
                            ([5, 5, 5], 2, 5), ([-4, -1, -2], 3, -4),
                            ([7], 1, 7)]:
    assert kth_largest_quickselect(values, k) == expected
```

Expected time O(n), worst-case O(n²). This version uses O(n) auxiliary space for its input-preserving copy; the iterative partition itself uses O(1). Omitting that copy gives an in-place version that modifies the input.

Reference added during the code-completion review; historical assessment results are unchanged.

## Assessment history

- [2026-10-09 Q4 — assessment](../../DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement)

## Related questions and knowledge

- [C003 — Online Median with Two Heaps](C003_Online_Median_with_Two_Heaps.md) — Heap size and ordering invariants.
- [C017 — Minimum Units for Overlapping Tasks](C017_Minimum_Units_for_Overlapping_Tasks.md) — Min-heap invariant and update order.
