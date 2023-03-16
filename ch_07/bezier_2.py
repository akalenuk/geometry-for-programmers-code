import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# points
xs = [0, 0.3, 1]
ys = [0.2, 0.8, 0.5]

# Bezier function
def b2x(t, xs):
    return (1-t)*(1-t)*xs[0] + 2*(1-t)*t*xs[1] + t*t*xs[2]

# no point in copypasting, ys and xs share the same basis
def b2y(t, ys):
    return b2x(t, ys)

ts = np.arange(0.0, 1.01, 0.01)
Bxs = np.vectorize(lambda t : b2x(t, xs))(ts)
Bys = np.vectorize(lambda t : b2y(t, ys))(ts)


fig, ax = plt.subplots()
ax.plot(Bxs, Bys)
ax.set(xlabel='x', ylabel='y', title='Quadratic Bezier')
ax.grid()
plt.scatter(xs, ys)
fig.savefig("bezier_2.png")
plt.show()
