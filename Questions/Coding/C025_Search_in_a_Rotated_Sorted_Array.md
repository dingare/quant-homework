# C025 — Search in a Rotated Sorted Array

## Metadata

- Category: Coding
- Tags: Arrays, Search, Invariants, Complexity
- Date Added: 2026-11-11
- Original drill: November 10, 2026, Q4.
- Status: Discussed; exact user code tested and found flawed, minimal iterative correction supplied and tested. Independent corrected resubmission not received.

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

## Submitted Approach and Implementation Issues

The user independently organized the search around sorted versus rotated intervals, midpoint comparisons, and recursive interval narrowing. This is the actual submitted implementation, not the corrected reference:

```python
import bisect

def locate_recursive(a,target,start,end):
    l = start
    r = end
    if l>=r:
        if l>r:
            return -1
        elif a[l]==target:
            return l
        else:
            return -1
    if a[r]>a[l]>target:
        return -1
    if a[l]<a[r]:
        if a[l]>target:
            return -1
        # else it is a strictly increasing
        i = l+bisect.bisect_left(a[l:r],target)
        if a[i]==target:
            return i
        else:
            return -1
    else:
        #rotated
        m = (l+r)//2
        if a[l]==target:
            return l
        if a[r]==target:
            return r
        if a[m] == target:
            return m
        if a[m]>a[l]: #rotated on the right
            if a[m]<target:
                if a[l]<target:
                    return locate_recursive(a,target,l,m)
                else:
                    return locate_recursive(a,target,m,r)
            else:
                if a[l]<target:
                    return locate_recursive(a,target,l,m)
                else:
                    return locate_recursive(a,target,m,r)
        else:
            if a[m]>target: #rotated on the left, and target in the left
                return locate_recursive(a,target,l,m)
            else:
                return locate_recursive(a,target,m,r) #target in the right, increasing
    return -1

def locate(a,target):
    return locate_recursive(a,target,0,len(a)-1)
```

The five supplied examples passed. Additional checks exposed two correctness failures and a complexity issue:

- For [1, 2, 3, 0], target 3, the first midpoint value is 2. A branch selects the left interval even though its values cannot contain 3, so the target is lost.
- For [1, 0], target 2, a recursive call retains the same two-element interval, eventually raising RecursionError. After ruling out the midpoint, the next interval should exclude it.
- The slice passed to bisect copies elements and costs linear time/space. Recursion also uses stack space. Thus the original code cannot meet the requested bounds, even on terminating cases with a large sliced sorted interval.

The interval-sorted branch's slice excludes its right endpoint, but the subsequent insertion-index check can still test that endpoint. This is not a separately diagnosed endpoint bug.

## Minimal Correction — Assistant Reference

Preserve the helper signature and the early bisect branch for a completely sorted interval. Use bisect's bounds directly, and update interval boundaries in a loop to avoid stack allocation. The historical helper name is retained to minimize changes; the function is iterative.

```python
import bisect


def locate_recursive(a, target, start, end):
    l = start
    r = end

    while l <= r:
        if a[l] <= a[r]:
            i = bisect.bisect_left(a, target, l, r + 1)
            return i if i <= r and a[i] == target else -1

        m = (l + r) // 2
        if a[m] == target:
            return m

        if a[m] >= a[l]:
            if a[l] <= target < a[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if a[m] < target <= a[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


def locate(a, target):
    return locate_recursive(a, target, 0, len(a) - 1)
```

### Invariant and search decisions

If the target exists, it remains inside the current inclusive interval. With distinct values, a completely increasing interval can be searched directly. Otherwise, compare the midpoint and left endpoint to identify a sorted half. Test both value bounds of that half to decide whether to retain it. The midpoint has already been tested and is excluded from the next interval.

Each continuing iteration removes at least half of the candidates. If the bisect branch executes, it returns immediately. Total time is $`O(\log n)`$ and auxiliary space is $`O(1)`$, with no input mutation. This invariant and correction were supplied; the reference is not a verified independent user repair.

### Why the original branching grew complicated

The original code tracked both the rotation location and the target location through nested cases. Some branches repeated the same inner decision regardless of the outer condition. A more compact decision structure asks which half is sorted, then whether the target lies in its value interval. The sorted-whole-interval bisect branch is optional; retaining it here preserves the user's organization without changing the asymptotic bounds.

## Follow-up — Duplicates

The user independently proposed that duplicates can force checking elements individually in the worst case. A concrete family supplied afterward was:

```text
[1, 1, 1, 1, 1, 1]   # target 0 absent
[1, 1, 1, 0, 1, 1]   # the single 0 can occupy any position
```

Every such array is a rotation of a nondecreasing array. Observing a 1 does not rule out an unexamined position containing the only 0. To establish absence in the all-ones case, the worst case requires examining all positions, giving a linear lower bound. Duplicates do not force linear work on every input, but logarithmic worst-case time is no longer guaranteed.

The reference code above assumes distinct values and is not a duplicate-supporting implementation.

## Connections

- [C024 — Next Permutation](C024_Next_Permutation_in_Place.md): the same session exposed Python slicing allocation; the safe-discard proof in this search is different from the permutation suffix invariant.

## Assessment History

- [November 10 Q4, continuation November 11](../../DailyTests/2026-11-10.md#q4--rotated-array-search): Partial / Hinted; exact user code practiced and tested, I errors observed, reference separately verified. The duplicate worst-case direction was independent; the concrete lower-bound family and explanation were supplied.
