from sympy import *

# the input is a pair of points (x1, y1), (x2, y2), 
# and a pair of corresponding tangent vectors (dx1, dy1), (dx2, dy2)
x1, y1, dx1, dy1 = symbols('x1 y1 dx1 dy1')
x2, y2, dx2, dy2 = symbols('x2 y2 dx2 dy2')

# the output is the arcs’ center points (ax1, ay1) and (ax2, ay2), 
ax1, ay1, ax2, ay2 = symbols('ax1 ay1 ax2 ay2')

# and corresponding radii r1 and r2
r1, r2 = symbols('r1 r2')

solutions = solve(
   [
    r2 - r1,  #radii are equal by design
    #both radius vectors are orthogonal to tangent vectors
    x1 + r1*dy1 - ax1,  
    y1 - r1*dx1 - ay1,
    x2 + r2*dy2 - ax2,
    y2 - r2*dx2 - ay2,
    # circles touch at some point, this means that the distance 
    # between their centers is the same as the sum of their radii
    (ax1-ax2)**2 + (ay1-ay2)**2 - (r1+r2)**2
], (ax1, ay1, ax2, ay2, r1, r2))

for s in solutions:
    print ()
    print ('ax1 = ' + pycode(s[0]))
    print ('ay1 = ' + pycode(s[1]))
    print ('ax2 = ' + pycode(s[2]))
    print ('ay2 = ' + pycode(s[3]))
    print ('r1 = ' + pycode(s[4]))
    print ('r2 = ' + pycode(s[5]))



