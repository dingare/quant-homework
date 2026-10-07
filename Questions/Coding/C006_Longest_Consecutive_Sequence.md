# C006 — Longest Consecutive Sequence

## Metadata

- Category: Coding
- Interview Relevance: High
- Tags: Hash Set, Hash Map, Boundary Invariant
- Date Added: 2026-10-06
- Status: Final
- Source: 2026-10-06 interview drill; worked solution added after the timed attempt at the user's request.

## Core Question

Given an unsorted integer array, return the longest consecutive sequence length in expected $O(n)$ time. Example: [100, 4, 200, 1, 3, 2] returns 4.

## Solution

### Hash Set: Expand Only from Sequence Starts

A value begins a run only if its predecessor is absent. Scan forward only from such starts.

```python
def longest_consecutive(nums):
    values = set(nums)
    best = 0
    for start in values:
        if start - 1 not in values:
            end = start
            while end in values:
                end += 1
            best = max(best, end - start)
    return best
```

Each distinct value is scanned as part of exactly one run. Under expected constant-time hashing, total time is $O(n)$ and auxiliary space is $O(n)$. Empty input returns zero; duplicates are removed.

### Boundary-Length Map: Complete the Interview Idea

For each new x, let left and right be the lengths of the intervals ending at x-1 and starting at x+1. Merge them with x:

$$
length=left+right+1.
$$

**Invariant:** each interval's two endpoints store its full length. Interior entries may be stale. If x is unseen, any present neighbor x-1 must be a right endpoint and any present neighbor x+1 must be a left endpoint; otherwise x would already belong to that interval.

```python
def longest_consecutive_boundary(nums):
    lengths = {}
    best = 0
    for x in nums:
        if x in lengths:
            continue
        left = lengths.get(x - 1, 0)
        right = lengths.get(x + 1, 0)
        merged = left + right + 1
        lengths[x] = merged
        lengths[x - left] = merged
        lengths[x + right] = merged
        best = max(best, merged)
    return best
```

Expected $O(n)$ time and $O(n)$ space. Store x to track membership, update both outer endpoints, and skip duplicates.

## Common Mistakes

- Expanding from every element repeats work and can become quadratic.
- Forgetting to skip duplicates corrupts the boundary merge.
- Updating only x leaves endpoint lengths wrong.
- Assuming all interior map lengths are current.

## Connections

- [C005 — Maximum subarray sum and implementation invariants](C005_Maximum_Subarray_Sum_Fixed_and_Minimum_Length.md)
- [Daily test: Q4](../../DailyTests/2026-10-06.md#q4--longest-consecutive-sequence)

## What to Remember

Either expand only from starts, or maintain correct lengths at both endpoints of each interval.
