## DoTheSeries (Difficulty: Hard)

Find the value of the sum: $1^2 - 2 \cdot 3^2 + 3 \cdot 5^2 - 4 \cdot 7^2 + 5 \cdot 9^2 - \dots + 15 \cdot 29^2$.

***

## Solution

This is an alternating series with a clear pattern. The most effective way to solve it is by grouping the terms in pairs. 

### Step 1: Define the General Term

First, let's find the formula for the $n^{th}$ term of the series, denoted by $T_n$.
* The coefficient is simply $n$.
* The squared term follows the sequence $1, 3, 5, \dots$, which is an arithmetic progression with the $n^{th}$ term being $(2n-1)$.
* The sign alternates, which can be represented by $(-1)^{n+1}$.

So, the general term is:
$$T_n = (-1)^{n+1} \cdot n \cdot (2n-1)^2$$

### Step 2: Group the Terms into Pairs

The series has 15 terms. We can group the first 14 terms into 7 pairs and deal with the 15th term separately.

$$S = (T_1 + T_2) + (T_3 + T_4) + \dots + (T_{13} + T_{14}) + T_{15}$$

Let's analyze a generic pair of terms, $(T_{2k-1} + T_{2k})$:

* $T_{2k-1} = (2k-1) \cdot [2(2k-1)-1]^2 = (2k-1)(4k-3)^2$
* $T_{2k} = -(2k) \cdot [2(2k)-1]^2 = -2k(4k-1)^2$

The sum of this pair is:
$$(2k-1)(4k-3)^2 - 2k(4k-1)^2$$
Expanding this expression:
$$(2k-1)(16k^2 - 24k + 9) - 2k(16k^2 - 8k + 1)$$
$$(32k^3 - 64k^2 + 42k - 9) - (32k^3 - 16k^2 + 2k)$$
$$-48k^2 + 40k - 9$$

### Step 3: Calculate the Sum of the Pairs

The sum of the first 14 terms is the sum of the 7 pairs, which we can find by summing the simplified expression from $k=1$ to $k=7$.

$$\text{Sum of Pairs} = \sum_{k=1}^{7} (-48k^2 + 40k - 9)$$
$$= -48 \sum_{k=1}^{7} k^2 + 40 \sum_{k=1}^{7} k - \sum_{k=1}^{7} 9$$

Using the standard summation formulas:
* $\sum_{k=1}^{N} k = \frac{N(N+1)}{2} \implies \sum_{k=1}^{7} k = \frac{7(8)}{2} = 28$
* $\sum_{k=1}^{N} k^2 = \frac{N(N+1)(2N+1)}{6} \implies \sum_{k=1}^{7} k^2 = \frac{7(8)(15)}{6} = 140$

Now, substitute these values back:
$$\text{Sum of Pairs} = -48(140) + 40(28) - 9(7)$$
$$= -6720 + 1120 - 63$$
$$= -5663$$

### Step 4: Calculate the Final Term and the Total Sum

The last term is $T_{15}$:
$$T_{15} = 15 \cdot (2 \cdot 15 - 1)^2 = 15 \cdot (29)^2 = 15 \cdot 841 = 12615$$

The total sum is the sum of the pairs plus the final term:
$$S = (\text{Sum of Pairs}) + T_{15}$$
$$S = -5663 + 12615 = 6952$$

**Therefore, the sum of the series is 6952.** 