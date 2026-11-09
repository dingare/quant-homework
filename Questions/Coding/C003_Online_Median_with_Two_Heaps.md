# C003 — Online Median with Two Heaps

## Metadata

- Category: Coding
- Secondary: Streaming Algorithms, Data Structures
- Difficulty: ★★★☆☆
- Tags: Median, Max Heap, Min Heap, Streaming, Lazy Deletion
- Review Priority: High
- Personal Note: Revisit the two-heap invariants and implement rolling-window lazy deletion without looking at notes.
- Date Added: 2026-08-13
- Status: Final

## Core Question

对数据流

```math
[4,1,7,-2,9,3,12,-5]
```

每读入一个数就输出当前中位数。要求插入 $`O(\log n)`$、查询 $`O(1)`$，并说明如何扩展为仅保留最近 $`k`$ 个观测的 rolling median。

## Solution

逐步排序可得 running medians：

```math
\boxed{[4,2.5,4,2.5,4,3.5,4,3.5]}.
```

维护两个堆：最大堆 $`L`$ 存较小的一半，最小堆 $`R`$ 存较大的一半，并保持

```math
\left||L|-|R|\right|\le1,
\qquad
\max(L)\le\min(R).
```

奇数个元素时，中位数为较大堆的根；偶数时为两个堆根的平均。

```python
import heapq


class OnlineMedian:
    def __init__(self) -> None:
        self.low = []   # store negatives: max-heap
        self.high = []  # min-heap

    def add(self, x: float) -> None:
        if not self.low or x <= -self.low[0]:
            heapq.heappush(self.low, -x)
        else:
            heapq.heappush(self.high, x)

        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low) + 1:
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        return -self.low[0] if len(self.low) > len(self.high) else self.high[0]
```

每次插入和再平衡至多做常数次 heap operation，因此为 $`O(\log n)`$；查询只读取堆根，为 $`O(1)`$。维护有序数组虽然查询快，但中间插入需要移动 $`O(n)`$ 个元素。

rolling median 的新增难点是删除过期值。普通 heap 不支持任意位置高效删除。常用做法是用哈希表记录待删除元素，在它到达堆顶时 lazy deletion；同时单独维护两个堆的有效大小。

## Rolling Median Implementation

The two heaps below store `(value, index)` entries and maintain the lower half with one extra live element when the window size is odd. `side` records only live indices and which heap owns them; absence means an expired entry. Prune expired roots before comparing or moving elements. `low_size` and `high_size` count live entries, independently of physical heap lengths. On expiration, remove the index from `side` and decrement its heap's live size; balancing then restores the size invariant.

Lazy deletion alone can retain O(n) buried entries. To keep auxiliary space O(k), rebuild both heaps from their live entries whenever their combined physical length exceeds `2*k`. Each rebuild costs O(k) and requires at least order k new insertions since the preceding rebuild, so its amortized overhead is constant per update.

```python
import heapq


def rolling_medians(values: list[int], k: int) -> list[float]:
    if not 1 <= k <= len(values):
        raise ValueError("Require 1 <= k <= len(values)")
    low, high = [], []
    side = {}  # live index -> 0 for low, 1 for high
    low_size = high_size = 0
    result = []

    def prune(heap):
        while heap and heap[0][1] not in side:
            heapq.heappop(heap)

    for i, value in enumerate(values):
        if i >= k:
            old_side = side.pop(i - k)
            if old_side == 0:
                low_size -= 1
            else:
                high_size -= 1
        prune(low)
        prune(high)

        boundary = -low[0][0] if low else (high[0][0] if high else value)
        if value <= boundary:
            heapq.heappush(low, (-value, i))
            side[i] = 0
            low_size += 1
        else:
            heapq.heappush(high, (value, i))
            side[i] = 1
            high_size += 1

        while low_size > high_size + 1:
            prune(low)
            negative, index = heapq.heappop(low)
            heapq.heappush(high, (-negative, index))
            side[index] = 1
            low_size -= 1
            high_size += 1
        while low_size < high_size:
            prune(high)
            number, index = heapq.heappop(high)
            heapq.heappush(low, (-number, index))
            side[index] = 0
            high_size -= 1
            low_size += 1
        prune(low)
        prune(high)

        if len(low) + len(high) > 2 * k:
            low = [entry for entry in low if side.get(entry[1]) == 0]
            high = [entry for entry in high if side.get(entry[1]) == 1]
            heapq.heapify(low)
            heapq.heapify(high)

        if i >= k - 1:
            if k % 2:
                result.append(float(-low[0][0]))
            else:
                result.append((-low[0][0] + high[0][0]) / 2)
    return result


stream = OnlineMedian()
observed = []
for value in [4, 1, 7, -2, 9, 3, 12, -5]:
    stream.add(value)
    observed.append(stream.median())
assert observed == [4, 2.5, 4, 2.5, 4, 3.5, 4, 3.5]
assert rolling_medians([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1, -1, -1, 3, 5, 6]
assert rolling_medians([2, 2, 2, 2], 2) == [2, 2, 2]
assert rolling_medians([-3, 4], 1) == [-3, 4]
assert rolling_medians([1, 4, 2, 3], 4) == [2.5]
```

Run after the online-median block. Online queries require at least one inserted value. Rolling time is amortized O(n log(k+1)); auxiliary space O(k), excluding the O(n-k+1) output. Inputs are unchanged. Index identities handle equal values without ambiguous expiration.

## Common Mistakes

- 只平衡堆大小，却不维护 $`\max(L)\le\min(R)`$。
- 用 heap 数组的物理长度代替 lazy deletion 后的有效长度。
- 忘记重复值要求删除计数而非布尔标记。

## What to Remember

```math
\boxed{\text{lower max-heap}+\text{upper min-heap}=\text{online median}.}
```

## Related questions and knowledge

- [C010 — Kth Largest: Heap and Quickselect](C010_Kth_Largest_Heap_and_Quickselect.md) — Heap size and ordering invariants.
- [C016 — Median of Two Sorted Arrays](C016_Median_of_Two_Sorted_Arrays.md) — Median selection from sorted data versus online median maintenance.
