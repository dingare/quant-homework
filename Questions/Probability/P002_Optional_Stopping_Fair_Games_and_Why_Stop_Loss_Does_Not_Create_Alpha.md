# P002 — Optional Stopping, Fair Games, and Why Stop-Loss Does Not Create Alpha

## Metadata

- Category: Probability
- Secondary: Stochastic Processes, Trading Intuition, Risk Management
- Difficulty: ★★★★☆
- Tags: Martingale, Optional Stopping, Hitting Probability, Stop-Loss, Fair Game
- Review Priority: High
- Date Added: 2026-07-05
- Status: Draft
- Personal Note: Emphasize the conditions of optional stopping. Under those conditions, stopping rules reshape the payoff distribution without changing the martingale's expected value. The Q53 variants below show why almost-sure termination alone is insufficient.

## Core Question

Suppose $`X_t`$ is a martingale with $`X_0=0`$, and define the stopping time

```math
\tau=\inf\{t: X_t\in\{a,-b\}\}
```

for $`a,b\gt 0`$.

Show that

```math
P(X_\tau=a)=\frac{b}{a+b}
```

and explain why changing stopping rules cannot generate alpha in a fair game.

## Why This Topic Matters

This is one of the cleanest ways to separate:

- alpha generation,
- risk management,
- path management.

Many trading rules look appealing because they improve win rate or truncate losses. When its hypotheses hold, optional stopping clarifies that changing the exit rule alone does not manufacture positive expectancy from a martingale. Unbounded waiting rules require a separate check, as the Q53 variants below illustrate.

## My Current Understanding

A martingale is a fair game in conditional expectation:

```math
E[X_t\mid\mathcal F_s]=X_s.
```

So the stopping rule can change:

- how often I win,
- how large wins are,
- how large losses are,
- how long the trade lasts,

but not the expected value, provided the stopping argument is valid.

## Hitting Probability Calculation

At the stopping time, the process ends at either $`a`$ or $`-b`$, so

```math
X_\tau\in\{a,-b\}.
```

Let

```math
p=P(X_\tau=a).
```

Then

```math
P(X_\tau=-b)=1-p.
```

If optional stopping applies, then

```math
E[X_\tau]=E[X_0]=0.
```

Therefore

```math
ap+(-b)(1-p)=0.
```

Solve:

```math
ap-b+bp=0
\quad\Longrightarrow\quad
p(a+b)=b
\quad\Longrightarrow\quad
\boxed{P(X_\tau=a)=\frac{b}{a+b}}.
```

Similarly,

```math
\boxed{P(X_\tau=-b)=\frac{a}{a+b}}.
```

## Intuition

The winning probability is higher when the loss barrier is farther away.

That sounds favorable, but the gain size and loss size adjust against each other. A closer profit target raises hit rate only because the upside is smaller. The expectation stays pinned at zero.

## Why Stop-Loss Does Not Create Alpha

Suppose a strategy exits at:

- a small gain very often,
- a large loss occasionally.

This can create an impressive win rate without creating positive expected value. What matters is:

```math
E[\text{PnL}]=
\sum \text{probability}\times \text{payoff}.
```

When optional-stopping conditions hold, exit engineering in a fair game changes the shape of outcomes, not the mean.

## Common Mistakes

- Confusing high win rate with positive expectancy.
- Thinking smaller losses automatically imply positive edge.
- Forgetting that optional stopping needs conditions; it is not a free pass for every unbounded stopping rule.
- Mistaking risk control for signal generation.

## Interview Follow-Ups

- What conditions are needed for the Optional Stopping Theorem?
- How does the conclusion change if the process has drift?
- How do stop-loss and take-profit rules affect skewness and drawdowns even if they do not create alpha?
- Why can a backtest look better after changing exits without the underlying signal improving?

## Market / Rates Application

In practice, stop-loss rules still matter. They can improve:

- tail control,
- capital usage,
- liquidity management,
- drawdown behavior.

But those are risk-management benefits, not proof of alpha. This distinction matters a lot in discretionary macro and systematic rates trading.

## What to Remember

Stopping Rule $`\neq`$ Alpha.

If the underlying process is a martingale and the stopping rule satisfies the required conditions, clever exits can change distribution, hit rate, and path behavior, but not expected profit. Almost-sure termination alone does not guarantee this equality.

Related review path: [首次命中、奇偶增强、覆盖与轮流归属框架](../../KnowledgeCards/Probability/First_Hitting_Parity_Coverage_and_Alternating_Ownership.md).

## Citadel Q53 and One-Sided Exit Variants — 2026-11-12

Source: user-supplied Citadel interview-preparation PDF, page 4, Q53, and the subsequent discussion. This section records assistant-explained solutions and the user's proposed variants; no timed result or independent mastery is inferred.

### 1. Original game: a forced exit at a loss of three

Flip a fair coin. Each head adds +1 and each tail adds -1 to cumulative P&L. You may stop at any time, but reaching -3 forces the game to end with payoff -3. Find an optimal stopping rule and the value function.

Let $`S_n`$ be the cumulative P&L, starting at an integer $`s\ge-3`$, and let $`H_{-3}`$ be its first hitting time of -3. An admissible stopping time satisfies $`\tau\le H_{-3}`$. The simple symmetric random walk reaches -3 almost surely, so these stopping times are almost surely finite, though their expectations need not be finite.

The optimal value is

