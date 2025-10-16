## Problem: Buckets of Water -MEDIUM

(Question Inspiration: https://projecteuler.net/problem=758)

There are three buckets labelled S (small), M (medium), and L (large). Initially:
Bucket S contains a litres,
Bucket M contains b litres,
Bucket L is empty,

where a and b are coprime positive integers with a ≤ b, and L has size a + b litres.

You can pour water from one bucket to another. Once a pour starts, it cannot stop until either the source bucket is empty or the destination bucket is full.

Let P(a, b) be the minimal number of pourings needed to leave exactly 1 litre in bucket S.

Some examples:

P(3,5) = 4
P(7,11) = 10
P(13,21) = 34

For all coprime pairs of positive integers (a, b) with 2 ≤ a < b ≤ 50, find the sum of P(a, b).

Give your answer modulo 1 000 000 007.

## Solution

from math import gcd

def min_pours(a, b):
cap = (a, b, a+b) # capacities
start = (a, b, 0) # initial state
visited = {start: 0} # state -> steps
states = [start]

    while states:
        next_states = []
        for state in states:
            steps = visited[state]
            if state[0] == 1:
                return steps
            for i in range(3):
                for j in range(3):
                    if i != j and state[i] > 0 and state[j] < cap[j]:
                        s = list(state)
                        amt = min(s[i], cap[j]-s[j])
                        s[i] -= amt
                        s[j] += amt
                        nxt = tuple(s)
                        if nxt not in visited:
                            visited[nxt] = steps + 1
                            next_states.append(nxt)
        states = next_states
    return None  # should never happen

# Compute sum

MOD = 1_000_000_007
ans = 0
for a in range(2, 51):
for b in range(a+1, 51):
if gcd(a, b) == 1:
ans = (ans + min_pours(a, b)) % MOD

print(ans)
