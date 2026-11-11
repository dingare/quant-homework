# C025 — Search in a Rotated Sorted Array

## Metadata

- Category: Coding
- Tags: Arrays, Search, Invariants, Complexity
- Date Added: 2026-11-11
- Original drill: November 10, 2026, Q4.
- Status: Pending; original prompt only. No hints or solution supplied.

## Core Question

An array was originally strictly increasing and was then cyclically rotated an unknown number of positions, possibly zero. All values remain distinct.

Implement runnable Python 3:

```python
def locate(a: list[int], target: int) -> int:
    ...
```

Return the target's index in the supplied array, or -1 if absent.

```text
a = [8, 11, 15, -4, 0, 3], target = 0 -> 4
a = [8, 11, 15, -4, 0, 3], target = 7 -> -1
a = [], target = 2 -> -1
```

Require $`O(\log n)`$ worst-case time and $`O(1)`$ auxiliary space, without modifying the input. State the invariant that justifies discarding elements.

Then answer orally: if duplicates are allowed, can the same worst-case time guarantee always be preserved? Justify your answer with a concrete family of inputs.

## Assessment History

- [November 10 Q4](../../DailyTests/2026-11-10.md#q4--rotated-array-search): Pending; no code submitted or answer assessed.
