import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')

N = 100
x = np.linspace(-1.4, 1.4, N)
y = np.linspace(-1.4, 1.4, N)

X, Y = np.meshgrid(x, y)

SDF = (X*X + Y*Y)**0.5  - 1.

# hollow shell is the result of the erode-unsign-dilate sequence
shell_width = 0.2
SDF_eroded = SDF + shell_width / 2
unsigned_DF = np.abs(SDF_eroded)
SDF_hollowed = unsigned_DF - shell_width / 2


# plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, SDF_hollowed, cmap=cm.coolwarm, levels=[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
fg = ax.contour(X, Y, SDF_hollowed, 
    levels = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1],
	colors = ['0.1', '0.1', '0.1', '0.1', '0.', '0.1', '0.1', '0.1', '0.1'],
	linewidths = [0.25, 0.25, 0.25, 0.25, 1, 0.25, 0.25, 0.25, 0.25])
fg2 = ax.contour(X, Y, SDF, levels=[0], colors=['0'], linewidths=[0.5], linestyles=['dashed'])
cbar = fig.colorbar(bg)

plt.show()
