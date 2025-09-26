## SnS (Difficulty: Medium)

Find the sum of the series $1 + 3 + 11 + 25 + 45 + 71 + \dots$ up to 20 terms.

***

## Solution

The given series is not an Arithmetic Progression (AP) or a Geometric Progression (GP). We can solve this using the **method of differences**.

### Step 1: Find the Pattern in the Differences

Let's write out the terms and find the differences between them.
* **Original Series ($T_n$):** 1, 3, 11, 25, 45, 71, ...
* **First Differences:**
    * $3 - 1 = 2$
    * $11 - 3 = 8$
    * $25 - 11 = 14$
    * $45 - 25 = 20$
    * $71 - 45 = 26$
    The first differences are `2, 8, 14, 20, 26, ...`. This is an AP with a common difference of 6.
* **Second Differences:**
    * $8 - 2 = 6$
    * $14 - 8 = 6$
    * $20 - 14 = 6$
    Since the second-order differences are constant, the general term ($T_n$) of the series is a quadratic equation of the form $T_n = an^2 + bn + c$.

### Step 2: Determine the General Term ($T_n$)

We can find the coefficients $a, b,$ and $c$ by using the first three terms of the series:
* For $n=1$: $T_1 = a(1)^2 + b(1) + c = a + b + c = 1$
* For $n=2$: $T_2 = a(2)^2 + b(2) + c = 4a + 2b + c = 3$
* For $n=3$: $T_3 = a(3)^2 + b(3) + c = 9a + 3b + c = 11$

Solving this system of equations:
1.  Subtract the first equation from the second: $(4a-a) + (2b-b) = 3-1 \implies 3a+b=2$
2.  Subtract the second equation from the third: $(9a-4a) + (3b-2b) = 11-3 \implies 5a+b=8$
3.  Now, subtract the new equations: $(5a+b) - (3a+b) = 8-2 \implies 2a=6 \implies \mathbf{a=3}$.
4.  Substitute $a=3$ into $3a+b=2$: $3(3)+b=2 \implies 9+b=2 \implies \mathbf{b=-7}$.
5.  Substitute $a=3$ and $b=-7$ into $a+b+c=1$: $3-7+c=1 \implies -4+c=1 \implies \mathbf{c=5}$.

So, the general term of the series is:
$$T_n = 3n^2 - 7n + 5$$

### Step 3: Calculate the Sum up to 20 Terms

We need to find the sum $S_{20} = \sum_{n=1}^{20} T_n$.
$$S_{20} = \sum_{n=1}^{20} (3n^2 - 7n + 5) = 3\sum_{n=1}^{20} n^2 - 7\sum_{n=1}^{20} n + \sum_{n=1}^{20} 5$$

Using the standard summation formulas:
* $\sum_{n=1}^{N} n^2 = \frac{N(N+1)(2N+1)}{6}$
* $\sum_{n=1}^{N} n = \frac{N(N+1)}{2}$
* $\sum_{n=1}^{N} c = cN$

For $N=20$:
$$
\begin{align*}
S_{20} &= 3\left(\frac{20(20+1)(2 \cdot 20+1)}{6}\right) - 7\left(\frac{20(20+1)}{2}\right) + (5 \cdot 20) \\
&= 3\left(\frac{20 \cdot 21 \cdot 41}{6}\right) - 7\left(\frac{20 \cdot 21}{2}\right) + 100 \\
&= 3(2870) - 7(210) + 100 \\
&= 8610 - 1470 + 100 \\
&= 7140 + 100 \\
&= 7240
\end{align*}
$$
Therefore, the sum of the series up to 20 terms is **7240**.