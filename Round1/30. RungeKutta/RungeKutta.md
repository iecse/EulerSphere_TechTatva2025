
# Runge-Kutta Method: Predicting Population Growth

## Problem Statement

A small town wants to **predict its population growth** over a short period. The population at time $t$ (in years) can be modeled by the differential equation:

$$
\frac{dy}{dt} = t + y
$$

where:

* $y(t)$ is the population (in thousands),
* $t$ is the time in years.

The initial population is:

$$
y(0) = 1 \text{ (thousand)}
$$

Your task is to estimate the population at **$t = 0.5$ years** using the **Runge-Kutta 4th order method (RK4)**.

---

## Constraints

* **Step size:** $h = 0.1$
* **Initial condition:** $y(0) = 1$
* **Target:** $y(0.5)$

The RK4 iteration formulas are:

$$
\boxed{
\begin{aligned}
k_1 &= h \cdot f(t_n, y_n) \\
k_2 &= h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right) \\
k_3 &= h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right) \\
k_4 &= h \cdot f(t_n + h, y_n + k_3) \\
y_{n+1} &= y_n + \frac{k_1 + 2k_2 + 2k_3 + k_4}{6}
\end{aligned}
}
$$

---

## Input

No input is required. All parameters are fixed:

* $h = 0.1$
* $y(0) = 1$
* Target $t = 0.5$

---

## Output

Print a **single integer**, which is the **nearest integer** to the population $y(0.5)$ (in thousands).

---

## Step-by-Step Example (RK4 Iteration)

| Step | $t_n$ | $y_n$ | $y_{n+1}$ |
| ---- | ----- | ----- | --------- |
| 0    | 0.0   | 1.000 | 1.110     |
| 1    | 0.1   | 1.110 | 1.232     |
| 2    | 0.2   | 1.232 | 1.367     |
| 3    | 0.3   | 1.367 | 1.516     |
| 4    | 0.4   | 1.516 | 1.681     |

**Nearest integer:**

$$
\boxed{2}
$$

---



