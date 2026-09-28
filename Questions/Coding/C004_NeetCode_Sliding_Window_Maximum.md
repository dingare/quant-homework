# C004 — NeetCode Sliding Window Maximum

## Metadata

- Category: Coding
- Difficulty: Hard
- Tags: Sliding Window, Segment Tree, Block DP, Monotonic Deque, Heap
- Date Added: 2026-09-27
- Status: Final

## Core Question

Return the maximum of every consecutive window of size `k`. Assume `1 <= k <= len(nums)`.

Example: `[1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3` → `[3, 3, 5, 5, 6, 7]`.

## Solution

Space below excludes the O(n - k + 1) output. Each snippet runs independently.

| Method | Data structure / core logic | Total time | Extra space |
| --- | --- | --- | --- |
| Segment tree | Flat array; merge maxima, query each window | O(n log n) | O(n) |
| Block DP | Two arrays; combine block suffix and prefix | O(n) | O(n) |
| Monotonic deque | Deque of candidate indices; discard dominated/expired entries | O(n) amortized | O(k) |
| heapq | Min-heap of negative values and indices; lazily remove expired roots | O(n log n) | O(n) |

### 1. Segment tree — build once, query windows

Put the input in leaves `tree[n:2*n]`, then build parents backward: `tree[i] = max(tree[2*i], tree[2*i+1])`. This iterative flat-array build costs O(n); each window query costs O(log n), giving O(n log n) overall and O(n) space. Queries use a half-open interval `[left, right)`.

```python
def max_sliding_window_tree(nums, k):
    n = len(nums)
    tree = [float("-inf")] * n + nums
    for i in range(n - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])

    def query(left, right):
        left += n
        right += n
        best = float("-inf")
        while left < right:
            if left % 2:
                best = max(best, tree[left])
                left += 1
            if right % 2:
                right -= 1
                best = max(best, tree[right])
            left //= 2
            right //= 2
        return best

    return [query(i, i + k) for i in range(n - k + 1)]
```

### 2. Block DP — join a suffix and a prefix

Split the array into blocks of size `k`. `leftMax[i]` is the maximum from the block start to `i`; `rightMax[i]` is the maximum from `i` to the block end. A window `[l, r]` has maximum `max(rightMax[l], leftMax[r])`: it spans two block pieces, or one whole block. Two passes plus O(1) per window give O(n) time and O(n) space.

```python
def max_sliding_window_dp(nums, k):
    n = len(nums)
    leftMax, rightMax = [0] * n, [0] * n
    for i in range(n):
        leftMax[i] = (nums[i] if i % k == 0
                      else max(leftMax[i - 1], nums[i]))
    for i in range(n - 1, -1, -1):
        rightMax[i] = (nums[i] if i == n - 1 or (i + 1) % k == 0
                       else max(rightMax[i + 1], nums[i]))
    return [max(rightMax[l], leftMax[l + k - 1])
            for l in range(n - k + 1)]
```

### 3. Monotonic deque — keep possible future maxima

Store **indices** in increasing order, with their values decreasing (non-increasing). Pop the **back** when a newer, larger value dominates it: the newer value also expires later. Pop the **front** when its index leaves the window. The front is the maximum. Each index enters once and leaves at most once: amortized O(n) time, O(k) space.

For example, deque values `[5]` become `[5, 3]` when `3` arrives: keep `3` because it may become maximum after the older `5` expires. A new `6` removes both.

```python
from collections import deque


def max_sliding_window_deque(nums, k):
    q, output = deque(), []
    for r, value in enumerate(nums):
        while q and q[0] <= r - k:
            q.popleft()
        while q and nums[q[-1]] < value:
            q.pop()
        q.append(r)
        if r >= k - 1:
            output.append(nums[q[0]])
    return output
```

### 4. heapq — largest value first, expire lazily

Store `(-value, index)` in Python's min-heap, so the most negative root represents the maximum. For a window ending at `i`, indices `<= i - k` are stale; remove stale roots before reading the answer. Buried stale entries remain until they reach the root, so the heap can grow to O(n): O(n log n) total time and O(n) space, not O(k) space.

Your original code is preserved below; only the required imports are added.

```python
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
```

## Connections

- [C002 — Shortest Subarray at Least K](C002_Shortest_Subarray_at_Least_K_with_a_Monotonic_Deque.md): same dominance-removal idea; different deque invariant.
- [C003 — Online Median with Two Heaps](C003_Online_Median_with_Two_Heaps.md): heap invariants and lazy deletion.

## What to Remember

Tree: query ranges. DP: precompute block edges. Deque: remove useless candidates. Heap: remove stale winners.
