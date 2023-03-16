from sympy import *

a1, a2, a3, a4 = symbols('a1 a2 a3 a4')
b1, b2, b3, b4 = symbols('b1 b2 b3 b4')
c1, c2, c3, c4 = symbols('c1 c2 c3 c4')
d1, d2, d3, d4 = symbols('d1 d2 d3 d4')

# 2D box product
A = Matrix([[a1, a2], [b1, b2]])
print(A.det())

# 3D box AKA triple probuct (also see SymPy dot and cross methods, and a & (b ^ c) construction)
A = Matrix([[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]])
print(A.det())

#4D box product
A = Matrix([[a1, a2, a3, a4], [b1, b2, b3, b4], [c1, c2, c3, c4], [d1, d2, d3, d4]])
print(A.det())
