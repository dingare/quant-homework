# C016 — Median of Two Sorted Arrays

## Metadata

- Category: Coding
- Tags: Binary Search, Partition Invariant
- Date Added: 2026-10-22
- Original drill dates: 2026-10-15
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-15 Q1

Source and assessment: [2026-10-15 Q1](../../DailyTests/2026-10-15.md#q1--median-of-two-sorted-arrays). The reference material below does not change that attempt’s recorded result.

### Question

Implement runnable Python 3 `combined_median(a, b) -> float` for two sorted integer arrays. Either may be empty, but their combined length is positive. Negative values and duplicates are allowed; do not modify the inputs, merge the arrays, or sort their combined contents. Target logarithmic time in the shorter array length and constant auxiliary space. Explain correctness/complexity and test empty arrays, unequal lengths and duplicates.

Examples: `[1,3]`, `[2]` gives 2.0; `[1,2]`, `[3,4]` gives 2.5; `[]`, `[-5,-1]` gives -3.0; `[1,1,1]`, `[1,2]` gives 1.0.

### Key solution

The user's independent approach partially merged the arrays until the median ranks. This can yield a correct linear-time solution, but does not meet the logarithmic target. If `p` values have been consumed and `i`/`j` point to the next unconsumed values, global one-based rank `k` is offset `k - p - 1` into the surviving suffix. When neither median has been collected, skip values before the lower median before collecting the two central values.

For the target solution, binary-search the partition of the shorter array. If its left side contains `i` elements, the other array contributes `j = left_size - i`.

```math
L=\left\lfloor\frac{m+n+1}{2}\right\rfloor,\qquad i+j=L.
```

Within-array ordering already holds. A valid partition only needs the two cross-boundary comparisons:

```math
a_{i-1}\le b_j,\qquad b_{j-1}\le a_i.
```

Treat empty left/right boundaries as negative/positive infinity. If the first comparison fails, decrease `i`; if the second fails, increase `i`. These failures remain failures farther in the wrong direction. At a valid partition, take the maximum left boundary for odd total length; average the maximum left and minimum right boundaries for even total length.

```python
def combined_median(a, b):
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    if m + n == 0:
        raise ValueError("At least one array must be nonempty")

    left_size = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = left_size - i
        a_left = a[i - 1] if i > 0 else float("-inf")
        a_right = a[i] if i < m else float("inf")
        b_left = b[j - 1] if j > 0 else float("-inf")
        b_right = b[j] if j < n else float("inf")

        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    raise ValueError("Inputs must be sorted")
```

Time is logarithmic in the shorter array length, with constant time when it is empty; auxiliary space is constant. Rebinding `a, b` does not mutate inputs.

## Assessment history

- [2026-10-15 Q1 — assessment](../../DailyTests/2026-10-15.md#q1--median-of-two-sorted-arrays)

## Related questions and knowledge

- [C009 — Minimize Maximum Contiguous Group Sum](C009_Minimize_Maximum_Contiguous_Group_Sum.md) — Monotone binary search; feasibility predicate versus partition invariant.
- [C003 — Online Median with Two Heaps](C003_Online_Median_with_Two_Heaps.md) — Median selection from sorted data versus online median maintenance.
