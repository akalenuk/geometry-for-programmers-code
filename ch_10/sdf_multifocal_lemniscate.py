import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')

N = 1000
x = np.linspace(-3, 3, N)
y = np.linspace(-3, 3, N)

X, Y = np.meshgrid(x, y)

# a point-to-point distance function
def distance_p2p(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# a product function. Like sum() but prod()
def prod(list):
    if len(list) == 2:
        return list[0]*list[1]
    else:
        return prod([list[0]*list[1]] + list[2:])

# input data for the lemniscate
foci = [(-0.6, -1.12), (-0.6, 1.12), (-1.12, -2.06), (-1.12, 2.06), (0.4, 0), (1.2, 0)]
r = 2

# it’s easier to govern the function with a quasi-offset
# by exponentiating the offset into the power
# proportional to the number of points
c = r**len(foci)

# a lemniscate is the isoline of the product of all distances to focii
SDF = prod([distance_p2p(X, Y, focus[0], focus[1]) for focus in foci]) - c


# plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, SDF, cmap=cm.coolwarm, levels = [-8000, -6000, -4000, -2000, 0, 2000, 4000, 6000, 8000])
fg = ax.contour(X, Y, SDF, 
    levels = [-8000, -6000, -4000, -2000, 0, 2000, 4000, 6000, 8000],
	colors = ['0.1', '0.1', '0.1', '0.1', '0.', '0.1', '0.1', '0.1', '0.1'],
	linewidths = [0.25, 0.25, 0.25, 0.25, 1, 0.25, 0.25, 0.25, 0.25])
cbar = fig.colorbar(bg)

plt.show()
