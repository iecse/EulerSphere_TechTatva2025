## Solution

# brute-force (straightforward)

def letter_value(ch): return ord(ch) - ord('A')
W_text = "PRIME"
x = [letter_value(c) for c in W_text] # [15,17,8,12,4]

def V_of_k(k):
    digits = [(k * xi) % 26 for xi in x]
    val = 0
    for d in digits:
        val = val*26 + d
    return val

total = 0
for k in range(1, 1001):
    if __import__('math').gcd(k, 26) == 1:
        total += V_of_k(k)
    print(total) # prints 2851886142

# Last 12 digits:

print(str(total).zfill(12)[-12:]) # "002851886142"