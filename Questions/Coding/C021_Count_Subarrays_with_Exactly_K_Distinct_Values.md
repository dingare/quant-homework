# C021 — Count Subarrays with Exactly K Distinct Values

## Metadata

- Category: Coding
- Tags: Sliding Window, Two Pointers, Frequency Map, Counting Invariant
- Date Added: 2026-11-01
- Original drill: October 31, 2026, Q1
- Status: Discussed; reference implementation supplied. User-code assessment is recorded separately.

## Core Question

Implement runnable Python 3:

```python
def count_segments(labels: list[int], k: int) -> int:
    ...
```

Return the number of nonempty contiguous subarrays containing exactly k distinct values. Different index boundaries count separately. There are up to 200,000 integers, including negative values and duplicates; k is nonnegative. Do not modify the input. Empty input or k = 0 returns 0.

- `[4, 7, 4, 9]`, k = 2 returns 4.
- `[5, 5, 5]`, k = 1 returns 6.

Derive expected linear time under standard hashing assumptions, explain the invariant and why each qualifying subarray is counted exactly once, state auxiliary space, and include runnable edge tests. Original budget: 20 minutes; actual time not recorded.

## Intuition and counting invariant

Let A(t) count nonempty subarrays with at most t distinct values. Then:

```math
\mathrm{Count}\{\text{subarrays with exactly }k\text{ distinct values}\}=A(k)-A(k-1).
```

For A(t), advance the right endpoint once per outer iteration. Maintain value frequencies in the current window. While the number of keys exceeds t, remove the leftmost value and advance left. Delete a key only when its frequency becomes zero.

After shrinking, left is the smallest valid starting index for this right endpoint. Every start from left through right produces a valid subarray; earlier starts remain invalid. This contributes right minus left plus one. For t = 0 the window becomes empty and contributes zero. Every subarray is counted exactly once, at its right endpoint.

For four equal values, A(1) receives contributions 1, 2, 3, 4, totaling 10. A(0) is zero. Adding only one per valid window misses different legal starting positions.

## Reference implementation

The following code was supplied by the assistant after the user's attempt; it is not a verified independent user rewrite.

```python
def count_segments(labels: list[int], k: int) -> int:
    if not labels or k == 0:
        return 0

    def at_most(limit: int) -> int:
        freq = {}
        left = 0
        total = 0

        for right, value in enumerate(labels):
            freq[value] = freq.get(value, 0) + 1

            while len(freq) > limit:
                old = labels[left]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]
                left += 1

            total += right - left + 1

        return total

    return at_most(k) - at_most(k - 1)


assert count_segments([4, 7, 4, 9], 2) == 4
assert count_segments([4, 4, 4, 4], 1) == 10
assert count_segments([4, 7, 7, 5], 2) == 4
assert count_segments([4, 4, 4, 4], 2) == 0
assert count_segments([0, 1], 1) == 2
assert count_segments([], 2) == 0
assert count_segments([1, 2], 0) == 0
```

Each pointer advances at most n times per helper call. Two calls therefore take expected O(n) time, with O(n) auxiliary space as a simple upper bound. Frequency storage during insertion is at most the smaller of n and k + 1 distinct keys. No index lists are required; list concatenation copies elements and `pop(0)` shifts elements, so those operations would undermine the linear-time argument.

## Common mistakes

- `res += 1` counts a single visited window rather than all valid starting indices.
- The contribution right minus left plus one applies to the at-most predicate; shorter windows can have fewer than k distinct values, so it cannot be substituted directly into an exactly-k branch.
- An outer condition `left <= right` can terminate on a temporarily empty window even when later right endpoints still need processing. The submitted code returned 1 rather than 2 on `[0, 1]`, k = 1.
- Distinct count alone does not determine whether adding or removing a value changes that count; maintain membership frequencies.

## Connections

- [C004 — Sliding Window Maximum](C004_NeetCode_Sliding_Window_Maximum.md): both advance window boundaries; this question uses a frequency constraint rather than a monotonic deque.
- [C007 — Longest Balanced Binary Subarray](C007_Longest_Balanced_Binary_Subarray.md): counting interval properties versus a prefix-state equality; the solution invariants differ.

## Assessment History

- [October 31 drill, continued through November 1 — Q1](../../DailyTests/2026-10-31.md#q1--exactly-k-distinct-subarrays).

## What to Remember

Exactly-k counting can be expressed as the difference of two at-most counts. Explain the legal-start interval before writing the counting update.
