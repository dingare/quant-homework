# S006 — Two Noisy Proxies and Errors-in-Variables

## Metadata

- Category: Statistics
- Secondary: Econometrics, Instrumental Variables, Signal Combination
- Difficulty: ★★★★☆
- Tags: Measurement Error, Attenuation Bias, Instrumental Variables, Noisy Proxies, Inverse-Variance Weighting
- Review Priority: High
- Date Added: 2026-07-23
- Status: Final

## Core Question

Let

$$
y=\beta x+\varepsilon,\qquad \beta=2,
$$

with

$$
\mathrm{Var}(x)=1,\qquad
\mathrm{Var}(\varepsilon)=4.
$$

The latent $x$ is not observed. Instead,

$$
z_1=x+u_1,\qquad z_2=x+u_2,
$$

where

$$
\mathrm{Var}(u_1)=1,\qquad
\mathrm{Var}(u_2)=3,
$$

and $x,\varepsilon,u_1,u_2$ are mutually independent.

Find the OLS probability limit using $z_1$, the IV probability limit using $z_2$ as an instrument, the population first stage, and the best unbiased linear combination of the two proxies.

## OLS and Attenuation

$$
\mathrm{Cov}(z_1,y)
=\mathrm{Cov}(x+u_1,2x+\varepsilon)=2,
$$

while

$$
\mathrm{Var}(z_1)=1+1=2.
$$

Therefore

$$
\boxed{
\mathrm{plim}\hat\beta_{\mathrm{OLS}}=1
}.
$$

In general, classical measurement error multiplies the true slope by the reliability ratio

$$
\frac{\mathrm{Var}(x)}
{\mathrm{Var}(x)+\mathrm{Var}(u_1)}.
$$

Noise inflates the regressor variance without increasing its covariance with the outcome.

## IV Using the Second Proxy

The IV estimand is

$$
\frac{\mathrm{Cov}(z_2,y)}
{\mathrm{Cov}(z_2,z_1)}
=\frac{2}{1}.
$$

Hence

$$
\boxed{
\mathrm{plim}\hat\beta_{\mathrm{IV}}=2
}.
$$

The instrument is relevant because both proxies share $x$, and valid because $u_2$ is independent of $u_1$ and $\varepsilon$.

The population first-stage coefficient is

$$
\boxed{
\pi=\frac{\mathrm{Cov}(z_2,z_1)}
{\mathrm{Var}(z_2)}
=\frac1{1+3}=\frac14
}.
$$

Validity does not imply strength: the noisy $z_2$ gives a relatively weak first stage.

## Minimum-Variance Unbiased Proxy

Restrict attention to

$$
\widetilde x=az_1+(1-a)z_2.
$$

The weights sum to one, so the coefficient on the latent $x$ is one. Minimize the noise variance

$$
V(a)=a^2+3(1-a)^2.
$$

The first-order condition gives

$$
8a-6=0,
$$

so

$$
\boxed{
a=\frac34,\qquad
\widetilde x=\frac34z_1+\frac14z_2
}.
$$

This is inverse-noise-variance weighting. The combined noise variance is

$$
\mathrm{Var}(\widetilde u)
=\left(\frac34\right)^2
+3\left(\frac14\right)^2
=\frac34.
$$

Regressing $y$ on this combined but still noisy proxy yields

$$
\boxed{
\mathrm{plim}\hat\beta_{\widetilde x}
=\frac{2}{1+3/4}
=\frac87\approx1.143
}.
$$

Combining proxies reduces attenuation but does not eliminate it.

## General Covariance-Weighted Combination

For $k$ unbiased proxies

$$
z=x\mathbf1+u,\qquad \mathrm{Cov}(u)=R,
$$

the minimum-noise weights satisfying $\mathbf1^\top w=1$ are

$$
\boxed{
w^\star=\frac{R^{-1}\mathbf1}
{\mathbf1^\top R^{-1}\mathbf1}
}.
$$

This is the same covariance-weighting principle that appears in GLS, efficient GMM, mean-variance optimization, and Kalman filtering.

## Important Knowledge Points

- Measurement error in a regressor creates attenuation, not merely a larger standard error.
- A second proxy can be a valid IV only when its measurement error is independent of the first proxy's error and the outcome disturbance.
- IV consistency and IV precision are different questions.
- Averaging proxies improves signal-to-noise but generally does not remove errors-in-variables bias.
- With correlated proxy errors, use the full covariance matrix rather than scalar inverse-variance weights.

## Common Mistakes

- Assuming any second proxy is automatically a valid instrument.
- Ignoring correlated measurement errors $E[u_1u_2]\neq0$.
- Saying IV is unbiased without checking relevance and exclusion.
- Expecting the minimum-variance proxy combination to recover the structural slope exactly.
- Confusing the best linear proxy for $x$ with the IV estimator of $\beta$.

## Finance Connection

Dealer inventory, repo specialness, order flow, positioning surveys, and futures basis can all be noisy measures of latent demand or scarcity. Weak observed alpha may reflect noisy measurement rather than weak latent predictability.

## What to Remember

$$
\boxed{
\text{OLS attenuates; an independent second proxy can identify by IV; covariance weighting denoises.}
}
$$

## Interview drill — 2026-10-07 Q3

Source and assessment: [2026-10-07 Q3](../../DailyTests/2026-10-07.md#q3--measurement-error-robust-se-and-iv). The reference material below does not change that attempt’s recorded result.

### Question

The true model is $`y=\alpha+\beta x+\epsilon`$, but only $`z=x+u`$ is observed. Assume x, u, and epsilon are mutually independent, $`E[u]=E[\epsilon]=0`$, $`\mathrm{Var}(x)=4`$, $`\mathrm{Var}(u)=1`$, and $`\beta=0.5`$. Regress y on z with an intercept.

1. Derive the probability limit of the OLS slope from covariance divided by variance.
2. Is the bias toward or away from zero?
3. Would heteroskedasticity-robust standard errors fix it?
4. Under what conditions could an instrumental variable help?

### Recorded solution

```math
\mathrm{plim}\hat\beta
=\frac{\mathrm{Cov}(z,y)}{\mathrm{Var}(z)}
=\frac{\beta\mathrm{Var}(x)}
{\mathrm{Var}(x)+\mathrm{Var}(u)}
=\frac45\beta=0.4.
```

For an instrument W, state relevance and validity: it predicts the true x, is uncorrelated with both measurement error u and structural error epsilon, and affects y only through x. These conditions imply correlation with z and orthogonality to the observed-regression error $`\epsilon-\beta u`$.

### Related Notes

- [S006 — Two Noisy Proxies and Errors-in-Variables](S006_Two_Noisy_Proxies_and_Errors_in_Variables.md): attenuation and a valid second-proxy instrument.
- [S010 — OLS Significance, Randomness, and Robust Standard Errors](S010_OLS_Significance_Randomness_and_Robust_Standard_Errors.md): inference corrections versus endogeneity.

## Assessment history

- [2026-10-07 Q3 — assessment](../../DailyTests/2026-10-07.md#q3--measurement-error-robust-se-and-iv)

## Related questions and knowledge

- [S019 — Weighted Common-Mean Inference](S019_Weighted_Common_Mean_Inference.md) — Precision weighting of noisy observations.
