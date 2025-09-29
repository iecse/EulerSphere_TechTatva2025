# The Painted Ball Paradox
## Difficulty – Medium

A box has 4 white and 6 black balls (10 total). One ball is chosen uniformly at random, **painted red** (its original color remains white/black for counting), and returned to the box. Then **two balls are drawn without replacement**.

Define:
- \(p_1\): the probability that **both drawn balls are black**, given that the **red ball is not drawn** in the two draws.  
- \(p_2\): the probability that the **red ball was originally black**, given that it was drawn.  
- \(E\): the **expected number of black balls** in the two draws.  

Let
$$
A \;=\; p_1 + p_2 + E.
$$  

Write \(A\) as a reduced fraction:

$$
\frac{m}{n}, \quad \gcd(m,n)=1,
$$

and report \(m+n\).


## Solution

### Step 1: Compute \(p_1\)

Let \(C_B\) = event “painted ball originally black,” and \(C_W\) = event “painted ball originally white.”  

Priors:
$$
\Pr(C_B)=\tfrac{6}{10}, 
\qquad
\Pr(C_W)=\tfrac{4}{10}.
$$  

If the red ball is **not drawn** (event \(R\)), then 9 balls are available for selection:

- Under \(C_B\): \(5B+4W\).  
- Under \(C_W\): \(6B+3W\).  

Probability that two draws avoid a specific ball:
$$
\Pr(R \mid C_B)=\Pr(R \mid C_W)=\frac{\binom{9}{2}}{\binom{10}{2}}
=\frac{36}{45}=\tfrac{4}{5}.
$$  

Posterior weights remain the same as priors:
$$
\Pr(C_B\mid R)=\tfrac{6}{10}, 
\qquad
\Pr(C_W\mid R)=\tfrac{4}{10}.
$$  

Now,  
- If \(C_B\):  
$$
\Pr(\text{2B}\mid R,C_B)=\frac{\binom{5}{2}}{\binom{9}{2}}
=\frac{10}{36}=\tfrac{5}{18}.
$$  
- If \(C_W\):  
$$
\Pr(\text{2B}\mid R,C_W)=\frac{\binom{6}{2}}{\binom{9}{2}}
=\frac{15}{36}=\tfrac{5}{12}.
$$  

Thus,
$$
p_1=\frac{6}{10}\cdot\frac{5}{18}+\frac{4}{10}\cdot\frac{5}{12}
=\tfrac{1}{3}.
$$  


### Step 2: Compute \(p_2\)

Event \(D\): “red ball is drawn.”  

Regardless of original color,  
$$
\Pr(D\mid C_B)=\Pr(D\mid C_W)=\frac{2}{10}.
$$  

By Bayes:
$$
p_2=\Pr(C_B\mid D)
=\frac{\Pr(C_B)\Pr(D\mid C_B)}
       {\Pr(C_B)\Pr(D\mid C_B)+\Pr(C_W)\Pr(D\mid C_W)}.
$$  

Substitute:
$$
p_2=\frac{\tfrac{6}{10}\cdot\tfrac{2}{10}}
          {\tfrac{6}{10}\cdot\tfrac{2}{10}+\tfrac{4}{10}\cdot\tfrac{2}{10}}
=\frac{12}{20}=\tfrac{3}{5}.
$$  


### Step 3: Compute \(E\)

Let \(X\) = number of black balls in two draws.  

By linearity of expectation:
$$
E[X]=\mathbb{E}[X_1]+\mathbb{E}[X_2]
=2\cdot \Pr(\text{single draw is black}).
$$  

Painting does not change total counts (still \(6B\) out of 10):  
$$
\Pr(\text{black})=\tfrac{6}{10}=\tfrac{3}{5}.
$$  

So,
$$
E=2\cdot\tfrac{3}{5}=\tfrac{6}{5}.
$$  


### Step 4: Combine

$$
A=p_1+p_2+E
=\tfrac{1}{3}+\tfrac{3}{5}+\tfrac{6}{5}.
$$  

Common denominator 15:
$$
A=\tfrac{5}{15}+\tfrac{9}{15}+\tfrac{18}{15}
=\tfrac{32}{15}.
$$  

So,
$$
m=32,\quad n=15,\quad m+n=47.
$$  


## Final Answer
$$
\boxed{47}
$$
