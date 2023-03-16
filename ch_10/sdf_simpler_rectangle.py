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

# quasi-SDF that still produces rectangular shape
@np.vectorize
def not_a_true_sdf_rect(x, y, xmin, ymin, xmax, ymax):
    return max([xmin-x, ymin-y, x-xmax, y-ymax])        

# real rectangular SDF    
@np.vectorize
def rect(x, y, xmin, ymin, xmax, ymax):
    center = [(xmax + xmin) / 2, (ymax + ymin) / 2]
    half_width = (xmax - xmin) / 2
    half_height = (ymax - ymin) / 2
    relative_x = x - center[0]
    relative_y = y - center[1]
    dx = max(0, abs(relative_x) - half_width)
    dy = max(0, abs(relative_y) - half_height)
    outside_d = (dx**2 + dy**2)**0.5
    inside_d = min(max(dx, dy), 0.0)
    return outside_d + inside_d
    
# feel free to try any
SDF = not_a_true_sdf_rect(X, Y, -6, -4, 6, 4)
#SDF = rect(X, Y, -6, -4, 6, 4)


# plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, SDF, cmap=cm.coolwarm, levels=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
fg = ax.contour(X, Y, SDF, 
    levels = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10],
	colors = ['0.1', '0.1', '0.1', '0.1', '0.1', '0.2', '0.1', '0.1', '0.1', '0.1', '0.1'],
	linewidths = [0.25, 0.25, 0.25, 0.25, 0.25, 1.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
cbar = fig.colorbar(bg)

plt.show()
