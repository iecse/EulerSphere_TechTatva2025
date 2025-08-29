# Peak Analysis

## Problem Statement

The Collatz Conjecture involves the following iterative process:

- If n is even: n → n/2
- If n is odd: n → 3n + 1

For any starting number n, define:

- **Peak Height P(n)**: The maximum value reached during the Collatz sequence before reaching 1
- **Total Steps S(n)**: The total number of steps to reach 1

For n = 7:

- Sequence: 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
- Peak Height P(7) = 52
- Total Steps S(7) = 16

Find the sum of all odd starting numbers n where 1 ≤ n ≤ 50,000 such that:

1. **P(n) > 3 × n** (the peak height exceeds 3 times the starting number)
2. **S(n) is divisible by 4** (the total steps is a multiple of 4)
3. **P(n) contains the digit '2'** when written in decimal form

## Notes

- Only consider odd starting numbers in the range [1, 50,000]
- The Collatz sequence always starts with the given number n
- Count the total steps until reaching 1 (not including 1 in the count)
- The peak height is the maximum value encountered during the entire sequence
- All three conditions must be satisfied simultaneously for a number to be included in the sum

## Answer

```
91725119
```
