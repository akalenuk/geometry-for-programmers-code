import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from matplotlib import collections as mc
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')

N = 100
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)

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

# distance to a segment
@np.vectorize
def line(x, y, x1, y1, x2, y2, w):
    return distance_p2e(x, y, x1, y1, x2, y2) - w

# V shape
def SDF(x, y):
    return np.minimum(line(x, y, 5, 2.5, 3, 6, 1.2), line(x, y, 5, 2.5, 7, 7.5, 1.2))
        
Z = SDF(X, Y)

# background plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, Z, cmap=cm.coolwarm, levels = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
fg = ax.contour(X, Y, Z, 
    levels = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
    colors=['0.1', '0.1', '0.1', '0.1', '0.1', '0.2', '0.1', '0.1', '0.1', '0.1', '0.1'],
    linewidths=[0.25, 0.25, 0.25, 0.25, 0.25, 1.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
cbar = fig.colorbar(bg)



# Step 1: do the cell border
border = []
for i in range(-10, 10):
    for j in range(-10, 10):
        # vertical line
        if SDF(j - 0.5, i + 0.5) * SDF(j + 0.5, i + 0.5) < 0:
            border += [[(j, i), (j, i+1)]]
        # horisontal line
        if SDF(j + 0.5, i - 0.5) * SDF(j + 0.5, i + 0.5) < 0:
            border += [[(j, i), (j+1, i)]]
        
# Step 2: fit the contour
epsilon = 1e-5

# an approximation of the partial /dx derivative
def dx(x, y):
    return (SDF(x+epsilon, y) - SDF(x, y)) / epsilon

# an approximation of the partial /dy derivative
def dy(x, y):
    return (SDF(x, y+epsilon) - SDF(x, y)) / epsilon

contour = []
for segment in border:
    new_segment = []
    for i in range(2):
        x, y = segment[i]
        pdx = dx(x, y) # x-part of the gradient vector
        pdy = dy(x, y) # y-part of the gradient vector
        # we’ll use the gradient’s length to normalize the fitting direction
        dxy_length = distance_p2p(pdx, pdy, 0, 0)
        # this is also the fitting vector’s new length
        sdf_value = SDF(x, y)
        new_p = (x - pdx / dxy_length * sdf_value, 
                 y - pdy / dxy_length * sdf_value)
        new_segment += [new_p]
        contour += [new_segment]    
        

# Step 3: smoothen the contour
smoothened = []
for segment in contour:
    x0 = segment[0][0]
    y0 = segment[0][1]
    x1 = segment[1][0]
    y1 = segment[1][1]

    # tangents from gradient
    #
    # the gradient is orthogonal to the tangent direction, 
    # so dx goes to the y-part and dy to the x-part of the tangent.
    dx0 = dy(x0, y0)
    dy0 = -dx(x0, y0)
    dx1 = dy(x1, y1)
    dy1 = -dx(x1, y1)

    # invert the tangents if they disagree with the segment direction
    #
    # there are two possible directions orthogonal to the gradient. 
    # Check whether the first best choice agrees with the piece's direction. 
    # Invert if it doesn’t.
    if dot2d(x1-x0, y1-y0, dx0, dy0) < 0:
        dx0 = -dx0
        dy0 = -dy0
    if dot2d(x1-x0, y1-y0, dx1, dy1) < 0:
        dx1 = -dx1
        dy1 = -dy1

    # compute the cubic coefficients
    a_x = dx0 + dx1 + 2*x0 - 2*x1
    b_x = -2*dx0 - dx1 - 3*x0 + 3*x1
    c_x = dx0
    d_x = x0
    a_y = dy0 + dy1 + 2*y0 - 2*y1
    b_y = -2*dy0 - dy1 - 3*y0 + 3*y1
    c_y = dy0
    d_y = y0

    # refine the contour
    #
    # this last step is not essential for the algorithm. 
    # It’s just instead of drawing the smooth contour 
    # as a set of cubic polynomials, we refine each into 
    # a set of short flat segments. Now we can draw the border, 
    # the line segment contour, and the smoothened result 
    # all in the same way.
    for i in range(10):
        t0 = i / 10.
        t1 = t0 + 1. / 10.
        x0 = a_x*t0**3 + b_x*t0**2 + c_x*t0 + d_x
        y0 = a_y*t0**3 + b_y*t0**2 + c_y*t0 + d_y
        x1 = a_x*t1**3 + b_x*t1**2 + c_x*t1 + d_x
        y1 = a_y*t1**3 + b_y*t1**2 + c_y*t1 + d_y
        smoothened += [[(x0, y0), (x1, y1)]]


# plot the result (uncomment the line you want to see intermediate results)
#lc = mc.LineCollection(border)
#lc = mc.LineCollection(contour)
lc = mc.LineCollection(smoothened)

lc.set_color("black")
lc.set_linewidth(2)
ax.add_collection(lc)

plt.show()
