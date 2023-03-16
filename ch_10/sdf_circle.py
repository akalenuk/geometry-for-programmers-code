import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')


# linspace is just a fancy word for an array with evenly spaced values in it
N = 100
x = np.linspace(-1.4, 1.4, N)
y = np.linspace(-1.4, 1.4, N)

# and a mesh grid is a 2D array. We have already seen both in chapter 8
X, Y = np.meshgrid(x, y)

# the signed distance function that shapes a circle
SDF = (X*X + Y*Y)**0.5  - 1.


# plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, SDF, cmap=cm.coolwarm, levels=[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
fg = ax.contour(X, Y, SDF, 
    levels = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1],
	colors = ['0.1', '0.1', '0.1', '0.1', '0.', '0.1', '0.1', '0.1', '0.1'],
	linewidths = [0.25, 0.25, 0.25, 0.25, 2, 0.25, 0.25, 0.25, 0.25])
cbar = fig.colorbar(bg)

plt.show()
