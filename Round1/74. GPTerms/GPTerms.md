# Problem 01

Let $a_1, a_2, a_3, ...$ be a G.P. of increasing positive terms.
If $a_1 a_5 = 28$ and $a_2 + a_4 = 29$, then $a_6$ is equal to:

---

## Solution

We are given a Geometric Progression (G.P.) with the first term $a$ and common ratio $r$. Since the terms are increasing and positive, we know $a > 0$ and $r > 1$.

1.  **Use the properties of a G.P. on the first equation:**
    In a G.P., the product of terms equidistant from the center is constant. Therefore, $a_1 a_5 = a_3^2$.
    $$a_3^2 = 28 \implies a_3 = \sqrt{28} = \sqrt{4 \times 7} = 2\sqrt{7}$$

2.  **Rewrite the second equation in terms of $a_3$:**
    We know that $a_2 = \frac{a_3}{r}$ and $a_4 = a_3 r$. Substituting these into the second given equation:
    $$a_2 + a_4 = 29$$   $$\frac{a_3}{r} + a_3 r = 29$$

3.  **Solve for the common ratio $r$:**
    Substitute the value of $a_3 = 2\sqrt{7}$:
    $$\frac{2\sqrt{7}}{r} + 2\sqrt{7} r = 29$$
    Multiply the entire equation by $r$ to eliminate the fraction:
    $$2\sqrt{7} + 2\sqrt{7} r^2 = 29r$$
    Rearrange into a standard quadratic equation form ($Ax^2 + Bx + C = 0$):
    $$2\sqrt{7} r^2 - 29r + 2\sqrt{7} = 0$$
    We solve this for $r$ using the quadratic formula, $r = \frac{-B \pm \sqrt{B^2 - 4AC}}{2A}$:
    $$r = \frac{29 \pm \sqrt{(-29)^2 - 4(2\sqrt{7})(2\sqrt{7})}}{2(2\sqrt{7})}$$   $$r = \frac{29 \pm \sqrt{841 - 16(7)}}{4\sqrt{7}} = \frac{29 \pm \sqrt{841 - 112}}{4\sqrt{7}}$$   $$r = \frac{29 \pm \sqrt{729}}{4\sqrt{7}} = \frac{29 \pm 27}{4\sqrt{7}}$$
    This gives two possible values for $r$:
    $$r_1 = \frac{29 + 27}{4\sqrt{7}} = \frac{56}{4\sqrt{7}} = \frac{14}{\sqrt{7}} = 2\sqrt{7}$$   $$r_2 = \frac{29 - 27}{4\sqrt{7}} = \frac{2}{4\sqrt{7}} = \frac{1}{2\sqrt{7}}$$
    Since the G.P. is **increasing**, we must have $r > 1$.
    As $2\sqrt{7} \approx 5.29$, we choose $r = 2\sqrt{7}$.

4.  **Calculate the required term, $a_6$:**
    We can find $a_6$ using the relation $a_6 = a_3 \cdot r^3$.
    $$a_6 = (2\sqrt{7}) \cdot (2\sqrt{7})^3$$   $$a_6 = (2\sqrt{7})^4 = 2^4 \cdot (\sqrt{7})^4 = 16 \cdot (7^2)$$   $$a_6 = 16 \cdot 49 = 784$$

---

Therefore, the value of $a_6$ is **784**.