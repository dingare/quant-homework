# Solutions — 推导、证明与 Python 参考实现

[复习包首页](README.md) · [返回练习页](02_Practice.md)

建议每次只读对应题的一节。这里的实现用于算法面试：输入符合原题条件，Python 3.10+，标准库即可；所有数组均不修改输入。空数组是额外友好约定，原题多数不提供空输入。

## Q1 — House Robber

[198 — Medium / 官方原题](https://leetcode.com/problems/house-robber/)

### 状态为什么足够

**D(k)：只使用前 k 个位置，能够选出的不相邻元素的最大总和。** k 表示数量，最后一个位置下标为 k−1。D(k) 的结果可以包含也可以不包含最后一个位置。

无需记录选过哪些位置：按最后一个位置分类后，剩余部分是一个完整的较短前缀，其所有合法选择已经由对应状态优化过。若改成从左向右逐步扩展并只存“已经赚了多少钱”，就还需记录上一位置是否被选；不能把这个限制直接丢掉。

### 决策、正确性与边界

```math
D(0)=0,\qquad D(1)=a_0,
\qquad D(k)=\max\{D(k-1),\ D(k-2)+a_{k-1}\}\quad(k\ge2).
```

不选最后一个，落在前 k−1 个；选它，前一个不能选，落在前 k−2 个。两类按是否选最后一个互斥且覆盖所有合法解。若某类用了非最优的较短前缀解，用最优前缀替换仍合法且不差，因此各类最优值正是上式的两个候选。边界正确，归纳得所有 D(k) 正确。

先按 k 递增填表；答案在 D(n)。原题非负，单元素答案是它本身。滚动实现从空前缀开始，每轮更新前 `prev1` 是前一前缀的答案；从第二轮起 `prev2` 是再短一个前缀的答案。第一轮两个零边界也给出正确结果。空数组返回 0，没有不可达状态。

### Python

```python
def house_robber(nums: list[int]) -> int:
    """LC 198: nonnegative values, adjacent positions cannot both be chosen."""
    prev2 = prev1 = 0
    for value in nums:
        current = max(prev1, prev2 + value)
        prev2, prev1 = prev1, current
    return prev1
```

时间 $`O(n)`$，辅助空间 $`O(1)`$；若重建选了哪些位置，用完整 D 表回溯或另存决策，空间为 $`O(n)`$。

**常见错误：** 每步只挑局部最大；选择当前元素时加到 D(k−1)；先覆盖旧变量又拿新值计算。`[4,5,4]` 的正确答案为 8。

**面试 follow-up：** 若首尾也相邻（House Robber II），n=1 单独处理，其余取“去掉首位置”与“去掉尾位置”两次线性问题的最大值；每个合法解至少落入一类。若允许负数且可一个也不选，单元素边界改为与 0 取最大。

## Q2 — Coin Change

[322 — Medium / 官方原题](https://leetcode.com/problems/coin-change/)

### 状态为什么足够

**D(a)：恰好凑出金额 a 的最少硬币枚数。** 每种面额无限供应，已用的硬币不改变剩余可选集合，因此只记录剩余 / 目标金额即可。若供应有限，金额一维状态本身就不够描述还可以使用哪些硬币。

### 决策、正确性与边界

按最后一枚面额 c 分类：

```math
D(0)=0,\qquad
D(a)=\min_{c\in\mathrm{coins},\ c\le a}\{D(a-c)+1\}.
```

无合法可达候选时为正无穷。任意可行方案都有最后一枚，移除后是金额 a−c 的可行方案；替换为该金额最少枚数方案不会变差。反过来，每个可达子解加一枚 c 都合法。两方向说明递推既不会遗漏最优解，也不会生成不合法答案。

同一组硬币可能由不同顺序被多次考虑，但我们取 min，重复候选不改变最优值。若改成“方案数”，必须先澄清是否区分顺序；不能直接把 min 换成加法。

所有 c 为正，因此 a−c 小于 a，金额从 1 到 amount 递增。答案为 D(amount)；不可达返回 −1。有限哨兵 `amount+1` 足够，因为任意可行方案至多使用 amount 枚正整数硬币；每次 min 不会把哨兵抬高。

### Python

```python
def coin_change(coins: list[int], amount: int) -> int:
    """LC 322: positive denominations, unlimited use, nonnegative amount."""
    impossible = amount + 1
    dp = [0] + [impossible] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    return -1 if dp[amount] == impossible else dp[amount]
```

设面额数为 m，目标金额为 A，时间 $`O(mA)`$，辅助空间 $`O(A)`$。它依赖金额数值，是伪多项式算法；本题 A 最大 10,000，适用。金额 0 返回 0，即使没有使用硬币。

**常见错误：** 正金额初始化为 0；假定最大面额优先一定最优；把硬币当成只能用一次。`[1,3,4]` 凑 6：贪心 4+1+1 要 3 枚，最优 3+3 要 2 枚。

**面试 follow-up：** 要返回一种方案，在每次严格改善时记录最后硬币，再从 A 减回 0。若改成每种面额至多用一次，需要引入处理到哪个物品的层次；若用一维压缩，每个物品对应的金额循环倒序。

## Q3 — Partition Equal Subset Sum

[416 — Medium / 官方原题](https://leetcode.com/problems/partition-equal-subset-sum/)

### 先改写，再定义足够的状态

总和 S 为奇数时不可能相等。S 为偶数时，设 T=S/2，只需选出和恰好为 T 的子集；没选的其余元素和自动也是 T。

**B(i,s)：只使用前 i 个元素，每个位置至多一次，能否恰好凑出 s。** 物品前缀决定还未使用的物品集合，s 决定目标，因此这两个索引足够。相同值的两个位置是两个不同物品。

### 二维递推与正确性

```math
B(0,0)=\mathrm{True},\qquad B(0,s)=\mathrm{False}\quad(s\gt0),
```

```math
B(i,s)=B(i-1,s)\ \lor\
\bigl(s\ge x_i\ \land\ B(i-1,s-x_i)\bigr).
```

这里物品用 1 到 n 编号，$`x_i`$ 对应 Python 的 `nums[i-1]`。不选当前物品与选当前物品两类覆盖全部子集，且都读上一行，保证当前物品只用一次。选与不选的具体子集互斥，但它们可能都能证明同一金额可达；布尔 or 允许这种重叠，不是在计数。

二维按 i 递增，s 在每一行可任意顺序；答案 B(n,T)。没有物品只能凑出 0。全部数值为正，超过 T 的金额永远不需要访问。空数组额外约定可以划成两个空子集，返回 True。

### 压成一维，为什么必须倒序

`possible[s]` 在处理一件物品前代表上一行，在处理完后代表新一行。处理当前值 x 时，需要读取旧的 `possible[s-x]`。

因为 x 为正，s−x 小于 s。从大到小更新时，更小的位置尚未被本轮写过，仍是上一行，所以安全。从小到大则会读到已经使用过 x 的本轮结果，等于允许重复使用这一件物品。

反例：`[1,2,5]` 的 S=8，T=4。只处理第一个 1，正序从 1 开始会依次把 1、2、3、4 标为 True，相当于凭空用了四个 1；正确答案应为 False。倒序时，仅能把 1 标为 True。

这与 Coin Change 的无限供应形成直接对照：要重复使用当前面额，可以读本层已经更新的小金额；只能使用一次时，必须保留上一层的数据。循环方向来自状态层次与读写依赖。

### Python

```python
def can_partition(nums: list[int]) -> bool:
    """LC 416: positive integers; each array position is usable once."""
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    possible = [False] * (target + 1)
    possible[0] = True
    for value in nums:
        for subtotal in range(target, value - 1, -1):
            possible[subtotal] = (
                possible[subtotal] or possible[subtotal - value]
            )
    return possible[target]
```

时间 $`O(nT)`$，辅助空间 $`O(T)`$，同样是按数值规模衡量的伪多项式算法。原题 T 不超过 10,000。总和计算需 $`O(n)`$；奇数情况可直接返回。

**常见错误：** 只检查总和是否为偶数；忘记空和 True；金额正序；把重复数值去重（会改变物品数量）。

**面试 follow-up：** 如果允许负数，容量区间与倒序论证都需重做，可用可达和集合并从旧集合生成新集合。要重建子集，保留二维表或妥善保存每一层前驱，不能随意引用会被后续覆盖的一维前驱。

## Q4 — Longest Increasing Subsequence

[300 — Medium / 官方原题](https://leetcode.com/problems/longest-increasing-subsequence/)

### 状态为什么足够

**L(i)：必须以位置 i 结尾的最长严格递增子序列长度。** i 固定了末尾值；在相同末尾下，更短的候选对未来延长不会优于更长的候选，因此保留最大长度即可。

仅存“前 i 个数的最长长度”然后尝试直接接新值，会丢失末尾信息。例如前缀 `[3,4,1]` 最长长度为 2，其末尾是 4，新值 2 接不上它，却能接在较短子序列 `[1]` 后面。

### 递推、正确性与顺序

```math
L(i)=1+\max\left(\{L(j):j\lt i,\ a_j\lt a_i\}\cup\{0\}\right).
```

以 i 结尾的解要么只有它自身，要么有唯一倒数第二个位置 j，且 j 在前、值更小。移除最后位置后是以 j 结尾的解，替换成最优者仍可接 i；反过来，每个候选都能接 i 构成合法子序列。这覆盖所有解，max 保留最优长度。

所有 L(i) 初始为 1，i 从左到右、j 扫描 i 之前的所有位置。答案是所有 L(i) 的最大值，而非最后一个 L(i)。`[1,2,3,0]` 的 L 为 `[1,2,3,1]`，答案为 3。没有可用前驱是合法单元素状态，不是不可达。

### Python：先掌握二次 DP

```python
def lis_length(nums: list[int]) -> int:
    """LC 300: quadratic DP for the strictly increasing subsequence length."""
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

时间 $`O(n^2)`$，辅助空间 $`O(n)`$。空数组返回 0。用 `<` 保证严格递增，不能改成 `<=`。

### 进阶：tails 的压缩思想

对已处理前缀，保存“每个长度能达到的最小末尾值”。同长度末尾更小的序列，对所有未来延续都至少同样好，因此支配末尾更大的序列。tails 按长度严格递增，用 `bisect_left` 找首个不小于新值的位置替换，或在末尾追加。

时间降到 $`O(n\log n)`$，空间 $`O(n)`$。tails 的各格可能来自不同子序列，本身未必是一个真实子序列；`[2,3,1]` 的最终 tails 为 `[1,3]`。严格递增用 left；允许不下降时才用 right。完整不变量解释可复习 [C020 — LIS / Minimum Deletions](../../../Questions/Coding/C020_Minimum_Deletions_for_a_Strictly_Increasing_Subsequence.md)。

**常见错误：** 把子序列当连续子数组；答案直接返回 L(n−1)；相等也延长；未解释 tails 的含义就套二分。

**面试 follow-up：** 二次 DP 在更新时记录前驱，最后从最大 L(i) 所在位置回溯一条 LIS。若问最少删除使严格递增，答案为 n−LIS 长度，因为保留下来的元素必然构成递增子序列。

## Q5 — Best Time to Buy and Sell Stock with Cooldown

[309 — Medium / 官方原题](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

### 先固定日终语义

每个值都是截至**第 d 天结束后**的最大净现金流，买入扣现金、卖出加现金。已持有的股票不额外按当天价格计入价值。

| 状态 | 中文定义 | 第 d+1 天能否买 |
| --- | --- | --- |
| H(d) / hold | 第 d 天日终持有一股 | 不能再买，必须先卖 |
| S(d) / sold | 第 d 天刚卖出，日终空仓 | 不能，次日冷冻 |
| R(d) / rest | 第 d 天日终空仓，而且当天没卖出 | 能；冷冻日若在今天已度过，明天可买 |

**为什么足够：** 合法未来动作只取决于日期、是否持仓、是否当天刚卖出。历史买价已进入净现金流，较差现金流的同状态历史在任何未来交易序列下都不能反超，因此无需把买价再作为状态维度。单纯“空仓”会合并 S 与 R，丢失能否次日买入的信息。

### 逐日转移与边界

```math
H(d)=\max\{H(d-1),\ R(d-1)-p_d\},
```

```math
S(d)=H(d-1)+p_d,\qquad
R(d)=\max\{R(d-1),\ S(d-1)\}.
```

在第 0 天之前初始化 H(−1)=S(−1)=负无穷，R(−1)=0。还没开始时只有不交易的空仓合法；H 不能初始化为 0，否则等于免费获得一股。

H 来自继续持仓或从昨日 R 买入；S 只来自昨日 H 卖出；R 来自继续休息或昨日刚卖后今天完成冷冻。所有合法日终情况都落在这三类且不会漏掉动作，各个转移都遵守冷冻限制。若有一条同状态路径净现金更优，用它替换不会改变未来动作集合，所以取 max 正确；对日期归纳即可证明。

关键时间线：第 d 天卖出进入 S(d)，第 d+1 天只能到 R(d+1)，最早第 d+2 天才能从 R(d+1) 买入。代码必须同时用昨日三个旧值计算今日新值。若先更新 R，再用新 R 算 H，就可能让昨日卖出的路径在今天买入。

最后答案为 `max(R(n-1), S(n-1))`，排除持仓，因为题目要完成交易后的利润。空数组时，初始化直接给出 0。

### 手推 `[1,2,3,0,2]`

| d | 价格 | H：持仓 | S：今天卖 | R：空仓且今天没卖 |
| --- | --- | --- | --- | --- |
| −1 | — | −∞ | −∞ | 0 |
| 0 | 1 | −1 | −∞ | 0 |
| 1 | 2 | −1 | 1 | 0 |
| 2 | 3 | −1 | 2 | 1 |
| 3 | 0 | 1 | −1 | 2 |
| 4 | 2 | 1 | 3 | 2 |

表中不同状态各自代表不同的最优历史，不必属于同一条交易路径。H(3)=1 来自第 1 天卖出赚 1、第 2 天冷冻、第 3 天以 0 买入；不来自第 2 天卖出后的历史。最优完整路径是买、卖、冷冻、买、卖，利润 3。

### Python

```python
def stock_cooldown(prices: list[int]) -> int:
    """LC 309: day-end hold / sold-today / rest, one-day cooldown."""
    hold = sold = float("-inf")
    rest = 0
    for price in prices:
        next_hold = max(hold, rest - price)
        next_sold = hold + price
        next_rest = max(rest, sold)
        hold, sold, rest = next_hold, next_sold, next_rest
    return int(max(rest, sold))
```

时间 $`O(n)`$，辅助空间 $`O(1)`$。常数空间依赖只读取昨日状态。单日价格返回 0；价格下降也返回 0。

**常见错误：** 用统一空仓状态直接买入；把 S 当作“历史上卖过”；在同一轮覆盖旧变量；最后把 H 也放入答案候选。`[1,2,0,3]` 正确为 3，忽略冷冻会错误得到 4。

**面试 follow-up：** 另一种后缀递归可用“日期、是否持仓”，因为卖出时直接跳到 d+2，显式跳过冷冻日；仍逐日只前进一天时，仅两种持仓状态就不够。冷冻 k 天可用带延迟的空仓价值或增加冷冻剩余天数。交易费应在买或卖的一处扣一次；恢复交易路径需保留逐日来源。

## Q6 — Predict the Winner

[486 — Medium / 官方原题](https://leetcode.com/problems/predict-the-winner/)

### 分差的定义必须随当前玩家换手

**G(l,r)：只剩闭区间 [l,r]，轮到当前玩家时，在双方最优决策下，他能保证的“自己未来得分 − 对方未来得分”。** 当前玩家可以是先手，也可以是后手；G 不永远站在最初先手的视角。

状态为什么足够：剩余合法动作只由两端决定，过去分数已经固定；所有数最终都被取走，当前区间总和固定，最大化自己的未来得分与最大化未来分差等价。无需再携带双方历史分数，也不必加一个玩家身份维度。

### 递推与减号的来源

```math
G(l,r)=\max\{a_l-G(l+1,r),\ a_r-G(l,r-1)\}.
```

取左端得到即时得分 $`a_l`$，接着轮到对手，对手在剩余区间能保证的分差是 G(l+1,r)。那是“对手减自己”，所以对自己是负贡献。右端同理。每端选择后，对手会选对自己最有利的续局；不能假设对手随便拿，也不能把子区间分差直接相加。

两种第一步覆盖所有合法策略；由较短区间的最优对抗值，分别得到当前两个动作能保证的精确分差，取 max 就是当前玩家最佳保证值。这是长度归纳 / minimax 的零和改写。

边界：单元素 G(i,i)=a_i；空区间的概念值为 0。代码对非空区间先设对角线，不实际访问空区间。G 可以为负，不可把每格用 0 与候选取 max。完整答案是 G(0,n−1) 是否大于等于 0，包含平局。

### 顺序与小例子

按区间长度递增即可。下面用 l 从右向左、r 从 l+1 向右：G(l+1,r) 已在较下面一行完成，G(l,r−1) 已在当前行左侧完成。

`[1,5,2]` 中，G(0,1)=4，G(1,2)=3，所以 G(0,2)=max(1−3,2−4)=−2，先手失败。G(1,2)=3 是轮到该区间玩家的优势，并不承诺它永远属于先手。

### Python

```python
def winner_score_difference(nums: list[int]) -> int:
    """LC 486 helper: optimal current-player minus other-player score."""
    n = len(nums)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for left in range(n - 1, -1, -1):
        dp[left][left] = nums[left]
        for right in range(left + 1, n):
            dp[left][right] = max(
                nums[left] - dp[left + 1][right],
                nums[right] - dp[left][right - 1],
            )
    return dp[0][n - 1]


def predict_the_winner(nums: list[int]) -> bool:
    """LC 486: both play optimally; a tie counts as a first-player win."""
    return winner_score_difference(nums) >= 0
```

时间 $`O(n^2)`$，辅助空间 $`O(n^2)`$。布尔结果之外保留分差函数，是为了验证符号和视角；仅测试胜负会漏掉部分错误。空数组额外约定平局，返回 True。

**常见错误：** 子区间前写加号；始终把 G 解释为先手分差；只取较大端点；将最终判断写成严格大于 0。

**面试 follow-up：** 一维压缩可以做到 $`O(n)`$ 空间：l 递减、r 递增，更新前 dp[r] 是 G(l+1,r)，更新后左邻 dp[r−1] 是 G(l,r−1)。若要报告先手分数，设总和为 S、最优分差为 g，则先手得分为 (S+g)/2。若改变为非零和收益，分差压缩需要重新论证。

## Q7 — Maximum Profit in Job Scheduling（选做 Hard）

[1235 — Hard / 官方原题](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

### 先用排序建立前缀结构

把工作按结束时间非递减排序，区间用左闭右开理解，结束等于开始合法。**D(k)：只从排序后前 k 个工作中选择互不重叠工作的最大总收益。**

对于第 k 个工作，所有结束不晚于其开始时间的前序工作恰好构成一个前缀。它们未来能否与当前工作衔接，由结束时间保证；不需要再记录选过的完整时间表。因此选当前工作后，兼容前缀的最优值就是足够摘要。

### 决策与正确性

设第 k 个工作的开始、结束、收益为 $`s_k,e_k,p_k`$；$`j_k`$ 为它之前结束时间不大于 $`s_k`$ 的工作数量：

```math
D(0)=0,\qquad
D(k)=\max\{D(k-1),\ p_k+D(j_k)\}.
```

不选当前工作，答案是前 k−1 个的最优值；选它，则所选其他工作全部来自兼容前缀。替换成该前缀的最优日程不会冲突，收益不差。两类覆盖且按是否选当前工作互斥，两个候选也都可实现，所以递推正确。按 k 递增，答案 D(n)。所有前缀都允许选空集合，没有不可达状态。

### 二分到底返回什么

Python 循环中 i 是当前工作的 0-based 下标，已经处理了 i 个工作。`bisect_right(ends, start, 0, i)` 在半开范围 `[0,i)` 搜索，返回结束时间不大于 start 的工作**数量**。这个数量可以直接作为 dp 下标。

`bisect_left` 会排除结束恰等于开始的工作，从而丢掉合法衔接。搜索上界明确设为 i，保证不引用未计算的未来状态。原题开始严格小于结束，相同结束时间的工作不能互相衔接，不影响这个论证。

例如 `(1,3,5),(2,4,6),(3,5,5)`，排序后 D 为 `[0,5,6,10]`；第三个工作兼容前序工作数为 1，所以取 `max(6,5+D(1))=10`。

### Python

```python
from bisect import bisect_right


def job_scheduling(
    start_time: list[int], end_time: list[int], profit: list[int]
) -> int:
    """LC 1235: start < end; touching endpoints are compatible."""
    jobs = sorted(zip(start_time, end_time, profit), key=lambda job: job[1])
    ends = [end for _, end, _ in jobs]
    dp = [0] * (len(jobs) + 1)
    for i, (start, _, reward) in enumerate(jobs):
        compatible_count = bisect_right(ends, start, 0, i)
        dp[i + 1] = max(dp[i], dp[compatible_count] + reward)
    return dp[-1]
```

文件开头需要 `from bisect import bisect_right`。排序耗时 $`O(n\log n)`$，n 次二分合计 $`O(n\log n)`$，辅助空间 $`O(n)`$，包括排序后的工作、ends、dp。无需按巨大时间范围建表，也无需深递归。

**常见错误：** 先选收益最高的工作；按开始排序却套结束排序的前缀递推；二分漏掉等号；把兼容数量减一后直接作为 dp 下标。

**面试 follow-up：** 记录每一步选 / 不选并跳到兼容前缀，可重建日程。若允许负收益且允许不选，本实现仍正确，最差为 0；若要求至少一个工作，边界和答案条件需要调整。若至多选 K 个工作，增加数量维度。参见已有 [C014 变体](../../../Questions/Coding/C014_Maximum_Profit_Compatible_Jobs.md)。

## 横向复述：七题不是七条孤立公式

| 题 | 被合并的历史具有怎样相同的未来？ | 聚合操作 | 关键计算顺序 |
| --- | --- | --- | --- |
| House Robber | 同一允许前缀，最后位置分类后留下相同较短问题 | max | 前缀递增 |
| Coin Change | 同一金额、同一无限面额集合 | min | 金额递增 |
| Partition | 同一物品前缀、同一目标和 | or | 物品递增，一维金额倒序 |
| LIS | 同一结尾位置；保留最长者 | max | 结尾递增 |
| Stock | 同日同持仓 / 卖出 / 休息，保留最大净现金 | max | 日递增，全部读取昨日值 |
| Winner | 同一剩余区间，统一当前玩家视角 | max + 视角变号 | 短区间先算 |
| Jobs | 同一结束排序前缀；选当前后回到兼容前缀 | max | 排序前缀递增 |

面试口述可用：“我先定义这个状态表示什么。当前所有合法动作是……每个动作的剩余问题正好是……这个信息足够，因为同状态的不同历史拥有相同的未来选择。边界是……依赖顺序是……答案在……按状态规模归纳，候选覆盖所有解且都能实现，所以取最优正确。”

## 验证范围

参考实现和验证脚本独立保存，运行入口见 [首页](README.md)。验证包括：

- 七题的小例子、空输入扩展、严格递增重复值、金额不可达、子集正序反例、冷冻期和平局、工作端点相等与输入乱序。
- House Robber / Partition / LIS 用小数组子集枚举对照；Coin Change 用金额图的 BFS；Jobs 用所有子集的区间冲突检查。
- Stock 对短价格序列完整枚举逐日合法交易动作，显式携带冷冻标记；未平仓的终局无效。
- Winner 用固定先手视角的 minimax，先手取 max、后手取 min，并与最优**数值分差**比较。
- 检查参考实现不修改输入；检查本页代码块与对应函数一致；执行仓库的 Markdown 数学检查与网页构建检查。

这些小规模对照主要检查边界和转移语义，不代替上面的正确性证明，也不证明大输入的性能。具体执行结果记录在 [验证记录](04_Validation.md)。
