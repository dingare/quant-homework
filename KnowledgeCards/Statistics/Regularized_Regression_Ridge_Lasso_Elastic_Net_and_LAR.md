# Regularized Regression: Ridge, Lasso, Elastic Net, and LAR

## Purpose and review status

- Category: Statistics
- Tags: Regularization, Ridge, SVD, Bias–Variance, Bayesian Prior, Effective Degrees of Freedom, Lasso, Elastic Net, Grouping Effect, LAR
- Date Added: 2026-10-26
- Source: User-requested synthesis of the “Ridge回归理解” discussion, with independently checked derivations and references for path and degrees-of-freedom claims. This is a synthesis, not a verbatim transcript.
- Status: Review reference; no new question attempt, rating, or mastery claim.

This card is a sibling of [OLS: Expectation, Variance, Residuals, and Prediction](OLS_Expectation_Variance_Residuals_and_Prediction.md). Use that card for the OLS sampling framework, residuals, and CI / PI derivations. [L001](../../Questions/LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md) contains the original Ridge / PCA question and assessment history; the SVD recap below connects it to regularization, prediction, and model complexity.

**Reading order:** Sections 1–6 explain Ridge; Sections 7–9 explain penalty geometry, Lasso, and Elastic Net; Sections 10–11 separate LAR paths from Lasso paths and their degrees of freedom.

| Method | Central idea | Complexity / path connection |
| --- | --- | --- |
| OLS | Minimize training squared error | Fully fit every identifiable direction |
| Ridge | Accept bias to reduce variance through smooth shrinkage | Each singular direction contributes fractional df |
| Lasso | Shrink coefficients and allow exact zeros | Active-set rank estimates fixed-lambda df |
| Elastic Net | Combine sparsity with an L2 cost for concentrated weights | Encourage stability among correlated substitutes |
| LAR / LARS-Lasso | Construct paths through equiangular moves | Distinguish entry steps from coefficient-drop events |

## 1. Setup, intercept, and penalty conventions

Start from the original model with an intercept and homoskedastic, uncorrelated errors. Hold the design fixed:

```math
\tilde y=\beta_0\mathbf 1+X\beta+\varepsilon,
\qquad E(\varepsilon\mid X)=0,
\qquad \mathrm{Cov}(\varepsilon\mid X)=\sigma^2 I_n.
```

Here $`X\in\mathbb R^{n\times p}`$ has centered feature columns, and $`p`$ counts **slopes only**. Define $`C=I_n-\mathbf1\mathbf1^\top/n`$ and $`y=C\tilde y`$. Then $`y=X\beta+C\varepsilon`$, and the intercept estimate is $`\bar{\tilde y}`$. In raw feature coordinates it is $`\bar{\tilde y}-\bar x^\top\hat\beta`$. The intercept is unpenalized.

The centered errors have covariance $`\sigma^2C`$, not $`\sigma^2I_n`$. Because $`X^\top C=X^\top`$, the slope covariance formulas below still have their usual form. Add one to slope degrees of freedom when restoring the estimated intercept. **The sibling OLS card counts the intercept inside its parameter count; this card does not.**

Use these objective functions consistently:

```math
\begin{aligned}
Q_R(\beta)&=\tfrac12\|y-X\beta\|_2^2+\tfrac\lambda2\|\beta\|_2^2,\\
Q_L(\beta)&=\tfrac12\|y-X\beta\|_2^2+\lambda_1\|\beta\|_1,\\
Q_{EN}(\beta)&=\tfrac12\|y-X\beta\|_2^2
+\lambda_1\|\beta\|_1+\tfrac{\lambda_2}{2}\|\beta\|_2^2.
\end{aligned}
```

All penalties are nonnegative. Ridge uses $`\lambda\gt0`$; a positive $`\lambda_2`$ makes Elastic Net strictly convex even if the design is rank deficient. Another common parameterization is $`\lambda_1=\lambda\alpha`$, $`\lambda_2=\lambda(1-\alpha)`$, with $`0\le\alpha\le1`$. Its endpoints are Lasso and Ridge.

