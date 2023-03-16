from sympy import *

z1, z2, z3, z4, a, b, c, d = symbols('z1 z2 z3 z4 a b c d')

print(solve([
    d - z1,
    a * 1./27. + b * 1./9. + c * 1./3. + d - z2,
    a * 8./27. + b * 4./9. + c * 1./3. + d - z3,
    a + b + c + d - z4,
    ], (a, b, c, d)))
