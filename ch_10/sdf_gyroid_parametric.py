import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')

N = 100
x = np.linspace(-16, 16, N)
y = np.linspace(-16, 16, N)

# these are the meshgrids that cover 
# the part of the infinite function we want to display
X, Y = np.meshgrid(x, y)

# this is the z-coordinate of the x-y plane section
z = 0.5

# this is the quasi-offset term
SDF = (np.sin(X)*np.sin(Y) + np.sin(Y)*np.cos(z) + np.sin(z)*np.cos(X) - Y / 32)


# plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, SDF, cmap=cm.coolwarm, levels = [-2, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2])
fg = ax.contour(X, Y, SDF, 
    levels = [-2, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2],
	colors = ['0.1', '0.1', '0.1', '0.1', '0.', '0.1', '0.1', '0.1', '0.1'],
	linewidths = [0.25, 0.25, 0.25, 0.25, 1, 0.25, 0.25, 0.25, 0.25])
cbar = fig.colorbar(bg)

plt.show()