Some software divides the squared-error term by $`n`$. Multiplying that entire objective by $`n`$ multiplies its penalty parameters by $`n`$ in the convention here. Check the factors of two as well; a numerical lambda is meaningless without the objective definition.

Standardize feature scales using training data before comparing penalized coefficients: a coefficient's size depends on the feature's units. Apply those same transformations to validation and new observations. Ridge is invariant under orthogonal rotations of the chosen feature coordinates, but not arbitrary rescaling; Lasso sparsity depends on the coordinate system.

## 2. Ridge versus OLS: what changes algebraically?

Differentiating the Ridge objective gives:

```math
-X^\top(y-X\hat\beta_R)+\lambda\hat\beta_R=0,
\qquad
\boxed{\hat\beta_R=(X^\top X+\lambda I_p)^{-1}X^\top y.}
```

OLS uses the same formula without $`\lambda I_p`$ when $`X`$ has full column rank. Ridge exists uniquely even without full rank because, for every nonzero $`v`$,

```math
v^\top(X^\top X+\lambda I_p)v
=\|Xv\|_2^2+\lambda\|v\|_2^2\gt0.
```

Write $`G=X^\top X`$. For the identifiable full-rank case:

```math
\begin{aligned}
\hat\beta_{OLS}&=\beta+G^{-1}X^\top\varepsilon,\\
\hat\beta_R-\beta
&=-\lambda(G+\lambda I_p)^{-1}\beta
+(G+\lambda I_p)^{-1}X^\top\varepsilon.
\end{aligned}
```

OLS is conditionally unbiased under the mean assumption. Ridge deliberately introduces a bias term; it does not repair endogeneity or omitted-variable bias. Multicollinearity alone makes OLS unstable without making it biased; see [S001](../../Questions/Statistics/S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md).

OLS minimizes training RSS, so Ridge cannot improve that minimum RSS on the same design. Ridge is used to improve estimation or future prediction by controlling variance. It need not outperform OLS on every dataset or for every true coefficient vector.

## 3. SVD: coefficient shrinkage and fitted-value shrinkage

Use a compact SVD with rank $`r`$:

```math
X=UDV^\top,\qquad
U^\top U=V^\top V=I_r,\qquad
D=\mathrm{diag}(d_1,\ldots,d_r),\quad d_j\gt0.
```

The columns $`v_j`$ describe feature combinations; $`u_j`$ describe observation-space directions. The eigenvalues of $`X^\top X`$ on its row space are $`d_j^2`$. The scores for feature direction $`v_j`$ are $`Xv_j=d_j u_j`$.

```math
\begin{aligned}
\hat\beta_{OLS}^{+}
&=\sum_{j=1}^r \frac{u_j^\top y}{d_j}v_j,\\
\hat\beta_R
&=\sum_{j=1}^r\frac{d_j}{d_j^2+\lambda}(u_j^\top y)v_j,\\
s_j&=\frac{d_j^2}{d_j^2+\lambda},\qquad
\hat\theta_{R,j}=s_j\hat\theta_{OLS,j},
\quad \theta_j=v_j^\top\beta.
\end{aligned}
```

The superscript plus means the minimum-norm OLS solution; it is ordinary OLS when full rank holds. Ridge sets coefficient components in the null space of $`X`$ to zero. Those components cannot be learned from the training responses.

Small $`d_j`$ means weak information about a coefficient direction: OLS divides by a small number and amplifies noise. Ridge shrinks that direction strongly. Large $`d_j^2`$ relative to lambda gives $`s_j\approx1`$; small $`d_j^2`$ gives $`s_j\approx0`$.

Multiplying by $`X`$ removes the inverse singular value from the OLS **training fit**:

