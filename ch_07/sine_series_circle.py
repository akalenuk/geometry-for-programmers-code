from math import factorial
from math import pi

# in series, coefficients come as a list
ais = []
for i in range(4):
    n = i*2+1
    ais += [0, (1 if i % 2 == 0 else -1) / factorial(n)]

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

# polynomial ax
Pts = np.arange(-pi, pi, pi/1000)
Pxs = np.vectorize(sine)(Pts)
Pys = -np.vectorize(cosine)(Pts)

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='Circle made with a series ax of sine')
ax.set_aspect('equal', adjustable='box')
ax.grid()
fig.savefig("sine_series_circle.png")
plt.show()
