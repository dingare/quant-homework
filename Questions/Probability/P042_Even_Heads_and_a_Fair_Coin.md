# P042 — Even Heads and a Fair Coin

## Metadata

- Category: Probability
- Tags: Independent Bernoulli Trials, Parity, Recursion, Product Expansion
- Date Added: 2026-11-10
- Status: Discussion summarized; the user proposed the recursion and the identical-probability signed expansion. The backward-induction completion and unequal-probability product were explained in the discussion.
- Source: User-provided question, outside the scheduled daily drill; no timed assessment recorded.

## Core Question

Suppose we have 10 coins, with head probabilities $`p_1,\ldots,p_{10}`$. If the probability of getting an even number of heads is $`1/2`$, what does this imply about the head probabilities?

**Assumption:** Each coin is tossed once, and all outcomes are mutually independent. The probabilities need not be equal. The argument relies on this independence assumption.

**Answer:** At least one coin has head probability $`1/2`$. In fact, this is both necessary and sufficient.

## Hint

Track the difference between the probabilities of an even and an odd number of heads. Adding a coin either preserves or flips parity.

## Solution

### 1. User's approach: recursion and backward induction

设前 $`n-1`$ 枚硬币出现偶数个正面的概率为 $`m`$，奇数个正面的概率为 $`1-m`$。最后一枚反面时保留奇偶性，正面时翻转奇偶性，因此：

```math
P(\text{even heads among }n)
=m(1-p_n)+(1-m)p_n.
```

若这个概率等于 $`1/2`$，则：

```math
m(1-p_n)+(1-m)p_n=\frac12
\quad\Longrightarrow\quad
(2m-1)(2p_n-1)=0.
```

所以，要么 $`p_n=1/2`$，要么 $`m=1/2`$。第二种情况表示前 $`n-1`$ 枚硬币也满足原条件，可以继续往前推。如果中途都没有遇到公平硬币，最终只剩第一枚，此时：

```math
P(\text{even heads among one coin})=1-p_1=\frac12.
```

仍然得到 $`p_1=1/2`$。因此至少有一个公平硬币。

### 2. Short proof: even probability minus odd probability

考虑乘积：

```math
\prod_{i=1}^{n}\big[(1-p_i)-p_i\big].
```

展开时，每个因子选择 $`1-p_i`$ 代表该枚硬币反面，选择 $`-p_i`$ 代表正面。独立性保证每项的绝对值就是对应完整结果的概率；正面个数决定符号：偶数个正面带正号，奇数个正面带负号。所以：

```math
\prod_{i=1}^{n}(1-2p_i)
=P(\text{even heads})-P(\text{odd heads}).
```

已知偶数概率为 $`1/2`$，奇数概率也为 $`1/2`$，故：

```math
\prod_{i=1}^{n}(1-2p_i)=0
\quad\Longrightarrow\quad
\exists i:\ p_i=\frac12.
```

反过来，只要其中一枚公平，乘积就是零，奇偶概率相等，因此二者均为 $`1/2`$。与两种概率之和为 1 联立，还得到通式：

```math
\boxed{
P(\text{even heads})
=\frac{1+\prod_{i=1}^{n}(1-2p_i)}{2}.
}
```

### 3. User's takeaway: equal probabilities are not required

用户已经想到相同正面概率时的表达式：

```math
\bigl(p-(1-p)\bigr)^n.
```

推广到不同的正面概率，只需把同一个因子的幂写成不同因子的乘积：

```math
\bigl(p-(1-p)\bigr)^n
\quad\longrightarrow\quad
\prod_{i=1}^{n}\bigl(p_i-(1-p_i)\bigr).
```

相同的概率允许用二项式系数合并同类项；不同的概率虽然不能这样合并，乘法展开和正负号规律仍然成立。

注意符号约定：这里正面取正、反面取负，所以第 $`k`$ 个正面计数对应的符号是 $`(-1)^{n-k}`$。本题 $`n=10`$ 为偶数，乘积仍是偶数概率减奇数概率；若希望通式对任意 $`n`$ 都保持这个方向，统一使用第二种解法中的 $`(1-p_i)-p_i`$。

## Key Knowledge Points

- 奇偶性只有两个状态；新硬币只会保留或翻转状态。
- 偶数概率减奇数概率可以压缩为一个乘积。
- 乘积结构要求独立性，不要求各枚硬币有相同的正面概率。
- 本题结论是至少一枚公平，不能推出每一枚都公平。

## Intuition

递推法每次去掉一枚硬币，乘积法则一次性展开所有硬币的奇偶贡献。两种方法表达的是同一个结构。

## Common Mistakes

- 停在“前面的偶数概率为一半，或者最后一枚公平”，没有补上往前归纳的过程。
- 将正面概率相同误当成乘积展开的必要条件。
- 漏写差值外的括号：应为 $`\bigl(p-(1-p)\bigr)^n`$，而非 $`p-(1-p)^n`$。
- 调换正反面的正负号后，忽略硬币总数对整体符号的影响。

## Connections

- [P031 — Exact Uniform Sampling from a Biased Coin](P031_Exact_Uniform_Sampling_from_a_Biased_Coin.md): 同样研究偏置硬币与公平结果；本题研究固定次数抛掷的奇偶性，P031 研究精确采样。
- [First-Hitting Parity, Coverage, and Alternating Ownership](../../KnowledgeCards/Probability/First_Hitting_Parity_Coverage_and_Alternating_Ownership.md): 都以奇偶性压缩状态；该卡讨论首次到达与停止时刻，本题是独立硬币的固定次数计数。

## Assessment History

2026-11-10 对话总结：用户独立提出正确的递推分解，并得到“前面的偶数概率为一半，或最后一枚公平”；助理补全反复归纳。用户表示已经想到相同概率下的有符号幂展开，尚未立即推广到不同概率；讨论中说明了乘积推广。不添加正式评分或独立掌握结论。

## What to Remember

**相同概率让同类项更容易合并；独立性才让每种结果的概率可以写成乘积。**

```math
P(\text{even})=\frac12
\quad\Longleftrightarrow\quad
\prod_{i=1}^{n}(1-2p_i)=0
\quad\Longleftrightarrow\quad
\text{at least one }p_i=\frac12.
```
