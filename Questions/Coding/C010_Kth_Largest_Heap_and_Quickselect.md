# C010 — Kth Largest: Heap and Quickselect

## Metadata

- Category: Coding
- Tags: Heaps, Selection, Partitioning
- Date Added: 2026-10-22
- Original drill dates: 2026-10-09
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-09 Q4

Source and assessment: [2026-10-09 Q4](../../DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement). The reference material below does not change that attempt’s recorded result.

### Question

Return the kth-largest array element without fully sorting. First give an `O(n log k)` method; then identify an expected-`O(n)` follow-up.

### Recorded answer details

Maintain a min-heap containing the largest k values seen so far. Push while `len(heap) < k`, then compare with its minimum. Time is `O(n log k)` and space `O(k)`. Quickselect partitions and continues only on the side containing index `n-k`; expected `O(n)`, worst-case `O(n^2)`.

## Assessment history

- [2026-10-09 Q4 — assessment](../../DailyTests/2026-10-09.md#q4--original-repeat-and-kth-largest-replacement)

## Related questions and knowledge

- [C003 — Online Median with Two Heaps](C003_Online_Median_with_Two_Heaps.md) — Heap size and ordering invariants.
- [C017 — Minimum Units for Overlapping Tasks](C017_Minimum_Units_for_Overlapping_Tasks.md) — Min-heap invariant and update order.
