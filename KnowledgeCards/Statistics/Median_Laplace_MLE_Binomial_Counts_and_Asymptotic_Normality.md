# Median: Laplace MLE, Binomial Counts, and Asymptotic Normality

## Source and reading order

- Filed November 1, 2026, from [October 31 drill / Q3](../../DailyTests/2026-10-31.md#q3--laplace-median-estimation), with discussion continuing through November 1.
- [Canonical question and solution](../../Questions/Statistics/S025_Laplace_Location_Median_MLE_and_Asymptotic_Variance.md).
- This card preserves the explanation given in discussion. The median conclusion was independently recalled; completing the log likelihood was user-reported, with the exact expression unsubmitted. The proofs and calculations were supplied. The user reported understanding and requested this archive; independent reconstruction remains unverified.

Reading path: absolute-deviation minimization → order-statistic rank → number of observations below a threshold → binomial normal approximation → the estimator's limiting distribution.

## 1. Why is the median the MLE?

Assume independent observations, n = 2m + 1, and known positive scale b:

```math
f(y;\mu)=\frac1{2b}e^{-|y-\mu|/b},\qquad
\ell(\mu)=-n\log(2b)-\frac1b\sum_{i=1}^n|Y_i-\mu|.
```

Maximizing the log likelihood minimizes the sum of absolute distances to the observations.

Move the candidate location a small positive distance delta to the right without crossing any observation. If j observations are on its left and n - j on its right, each left distance increases by delta and each right distance decreases by delta:

```math
\Delta L=j\delta-(n-j)\delta=(2j-n)\delta.
```

Below the median, more observations are on the right, so moving right decreases the loss. Above it, more observations are on the left, so moving right increases the loss. These directions establish global optimality without requiring a derivative at the kink:

```math
\widehat\mu=Y_{(m+1)}.
```

## 2. Why does the median event equal a count event?

For a fixed real number x, define a threshold close to the true location and count the observations at or below it:

```math
a_n=\mu+\frac{x}{\sqrt n},\qquad
N_n=\sum_{i=1}^n\mathbf1\{Y_i\le a_n\}.
```

First rearrange the scaled-error inequality. Then use the fact that the median is the observation of rank m + 1:

```math
\begin{aligned}
\{\sqrt n(\widehat\mu-\mu)\le x\}
&=\{\widehat\mu\le a_n\}\\
&=\{\text{at least }m+1\text{ observations are at most }a_n\}\\
&=\{N_n\ge m+1\}.
\end{aligned}
```

These are the same event, so their probabilities are exactly equal, not approximately equal.

For the ordered sample 1, 3, 7, 9, 12, the median is 7. At threshold 8, the median is below the threshold and at least three observations are below it. Conversely, if at least three observations are at most a threshold, the third order statistic must also be at most that threshold.

## 3. Why is the count binomial?

Each independent observation is at most the threshold with probability F(a_n). Therefore:

```math
N_n\sim\mathrm{Binomial}(n,p_n),\qquad p_n=F(a_n).
```

At the Laplace distribution's center, the CDF is one half and its derivative is 1/(2b). A first-order expansion gives:

```math
p_n=F\left(\mu+\frac{x}{\sqrt n}\right)
=\frac12+\frac{x}{2b\sqrt n}+o(n^{-1/2}).
```

The success probability differs from one half by order one over square root of n. Multiplication by n produces a count-mean shift of order square root of n. The sign of the shift follows the sign of x.

## 4. What does standardization do?

We now need the probability that a random count reaches the fixed majority threshold:

```math
P(N_n\ge m+1),\qquad m+1=\frac{n+1}{2}.
```

The count's mean and standard deviation satisfy:

```math
np_n=\frac n2+\frac{x\sqrt n}{2b}+o(\sqrt n),\qquad
\sqrt{np_n(1-p_n)}\sim\frac{\sqrt n}{2}.
```

Standardization expresses the threshold's distance from the count's mean in units of its standard deviation:

```math
\frac{\text{threshold}-\text{mean}}{\text{standard deviation}}
=\frac{(n+1)/2-np_n}{\sqrt{np_n(1-p_n)}}
\longrightarrow-\frac xb.
```

The binomial normal approximation then gives:

```math
P(N_n\ge m+1)\longrightarrow
P(Z\ge-x/b)=\Phi(x/b),\qquad Z\sim N(0,1).
```

For example, when x = b, the threshold is approximately one standard deviation below the count's mean, so the chance of exceeding it is about 84%.

Returning to the original scaled estimation error, its limiting CDF is Phi(x/b). Thus:

```math
\boxed{\sqrt n(\widehat\mu-\mu)\xrightarrow{d}N(0,b^2)},
\qquad
\widehat\mu\approx N\left(\mu,\frac{b^2}{n}\right).
```

The second statement is a large-sample approximation, not an exact finite-sample normal law or exact variance formula.

## 5. Comparing the sample mean: where does the integral come from?

Write z = y - mu, combine the positive and negative halves by symmetry, and substitute u = z/b:

```math
\mathrm{Var}(Y)
=2\int_0^\infty z^2\frac1{2b}e^{-z/b}\,dz
=b^2\int_0^\infty u^2e^{-u}\,du.
```

Integrate by parts twice, differentiating the polynomial and integrating the exponential:

```math
\begin{aligned}
\int_0^\infty u^2e^{-u}\,du
&=[-u^2e^{-u}]_0^\infty+2\int_0^\infty ue^{-u}\,du,\\
\int_0^\infty ue^{-u}\,du
&=[-ue^{-u}]_0^\infty+\int_0^\infty e^{-u}\,du=1.
\end{aligned}
```

The boundary terms vanish: the polynomial factor is zero at the lower boundary, and exponential decay dominates polynomial growth at infinity. The first integral therefore equals 2. Independence then gives:

```math
\mathrm{Var}(Y)=2b^2,\qquad
\mathrm{Var}(\bar Y)=\frac{2b^2}{n},\qquad
\mathrm{Avar}(\widehat\mu)=\frac{b^2}{n}.
```

Under this Laplace model, the median has half the mean's first-order asymptotic variance. The efficiency comparison is model-specific; it does not establish that the median is always preferable.

## 6. What happens when one observation becomes extreme?

Fix four observations at 1, 3, 7 and 9. Increase the fifth observation M toward positive infinity. Once M exceeds 9, the mean is (20 + M)/5 and keeps increasing, while the median stays 7.

For an odd sample size of at least three, the median can change as the selected observation moves through the ranks, but eventually becomes constant once that observation is largest. With n = 1, both estimators equal the only observation and both diverge.

## 7. Later independent check

If revisited soon, label the attempt intentional spaced repetition of October 31 Q3, including the November 1 continuation. Reconstruct the event equivalence, the binomial count's mean and standard deviation, and the standardized majority threshold before identifying the limiting CDF. Keep reported understanding distinct from independent derivation.

Related: [S025](../../Questions/Statistics/S025_Laplace_Location_Median_MLE_and_Asymptotic_Variance.md) · [P022 — Discrete Median](../../Questions/Probability/P022_Discrete_Median_and_Symmetry.md) · [OLS card: LLN, CLT and normality](OLS_Expectation_Variance_Residuals_and_Prediction.md).