```math
\boxed{V(s)=s,\qquad s\ge-3}.
```

Immediate stopping attains this value. In particular, $`V(0)=0`$. If an initial toss is compulsory, tossing once and then stopping still has expectation zero from the initial state.

To prove that no strategy does better, observe that the stopped wealth plus three is a nonnegative martingale. For every fixed integer $`n`$,

```math
E_s[S_{\tau\wedge n}+3]=s+3.
```

Fatou's lemma gives

```math
E_s[S_\tau+3]
\le\liminf_{n\to\infty}E_s[S_{\tau\wedge n}+3]
=s+3,
```

so $`E_s[S_\tau]\le s`$. Immediate stopping achieves equality. The one-step Bellman equation is consistent with this value, but its equality alone is not a substitute for the upper-bound argument:

```math
V(s)=\max\left\{s,\frac{V(s+1)+V(s-1)}2\right\},\qquad s\gt-3,
\qquad V(-3)=-3.
```

The optimal strategy is not unique. Starting at zero, choose any positive integer profit target $`b`$ and stop upon hitting either $`b`$ or -3. Gambler's ruin gives

```math
P_0(H_b\lt H_{-3})=\frac3{b+3},\qquad
E_0[S_{H_b\wedge H_{-3}}]
=b\frac3{b+3}-3\frac b{b+3}=0.
```

For example, targeting +1 wins one unit with probability three quarters and loses three units with probability one quarter. The high win probability does not create positive expected profit.

Not every stopping rule has expectation zero: never stopping voluntarily ends at -3 almost surely and has expected payoff -3. Thus the original game's general guarantee is an upper bound on expected payoff, not equality for every almost-surely finite stopping time.

### 2. Remove the loss limit: the admissible waiting rules matter

Suppose there is no forced loss exit and no waiting cost or discounting. Choose any fixed positive integer target $`b`$ and wait until the walk reaches it:

```math
H_b=\inf\{n\ge0:S_n=b\}.
```

Starting at zero, recurrence of the simple symmetric random walk implies

```math
P_0(H_b\lt\infty)=1,\qquad
S_{H_b}=b\text{ almost surely},\qquad E_0[S_{H_b}]=b.
```

Each fixed target therefore produces that terminal payoff almost surely. Since the target may be arbitrarily large, the optimal-value supremum is unbounded if almost-surely finite stopping times with infinite mean are allowed.

The essential cost is

```math
\boxed{E_0[H_b]=\infty}.
```

The strategy may endure arbitrarily large interim losses. Almost-sure termination means the waiting time is finite on almost every path; it does not imply a finite average waiting time.

If instead the admissible rules must satisfy $`E_0[\tau]\lt\infty`$, bounded increments make optional stopping valid:

```math
E_0[S_\tau]=0.
```

The optimal value is then zero. Requiring termination by a fixed finite deadline also gives value zero. The strategy of waiting for a fixed positive target is excluded from the finite-mean class.

### 3. Replace the loss exit by an automatic profit exit at +3

Now reaching +3 forces exit, there is no loss limit, and voluntary stopping is still allowed. With almost-surely finite stopping times of possibly infinite mean, wait until +3. It is reached almost surely and pays exactly three units:

```math
P_0(H_3\lt\infty)=1,\qquad E_0[S_{H_3}]=3,\qquad E_0[H_3]=\infty.
```

No terminal payoff can exceed +3, so this strategy is optimal. More generally, from any integer state $`s\le3`$,

```math
\boxed{V(s)=3}.
```

The loss-exit and profit-exit rules are mirror images, but maximizing expected payoff gives different choices. With the loss exit, immediate stopping avoids accepting the certain eventual loss. With the profit exit and no loss bound, waiting attains the maximum permitted payoff. Changing the sign of the process also reverses the direction of the optimization; it does not preserve a maximization problem unchanged.

If finite expected stopping time is required, waiting until +3 is inadmissible. Every admissible rule then has expected payoff equal to the current state, so the initial optimal value returns to zero.

### 4. Comparison and interview takeaway

All values in the table start at zero. The middle column allows almost-surely finite stopping times with infinite expected duration; the last column requires finite expected duration.

| Exit rule | Value with no finite-mean waiting requirement | Value with finite expected stopping time |
| --- | --- | --- |
| Forced loss exit at -3 | 0; stopping immediately is optimal | 0 |
| No forced exit barrier | Unbounded supremum; choose arbitrarily high fixed profit targets | 0 |
| Forced profit exit at +3 | 3; wait for +3 | 0 |

Before invoking optional stopping, state the permitted waiting times and capital constraints. A fair one-step conditional expectation does not by itself imply equality of initial and terminal expectations at every unbounded stopping time. The original loss limit supplies a nonnegative shifted process and an expected-payoff upper bound; removing that limit changes the optimization problem.

### Discussion record

On 2026-11-12, the user requested the Q53 solution, asked how removing the loss limit changes the answer, and then proposed an automatic exit at +3. The assistant explained the value functions, hitting-target strategies and finite-mean stopping-time distinction. The user reported understanding and requested GitHub archival. This records a guided discussion, without adding a formal rating, elapsed time or independent-solve claim.

## Related questions and knowledge

- [P026 — Finite-Horizon Optimal Stopping](P026_Finite_Horizon_Optimal_Stopping.md) — Stopping policies and the assumptions behind stopping results.
