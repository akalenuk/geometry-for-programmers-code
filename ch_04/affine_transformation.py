from sympy import *

# Affine transformation in 2D looks like this: 
#   xt = a11*x + a12 *y + a13; 
#   yt = a21*x + a22*y + a23, 
# we need 6 coefficients to define it.
a11, a12, a13, a21, a22, a23 = symbols('a11 a12 a13 a21 a22 a23')

# It is a 3-point transformation so we need to define 3 starting points.
x1, y1, x2, y2, x3, y3 = symbols('x1 y1 x2 y2 x3 y3')

# And, since we are going to infer the coefficients from the actual 
# transformation of 3 points, we need to define the 3 ending points as well.
xt1, yt1, xt2, yt2, xt3, yt3 = symbols('xt1 yt1 xt2 yt2 xt3 yt3')

solution = solve([
    a11 * x1 + a12 * y1 + a13 - xt1,
    a21 * x1 + a22 * y1 + a23 - yt1,
    a11 * x2 + a12 * y2 + a13 - xt2,
    a21 * x2 + a22 * y2 + a23 - yt2,
    a11 * x3 + a12 * y3 + a13 - xt3,
    a21 * x3 + a22 * y3 + a23 - yt3
], (a11, a12, a13, a21, a22, a23))

print(solution)
