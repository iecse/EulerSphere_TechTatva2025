# The M-Centered Selection
## Difficulty – Hard

From the 26 English letters (A–Z), we want to choose **7 distinct letters** arranged in alphabetical order.  
The following conditions apply:

1. The **4th letter** must be **M**.  
2. Exactly **two vowels** (A, E, I, O, U) must appear among the 7 letters.  
3. The **smallest letter** chosen must be from {A, B, C}.  
4. The **largest letter** chosen must be from {U, V, W, X, Y, Z}.  
5. There must be **strictly more letters on the right of M** than on the left.  

Find the total number of such valid selections.


## Solution

### Step 1: Distribution of letters
Since M is fixed as the 4th letter, the split is:

- Case 1: 1 left, 5 right  
- Case 2: 2 left, 4 right  

We cannot have 3 left and 3 right, since right must be strictly more.


### Step 2: Left side (before M)
Letters available: A–L (12 total).  

Condition: at least one must be from  

$$
\{A, B, C\}
$$


### Step 3: Right side (after M)
Letters available: N–Z (13 total).  

Condition: at least one must be from  

$$
\{U, V, W, X, Y, Z\}
$$


### Step 4: Vowel restriction
We need exactly 2 vowels in total.  

Left vowels:  

$$
\{A, E, I\}
$$

Right vowels:  

$$
\{O, U\}
$$

So the possible splits are:  

$$
(\text{vowels left}) + (\text{vowels right}) = 2
$$


## Case Analysis

### Case 1: 1 left, 5 right
- Left choice: pick 1 from A–L, must include {A, B, C}.  

Number of ways:  
$$
3
$$

- Right choice: pick 5 from N–Z, must include {U, V, W, X, Y, Z}.  

Number of ways:  
$$
\binom{13}{5} - \binom{7}{5} = 1287 - 21 = 1266
$$

- Vowel condition:  
  - If left is vowel: need 1 vowel on right.  
  - If left is consonant: need 2 vowels (O and U) on right.  

So total for Case 1 is:  

$$
(3 \times \binom{11}{4}) + (9 \times \binom{11}{3})
$$

$$
= (3 \times 330) + (9 \times 165) = 990 + 1485 = 2475
$$


### Case 2: 2 left, 4 right
- Left choice: pick 2 from A–L, with at least one from {A, B, C}.  

Number of ways:  
$$
\binom{12}{2} - \binom{9}{2} = 66 - 36 = 30
$$

- Right choice: pick 4 from N–Z, with at least one from {U, V, W, X, Y, Z}.  

Number of ways:  
$$
\binom{13}{4} - \binom{7}{4} = 715 - 35 = 680
$$


#### Vowel distributions:

1. **2 vowels left, 0 right**  

$$
\binom{3}{2} \times \binom{9}{0} \times \binom{11}{4} 
= 3 \times 1 \times 330 = 990
$$


2. **1 vowel left, 1 right**  

$$
(3 \times 2) \times \binom{9}{1} \times \binom{11}{3} 
= 6 \times 9 \times 165 = 8910
$$


3. **0 vowels left, 2 right**  

$$
1 \times \binom{9}{2} \times \binom{11}{2} 
= 36 \times 55 = 1980
$$


So total for Case 2 is:  

$$
990 + 8910 + 1980 = 11,880
$$


## Step 5: Final Answer
Adding both cases:

$$
2475 + 11,880 = 14,355
$$

Thus, the total number of valid selections is:

$$
\boxed{14,355}
$$
