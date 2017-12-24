import numpy as np
import random 
import math 
import matplotlib.pyplot as plt

#Valores iniciales
# n=11
R=np.zeros((11,1))
# #R=range(101)
R[0]=1
# mu=0.3

#R = [1]
mu=0.3
n=10


def GalaxiaDisco(R):
	#mu=(random.uniform(0,1))
	#R1=R0-(1-math.exp(-R0)*(R0+1)-mu)/(math.exp(-R0)*(R0+1)-(math.exp(-R0)))
	# for i in range(1,n-1):
	# 	R[i+1]= R[i]-(1-math.exp(-R[i])*(R[i]+1)-mu)/(math.exp(-R[i])*(R[i]+1)-(math.exp(-R[i])))
	for i in range(0,10):
		print "INDEX :"
		print i
		print "R[i] is:"
		print R[i]
		R[i+1]=R[i]-(1-math.exp(-R[i])*(R[i]+1)-mu)/(math.exp(-R[i])*(R[i]+1)-(math.exp(-R[i])))
		print "R[i+1] obtenido es:"
		print R[i+1]

GalaxiaDisco(R)

print R