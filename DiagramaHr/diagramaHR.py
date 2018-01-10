#Diagrama HR(Hertzsprung-Russell)para relacionar las propiedades de las estrellas
#Temperatura-Magnitud Abs

from numpy  import *
from matplotlib.pyplot import *

datos=genfromtxt("hygdata_v3.csv", delimiter=",") #Cargamos los datos

magnitud_aparente=datos[1:,13]
mag_abs= datos[1:,14]
color_index= datos[1:,16]

filtro=magnitud_aparente<5

figure()
plot(color_index,mag_abs,'o',color='red',markersize=0.5)
plot(color_index[filtro],mag_abs[filtro],'o',color='yellow',markersize=1)


savefig("diagramaHR1.png")
title("DIAGRAMA HR")
xlabel("INDICE DE COLOR")
xlim(-0.5,3.0)
ylabel("MAGNITUD")
ylim(20,-10)


print (mag_abs,color_index);
matplotlib.pyplot.show()
