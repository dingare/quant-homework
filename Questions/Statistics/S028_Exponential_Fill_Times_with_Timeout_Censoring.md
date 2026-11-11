# S028 — Exponential Fill Times with Timeout Censoring

## Metadata

- Category: Statistics
- Tags: Likelihood, Censoring, Estimation, Fisher Information
- Date Added: 2026-11-11
- Original drill: November 10, 2026, Q3.
- Status: Discussed; full reference and expected-versus-observed information distinction recorded. Dated independent/assisted evidence is linked below.

## Core Question

You study the time required to fill an order. For independent orders, the latent fill times have density

```math
f(t;\lambda)=\lambda e^{-\lambda t},\qquad t\geq0,\quad\lambda\gt0.
```

Every order is canceled at a fixed, known timeout $`c\gt0`$ if it has not filled. For each of n orders you observe only

```math
Y_i=\min(T_i,c),\qquad \delta_i=\mathbf 1\{T_i\leq c\}.
```

Assume this model is correct and orders do not affect one another.

1. Construct the likelihood from the actual observations and derive the maximum-likelihood estimate of lambda. Address the case in which no orders fill.
2. Derive the expected Fisher information and a plug-in large-sample standard error. Explain how the timeout affects precision.
3. A colleague discards canceled orders and estimates lambda as the reciprocal of the average completed fill time. Is this consistent for lambda? If not, determine the direction of the distortion.

Keep the answer interview-length; no code is required.

## Solution

### Full likelihood and rate estimate

Write $`D=\sum_i\delta_i`$ for the number of fills and $`S=\sum_iY_i`$ for total observed time. The user correctly proposed the single-order likelihood contribution in its additive form:

```math
L_i(\lambda)=(1-\delta_i)e^{-\lambda c}
+\delta_i\lambda e^{-\lambda Y_i}.
```

The unfilled branch contributes a survival probability; the filled branch contributes the density at the observed time. Since an unfilled order has $`Y_i=c`$, this has the equivalent compact representation

```math
L_i(\lambda)=\lambda^{\delta_i}e^{-\lambda Y_i}.
```

The additive expression is correct. Using the binary indicator to select its active branch makes the product likelihood and logarithm simpler:

```math
L(\lambda)=\lambda^D e^{-\lambda S},\qquad
\ell(\lambda)=D\log\lambda-\lambda S.
```

For $`D\gt0`$ and positive total observation time,

```math
\ell'(\lambda)=\frac D\lambda-S,\qquad
\hat\lambda=\frac DS,\qquad
\ell''(\lambda)=-\frac D{\lambda^2}\lt0.
```

The rate estimate is fills divided by total observed order time, including the timeout duration of every unfilled order. If no orders fill, $`S=nc`$ and the likelihood decreases with lambda. Its supremum occurs as $`\lambda\downarrow0`$; the strictly positive parameter space has no attained MLE. Allowing the boundary gives estimate zero.

### Using only fill indicators

The user's first approach correctly identified

```math
D\sim\mathrm{Binomial}(n,p),\qquad p=1-e^{-\lambda c},\qquad
\hat p=\frac Dn.
```

This is the binomial MLE for the coarsened data containing only fill indicators. The question observes actual fill times as well, so the full-data likelihood above uses additional information. Do not label the binomial construction intrinsically invalid.

### Expected Fisher information and plug-in standard error

Under the usual regularity conditions, expected information for the full sample is negative expected log-likelihood curvature:

```math
I_n(\lambda)
=-E_\lambda[\ell''(\lambda)]
=E_\lambda[(\ell'(\lambda))^2].
```

Independent identical observations give $`I_n=nI_1`$. Here

```math
E[D]=n(1-e^{-\lambda c}),\qquad
I_n(\lambda)=\frac{n(1-e^{-\lambda c})}{\lambda^2}.
```

The regular interior large-sample approximation and expected-information plug-in standard error are

```math
\mathrm{Var}(\hat\lambda)\approx
\frac{\lambda^2}{n(1-e^{-\lambda c})},\qquad
\widehat{\mathrm{SE}}_{\mathrm{exp}}
=\frac{\hat\lambda}{\sqrt{n(1-e^{-\hat\lambda c})}}.
```

For fixed sample size and true rate, increasing the timeout increases information and decreases this approximate estimator variance. As the timeout tends to infinity, the variance approximation approaches $`\lambda^2/n`$, the complete-observation result. The parameter is fixed and unknown; it is the estimator whose sampling variance is being discussed.

### Observed information also gives a usable standard error

Retaining the actual count D gives the observed information for this sample:

```math
J_n(\lambda)=-\ell''(\lambda)=\frac D{\lambda^2},\qquad
\widehat{\mathrm{SE}}_{\mathrm{obs}}=\frac{\hat\lambda}{\sqrt D}.
```

Expected information averages that curvature across repeated samples at fixed lambda. Using D is valid for the observed-information route; taking its expectation is required by the definition of expected information, not a requirement for every standard-error estimate. Since $`D/n`$ approaches $`1-e^{-\lambda c}`$, the two plug-in standard errors are asymptotically equivalent but need not agree in finite samples. The no-fill boundary case does not support these ordinary interior normal approximations.

### Discarding canceled orders

Completed orders are selected from the conditional distribution of T given a fill before c. They have a shorter mean time:

```math
E[T\mid T\leq c]\lt E[T]=\frac1\lambda.
```

Therefore the reciprocal completed-time average converges to the wrong, higher rate:

```math
\frac1{\overline T_{\mathrm{completed}}}
\xrightarrow{p}\frac1{E[T\mid T\leq c]}\gt\lambda.
```

Selection shortens the mean duration; taking its reciprocal raises the estimated rate. The selected quantity is the duration T, not the fixed rate parameter.

## Connections

- [S011 — Exponential MLE and Fisher Information](S011_Exponential_MLE_and_Fisher_Information.md): the complete-observation foundation; this note adds timeout censoring and distinguishes expected from observed information.

## Assessment History

- [November 10 Q3, continuation November 11](../../DailyTests/2026-11-10.md#q3--fill-times-with-timeout-censoring): Partial / Hinted; valid indicator-only proposal and correct additive likelihood, independent timeout-precision direction, recalled Fisher definition with assistance, and supplied reciprocal-bias correction. Formula display requested for checking/typing convenience does not itself establish inability to derive.
