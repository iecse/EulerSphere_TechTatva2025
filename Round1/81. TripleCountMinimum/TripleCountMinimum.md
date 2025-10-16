# Triple Count Minimum

## Problem Statement

A Primitive Pythagorean Triple (PPT) $(a, b, c)$ is a set of three positive integers that satisfy $a^2 + b^2 = c^2$, with $\gcd(a, b, c) = 1$.

In a simplified context related to generating PPTs, we define $\mathbf{R}(n)$ based on the prime factorization of a number.

Define $\mathbf{R}(n)$ to be the smallest odd number $m$ that has exactly $n$ distinct prime factors.

The number of distinct prime factors of $m$ is denoted by $\omega(m)$. Thus, $\mathbf{R}(n)$ is the smallest odd $m$ such that $\omega(m) = n$.

The smallest odd number with $n$ distinct prime factors is simply the product of the first $n$ odd prime numbers. Let $p_i$ be the $i$-th odd prime number ($p_1=3, p_2=5, p_3=7, \dots$).

$$\mathbf{R}(n) = \prod_{i=1}^{n} p_i$$

### Find the value of:

$$\sum_{k=1}^{10} \mathbf{R}(k)$$

Give your answer modulo $1000003$.

---

## Code (Python)

python
def solve_r_sum_problem(): # First 10 odd prime numbers
odd_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    # The modulus
    M = 1000003

    total_sum = 0
    current_product = 1

    for p in odd_primes:
        # Calculate R(k) = product of the first k odd primes
        current_product *= p

        # Add R(k) to the total sum
        total_sum += current_product

    # The final answer is the total sum modulo M
    final_answer = total_sum % M

    print(f"Total Sum (S): {total_sum}")
    print(f"Modulo (M): {M}")
    print(f"Final Answer (S mod M): {final_answer}")

    return final_answer

# Execution

# solve_r_sum_problem()

# Output: Final Answer (S mod M): 448615
