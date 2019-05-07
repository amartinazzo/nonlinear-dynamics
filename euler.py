x0 = -1
v0 = -2
m = 1		# mass
k = 2		# spring
beta = 0	# friction

dt = 0.05
tf = 0.5

n_steps = int(tf/dt)

x = [x0]
v = [v0]

for i in range(1,n_steps+1):
	c = -k*x[-1]/m - beta*v[-1]/m

	x.append(x[-1] + v[-1]*dt)
	v.append(v[-1] + c*dt)

	print('x[{}]={}'.format(i*dt, x[-1]))
	print('v[{}]={}'.format(i*dt, v[-1]))