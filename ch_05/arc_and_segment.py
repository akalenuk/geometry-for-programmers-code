from sympy import *

# the input is a pair of points (x1, y1), (x2, y2),
# and a pair of corresponding tangent vectors (dx1, dy1), (dx2, dy2)
x1, y1, dx1, dy1 = symbols('x1 y1 dx1 dy1')
x2, y2, dx2, dy2 = symbols('x2 y2 dx2 dy2')

# the circle's radius
r1 = symbols('r1')

# (ix, iy) is the point where the arc meets the line
ix, iy = symbols('ix iy')

# the output is now only one arc's center (ax1, ay1), 
# and we already know its radius from the input. 
# The other piece of output is the parameter t2 that says where the line ends
ax1, ay1, t2 = symbols('ax1 ay1 t2')

solutions = solve(
   [
    # if we rotate a tangent vectors 90 degrees, multiply it by "r1" and put it from the first point,
    # it will end up in the arc's centert
    x1 - r1*dy1 - ax1,
    y1 + r1*dx1 - ay1,
    # the intersection point lies on the tangent line positioned by parameter t2: 
    # (ix, iy) = (x2, y2) + t2*(dx2, dy2)
    x2 + dx2 * t2 - ix,
    y2 + dy2 * t2 - iy,
    # the intersection point also belongs to the arc, so the vector from it to the arc center is
    # orthogonal to the second tangent vector
    (ix-ax1)*dx2 + (iy-ay1)*dy2                                    
], (ax1, ay1, t2, ix, iy))

print (pycode(solutions))

