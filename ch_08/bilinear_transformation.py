from sympy import *

# the symbols are more or less like in the book, 
# only the initial positions of points now lose the “i” index for brevity
a11, a12, a13, a14 = symbols('a11 a12 a13 a14')
a21, a22, a23, a24 = symbols('a21 a22 a23 a24')
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
y1, y2, y3, y4 = symbols('y1 y2 y3 y4')
xt1, xt2, xt3, xt4 = symbols('xt1 xt2 xt3 xt4')
yt1, yt2, yt3, yt4 = symbols('yt1 yt2 yt3 yt4')

# the system consists of 4 pairs of “x transforms to xt” 
# and “y transforms to yt” equations
system = [
    a11*x1*y1 + a12*x1 + a13*y1 + a14 - xt1,
    a21*x1*y1 + a22*x1 + a23*y1 + a24 - yt1,
    a11*x2*y2 + a12*x2 + a13*y2 + a14 - xt2,
    a21*x2*y2 + a22*x2 + a23*y2 + a24 - yt2,
    a11*x3*y3 + a12*x3 + a13*y3 + a14 - xt3,
    a21*x3*y3 + a22*x3 + a23*y3 + a24 - yt3,
    a11*x4*y4 + a12*x4 + a13*y4 + a14 - xt4,
    a21*x4*y4 + a22*x4 + a23*y4 + a24 - yt4
]

# this runs for 0.26 seconds (on the reference machine AKA my PC)
all_as = solve(system, (a11, a12, a13, a14, a21, a22, a23, a24))

if False: # alternative take
    x_system = [
        a11*x1*y1 + a12*x1 + a13*y1 + a14 - xt1,
        a11*x2*y2 + a12*x2 + a13*y2 + a14 - xt2,
        a11*x3*y3 + a12*x3 + a13*y3 + a14 - xt3,
        a11*x4*y4 + a12*x4 + a13*y4 + a14 - xt4
    ]

    y_system = [
        a21*x1*y1 + a22*x1 + a23*y1 + a24 - yt1,
        a21*x2*y2 + a22*x2 + a23*y2 + a24 - yt2,
        a21*x3*y3 + a22*x3 + a23*y3 + a24 - yt3,
        a21*x4*y4 + a22*x4 + a23*y4 + a24 - yt4
    ]

    # this runs in 0.18 seconds
    axs = solve(x_system, (a11, a12, a13, a14))
    ays = solve(y_system, (a21, a22, a23, a24))


# testing points
xis = [0.0, 1.0, 1.0, 0.0]
yis = [0.0, 0.0, 1.0, 1.0]
xts = [0.25, 0.75, 1.25, 0.25]
yts = [0.25, 0.25, 1.25, 0.75]

# substitute the solution's argument with numeric points
a11_ = all_as[a11].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])
a12_ = all_as[a12].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])
a13_ = all_as[a13].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])
a14_ = all_as[a14].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])
a21_ = all_as[a21].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])
a22_ = all_as[a22].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])
a23_ = all_as[a23].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])
a24_ = all_as[a24].subs([(x1, xis[0]), (x2, xis[1]), (x3, xis[2]), (x4, xis[3]),
                         (y1, yis[0]), (y2, yis[1]), (y3, yis[2]), (y4, yis[3]),
                         (xt1, xts[0]), (xt2, xts[1]), (xt3, xts[2]), (xt4, xts[3]),
                         (yt1, yts[0]), (yt2, yts[1]), (yt3, yts[2]), (yt4, yts[3])])


# make the plot
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# points from a standard square
xs_before = []
ys_before = []
xs_after = []
ys_after = []
for i in range(10 + 1):
    for j in range(10 + 1):
        x = j / 10.
        y = i / 10.
        xs_before += [x]
        ys_before += [y]
        xs_after += [a11_*x*y + a12_*x + a13_*y + a14_]
        ys_after += [a21_*x*y + a22_*x + a23_*y + a24_]

fig, ax = plt.subplots()
ax.set(xlabel='x', ylabel='y', title='Bilinear transforamtion')
ax.grid()
plt.scatter(xs_before, ys_before)
plt.scatter(xs_after, ys_after)
fig.savefig("bilinear_transformation.png")
plt.show()
