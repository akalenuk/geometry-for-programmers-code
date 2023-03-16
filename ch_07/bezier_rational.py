import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# points and weights
xs = [0, 0.3, 0.7, 1]
ys = [0.2, 0.8, 1., 0.5]
ws = [1., 0.5, 0.5, 1.]

# rational Bezier function
def b3x(t, xs):
    n = ((1-t)*(1-t)*(1-t)*xs[0]*ws[0]
        + 3*(1-t)*(1-t)*t*xs[1]*ws[1]
        + 3*(1-t)*t*t*xs[2]*ws[2]
        + t*t*t*xs[3]*ws[3])
    d = ((1-t)*(1-t)*(1-t)*ws[0]
        + 3*(1-t)*(1-t)*t*ws[1]
        + 3*(1-t)*t*t*ws[2]
        + t*t*t*ws[3])
    return n / d

def b3y(t, ys):
    return b3x(t, ys)

ts = np.arange(0.0, 1.01, 0.01)
Bxs = np.vectorize(lambda t : b3x(t, xs))(ts)
Bys = np.vectorize(lambda t : b3y(t, ys))(ts)


fig, ax = plt.subplots()
ax.plot(Bxs, Bys)
ax.set(xlabel='x', ylabel='y', title=str(ws))
ax.grid()
plt.scatter(xs, ys)
fig.savefig("bezier_rational_3.png")
plt.show()
