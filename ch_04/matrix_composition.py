from sympy import *

# translation to 0, 0
a1 = Matrix([[1, 0, -1], [0, 1, -1], [0, 0, 1]])

# rotation
a2 = Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])

# translation back
a3 = Matrix([[1, 0, 1], [0, 1, 1], [0, 0, 1]])

# composition
c=a3*a2*a1
print("  composition:")
print(c)

p1 = Matrix([0.75, 0.5, 1])
p2 = Matrix([1.25, 0.5, 1])
p3 = Matrix([1.25, 1.5, 1])
p4 = Matrix([0.75, 1.5, 1])
print("")
print("  points:")
print(p1)
print(p2)
print(p3)
print(p4)

pt1 = c * p1
pt2 = c * p2
pt3 = c * p3
pt4 = c * p4

print("")
print("  transformed points:")
print(pt1)
print(pt2)
print(pt3)
print(pt4)

