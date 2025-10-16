## Linear System Challenge

### Problem Statement

Consider the system of linear equations:

$$
\begin{align}
3x + 2y + z &= 7 \\
x + 4y + 2z &= 11 \\
2x + y + 5z &= 13
\end{align}
$$

Let $(x_0, y_0, z_0)$ be the solution. Find $\lfloor 1000(x_0 + y_0 + z_0) \rfloor$ modulo 1000000007.

### Notes

- Solve using Gaussian elimination or Cramer's rule
- Convert the exact fractional solution to decimal form
- Multiply by 1000 and take the floor
- The system has a unique solution

### Answer

```
4222
```
