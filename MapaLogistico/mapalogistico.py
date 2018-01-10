#Crear las funciones basicas para evaluar el mapa logitico
#Creado: 4-Feb-2016
#Autor:@geraldine

import numpy
import matplotlib
import matplotlib.pyplot

r = 3.7
y0 = 0.1
y1 = r * y0 *(1-y0)
y2 = r * y1* (1-y1)
y3 = r * y2*(1-y2)
y=range(50)
t=range(50)


#print y1
#print y2
#print y3

#print 'antes de for' 

#imprimiendo una lista
#for i in [0,1,23,4,5]: 
 #   y1 = r * y0 *(1-y0)
 #   y0=y1
 #   print y1
    
#print 'despues de for'

for i in range(50):
     y1 = r * y0 *(1-y0)
     y0 = y1
     y[i]=y1
  
print y
print "CONTENIDO DE YNEW Y TNEW"


#transforma los arreglo que creo a los arreglo de numpy
ynew = numpy.array(y)
tnew = numpy.array(t)

print ynew

matplotlib.pyplot.plot(tnew, ynew) 
matplotlib.pyplot.show() 
