# Problem 02

The sum of the infinite series is $\frac{1}{5}(\frac{1}{5} - \frac{1}{7}) + (\frac{1}{5})^2((\frac{1}{5})^2 - (\frac{1}{7})^2) + (\frac{1}{5})^3((\frac{1}{5})^3 - (\frac{1}{7})^3) + \dots$ equal to:



---

## Solution

### Breaking Down the Series 

First, let's look at the general form of each term in the series. The nth term, let's call it $T_n$, can be written as:
$$T_n = \left(\frac{1}{5}\right)^n \left[ \left(\frac{1}{5}\right)^n - \left(\frac{1}{7}\right)^n \right]$$

By distributing the first part, we can simplify this expression:
$$T_n = \left(\frac{1}{5}\right)^{2n} - \left(\frac{1}{5}\right)^n \left(\frac{1}{7}\right)^n$$
$$T_n = \left(\frac{1}{25}\right)^n - \left(\frac{1}{35}\right)^n$$

The entire infinite series is the sum of these terms from $n=1$ to infinity. So, we can rewrite the problem as:
$$S = \sum_{n=1}^{\infty} \left[ \left(\frac{1}{25}\right)^n - \left(\frac{1}{35}\right)^n \right]$$

This can be split into two separate infinite geometric series:
$$S = \sum_{n=1}^{\infty} \left(\frac{1}{25}\right)^n - \sum_{n=1}^{\infty} \left(\frac{1}{35}\right)^n$$

***

### Applying the Geometric Series Formula 

The formula for the sum of an infinite geometric series is $S_{\infty} = \frac{a}{1-r}$, where **a** is the first term and **r** is the common ratio.

**1. For the first series:** $\sum (\frac{1}{25})^n$
* First term, $a_1 = \frac{1}{25}$
* Common ratio, $r_1 = \frac{1}{25}$
* Sum = $\frac{1/25}{1 - 1/25} = \frac{1/25}{24/25} = \frac{1}{24}$

**2. For the second series:** $\sum (\frac{1}{35})^n$
* First term, $a_2 = \frac{1}{35}$
* Common ratio, $r_2 = \frac{1}{35}$
* Sum = $\frac{1/35}{1 - 1/35} = \frac{1/35}{34/35} = \frac{1}{34}$

***


Now, we just need to subtract the sum of the second series from the sum of the first:
$$S = \frac{1}{24} - \frac{1}{34}$$

To subtract these fractions, we find a common denominator, which is 408.
$$S = \frac{17}{408} - \frac{12}{408} = \frac{17 - 12}{408} = \frac{5}{408}$$



---

**Answer:** The correct answer is  $\frac{5}{408}$.