```math
\begin{aligned}
\hat y_{OLS}&=UU^\top y,\\
\hat y_R&=S_\lambda y,\qquad
S_\lambda=U\,\mathrm{diag}(s_j)U^\top,\\
\hat y_R&=\sum_{j=1}^r s_j u_j(u_j^\top y).
\end{aligned}
```

Thus unstable coefficients do not automatically imply equally unstable predictions at the training design. New observations can expose the unstable feature combinations; Section 4 makes this explicit.

Ridge shrinks each singular-direction coefficient, not each original coefficient independently by the same factor. After rotating back, an individual original coefficient can increase in magnitude or change sign. The total coefficient norm is no larger than that of minimum-norm OLS. Principal component regression makes a hard keep/drop choice of directions; Ridge uses smooth weights. Neither ranks directions by their true predictive signal merely from the singular values.

## 4. Bias, variance, and prediction: separate the targets

For a full-rank design and fixed lambda, with expectations over repeated errors:

```math
\begin{aligned}
E(\hat\beta_R\mid X)&=(G+\lambda I_p)^{-1}G\beta,\\
\mathrm{Bias}(\hat\beta_R\mid X)&=-\lambda(G+\lambda I_p)^{-1}\beta,\\
\mathrm{Cov}(\hat\beta_R\mid X)
&=\sigma^2(G+\lambda I_p)^{-1}G(G+\lambda I_p)^{-1}.
\end{aligned}
```

In singular direction $`j`$:

```math
\begin{aligned}
\mathrm{Bias}(\hat\theta_{R,j})&=-\frac{\lambda}{d_j^2+\lambda}\theta_j,\\
\mathrm{Var}(\hat\theta_{R,j})&=\frac{\sigma^2d_j^2}{(d_j^2+\lambda)^2}
=s_j^2\frac{\sigma^2}{d_j^2},\\
\mathrm{MSE}(\hat\theta_{R,j})
&=\frac{\lambda^2\theta_j^2+\sigma^2d_j^2}{(d_j^2+\lambda)^2}.
\end{aligned}
```

The OLS variance is $`\sigma^2/d_j^2`$. Ridge lowers variance in every identifiable singular direction. MSE also includes squared bias, so variance reduction alone does not prove a better estimator. Under rank deficiency, a true coefficient component outside the row space contributes additional squared bias.

For the centered training mean $`m=X\beta`$:

```math
\begin{aligned}
E(\hat y_R\mid X)-m&=(S_\lambda-I_n)m,\\
\mathrm{Cov}(\hat y_R\mid X)&=\sigma^2S_\lambda^2,\\
E\|\hat y_R-m\|_2^2
&=\sum_{j=1}^r\left[(1-s_j)^2d_j^2\theta_j^2+\sigma^2s_j^2\right].
\end{aligned}
```

This is error in estimating the **training mean**, not training RSS and not future-observation error. The intercept contributes a separate mean-estimation variance when restored.

For a fixed new feature vector $`x_0`$ centered using the training feature means, the slope part of the prediction is:

```math
\hat m_{0,R}^{\mathrm{slope}}
=x_0^\top\hat\beta_R
=\sum_{j=1}^r(x_0^\top v_j)
\frac{d_j}{d_j^2+\lambda}(u_j^\top y).
```

When full rank holds, its conditional variance is:

```math
\mathrm{Var}(x_0^\top\hat\beta_R\mid X,x_0)
=\sigma^2\sum_{j=1}^p(x_0^\top v_j)^2
\frac{d_j^2}{(d_j^2+\lambda)^2}.
```

The OLS summand replaces the final factor by $`1/d_j^2`$. Predictions become sensitive when the new vector has a substantial component in a weak training direction. For full prediction, restore $`\bar{\tilde y}`$; its variance is $`\sigma^2/n`$ and its covariance with the slope prediction is zero under the stated covariance model.

