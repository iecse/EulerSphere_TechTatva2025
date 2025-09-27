def matrix_from_e_p_q(e, p, q):
    a = e + p
    b = e + q
    c = e - p - q
    d = e - 2*p - q
    f = e + 2*p + q
    g = e + p + q
    h = e - q
    i = e - p
    return (a,b,c,d,e,f,g,h,i)

def is_valid_grid(grid):
    return all(0 <= x <= 9 for x in grid)

def is_magic(grid):
    a,b,c,d,e,f,g,h,i = grid
    S = a+b+c
    return (d+e+f == S and g+h+i == S and
            a+d+g == S and b+e+h == S and c+f+i == S and
            a+e+i == S and c+e+g == S)

def count_magic_grids():
    grids = set()
    for e in range(10):
        for p in range(-9, 10):
            for q in range(-9, 10):
                grid = matrix_from_e_p_q(e, p, q)
                if is_valid_grid(grid) and is_magic(grid):
                    grids.add(grid)
    return len(grids)

print(count_magic_grids())
