# P013 — Bayesian Gaussian Signal Fusion with Correlated Noise

## Metadata

- Category: Probability
- Secondary: Bayesian Statistics, Multivariate Normal Distributions, Signal Processing
- Difficulty: ★★★☆☆
- Tags: Gaussian Conjugacy, Correlated Noise, Posterior Predictive, Precision Weighting
- Review Priority: High
- Date Added: 2026-08-26
- Status: Final

## Core Question

Let

$$
\theta\sim N(0,1),
$$

and observe

$$
X=\mathbf1\theta+\varepsilon,
\qquad
\varepsilon\sim N(0,\Sigma_\varepsilon),
$$

where

$$
\Sigma_\varepsilon=
\begin{pmatrix}
1&0.5\\
0.5&2
\end{pmatrix},
\qquad
X=
\begin{pmatrix}
2\\-0.5
\end{pmatrix}.
$$

Find the posterior distribution of $\theta$, compute $P(\theta\gt0\mid X)$, and find $P(Z\gt1\mid X)$ for $Z=\theta+\eta$ with independent $\eta\sim N(0,1)$. Compare with a model that incorrectly treats the observation errors as independent.

## Hint

For prior variance $V_0=1$ and loading vector $\mathbf1$,

$$
V_1^{-1}=V_0^{-1}+\mathbf1^\top\Sigma_\varepsilon^{-1}\mathbf1,
$$

$$
m_1=V_1\mathbf1^\top\Sigma_\varepsilon^{-1}X.
$$

## Solution

The noise precision matrix is

$$
\Sigma_\varepsilon^{-1}
=\frac{1}{7/4}
\begin{pmatrix}
2&-1/2\\
-1/2&1
\end{pmatrix}
=\begin{pmatrix}
8/7&-2/7\\
-2/7&4/7
\end{pmatrix}.
$$

Therefore

$$
\mathbf1^\top\Sigma_\varepsilon^{-1}\mathbf1=\frac87
$$

and

$$
\mathbf1^\top\Sigma_\varepsilon^{-1}X=\frac{11}{7}.
$$

The posterior variance and mean are

$$
V_1=\left(1+\frac87\right)^{-1}=\frac7{15},
$$

$$
m_1=\frac7{15}\cdot\frac{11}{7}=\frac{11}{15}.
$$

Hence

$$
\boxed{\theta\mid X\sim N\left(\frac{11}{15},\frac7{15}\right)}.
$$

### Posterior Sign Probability

Standardizing the posterior,

$$
P(\theta\gt0\mid X)
=\Phi\left(\frac{11/15}{\sqrt{7/15}}\right)
\approx\boxed{0.86}.
$$

### Posterior Predictive Probability

Because $Z=\theta+\eta$ and $\eta$ is independent,

$$
Z\mid X\sim N\left(\frac{11}{15},1+\frac7{15}\right)
=N\left(\frac{11}{15},\frac{22}{15}\right).
$$

Thus

$$
P(Z\gt1\mid X)
=1-\Phi\left(
\frac{1-11/15}{\sqrt{22/15}}
\right)
\approx\boxed{0.41}.
$$

### Incorrect Independent-Errors Comparison

If one keeps the marginal noise variances $1$ and $2$ but sets their covariance to zero, then

$$
V_{\mathrm{ind}}
=\left(1+1+\frac12\right)^{-1}
=0.4,
$$

$$
m_{\mathrm{ind}}
=0.4\left(2+\frac{-0.5}{2}\right)
=0.7.
$$

Therefore

$$
\boxed{\theta\mid X,\text{ independent-error model}\sim N(0.7,0.4)}.
$$

The independent model reports a smaller variance because it treats positively correlated signals as containing more distinct information than they really do. That is overconfidence. In this numerical example the posterior mean also changes because correlation changes the optimal precision weights, not just the total precision.

## Intuition

Two signals that share noise partly repeat one another. Positive error correlation lowers their incremental combined information. The precision matrix automatically discounts the common component and can assign weights that differ sharply from inverse marginal-variance weights.

## Interview Takeaways

- Correlated Gaussian signals are combined with the full inverse covariance matrix.
- Posterior precision equals prior precision plus signal precision.
- Predictive variance includes both posterior parameter uncertainty and new observation noise.
- Ignoring positive correlation usually makes credible intervals too narrow.

## Finance / Market Application

Analyst revisions, alternative-data features, and related market indicators often share sources. Treating them as independent double-counts common information, exaggerates conviction, and can lead to excessive position sizing.

## What to Remember

$$
\boxed{
\theta\mid X\sim N\left(\frac{11}{15},\frac7{15}\right),
\quad
P(\theta\gt0\mid X)\approx0.86,
\quad
P(Z\gt1\mid X)\approx0.41
}.
$$
