from sympy import *

z1, z2, z3, a, b, c = symbols('z1 z2 z3 a b c')

print(solve([
    c - z1,
    a * 0.25 + b * 0.5 + c - z2,
    a + b + c - z3,
    ], (a, b, c)))
