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

## Algorithm to Implementation

The outer search retains the smallest feasible capacity inside `[low, high]`. For a trial limit, greedily fill the current group and start another only when necessary. Any valid partition must end its first group no later than this longest feasible prefix; repeating the argument shows the greedy scan uses the fewest groups. Therefore needing more than k groups proves infeasibility. A feasible limit moves `high` down; an infeasible limit moves `low` above it.

```python
def minimize_largest_group_sum(nums: list[int], k: int) -> int:
    if not nums or k < 1:
        raise ValueError("Require nonempty positive nums and k >= 1")

    def feasible(limit):
        groups, current = 1, 0
        for value in nums:
            if current + value > limit:
                groups += 1
                current = value
                if groups > k:
                    return False
            else:
                current += value
        return True

    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if feasible(mid):
            high = mid
        else:
            low = mid + 1
    return low


assert minimize_largest_group_sum([7, 2, 5, 10, 8], 2) == 18
assert minimize_largest_group_sum([7, 2, 5], 1) == 14
assert minimize_largest_group_sum([7, 2, 5], 5) == 7
assert minimize_largest_group_sum([9], 1) == 9
```

Assumes positive integer entries, as specified in the question; this greedy predicate does not extend to arbitrary signed inputs. Time O(n log(S+1)), auxiliary space O(1), where S is the total sum. Input is unchanged. Shipping capacity within k days uses the same function when weights are positive and loading preserves input order.

Reference added during the code-completion review; historical assessment results are unchanged.

## Assessment history

- [2026-10-09 Q4 original — ship-capacity repeat](../../DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement). Exact prompt wording was not retained; the archived record identifies the same binary-search / greedy-feasibility structure. This accidental repeat is excluded from new coverage.
- [2026-10-08 Q4 — assessment](../../DailyTests/2026-10-08.md#q4--minimize-the-largest-group-sum)

## Related questions and knowledge

- [C016 — Median of Two Sorted Arrays](C016_Median_of_Two_Sorted_Arrays.md) — Monotone binary search; feasibility predicate versus partition invariant.
