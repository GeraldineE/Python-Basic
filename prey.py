
# Marzo 1 2016
#plot of the evolution of population of the prey for 10 months 
#Environments is the predator-prey relationship 

import numpy
import matplotlib
import matplotlib.pyplot


n = 3
delta = 0.1 * n

t=range(101)
Y=range(101)
X= range(101)
Xn = 15
Yn= 100
Ky= 2.0
Kyx=0.01
Kx= 1.06
Kxy = 0.01 



for i in range(101):
	Y1=Yn - delta*(Ky*Yn-(Ky*Xn*Yn))
	Yn=Y1
	Y[i]=Y1 
#print Y

for i in range(101):
    X1=Xn - delta*(Kyx*Yn*Xn-(Kx*Xn))
    Xn=X1
    X[i]=X1 

Ynew = numpy.array(Y)
Xnew = numpy.array(X)
t=numpy.array(t)
print Ynew
#print t
print Xnew
matplotlib.pyplot.plot(Ynew,Xnew)
matplotlib.pyplot.plot(Xnew,Ynew)
matplotlib.pyplot.show()
