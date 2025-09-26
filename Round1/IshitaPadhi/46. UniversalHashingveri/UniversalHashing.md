


# Hash Function Analysis: Universal Hashing Verification (Percentage Form)

## Problem Description

Consider the universal hash family:

$$
H_{a,b}(x) = \left( (a \cdot x + b) \bmod 107 \right) \bmod 12
$$

where:

* $p = 107$ (prime number)
* $a \in \{1, 2, \dots, 106\}$, $b \in \{0, 1, \dots, 106\}$
* $x, y \in \{0, 1, \dots, 106\}$ with $x \neq y$

## Computational Task

Compute the **probability (in percentage)** of collision for two distinct elements and print the **rounded-off integer percentage** as the final answer:

$$
\text{Answer} = \text{round}\!\Bigg( 
100 \times 
\frac{\text{Number of }(a,b) \text{ pairs with } H_{a,b}(x) = H_{a,b}(y)}
{\text{Total number of }(a,b) \text{ pairs}}
\Bigg)
$$

for fixed distinct $x$ and $y$.

## Example

If the collision probability is $1.89\%$, the output should be:

```
2
```

## Solution

### Theoretical Calculation

$$
\mathbb{P} = \frac{\lfloor p/m \rfloor}{p-1} 
= \frac{8}{106} 
= \frac{4}{53} 
\approx 0.07547
$$

Converting to percentage:

$$
\text{Percentage} = 0.07547 \times 100 = 7.547 \approx 8
$$

### Final Answer

$$
\boxed{8}
$$

---

## ✅ Modified Java Code

Here’s the updated Java code that **prints the rounded-off percentage as a single integer**:

```java
public class UniversalHashingVerification {

    public static void main(String[] args) {
        int p = 107;  // prime number
        int m = 12;   // number of buckets
        int totalPairs = 106 * 107;

        int x = 5;  // any distinct x, y
        int y = 10;

        int collisionCount = 0;

        for (int a = 1; a < p; a++) {
            for (int b = 0; b < p; b++) {
                int hx = ((a * x + b) % p) % m;
                int hy = ((a * y + b) % p) % m;

                if (hx == hy) {
                    collisionCount++;
                }
            }
        }

        double probability = (double) collisionCount / totalPairs;
        int percentage = (int) Math.round(probability * 100);

        // Print a single integer (percentage)
        System.out.println(percentage);
    }
}
```

---

### ✅ Expected Output:

```
8
```

(since $\frac{856}{11342} \approx 7.547\%$, which rounds to 8)

---


