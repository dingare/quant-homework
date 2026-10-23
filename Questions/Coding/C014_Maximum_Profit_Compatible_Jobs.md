# C014 — Maximum-Profit Compatible Jobs

## Metadata

- Category: Coding
- Tags: Intervals, Dynamic Programming, Binary Search
- Date Added: 2026-10-22
- Original drill dates: 2026-10-11
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-11 Q4

Source and assessment: [2026-10-11 Q4](../../DailyTests/2026-10-11.md#q4--maximum-profit-compatible-jobs). The reference material below does not change that attempt’s recorded result.

### Question

Implement `max_profit(jobs)` for up to 200,000 `(start,end,profit)` jobs with $`\mathrm{start}\lt\mathrm{end}`$. Input order arbitrary, duplicate intervals and negative profits allowed. Endpoints may touch; selecting none is allowed. Explain complexity and test. `[(1,3,5),(2,5,6),(3,6,5),(6,7,4)]` returns 14.

### Key solution

Sort by finish time. Let $`D_i`$ be best profit from the first $`i`$ jobs and $`j_i`$ the number of earlier jobs ending no later than job $`i`$ starts:

```math
D_0=0,\qquad D_i=\max\{D_{i-1},D_{j_i}+p_i\}.
```

In a zero-based loop, use `j = bisect_right(ends, start, 0, i)` and `dp[i+1] = max(dp[i], dp[j] + profit)`. Time $`O(n\log n)`$; space $`O(n)`$.

## Assessment history

- [2026-10-11 Q4 — assessment](../../DailyTests/2026-10-11.md#q4--maximum-profit-compatible-jobs)

## Related questions and knowledge

- [C012 — Edit Distance](C012_Edit_Distance.md) — Optimal substructure and the meaning of a DP state.
- [C017 — Minimum Units for Overlapping Tasks](C017_Minimum_Units_for_Overlapping_Tasks.md) — Interval scheduling; maximum profit versus minimum required units.
