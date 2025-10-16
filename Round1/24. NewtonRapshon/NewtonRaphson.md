
## Problem Statement

You are given a cubic equation:

$$
f(x) = x^3 - 7x^2 + 14x - 6
$$

Your task is to find **a root of this equation** starting from an initial guess $x_0 = 3$.

### Conditions:

* **Initial value:** $x_0 = 3$
* **Stopping criterion:** Stop iterating when

$$
|x_{n+1} - x_n| < 0.001
$$

or after **20 iterations**, whichever comes first.

Once you obtain the approximate root, **round it off to the nearest integer** and print it as the final answer.

---

### Example:

If your computed root is $x \approx 7.556$,
your output should be: 7



### Final Solution :

```
3
```


