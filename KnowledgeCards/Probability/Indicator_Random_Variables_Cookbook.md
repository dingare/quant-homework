# Indicator Random Variables Cookbook

## Purpose

Indicator variables turn counting questions into sums of simple Bernoulli random
variables. The central workflow is:

$$
\text{define events}
\longrightarrow
\text{write a count as a sum}
\longrightarrow
\text{compute marginal and joint probabilities}
\longrightarrow
\text{classify overlap types}.
$$

This method applies to fixed points, inversions, collisions, occupied boxes, runs,
graph motifs, and many other quant-interview probability problems.

## 1. Definition

For an event $A$, define

$$
I_A=\mathbf 1_A=
\begin{cases}
1,&A\text{ occurs},\\
0,&A\text{ does not occur}.
\end{cases}
$$

The fundamental identity is

$$
E[I_A]=P(A).
$$

Also, because $I_A^2=I_A$,

$$
Var(I_A)=P(A)[1-P(A)].
$$

## 2. Turn a Count into a Sum

If $X$ counts how many objects satisfy a property, define one indicator per
candidate object:

$$
I_i=\mathbf 1\{\text{object }i\text{ satisfies the property}\},
\qquad
X=\sum_i I_i.
$$

Then linearity of expectation gives

$$
E[X]=\sum_i P(I_i=1).
$$

Independence is not required. In a symmetric problem with $N$ indicators and
$P(I_i=1)=p$, this reduces to $E[X]=Np$.

## 3. Variance of a Sum of Indicators

For $X=\sum_i I_i$,

$$
Var(X)=\sum_i Var(I_i)+2\sum_{i\lt j}Cov(I_i,I_j)
$$

For indicators,

$$
Cov(I_A,I_B)=P(A\cap B)-P(A)P(B)
$$

Thus most indicator-variance questions reduce to computing joint probabilities.

- Independent events have zero covariance.
- If $P(A\cap B)\gt P(A)P(B)$, the covariance is positive.
- If $P(A\cap B)\lt P(A)P(B)$, the covariance is negative.

Zero covariance does not generally imply independence.

## 4. Equivalent Second-Moment Method

The identity

$$
Var(X)=E[X^2]-E[X]^2
$$

is completely equivalent. Since $I_i^2=I_i$,

$$
X^2=\sum_i I_i+2\sum_{i\lt j}I_iI_j,
$$

and therefore

$$
E[X^2]
=\sum_i P(I_i=1)
+2\sum_{i\lt j}P(I_i=1,I_j=1).
$$

The covariance form is usually easier to organize because dependence is explicit.

## 5. Factorial-Moment Trick

Sometimes it is easier to compute

$$
X(X-1)=\sum_{i\ne j}I_iI_j.
$$

Hence

$$
E[X(X-1)]=\sum_{i\ne j}P(I_i=1,I_j=1),
$$

and

$$
Var(X)=E[X(X-1)]+E[X]-E[X]^2.
$$

This is especially useful for collision, matching, and occupancy problems.

## 6. Classify Pairs by Overlap

Do not calculate every covariance separately. Determine which structural features
change the joint probability. Typical classes are:

- disjoint indicators;
- indicators sharing one index or position;
- adjacent versus nonadjacent patterns;
- mutually exclusive events;
- events coupled by a fixed-total constraint.

For each class:

1. compute one representative joint probability;
2. convert it to a covariance;
3. count how many unordered pairs belong to the class;
4. multiply and sum.

If the variance is written with $\sum_{i\lt j}$, count each pair once and retain the
factor $2$. Do not count both $(i,j)$ and $(j,i)$ and then multiply by $2$
again.

## 7. Sampling Without Replacement

Fixed totals create global dependence. If a sequence contains exactly $m$ heads
and $n$ tails, then for distinct positions $i,j$,

$$
P(X_i=H,X_j=H)
=\frac{m}{m+n}\frac{m-1}{m+n-1},
$$

not $[m/(m+n)]^2$.

Therefore, even indicators that use disjoint positions need not be independent.
These joint probabilities are hypergeometric or sampling-without-replacement
probabilities.

More generally, under a conditioning event $B$,

$$
E[I_A\mid B]=P(A\mid B),
$$

so all marginal and joint probabilities must respect the conditioning.

## 8. Standard Patterns

### Birthday collisions

For $n$ people and $d$ equally likely birthdays, let

$$
I_{ij}=\mathbf 1\{\text{people }i,j\text{ share a birthday}\}.
$$

Then the number of colliding pairs is $X=\sum_{i\lt j}I_{ij}$, and

$$
E[X]=\binom n2\frac1d.
$$

For variance, classify two pairs according to whether they share a person.

### Permutation fixed points

