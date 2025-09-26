## ModI(Difficulty : Medium)

The remainder, when $7^{103}$ is divided by 23, is equal to:

***

## Solution

We can solve this efficiently using *modular arithmetic* and *Fermat's Little Theorem*.

### Step 1: Apply Fermat's Little Theorem

Fermat's Little Theorem states that if $p$ is a prime number, then for any integer $a$ not divisible by $p$, the following relationship holds:
$$a^{p-1} \equiv 1 \pmod{p}$$

In this problem, our prime number is $p=23$ and $a=7$. Applying the theorem gives us a key simplification:
$$7^{23-1} \equiv 1 \pmod{23}$$
$$7^{22} \equiv 1 \pmod{23}$$

This means that any multiple of $7^{22}$ will have a remainder of 1 when divided by 23.

### Step 2: Reduce the Exponent

Now, we can use this result to simplify the original expression $7^{103}$. We just need to express the exponent 103 in terms of 22.
$$103 \div 22 = 4 \text{ with a remainder of } 15$$
So, we can write $103 = 22 \times 4 + 15$.

Substituting this back into our expression:
$$7^{103} = 7^{(22 \times 4 + 15)} = (7^{22})^4 \cdot 7^{15}$$

### Step 3: Simplify the Problem

Now let's find the remainder.
$$7^{103} \pmod{23} \equiv ((7^{22})^4 \cdot 7^{15}) \pmod{23}$$Since we know $7^{22} \equiv 1 \pmod{23}$, this becomes:$$\equiv (1^4 \cdot 7^{15}) \pmod{23}$$
$$\equiv 7^{15} \pmod{23}$$
The problem is now reduced to finding the remainder of $7^{15}$ divided by 23.

### Step 4: Calculate the Final Remainder

We can calculate $7^{15} \pmod{23}$ by breaking it down into smaller, manageable powers.
* $7^1 \equiv 7 \pmod{23}$
* $7^2 = 49 \equiv 3 \pmod{23}$ (since $49 = 2 \times 23 + 3$)
* $7^4 = (7^2)^2 \equiv 3^2 \equiv 9 \pmod{23}$
* $7^8 = (7^4)^2 \equiv 9^2 = 81 \equiv 12 \pmod{23}$ (since $81 = 3 \times 23 + 12$)

Now we can build $7^{15}$ using these parts, since $15 = 8 + 4 + 2 + 1$.
$$
\begin{align*}
7^{15} &= 7^8 \cdot 7^4 \cdot 7^2 \cdot 7^1 \\
&\equiv (12 \cdot 9 \cdot 3 \cdot 7) \pmod{23} \\
&\equiv (108 \cdot 21) \pmod{23} \\
&\equiv (16 \cdot 21) \pmod{23} \quad (\text{since } 108 = 4 \times 23 + 16) \\
&\equiv 336 \pmod{23}
\end{align*}
$$Finally, we divide 336 by 23:$$336 = 14 \times 23 + 14$$
So, the remainder is 14.

Therefore, $7^{103} \equiv 14 \pmod{23}$.

Final answer = 14
$$