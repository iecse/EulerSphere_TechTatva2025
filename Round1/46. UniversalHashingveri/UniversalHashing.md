


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
\approx 0.074766
$$

Converting to percentage:

7.4766355 

### Final Answer

$$
\boxed{7}
$$

---





