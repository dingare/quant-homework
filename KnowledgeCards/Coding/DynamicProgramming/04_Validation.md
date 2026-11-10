# 验证记录 — Dynamic Programming

[复习包首页](README.md) · [解答](03_Solutions.md)

执行日期：2026-10-25。参考实现使用 Python 标准库，验证随机种子固定为 20261025，便于重现。

## 算法与文档一致性

在仓库根目录运行：

```bash
python3 KnowledgeCards/Coding/DynamicProgramming/verify.py
```

结果：**3,661 项检查全部通过**。其中数字分差与布尔胜负是分别核对的两项检查，不是两套不同输入。

| 分组 | 检查数 | 方法 |
| --- | --- | --- |
| 题例、边界与空输入扩展 | 30 | 显式期望值，覆盖练习页全部例子 |
| 输入不被修改 | 30 | 对比调用前后各参数 |
| House Robber | 60 | 小数组全部子集，排除相邻选择 |
| Partition | 60 | 全部子集判断是否恰好一半 |
| LIS | 60 | 全部子序列，直接判断严格递增 |
| Coin Change | 60 | 金额状态图 BFS 找最短路径 |
| Stock with Cooldown | 1,093 | 长度 0–6、价格取 0/1/2 的所有序列；逐日完整动作搜索，显式冷冻标记 |
| Winner 数值分差 | 1,093 | 同样的小数组，固定先手视角 minimax |
| Winner 布尔结果 | 1,093 | 与 minimax 分差是否非负比较 |
| Job Scheduling | 80 | 工作子集枚举，成对检查区间冲突 |
| 负收益工作扩展 | 1 | 全部不选可得 0 |
| 解答代码一致性 | 1 | 对比全部 8 个参考函数的语法树（七题含一个分差辅助函数） |

没有把同一 DP 递推简单改写成另一套 DP 后当作独立真值。小规模对照聚焦状态语义、冷冻期、分差符号、重复值和等号边界；正确性仍以解答中的论证为依据。

## 数学标记与站点

按仓库已有的固定版本依赖 `Tools/requirements-site.txt`，执行：

```bash
python3 Tools/check_math_markdown.py KnowledgeCards/Coding/DynamicProgramming README.md INDEX.md
python3 -m unittest discover -s Tools -p 'test_*.py'
python3 Tools/build_site.py
```

- 本次所有 Markdown 的数学标记检查通过。
- 仓库原有 17 项站点 / 数学渲染测试通过。
- 全站构建通过；本地页面与章节链接检查通过。
- 练习页与解答页独立；提示使用折叠区，公式放在正常 Markdown 数学区域；Python 参考代码完整保存在独立文件。

## 来源与范围

七题的官方题号、题名、当前难度及影响解法的条件，已核对 [首页题单](README.md) 中的 LeetCode 官方原题链接。题意、推导和例子按教学需要简要转述，未复制完整题面。

本轮没有新增作答记录或掌握评级。这里只验证参考实现和材料；它不代表已经完成用户的闭卷练习，也不是对任何具体面试题目的预测。
