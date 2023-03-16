from math import factorial

# in series, coefficients come as a list
ais = []
for i in range(4):
    n = i*2+1
    ais += [0, (1 if i % 2 == 0 else -1) / factorial(n)]

print("  polynomial coefficients:")
print(ais)

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
fig.savefig("sine_series.png")
plt.show()
