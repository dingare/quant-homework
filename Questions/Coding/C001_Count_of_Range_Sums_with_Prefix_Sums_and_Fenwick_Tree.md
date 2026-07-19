# C001 — Count of Range Sums with Prefix Sums and a Fenwick Tree

## Metadata

- Category: Coding
- Secondary: Algorithms, Data Structures, Trading P&L
- Difficulty: ★★★★☆
- Tags: Prefix Sums, Fenwick Tree, Coordinate Compression, Merge Sort, Range Counting
- Review Priority: High
- Date Added: 2026-07-19
- Status: Finalized
- Personal Note: Convert interval sums into ordered pairs of prefix sums, while preserving time order.

## Core Question

A trading strategy produces daily P&L increments

```math
a=[2,-1,3,-2,1].
```

For every contiguous interval $[i,j]$, define

```math
S_{i,j}=\sum_{t=i}^j a_t.
```

Count the intervals satisfying

```math
1\le S_{i,j}\le3,
```

then design an $O(n\log n)$ algorithm that also works when the array contains negative values.

## Hint

Define prefix sums

```math
P_0=0,
\qquad
P_k=\sum_{t=0}^{k-1}a_t.
```

Because $S_{i,j}=P_{j+1}-P_i$, for each new $P_r$ count earlier $P_\ell$ satisfying

```math
P_r-U\le P_\ell\le P_r-L.
```

## Solution

The prefix sums are

```math
P=[0,2,1,4,2,3].
```

The ten valid intervals, written with zero-based inclusive endpoints, are

```math
(0,0),(0,1),(0,3),(0,4),(1,2),
(1,4),(2,2),(2,3),(2,4),(4,4).
```

Therefore the answer is

```math
\boxed{10}.
```

For the general problem, scan prefix sums from left to right. Before inserting the current prefix sum $P_r$, query how many previously inserted values fall in

```math
[P_r-U,\;P_r-L].
```

A coordinate-compressed Fenwick tree supports both the range-count query and insertion in $O(\log n)$ time, so total time is $O(n\log n)$ and storage is $O(n)$.

```python
from bisect import bisect_left, bisect_right
from typing import List


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        if index < 0:
            return 0

        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


def count_range_sums(nums: List[int], lower: int, upper: int) -> int:
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    coordinates = sorted(
        set(
            prefix
            + [value - lower for value in prefix]
            + [value - upper for value in prefix]
        )
    )

    tree = FenwickTree(len(coordinates))
    count = 0

    for current in prefix:
        left_value = current - upper
        right_value = current - lower

        right_index = bisect_right(coordinates, right_value) - 1
        left_index = bisect_left(coordinates, left_value) - 1

        count += (
            tree.prefix_sum(right_index)
            - tree.prefix_sum(left_index)
        )

        current_index = bisect_left(coordinates, current)
        tree.add(current_index, 1)

    return count


assert count_range_sums([2, -1, 3, -2, 1], 1, 3) == 10
```

## Alternative: Modified Merge Sort

Divide the prefix sums by index. After recursively sorting the left and right halves, use two forward-moving pointers in the right half for each left prefix $P_i$:

```math
j_{\mathrm{low}}=\min\{j:P_j-P_i\ge L\},
```

```math
j_{\mathrm{high}}=\min\{j:P_j-P_i>U\}.
```

Then $j_{\mathrm{high}}-j_{\mathrm{low}}$ is the number of valid cross-half pairs. Each merge level costs $O(n)$, giving

```math
T(n)=2T(n/2)+O(n)=O(n\log n).
```

## Key Knowledge Points

- Prefix sums convert contiguous-interval sums into differences of two values.
- The ordering condition $\ell<r$ must be preserved.
- A Fenwick tree needs coordinate compression because prefix sums may be negative or large.
- Modified merge sort is an equally valid $O(n\log n)$ solution.
- A standard sliding window fails because negative increments destroy monotonicity.

## Intuition

The brute-force algorithm enumerates all $O(n^2)$ intervals. The prefix-sum transformation asks a different question: for each current prefix, how many earlier prefixes lie inside a numerical range? An ordered counting structure answers that without revisiting every earlier index.

## Common Mistakes

- Sorting all prefix sums once and losing the temporal condition $\ell<r$.
- Inserting the current prefix before querying, which may count an empty interval.
- Mishandling inclusive endpoints with `bisect_left` and `bisect_right`.
- Using a two-pointer sliding window when negative values are allowed.
- Forgetting the initial prefix sum $P_0=0$.

## Interview Follow-ups

1. Count intervals satisfying $|S_{i,j}|\le K$.
2. Return the shortest valid interval rather than the count.
3. Explain precisely why a sliding window fails with negative values.
4. Adapt the Fenwick approach to an online stream.
5. Count intervals whose average lies in $[\alpha,\beta]$.

## Market / Rates Application

The pattern appears when examining all possible holding periods in a P&L or signal series—for example, windows whose cumulative slippage, carry, inventory P&L, or order flow lies within a specified band.

## Connections

- Prefix sums and cumulative P&L
- Order-statistics trees and Fenwick trees
- Coordinate compression
- Divide-and-conquer counting
- Range-sum and inversion-count problems

## What to Remember

> Count range sums by querying earlier prefix sums in $[P_r-U,P_r-L]$ before inserting $P_r$.
