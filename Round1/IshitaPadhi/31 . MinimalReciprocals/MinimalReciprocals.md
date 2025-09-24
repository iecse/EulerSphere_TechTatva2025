
# Minimal Reciprocal Solutions

## Problem Statement

A mathematics research lab is investigating **Diophantine equations** of the form:

$$
\frac{1}{x} + \frac{1}{y} = \frac{1}{n}
$$

where $x, y, n$ are **positive integers**.

Your task is:

> Find the **smallest positive integer $n$** such that the number of distinct solution pairs $(x, y)$ exceeds **1000**.

Two solutions $(x_1, y_1)$ and $(x_2, y_2)$ are considered the same if one is a permutation of the other.

---

## Mathematical Background

The equation can be rewritten as:

$$
(x - n)(y - n) = n^2
$$

$$
\boxed{x = n + d, \quad y = n + \frac{n^2}{d} \text{ for each positive divisor } d \text{ of } n^2}
$$

Thus, the **number of distinct solution pairs** is equal to **the number of positive divisors of $n^2$**.

> Denote the number of solutions as:
>
> $$
> \text{solutions}(n) = \text{number of divisors of } n^2
> $$

Your goal is to find the **smallest $n$** such that:

$$
\text{solutions}(n) > 1000
$$

---

## Input

No input is required. The threshold is fixed:

$$
\text{solutions} > 1000
$$

---

## Output

Print a **single integer**, which is the **smallest $n$** satisfying the condition.

---

## Hint

* Factorization of $n$ is key.
* If $n = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$, then the number of divisors of $n^2$ is:

$$
\boxed{\text{divisors}(n^2) = (2a_1 + 1)(2a_2 + 1) \dots (2a_k + 1)}
$$

* Search **efficiently** starting from $n = 1$.

---

## Hackathon Solution (Java)

```java
public class MinimalReciprocal {
    public static void main(String[] args) {
        int target = 1000;
        int n = 1;

        while (true) {
            int count = 0;
            for (int d = 1; d * d <= n * n; d++) {
                if ((n * n) % d == 0) {
                    count++;
                }
            }
            if (count > target) {
                System.out.println(n);
                break;
            }
            n++;
        }
    }
}
```

**Output:**

```
180
```

---

