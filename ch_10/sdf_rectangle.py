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

# dot product
def dot2d(x1, y1, x2, y2):
    return x1*x2 + y1*y2

# box product
def box2d(x1, y1, x2, y2):
    return x1*y2 - x2*y1
    
# point-to-point distance
def distance_p2p(x1, y1, x2, y2):
    return dot2d(x2-x1, y2-y1, x2-x1, y2-y1)**0.5
    # this is the alternative take, feel free to swap
    #return ((x2-x1)**2 + (y2-y1)**2)**0.5

# point-to-line signed distance
def signed_distance_p2l(x, y, x1, y1, x2, y2):
    return box2d(x-x1, y-y1, x2-x1, y2-y1) / distance_p2p(x1, y1, x2, y2)
    
# sign of a point-to-line distance
def sign_of_distance_p2l(x, y, x1, y1, x2, y2):
    return 1 if signed_distance_p2l(x, y, x1, y1, x2, y2) >= 0 else -1

# point-to-line Euclidean distance
def distance_p2l(x, y, x1, y1, x2, y2):
    return abs(signed_distance_p2l(x, y, x1, y1, x2, y2))
    
# point-to-edge distance
def distance_p2e(x, y, x1, y1, x2, y2):
    projection_normalized = (dot2d(x-x1, y-y1, x2-x1, y2-y1)
        / distance_p2p(x1, y1, x2, y2) ** 2)
    if projection_normalized < 0:
        return distance_p2p(x, y, x1, y1)
    elif projection_normalized > 1:
        return distance_p2p(x, y, x2, y2)
    else:
        return distance_p2l(x, y, x1, y1, x2, y2)

# signed distance to rectangle
@np.vectorize
def rect(x, y, xmin, ymin, xmax, ymax):
    d1 = distance_p2e(x, y, xmin, ymax, xmin, ymin)
    d2 = distance_p2e(x, y, xmax, ymax, xmin, ymax)
    d3 = distance_p2e(x, y, xmax, ymin, xmax, ymax)
    d4 = distance_p2e(x, y, xmin, ymin, xmax, ymin)
    if d1 < d2 and d1 < d3 and d1 < d4:
        return d1*sign_of_distance_p2l(x, y, xmin, ymax, xmin, ymin)
    elif d2 < d3 and d2 < d4:
        return d2*sign_of_distance_p2l(x, y, xmax, ymax, xmin, ymax)
    elif d3 < d4:
        return d3*sign_of_distance_p2l(x, y, xmax, ymin, xmax, ymax)
    else:
        return d4*sign_of_distance_p2l(x, y, xmin, ymin, xmax, ymin)
        
SDF = rect(X, Y, -6, -4, 6, 4)


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
