import sympy as sp

x = sp.symbols('x')
M = sp.Matrix([[x+2, 3, 1], [2, x-1, 4], [1, 2, x+3]])
det_M = sp.expand(M.det())
poly = sp.Poly(det_M, x)
c2 = poly.nth(2)
N = c2**3 + 7*c2**2 - 15*c2 + 100
result = N % 1000000007
print(result)