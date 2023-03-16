import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import ticker, cm
from numpy import ma

matplotlib.interactive(True)
matplotlib.use('WebAgg')

def distance_p2p(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# quasi-inverse function local to (0, 1]
@np.vectorize
def quasi_inverse(x):
    if x < 1:
        return (1 - 2*x + x*x)/x
    return 1e-15 # not to cause div by zero


# quasi-inverse function with variative locality
def quasi_inverse_with_locality(x, locality):
    return quasi_inverse(x / locality)

        
N = 1000
x = np.linspace(-16, 16, N)
y = np.linspace(-16, 16, N)

X, Y = np.meshgrid(x, y)

balls = [(-6, -5), (9, -8), (0, 9)]
offset = -2.5
locality = 25

# in this SDF, real inverse is replaced with quasi-inverse
SDF = (quasi_inverse_with_locality( 
        sum([quasi_inverse_with_locality(distance_p2p(X, Y, ball[0], ball[1]), locality) for ball in balls]), locality)
      / len(balls) 
      + offset)


# plotting
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
bg = ax.contourf(X, Y, SDF, cmap=cm.coolwarm, levels = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50])
fg = ax.contour(X, Y, SDF, 
    levels = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],
	colors = ['0.1', '0.1', '0.1', '0.1', '0.1', '0.', '0.1', '0.1', '0.1', '0.1', '0.1'],
	linewidths = [0.25, 0.25, 0.25, 0.25, 0.25, 1, 0.25, 0.25, 0.25, 0.25, 0.25])
cbar = fig.colorbar(bg)

plt.show()
