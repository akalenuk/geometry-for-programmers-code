# circle in NURBS
sr2i = 1.0 / (2**0.5)
xs = [1.0,  sr2i,  0.0, -sr2i, -1.0, -sr2i,  0.0,  sr2i,  1.0]
ys = [0.0,  sr2i,  1.0,  sr2i,  0.0, -sr2i, -1.0, -sr2i,  0.0]
ws = [1.0,  sr2i,  1.0,  sr2i,  1.0,  sr2i,  1.0,  sr2i,  1.0]
n = len(xs)
knot = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4];
degree = 2;


def index_in_knots(t, nurbs_knot):
	for i in range(len(nurbs_knot) - 1):
		if t >= nurbs_knot[i] and t < nurbs_knot[i+1]:
			return i
	return -1

def nurbs_in_t(t, control_xs, control_ys, control_ws, knot, p):
	# de Boor
	k = index_in_knots(t, knot)

	
	d_x = []
	d_y = []
	d_w = []
	for j in range(p + 1):
		d_x += [control_xs[j + k - p]]
		d_y += [control_ys[j + k - p]]
		d_w += [control_ws[j + k - p]]

	for r in range(1, p+1):
		for j in reversed(range(r, p+1)):
			a = (t - knot[j+k-p]) / (knot[j+1+k-r] - knot[j+k-p])
			d_x[j] = (1.0 - a) * d_x[j-1] + a * d_x[j]
			d_y[j] = (1.0 - a) * d_y[j-1] + a * d_y[j]
			d_w[j] = (1.0 - a) * d_w[j-1] + a * d_w[j]

	return [d_x[p] / d_w[p], d_y[p] / d_w[p]]


def circle(t):
	global xs, ys, ws, knot, degree
	return nurbs_in_t(t, xs, ys, ws, knot, degree)


# make the plot
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.interactive(True)
matplotlib.use('WebAgg')

# polynomial curve
ts = np.arange(0.00, 4.00, 0.01)
Pxs = []
Pys = []
for t in ts:
	xy = circle(t)
	Pxs += [xy[0]]
	Pys += [xy[1]]

fig, ax = plt.subplots()
ax.plot(Pxs, Pys)
ax.set(xlabel='x', ylabel='y', title='de Boor\'s circle')
ax.grid()
ax.set_aspect('equal', adjustable='box')
plt.scatter([x/w for x,w in zip(xs,ws)], [y/w for y,w in zip(ys,ws)])
fig.savefig("nurbs_circle.png")
plt.show()
