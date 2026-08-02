# C002 — Shortest Subarray at Least $K$ with a Monotonic Deque

## Metadata

- Category: Coding
- Secondary: Algorithms, Prefix Sums, Data Structures
- Difficulty: ★★★★★
- Tags: Prefix Sum, Monotonic Deque, Shortest Subarray, Dominance, Negative Values
- Review Priority: High
- Date Added: 2026-07-26
- Status: Final

## Core Question

Given

$$
a=[2,-1,2,-4,3,1,-1,2]
$$

and $K=5$, find the shortest contiguous subarray whose sum is at least $K$. Then design an $O(n)$ algorithm that works even when values can be negative.

## Example Answer

The prefix sums are

$$
S=[0,2,1,3,-1,2,3,2,4].
$$

At prefix index $8$,

$$
S_8-S_4=4-(-1)=5.
$$

This corresponds to zero-based array indices

$$
[4,7],
$$

whose values are

$$
[3,1,-1,2].
$$

No window of length one, two, or three reaches $5$. Therefore

$$
\boxed{\text{shortest length}=4,\qquad\text{indices}=[4,7]}.
$$

## Prefix-Sum Reformulation

Define

$$
S_0=0,
\qquad
S_j=\sum_{t=0}^{j-1}a_t.
$$

The window $[i,j-1]$ has sum at least $K$ exactly when

$$
S_j-S_i\ge K.
$$

For each endpoint $j$, we want a useful earlier index $i$ with a small prefix value but as large an index as possible, because that gives a shorter window.

## Monotonic-Deque Invariant

Maintain a deque $D$ of prefix indices such that

$$
S_{D_0}\lt S_{D_1}\lt \cdots\lt S_{D_m}.
$$

For each $j$, perform two operations.

### 1. Pop Valid Starts from the Front

While

$$
S_j-S_{D_0}\ge K,
$$

record the candidate length $j-D_0$ and remove $D_0$.

This start can be discarded: for every future endpoint, it would produce an even longer window.

### 2. Pop Dominated Starts from the Back

While

$$
S_{D_m}\ge S_j,
$$

remove $D_m$.

The new index $j$ dominates $D_m$ because

$$
j\gt D_m
\qquad\text{and}\qquad
S_j\le S_{D_m}.
$$

For every future endpoint $r$,

$$
S_r-S_j\ge S_r-S_{D_m},
$$

and starting at $j$ also creates a shorter window.

Finally, append $j$.

## Python Solution

```python
from collections import deque
from typing import Optional


def shortest_subarray_at_least_k(
    values: list[int],
    target: int,
) -> tuple[int, Optional[tuple[int, int]]]:
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)

    candidates: deque[int] = deque()
    best_length = len(values) + 1
    best_window: Optional[tuple[int, int]] = None

    for right, current in enumerate(prefix):
        while (
            candidates
            and current - prefix[candidates[0]] >= target
        ):
            left = candidates.popleft()
            if right - left < best_length:
                best_length = right - left
                best_window = (left, right - 1)

        while (
            candidates
            and prefix[candidates[-1]] >= current
        ):
            candidates.pop()

        candidates.append(right)

    if best_window is None:
        return -1, None

    return best_length, best_window


assert shortest_subarray_at_least_k(
    [2, -1, 2, -4, 3, 1, -1, 2],
    5,
) == (4, (4, 7))
```

Each prefix index is appended once and removed at most once from each end. Therefore

$$
\boxed{\text{time }O(n),\qquad\text{space }O(n)}.
$$

## Why a Sliding Window Fails

When all values are nonnegative, extending a window cannot decrease its sum, so two pointers work. Negative values destroy this monotonicity:

- extending a window may reduce its sum;
- shrinking a window may increase its sum.

The deque restores a different monotonic structure—an ordered frontier of nondominated prefix sums.

## Key Knowledge Points

- Prefix sums convert a subarray condition into a difference condition.
- The deque stores candidates, not arbitrary previous prefixes.
- Front pops certify valid windows.
- Back pops remove dominated candidates.
- Amortized $O(1)$ deque operations yield total $O(n)$.
- “Small prefix value + recent index” is the desirable combination.

## Common Mistakes

- Applying a nonnegative sliding-window method when negative values are present.
- Reversing the order of the two while-loops without understanding the invariant.
- Returning prefix indices instead of array indices.
- Using $\gt $ where $\ge K$ is required.
- Claiming $O(1)$ total space while storing all prefix sums.

## Interview Follow-Ups

1. Return all shortest valid windows.
2. Explain why the algorithm is amortized $O(n)$.
3. Handle a streaming input.
4. Compare this problem with count-of-range-sums.
5. Find the longest subarray whose sum is at most $K$.

## Finance Connection

This can identify the shortest horizon over which cumulative P&L, alpha, order flow, or DV01-adjusted return crosses a threshold, even when increments are signed.

## What to Remember

$$
\boxed{
\text{prefix sums}
+\text{monotonic deque}
+\text{dominance}
=O(n)
}.
$$

