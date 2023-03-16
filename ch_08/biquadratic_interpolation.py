# the polynomial
def P2(z1, z2, z3, x):
    a = 2.0*z1 - 4.0*z2 + 2.0*z3
    b = -3.0*z1 + 4.0*z2 - z3
    c = z1
    return a*x*x + b*x + c

# Z-values
z11 = 0.3; z12 = 0.5; z13 = 0.9
z21 = 0.4; z22 = 0.7; z23 = 1.1
z31 = 0.8; z32 = 1.4; z33 = 1.5

# three y-interpolants
def z1(y): return P2(z11, z12, z13, y)
def z2(y): return P2(z21, z22, z23, y)
def z3(y): return P2(z31, z32, z33, y)

# and a single x-interpolant that brings them up together
def z(x, y): return P2(z1(y), z2(y), z3(y), x)


# plotting
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.interactive(True)
matplotlib.use('WebAgg')

x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)

X, Y = np.meshgrid(x, y)
Z = z(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.plot_wireframe(X, Y, Z, color='#457fd6')
ax.set_title('');
plt.show()
