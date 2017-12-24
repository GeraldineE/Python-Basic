
#Conocer la concentracion de aspirina en la sangre de una persona 

import numpy
import matplotlib
import matplotlib.pyplot


delta = 0.1
k= 0.2
t= range(101)
Q=range(101)
Q0 = 200
for i in range(101):
	Q1=Q0 - delta*k*Q0
	Q0=Q1
	Q[i]=Q1 
print Q 
Qnew = numpy.array(Q)
tnew=numpy.array(t)*6
print Qnew
print tnew
matplotlib.pyplot.plot(tnew,Qnew)
matplotlib.pyplot.show()