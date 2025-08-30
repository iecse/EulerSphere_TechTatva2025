from itertools import permutations

def is_magic(p):
    return all(sum(p[3*i:3*i+3])==15 for i in range(3)) and \
           all(sum(p[i::3])==15 for i in range(3)) and \
           sum(p[0::4])==15 and sum(p[2:7:2])==15

squares=[p for p in permutations(range(1,10)) if is_magic(p)]

print(len(squares))