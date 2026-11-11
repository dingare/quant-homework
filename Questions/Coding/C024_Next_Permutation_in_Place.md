# C024 — Next Permutation in Place

## Metadata

- Category: Coding
- Interview Relevance: Lexicographic greedy reasoning, suffix invariants, duplicate handling, and implementation under time and space constraints.
- Tags: Arrays, Greedy, Invariants, In-Place Reversal, Complexity
- Date Added: 2026-11-11
- Original drill: November 10, 2026, Q1; discussed through November 11.
- Status: Discussed; the minimal constant-space correction was supplied on request. Dated performance and verification limits are in the assessment link below.

## Core Question

Implement runnable Python 3:

```python
def next_permutation(a: list[int]) -> None:
    ...
```

Modify a in place into the lexicographically smallest permutation strictly greater than its current ordering. If no greater permutation exists, replace it with the lexicographically smallest ordering. Duplicate values are allowed.

```text
[1, 2, 3] -> [1, 3, 2]
[1, 3, 2] -> [2, 1, 3]
[2, 2, 1] -> [1, 2, 2]
[]        -> []
```

Use $`O(n)`$ time and $`O(1)`$ auxiliary space. Do not enumerate permutations or call a sorting routine. Explain why the result is the immediate successor rather than merely a larger permutation.

## Solution and Intuition

Scan from right to left while the encountered values are nondecreasing in that scanning direction. Equivalently, the suffix in the original array is nonincreasing. Equal values belong to the suffix.

If the entire array is nonincreasing, it is already the largest ordering; reverse the whole array. Otherwise, the position immediately before this suffix is the pivot.

The suffix alone cannot be rearranged into a greater ordering. Preserve the longest possible prefix by increasing the pivot. Replace it with the smallest suffix value strictly greater than it. Since the suffix is nonincreasing, scanning from its right end finds precisely that value first. Exchange the two positions. The suffix remains nonincreasing after replacement, so reversing it gives the smallest possible suffix.

Example:

```text
[1, 5, 4, 2] -> [2, 5, 4, 1] -> [2, 1, 4, 5]
```

This preserves the earlier prefix, makes the smallest possible pivot increase, and minimizes everything afterward.

## Latest Handwritten Submission — Correct Returned Values, Incomplete In-Place Mutation

This is the user's submitted implementation, preserved without repair. It is not the constant-space reference.

```python
import bisect

def find_swap_i(numbers,x):
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i]>x:
            return i
    return -1

def reverse(numbers):
    l = 0
    r = len(numbers)-1
    while l<r:
        numbers[l], numbers[r] = numbers[r],numbers[l]
        l+=1
        r-=1
    return numbers

def next_permutation(a):
    l = len(a)
    i = len(a)-1
    prev = -float('inf')
    while i>=0:
        if a[i]>=prev:
            prev = a[i]
            i-=1
        else:
            swap_i = i+1+find_swap_i(a[i+1:],a[i])
            a[swap_i],a[i] = a[i], a[swap_i]
            return a[:i+1]+reverse(a[i+1:])
    return reverse(a)
```

The right-to-left scan, strict successor selection and duplicate handling are correct. The remaining issue is Python list ownership: a slice creates a separate list. Reversing a sliced suffix changes the copy, and concatenation returns another list. The original list has only been partially updated on the pivot branch.

```text
Input:               [1, 0, 2, 1]
Returned permutation: [1, 1, 0, 2]
Original list after:  [1, 1, 2, 0]
```

A helper can use constant space internally while the caller allocates linear space before invoking it. Returning a newly constructed correct list does not satisfy the requested in-place interface.

## Minimal Constant-Space Correction — Assistant Reference

Keep the user's scan, prev variable, linear successor search, and separate reversal helper. Pass the original list and index boundaries instead of slices. The successor helper now returns an absolute index, so no suffix offset is added.

```python
def find_swap_i(numbers, x, start):
    for i in range(len(numbers)-1, start-1, -1):
        if numbers[i] > x:
            return i
    return -1


def reverse(numbers, l, r):
    while l < r:
        numbers[l], numbers[r] = numbers[r], numbers[l]
        l += 1
        r -= 1


def next_permutation(a):
    i = len(a)-1
    prev = -float('inf')

    while i >= 0:
        if a[i] >= prev:
            prev = a[i]
            i -= 1
        else:
            swap_i = find_swap_i(a, a[i], i+1)
            a[swap_i], a[i] = a[i], a[swap_i]
            reverse(a, i+1, len(a)-1)
            return

    reverse(a, 0, len(a)-1)


a = [1, 0, 2, 1]
next_permutation(a)
assert a == [1, 1, 0, 2]
```

A strict successor exists on the pivot branch because the immediate right neighbor exceeds the pivot. Thus find_swap_i cannot return -1 there. With no pivot, the whole array is reversed, including empty and singleton inputs.

## Complexity and Common Mistakes

- Finding the pivot, finding a successor, and reversing the suffix are successive linear operations, not nested scans. Their total is $`O(n)`$.
- A binary successor search would run once, giving $`O(n+\log n)=O(n)`$ overall; it is unnecessary for the target bound.
- The corrected implementation stores only indices and scalar values: $`O(1)`$ auxiliary space.
- The initial reversed-list implementation used a strict comparison while collecting the suffix; equality could trigger an invalid successor lookup. The later handwritten submission fixed this with a non-strict comparison.
- Slice assignment can update the original list, but constructing slices or concatenated results still consumes $`O(n)`$ extra space. Passing index boundaries avoids those copies.
- The required function returns None; inspect a after the call rather than printing the function's return value.

## Connections

- [C025 — Rotated-Array Search](C025_Search_in_a_Rotated_Sorted_Array.md): another invariant-based array problem in the same drill; its submitted code, correction and completed assessment are now filed.
- [C023 — Trapping Rain Water](C023_Trapping_Rain_Water_with_Two_Pointers.md): both require a correctness invariant and constant auxiliary space, but their safe-decision arguments differ.

## Assessment History

- [November 10 Q1, continued November 11](../../DailyTests/2026-11-10.md#q1--next-permutation): independent core algorithm, assisted complexity/duplicate and slice corrections, exact user-code validation, and separate assistant-reference validation.

## What to Remember

A nonincreasing suffix is already maximal. Increase the rightmost possible pivot by the smallest possible amount, then minimize the suffix. In Python, audit slices and concatenation as well as the helper bodies when claiming constant auxiliary space.