Let $I_i=\mathbf 1\{\pi(i)=i\}$. Then

$$
E[X]=\sum_{i=1}^n\frac1n=1.
$$

For $i\ne j$,

$$
P(I_i=1,I_j=1)=\frac{(n-2)!}{n!}=\frac1{n(n-1)}.
$$

### Inversions

Let

$$
I_{ij}=\mathbf 1\{\pi_i\gt\pi_j\},\qquad i\lt j.
$$

Then

$$
E[X]=\binom n2\frac12=\frac{n(n-1)}4.
$$

For variance, classify pairs of comparisons by whether they share an index. See
[P006 — Inversion Count](../../Questions/Probability/P006_Inversion_Count_in_a_Random_Permutation.md).

### Random matching

In a uniformly random perfect matching of $2n$ labeled people, let

$$
I_i=\mathbf 1\{\text{target couple }i\text{ is matched together}\}.
$$

The count $X=\sum_i I_i$ illustrates the full indicator toolkit: linearity of
expectation, dependent joint-success probabilities, overlap-based covariance,
factorial moments, and a Poisson limit. See
[P005 — One-Round Random Matching Patterns](../../Questions/Probability/P005_One_Round_Random_Matching_Patterns.md).

### Occupied boxes

If $n$ balls are placed independently and uniformly into $m$ boxes, let

$$
I_j=\mathbf 1\{\text{box }j\text{ is nonempty}\}.
$$

Then

$$
E[X]=m\left[1-\left(1-\frac1m\right)^n\right].
$$

For variance, compute the probability that two specified boxes are both nonempty.

### Runs and sign changes

Let

$$
I_i=\mathbf 1\{X_i\ne X_{i+1}\},
\qquad
C=\sum_{i=1}^{N-1}I_i.
$$

If $R$ is the number of runs, then $R=C+1$. For a random ordering of $m$
heads and $n$ tails,

$$
E[R]=1+\frac{2mn}{m+n},
$$

and

$$
Var(R)
=\frac{2mn(2mn-m-n)}{(m+n)^2(m+n-1)}.
$$

The closed form follows from classifying adjacent and nonadjacent indicator pairs.
See [P008 — Runs in a Conditioned Coin-Toss Sequence](../../Questions/Probability/P008_Runs_in_a_Conditioned_Coin_Toss_Sequence.md).

### Random graphs

In $G(n,p)$, one edge indicator per possible pair gives

$$
E[N_{\text{edges}}]=\binom n2p.
$$

One triangle indicator per vertex triple gives

$$
E[N_{\text{triangles}}]=\binom n3p^3.
$$

For the triangle-count variance, classify pairs of triangles by their shared edges
or vertices.

## 9. Rare Events and Poisson Approximation

If $X=\sum_iI_i$, individual events are rare, and dependence is weak or local,
then often

$$
X\approx Poisson(\lambda),
\qquad
\lambda=E[X].
$$

This occurs in birthday collisions, defaults, hashing collisions, and sparse random
graph motifs. Under the approximation,

$$
E[X]\approx Var(X)\approx\lambda.
$$

## 10. Interview Workflow

1. Identify exactly what is being counted.
2. Define one indicator for each candidate object.
3. Write the count as a sum of indicators.
4. Use linearity of expectation immediately.
5. For variance, write the covariance expansion or use factorial moments.
6. Classify pairs by overlap or dependence structure.
7. Compute one joint probability per class.
8. Count the number of pairs in each class carefully.
9. Check whether the problem conditions on fixed totals.
10. Consider a Poisson or normal approximation only after the exact first two
    moments are understood.

## 11. Common Mistakes

- Assuming indicators are independent without checking shared randomness.
- Assuming disjoint indicators are independent under a global fixed-total constraint.
- Replacing a joint probability with a product of marginals without justification.
- Forgetting the factor $2$ in the covariance expansion.
- Double-counting ordered pairs and also multiplying by $2$.
- Computing one covariance correctly but miscounting how many pairs have that type.
- Ignoring the conditioning event when computing probabilities.

## 12. Core Formula Sheet

$$
E[I_A]=P(A)
$$

$$
Var(I_A)=P(A)[1-P(A)]
$$

$$
Cov(I_A,I_B)=P(A\cap B)-P(A)P(B)
$$

$$
Var\left(\sum_iI_i\right)
=\sum_i Var(I_i)
+2\sum_{i\lt j}Cov(I_i,I_j)
$$

The durable skill is not memorizing the answer to each counting problem. It is
recognizing the same reusable sequence:

$$
\text{events}
\rightarrow
\text{indicators}
\rightarrow
\text{marginal probabilities}
\rightarrow
\text{joint probabilities}
\rightarrow
\text{overlap counts}
.
$$
