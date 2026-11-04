# P039 — Expected Wealth and Typical Multiplicative Growth

## Metadata

- Category: Probability
- Tags: Multiplicative Wealth, Expectation, Long-Run Behavior
- Date Added: 2026-11-01
- Original drill: November 1, 2026, Q4
- Status: Partial / Hinted, discussed November 3. Expected wealth and rare-path explanation independently correct; almost-sure growth needed a hint.

## Core Question

Start with wealth $`W_0=1`$. Each day, independently, a strategy multiplies its entire current wealth by:

- 1.5 with probability 1/2;
- 0.6 with probability 1/2.

There are no deposits, withdrawals, or costs.

1. Derive $`E[W_n]`$.
2. Determine what happens to $`W_n`$ as n tends to infinity along almost every realization. Support your conclusion mathematically.
3. A researcher argues, "Expected wealth grows, so an investor who runs the strategy long enough should eventually make money." Assess that claim and reconcile your answers.

Keep the interpretation to a few sentences. Original budget: 8 minutes; actual time Not recorded.

## Solution and Interpretation

Let $`M_i`$ be the independent daily multipliers. Since $`W_n=\prod_{i=1}^n M_i`$ and $`E[M_i]=(1.5+0.6)/2=1.05`$,

```math
E[W_n]=\prod_{i=1}^n E[M_i]=1.05^n.
```

If $`N_n`$ is the number of $`1.5`$ days, then $`W_n=1.5^{N_n}0.6^{n-N_n}`$. By the law of large numbers, $`N_n/n\to1/2`$ almost surely, so

```math
\frac{\log W_n}{n}
=\frac{N_n}{n}\log1.5+\left(1-\frac{N_n}{n}\right)\log0.6
\longrightarrow\frac12\log(1.5\cdot0.6)
=\frac12\log0.9\lt0.
```

Thus $`W_n\to0`$ almost surely. The scale $`0.9^{n/2}`$ describes the long-run logarithmic rate, not the exact wealth on every path. A small share of exceptionally large-wealth paths can lift $`E[W_n]`$ even as almost every individual path tends to zero. Large variance reflects this skew but is not the proof of almost-sure decay; the negative log-growth rate is.

## Assessment History

- [November 1 Q4, discussed November 3](../../DailyTests/2026-11-01.md#q4--multiplicative-wealth): $`1.05^n`$ independently correct. Initial infinity inference from growing mean was corrected after the assistant supplied the count/log representation; the user then gave $`0.9^{n/2}`$ and independently identified the rare-large-path explanation. Overall Partial / Hinted; “not stationary” was off-target terminology, not a separate gap. K/R unresolved, no I task, actual time Not recorded.
