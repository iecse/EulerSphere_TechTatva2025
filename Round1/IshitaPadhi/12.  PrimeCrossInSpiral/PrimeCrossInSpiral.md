# Prime Cross in Spiral

## Description

Starting from **1** at the center of a square spiral and moving **anticlockwise**, we form layers of increasing **odd side length**.

### Example: Spiral with Side Length 5

| 21 | 22 | 23 | 24 | 25 |
|----|----|----|----|----|
| 20 |  7 |  8 |  9 | 10 |
| 19 |  6 |  1 |  2 | 11 |
| 18 |  5 |  4 |  3 | 12 |
| 17 | 16 | 15 | 14 | 13 |

Numbers along the diagonals:

\[
21, \ 7, \ 1, \ 3, \ 13, \ 17, \ 5, \ 9, \ 25
\]

Primes on diagonals:

\[
7, \ 3, \ 13, \ 17, \ 5
\]

---

## Task

Continue building larger spirals (side lengths \(1, 3, 5, 7, 9, \dots\)) and find the **first side length** for which:

\[
\frac{\text{Prime Count on Diagonals}}{\text{Total Diagonal Numbers}} < 20\%
\]

---

## Input

No input required.

---

## Output

A single integer:  
The **side length** of the square spiral where the prime ratio first drops below **20%**.

---

## Constraints

- Only **odd side lengths** are allowed.  
- The center number \(1\) is **not considered prime**.

---

## Solution

\[
\boxed{309}
\]

