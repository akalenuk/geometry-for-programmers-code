from sympy import *

ax, bx, cx, dx = symbols('ax bx cx dx')
ay, by, cy, dy = symbols('ay by cy dy')
x1, x2, dx1, dx2 = symbols('x1 x2 dx1 dx2')
y1, y2, dy1, dy2 = symbols('y1 y2 dy1 dy2')

x_system = [
    dx - x1,
    cx - dx1,
    ax + bx + cx + dx - x2,
    3*ax + 2*bx + cx - dx2
]

y_system = [
    dy - y1,
    cy - dy1,
    ay + by + cy + dy - y2,
    3*ay + 2*by + cy - dy2
]

axs = solve(x_system, (ax, bx, cx, dx))
ays = solve(y_system, (ay, by, cy, dy))

print("  ax and ay coefficients:")
print(axs)
print(ays)

# the curve
def Px(t, xs, dxs):
    ax = dxs[0] + dxs[1] + 2*xs[0] - 2*xs[1]
    bx = -2*dxs[0] - dxs[1] - 3*xs[0] + 3*xs[1]
    cx = dxs[0]
    dx = xs[0]
    return ax*t**3 + bx*t**2 + cx*t + dx

def Py(t, ys, dyx):
    return Px(t, ys, dys) # they share the same formula

# testing points and tangents
xs = [0.25, 0.75]
ys = [0.25, 0.75]
dxs = [0.025, -0.125]
dys = [0.8, -0.7]

# make the plot
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# polynomial curve
t = np.arange(-0.1, 1.1, 0.01)
Pxs = Px(t, xs, dxs)
Pys = Py(t, ys, dys)

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Parametric polynomial curve with tangents')
ax.grid()
plt.scatter(xs, ys)
plt.arrow(xs[0], ys[0], dxs[0], dys[0])
plt.arrow(xs[1], ys[1], dxs[1], dys[1])
fig.savefig("parametric_polynomial_tangents.png")
plt.show()
