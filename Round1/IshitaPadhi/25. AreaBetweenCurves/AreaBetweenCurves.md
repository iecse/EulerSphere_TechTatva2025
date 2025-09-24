
---

# Definite Integration: Area Between Curves 

## Problem Statement

You are tasked with calculating the **area between two curves** using **numerical integration**. Consider the functions:

$$
f(x) = x^3 - 2x^2 + x + 1
$$

$$
g(x) = x^2 + 1
$$

Compute the area between $f(x)$ and $g(x)$ over the interval:

$$
[0, 2]
$$


---

## Task

The solution should be  rounded off to the nearest integer

---


## Solution

We first define the difference:

$$
h(x) = |f(x) - g(x)| = |x^3 - 3x^2 + x|
$$

We can approximate the area using the **Trapezoidal Rule** with small intervals. For example, using $n = 1000$ subdivisions:

$$
\text{Area} \approx \frac{\Delta x}{2} \left[ h(x_0) + 2\sum_{i=1}^{n-1} h(x_i) + h(x_n) \right]
$$

Where:

$$
\Delta x = \frac{2 - 0}{n} = \frac{2}{1000} = 0.002
$$

Computing numerically, we get:

$$
\text{Area} \approx  2.0450849718229454
$$

**Nearest integer:**

$$
\boxed{2}
$$

---



