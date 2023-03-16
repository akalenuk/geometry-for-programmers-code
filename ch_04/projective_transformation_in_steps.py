from sympy import *

# transformation matrix coefficients
a, b, c, d, e, f, g, h, i = symbols('a b c d e f g h i')

# points before the transformation
x1, y1, x2, y2, x3, y3, x4, y4 = symbols('x1 y1 x2 y2 x3 y3 x4 y4')

# points after the transformation
xt1, yt1, xt2, yt2, xt3, yt3, xt4, yt4 = symbols('xt1 yt1 xt2 yt2 xt3 yt3 xt4 yt4')

solution_1 = solve([
	xt1 * i - c, 
	yt1 * i - f, 
	i - 1 
], (c, f, i))
print("  c, f, i:")
print(solution_1)

c = xt1
f = yt1
i = 1
solution_2 = solve([
	xt2 * g + xt2 * i - a - c, 
	yt2 * g + yt2 * i - d - f, 
	xt4 * h + xt4 * i - b - c, 
	yt4 * h + yt4 * i - e - f, 
], (a, b, d, e))
print("")
print("  a, b, d, e:")
print(solution_2)

a = g*xt2 - xt1 + xt2
d = g*yt2 - yt1 + yt2
b = h*xt4 - xt1 + xt4
e = h*yt4 - yt1 + yt4

solution_3 = solve([
	xt3 * g + xt3 * h + xt3 * i - a - b - c, 
	yt3 * g + yt3 * h + yt3 * i - d - e - f, 
], (g, h))
print("")
print("  g, h:")
print(solution_3)

