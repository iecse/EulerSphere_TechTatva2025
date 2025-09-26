## TakeABreak (Difficulty: Medium)

Find the value of the following limit:

$$\lim_{n \to \infty} \left( \frac{1}{1 + n^2} + \frac{2}{2 + n^2} + \dots + \frac{n}{n + n^2} \right)$$

## Solution using the Squeeze Theorem

### Step 1: Define the Sequence

Let $P_n$ be the sequence given in the problem.
$$P_n = \frac{1}{1+n^2} + \frac{2}{2+n^2} + \dots + \frac{n}{n+n^2}$$

### Step 2: Find an Upper Bound

To find an **upper bound**, we can make each fraction in the sum larger by making its denominator smaller. The smallest denominator in the series is $1+n^2$.

$$
\begin{align*}
P_n &< \frac{1}{1+n^2} + \frac{2}{1+n^2} + \dots + \frac{n}{1+n^2} \\
P_n &< \frac{1+2+3+\dots+n}{1+n^2}
\end{align*}
$$

Since the sum of the first $n$ integers is $\frac{n(n+1)}{2}$, we get:
$$P_n < \frac{n(n+1)}{2(1+n^2)}$$

### Step 3: Find a Lower Bound

To find a **lower bound**, we can make each fraction smaller by making its denominator larger. The largest denominator in the series is $n+n^2$.

$$
\begin{align*}
P_n &> \frac{1}{n+n^2} + \frac{2}{n+n^2} + \dots + \frac{n}{n+n^2} \\
P_n &> \frac{1+2+3+\dots+n}{n+n^2}
\end{align*}
$$

This gives us the lower bound:
$$P_n > \frac{n(n+1)}{2(n+n^2)}$$

### Step 4: Apply the Squeeze Theorem

Now we have "squeezed" $P_n$ between two other sequences:
$$\frac{n(n+1)}{2(n+n^2)} < P_n < \frac{n(n+1)}{2(1+n^2)}$$

Next, we take the limit of the outer two sequences as $n \to \infty$. To do this, we can divide the numerator and denominator by the highest power of $n$, which is $n^2$.

* **Limit of the lower bound:**
    $$
    \lim_{n \to \infty} \frac{n(n+1)}{2(n+n^2)} = \lim_{n \to \infty} \frac{n^2+n}{2n^2+2n} = \lim_{n \to \infty} \frac{1 + \frac{1}{n}}{2 + \frac{2}{n}} = \frac{1+0}{2+0} = \frac{1}{2}
    $$

* **Limit of the upper bound:**
    $$
    \lim_{n \to \infty} \frac{n(n+1)}{2(1+n^2)} = \lim_{n \to \infty} \frac{n^2+n}{2+2n^2} = \lim_{n \to \infty} \frac{1 + \frac{1}{n}}{\frac{2}{n^2} + 2} = \frac{1+0}{0+2} = \frac{1}{2}
    $$

Since both the lower and upper bounds approach $\frac{1}{2}$, the limit of $P_n$ must also be $\frac{1}{2}$.

$$\frac{1}{2} \le \lim_{n \to \infty} P_n \le \frac{1}{2}$$

Therefore, the final answer is:
$$\lim_{n \to \infty} P_n = \frac{1}{2}$$