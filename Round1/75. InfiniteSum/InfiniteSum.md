# Problem

The sum of all real values of k for which $(\frac{1}{8})^k \times (\frac{1}{32768})^{\frac{1}{3}} = \frac{1}{8} \times (\frac{1}{32768})^{\frac{1}{k}}$ is

---

## Solution

The key to solving this equation is to express all the numbers in a common base, which in this case is 2.

1.  **Convert the bases:**

    - $8 = 2^3 \implies \frac{1}{8} = 2^{-3}$
    - $32768 = 2^{15} \implies \frac{1}{32768} = 2^{-15}$

2.  **Substitute the new bases into the equation:**
    $$(2^{-3})^k \times (2^{-15})^{\frac{1}{3}} = (2^{-3})^1 \times (2^{-15})^{\frac{1}{k}}$$

3.  **Simplify using exponent rules:**
    Using the rule $(a^m)^n = a^{mn}$, we can simplify both sides.

    - **Left-hand side:** $2^{-3k} \times 2^{-15/3} = 2^{-3k} \times 2^{-5} = 2^{-3k - 5}$
    - **Right-hand side:** $2^{-3} \times 2^{-15/k} = 2^{-3 - 15/k}$

4.  **Equate the exponents:**
    Now that both sides have the same base, we can set their exponents equal to each other:
    $$-3k - 5 = -3 - \frac{15}{k}$$

5.  **Solve the resulting equation for k:**
    First, multiply the entire equation by -1 to make it cleaner:
    $$3k + 5 = 3 + \frac{15}{k}$$
    Now, multiply by $k$ to eliminate the fraction (note: $k \neq 0$ from the original equation).
    $$k(3k + 5) = k(3 + \frac{15}{k})$$
    $$3k^2 + 5k = 3k + 15$$
    Rearrange this into a standard quadratic equation ($ax^2 + bx + c = 0$):
    $$3k^2 + 2k - 15 = 0$$

6.  **Find the sum of the roots:**
    The problem asks for the sum of all real values of $k$, which are the roots of this quadratic equation. For any quadratic equation $ax^2 + bx + c = 0$, the sum of the roots is given by the formula $-\frac{b}{a}$.

    - Here, $a=3$, $b=2$, and $c=-15$.

    Sum of roots = $-\frac{2}{3}$

    (The discriminant $b^2 - 4ac = 2^2 - 4(3)(-15) = 4 + 180 = 184 > 0$, confirming the roots are real.)

---

**Answer:** The sum of all real values of k is $-\frac{2}{3}$.