If a future response has an independent error with variance $`\sigma^2`$ and the same conditional-mean model, its prediction MSE is squared mean-prediction bias plus mean-estimation variance plus $`\sigma^2`$. Lower coefficient variance is not a guarantee of lower prediction MSE under distribution shift.

## 5. Bayesian interpretation: a Gaussian prior produces Ridge

Add a Gaussian likelihood and independent isotropic Gaussian prior for the slopes. Let the columns of $`Q\in\mathbb R^{n\times(n-1)}`$ be an orthonormal basis for the centered subspace, and write $`y_*=Q^\top y`$ and $`X_*=Q^\top X`$:

```math
y_*\mid\beta\ \sim\ N(X_*\beta,\sigma^2I_{n-1}),
\qquad \beta\sim N(0,\tau^2I_p).
```

This avoids treating demeaning as if it left independent errors in all original observation coordinates. Since $`\|y_*-X_*\beta\|_2^2=\|y-X\beta\|_2^2`$, take the noise and prior scales as fixed and write the negative log posterior, up to constants, as:

```math
\frac{\|y-X\beta\|_2^2}{2\sigma^2}
+\frac{\|\beta\|_2^2}{2\tau^2}.
```

Multiplication by $`\sigma^2`$ gives the Ridge objective with:

```math
\boxed{\lambda=\frac{\sigma^2}{\tau^2}},\qquad
\beta\mid y,X\sim N(\hat\beta_R,V_{\mathrm{post}}),\qquad
V_{\mathrm{post}}=\sigma^2(G+\lambda I_p)^{-1}.
```

The Gaussian posterior mean and mode coincide, so both equal Ridge. A smaller prior variance expresses stronger preference for small coefficients; larger noise relative to prior scale increases shrinkage. A prior $`N(b_0,\tau^2I_p)`$ instead pulls toward $`b_0`$:

```math
E(\beta\mid y,X)
=(G+\lambda I_p)^{-1}(X^\top y+\lambda b_0).
```

The posterior covariance is **not** the frequentist sampling covariance in Section 4. One conditions on observed data and describes uncertainty about beta under the prior; the other holds the true beta fixed and repeats the data. A zero-mean prior does not assert that the true coefficients must be zero. Regularization strength chosen by cross-validation also need not be interpreted as a literal subjective prior.

An independent Laplace prior produces the Lasso objective for the posterior **mode**, with the matching scale convention. The Lasso estimate is generally not the posterior mean, and a continuous Laplace prior does not itself put positive prior probability on exact zeros.

## 6. Effective degrees of freedom: how responsive is the fit?

For a fitted-mean rule $`\hat\mu(\tilde y)`$, define fitting degrees of freedom by covariance with the observations, holding the design and tuning parameters fixed:

```math
\mathrm{df}(\hat\mu)
=\frac1{\sigma^2}\sum_{i=1}^n
\mathrm{Cov}(\hat\mu_i,\tilde y_i\mid X).
```

For a fixed linear smoother $`\hat\mu=H\tilde y`$, this is $`\mathrm{tr}(H)`$. Intuitively, a fitted value that follows a perturbation in the observed responses more strongly uses more flexibility. This measures the behavior of the fitted values, not the number of stored coefficients.

For Ridge slopes:

```math
\boxed{\mathrm{df}_R^{\mathrm{slope}}(\lambda)
=\mathrm{tr}(S_\lambda)
=\sum_{j=1}^r\frac{d_j^2}{d_j^2+\lambda}.}
```

Each direction contributes between zero and one. For example, $`d_1^2=100`$, $`d_2^2=1`$, and $`\lambda=1`$ give $`100/101+1/2\approx1.49`$ slope df, although both coefficients can be nonzero. As lambda tends to zero the slope df tends to rank $`r`$; as lambda tends to infinity it tends to zero. The estimated unpenalized intercept adds one.

### Fitting df is not an automatic residual-variance denominator

