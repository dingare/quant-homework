# C020 — Minimum Deletions for a Strictly Increasing Subsequence

## Metadata

- Category: Coding
- Tags: Dynamic Programming, Dominance, Greedy State Compression, Binary Search, LIS
- Date Added: 2026-10-24
- Original drill: October 23, 2026, Q1
- Status: Worked reference; assisted reasoning and verified user implementation are assessed separately.

## Core Question

Implement runnable Python 3:

```python
def min_deletions(nums: list[int]) -> int:
    ...
```

Return the minimum number of elements that must be deleted so that the remaining elements, in their original order, form a strictly increasing sequence. The remaining elements need not be contiguous.

- Up to 200,000 integers; duplicates and negative values are allowed.
- Do not modify the input. Empty input returns 0.
- Examples: `[3,1,2,2,4]` returns 2; `[5,5,5]` returns 2; `[]` returns 0.

Derive an $`O(n\log n)`$ approach. Explain the invariant that makes updates safe, justify optimality, state auxiliary space, and include runnable tests for duplicates, decreasing input and empty input.

## Solution and Intuition

### 1. Reframe deletion as retention

If the longest strictly increasing subsequence has length L, the answer is $`n-L`$. Every valid retained sequence is an increasing subsequence; keeping a longest one attains this deletion count. Only the count is required, so reconstructing deleted indices is unnecessary.

### 2. Start with the direct DP

Let dp[i] be the longest increasing subsequence ending at position i:

```math
dp[i]=1+\max_{j\lt i,\ nums[j]\lt nums[i]}dp[j],
```

where an empty maximum contributes zero. This gives a correct $`O(n^2)`$ starting point.

### 3. Eliminate dominated endings

For two processed-prefix subsequences of the same length, ending at 4 versus 7, any future value that can extend the latter can extend the former. The smaller ending therefore dominates the larger ending for future length calculations.

Maintain `tails[k-1]`: the smallest achievable ending value among all length-k increasing subsequences in the processed prefix. Only one ending per length is needed. These endings are strictly increasing: a subsequence attaining the minimum ending for length k+1 has a length-k prefix ending strictly below it; the minimum ending for length k is no larger than that prefix ending.

### 4. Update by binary search

For a new value x, find the first position i with `tails[i] >= x`.

- All earlier endings are smaller than x. A subsequence of length i can be extended by x, producing length i+1.
- Replacing `tails[i]` with x improves or preserves the smallest ending for length i+1.
- Shorter lengths already have smaller endings, so x does not improve them.
- A longer new subsequence ending at x would require an existing length-(i+1) subsequence ending below x, contradicting the choice of i.
- If there is no such position, x extends the longest current subsequence and is appended.

Thus each update preserves exactly the stated invariant. After all inputs, `len(tails)` is L. Binary search finds the update position; it does not guess the final deletion count or L.

Example: when `tails = [1,4,7]`, a new 5 replaces 7. A length-two subsequence ending at 4 can extend to length three ending at 5. Replacing 4 would worsen the length-two state, while appending would incorrectly claim a length-four subsequence.

**Important:** `tails` is a collection of best endings for different lengths, not necessarily one actual subsequence. Updating an ending is not a literal deletion or modification of an earlier input value. For `[2,3,1]`, final `tails` is `[1,3]`, which is not a subsequence in that order.

## Exact User Submission — Verified

The following is the submitted implementation, not an assistant rewrite. It was written after the state and update logic were explained.

```python
import bisect

def min_deletions(nums):
    tails = []
    for n in nums:
        if len(tails)<1:
            tails.append(n)
        else:
            if n>tails[-1]:
                tails.append(n)
            else:
                i = bisect.bisect_left(tails,n)
                tails[i] = n
    return len(nums)-len(tails)

print(min_deletions([3,1,3,2,5,6]))
print(min_deletions([]))
print(min_deletions([3]*5))
```

Outputs: 2, 0, 4. Using `bisect_left` replaces an equal ending, so duplicates do not extend a strictly increasing subsequence. Time is $`O(n\log n)`$ and auxiliary space is $`O(n)`$ in the worst case. The input is unchanged.

Verification evidence and the assisted-versus-independent distinction are in the dated assessment below.

## Interview Classification

This combines DP thinking, greedy dominance of equal-length states, and binary search on ordered state values. It is equivalent to [LeetCode 300 — Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/), officially Medium; the logarithmic-update algorithm is its follow-up requirement. The explanation that deriving tails is harder than implementing it is a pedagogical assessment, not a different official difficulty rating.

## Assessment History

- [October 23 Q1 — assessment, archived October 24](../../DailyTests/2026-10-23.md#q1--minimum-deletions-for-a-strictly-increasing-subsequence)

## Connections

- [C009 — Minimize Maximum Contiguous Group Sum](C009_Minimize_Maximum_Contiguous_Group_Sum.md): binary search on an answer with a feasibility predicate, versus binary search for a state-update position here.
- [C012 — Edit Distance](C012_Edit_Distance.md): explicit DP-state meaning and optimal substructure; the state representation and recurrence differ.

## What to Remember

For equal progress, ask whether one state is at least as useful for every possible future continuation. Here equal length plus a smaller ending is enough to discard competing endings.
