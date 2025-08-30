# Digital Root Chains Problem

## Problem Statement

Define a "digital transformation" of a positive integer as follows: multiply each digit by its position (1-indexed from the right), then sum the results.

### Example

For the number 1234:

- Digit 4 is at position 1: 4 × 1 = 4
- Digit 3 is at position 2: 3 × 2 = 6
- Digit 2 is at position 3: 2 × 3 = 6
- Digit 1 is at position 4: 1 × 4 = 4
- Sum: 4 + 6 + 6 + 4 = 20

Starting with any positive integer, repeatedly apply this transformation until you either:

1. **Reach a single digit** (terminating chain)
2. **Enter a cycle** (non-terminating chain)

### Chain Length

The chain length is the total number of steps in the sequence, including:

- The starting number
- All intermediate results
- The final single digit (for terminating chains)

Find the sum of all starting numbers less than 1,000,000 that produce terminating chains of length **exactly 7**.

## Notes

- Only consider positive integers as starting numbers
- The transformation uses 1-indexed positions from the right
- A chain terminates when it reaches any single digit (0-9)
- If a chain enters a cycle (repeats a previous value), it's non-terminating
- We only want chains with length exactly 7

## Answer

```
0
```