Let $`H=\mathbf1\mathbf1^\top/n+S_\lambda`$ be the full smoother and $`\mu=E(\tilde y\mid X)`$ the original mean. Direct expansion yields:

```math
E\|\tilde y-H\tilde y\|_2^2
=\|(I_n-H)\mu\|_2^2
+\sigma^2\left[n-2\mathrm{tr}(H)+\mathrm{tr}(H^\top H)\right].
```

OLS has an idempotent projection matrix and zero mean residual when correctly specified, giving the familiar denominator $`n-\mathrm{rank}(H)`$. Ridge generally has neither property. Dividing RSS by $`n-\mathrm{df}_R`$ is therefore not a general unbiased error-variance estimator. Even the displayed noise coefficient does not remove the squared-bias term. Do not reuse the exact OLS t intervals solely by substituting effective df.

## 7. Lq penalty geometry: why a larger q looks more square

For a two-coefficient picture, fix the axis intercepts through the unit constraint:

```math
B_q=\{(b_1,b_2):|b_1|^q+|b_2|^q\le1\},\qquad q\gt0.
```

For $`q\ge1`$ this is an Lq norm ball. For $`0\lt q\lt1`$ the same expression defines a nonconvex region, not a norm ball.

| q | Two-dimensional shape | Consequence for sparse solutions |
| --- | --- | --- |
| Approaches zero from above | Strongly pinched toward the axes | Strong sparsity preference; nonconvex optimization |
| 1 | Diamond with corners on the axes | Corners can produce exact zeros |
| Between 1 and 2 | Rounded diamond | Differentiable at an axis; no generic threshold interval |
| 2 | Circle | Smooth shrinkage; generally no exact zeros |
| Greater than 2 | Rounded square | Allows relatively larger simultaneous coordinates |
| Tends to infinity | Axis-aligned square | Equivalent limiting bound on the largest absolute coefficient |

On the diagonal $`b_1=b_2=t\ge0`$, the boundary satisfies:

```math
2t^q=1\quad\Longrightarrow\quad t=2^{-1/q}\longrightarrow1.
```

The axis intercept stays at one, while the diagonal boundary moves outward toward the corner $`(1,1)`$. More generally $`\|b\|_q\to\max_j|b_j|`$, so the limiting unit region is a square in two dimensions and a cube in higher dimensions. The picture depends on fixing the constraint scale; comparing unrelated radii would be misleading.

For nonzero fixed coefficients, $`\sum_j|b_j|^q`$ approaches the number of nonzero entries as $`q\downarrow0`$. This is a pointwise connection to the L0 count; it is not a claim that L0 is a norm or that a chosen optimization algorithm must converge to best-subset selection.

In the constrained formulation, expand the penalty region until a squared-error contour first touches it. Axis corners make a zero coordinate possible over a range of responses. A square also has corners, but its corners have **both** coordinates nonzero. Thus “more square” does not mean “more sparse.”

For the penalty $`\sum_j|b_j|^q`$, its one-coordinate derivative away from zero is $`q\,\mathrm{sign}(b_j)|b_j|^{q-1}`$. It tends to zero at the origin for $`q\gt1`$, has a subgradient interval for $`q=1`$, and has unbounded magnitude near zero for $`0\lt q\lt1`$. This explains why smooth penalties usually shrink without thresholding, while L1 creates exact zeros. A zero remains possible for a smooth penalty in special data configurations.

## 8. Lasso: exact zeros come from the KKT condition

Let $`r=y-X\hat\beta_L`$. The optimality condition for the convex Lasso problem is:

```math
X^\top r=\lambda_1 z,\qquad
z_j=\begin{cases}
\mathrm{sign}(\hat\beta_{L,j}),&\hat\beta_{L,j}\ne0,\\
\text{any value in }[-1,1],&\hat\beta_{L,j}=0.
\end{cases}
```

An inactive feature can remain at zero whenever its absolute residual correlation is at most lambda. An active feature has residual correlation equal to lambda in its coefficient's sign. This threshold region is the algebra behind the diamond's corners.

