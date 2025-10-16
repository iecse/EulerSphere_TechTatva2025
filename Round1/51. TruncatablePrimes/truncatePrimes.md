
# Problem: Modified Truncatable Primes

## Description

A **truncatable prime** is a prime number that remains prime when digits are successively removed from either end.

For example, the number **3797** has this property:

* **Left to right truncation:** 3797 → 797 → 97 → 7 (all prime)
* **Right to left truncation:** 3797 → 379 → 37 → 3 (all prime)

This problem considers a **modified definition**, where **single-digit primes are excluded** from being classified as truncatable primes.

**Task:** Find the sum of all primes that are both left-truncatable and right-truncatable according to this modified definition.

---

## Computational Task

Find the sum of all primes that satisfy:

1. The prime remains prime when **any number of digits are removed from the left**.
2. The prime remains prime when **any number of digits are removed from the right**.
3. The prime has **more than one digit** (excluding 2, 3, 5, and 7).

---

## Example

For the prime **3797**:

* **Left truncation:** 3797 → 797 → 97 → 7
* **Right truncation:** 3797 → 379 → 37 → 3

All resulting numbers are prime, so 3797 is a truncatable prime.

---

## Solution Approach

### Computational Approach

A brute-force search through all primes would be inefficient. Instead, we **build truncatable primes digit by digit**, ensuring all intermediate numbers are prime.

### Mathematical Analysis

* **Right-truncatable primes:** Can be built by appending digits to known right-truncatable primes. The last digit must be 3 or 7 (numbers ending with 2 or 5 are not prime except 2 and 5 themselves).
* **Left-truncatable primes:** Can be built by prepending digits to known left-truncatable primes. The first digit can be any digit from 1–9.
* **Two-way truncatable primes:** Must satisfy both conditions simultaneously.

### Algorithm

1. Start with single-digit primes: 2, 3, 5, 7 (as building blocks).
2. Build **right-truncatable primes** by appending digits (1, 3, 7, 9) to the right.
3. Build **left-truncatable primes** by prepending digits (1–9) to the left.
4. Find the **intersection of both sets** (excluding single-digit primes).
5. Verify that all truncations remain prime.

---

## Final Answer

There are **exactly eleven primes** satisfying the modified truncatable prime condition.

* **Sum of these primes:** 748,317
* **The primes are:** 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, and 739397

---

