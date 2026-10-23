# C012 — Edit Distance

## Metadata

- Category: Coding
- Tags: Dynamic Programming, String Alignment
- Date Added: 2026-10-22
- Original drill dates: 2026-10-10
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-10 Q4

Source and assessment: [2026-10-10 Q4](../../DailyTests/2026-10-10.md#q4--edit-distance). The reference material below does not change that attempt’s recorded result.

### Question

Return the minimum unit-cost insertions, deletions or replacements to transform `source` into `target`. No swaps; empty strings allowed; each length at most 2,000. Implement `min_changes`, explain complexity and test. Examples: `cat → cut` costs 1, empty → `abc` costs 3, `ab → ba` costs 2.

### Key solution

Use prefix lengths as states, with empty-prefix boundaries:

```math
D_{0,j}=j,\quad D_{i,0}=i,\qquad
D_{i,j}=\min\left\{D_{i-1,j}+1,\ D_{i,j-1}+1,\ D_{i-1,j-1}+\mathbf1\{s_i\ne t_j\}\right\}.
```

```python
def min_changes(source, target):
    n, m = len(source), len(target)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n):
        for j in range(m):
            if source[i] == target[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = 1 + min(
                    dp[i + 1][j],  # insertion
                    dp[i][j + 1],  # deletion
                    dp[i][j],      # replacement
                )
    return dp[n][m]
```

Time and space $`O(nm)`$; two rolling rows reduce auxiliary space to $`O(\min(n,m))`$.

## Assessment history

- [2026-10-10 Q4 — assessment](../../DailyTests/2026-10-10.md#q4--edit-distance)

## Related questions and knowledge

- [C014 — Maximum-Profit Compatible Jobs](C014_Maximum_Profit_Compatible_Jobs.md) — Optimal substructure and the meaning of a DP state.
