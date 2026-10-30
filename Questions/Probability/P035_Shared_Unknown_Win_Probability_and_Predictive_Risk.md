# P035 — Shared Unknown Win Probability and Predictive Risk

## Metadata

- Category: Probability
- Tags: Bayes, Conditional Independence, Total Variance, Predictive Risk
- Date Added: 2026-10-22
- Original drill dates: 2026-10-20
- Status: Archived interview material; performance is recorded separately below.

## Interview drill — 2026-10-20 Q2

Source and assessment: [2026-10-20 Q2](../../DailyTests/2026-10-20.md#q2--prediction-with-a-shared-unknown-win-probability). The reference material below does not change that attempt’s recorded result.

### Question

A strategy has a fixed but unknown win probability P, drawn once from $`\mathrm{Uniform}(0,1)`$. Conditional on $`P=p`$, outcomes $`W_1,W_2,\ldots`$ are independent Bernoulli(p) variables. The first four outcomes are:

```math
D=(W_1,W_2,W_3,W_4)=(1,1,1,0).
```

1. Derive the conditional density of P given D, then calculate the probability that the next trade wins.
2. Calculate the probability that both of the next two trades win. Are those two outcomes independent conditional on D? Explain.
3. Let $`N=\sum_{t=5}^{14}W_t`$. Calculate $`\mathrm{Var}(N\mid D)`$. Compare it with a risk engine that treats the next ten trades as independent, each having the win probability from part 1. Explain the source of any difference.

Derive the quantities rather than quoting a conjugate-prior formula.

### Key solution

For the specified ordered record, the user's independently correct likelihood is $`p^3(1-p)`$. With uniform prior density:

```math
P(D)=\int_0^1p^3(1-p)\,dp=\frac14-\frac15=\frac1{20},
\qquad
f_{P\mid D}(p)=20p^3(1-p),\quad 0\lt p\lt 1.
```

The density is zero outside that interval. The next-win probability averages p over this density:

```math
P(W_5=1\mid D)=\int_0^1p\,f_{P\mid D}(p)\,dp
=20\left(\frac15-\frac16\right)=\frac23.
```

Given the true p, two future wins have probability p squared. Averaging over the still-unknown shared parameter gives:

```math
P(W_5=W_6=1\mid D)
=\int_0^1p^2f_{P\mid D}(p)\,dp
=20\left(\frac16-\frac17\right)=\frac{10}{21}
\ne\left(\frac23\right)^2.
```

Thus future outcomes are independent given the true P, but not given only D. A higher shared P makes both outcomes more likely to be wins. Seeing a fifth-trade win updates the prediction for the sixth:

```math
P(W_6=1\mid W_5=1,D)=\frac{10/21}{2/3}=\frac57\ne\frac23.
```

For every future single trade and every distinct future pair:

```math
\mathrm{Var}(W_t\mid D)=\frac23-\left(\frac23\right)^2=\frac29,
\qquad
\mathrm{Cov}(W_i,W_j\mid D)=\frac{10}{21}-\frac49=\frac{2}{63}.
```

There are ten single variances and twice 45 unordered pair covariances:

```math
\mathrm{Var}(N\mid D)
=10\frac29+90\frac{2}{63}
=\frac{320}{63}\approx5.08.
```

The independent Bernoulli(2/3) risk engine instead gives $`10(2/3)(1/3)=20/9\approx2.22`$. It retains the correct single-trade marginal variance but omits positive pairwise dependence. The shared parameter uncertainty, rather than a causal effect of one outcome on another, creates the posterior predictive dependence.

The requested intuition follows from total variance. For a count of n future wins, conditional on current data D:

```math
\mathrm{Var}(N\mid D)
=nE[P(1-P)\mid D]+n^2\mathrm{Var}(P\mid D),
\qquad
\mathrm{Var}(N/n\mid D)
=\frac{E[P(1-P)\mid D]}n+\mathrm{Var}(P\mid D).
```

At fixed current information, averaging more future outcomes reduces independent outcome noise but does not remove uncertainty about their common P. Actually observing new data and updating the posterior can reduce that parameter uncertainty. Predictive dependence under uncertainty does not establish time dependence of outcomes conditional on the fixed true P.

**Practical discussion requested by the user:** distinguish outcome risk from uncertainty in estimated strategy quality. With a uniform prior and n conditionally independent fixed-probability observations containing k wins, posterior density is proportional to $`p^k(1-p)^{n-k}`$, and posterior mean is $`(k+1)/(n+2)`$. A posterior interval and probability of exceeding a specified benchmark convey more than the sample win rate alone. The same observed win rate with four versus hundreds of trades has different uncertainty. This simple model does not itself repair selection bias, time dependence, changing strategy quality or data leakage; win rate alone also omits payoff sizes and costs. Evaluation data not used to select the strategy and assumptions appropriate to the data remain relevant. This was a methodological explanation, not an independently submitted evaluation protocol.

## Assessment history

- [2026-10-20 Q2 — assessment](../../DailyTests/2026-10-20.md#q2--prediction-with-a-shared-unknown-win-probability)

## Related questions and knowledge

- [P024 — Bayesian Coin Selection and Prediction](P024_Bayesian_Coin_Selection_and_Prediction.md) — Posterior predictive averaging over a shared latent parameter; the October 30 discussion derives Beta updating and compares an unknown coin bias with a separate fair-coin model.
- [P030 — Product Distribution and Event Conditioning](P030_Product_Distribution_and_Event_Conditioning.md) — Conditioning and independence depend on the information retained.
- [T012 — Probability Forecasts, Calibration, and Evaluation](../TimeSeries/T012_Probability_Forecasts_Calibration_and_Evaluation.md) — Predictive probability and the evaluation of its quality.
- [Indicator Random Variables Cookbook](../../KnowledgeCards/Probability/Indicator_Random_Variables_Cookbook.md) — Knowledge card.