For orthonormal feature columns $`X^\top X=I_p`$, set $`z_j=x_j^\top y`$. The coordinates separate:

```math
\hat\beta_{R,j}=\frac{z_j}{1+\lambda},\qquad
\hat\beta_{L,j}=\mathrm{sign}(z_j)(|z_j|-\lambda_1)_+,
\qquad (a)_+=\max(a,0).
```

For orthogonal columns with squared norm $`a_j`$, the Lasso expression is instead $`\mathrm{sign}(z_j)(|z_j|-\lambda_1)_+/a_j`$. General correlated designs do not allow independent soft-thresholding of the OLS coefficients.

Lasso combines selection and shrinkage. Strongly correlated features can substitute for each other, so small data changes can change which feature is selected. This does not mean it always chooses exactly one feature per correlated group, or that a selected feature is causally important. Exact duplicate columns can give nonunique coefficients, although the squared-loss fitted values remain unique.

## 9. Elastic Net and the grouping effect

Elastic Net keeps the L1 threshold and adds an L2 cost for concentrating weight. With $`r=y-X\hat\beta_{EN}`$, its KKT condition is:

```math
X^\top r=\lambda_1 z+\lambda_2\hat\beta_{EN}.
```

Suppose features $`i`$ and $`j`$ have active coefficients of the same sign. Subtract their two equations:

```math
\lambda_2(\hat\beta_i-\hat\beta_j)=(x_i-x_j)^\top r,
\qquad
|\hat\beta_i-\hat\beta_j|
\le\frac{\|x_i-x_j\|_2\|r\|_2}{\lambda_2}.
```

If the centered columns have unit norm and correlation $`\rho`$, then $`\|x_i-x_j\|_2=\sqrt{2(1-\rho)}`$. Similar columns therefore encourage similar coefficients when the same-sign condition holds and $`\lambda_2\gt0`$. This is a tendency with explicit conditions, not a guarantee that every correlated group enters together. For negative correlation, first reverse one feature's sign to interpret the analogous relationship. See [Zou and Hastie (2005)](https://doi.org/10.1111/j.1467-9868.2005.00503.x) for the original grouping analysis.

### Identical-feature example

Let $`x_1=x_2=x`$ and fix the combined coefficient $`c=b_1+b_2\gt0`$. The prediction depends only on $`c`$.

```math
\begin{aligned}
|b_1|+|b_2|&=c\quad\text{for every nonnegative split},\\
b_1^2+b_2^2&=\frac{c^2}{2}+\frac{(b_1-b_2)^2}{2}.
\end{aligned}
```

Lasso is indifferent among these splits. Ridge and Elastic Net with positive L2 penalty uniquely prefer $`b_1=b_2=c/2`$. For nearly identical columns, the L2 term discourages unstable transfers of weight between substitutes. Elastic Net does not require predeclared groups; group lasso is a different penalty designed for explicit groups.

This card uses the common penalized-objective definition in Section 1. The original Elastic Net paper also distinguishes that fit from a subsequently rescaled estimator; do not mix their coefficient formulas or tuning conventions.

## 10. What LAR does, and how the Lasso path differs

**LAR means least angle regression.** LARS names the path-building algorithm family. Ordinary LAR and the LARS modification that computes the Lasso path are related procedures with different continuation rules.

Start with centered, comparably scaled predictors and zero coefficients. Choose the feature most correlated with the residual; move its coefficient toward its least-squares fit. Stop when another feature ties in absolute residual correlation. Continue in an equiangular direction for the signed active columns, maintaining equal signed correlations until the next event. Ordinary LAR keeps the entered columns in its active set under the usual nondegenerate construction.

