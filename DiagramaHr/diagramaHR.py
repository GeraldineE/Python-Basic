#Diagrama HR para relacionar las propiedades de las estrellas
#Temperatura-Magnitud Abs

from numpy  import *
from matplotlib.pyplot import *

datos=genfromtxt("hygdata_v3.csv", delimiter=",") #Cargamos los datos

mag_abs= datos[1:,14]
color_index= datos[1:,16]

figure()
plot(color_index,mag_abs,'o',color='blue',markersize=-1)
savefig("diagramaHR.png")
xlabel("$BV")
xlim((-0.5,3.0))
ylabel("$Magnitud")
ylim((20,-10))



print (mag_abs,color_index);
