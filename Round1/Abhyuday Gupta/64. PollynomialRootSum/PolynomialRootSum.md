## Polynomial Root Sum

### Problem Statement

Find all roots of the polynomial $P(x) = x^4 - 10x^3 + 35x^2 - 50x + 24$.

Let $r_1, r_2, r_3, r_4$ be the four roots. Calculate $r_1^2 + r_2^2 + r_3^2 + r_4^2$.

### Notes

- Use Newton's identities or Vieta's formulas
- $r_1^2 + r_2^2 + r_3^2 + r_4^2 = (\sum r_i)^2 - 2\sum_{i<j} r_i r_j$
- From Vieta's formulas: $\sum r_i = 10$, $\sum_{i<j} r_i r_j = 35$
- Calculate exactly without finding individual roots

### Answer

```
30
```
