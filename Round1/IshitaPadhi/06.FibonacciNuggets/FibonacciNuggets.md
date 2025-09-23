# Fibonacci Nugget Series

## Description
Consider the series:

$$
S(x) = F_1x + F_2x^2 + F_3x^3 + \cdots
$$

where \( F_k \) is the \( k \)-th Fibonacci number:  
\( F1 = 1, \; F2 = 1, \; F3 = 2, \; F4 = 3... \).

---

## Task
We say that \( x \) produces a **nugget** if the value of \( S(x) \) (evaluated to infinity) is a positive integer.  

Show that this infinite sum can be expressed in closed form as:

$$
S(x) = \frac{x}{1 - x - x^2}
$$

Write a program to find the sum of all integer nuggets of \( S(x) \) for:

$$
1 \leq n \leq 20
$$

where \( n = S(x) \) is the nugget value.

---

## Example

For \( x = 1/2 \):

$$
S\!\left(\tfrac{1}{2}\right) 
= \frac{\tfrac{1}{2}}{1 - \tfrac{1}{2} - \left(\tfrac{1}{2}\right)^2} 
= \frac{\tfrac{1}{2}}{1 - \tfrac{1}{2} - \tfrac{1}{4}} 
= \frac{\tfrac{1}{2}}{\tfrac{1}{4}} 
= 2
$$

Hence, \( 2 \) is a nugget.  

---

For \( x = 1/3 \):

$$
S\!\left(\tfrac{1}{3}\right) 
= \frac{\tfrac{1}{3}}{1 - \tfrac{1}{3} - \left(\tfrac{1}{3}\right)^2} 
= \frac{\tfrac{1}{3}}{1 - \tfrac{1}{3} - \tfrac{1}{9}} 
= \frac{\tfrac{1}{3}}{\tfrac{5}{9}} 
= \tfrac{3}{5}
$$

This is not an integer, so it is **not** a nugget.  

---

## Solution
The nuggets found in the range  are:

$$
2 \quad \text{and} \quad 15
$$

Thus, the sum of nuggets is:

$$
2 + 15 = 17
$$

---

## Final Answer
$$
\boxed{17}
$$
