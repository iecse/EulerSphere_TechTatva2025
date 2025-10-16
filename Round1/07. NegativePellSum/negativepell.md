# The Negative Pell Sum Challenge

## Problem Statement

Consider the **negative Pell equation** of the form:
$$x^2 - Dy^2 = -1$$

Unlike the standard Pell equation, the negative Pell equation $x^2 - Dy^2 = -1$ has integer solutions if and only if the period length of the continued fraction representation of $\sqrt{D}$ is **odd**.

When solutions exist, we can find the fundamental (minimal positive) solution using continued fractions, similar to the standard Pell equation.

For example:

- When $D = 2$: $1^2 - 2 \times 1^2 = -1$ (fundamental solution: $x = 1, y = 1$)
- When $D = 5$: $2^2 - 5 \times 1^2 = -1$ (fundamental solution: $x = 2, y = 1$)
- When $D = 10$: $3^2 - 10 \times 1^2 = -1$ (fundamental solution: $x = 3, y = 1$)
- When $D = 4$: No solutions exist (period length is even)

## Your Task

Find all values of $D \leq 100$ where $D$ is not a perfect square and the negative Pell equation $x^2 - Dy^2 = -1$ has solutions.

For each such $D$, find the fundamental solution $(x, y)$ and compute the product $x \times y$.

**What is the sum of all these products $x \times y$ for valid values of $D \leq 100$?**

## Answer

```
116448421
```
