from sympy import *

ax, bx, cx, dx = symbols('ax bx cx dx')
ay, by, cy, dy = symbols('ay by cy dy')
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
y1, y2, y3, y4 = symbols('y1 y2 y3 y4')

# as you can see, the systems are identical. 
# It’s just “x” becomes “y” in the latter. In cases such as this, 
# you can save yourself some time on symbolic computation, 
# just solve one and use its solution for every coordinate.
x_system = [
    dx - x1,
    (1/27)*ax + (1/9)*bx + (1/3)*cx + dx - x2,
    (8/27)*ax + (4/9)*bx + (2/3)*cx + dx - x3,
    ax + bx + cx + dx - x4
]

y_system = [
    dy - y1,
    (1/27)*ay + (1/9)*by + (1/3)*cy + dy - y2,
    (8/27)*ay + (4/9)*by + (2/3)*cy + dy - y3,
    ay + by + cy + dy - y4
]

axs = solve(x_system, (ax, bx, cx, dx))
ays = solve(y_system, (ay, by, cy, dy))

print("  ax and ay coefficients:")
print(axs)
print(ays)


# the curve
def Px(t, xs):
    ax = -4.5*xs[0] + 13.5*xs[1] - 13.5*xs[2] + 4.5*xs[3]
    bx = 9.0*xs[0] - 22.5*xs[1] + 18.0*xs[2] - 4.5*xs[3]
    cx = -5.5*xs[0] + 9.0*xs[1] - 4.5*xs[2] + xs[3]
    dx = xs[0]
    return ax*t**3 + bx*t**2 + cx*t + dx

def Py(t, ys):
    return Px(t, ys) # they share the same formula

# testing points
xs = [0.25, 0.75, 0.75, 0.25]
ys = [0.25, 0.25, 0.75, 0.75]

# make the plot
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# polynomial curve
t = np.arange(-0.05, 1.05, 0.01)
Pxs = Px(t, xs)
Pys = Py(t, ys)

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Parametric polynomial curve')
ax.grid()
plt.scatter(xs, ys)
fig.savefig("parametric_polynomial.png")
plt.show()
