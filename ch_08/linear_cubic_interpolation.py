# see getting_cubic_interpolation.py
def P3(z1, z2, z3, z4, x):
    a = 5.4*z1 - 2.7*z2 - 5.4*z3 + 2.7*z4
    b = -4.2*z1 - 0.9*z2 + 7.2*z3 - 2.1*z4
    c = -2.2*z1 + 3.6*z2 - 1.8*z3 + 0.4*z4
    d = z1
    return a*x*x*x + b*x*x + c*x + d

# that's just linear interpolation
def P1(z1, z2, y):
    return z1*(1-y) + z2*y

z11 = 0.5; z12 = 0.6;
z21 = 0.4; z22 = 0.5;
z31 = 0.7; z32 = 0.9;
z41 = 0.6; z42 = 0.7;

# four linear y-interpolants
def z1(y): return P1(z11, z12, y)
def z2(y): return P1(z21, z22, y)
def z3(y): return P1(z31, z32, y)
def z4(y): return P1(z41, z42, y)

# and a single cubic x-interpolant
# that makes them into a two-variable function
def z(x, y): return P3(z1(y), z2(y), z3(y), z4(y), x)


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
ax.plot_wireframe(X, Y, Z, color='#339428')
ax.set_title('');
plt.show()
