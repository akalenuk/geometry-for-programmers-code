from sympy import *

xs = [1, 2, 3, 4, 5]
ys = [4, 2, 3, 2, 4]
N = len(xs)

# the Vandermonde matrix
Vandermonde = Matrix([[xs[i]**j for j in range(N)] for i in range(N)])

# the target function’s values
Ys = Matrix(ys)

# polynomial’s coefficients in symbolic form
a0, a1, a2, a3, a4 = symbols('a0 a1 a2 a3 a4')
Pol = Matrix([a0, a1, a2, a3, a4])

# solving the system for the polynomial’s coefficients
solution = solve(Vandermonde*Pol - Ys, (a0, a1, a2, a3, a4))

# putting the coefficients into a list for convenient storage and evaluation
a = [value for key, value in solution.items()]


# the plotting code
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')
Pxs = np.arange(0.5, 5.5, 0.01)
Pys = sum([a[i]*Pxs**i for i in range(N)])

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Interpolating polynomial')
ax.grid()
plt.scatter(xs, ys)
fig.savefig("interpolating.png")
plt.show()


