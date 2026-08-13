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

$$
[4,1,7,-2,9,3,12,-5]
$$

每读入一个数就输出当前中位数。要求插入 $O(\log n)$、查询 $O(1)$，并说明如何扩展为仅保留最近 $k$ 个观测的 rolling median。

## Solution

逐步排序可得 running medians：

$$
\boxed{[4,2.5,4,2.5,4,3.5,4,3.5]}.
$$

维护两个堆：最大堆 $L$ 存较小的一半，最小堆 $R$ 存较大的一半，并保持

$$
\left||L|-|R|\right|\le1,
\qquad
\max(L)\le\min(R).
$$

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

每次插入和再平衡至多做常数次 heap operation，因此为 $O(\log n)$；查询只读取堆根，为 $O(1)$。维护有序数组虽然查询快，但中间插入需要移动 $O(n)$ 个元素。

rolling median 的新增难点是删除过期值。普通 heap 不支持任意位置高效删除。常用做法是用哈希表记录待删除元素，在它到达堆顶时 lazy deletion；同时单独维护两个堆的有效大小。

## Common Mistakes

- 只平衡堆大小，却不维护 $\max(L)\le\min(R)$。
- 用 heap 数组的物理长度代替 lazy deletion 后的有效长度。
- 忘记重复值要求删除计数而非布尔标记。

## What to Remember

$$
\boxed{\text{lower max-heap}+\text{upper min-heap}=\text{online median}.}
$$
