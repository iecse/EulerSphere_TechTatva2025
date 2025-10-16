# Pairs with GCD 6  
## Question Difficulty – Easy

Let \(m\) and \(n\), with \(m < n\), be two 2-digit numbers.  
Find the total number of ordered pairs \((m,n)\) such that  

$$
\gcd(m,n) = 6.
$$


## Solution:

Let  

$$
m = 6a, \quad n = 6b.
$$

Then,  

$$
\gcd(m,n) = 6 \;\; \implies \;\; \gcd(a,b) = 1.
$$

Since \(m,n\) are two-digit numbers:  

$$
10 \leq m \leq 99, \quad 10 \leq n \leq 99,
$$  

which gives:  

$$
10 \leq 6a \leq 99 \;\; \implies \;\; 2 \leq a \leq 16,
$$  

$$
10 \leq 6b \leq 99 \;\; \implies \;\; 2 \leq b \leq 16.
$$  

So, we need coprime pairs \(a,b\) such that  

$$
2 \leq a < b \leq 16.
$$


### Step 1: Listing coprime pairs  

- For \(a=2\): \(b = 3,5,7,9,11,13,15\)  
- For \(a=3\): \(b = 4,5,7,8,10,11,13,14,16\)  
- For \(a=4\): \(b = 5,7,9,11,13,15\)  
- For \(a=5\): \(b = 6,7,8,9,11,12,13,14,16\)  
- For \(a=6\): \(b = 7,11,13\)  
- For \(a=7\): \(b = 8,9,10,11,12,13,15,16\)  
- For \(a=8\): \(b = 9,11,13,15\)  
- For \(a=9\): \(b = 10,11,13,14,16\)  
- For \(a=10\): \(b = 11,13\)  
- For \(a=11\): \(b = 12,13,14,15,16\)  
- For \(a=12\): \(b = 13\)  
- For \(a=13\): \(b = 14,15,16\)  
- For \(a=14\): \(b = 15\)  
- For \(a=15\): \(b = 16\)  


### Step 2: Count  

Counting all possibilities, we obtain:  

$$
64 \;\; \text{ordered pairs } (m,n).
$$


## Final Answer:

$$
\boxed{64}
$$
