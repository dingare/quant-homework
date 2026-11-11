# P042 — Even Heads and a Fair Coin

## Metadata

- Category: Probability
- Tags: Independent Bernoulli Trials, Parity, Recursion, Product Expansion
- Date Added: 2026-11-10
- Status: Discussion summarized; the user proposed the recursion and the identical-probability signed expansion. The backward-induction completion and unequal-probability product were explained in the discussion.
- Source: User-provided question, outside the scheduled daily drill; no timed assessment recorded.

## Core Question

Suppose we have 10 coins, with head probabilities $`p_1,\ldots,p_{10}`$. If the probability of getting an even number of heads is $`1/2`$, what does this imply about the head probabilities?

**Assumption:** Each coin is tossed once, and all outcomes are mutually independent. The probabilities need not be equal. The argument relies on this independence assumption.

**Answer:** At least one coin has head probability $`1/2`$. In fact, this is both necessary and sufficient.

## Hint

Track the difference between the probabilities of an even and an odd number of heads. Adding a coin either preserves or flips parity.

## Solution

### 1. User's approach: recursion and backward induction

Let $`m`$ be the probability of an even number of heads among the first $`n-1`$ coins. The probability of an odd number is $`1-m`$. A tail on the last coin preserves parity, while a head flips it. Therefore:

```math
P(\text{even heads among }n)
=m(1-p_n)+(1-m)p_n.
```

If this probability equals $`1/2`$, then:

```math
m(1-p_n)+(1-m)p_n=\frac12
\quad\Longrightarrow\quad
(2m-1)(2p_n-1)=0.
```

Thus either $`p_n=1/2`$ or $`m=1/2`$. In the second case, the first $`n-1`$ coins satisfy the same condition, so repeat the argument. If no fair coin has been found by the time only the first coin remains, then:

```math
P(\text{even heads among one coin})=1-p_1=\frac12.
```

This gives $`p_1=1/2`$. Hence at least one coin is fair.

### 2. Short proof: even probability minus odd probability

Consider the product:

```math
\prod_{i=1}^{n}\big[(1-p_i)-p_i\big].
```

In the expansion, choosing $`1-p_i`$ from a factor represents a tail, and choosing $`-p_i`$ represents a head. Independence makes the absolute value of each term the probability of its corresponding complete outcome. An even number of heads gives a positive term; an odd number gives a negative term. Consequently:

```math
\prod_{i=1}^{n}(1-2p_i)
=P(\text{even heads})-P(\text{odd heads}).
```

Since the even probability is $`1/2`$, the odd probability is also $`1/2`$. Hence:

```math
\prod_{i=1}^{n}(1-2p_i)=0
\quad\Longrightarrow\quad
\exists i:\ p_i=\frac12.
```

Conversely, if any coin is fair, the product is zero. The even and odd probabilities are equal and sum to one, so both equal $`1/2`$. Combining the sum and difference of the two probabilities also gives the general formula:

```math
\boxed{
P(\text{even heads})
=\frac{1+\prod_{i=1}^{n}(1-2p_i)}{2}.
}
```

### 3. User's takeaway: equal probabilities are not required

The user had already recognized the following expression when all head probabilities are equal:

```math
\bigl(p-(1-p)\bigr)^n.
```

To allow different head probabilities, replace the power of one factor with a product of different factors:

```math
\bigl(p-(1-p)\bigr)^n
\quad\longrightarrow\quad
\prod_{i=1}^{n}\bigl(p_i-(1-p_i)\bigr).
```

Equal probabilities allow terms to be grouped using binomial coefficients. With unequal probabilities, that grouping is unavailable, but the product expansion and its sign pattern still apply.

Check the sign convention: this expression assigns a positive factor to a head and a negative factor to a tail, so an outcome with $`k`$ heads has sign $`(-1)^{n-k}`$. Here $`n=10`$ is even, so the product is still the even probability minus the odd probability. To preserve that direction for every $`n`$, use $`(1-p_i)-p_i`$ as in the second proof.

## Key Knowledge Points

- Parity has only two states; each new coin preserves or flips the state.
- The even probability minus the odd probability can be expressed as one product.
- The product structure requires independence, but not identical head probabilities.
- The conclusion requires at least one fair coin; it does not imply that every coin is fair.

## Intuition

The recursive proof removes one coin at a time. The product proof combines every coin's contribution to parity at once. Both express the same structure.

## Common Mistakes

- Stopping at “the preceding even probability is one half, or the last coin is fair” without completing the backward induction.
- Treating identical head probabilities as a requirement for the product expansion.
- Omitting the parentheses around the entire difference: use $`\bigl(p-(1-p)\bigr)^n`$, not $`p-(1-p)^n`$.
- Reversing the head/tail sign convention without checking how the total number of coins affects the overall sign.

## Connections

- [P031 — Exact Uniform Sampling from a Biased Coin](P031_Exact_Uniform_Sampling_from_a_Biased_Coin.md): Both concern biased coins and fair outcomes. This question studies parity after a fixed number of tosses; P031 studies exact sampling.
- [First-Hitting Parity, Coverage, and Alternating Ownership](../../KnowledgeCards/Probability/First_Hitting_Parity_Coverage_and_Alternating_Ownership.md): Both use parity to reduce the state space. The card studies first hitting and stopping times; this question counts heads in a fixed set of independent coin tosses.

## Assessment History

Discussion on 2026-11-10: The user independently proposed the correct recursive decomposition and obtained “the preceding even probability is one half, or the last coin is fair.” The assistant completed the backward induction. The user reported already recognizing the signed power expansion for equal probabilities, but had not immediately generalized it to unequal probabilities; the product extension was explained in the discussion. No formal rating or claim of independent mastery is added.

## What to Remember

**Equal probabilities make terms easier to group; independence makes each outcome probability a product.**

```math
P(\text{even})=\frac12
\quad\Longleftrightarrow\quad
\prod_{i=1}^{n}(1-2p_i)=0
\quad\Longleftrightarrow\quad
\text{at least one }p_i=\frac12.
```
