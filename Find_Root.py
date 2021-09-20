import math


#the arguments
a = 4.5000
b = 5.5000
#the midpoint
c = float(.5*(a+b))

# the function to work with
def f(number_x):
	x = float(number_x)
	f = float(x*math.exp(x)-(5*(math.exp(x)-1)))
	return f
	

#the loops to narrow down the root
i = 0
for i in range(0,50):
	if math.copysign(f(c), 1) < 0.01:
		print(c)
	elif f(a)*f(c) < 0:
		a = c
	else:
		b = c
	c = .5*(a+b)

print(c)