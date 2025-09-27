## Newton's Method Iteration Count

### Problem Statement

Apply Newton's method to find the root of $f(x) = x^3 - 7x + 3$ starting with $x_0 = 2$.

How many iterations are needed so that $|x_n - x_{n-1}| < 10^{-8}$?

### Notes

- Use Newton's formula: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
- $f'(x) = 3x^2 - 7$
- Count the number of iterations until convergence
- Submit the iteration count as an integer

---

```
6
```
