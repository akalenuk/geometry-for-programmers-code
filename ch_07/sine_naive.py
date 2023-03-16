from sympy import *
from math import pi

x, a, b, c, d, e, f = symbols('x a b c d e f')

sine = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
sine_d = diff(sine, x)

the_system = [
    sine.subs(x, 0),
    sine.subs(x, pi / 2) - 1,
    sine.subs(x, -pi / 2) + 1,
    sine_d.subs(x, 0) - 1,
    sine_d.subs(x, pi / 2),
    sine_d.subs(x, -pi / 2),
]

res = solve(the_system, (a, b, c, d, e, f))

print("  polynomial coefficients:")
for var, value in res.items():
    print(var, value)


# store coefficients in a list
ais = []
for var, value in res.items():
   ais = [value] + ais

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
print("")
print("  mean error of the approximation:", np.sum(np.abs(sine_ys - Pys)) / len(Pxs))

fig, ax = plt.subplots()
ax.plot(Pxs, sine_ys, color='grey')
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Sine')
ax.grid()
fig.savefig("sine_naive.png")
plt.show()
