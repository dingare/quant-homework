# C007 — Longest Balanced Binary Subarray

## Metadata

- Category: Coding
- Tags: Prefix Sums, Earliest Occurrence, Hashing
- Date Added: 2026-10-22
- Original drill dates: 2026-10-07, 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-07 Q4

Source and assessment: [2026-10-07 Q4](../../DailyTests/2026-10-07.md#q4--longest-balanced-binary-subarray). The reference material below does not change that attempt’s recorded result.

### Question

Given a binary array, return the maximum length of a contiguous subarray containing equal numbers of zeros and ones. Example: [0, 1, 0, 0, 1, 1, 0] returns 6. Target $`O(n)`$ time and $`O(n)`$ space. Explain the invariant, write Python 3, and test one edge case.

### Recorded solution

Equal counts become a zero-sum subarray. Repeated prefix balances identify valid intervals. Store the earliest occurrence only to maximize length, initialized with first = {0: -1}; at index i, use i - first[balance]. Do not overwrite an earlier index.

### Related Notes

- [C001 — Count of Range Sums with Prefix Sums and a Fenwick Tree](C001_Count_of_Range_Sums_with_Prefix_Sums_and_Fenwick_Tree.md): related prefix-difference representation, not the same algorithm. This equal-balance problem needs a first-occurrence hash, not a Fenwick tree.

## Assessment history

- [2026-10-07 Q4 — assessment](../../DailyTests/2026-10-07.md#q4--longest-balanced-binary-subarray)
- [2026-10-09 Q8 — assessment](../../DailyTests/2026-10-09.md#q8--equal-01-subarray)

## Related questions and knowledge

- [C001 — Count of Range Sums with Prefix Sums and a Fenwick Tree](C001_Count_of_Range_Sums_with_Prefix_Sums_and_Fenwick_Tree.md) — Prefix differences; earliest-index hashing versus ordered range counting.
