# C017 — Minimum Units for Overlapping Tasks

## Metadata

- Category: Coding
- Tags: Intervals, Heaps, Greedy Optimality
- Date Added: 2026-10-22
- Original drill dates: 2026-10-17
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-17 Q1

Source and assessment: [2026-10-17 Q1](../../DailyTests/2026-10-17.md#q1--minimum-units-for-overlapping-tasks). The reference material below does not change that attempt’s recorded result.

### Question

Implement runnable Python 3 `allocate_units(intervals: list[tuple[int, int]]) -> tuple[int, list[int]]`. Task i occupies one identical processing unit throughout the half-open interval from its start to its end. Tasks sharing an endpoint may reuse a unit. Return the minimum unit count and a unit ID for each task in original input order; IDs range from zero to count minus one. Up to 200,000 tasks in arbitrary order; integer endpoints with start strictly before end; identical intervals allowed. Do not modify the input. Empty input returns `(0, [])`.

Target $`O(n\log n)`$ time. Explain the invariant and optimality, distinguish auxiliary from output space, and include runnable tests for shared endpoints, identical intervals and empty input.

### Key solution

Sort tasks by start time while retaining original indices. Keep exactly one heap entry `(latest_end, unit_id)` per allocated unit. If the minimum end is at or before the next start, replace that entry; otherwise allocate another unit. A minimal repair of the user's approach is:

```python
import heapq


def allocate_units(intervals):
    if not intervals:
        return 0, []
    unit = []
    unit_number = 0
    order = [0] * len(intervals)
    sorted_intervals = sorted(enumerate(intervals), key=lambda x: x[1][0])
    for i_index, (s, e) in sorted_intervals:
        earliest = unit[0] if unit else (-float('inf'), 0)
        if earliest[0] <= s:
            if unit:
                heapq.heappop(unit)
            order[i_index] = earliest[1]
            heapq.heappush(unit, (e, earliest[1]))
        else:
            unit_number += 1
            order[i_index] = unit_number
            heapq.heappush(unit, (e, unit_number))
    return unit_number + 1, order
```

When a new unit is required, every existing unit's latest task is still active at the current start. Those tasks and the new task overlap, so every feasible allocation needs at least this many units. Reuse preserves feasibility. This proves minimum count. Time is $`O(n\log n)`$; the heap uses $`O(R)`$ for R units, the sorted task copy uses $`O(n)`$ auxiliary space, and output uses $`O(n)`$ space.

## Assessment history

- [2026-10-17 Q1 — assessment](../../DailyTests/2026-10-17.md#q1--minimum-units-for-overlapping-tasks)

## Related questions and knowledge

- [C014 — Maximum-Profit Compatible Jobs](C014_Maximum_Profit_Compatible_Jobs.md) — Interval scheduling; maximum profit versus minimum required units.
- [C010 — Kth Largest: Heap and Quickselect](C010_Kth_Largest_Heap_and_Quickselect.md) — Min-heap invariant and update order.
