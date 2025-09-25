# Iterative Convergence Algorithm

## Problem Statement

Let
$$f(x) = \ln x + x^2 - 3, \qquad f'(x) = \frac{1}{x} + 2x$$

Start with $x_0 = 1$ and iterate
$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$

until $|x_{k+1} - x_k| < 10^{-12}$. Let $x^*$ be the **first** iterate $x_{k+1}$ that satisfies this stopping criterion.

Define
$$N = \lfloor 10^9 \, x^* \rfloor$$

**Submit the integer N only.**

## Notes

- Use the Newton-Raphson method for root finding
- The function $f(x) = \ln x + x^2 - 3$ is only defined for $x > 0$
- Starting point is $x_0 = 1$
- Stop when the absolute difference between consecutive iterates is less than $10^{-12}$
- $x^*$ is the first iterate that satisfies the stopping criterion
- Calculate $N$ by multiplying $x^*$ by $10^9$ and taking the floor
- Ensure sufficient precision in calculations for accurate results

## Answer

```
1592142937
```
