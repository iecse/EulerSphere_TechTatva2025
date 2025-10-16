## DiFi (Difficulty: Medium)

If $x = x(t)$ is the solution of the differential equation $(t+1)dx = [2x + (t+1)^4]dt$, with the initial condition $x(0) = 2$, find the value of $x(1)$.

***

## Solution

This is a **first-order linear differential equation**. We can solve it by rearranging it into the standard form and using an integrating factor. 

### Step 1: Rearrange into Standard Form

First, let's rearrange the equation into the form $\frac{dx}{dt} + P(t)x = Q(t)$.

$$(t+1)\frac{dx}{dt} = 2x + (t+1)^4$$
$$\frac{dx}{dt} = \frac{2}{t+1}x + (t+1)^3$$
$$\frac{dx}{dt} - \frac{2}{t+1}x = (t+1)^3$$

From this, we can identify:
* $P(t) = -\frac{2}{t+1}$
* $Q(t) = (t+1)^3$

### Step 2: Find the Integrating Factor (I.F.)

The integrating factor is given by the formula $I.F. = e^{\int P(t) dt}$.

$$I.F. = e^{\int -\frac{2}{t+1} dt}$$
$$I.F. = e^{-2 \ln(t+1)} = e^{\ln((t+1)^{-2})}$$
$$I.F. = (t+1)^{-2} = \frac{1}{(t+1)^2}$$

### Step 3: Find the General Solution

The general solution is found using the formula $x \cdot (I.F.) = \int Q(t) \cdot (I.F.) dt + C$.

$$x \cdot \frac{1}{(t+1)^2} = \int (t+1)^3 \cdot \frac{1}{(t+1)^2} dt + C$$
$$\frac{x}{(t+1)^2} = \int (t+1) dt + C$$
$$\frac{x}{(t+1)^2} = \frac{(t+1)^2}{2} + C$$

Multiplying by $(t+1)^2$ gives the general solution for $x(t)$:
$$x(t) = \frac{(t+1)^4}{2} + C(t+1)^2$$

### Step 4: Use the Initial Condition to Find C

We are given that $x(0) = 2$. Let's substitute $t=0$ and $x=2$ into the general solution to find the constant $C$.

$$2 = \frac{(0+1)^4}{2} + C(0+1)^2$$
$$2 = \frac{1}{2} + C$$
$$C = 2 - \frac{1}{2} = \frac{3}{2}$$

### Step 5: Find the Final Value

Now we have the particular solution:

$$x(t) = \frac{(t+1)^4}{2} + \frac{3}{2}(t+1)^2$$

Finally, we can find the value of $x(1)$ by substituting $t=1$:

$$x(1) = \frac{(1+1)^4}{2} + \frac{3}{2}(1+1)^2$$
$$x(1) = \frac{2^4}{2} + \frac{3}{2}(2^2)$$
$$x(1) = \frac{16}{2} + \frac{3}{2}(4)$$
$$x(1) = 8 + 6 = 14$$

**Therefore, the value of $x(1)$ is 14.**