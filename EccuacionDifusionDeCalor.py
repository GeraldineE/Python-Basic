#ECUACION DE DIFUSION EN UNA DIMESION
# Para una varilla de l=1mt, con n=100
#hasta una temperatura Nt=300 
import numpy as np 
import matplotlib.pyplot as plt

#CONDICIONES DE DISCRETIZACION
n=100
l=1
h=l/n
x = np.linspace(0,l,n)
#u1=np.zeros((n,1))
u0=np.zeros((n,1))
u1=u0
#plt.plot(x,u0)
t=3
alfa=0.05
delta=0.01
#nt=t/delta
nt=300
beta=(alfa*delta)/(h**2)


#ECUACION DE DIFUSION 
print beta,alfa,delta,h

for j in range(nt):
	
	u0[0]=0
	u0[n-1]=0
	for i in range(n-1):	
		u1[i]=beta*(u0[i-1])+u0[i]*(1-2*beta)+beta*u0[i+1]
		

fig = plt.figure()    

#plt.plot(x,u1,color='black')
plt.scatter(x,u1) 
plt.grid()
plt.show()
#fig=plt.figure()
#x,u1=np.meshgrid(x,u1)
#xlabel("X")
#ylabel("temperatura")
#ylim((0.0,10))
#xlim((0.0,1.0))
