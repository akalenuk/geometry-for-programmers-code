from sympy import *

# four coefficients for the linear transformation
a11, a12, a21, a22 = symbols('a11 a12 a21 a22')

# two points before the transformation
x1, y1, x2, y2 = symbols('x1 y1 x2 y2')

# two points after the transforamtion
xt1, yt1, xt2, yt2 = symbols('xt1 yt1 xt2 yt2')

solution = solve([
    a11 * x1 + a12 * y1 - xt1,
    a21 * x1 + a22 * y1 - yt1,
    a11 * x2 + a12 * y2 - xt2,
    a21 * x2 + a22 * y2 - yt2
], (a11, a12, a21, a22))

print(solution)
