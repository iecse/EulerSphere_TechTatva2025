## Eigenvalue Sum Squares

### Problem Statement

For the matrix:

$$
M = \begin{pmatrix}
3 & 1 & 2 \\
1 & 4 & 1 \\
2 & 1 & 5
\end{pmatrix}
$$

Find $\lambda_1^2 + \lambda_2^2 + \lambda_3^2$ where $\lambda_1, \lambda_2, \lambda_3$ are the eigenvalues.

### Notes

- Use the trace property: $\lambda_1 + \lambda_2 + \lambda_3 = \text{tr}(M)$
- Use the fact that $\lambda_1^2 + \lambda_2^2 + \lambda_3^2 = \text{tr}(M^2)$
- Calculate $M^2$ and find its trace
- No need to find individual eigenvalues

---

### Answer

```
62
```
