# C023 — Trapping Rain Water with Two Pointers

## Metadata

- Category: Coding
- Tags: Two Pointers, Per-Position Contribution, Boundary Invariant
- Date Added: 2026-11-07
- Original drill: November 7, Q1
- Status: Discussed; algorithm supplied, exact user implementation verified. See the dated assessment for performance evidence.

## Core Question

You are given nonnegative integer heights representing adjacent bars of unit width. Rain falls onto the bars; water can escape beyond either end.

Implement runnable Python 3:

```python
def trapped_water(heights: list[int]) -> int:
    ...
```

Return the total volume of trapped water. There are up to 200,000 bars; empty input returns 0. Do not modify the input. `[3,0,2,0,4]` returns 7 and `[2,2,2]` returns 0.

Derive an approach using $`O(n)`$ time and $`O(1)`$ auxiliary space. Explain the invariant that makes each decision safe, justify why every contribution is counted correctly, and include runnable edge tests.

## Intuition — 从整段面积到每列贡献

本次讨论中最重要的表示转换：先问“每列贡献多少水”，再考虑双指针。按整段凹槽计算需要处理临时水位、边界变化和重复计数；拆成每列以后，只需要知道左右边界如何限制这一列的水位。

```math
L_i=\max_{0\le j\le i}h_j,\qquad
R_i=\max_{i\le j\lt n}h_j,\qquad
w_i=\min(L_i,R_i)-h_i.
```

左右最大值包括当前位置，因此贡献非负。预先存储两个最大值数组可得到线性时间、线性空间算法。

继续省空间时，不必总知道右侧最高值的精确值：若左侧最高为 3，而右侧已经找到高度至少为 5 的边界，未知的中间高度不会改变当前左列的水位 3。关键是已知边界足够高，而不是先猜出“双指针”这个名称。

### Original interval-area idea and its limits

For boundary indices l and r, the rectangle-minus-bars expression is valid when every interior bar is no higher than the shorter boundary:

```math
V(l,r)=\min(h_l,h_r)(r-l-1)-\sum_{i=l+1}^{r-1}h_i.
```

This is a segment total, not automatically a new contribution. For `[5,0,3,0,4]`, the first basin contributes 3 before the final boundary is seen; the full segment later contains 9, so the additional amount is 6. For `[5,0,3,0,2]`, an interior bar exceeds the final right boundary; blindly applying the full-segment rectangle gives 3 rather than the actual 5. Different basins can have different water levels.

The user's clarification was that the proposed scan incrementally updated water volume, not that it recomputed and added the entire segment. Preserve this clarification rather than attributing the assistant's initial interpretation to the user.

## Solution and invariant

Maintain left and right indices bounding the unprocessed interval, together with the maximum height scanned from each end. Include the current endpoint heights in these maxima before comparing them.

- If the left maximum is no greater than the right maximum, the exact left-side maximum for the left column is known, and a right-side boundary at least that high is already known. Its water contribution is the left maximum minus its height. Process that column and move left forward.
- Otherwise, the symmetric argument determines the right column using the right maximum. Process it and move right backward.

Every processed column has its final contribution determined; later discoveries cannot change it. Every column is processed exactly once. The two indices move a total of n times, giving linear time and constant auxiliary space. This proof and complexity explanation were supplied in discussion, not independently demonstrated by the user.

## Exact user implementation — unchanged

Submitted after the algorithm was explained; it required no repair.

```python
def trapped_water(heights):
    l = 0
    r = len(heights)-1
    l_max, r_max = 0,0
    total = 0
    while l<=r:
        l_max = max(l_max,heights[l])
        r_max = max(r_max,heights[r])
        if l_max<=r_max:
            total+= l_max - heights[l]
            l +=1
        else:
            total+= r_max - heights[r]
            r-=1
    return total

print(trapped_water([5,0,3,0,4]))
```

Output: `9`. The dated assessment records the original validation, including edge cases, randomized comparisons, input preservation and large inputs.

## What to Remember

总量 → 每个位置的贡献 → 贡献依赖什么信息 → 一个已知的界是否足以确定贡献。这里有两次转换：整段面积到每列贡献；精确知道两侧最高到只需证明另一侧足够高。Reported understanding of this representation is not an independently demonstrated cold reconstruction.

## Connections

- [C021 — Exactly-K Distinct Subarrays](C021_Count_Subarrays_with_Exactly_K_Distinct_Values.md): another contribution-counting problem, with a different window invariant and state.
- [C004 — Sliding Window Maximum](C004_NeetCode_Sliding_Window_Maximum.md): a different method for maintaining maxima; it does not establish this problem's finalization invariant.

## Assessment History

- [November 7 Q1](../../DailyTests/2026-11-07.md#q1--trapping-rain-water): Partial / Hinted overall; exact user implementation verified. See the log for assistance, clarification and timing limits.
