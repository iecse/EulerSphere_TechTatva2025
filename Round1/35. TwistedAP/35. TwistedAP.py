import math
from itertools import product

n, limit = 5, 20
total = 0

for a, d in product(range(1, limit+1), repeat=2):
    terms = [a + i*d for i in range(n)]
    if int(sum(terms)**0.5)**2 == sum(terms) and round(math.prod(terms)**(1/3))**3 == math.prod(terms):
        total += a + d

print(total)
