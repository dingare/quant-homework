# P041 — Uniform Extremes: Ratio and Maximum Independence

## Metadata

- Category: Probability
- Tags: Order Statistics, Joint Density, Change of Variables, Independence, Conditional Expectation
- Date Added: 2026-11-08
- Original drill: November 8, Q2
- Status: Discussed with assistance; independent rederivation remains open. See the dated assessment for assistance and independently proposed steps.

## Core Question

Let U_1, ..., U_n be independent Uniform(0,1) random variables, where n is at least 2. Define:

```math
A=\min_i U_i,\qquad M=\max_i U_i,\qquad R=\frac AM.
```

1. Derive the joint density of R and M, including its support.
2. Are R and M independent? Justify your conclusion from your derivation.
3. Find the conditional expectation of A given M = m for m strictly between 0 and 1, and use it to obtain the unconditional expectation of A.

Derive the relevant distributions rather than quoting a named order-statistic formula. No code is required.

## Solution

### 1. Begin with the minimum and maximum jointly

For small disjoint intervals around a and m, select the sample responsible for the minimum in n ways and the sample responsible for the maximum in n minus one ways. Every other sample must lie between those endpoints. The leading small-rectangle probability is:

```math
P\bigl(A\in[a,a+da],\ M\in[m,m+dm]\bigr)
\approx n(n-1)(m-a)^{n-2}\,da\,dm.
```

Thus:

```math
f_{A,M}(a,m)=n(n-1)(m-a)^{n-2},\qquad 0\lt a\lt m\lt1,
```

and zero elsewhere. The approximation describes the leading density term, not a finite-interval identity. For n = 2 there are no remaining samples, so the interior power is zero and the joint density is 2 on the triangle.

### 2. Change coordinates and include the area factor

Use the inverse transformation:

```math
a=rm,\qquad m=m,\qquad
\left|\det\frac{\partial(a,m)}{\partial(r,m)}\right|
=\left|\det\begin{pmatrix}m&r\\0&1\end{pmatrix}\right|=m.
```

固定 m 时，a 随 r 放大 m 倍，所以小面积满足 da dm = m dr dm。密度必须乘上这个面积因子，才能保持同一区域的概率不变。代入得到：

```math
\begin{aligned}
f_{R,M}(r,m)
&=m f_{A,M}(rm,m)\\
&=n(n-1)m(m-rm)^{n-2}\\
&=n(n-1)m^{n-1}(1-r)^{n-2},
\qquad 0\lt r\lt1,\quad0\lt m\lt1.
\end{aligned}
```

The transformed support is a rectangle: the admissible range of r no longer depends on m.

### 3. Factorization and independence

```math
f_R(r)=(n-1)(1-r)^{n-2},\quad0\lt r\lt1,
\qquad f_M(m)=nm^{n-1},\quad0\lt m\lt1.
```

Both factors integrate to one on their supports, and:

```math
f_{R,M}(r,m)=f_R(r)f_M(m).
```

Therefore R and M are independent. A and M are dependent, but dividing A by the random scale M can remove that dependence. Checking only algebraic factorization is incomplete without also checking the support and normalization.

### 4. Conditional and unconditional expectations through R

The user independently proposed the conditional-mean representation below after independence had been explained:

```math
E[A\mid M=m]=mE[R\mid M=m]=mE[R].
```

For the ratio mean, substitute t = 1 minus r:

```math
\begin{aligned}
E[R]
&=(n-1)\int_0^1r(1-r)^{n-2}\,dr\\
&=(n-1)\int_0^1(1-t)t^{n-2}\,dt\\
&=(n-1)\left(\frac1{n-1}-\frac1n\right)=\frac1n.
\end{aligned}
```

```math
E[M]=n\int_0^1m^n\,dm=\frac{n}{n+1},
\qquad
\boxed{E[A\mid M=m]=\frac mn},
```

```math
\boxed{E[A]=E\bigl[E[A\mid M]\bigr]
=E[M]E[R]=\frac1{n+1}}.
```

Given the maximum value m, the other n minus one observations, after accounting for which observation attains the maximum, behave as independent Uniform(0,m) samples. Their minimum has expectation m divided by n. The displayed conditional expectations use the regular conditional law; they do not require the event M = m to have positive point probability.

### 5. Direct marginal method for the minimum

The user independently pointed out that the unconditional expectation can be computed directly from A's marginal distribution, without introducing R. This is correct; the R-based route above follows the requested conditional-expectation chain but is not necessary for the unconditional mean.

A exceeds a exactly when every sample exceeds a. Independence gives:

```math
P(A\gt a)=(1-a)^n,\qquad0\lt a\lt1,
```

```math
F_A(a)=\begin{cases}
0,&a\le0,\\
1-(1-a)^n,&0\lt a\lt1,\\
1,&a\ge1,
\end{cases}
\qquad
f_A(a)=n(1-a)^{n-1}\quad(0\lt a\lt1),
```

with density zero outside that interval. The maximum, by contrast, satisfies:

```math
F_M(m)=m^n,\qquad f_M(m)=nm^{n-1},\qquad0\lt m\lt1.
```

The minimum's density is flat when n = 1 and decreases toward the right for n at least 2; the maximum's density increases toward the right when n at least 2. This is a quick check against swapping the two densities.

Direct integration, with t = 1 minus a, gives:

```math
\begin{aligned}
E[A]
&=n\int_0^1a(1-a)^{n-1}\,da\\
&=n\int_0^1(1-t)t^{n-1}\,dt\\
&=n\left(\frac1n-\frac1{n+1}\right)=\frac1{n+1}.
\end{aligned}
```

The equivalent survival-integral check is:

```math
E[A]=\int_0^1P(A\gt a)\,da
=\int_0^1(1-a)^n\,da=\frac1{n+1}.
```

These are reference derivations; the user proposed the marginal route, but did not independently submit these density formulas or integral evaluations in this discussion.

## Common Mistakes

- Marginal densities alone do not determine a joint density. Do not multiply the marginals of A and M, which are dependent.
- Use the inverse transformation's Jacobian. Substitution alone misses the factor m.
- The original support is triangular, whereas the transformed support is rectangular. Both matter for independence.
- A wrong density expression does not, by itself, establish a misunderstanding of the independence criterion. Preserve the user's clarification in the dated record.
- The direct marginal method for E[A] is fully valid. It does not answer the separate conditional-expectation question by itself.

## Connections

- [Random Points, Order Statistics, and Spacings](../../KnowledgeCards/Probability/Random_Points_Order_Statistics_and_Spacings.md): extrema, boundary gaps and the minimum's mean.
- [P030 — Product Distribution and Event Conditioning](P030_Product_Distribution_and_Event_Conditioning.md): transformed densities and careful support tracking, with a different transformation and conditioning event.

## Assessment History

- [November 8 Q2](../../DailyTests/2026-11-08.md#q2--uniform-extremes-and-ratio): guided derivations, independently proposed conditional-mean representation and direct-marginal alternative, density-expression clarification, and the planned later independent rederivation.

## What to Remember

Choose who supplies the two extremes; constrain all remaining samples. For a coordinate change, write the inverse map, the area factor and the support. Independence must be checked in the new coordinates. The unconditional mean can also be obtained directly from the minimum's marginal law.
