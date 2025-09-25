
# Newton-Raphson Method

## Problem Statement

You are tasked with finding the root of a nonlinear equation using the **Newton-Raphson method**. Consider the function:

$$
f(x) = x^3 - 7x^2 + 14x - 6
$$

Use the following constraints:

* **Initial guess:** $x_0 = 3$
* **Tolerance:** $\epsilon = 0.001$
* **Maximum iterations:** 20

The iteration should stop when either:

$$
\left| x_{n+1} - x_n \right| < \epsilon
$$

or the maximum number of iterations is reached.

---

## Newton-Raphson Formula (Reference)

$$
\boxed{
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
}
$$

where the derivative of $f(x)$ is:

$$
f'(x) = 3x^2 - 14x + 14
$$

---

## Output

Print a **single integer**, which is the nearest integer to the root found using Newton-Raphson.

---

## Solution

Start with $x_0 = 3$ and iteratively apply the **Newton-Raphson formula** until:

$$
\left| x_{n+1} - x_n \right| < 0.001 \quad \text{or maximum 20 iterations reached.}
$$

Finally, round the computed root to the **nearest integer**.

---

### Step-by-Step Calculation (First Few Iterations)

| Iteration | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $x_{n+1}$ |
| --------- | ----- | -------- | --------- | --------- |
| 1         | 3.000 | 6.000    | 17.000    | 2.647     |
| 2         | 2.647 | 0.751    | 8.113     | 2.558     |
| 3         | 2.558 | 0.017    | 7.468     | 2.556     |
| 4         | 2.556 | 0.0002   | 7.450     | 2.556     |

**Nearest integer root:**

$$
\boxed{3}
$$

