# Pythagorean Triple Tiling

## Description

A **Pythagorean triple** is a set of integers \(a, b, c\) such that:

$$
a^2 + b^2 = c^2
$$

Such a triple represents the sides of a right triangle.

---

## Tiling Condition

Now imagine trying to tile a \( c \times c \) square using 4 copies of such a triangle.  

For this tiling to perfectly fill the square without gaps, the following condition must hold:

c % (c - b) = 0 

That is, the difference between the hypotenuse \( c \) and the longer leg \( b \) must exactly divide \( c \).

---

## Figures

Below are illustrations showing how Pythagorean triples can tile a square:

<img width="299" height="137" alt="image" src="https://github.com/user-attachments/assets/906c0674-1c74-43eb-a0c3-ba2d7a06ff8f" />


## Task

Given an integer \( N \), find the total number of valid Pythagorean triples \((a, b, c)\) such that:

1. \( a < b < c <= N )  
2. \( a^2 + b^2 = c^2 \)  
3. The tiling condition holds: \( c % (c - b) = 0 \)  

Compute the total count for:

$$
N = 500
$$

---

## Solution

The total number of valid triples is:

$$
199
$$
