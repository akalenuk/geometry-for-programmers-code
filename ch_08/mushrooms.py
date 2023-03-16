from sympy import *
import numpy as np
import math
import random

# initial shape in heights and radii
zs = [0.0, 0.25, 0.5, 0.75, 1.0]
rs = [0.2, 0.4, 0.2, 0.8, 0.0]
N = len(zs)

# variativity. rs is altered right here, dz is then added to z
rs = [r+random.random()*0.5 for r in rs[:-1]]+[rs[-1]]
dz = random.random()*0.6

# interpolate the r(z) function to get a profile line
Vandermonde = Matrix([[zs[i]**j for j in range(N)] for i in range(N)])
Rs = Matrix(rs)
a0, a1, a2, a3, a4 = symbols('a0 a1 a2 a3 a4')
Pol = Matrix([a0, a1, a2, a3, a4])

solution = solve(Vandermonde*Pol - Rs, (a0, a1, a2, a3, a4))
a = [value for key, value in solution.items()]

def P(x, a):
    return sum([a[i]*x**i for i in range(len(a))])

# make a surface
u = np.linspace(0, 1, 59)
v = np.linspace(0, 1, 59)

theta = u * 2 * np.pi

r, _ = np.meshgrid(P(v, a), u)
v, theta = np.meshgrid(v, theta)

# the surface of revolution
x = r * np.cos(theta)
y = r * np.sin(theta)
z = v * (1 + dz)


# plotting
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib

matplotlib.interactive(True)
matplotlib.use('WebAgg')

from matplotlib.tri import Triangulation
tri = Triangulation(np.ravel(z), np.ravel(theta))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.plot_trisurf(np.ravel(x), np.ravel(y), np.ravel(z), triangles=tri.triangles,
                cmap='viridis', linewidths=0.2);
ax.set_xlim(-0.8, 0.8); ax.set_ylim(-0.8, 0.8); ax.set_zlim(0, 1 + dz);
ax.set_title('');
plt.show()

