## GreatLog (Difficulty: Hard)

Let $[\cdot]$ denote the **greatest integer function** (floor function). If the following equation is true:
$$\int_{0}^{e^3} \left[ \frac{1}{e^{x-1}} \right] dx = \alpha - \log_e 2$$
then what is the value of $\alpha^3$?

***

## Solution

The solution involves breaking the integral into intervals where the value of the greatest integer function is constant.

### Step 1: Analyze the Function

First, let's analyze the function inside the greatest integer brackets. Let $f(x) = \frac{1}{e^{x-1}}$, which can be simplified to $f(x) = e^{1-x}$.

The value of the greatest integer function, $[f(x)]$, changes only when $f(x)$ crosses an integer value (e.g., 1, 2, 3, ...). Since $f(x) = e^{1-x}$ is a decreasing function, we need to find the values of $x$ where these transitions occur.

### Step 2: Find the Interval Boundaries

Let's evaluate the function at the start of our integration interval, $x=0$:
$$f(0) = e^{1-0} = e \approx 2.718$$
This tells us that the greatest integer function will have values of 2 and 1 before it drops to 0. Let's find the $x$-values where $f(x)$ is exactly 2 and 1.

* **When $f(x) = 2$:**
    $$e^{1-x} = 2$$
    $$1-x = \ln(2)$$
    $$x = 1 - \ln(2)$$

* **When $f(x) = 1$:**
    $$e^{1-x} = 1$$
    $$1-x = \ln(1) = 0$$
    $$x = 1$$

These $x$-values are the points where the value of $[f(x)]$ changes.

### Step 3: Split the Integral

Based on the boundaries we found, we can determine the constant value of $[f(x)]$ in each interval:

1.  For $x$ in the interval $[0, 1-\ln 2)$, the value of $f(x) = e^{1-x}$ is in the range $(2, e]$. Thus, $[f(x)] = 2$.
2.  For $x$ in the interval $[1-\ln 2, 1)$, the value of $f(x)$ is in the range $(1, 2]$. Thus, $[f(x)] = 1$.
3.  For $x$ in the interval $[1, e^3]$, the value of $f(x)$ is in the range $(0, 1]$. Thus, $[f(x)] = 0$ for $x > 1$ and $[f(x)]=1$ just at the single point $x=1$. For integration purposes over this range, the value is effectively 0.

Now we can split the original integral into three parts:
$$\int_{0}^{e^3} [e^{1-x}] \,dx = \int_{0}^{1-\ln 2} 2 \,dx + \int_{1-\ln 2}^{1} 1 \,dx + \int_{1}^{e^3} 0 \,dx$$

### Step 4: Evaluate the Integral

Let's calculate each part:

$$
\begin{align*}
I &= [2x]_{0}^{1-\ln 2} + [x]_{1-\ln 2}^{1} + [0]_{1}^{e^3} \\
&= (2(1-\ln 2) - 0) + (1 - (1-\ln 2)) + 0 \\
&= (2 - 2\ln 2) + (1 - 1 + \ln 2) \\
&= 2 - 2\ln 2 + \ln 2 \\
&= 2 - \ln 2
\end{align*}
$$

### Step 5: Solve for $\alpha$ and $\alpha^3$

We are given that the value of the integral is $\alpha - \log_e 2$, which is $\alpha - \ln 2$.
$$2 - \ln 2 = \alpha - \ln 2$$
By comparing the two sides, we can see that:
$$\alpha = 2$$
The question asks for the value of $\alpha^3$:
$$\alpha^3 = 2^3 = \bf{8}$$