import numpy 
import matplotlib
import matplotlib.pyplot 



Q0=200
t=range(101)
Q=range(101)
delta = 0.1
k=0.2

def RungeKutta(x):
	deriv = -k*x

	return  deriv

for i in range(101):
	Q1= Q0+ delta*RungeKutta(Q0 + (1/2)* delta*RungeKutta(Q0))
	Q0=Q1
	Q[i]=Q1
	t[i]=i* delta
Qnew = numpy.array(Q)
tnew=numpy.array(t)

print Qnew
print tnew


matplotlib.pyplot.plot(tnew,Qnew)
matplotlib.pyplot.show()

