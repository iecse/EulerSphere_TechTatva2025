
# Maximum Path Sum 

## Problem Statement

You are given a triangular arrangement of integers. Starting from the top of the triangle, you must move to adjacent numbers on the row below, one step at a time. Your task is to **find the maximum possible total from top to bottom**.

At each step, you may only move to one of the two adjacent numbers directly below your current position.

---

## Task

Given the fixed triangle below:

```
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
```

Your goal is to calculate:

$$
\text{Maximum Total} = \max(\text{Sum of Numbers along any valid path from top to bottom})
$$

---

## Input

No input is required — the triangle is fixed as given above.

---

## Output

Print a **single integer**, which is the **maximum total from top to bottom** following the rules.

---

## Example

For a smaller triangle:

```
3
7 4
2 4 6
8 5 9 3
```

The maximum path sum is:

$$
3 + 7 + 4 + 9 = 23
$$

---

## Solution

For the given triangle:

```
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
```

The maximum path is:

$$
7 \;+\; 3 \;+\; 8 \;+\; 7 \;+\; 5 = 30
$$

Thus, the answer is:

$$
\boxed{30}
$$

---

