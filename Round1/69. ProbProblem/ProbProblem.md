## ProbProblem (Difficulty: Medium)

Two numbers, $k_1$ and $k_2$, are randomly chosen from the set of natural numbers. Find the probability that the value of $i^{k_1} + i^{k_2}$ is non-zero, where $i = \sqrt{-1}$.

***

## Solution

The key to solving this problem is to understand the cyclical nature of the powers of $i$.

### Step 1: Possible Values of $i^k$

For any natural number $k$, the expression $i^k$ cycles through four distinct values: $i, -1, -i, 1$. Since $k_1$ and $k_2$ are chosen randomly, we can consider the four possible outcomes for both $i^{k_1}$ and $i^{k_2}$.

### Step 2: Total Possible Outcomes

We are looking at the pair of values $(i^{k_1}, i^{k_2})$. Since there are 4 distinct outcomes for $i^{k_1}$ and 4 for $i^{k_2}$, the total number of possible combinations is:

$$\text{Total Cases} = 4 \times 4 = 16$$

### Step 3: Identify Unfavorable Outcomes

The desired outcome is that the sum is non-zero ($i^{k_1} + i^{k_2} \neq 0$). The opposite of this, the **unfavorable case**, is when the sum is zero:

$$i^{k_1} + i^{k_2} = 0 \implies i^{k_1} = -i^{k_2}$$

This condition is met for the following pairs of values for $(i^{k_1}, i^{k_2})$:
* $(1, -1)$
* $(-1, 1)$
* $(i, -i)$
* $(-i, i)$

There are a total of **4 unfavorable outcomes**.

### Step 4: Calculate the Final Probability

The number of **favorable outcomes** (where the sum is non-zero) is the total number of outcomes minus the unfavorable ones.

$$\text{Favorable Outcomes} = \text{Total Cases} - \text{Unfavorable Cases} = 16 - 4 = 12$$

The probability is the ratio of favorable outcomes to the total number of outcomes:

$$P(\text{sum} \neq 0) = \frac{\text{Number of Favorable Outcomes}}{\text{Total Number of Outcomes}} = \frac{12}{16}$$

Simplifying the fraction gives us the final answer.

$$P(\text{sum} \neq 0) = \frac{3}{4}$$

**Therefore, the probability that the value is non-zero is $\frac{3}{4}$.**