# C009 — Minimize Maximum Contiguous Group Sum

## Metadata

- Category: Coding
- Tags: Binary Search, Greedy Feasibility, Partitioning
- Date Added: 2026-10-22
- Original drill dates: 2026-10-08; ship-capacity repeat on 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-08 Q4

Source and assessment: [2026-10-08 Q4](../../DailyTests/2026-10-08.md#q4--minimize-the-largest-group-sum). The reference material below does not change that attempt’s recorded result.

### Question

Partition a list of positive integers into at most k nonempty contiguous groups to minimize the largest group sum. For nums = [7,2,5,10,8] and k = 2, return 18. Write efficient Python 3 and explain correctness and complexity.

### Recorded solution

Binary-search a limit M between max(nums) and sum(nums). Greedily extend each group until the next element would exceed M, then open a group. For positive integers, taking the longest feasible prefix minimizes the number of groups. Feasible means at most k groups; increasing M preserves feasibility. Search for the first feasible integer limit. Time $`O(n\log(S+1))`$, where S is the sum; auxiliary space $`O(1)`$. Assume a nonempty list and $`k\ge1`$.

### Related Notes

- [New binary-search-on-answer gap](../../Backlog.md#october-8-interview-knowledge-gaps).
- [C005 — Maximum Subarray Sum, Fixed and Minimum Length](C005_Maximum_Subarray_Sum_Fixed_and_Minimum_Length.md): related contiguous-sum setting, but a different objective and algorithm; prefix sums alone do not solve this partition problem efficiently.

## Assessment history

- [2026-10-09 Q4 original — ship-capacity repeat](../../DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement). Exact prompt wording was not retained; the archived record identifies the same binary-search / greedy-feasibility structure. This accidental repeat is excluded from new coverage.
- [2026-10-08 Q4 — assessment](../../DailyTests/2026-10-08.md#q4--minimize-the-largest-group-sum)

## Related questions and knowledge

- [C016 — Median of Two Sorted Arrays](C016_Median_of_Two_Sorted_Arrays.md) — Monotone binary search; feasibility predicate versus partition invariant.