To trace the Lasso path, add a **drop rule**: if an active coefficient reaches zero before the next entry, stop there and remove it before continuing. Otherwise proceeding could violate the Lasso KKT sign condition. A dropped variable can re-enter later. The paths agree while the drop rule is unnecessary; under suitable design conditions they agree throughout. This relationship is established in [Efron et al. (2004)](https://doi.org/10.1214/009053604000000067).

| Feature | Ordinary LAR path | LARS-Lasso path |
| --- | --- | --- |
| Main construction | Equiangular moves among entered predictors | Equiangular moves plus coefficient-drop events |
| Must solve the Lasso objective everywhere? | No | Yes, with the Lasso modification and usual handling of degeneracies |
| Coefficient reaching zero | No mandatory Lasso drop rule | Drop; possible later re-entry |
| Path event count | Often indexed by successive additions | Entries and drops; can exceed final model size |

Neither procedure is forward stepwise regression, which refits the selected model fully at each addition. Ties and dependent columns require care; do not assume one uniquely entering variable per event for every design.

## 11. LAR versus Lasso degrees of freedom

### First fix what is being held constant

The covariance definition in Section 6 applies to both. For nonlinear fitted-mean rules, under Gaussian errors and the regularity conditions for Stein's identity:

```math
\mathrm{df}(\hat\mu)
=E\left[\sum_{i=1}^n\frac{\partial\hat\mu_i}{\partial\tilde y_i}\right].
```

An observed divergence can estimate df; theoretical df is an expectation over new responses. Counts such as active-set size are random when the selected model depends on those responses. Parameter count, number of algorithm steps, and fitting df are different concepts.

### Ridge: fractional contributions from all directions

With fixed lambda, slope df is exactly $`\sum_j s_j`$. Nonzero coefficient count does not measure its complexity well because most coefficients remain nonzero while the response to noise is reduced.

### Lasso: active-set rank at fixed lambda

Take $`\lambda_1\gt0`$ fixed independently of the responses and $`\tilde y\sim N(\mu,\sigma^2 I_n)`$. Let $`A=\{j:\hat\beta_{L,j}\ne0\}`$. Locally, where the active set and signs stay unchanged and its columns are independent:

```math
\hat\beta_A=(X_A^\top X_A)^{-1}(X_A^\top y-\lambda_1 z_A),
\qquad
\frac{\partial(X_A\hat\beta_A)}{\partial y}
=X_A(X_A^\top X_A)^{-1}X_A^\top.
```

The shrinkage term is locally constant in the responses. The derivative is a projection with trace equal to active-set rank. More generally, even with arbitrary fixed designs:

```math
\boxed{\mathrm{df}_L^{\mathrm{slope}}(\lambda_1)
=E[\mathrm{rank}(X_A)].}
```

If the active columns are independent, this becomes $`E[|A|]`$, and the observed nonzero count is an unbiased df estimate. With dependent columns or nonunique coefficients, raw nonzero count can overcount the fit; the rank result is the robust statement. See [Tibshirani and Taylor (2012), Theorem 2](https://arxiv.org/abs/1111.0653).

This does not make the fitted coefficients equal to an OLS refit on the selected variables. Lasso still shrinks them; the result concerns sensitivity of fitted values and an expectation over selection. Refitting OLS after selection changes the fitted-mean rule and can add search complexity.

### LAR: the familiar k-step rule needs its conditions

The usual summary is that a LAR fit after $`k`$ steps has about $`k`$ slope df. In the original LARS analysis, equality is proved under the **positive cone condition**; this holds for orthogonal designs but not all designs. Outside it, the step count is a useful approximation, not a universal theorem. See [Efron et al. (2004), Section 4 and Theorem 4](https://doi.org/10.1214/009053604000000067).

Step 0 is the zero slope fit; in the nondegenerate indexing, the first completed move has one nonzero coefficient. Do not count a newly tied predictor with coefficient still zero as an additional completed coefficient fit. Nor should the count be interpreted as $`k`$ independent observations consumed: it measures aggregate sensitivity to the responses.

### Are LAR and Lasso df the same?

**Not as a blanket statement.** Their paths can differ, and they are often indexed differently. For LAR, $`k`$ indexes algorithmic progress with the qualifications above. For fixed-lambda Lasso, active-set rank estimates df; a history of additions and drops does not. The numerical summaries can coincide in settings where the paths coincide and the parameterization is matched.

The fixed-lambda theorem cannot automatically be applied after choosing lambda from the same responses by cross-validation, nor after evaluating at a response-dependent path knot or choosing a step by searching the path. Those are different fitted-mean rules. Add one throughout when the unpenalized intercept is estimated.

## 12. Retrieval checklist and practical use

| Prompt | Answer to retrieve |
| --- | --- |
| Why can Ridge help when OLS is unbiased? | MSE includes variance; shrinking weak directions can reduce it enough to offset squared bias. |
| Why are predictions sometimes stable despite unstable OLS coefficients? | Training predictions project onto the column space; a new feature vector's alignment with weak directions determines its exposure. |
| Does Ridge shrink every original coefficient by one common multiplier? | No; its simple multipliers act in the singular-vector basis. |
| Why does a Gaussian prior give Ridge? | Negative log likelihood plus negative log prior gives squared error plus an L2 penalty. |
| Why is Ridge df smaller than the number of coefficients? | Each singular direction follows the responses only fractionally. |
| Why does L1 create zeros? | Its subgradient at zero accepts an interval of residual correlations. |
| Why does larger q look more square? | Axis intercepts stay fixed while diagonal coordinates approach one. |
| Why does Elastic Net group correlated features? | Its L2 term penalizes concentrating a shared prediction weight in one interchangeable feature. |
| What changes LAR into a Lasso path algorithm? | Drop a coefficient when it reaches zero; allow later re-entry. |
| Is Lasso df the number of path steps? | No; use active-set rank at fixed lambda, with expectation for theoretical df. |

For many weak, correlated signals and a prediction objective, Ridge is a natural candidate. For an explicit sparse representation, consider Lasso; Elastic Net is a candidate when sparsity and correlated-feature stability both matter. Compare them using validation appropriate to the prediction task rather than assuming a universal winner. For time series, fit preprocessing and tune penalties inside chronological training folds; see [T007](../../Questions/TimeSeries/T007_Random_Forest_Rates_Signals_and_Time_Series_Validation.md).

## Related notes and references

- [OLS knowledge card](OLS_Expectation_Variance_Residuals_and_Prediction.md): repeated sampling, exact OLS inference, and mean versus observation prediction.
- [L001 — Ridge as PCA shrinkage](../../Questions/LinearAlgebra/L001_Ridge_Regression_as_PCA_Shrinkage.md): original SVD derivation and related drill records.
- [SVD, QR, Conditioning, Least Squares, and PCA](../LinearAlgebra/SVD_QR_Conditioning_Least_Squares_and_PCA.md): decomposition foundations and stable computation.
- [S001 — OLS bias versus variance](../../Questions/Statistics/S001_OLS_Bias_vs_Variance_with_Correlated_Regressors.md): multicollinearity versus omitted-variable bias.
- [Hastie, Tibshirani, and Friedman, The Elements of Statistical Learning, Chapter 3](https://hastie.su.domains/ElemStatLearn/main.html): regularization and linear-model background.
- [Efron, Hastie, Johnstone, and Tibshirani (2004), Least Angle Regression](https://doi.org/10.1214/009053604000000067): LAR, the Lasso modification, and the qualified step-count df result.
- [Zou and Hastie (2005), Regularization and Variable Selection via the Elastic Net](https://doi.org/10.1111/j.1467-9868.2005.00503.x): grouping effect and original estimator conventions.
- [Tibshirani and Taylor (2012), Degrees of Freedom in Lasso Problems](https://arxiv.org/abs/1111.0653): fixed-lambda df for general design matrices.
