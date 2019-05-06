import matplotlib.pyplot as plt
import numpy as np


def logistic_map(x0, r, n):
	x = [x0]
	for i in range(n):
		x.append(r*x[-1]*(1-x[-1]))
	return x


def bifurcation_diagram(r0, rf, x0=0.2):
	x_val = []
	r_val = []
	r_values = np.linspace(r0, rf, 1000)
	for r in r_values:
		x = logistic_map(x0, r, 100)
		for x_el in x[:-12]:
			x_val.append(x_el)
			r_val.append(r)
	plt.scatter(r_val, x_val, c='black', s=0.05, alpha=0.15)
	plt.show()