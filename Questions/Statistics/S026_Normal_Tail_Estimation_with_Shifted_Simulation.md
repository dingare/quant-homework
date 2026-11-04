# S026 — Shifted Simulation: Normal Tail and Rare Drawdown

## Metadata

- Category: Statistics
- Tags: Monte Carlo, Estimator Unbiasedness, Variance, Rare Events, Shifted Sampling
- Date Added: 2026-11-01
- Original drill: November 1, 2026, Q3
- Status: Original prompt withdrawn November 3 after a valid alternative and an exact calculation exposed its design flaw. Replacement Q3 below is Pending, unattempted, with no hint or solution supplied.

## Original Q3 — Withdrawn After Discussion

You want to estimate the following probability by simulation:

```math
p=P(Z\gt3),\qquad Z\sim N(0,1).
```

A colleague instead generates independent draws $`X_1,\ldots,X_N\sim N(m,1)`$, where $`m\gt0`$, and reports the fraction exceeding 3.

1. What quantity does that fraction estimate? Construct an estimator of p using these same draws that is unbiased for every fixed m. Derive any weighting explicitly.
2. Derive your estimator's variance and compare its expression with the variance of direct simulation from N(0,1). You may express the answer using the standard normal CDF Phi.
3. Does moving m farther to the right necessarily improve precision? Explain why the observed number of threshold exceedances is insufficient to decide.

No code or numerical normal-tail evaluation is required. Original budget: 14 minutes; actual time Not recorded.

### Why this prompt was withdrawn

The target is exactly $`1-\Phi(3)`$ under the stated model, so a normal-CDF evaluation already gives it. The user also independently proposed using the shifted draws to count values above the known threshold $`m+3`$. With m fixed and known as the simulation parameter, this is a valid unbiased estimator of the original probability, with the same Bernoulli variance as direct simulation. The original question did not require keeping the event threshold at 3 under the shifted simulation; this alternative fully satisfies its wording without testing the intended weighting idea. Estimating m from these same draws is unnecessary and would change the unbiasedness argument, but the user's central shifted-threshold construction is correct. This is a prompt-design problem, not a Miss or a user K/R/I gap. Preserve the original wording for audit; do not score it as a failed attempt.

## Replacement Q3 — Rare Drawdown from Shifted Paths

Over ten trading days, let $`Z_1,\ldots,Z_{10}`$ be independent $`N(0,1)`$ daily shocks, and define cumulative P&L $`S_t=Z_1+\cdots+Z_t`$. A risk researcher wants to estimate by simulation:

```math
p=P\!\left(\min_{1\le t\le10}S_t\le-8\right).
```

To generate more downside paths, the researcher draws independent shocks $`X_i\sim N(-a,1)`$, where the positive shift a is chosen and known. For every simulated path, all ten $`X_i`$ values are retained, and the same cumulative-path event is evaluated using those values. The target p still refers to the original zero-mean shocks.

1. What probability does the fraction of shifted paths hitting the barrier estimate? Construct an estimator of p that evaluates the barrier event on the shifted paths and corrects for their changed distribution. Derive the weight for a complete path from the two joint densities.
2. Express the variance of this estimator using an expectation under the shifted simulation. Compare its structure with the variance of direct simulation under the original model. You need not evaluate a multivariate integral.
3. If a is so large that almost every shifted path hits the barrier, does that guarantee better precision? Explain what evidence from the weighted simulated outputs would help you choose a shift.

Keep the derivation interview-length. No code is required. Replacement budget: 14 minutes; actual time Not recorded. No hint or solution has been supplied for this replacement.

## Assessment History

- [November 1 Q3, discussed November 3](../../DailyTests/2026-11-01.md#q3--shifted-simulation): original prompt withdrawn after the user identified a valid recentering estimator and questioned the point of simulating an exactly available normal tail. No Miss or K/R/I gap assigned. Replacement prompt above remains Pending with no hint or solution.
