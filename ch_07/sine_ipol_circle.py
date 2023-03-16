from math import factorial
from math import pi
from math import sin

# coefficients as a list
from sympy import *

xs = [(i / 4.) * pi  - pi / 2. for i in range(5)]
ys = [sin(xi) for xi in xs]
N = len(xs)

Vandermonde = Matrix([[xs[i]**j for j in range(N)] for i in range(N)])
Ys = Matrix(ys)
a0, a1, a2, a3, a4 = symbols('a0 a1 a2 a3 a4')
Pol = Matrix([a0, a1, a2, a3, a4])

solution = solve(Vandermonde*Pol - Ys, (a0, a1, a2, a3, a4))
ais = [value for key, value in solution.items()]

print("  polynomial coefficients:")
print(ais)

def sine(x):
    global ais
    def sine_quarter(x):
        return sum([ais[i]*x**i for i in range(len(ais))])
    if x < 0:
        return -sine(-x)
    if x <= pi / 2:
        return sine_quarter(x)
    if x <= pi:
        return sine_quarter(pi - x)
    else:
        return sine(x - 2*pi)

def cosine(x):
    return sine(x + pi/2.)

# make the plot
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# polynomial model
Pts = np.arange(-pi, pi, pi/1000)
Pxs = np.vectorize(sine)(Pts)
Pys = -np.vectorize(cosine)(Pts)

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='A circle made with the sine model')
ax.set_aspect('equal', adjustable='box')
ax.grid()
fig.savefig("sine_ipol_circle.png")
plt.show()
