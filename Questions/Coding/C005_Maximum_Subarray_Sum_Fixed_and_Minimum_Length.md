# C005 — Maximum Subarray Sum with Fixed and Minimum Length

## Metadata

- Category: Coding
- Interview Relevance: High
- Tags: Sliding Window, Prefix Sums, Running Minimum, Invariants
- Date Added: 2026-10-06
- Status: Final
- Source: 2026-10-06 interview drill; worked solution added after the timed attempt at the user's request.

## Core Question

Given nums and fixed k, return the starting index of the length-k subarray with maximum sum. Follow-up: if the length is at least k, how would you solve it and what complexity would you target?

Reference conventions: values may be negative; use zero-based indices and keep the earliest starting index on ties. The minimum-length follow-up targets linear time.

## Solution

### Fixed Length

Maintain the sum of exactly k consecutive values. Each step adds the entering value and subtracts the leaving value. Compare only complete windows. Initialize with the first window, not zero, so all-negative inputs work.

```python
def max_sum_fixed_k(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("Require 1 <= k <= len(nums)")
    current = best = sum(nums[i] for i in range(k))
    best_start = 0
    for right in range(k, len(nums)):
        current += nums[right] - nums[right - k]
        start = right - k + 1
        if current > best:
            best, best_start = current, start
    return best_start
```

Time $`O(n)`$; auxiliary space $`O(1)`$.

### Length at Least k

Let $`P[0]=0`$ and $`P[j]=\sum_{i=0}^{j-1}nums[i]`$. The sum of the half-open interval $`[i,j)`$ is $`P[j]-P[i]`$. For each endpoint j, eligible starts satisfy $`0\le i\le j-k`$.

```math
\max_{0\le i\le j-k}(P[j]-P[i])
=P[j]-\min_{0\le i\le j-k}P[i].
```

**Invariant:** before evaluating j, the running minimum is the smallest prefix sum among indices 0 through j-k, with the earliest minimizing index. Add the newly eligible prefix before evaluating the candidate.

```python
def max_sum_at_least_k(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("Require 1 <= k <= len(nums)")
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    min_prefix, min_index = 0, 0
    best_sum = float("-inf")
    best_start, best_end = 0, k
    for end in range(k, len(nums) + 1):
        eligible = end - k
        if prefix[eligible] < min_prefix:
            min_prefix, min_index = prefix[eligible], eligible
        candidate = prefix[end] - min_prefix
        if candidate > best_sum or (
            candidate == best_sum and min_index < best_start
        ):
            best_sum = candidate
            best_start, best_end = min_index, end
    return best_start, best_end, best_sum
```

Returns the start, exclusive end, and sum. Time $`O(n)`$ and space $`O(n)`$. A streaming pair of running sums can reduce auxiliary space to $`O(1)`$.

Negative values destroy the monotonic behavior needed for a greedy two-pointer rule. Prefix sums convert interval optimization into choosing the smallest eligible left prefix.

## Common Mistakes

- Initializing the best sum to zero fails on all-negative arrays.
- Forgetting the newly eligible prefix creates an off-by-one error.
- Confusing maximum window sum with maximum element in a window.
- Using two-pointer greedy with arbitrary signed inputs.

## Connections

- [C001 — Prefix sums and range sums](C001_Count_of_Range_Sums_with_Prefix_Sums_and_Fenwick_Tree.md)
- [C002 — Prefix sums and monotonic deque](C002_Shortest_Subarray_at_Least_K_with_a_Monotonic_Deque.md)
- [Daily test: Q1](../../DailyTests/2026-10-06.md#q1--maximum-sum-subarray)

## What to Remember

Fixed length: update one window sum. Minimum length: subtract the smallest eligible prefix.

### Constant-space minimum-length implementation

For each exclusive endpoint, `total` is its prefix sum. `eligible_prefix` tracks the newly eligible starting prefix by adding exactly one earlier input value per step. Keep its smallest value and earliest index. This implements the same recurrence without storing the full prefix array; return conventions match `max_sum_at_least_k`.

```python
def max_sum_at_least_k_constant_space(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("Require 1 <= k <= len(nums)")
    total = eligible_prefix = min_prefix = 0
    min_index = 0
    best_sum = float("-inf")
    best_start, best_end = 0, k
    for end, value in enumerate(nums, 1):
        total += value
        if end < k:
            continue
        eligible = end - k
        if eligible > 0:
            eligible_prefix += nums[eligible - 1]
        if eligible_prefix < min_prefix:
            min_prefix, min_index = eligible_prefix, eligible
        candidate = total - min_prefix
        if candidate > best_sum or (candidate == best_sum and min_index < best_start):
            best_start, best_end, best_sum = min_index, end, candidate
    return best_start, best_end, best_sum


assert max_sum_fixed_k([-5, -2, -3], 2) == 1
assert max_sum_fixed_k([1, 1, 1], 2) == 0
assert max_sum_at_least_k([-5, -2, -3], 2) == (1, 3, -5)
assert max_sum_at_least_k_constant_space([-5, -2, -3], 2) == (1, 3, -5)
assert max_sum_at_least_k_constant_space([1, 1, 1], 2) == (0, 3, 3)
```

Time O(n), auxiliary space O(1); input is unchanged.

## Assessment history

- [2026-10-06 Q1 — assessment](../../DailyTests/2026-10-06.md#q1--maximum-sum-subarray)
