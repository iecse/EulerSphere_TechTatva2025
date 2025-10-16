## Matrix Norm Challenge

### Problem Statement

For the matrix:

$$
B = \begin{pmatrix}
1 & 3 & 2 \\
2 & 1 & 4 \\
3 & 2 & 1
\end{pmatrix}
$$

Calculate $\lfloor 10000 \cdot ||B||_F \rfloor$ where $||B||_F$ is the Frobenius norm.

### Notes

- Frobenius norm: $||B||_F = \sqrt{\sum_{i,j} b_{ij}^2}$
- Calculate the sum of squares of all matrix elements
- Take the square root and multiply by 10000
- Apply floor function and then modular arithmetic

### Answer

```
70000
```
