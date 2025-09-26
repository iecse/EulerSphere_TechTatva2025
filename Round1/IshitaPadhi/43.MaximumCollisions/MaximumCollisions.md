

# Hash Function Analysis: Maximum Collision Analysis

## Problem Description

Consider the double-hash function:

$$
H_{a,b}(n) = \left( (a \cdot n^2 + b \cdot n) \bmod 103 \right) \bmod 20
$$

where:

* $p = 103$ (prime number)
* $a, b \in \{1, 2, \dots, 102\}$
* $n \in \{0, 1, 2, \dots, 102\}$
* $m = 20$ (number of buckets)

## Computational Task

Find the maximum number of collisions occurring in any single bucket across all possible parameter pairs $(a,b)$:

$$
\text{Answer} = \max_{a,b \in \{1,\dots,102\}} \left( \max_{j=0}^{19} \text{BucketSize}_j(a,b) \right)
$$

**Output:**
A single integer value representing the worst-case maximum bucket size.

## Example

If for some $(a,b)$, the bucket sizes are:

$$
[8,7,6,5,4,3,2,1,0,\dots]
$$

then the maximum bucket size for that pair is **8**.

## Solution

### Computational Approach

1. Iterate over all $102 \times 102 = 10,404$ parameter pairs
2. For each pair, compute the bucket distribution
3. Track the maximum bucket size encountered across all pairs

### Mathematical Analysis

* Total elements: $103$
* Number of buckets: $20$
* Average load factor: $103/20 = 5.15$
* Quadratic hash function provides good distribution
* Due to birthday paradox, some collisions are inevitable
* We seek the worst-case scenario across all parameter choices

### Algorithm

```python
def find_max_collisions():
    p = 103
    m = 20
    max_collisions = 0
    
    for a in range(1, p):
        for b in range(1, p):
            buckets = [0] * m
            
            for n in range(p):
                hash_val = (a*n*n + b*n) % p
                bucket = hash_val % m
                buckets[bucket] += 1
            
            current_max = max(buckets)
            if current_max > max_collisions:
                max_collisions = current_max
    
    return max_collisions
```

### Final Answer

$$
\boxed{11}
$$

---
