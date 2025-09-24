
# Definite Integration 

## Problem Statement

Compute the definite integral of the function

$$
f(x) = 2e^{x^2} - 3\sin(x) + 4\cos(2x)
$$

over the interval

$$
[0,\ \tfrac{\pi}{4}]
$$

That is, evaluate

$$
I = \int_{0}^{\pi/4} \big(2e^{x^2} - 3\sin x + 4\cos 2x\big)\,dx.
$$

> **Note:** $e^{x^2}$ does **not** have an elementary antiderivative, so an analytical closed-form is not expected — you must use a **numerical integration method** (composite Simpson, adaptive Simpson, Gauss–Legendre, etc.) to compute $I$ accurately.

---

## Input

* No input — all values are fixed.

---

## Output

* Print a **single integer**: the **integer part** of $I$.
  That is, if $I = 3.984$ you should print `3` (truncate the decimal part).

---

## Constraints / Notes for Participants

* Use a numerical integration method with sufficient accuracy so that the integer part is correct (safely accurate to at least 3 decimal places).
* Explain which numerical method you used and why the chosen number of subdivisions / tolerance is sufficient.
* Time/memory limits are standard — implement efficiently.

---

## Reference Result

Using a reliable numerical integration I get:

$$
I \approx 3.0848156539861051
$$

Integer part (truncate) =

$$
\boxed{3}
$$

---

## Reference Java Implementation (Composite Simpson)

This reference uses the composite Simpson rule with a large even number of subintervals for accuracy. It prints the integer part (truncated) of the computed integral.

```java
public class DefiniteIntegral {
    // f(x) = 2*e^{x^2} - 3*sin(x) + 4*cos(2x)
    static double f(double x) {
        return 2.0 * Math.exp(x * x) - 3.0 * Math.sin(x) + 4.0 * Math.cos(2.0 * x);
    }

    // Composite Simpson's rule on [a,b] with n even subdivisions
    static double compositeSimpson(double a, double b, int n) {
        if (n % 2 == 1) n++; // ensure even
        double h = (b - a) / n;
        double sum = f(a) + f(b);

        // Sum odd terms (4 * f(x_i)) and even terms (2 * f(x_i))
        for (int i = 1; i < n; i++) {
            double x = a + i * h;
            if (i % 2 == 0) sum += 2.0 * f(x);
            else sum += 4.0 * f(x);
        }

        return sum * (h / 3.0);
    }

    public static void main(String[] args) {
        double a = 0.0;
        double b = Math.PI / 4.0;

        // Choose a large even n for high accuracy. 100_000 is usually safe here.
        int n = 100_000;

        double integral = compositeSimpson(a, b, n);

        // Print the integer part (truncate decimal) as required
        int integerPart = (int) integral; // for positive integral this truncates toward zero
        System.out.println(integerPart);

        // (Optional debug lines; remove for the final submission)
        // System.out.println("Computed integral = " + integral);
    }
}
```

### Implementation notes

* I used `n = 100000` subdivisions (even). That yields high accuracy for this integrand on $[0,\pi/4]$. If you prefer, you can use an adaptive Simpson implementation with a tolerance like `1e-9`.
* Casting to `(int)` truncates the fractional part (for this positive integral that equals the integer part).
* If you run the program you should see output:

```
3
```


