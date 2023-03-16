from sympy import *

a1 = Matrix([[1, 0, -1], [0, 1, -1], [0, 0, 1]])
a2 = Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
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


# inversion

def minor(M, i, j):
    M_copy = M[:, :]
    M_copy.col_del(j)
    M_copy.row_del(i) 
    return M_copy

def cofactor(M):
    C = M[:, :]
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            determinant = minor(M, i, j).det() # this is the determinant in SymPy
            sign = 1 if i+j%2 == 1 else -1
            C[i, j] = sign*determinant
    return C

def not_a_real_inverse(M):
    # dividing by the determinant is optional
    return cofactor(M).T # / cofactor(M).det()

print("")
print("  real inverse:")
print(c.inv() * pt1)
print(c.inv() * pt2)
print(c.inv() * pt3)
print(c.inv() * pt4)

print("")
print("  inverse transformation, not a real inversion:")
print(not_a_real_inverse(c) * pt1)
print(not_a_real_inverse(c) * pt2)
print(not_a_real_inverse(c) * pt3)
print(not_a_real_inverse(c) * pt4)
