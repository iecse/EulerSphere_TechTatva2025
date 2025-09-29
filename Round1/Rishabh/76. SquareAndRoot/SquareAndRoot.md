# Problem

If $(a + b\sqrt{3})^2 = 52 + 30\sqrt{3}$, where $a$ and $b$ are natural numbers, then $a + b$ equals:

## Solution

We are given the equation:
$$(a + b\sqrt{3})^2 = 52 + 30\sqrt{3}$$

1.  **Expand the left-hand side (LHS):**
    Using the formula $(x+y)^2 = x^2 + 2xy + y^2$, we get:
    $$(a + b\sqrt{3})^2 = a^2 + 2(a)(b\sqrt{3}) + (b\sqrt{3})^2$$
    $$= a^2 + 2ab\sqrt{3} + 3b^2$$
    $$= (a^2 + 3b^2) + (2ab)\sqrt{3}$$

2.  **Equate the expanded LHS with the right-hand side (RHS):**
    $$(a^2 + 3b^2) + (2ab)\sqrt{3} = 52 + 30\sqrt{3}$$

3.  **Compare the rational and irrational parts:**
    For the equality to hold, the rational parts on both sides must be equal, and the irrational parts must also be equal.

    - Rational part: $a^2 + 3b^2 = 52$
    - Irrational part: $2ab = 30 \implies ab = 15$

4.  **Solve the system of equations:**
    Since $a$ and $b$ are natural numbers, we find pairs of factors for $ab = 15$:

    - (1, 15)
    - (3, 5)
    - (5, 3)
    - (15, 1)

    Now we substitute these pairs into the first equation, $a^2 + 3b^2 = 52$, to find the correct pair.

    - If $(a, b) = (1, 15)$: $1^2 + 3(15^2) = 1 + 3(225) = 676 \neq 52$
    - If $(a, b) = (3, 5)$: $3^2 + 3(5^2) = 9 + 3(25) = 9 + 75 = 84 \neq 52$
    - If $(a, b) = (5, 3)$: $5^2 + 3(3^2) = 25 + 3(9) = 25 + 27 = 52$. **This is correct.**
    - If $(a, b) = (15, 1)$: $15^2 + 3(1^2) = 225 + 3 = 228 \neq 52$

    So, the values are $a=5$ and $b=3$.

5.  **Calculate the final result:**
    The question asks for the value of $a+b$.
    $$a + b = 5 + 3 = 8$$

---

✅ **Answer:** The correct values are $a=5$ and $b=3$, so $a + b = \textbf{8}$.
