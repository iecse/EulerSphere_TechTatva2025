## Problem: Hilbert’s Prime Hotel

An infinite number of people (numbered 1, 2, 3, …) are lined up to get a room in Hilbert’s Prime Hotel, which has infinitely many blocks and infinitely many rooms per block.
Rooms are assigned as follows:
Person n takes the first vacant room in the lowest-numbered block that is either empty or where the most recent occupant m satisfies m + n is prime.

Define Q(b, r) = n if person n occupies room r in block b, 0 otherwise.

Examples:
Q(1,1) = 1, Q(1,2) = 2, Q(1,3) = 3, Q(2,1) = 5, Q(3,1) = 7
Find the sum of all Q(b, r) for positive integers b and r such that

b×r=980100

Give the last 8 digits of your answer.

## Solution

import math

def sieve(n):
is_prime = [True]*(n+1)
is_prime[0]=is_prime[1]=False
for i in range(2,int(n\*\*0.5)+1):
if is_prime[i]:
for j in range(i*i,n+1,i):
is_prime[j]=False
return is_prime

def hilbert_prime_hotel(limit_b, limit_r, target_product): # Prime sieve for fast primality check
primes = sieve(2000000)

    # Store last occupant of each block and room count
    last_occupant = {}
    room_count = {}
    table = {}  # (b, r) -> n

    max_r = target_product // 1  # worst case
    n = 1
    while True:
        assigned = False
        b = 1
        while True:
            if b not in last_occupant:
                # Empty block -> assign here
                last_occupant[b] = n
                room_count[b] = 1
                table[(b,1)] = n
                break
            else:
                m = last_occupant[b]
                if primes[m+n]:
                    # Valid block
                    room_count[b] += 1
                    last_occupant[b] = n
                    table[(b, room_count[b])] = n
                    break
            b += 1

        # stop when we have filled enough
        if max(table.keys(), key=lambda x: x[1])[1] >= limit_r:
            break
        n += 1

    # sum for factor pairs
    ans = 0
    for b in range(1, int(math.isqrt(target_product))+1):
        if target_product % b == 0:
            r = target_product // b
            if (b,r) in table:
                ans += table[(b,r)]
            if (r,b) in table and r!=b:
                ans += table[(r,b)]
    return ans % (10**8)

target = 980100
print(hilbert_prime_hotel(1000, target, target))
