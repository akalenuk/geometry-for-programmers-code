import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from matplotlib import collections as mc
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')

from pylab import rcParams
rcParams['figure.figsize'] = 8, 8

# width
w = 16

# height
h = 16

# linspace parameters. Visualisation only, irrelevant for the algorithm
N = 128
x = np.linspace(0, w, N)
y = np.linspace(0, h, N)

# the image is a two-dimensional array of 1-channel 8-bit depth “grey values”
img = [
[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[0,  77, 125,38, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[0,  120,255,254,203,144,96, 3,  0,  0,  0,  0,  0,  0,  0,  0],
[0,  34, 253,255,255,255,255,230,154,94, 8,  0,  0,  0,  0,  0],
[0,  0,  196,255,255,255,255,255,255,252,241,139,83, 6,  0,  0],
[0,  0,  149,255,255,255,255,255,255,255,255,255,250,213,80, 0],
[0,  0,  98, 255,255,255,255,255,255,255,255,255,255,224,58, 0],
[0,  0,  2,  224,255,255,255,255,255,255,255,242,152,4,  0,  0],
[0,  0,  0,  145,255,255,255,255,255,255,255,154,1,  0,  0,  0],
[0,  0,  0,  82, 251,255,255,255,255,255,255,253,156,1,  0,  0],
[0,  0,  0,  6,  237,255,255,255,255,255,255,255,252,146,3,  0],
[0,  0,  0,  0,  149,255,255,243,149,252,255,255,255,240,21, 0],
[0,  0,  0,  0,  69, 249,255,152,1,  150,252,255,238,71, 0,  0],
[0,  0,  0,  0,  0,  211,224,4,  0,  1,  137,240,86, 0,  0,  0],
[0,  0,  0,  0,  0,  73, 57, 0,  0,  0,  2,  20, 0,  0,  0,  0],
[0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
]

# with distance threshold, we govern where we want our isoline to pass. 
# The number 128 implies that we expect a curve roughly 
# in the middle between full light and full dark pixels
distance_threshold = 128

# with the accuracy threshold, we regulate how fast our fitting will exit. 
# It’s a lever to balance speed and accuracy
accuracy_threshold = 2


# a function of pixel values. It is not continuous
@np.vectorize
def img_as_f(x, y):
    if x > 0 and x < w and y >= 0 and y < h:
        return img[h-1-int(y)][int(x)]
    return 0

# a smooth and continuous image function
@np.vectorize
def img_as_smooth_f(x, y):
    if x > 0 and x < w and y >= 0 and y < h:
        # this is a trick to shift the whole function
        # to (0.5, 0.5) vector. Without this shift, 
        # our pixel's colors are defined in the pixels’ 
        # top left corners. With this shift, the colors
        # are now defined in the pixel’s centers.
        centered_x = x - 0.5
        centered_y = y - 0.5

        # truncated coordinates
        ix = int(centered_x)
        iy = int(centered_y)

        # these are the in-pixel distance coefficients. 
        # We take 4 of them – one per each pixel’s side
        x0 = centered_x - ix
        x1 = 1 - x0
        y0 = centered_y - iy
        y1 = 1 - y0

        # literally the corner cases. 
        # With our (0.5, 0.5) shifts, the corners now coincide 
        # with the pixel’s centers, so if we detect a corner case, 
        # we just return the color value from the corresponding pixel
        if x0 == 0 and y0 == 0:
            return img_as_f(ix, iy)
        if x0 == 0 and y1 == 0:
            return img_as_f(ix, iy + 1)
        if x1 == 0 and y0 == 0:
            return img_as_f(ix + 1, iy)
        if x1 == 0 and y1 == 0:
            return img_as_f(ix + 1, iy + 1)

        # pixel’s sides. 
        # Special cases of inverse distance interpolation 
        # with just two interpolated values
        if x0 == 0:
            return ((img_as_f(ix, iy) / y0 + img_as_f(ix, iy + 1) / y1) 
                   / (1/y0 + 1/y1))
        if x1 == 0:
            return ((img_as_f(ix+1, iy) / y0 + img_as_f(ix+1, iy + 1) / y1) 
                   / (1/y0 + 1/y1))
        if y0 == 0:
            return ((img_as_f(ix, iy) / x0 + img_as_f(ix + 1, iy) / x1) 
                   / (1/x0 + 1/x1))
        if y1 == 0:
            return ((img_as_f(ix, iy+1) / x0 + img_as_f(ix + 1, iy+1) / x1) 
                   / (1/x0 + 1/x1))

        # finally, the general case of inverse distance interpolation;
        # all four corner values are being mixed together
        return ((img_as_f(ix, iy) / (x0*y0) + 
                img_as_f(ix, iy+1) / (x0*y1) + 
                img_as_f(ix+1, iy) / (x1*y0) + 
                img_as_f(ix+1, iy+1) / (x1*y1)) 
               / (1/(x0*y0) + 1/(x0*y1) + 1/(x1*y0) + 1/(x1*y1)))
    return 0


def dot2d(x1, y1, x2, y2):
    return x1*x2 + y1*y2
  
def distance_p2p(x1, y1, x2, y2):
    return dot2d(x2-x1, y2-y1, x2-x1, y2-y1)**0.5

X, Y = np.meshgrid(x, y)


def SDF(x, y):
    return img_as_smooth_f(x, y) - distance_threshold
        
Z = SDF(X, Y) + distance_threshold

fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, Z, cmap=cm.Blues_r, levels = [16 * i for i in range(-16, 16)])
cbar = fig.colorbar(bg)

# Step 1: do the cell border

# the border will be a list of line segments 
# where each line segment is a 2-piece list of 2D points
border = []
for i in range(0, 16):
    for j in range(0, 16):
        # vertical line
        if SDF(j - 0.5, i + 0.5) * SDF(j + 0.5, i + 0.5) < 0:
            border += [[(j, i), (j, i+1)]]
        # horisontal line
        if SDF(j + 0.5, i - 0.5) * SDF(j + 0.5, i + 0.5) < 0:
            border += [[(j, i), (j+1, i)]]
        
# Step 2: fit the contour

# we approximate partial derivatives with differences. 
# An epsilon – is a difference step size. Normally, 
# the smaller the size, the better the approximation
epsilon = 1e-5

# partial derivatives
def dx(x, y):
    return (SDF(x+epsilon, y) - SDF(x-epsilon, y)) / (2*epsilon)
def dy(x, y):
    return (SDF(x, y+epsilon) - SDF(x, y-epsilon)) / (2*epsilon)

contour = []
# we take the vertices from the initial border as a set of starting points
for segment in border:
    new_segment = []
    for i in range(2):
        x, y = segment[i]
        sdf_value = SDF(x, y)
        while abs(sdf_value) > accuracy_threshold: # the exit condition
            step_length = sdf_value / 256
            pdx = dx(x, y)
            pdy = dy(x, y)
            dxy_length = distance_p2p(pdx, pdy, 0, 0)
            # the iteration itself
            x = x - pdx / dxy_length * step_length 
            y = y - pdy / dxy_length * step_length
            sdf_value = SDF(x, y)
        new_segment += [(x, y)]
    contour += [new_segment]    
        

# Step 3: smoothen the contour
smoothened = []
for segment in contour:
    # initial values for the cubics’ ends 
    # come from the segments’ vertices
    x0 = segment[0][0]
    y0 = segment[0][1]
    x1 = segment[1][0]
    y1 = segment[1][1]

    # initial tangent vectors come from partial derivatives
    dx0 = dy(x0, y0)
    dy0 = -dx(x0, y0)
    dx1 = dy(x1, y1)
    dy1 = -dx(x1, y1)

    # invert the tangents if the disagree with the segment direction
    if dot2d(x1-x0, y1-y0, dx0, dy0) < 0:
        dx0 = -dx0
        dy0 = -dy0
    if dot2d(x1-x0, y1-y0, dx1, dy1) < 0:
        dx1 = -dx1
        dy1 = -dy1

    # normalize the partial derivatives to get rid of the “loops”
    dxy_length0 = distance_p2p(dx0, dy0, 0, 0)
    dxy_length1 = distance_p2p(dx1, dy1, 0, 0)
    dx0 = dx0 / dxy_length0
    dy0 = dy0 / dxy_length0
    dx1 = dx1 / dxy_length1
    dy1 = dy1 / dxy_length1

    # compute the cubic coefficients
    #
    # We get the cubics’ coefficients by solving 
    # two systems of equations. Here are the ready-made
    # solutions provided to us by SymPy (see chapter 11)
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
    # This is just a technicality – we turn cubics
    # back into linear segments so we can draw them
    # in the same way we drew the initial and fitted contours
    for i in range(16):
        t0 = i / 16.
        t1 = t0 + 1. / 16.
        x0 = a_x*t0**3 + b_x*t0**2 + c_x*t0 + d_x
        y0 = a_y*t0**3 + b_y*t0**2 + c_y*t0 + d_y
        x1 = a_x*t1**3 + b_x*t1**2 + c_x*t1 + d_x
        y1 = a_y*t1**3 + b_y*t1**2 + c_y*t1 + d_y
        smoothened += [[(x0, y0), (x1, y1)]]

# draw the result
#
# Feel free to uncomment any line you want. 
# All the contours are plotted in the similar way.

#lc = mc.LineCollection(border)
#lc = mc.LineCollection(contour)
lc = mc.LineCollection(smoothened)

lc.set_color("black")
lc.set_linewidth(3)
ax.add_collection(lc)

plt.show()
