from math import pi
from math import sin

# in interpolation, we use Vandermonde matrix to build the equation
from sympy import *

# Let’s spread “x”s evenly over the range from -pi/2 to +pi/2
xs = [(i / 4.) * pi  - pi / 2. for i in range(5)]
ys = [sin(xi) for xi in xs]
N = len(xs)

# The coefficients of the interpolating polynomial will then come from solving the Vandermonde equation
Vandermonde = Matrix([[xs[i]**j for j in range(N)] for i in range(N)])
Ys = Matrix(ys)
a0, a1, a2, a3, a4 = symbols('a0 a1 a2 a3 a4')
Pol = Matrix([a0, a1, a2, a3, a4])

solution = solve(Vandermonde*Pol - Ys, (a0, a1, a2, a3, a4))
ais = [value for key, value in solution.items()]


# make the plot
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# polynomial ax
Pxs = np.arange(-1.6, 1.6, 0.01)
Pys = sum([ais[i]*Pxs**i for i in range(len(ais))])

# real sine
sine_ys = np.sin(Pxs)

# print mean error
print("  mean error of the approximation:", np.sum(np.abs(sine_ys - Pys)) / len(Pxs))

fig, ax = plt.subplots()
ax.plot(Pxs, sine_ys, color='grey')
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Sine')
ax.grid()
plt.scatter(xs, ys)
fig.savefig("sine_ipol.png")
plt.show()
