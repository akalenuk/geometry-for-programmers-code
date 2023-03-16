from sympy import *
import numpy as np
import math
import random

# generation
zs = [0.0, 0.25, 0.5, 0.75, 1.0]
rs = [0.2, 0.4, 0.2, 0.8, 0.0]
N = len(zs)

radius_variation = 0.5
height_variation = 0.6
deformation_variation = 0.7

rs = [r+random.random()*radius_variation for r in rs[:-1]]+[rs[-1]]
dz = random.random()*height_variation

Vandermonde = Matrix([[zs[i]**j for j in range(N)] for i in range(N)])
Rs = Matrix(rs)
a0, a1, a2, a3, a4 = symbols('a0 a1 a2 a3 a4')
Pol = Matrix([a0, a1, a2, a3, a4])

solution = solve(Vandermonde*Pol - Rs, (a0, a1, a2, a3, a4))
a = [value for key, value in solution.items()]

def P(x, a):
    return sum([a[i]*x**i for i in range(len(a))])

u = np.linspace(0, 1, 59)
v = np.linspace(0, 1, 59)

theta = u * 2 * np.pi

r, _ = np.meshgrid(P(v, a), u)
v, theta = np.meshgrid(v, theta)

x = r * np.cos(theta)
y = r * np.sin(theta)
z = v * (1 + dz)


# deformation
dxs = [-1, 1, 1, -1, -1, 1, 1, -1]
dys = [-1, -1, 1, 1, -1, -1, 1, 1]
dzs = [0, 0, 0, 0, 1+dz, 1+dz, 1+dz, 1+dz]
ddxs = [random.random()*deformation_variation - deformation_variation/2 for i in range(len(dxs))]
ddys = [random.random()*deformation_variation - deformation_variation/2 for i in range(len(dys))]
ddzs = [random.random()*deformation_variation - deformation_variation/2 for i in range(len(dzs))]

def F(x, y, z, dds): # inverse distance interpolation
    global dxs, dys, dzs, n
    N = 0. # numerator
    D = 0. # denominator
    for i in range(len(dds)):
        # Euclidean distance
        di = ((x-dxs[i])**2 + (y-dys[i])**2 + (z-dzs[i])**2)**0.5
        if di == 0.:
            return dds[i]
        ki = 1/di # weight function
        N += ki * dds[i]
        D += ki
    return N / D

# applying the deformation to all the vertices
for i in range(len(x)):
    for j in range(len(x[0])):
        xij = x[i][j]
        yij = y[i][j]
        zij = z[i][j]
        ddx = F(xij, yij, zij, ddxs)
        ddy = F(xij, yij, zij, ddys)
        ddz = F(xij, yij, zij, ddzs)
        x[i][j] += ddx
        y[i][j] += ddy
        z[i][j] += ddz


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
ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_zlim(0, 1.2 + dz);
ax.set_title('');
plt.show()

