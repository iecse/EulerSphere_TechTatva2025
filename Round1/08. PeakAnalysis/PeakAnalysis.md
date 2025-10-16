# Peak Analysis

## Problem Statement

The Collatz Conjecture involves the following iterative process:

- If n is even: n → n/2
- If n is odd: n → 3n + 1

For any starting number n, define:

- **Peak Height P(n)**: The maximum value reached during the Collatz sequence before reaching 1
- **Total Steps S(n)**: The total number of steps to reach 1

For example, n = 7:

- Sequence: 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
- Peak Height P(7) = 52
- Total Steps S(7) = 16

Find the number of integers n where 1 ≤ n ≤ 1000 such that the peak height P(n) is a perfect square.

## Notes

- Consider all positive integers in the range [1, 1000]
- The Collatz sequence always starts with the given number n
- Count the total steps until reaching 1 (not including 1 in the count)
- The peak height is the maximum value encountered during the entire sequence
- A perfect square is a number that can be expressed as k² for some positive integer k

## Answer

```
58
```
