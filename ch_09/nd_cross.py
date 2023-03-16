from sympy import *

e1, e2, e3, e4 = symbols('e1 e2 e3 e4')
a1, a2, a3, a4 = symbols('a1 a2 a3 a4')
b1, b2, b3, b4 = symbols('b1 b2 b3 b4')
c1, c2, c3, c4 = symbols('c1 c2 c3 c4')

# 2D cross product
A = Matrix([[e1, e2], [a1, a2]])
print(A.det())

# 3D cross product (also see SymPy cross method and ^ operator)
A = Matrix([[e1, e2, e3], [a1, a2, a3], [b1, b2, b3]])
print(A.det())

# 4D cross product
A = Matrix([[e1, e2, e3, e4], [a1, a2, a3, a4], [b1, b2, b3, b4], [c1, c2, c3, c4]])
print(A.det())
print(collect(A.det(), [e1, e2, e3, e4]))
