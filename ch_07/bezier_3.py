import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# points
xs = [0, 0.3, 0.7, 1]
ys = [0.2, 0.8, 1., 0.5]

# cubic Bezier formula
def b3x(t, xs):
    return (1-t)*(1-t)*(1-t)*xs[0] + 3*(1-t)*(1-t)*t*xs[1] + 3*(1-t)*t*t*xs[2] + t*t*t*xs[3]

def b3y(t, ys):
    return b3x(t, ys)

ts = np.arange(0.0, 1.01, 0.01)
Bxs = np.vectorize(lambda t : b3x(t, xs))(ts)
Bys = np.vectorize(lambda t : b3y(t, ys))(ts)


fig, ax = plt.subplots()
ax.plot(Bxs, Bys)
ax.set(xlabel='x', ylabel='y', title='Cubic Bezier')
ax.grid()
plt.scatter(xs, ys)
fig.savefig("bezier_3.png")
plt.show()
