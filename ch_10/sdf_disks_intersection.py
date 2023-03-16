import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')

N = 100
x = np.linspace(-10, 10, N)
y = np.linspace(-10, 10, N)

X, Y = np.meshgrid(x, y)

def circle(X, Y, r):
    return np.sqrt(X*X + Y*Y) - r

# left circle
SDF1 = circle(X+2, Y, 6)

# right circle
SDF2 = circle(X-2, Y, 6)

# intersection
SDF = np.maximum(SDF1, SDF2)


# plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, SDF, cmap=cm.coolwarm, levels = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
fg = ax.contour(X, Y, SDF, 
    levels = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10],
	colors=['0.1', '0.1', '0.1', '0.1', '0.1', '0.2', '0.1', '0.1', '0.1', '0.1', '0.1'],
	linewidths=[0.25, 0.25, 0.25, 0.25, 0.25, 1.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
fg1 = ax.contour(X, Y, SDF1, levels=[0], colors=['0'], linewidths=[0.5], linestyles=['dashed'])
fg2 = ax.contour(X, Y, SDF2, levels=[0], colors=['0'], linewidths=[0.5], linestyles=['dashed'])
cbar = fig.colorbar(bg)

plt.show()
