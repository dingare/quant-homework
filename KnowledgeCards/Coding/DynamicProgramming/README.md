# Dynamic Programming — 经典逻辑题复习包

- Added: 2026-10-25
- Category: Coding / Knowledge Card
- Status: 学习参考与练习题单；尚未记录本轮作答或掌握程度。
- 目标：能用中文说清状态、决策、边界和正确性，再写出 Python。选题用于训练思考方式，不是任何具体公司的考题预测。

## 阅读顺序

1. [DP Revisit：从枚举到状态合并](01_DP_Revisit.md) — 先复习方法，再手推一个小例子。
2. [Practice：题目、例子、引导问题与分级提示](02_Practice.md) — 先停留在这一份，自行写状态与递推。
3. [Solutions：完整推导、证明、代码与追问](03_Solutions.md) — 每题尝试后，只看对应一节。

可运行代码：[reference.py](https://github.com/dingare/quant-homework/blob/main/KnowledgeCards/Coding/DynamicProgramming/reference.py)。验证脚本：[verify.py](https://github.com/dingare/quant-homework/blob/main/KnowledgeCards/Coding/DynamicProgramming/verify.py)。代码与解答在独立文件，练习页不展示完整答案。

## 题单与优先级

题号、英文题名和难度已于 2026-10-25 核对下列 LeetCode 官方页面。中文题意为简要转述，完整约束以链接为准。七道题覆盖六类状态设计；无需一晚全部完成。

| 编号 | 官方原题 | 难度 | 练习重点 | 顺序 / 优先级 |
| --- | --- | --- | --- | --- |
| Q1 | [198. House Robber](https://leetcode.com/problems/house-robber/) | Medium | 一维选择、前缀最优、滚动数组 | 今晚 1 / 必做 |
| Q2 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | Medium | 无限使用、恰好凑出、不可达状态 | 今晚 2 / 必做 |
| Q3 | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 0/1 背包、布尔状态、倒序更新 | 今晚 3 / 必做 |
| Q4 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | 以某点结尾与整个前缀的区别 | 次日 1 / 核心 |
| Q5 | [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | 日期、持仓、当天卖出、冷冻期 | 今晚 4 / 必做 |
| Q6 | [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | Medium | 区间、零和博弈、当前玩家分差 | 次日 2 / 核心 |
| Q7 | [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) | Hard | 排序、二分、带权区间选择 | 次日 3 / 选做 |

Q4 放到次日是为了给今晚的状态机留出推导时间。其二次 DP 是基础要求；二分优化只是进阶。Q7 的 Hard 是官方难度，核心仍是熟悉的“选 / 不选”，无需竞赛技巧。

## 今晚 105 分钟

| 时间段 | 内容 | 当段交付 |
| --- | --- | --- |
| 0–15 分钟 | DP Revisit | 不看笔记，解释“两个历史何时能合并” |
| 15–30 分钟 | Q1 House Robber | 状态一句话、递推、边界、滚动代码 |
| 30–50 分钟 | Q2 Coin Change | 解释无限使用、初始化和贪心反例 |
| 50–70 分钟 | Q3 Partition | 先二维再一维；手推正序复用错误 |
| 70–95 分钟 | Q5 Stock with Cooldown | 画三状态转移，逐日检查冷冻期 |
| 95–105 分钟 | 闭卷复述 | 重写 Q3 的循环与 Q5 的状态定义 |

只有 90 分钟时：Revisit 10、Q1 12、Q2 18、Q3 18、Q5 22、复述 10。若有 120 分钟，额外 15 分钟用于修正今晚一题或闭卷重写；不强行添加 Hard。卡住 5–7 分钟时看一层提示，然后重新尝试；到时间仍未完成，就记录卡点，读相应解答后合上重写。

次日约 70–85 分钟：Q4 20、Q6 25、Q7 25–40（选做）。面试前再用 20–30 分钟，随机抽 Q2 / Q3 与 Q5 / Q6 各一题，先口述状态与边界，再写代码；有余力复习已存在的 [C012 — Edit Distance](../../../Questions/Coding/C012_Edit_Distance.md)，不增加本轮必做题数。

## 每题完成标准

- 用完整中文定义一个表格单元，说明索引代表“前多少个”“以谁结尾”“哪一天结束”或“谁的视角”。
- 枚举合法决策，写出边界、不可能状态、计算顺序和答案位置。
- 用一个微型输入手推，并用归纳 / 最优子结构说明为什么不会漏掉最优解。
- 说出时间、辅助空间及一次常见误写；然后写代码。

## 运行与验证

在仓库根目录使用 Python 3.10+，无第三方依赖：

```bash
python3 KnowledgeCards/Coding/DynamicProgramming/verify.py
```

脚本检查七题的例子与边界，并用小规模完整枚举 / 独立搜索对照参考实现。股票对照逐日合法动作搜索，博弈对照固定玩家视角 minimax，避免仅把同一递推重写一遍。解答中的代码块由参考文件对应函数生成，并核对一致性。验证范围和结果见解答末尾。

## 与现有材料的连接

- [C020 — Minimum Deletions / LIS](../../../Questions/Coding/C020_Minimum_Deletions_for_a_Strictly_Increasing_Subsequence.md)：本轮先复习二次 DP，再连接到已有 tails 不变量。
- [C014 — Maximum-Profit Compatible Jobs](../../../Questions/Coding/C014_Maximum_Profit_Compatible_Jobs.md)：Q7 的已有变体，允许负收益和更大输入；本轮代码允许不选任何工作。
- [P026 — Finite-Horizon Optimal Stopping](../../../Questions/Probability/P026_Finite_Horizon_Optimal_Stopping.md)：同样先定义未来价值与充分状态，再做倒推。

本目录作为复习卡保存，不新增 C 编号，不改变题库计数、历史评分或完成记录。
