import math
from itertools import product

def prufer_to_tree(sequence):
    n = len(sequence) + 2
    degree = [1] * n
    
    for num in sequence:
        degree[num] += 1
    
    edges = []
    ptr = 0
    
    for i in range(len(sequence)):
        while degree[ptr] != 1:
            ptr += 1
        
        leaf = ptr
        node = sequence[i]
        edges.append((leaf, node))
        
        degree[ptr] -= 1
        degree[node] -= 1
        
        if degree[node] == 1 and node < ptr:
            ptr = node
    
    remaining = [i for i in range(n) if degree[i] == 1]
    edges.append((remaining[0], remaining[1]))
    
    return edges

def compute_spectral_product(edges, n):
    degree = [0] * n
    
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    product = 1
    for d in degree:
        product *= d
    
    return product

def is_perfect_square(n):
    if n <= 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def solve():
    n = 9
    prufer_length = n - 2
    
    valid_products = set()
    
    for sequence in product(range(n), repeat=prufer_length):
        try:
            edges = prufer_to_tree(list(sequence))
            spectral_product = compute_spectral_product(edges, n)
            
            if is_perfect_square(spectral_product) and spectral_product % 7 == 0:
                valid_products.add(spectral_product)
        except:
            continue
    
    return sum(valid_products)

print(solve())