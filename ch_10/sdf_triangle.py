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

# signed distance to a triangle
@np.vectorize
def triangle(x, y, x1, y1, x2, y2, x3, y3):
    d1 = distance_p2e(x, y, x1, y1, x2, y2)
    d2 = distance_p2e(x, y, x2, y2, x3, y3)
    d3 = distance_p2e(x, y, x3, y3, x1, y1)
    sign = -1 if sum([sign_of_distance_p2l(x, y, x1, y1, x2, y2)
                    , sign_of_distance_p2l(x, y, x2, y2, x3, y3)
                    , sign_of_distance_p2l(x, y, x3, y3, x1, y1)]) == -3 else 1;
    return min([d1, d2, d3]) * sign
        
SDF = triangle(X, Y, -6, -5, 6, -5, 0, 7)


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
