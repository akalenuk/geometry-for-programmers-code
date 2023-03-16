from sympy import *

xs = [1, 2, 3, 4, 5]
ys = [8 + 20/60., 8 + 4/60., 7 + 56/60., 7 + 52/60., 8 + 0/60.]
N = len(xs)
M = 1

# the least squares matrix
LS = Matrix([[sum([xs[i]**(row + collumn) for i in range(N)]) for collumn in range(M+1)] for row in range(M+1)])

# the least squares column-vector
B = Matrix([sum([ys[i]*(xs[i]**row) for i in range(N)]) for row in range(M+1)])

# This tunrs approximation into interpolation
#a0, a1, a2, a3, a4 = symbols('a0 a1 a2 a3 a4')
#Pol = Matrix([a0, a1, a2, a3, a4])
#solution = solve(LS*Pol - B, (a0, a1, a2, a3, a4))


# polynomial in its symbolic form
a0, a1 = symbols('a0 a1')
Pol = Matrix([a0, a1])

# solving the system for the polynomial’s coefficients
solution = solve(LS*Pol - B, (a0, a1))

# storing the coefficients in a list for convenient reuse
a = [value for key, value in solution.items()]


# the plotting code
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')
Pxs = np.arange(0.5, 5.5, 0.01)
Pys = sum([a[i]*Pxs**i for i in range(M+1)])

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Approximating polynomial')
ax.grid()
plt.scatter(xs, ys)
# save a picture if you want
#fig.savefig("approximation_4.png")
plt.show()


