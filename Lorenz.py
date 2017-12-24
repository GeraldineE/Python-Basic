# Clase del 3 de marzo del 2016
# Atractor de Lorenz 3D
# https://en.wikipedia.org/wiki/Lorenz_system

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(x, y, z, sigma=10, rho=28, betha=2.667):
    x_dt = sigma*(y - x)
    y_dt = x*(rho - z) - y
    z_dt = x*y - betha*z
    return x_dt, y_dt, z_dt

cantidad=10000

# Creacion de arreglos
x=range(cantidad+1)
y=range(cantidad+1)
z=range(cantidad+1)

# Valores Iniciales
dt = 0.01
x[0]=0
y[0]=1
z[0]=1.05

for i in range(cantidad):
    x_dt, y_dt, z_dt = lorenz(x[i],y[i],z[i])
    x[i+1] = x[i] + (x_dt*dt)
    y[i+1] = y[i] + (y_dt*dt)
    z[i+1] = z[i] + (z_dt*dt)

# Grafica
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)

plt.show()