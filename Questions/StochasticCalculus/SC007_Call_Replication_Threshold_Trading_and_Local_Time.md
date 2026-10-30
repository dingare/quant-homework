# SC007 — Call Replication, Threshold Trading, and Local Time

## Metadata

- Category: Stochastic Calculus
- Secondary: Probability, Derivatives Pricing, Trading Strategies
- Difficulty: Intermediate intuition; advanced continuous-time explanation
- Interview Relevance: Distinguishing a payoff diagram from a self-financing trading strategy
- Tags: European Call, Threshold Trading, Self-Financing, Finite Variation, Quadratic Variation, Tanaka Formula, Local Time, Itô Integral
- Date Added: 2026-10-30
- Source: The user's October 30 option-replication discussion and subsequent interview recollection. The question below reconstructs the mathematical issue; it is not a verbatim interview transcript.
- Status: Reference solution available; independent understanding remains unverified. See [Assessment History](#assessment-history).

**Reading order:** Core Question → Hint → Intuition → Geometry → Solution 1–4. Continue to Solution 5–8 for the mathematics. The final approximation discussion is optional on a first reading.

## Core Question

Consider a European call with strike $`K=100`$ and maturity $`T`$. Assume zero interest rates, no dividends, no transaction costs, and continuous stock prices. You may borrow and lend at the same zero rate.

Someone proposes this strategy:

> Hold one share whenever the stock price is above 100, and hold no shares whenever it is at or below 100. Buy on an upward crossing of 100 and sell on a downward crossing of 100.

They argue that every completed round trip buys and sells at 100, so it costs nothing. If the stock finishes above 100, the final share earns exactly its price above 100. Therefore, they claim, the strategy replicates the call payoff.

1. Why does this argument look correct on a continuous, piecewise-linear price path?
2. If you rebalance only at discrete observation times, what can go wrong? Explain a downward crossing near maturity and give a numerical example.
3. Does ideal continuous rebalancing make the strategy replicate a call when prices follow a nondegenerate Brownian diffusion? Explain the intuition before using stochastic calculus.
4. Define the strategy's self-financing wealth and derive its difference from the call payoff using Tanaka's formula.
5. Why does simply declaring “one share financed by borrowing the strike” fail to prove self-financing? Would giving the strategy the call premium fix the problem?

For the initial comparison, use initial wealth equal to intrinsic value, $`V_0=(S_0-K)^+`$; this is zero if the stock starts below or at the strike. Later compare this with starting from the actual option premium.

## Hint

Separate three objects: **the payoff you want, the stock holding you choose, and the cash account required to finance that holding**.

Start with a path you can draw. Next, calculate the profit of a strategy that observes only a few prices. Then ask what happens to the sum of many small crossing errors as the observation grid becomes finer. Continuity alone does not tell you whether that sum vanishes.

## Intuition

### 1. The proposed trade matches the slope of intrinsic value

A call's terminal payoff is zero below the strike and rises dollar for dollar above it. Holding zero shares below the strike and one share above it therefore matches the payoff diagram's slope.

For a smooth, ordinary price curve, accumulating “slope times price change” reconstructs the change in the payoff. This is why the proposed strategy is persuasive. It identifies the correct slope of **intrinsic value**, but it still has to establish that trading can finance that value process.

### 2. On a simple drawn path, the crossing argument actually works

Imagine the stock starts at 99, crosses 100, reaches 104, returns to 100, and eventually finishes at 102. If you can trade at every crossing of this fixed piecewise-linear path, the first purchase and sale break even. The last purchase at 100 earns 2. The call also pays 2.

This example is valid under its assumptions. A useful explanation must preserve that fact and identify which assumption changes in a Brownian model.

### 3. A discrete observation grid reveals the missing effect

Suppose you see 100.1, hold one share, and next see 99.7. You lose 0.4 over that interval, but intrinsic value falls by only 0.1. The extra 0.3 is a crossing discrepancy.

An upward crossing has a corresponding effect: if you hold no shares at 99.8 and next observe 100.3, you miss the 0.3 increase in intrinsic value. The [worked example](#4-a-discrete-rebalancing-example) adds these discrepancies explicitly.

This is the useful part of the user's “last short interval falling through 100” idea. To make it an argument, specify when you observe, when you trade, and what price you receive. A single discrete crossing does not by itself settle the continuous-time question.

### 4. The hard question is whether small errors add up to zero

For one fixed finite piecewise-linear path, refining the observation grid removes the discrepancy. Brownian paths retain fluctuations at arbitrarily small scales. Individual crossing errors shrink, but their cumulative limit can remain positive.

That limiting correction is half the local time at the strike. At this stage, think of local time as a measure of accumulated fluctuation near the payoff's kink. The precise definition comes later; it is not a transaction fee or a jump in the stock price.

### 5. A quick expectation check already challenges free replication

Under a suitable zero-rate risk-neutral model, a self-financing stock-trading gain has expected value zero. A call starting at the money has a nonnegative payoff and a positive chance of paying something, so its expected payoff is positive.

Consequently, a zero-initial-wealth trading rule cannot replicate that payoff under these conditions. This is a useful check before calculating the exact pathwise shortfall. It relies on the martingale and integrability assumptions stated below, rather than on a general claim that every stochastic integral has expectation zero.

## Geometry

The payoff function $`g(s)=(s-K)^+`$ has two straight pieces:

| Stock price | Payoff | Slope | Proposed stock holding |
| --- | --- | --- | --- |
| $`s\lt K`$ | $`0`$ | $`0`$ | No shares |
| $`s\gt K`$ | $`s-K`$ | $`1`$ | One share |

The crucial feature is the **kink at the strike**. Away from it, the slope is constant. At the kink, the slope increases from zero to one. For a smooth convex function, Itô's formula adds a curvature correction. For this nonsmooth convex payoff, Tanaka's formula supplies the corresponding local-time correction.

The slope of this terminal payoff diagram is different from the delta of an option with time remaining. Before expiry, the option's value reflects possible future movement across the strike.

## Solution

### 1. Define the payoff, gain, wealth, and financing separately

Set

```math
g(s)=(s-K)^+,\qquad
H_t=\mathbf1_{\{S_t\gt K\}}.
```

The quantities to keep separate are:

| Quantity | Meaning |
| --- | --- |
| $`g(S_T)`$ | Call payoff at maturity |
| $`H_t`$ | Number of shares held |
| $`G_t=\int_0^t H_u\,dS_u`$ | Cumulative stock-trading gain |
| $`V_t=V_0+G_t`$ | Wealth of the self-financing strategy at zero interest |
| $`B_t=V_t-H_tS_t`$ | Cash balance, possibly negative |
| $`C_0`$ | Initial option premium |

Self-financing means that purchases and sales are funded within the portfolio, rather than through additional deposits or withdrawals. At zero interest and without dividends, changes in wealth therefore equal stock-trading gains.

A call bought for $`C_0`$ has terminal payoff $`g(S_T)`$ and, in this zero-rate setting, net profit $`g(S_T)-C_0`$. Comparing a call payoff with a strategy's gain without aligning initial capital is incomplete.

For the stochastic calculation, take a continuous Itô diffusion

```math
dS_t=\mu_t\,dt+\nu_t\,dW_t.
```

Assume the usual local integrability conditions and standard nondegeneracy near $`K`$, as in Black–Scholes with positive strike and volatility. Use the usual Brownian filtration. The bounded predictable holding $`H`$ is integrated in the Itô sense. The expectation arguments additionally require the stated true-martingale and square-integrability conditions. Jumps, sticky boundaries, and reflection are outside this setup.

### 2. Why exact crossing trades work on finite-variation paths

For a continuous finite-variation path, the ordinary change-of-variables formula gives

```math
g(S_T)-g(S_0)
=\int_0^T\mathbf1_{\{S_t\gt K\}}\,dS_t.
```

Here the integral is a pathwise Lebesgue–Stieltjes integral. With $`V_0=g(S_0)`$, the strategy's terminal wealth equals the call payoff.

For a finite piecewise-linear path, the earlier round-trip explanation makes this identity concrete: completed excursions above the strike begin and end at the same price, and a final unfinished excursion contributes the final intrinsic value.

The relevant property is **continuous finite variation**, not merely a finite number of crossings. The chain-rule identity also holds for continuous finite-variation paths with infinitely many crossings.

### 3. Write down the discrete crossing remainder

On an observation grid, hold the position chosen at the left endpoint until the next observation. For one interval, write $`x=S_{t_i}`$ and $`y=S_{t_{i+1}}`$. Define

```math
R_i=g(y)-g(x)-\mathbf1_{\{x\gt K\}}(y-x).
```

The cases are elementary:

```math
R_i=
\begin{cases}
y-K,&x\le K\lt y,\\
K-y,&y\le K\lt x,\\
0,&x,y\text{ remain on the same side of }K.
\end{cases}
```

The boundary cases where an endpoint equals the strike are covered by these conventions; the remainder is always nonnegative. Equivalently, this follows from convexity and the chosen slope at the starting price.

Adding intervals telescopes the payoff changes:

```math
g(S_T)-g(S_0)
=\sum_i\mathbf1_{\{S_{t_i}\gt K\}}
 (S_{t_{i+1}}-S_{t_i})+\sum_iR_i.
```

For the downward crossing $`100.1\to99.7`$ at strike 100, payoff changes by $`-0.1`$, stock-trading gain is $`-0.4`$, and the remainder is $`0.3`$. A shorter time interval alone does not determine a smaller discrepancy; the price movement and the trading convention matter.

### 4. A discrete rebalancing example

Let $`K=100`$ and start with zero wealth. Observe only the prices below and rebalance after each observation. Each interval's gain uses the holding chosen at its starting price.

| Starting price | Ending price | Shares during interval | Trading gain | Payoff change minus gain |
| ---: | ---: | ---: | ---: | ---: |
| 99.8 | 100.3 | 0 | 0.0 | 0.3 |
| 100.3 | 100.1 | 1 | -0.2 | 0.0 |
| 100.1 | 99.7 | 1 | -0.4 | 0.3 |
| 99.7 | 100.2 | 0 | 0.0 | 0.2 |
| 100.2 | 101.0 | 1 | 0.8 | 0.0 |
| **Total** | | | **0.2** | **0.8** |

The call pays 1, while self-financing trading earns 0.2. The missing 0.8 is exactly the sum of crossing remainders.

If these same observations are connected by a fixed continuous piecewise-linear curve and you trade exactly at every crossing of 100, trading instead earns 1. Thus this table illustrates **discrete observation and rebalancing error**. It is not a numerical computation of Brownian local time.

### 5. Brownian roughness and Tanaka's exact correction

Brownian motion has infinite total variation on every nontrivial time interval, almost surely. Its squared increments have a nonzero cumulative limit, called quadratic variation:

```math
[W]_t=t,\qquad
[S]_t=\int_0^t\nu_u^2\,du.
```

For a continuous finite-variation path, quadratic variation is zero. This distinction explains why an ordinary chain rule is insufficient for a Brownian diffusion.

For a smooth function, Itô's formula contains a second-order term:

```math
df(S_t)=f'(S_t)\,dS_t+\frac12f''(S_t)\,d[S]_t.
```

The call payoff is not twice differentiable at $`K`$. Informally, smoothing the kink concentrates the curvature correction near the strike. Tanaka's formula gives the precise limiting identity:

```math
\boxed{
(S_T-K)^+=(S_0-K)^+
+\int_0^T\mathbf1_{\{S_t\gt K\}}\,dS_t
+\frac12L_T^K(S).
}
```

With $`V_0=g(S_0)`$, subtract the local-time term to obtain the strategy's wealth:

```math
\boxed{V_T=g(S_T)-\frac12L_T^K(S).}
```

This is the exact shortfall. It can be zero on some paths, such as paths that never reach the strike. Replication, however, requires matching the payoff almost surely across the model's possible outcomes. A nondegenerate diffusion generally leaves a nonzero shortfall with positive probability.

For the positive-part formula, the local-time coefficient is **one half**; for the absolute-value formula it is **one**. See [Björk, Tanaka formulas, Section 5.2](https://arxiv.org/pdf/1512.08912#page=24) for the normalization.

### 6. What local time measures

In the standard nondegenerate diffusion setting used here, local time can be expressed through the shrinking-band limit

```math
L_T^K(S)=\lim_{\varepsilon\downarrow0}
\frac{1}{2\varepsilon}
\int_0^T\mathbf1_{\{|S_t-K|\lt\varepsilon\}}\,d[S]_t.
```

First take a narrow price band around the strike. Measure the quadratic variation accumulated while the stock is in that band. Divide by the band's width, then shrink the band. The result is a density of accumulated fluctuation at that price level.

Local time is nonnegative, starts at zero, and increases only when the process is at the strike. It is not ordinary clock time spent exactly at 100: a nondegenerate diffusion spends zero Lebesgue time at a fixed level, almost surely, while the normalized shrinking-band quantity can be positive. For finite-variation paths, **semimartingale local time with this quadratic-variation normalization** is zero.

This is the occupation-density interpretation of local time. It also explains why an arbitrarily narrow region can produce a finite contribution after normalization. See [Björk, Section 4.1](https://arxiv.org/pdf/1512.08912#page=14).

### 7. The cash-account trap, option premium, and actual delta hedging

**The cash-account trap.** Suppose you declare

```math
B_t=-KH_t.
```

Then the marked portfolio value satisfies

```math
H_tS_t+B_t=H_t(S_t-K)=g(S_t).
```

This is an algebraic identity. It does not show that the specified cash balance can be maintained using only proceeds from trading. Tanaka's formula shows the funding requirement:

```math
g(S_t)=g(S_0)+G_t+A_t,\qquad
A_t=\frac12L_t^K(S).
```

To maintain intrinsic value while imposing that stock holding, cumulative external funding must supply $`A_t`$. Without that funding, the self-financing cash balance is $`V_0+G_t-H_tS_t`$, rather than automatically $`-KH_t`$. This distinction is the stop-loss/start-gain paradox; see [Carr and Jarrow's paper](https://engineering.nyu.edu/sites/default/files/2019-03/Carr-stop-loss-start-gain-strategy.pdf).

**Time value.** In a zero-rate, no-dividend replicating model such as Black–Scholes, assume $`S`$ is a square-integrable martingale under the pricing measure $`Q`$. The bounded holding then has a zero-mean gain. Taking expectations in Tanaka's identity gives

```math
C_0=E_Q[g(S_T)]
=g(S_0)+\frac12E_Q[L_T^K(S)].
```

The expected correction accounts for the option's time value in this setup. Realized local time is random; the initial premium is a fixed price known at inception.

**Starting with the option premium.** If the same threshold rule starts with $`C_0`$, its terminal discrepancy becomes

```math
\begin{aligned}
V_T^{\mathrm{premium}}-g(S_T)
&=C_0-g(S_0)-\frac12L_T^K(S)\\
&=\frac12\left(E_Q[L_T^K(S)]-L_T^K(S)\right).
\end{aligned}
```

Its mean is zero under these assumptions, but the discrepancy is generally random and not identically zero. Matching expected value does not establish replication.

**Actual delta hedging.** In Black–Scholes, the replicating stock holding before expiry is $`\partial C(t,S_t)/\partial S`$, funded by the appropriate cash account and initial premium. It reflects time remaining and possible future crossings; it is generally not the zero-or-one slope of current intrinsic value.

### 8. Optional extension: why drawing finer paths gives a different limit

For standard nondegenerate Brownian diffusions and deterministic observation grids with mesh tending to zero, causal left-endpoint gains converge in probability to the Itô integral:

```math
\sum_i\mathbf1_{\{S_{t_i}\gt K\}}
(S_{t_{i+1}}-S_{t_i})
\longrightarrow
\int_0^T\mathbf1_{\{S_t\gt K\}}\,dS_t.
```

Combining this with the exact discrete remainder identity yields

```math
\sum_iR_i\longrightarrow\frac12L_T^K(S).
```

Although individual remainders shrink, their sum need not disappear.

Now linearly interpolate the sampled prices to obtain a finite-variation path $`S^{(n)}`$. Those interpolations converge uniformly to the continuous price path, yet their ordinary integrals satisfy

```math
\int_0^T\mathbf1_{\{S_t^{(n)}\gt K\}}\,dS_t^{(n)}
=g(S_T^{(n)})-g(S_0^{(n)})
\longrightarrow g(S_T)-g(S_0).
```

The limits differ because **uniform convergence of price paths does not by itself imply convergence of trading gains**. Integrating along an already drawn segment permits exact crossing trades on that segment. Constructing its interior uses the next observed endpoint, which is future information relative to times inside the segment; this is not the same causal strategy on the original market.

A smooth example makes the distinction visible without a payoff kink:

```math
\int_0^T S_t^{(n)}\,dS_t^{(n)}
=\frac12\left((S_T^{(n)})^2-(S_0^{(n)})^2\right),
```

```math
\int_0^T S_t\,dS_t
=\frac12\left(S_T^2-S_0^2-[S]_T\right).
```

The correction survives even though the interpolated prices approximate the observed path closely. For the discontinuous threshold holding, use Tanaka's identity rather than applying a smooth-function approximation theorem without checking its hypotheses.

## Key Knowledge Points

- **Self-financing is a financing condition:** wealth changes must come from the chosen holdings, not from unexplained cash resets.
- **A model assumption determines the calculus:** continuous finite variation permits an ordinary chain rule; a Brownian diffusion introduces quadratic variation.
- **Convexity produces nonnegative discrete remainders:** for the call, the cumulative continuous-time correction is half its local time at the strike.
- **Local time uses quadratic-variation occupation density:** it is different from clock time spent exactly at the strike.
- **Expected equality is weaker than replication:** the latter requires the correct payoff almost surely.

## Common Mistakes

| Mistake | Correction |
| --- | --- |
| “The price is continuous, so every round trip must cancel.” | That reasoning works for the fixed finite-variation example; it does not justify the same infinite-scale limit for Brownian paths. |
| “A single downward crossing disproves ideal continuous replication.” | State the observation and execution convention. A discrete crossing illustrates rebalancing error; the continuous diffusion needs the local-time argument. |
| “Borrowing 100 whenever I hold a share proves self-financing.” | Check whether trading itself maintains that cash balance. An algebraic portfolio value is not a financing proof. |
| “The holding must be the option delta because it matches the payoff slope.” | The payoff slope is terminal intrinsic-value sensitivity. Before expiry, option delta reflects remaining uncertainty. |
| “Local time means the stock waits exactly at 100.” | It measures a normalized occupation density using quadratic variation. |
| “Local time is another name for transaction costs.” | The correction exists in this frictionless continuous model. |
| “Adding the call premium solves it.” | It corrects the expected funding gap under the specified pricing assumptions, not the realized random discrepancy. |
| “An Itô integral always has mean zero.” | The martingale and integrability conditions matter. Physical-measure drift also matters. |
| “The fixed-grid table computes local time.” | It computes discrete crossing remainders; local time arises as an appropriate diffusion limit. |

## Interview Follow-ups

1. **Can you answer without immediately quoting Tanaka?** Explain the piecewise-linear case, calculate one discrete crossing discrepancy, and use the risk-neutral expectation check. Then identify what the exact formula must resolve.
2. **What if the stock never touches the strike?** Local time at the strike is zero, and the threshold rule matches the intrinsic-value change on that path. This does not establish replication across all outcomes.
3. **What if the stock starts above the strike?** Begin with $`g(S_0)=S_0-K`$ for the intrinsic-value comparison; otherwise an initial-capital mismatch is mixed into the local-time effect.
4. **What if interest rates or dividends are nonzero?** Rebuild the self-financing equation with financing and income terms. Do not reuse the zero-rate fixed-strike decomposition unchanged.
5. **What if prices jump?** Additional jump-crossing remainders enter the change-of-variables formula. The continuous-diffusion result here does not cover that model.
6. **Is a well-defined gain automatically an admissible strategy?** No. Stochastic integrability, self-financing, and an admissible lower bound on wealth are separate requirements. Do not treat the rule as a zero-cost arbitrage.
7. **Can you check the expectation numerically by hand?** In the arithmetic Brownian toy model $`S_t=100+20W_t`$, at strike 100 and maturity 1, the gain has mean zero while the call payoff has mean $`20/\sqrt{2\pi}\approx7.98`$. Tanaka gives the same value for half the expected local time. This toy model permits negative prices; it illustrates the mechanism rather than modeling a positive stock price.

## Market / Rates Application

The practical lesson is to distinguish a **state-dependent exposure rule** from a funded option hedge. A rule that switches exposure when a stock, yield, or spread crosses a threshold does not inherit an option payoff merely because its positions resemble the payoff's slopes.

For a rates instrument, work with the actual tradable price, cash flows, and financing. Yield is not itself a self-financing traded asset, and a call on a bond price is not a call on its yield. This is a review extension, not an additional question recalled from the interview.

## Connections

- [SC001 — Itô's Lemma and Discounted Price Martingale](SC001_Itos_Lemma_and_Discounted_Price_Martingale.md): starts with smooth functions and explains the role of the pricing measure.
- [SC002 — Change of Measure](SC002_Change_of_Measure_I_Understanding_P_Q_and_the_Radon_Nikodym_Derivative.md): distinguishes physical dynamics from risk-neutral pricing and expectation arguments.
- [P002 — Fair Games and Stop-Loss](../Probability/P002_Optional_Stopping_Fair_Games_and_Why_Stop_Loss_Does_Not_Create_Alpha.md): a trading or stopping rule does not generate free expected gains under the relevant martingale conditions.
- [Threshold Trading / Local Time review card](../../KnowledgeCards/StochasticCalculus/Call_Payoff_Threshold_Trading_Tanaka_and_Local_Time.md): compact reading map and link to the preserved assessment anchor.

## Assessment History

### Interview assessment — 2026-10-30

- The user confirmed that this topic was asked in the October 30 real interview. It is not a DailyTests session.
- Latest self-reported completion: **at most about 20%**, superseding the initial estimate of 40–50%. This is not an interviewer score or a probability of passing.
- Recorded answer: the user considered a very short interval near maturity in which the price drops from above 100 to below 100, and used it to question the proposed replication.
- The exact cash-flow calculation, hint usage, and elapsed time were not recorded. The complete continuous-time argument was not independently verified.
- The worked solution above is post-interview reference material. It does not change the assessment to a cold solve, establish mastery, or justify assigning a Knowledge / Retrieval / Implementation gap without evidence.

## What to Remember

**Suggested interview answer:** “The crossing argument works on a continuous finite-variation path. With discrete observations, crossings create nonnegative remainders between changes in call intrinsic value and stock-trading gains. In a Brownian model their cumulative limit can survive: Tanaka's formula identifies it as half the local time at the strike. Thus, starting from intrinsic value, the self-financing threshold strategy is short by that amount. Assigning cash equal to minus the strike while holding a share silently supplies the missing funding. The actual option hedge uses the option's pre-expiry delta and its premium.”

```math
\boxed{
\text{Call payoff}
=\text{initial intrinsic value}
+\text{threshold-trading gain}
+\frac12\text{local time at the strike}.
}
```

For independent review:

- [ ] Explain why the simple drawn-path argument is correct in its own setting.
- [ ] Recalculate the discrete table and specify the cash account.
- [ ] Derive the shortfall from Tanaka and check the one-half coefficient.
- [ ] Explain local time without confusing it with clock time or fees.
- [ ] Explain why matching expected value or uniformly approximating a price path is insufficient for replication.
