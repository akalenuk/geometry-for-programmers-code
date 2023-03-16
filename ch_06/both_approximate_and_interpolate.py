from sympy import *

xs = [10, 11, 12, 13, 14]
ys = [-42, -41, -38, -37, -37]
N = len(xs)
M = 2

# the least squares matrix
LS = Matrix([[sum([xs[k]**(i+j) for k in range(N)]) for j in range(M+1)] for i in range(M+1)])

# the least squares column-vector
B = Matrix([sum([ys[k]*(xs[k]**i) for k in range(N)]) for i in range(M+1)])

last_point_reentrance = 0
a = [0, 0, 0]

# this calculates the polynomial from a list of coefficients
def P(x, a):
    return sum([a[i]*x**i for i in range(len(a))])

# the algorithm tries adding the last point again and again until the precision expectations are met
precision = 0.01
while abs(P(xs[N-1], a) - ys[N-1]) > precision:
   LS_more = Matrix([[last_point_reentrance*xs[N-1]**(i+j) for j in range(M+1)] for i in range(M+1)])
   B_more = Matrix([last_point_reentrance*ys[N-1]*xs[N-1]**i for i in range(M+1)])

   a0, a1, a2 = symbols('a0 a1 a2')
   Pol = Matrix([a0, a1, a2])

   solution = solve((LS+LS_more)*Pol - (B+B_more), (a0, a1, a2))
   a = [value for key, value in solution.items()]
   # on each iteration, exactly one new last point is added. 
   # But you can add more if you want the algorithm to converge faster
   last_point_reentrance += 1


# the plotting code
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')
Pxs = np.arange(9.5, 15.5, 0.01)
Pys = sum([a[i]*Pxs**i for i in range(M+1)])

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Approximating polynomial')
ax.grid()
plt.scatter(xs, ys)
fig.savefig("approximation_t3.png")
plt.show()


