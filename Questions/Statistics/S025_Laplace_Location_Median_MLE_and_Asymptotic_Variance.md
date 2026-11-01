# S025 — Laplace Location: Median MLE and Asymptotic Variance

## Metadata

- Category: Statistics
- Tags: Maximum Likelihood, Sample Median, Order Statistics, Binomial CLT, Robustness
- Date Added: 2026-11-01
- Original drill: October 31, 2026, Q3; discussion continued through November 1
- Status: All three parts explained; independent derivation not yet verified.

## Core Question

Independent observations have density:

```math
f(y;\mu)=\frac1{2b}\exp\left(-\frac{|y-\mu|}{b}\right),
\qquad b\gt0.
```

The scale b is known, the location mu is unknown, and n is odd.

1. Derive the maximum-likelihood estimator of mu and justify optimality.
2. Derive the limiting distribution of the square-root-n-scaled estimation error, without simply quoting a general quantile variance formula.
3. Compare its large-sample variance with that of the sample mean. Holding the other observations fixed, explain the effect of sending one observation to positive infinity.

Original budget: 12 minutes; actual time not recorded. A few equations and concise reasoning suffice; a formal asymptotic proof was not required.

## Solution

### 1. Median maximizes likelihood

```math
\ell(\mu)=-n\log(2b)-\frac1b\sum_{i=1}^n|Y_i-\mu|.
```

Write n = 2m + 1. Between observations, if j points lie to the left of mu, moving mu right by a small positive delta changes total absolute deviation by:

```math
j\delta-(n-j)\delta=(2j-n)\delta.
```

Below the sample median this change is negative; above it, positive. The loss therefore decreases up to the median and increases afterward. This proves global optimality without requiring a derivative at the kink:

```math
\widehat\mu=Y_{(m+1)}.
```

### 2. Convert a median event to a binomial-count event

The detailed English walkthrough, including the event equivalence, threshold standardization and integral calculation, is in the [median study card](../../KnowledgeCards/Statistics/Median_Laplace_MLE_Binomial_Counts_and_Asymptotic_Normality.md).

For fixed real x, define:

```math
a_n=\mu+\frac{x}{\sqrt n},\qquad
N_n=\sum_{i=1}^n\mathbf1\{Y_i\le a_n\}.
```

The median is at most a_n exactly when at least m + 1 observations are at most a_n:

```math
P\left(\sqrt n(\widehat\mu-\mu)\le x\right)
=P(N_n\ge m+1),\qquad
N_n\sim\mathrm{Binomial}(n,p_n).
```

Since the CDF has value one half and derivative 1/(2b) at mu:

```math
p_n=F(a_n)=\frac12+\frac{x}{2b\sqrt n}+o(n^{-1/2}).
```

The count's mean shifts by order square root of n, the same order as its standard deviation. Standardizing the majority threshold gives:

```math
\frac{(n+1)/2-np_n}{\sqrt{np_n(1-p_n)}}\longrightarrow-\frac xb.
```

The binomial normal approximation then yields:

```math
P(N_n\ge m+1)\longrightarrow1-\Phi(-x/b)=\Phi(x/b),
\qquad
\boxed{\sqrt n(\widehat\mu-\mu)\xrightarrow{d}N(0,b^2)}.
```

Thus the median's first-order asymptotic variance is b squared divided by n; this is not an exact finite-sample variance claim.

### 3. Mean variance and a single extreme observation

Symmetry gives mean mu. With u = z/b:

```math
\mathrm{Var}(Y)
=2\int_0^\infty z^2\frac1{2b}e^{-z/b}\,dz
=b^2\int_0^\infty u^2e^{-u}\,du
=2b^2.
```

Independence gives:

```math
\mathrm{Var}(\bar Y)=\frac{2b^2}{n},
\qquad
\mathrm{Avar}(\widehat\mu)=\frac{b^2}{n}.
```

Under this Laplace model the median has half the mean's first-order asymptotic variance. This comparison is model-specific.

For fixed observations 1, 3, 7, 9 and a fifth observation M exceeding 9, the mean is (20 + M)/5 and diverges as M increases. The median stays 7. In general, for odd n at least three, the median can change as the selected observation moves through the ranks, but eventually becomes constant once that observation is largest. For n = 1, mean and median are the same observation and both diverge.

## Common mistakes and clarifications

- The count event uses at least m + 1 observations, because that is the median's rank.
- Standardize the random count using its own mean and standard deviation; the threshold's limit is negative x/b, so the desired upper tail is Phi(x/b).
- Distinguish the limiting variance b squared of the scaled error from the estimator's approximate variance b squared divided by n.
- Asking why two events are equivalent, what standardization does, or how integration by parts works does not alone establish a new knowledge gap.
- Reported understanding after explanation is preserved; it does not establish independent reconstruction.

## Connections

- [Median study card](../../KnowledgeCards/Statistics/Median_Laplace_MLE_Binomial_Counts_and_Asymptotic_Normality.md): English step-by-step review of this discussion.
- [P022 — Discrete Median and Symmetry](../Probability/P022_Discrete_Median_and_Symmetry.md): order-statistic events, with a different sampling model.
- [S011 — Exponential MLE and Fisher Information](S011_Exponential_MLE_and_Fisher_Information.md): likelihood-based estimators; the present estimator comes from absolute-deviation geometry and a binomial-count asymptotic argument.

## Assessment History

- [October 31 drill, continued through November 1 — Q3](../../DailyTests/2026-10-31.md#q3--laplace-median-estimation).
