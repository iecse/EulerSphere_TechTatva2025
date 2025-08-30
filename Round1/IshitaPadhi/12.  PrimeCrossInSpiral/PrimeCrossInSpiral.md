**DESCRIPTION**

 Prime Cross in Spiral

Starting from the number 1 at the center of a square spiral and moving anticlockwise, we form layers of increasing side length.

For example, a spiral with side length 5 looks like this:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13


The numbers along the two diagonals are:
21, 7, 1, 3, 13, 17, 5, 1, 9, 25.

Out of these, 7, 3, 13, 17, 5 are prime.
That’s 5 primes out of 9 diagonal numbers, giving a ratio of about 55.5%.

Task
Continue building larger and larger spirals (always with odd side lengths: 1, 3, 5, 7, 9, …).
Find the first side length of the spiral for which the ratio of primes on both diagonals falls below 20%.

Input
No input required.

Output
A single integer: the side length of the square spiral where the prime ratio first drops below 20%.

Constraints

The spiral is built with odd side lengths only.

The center number (1) is not considered prime.


**SOLUTION**

309
