##SIMULACION DE UN COHETE
##SEBASTIAN-GERALDINE-DANIEL-PAOLA-DANIELA
##CREADO 2014 VPYTHON
##SEMILLERO FISICA COMPUTACIONAL UNIVERSIDAD DE MEDELLIN
from __future__ import division
from visual import *
from physutil import *
from visual.graph import *

scene.range = 5000



##Inicio comentario1
#Aca se le pide al usuario que ingrese los datos por teclado

velocidadCohete = float(input("Ingrese velocidad  inicial del cohete: "))
#f_empuje = float(input("Ingrese fuerza de empuje: "))
vel_escape_combustible = float(input("Ingrese velocidad de escape del combustible: "))
tasa_perdida_masa = float(input("Ingrese la rapidez de la perdida de masa: "))
#m = float(input("Ingrese la masa del cohete: "))
m0 = float(input("Ingrese la masa incial del cohete: "))
g = float(input("Ingrese la gravedad: "))
dt = float(input("Ingrese el paso temporal: "))
#d_aire = float(input("Ingrese densidad del aire: "))
coef_friccion = float(input("Ingrese el coeficiente de arrastre "))
area = float(input("Ingrese el area: "))

##Fin comentario1



##Inicio comentario 2

#Aca valida que la FUERZA DE EMPUJE debe ser mayor que el producto de MASA y GRAVEDAD, en caso de que el usuario ingrese datos que no cumplan esta validacion
#el programa se quedara dentro del ciclo while, donde vuelve a preguntar la FUERZA DE EMPUJE, MASA y GRAVEDAD hasta  hasta el momento que ingrese los datos con las especicaciones
#Que debe cumplir el programa
##while(f_empuje <= m*g):
##    print("La fuerza de de empuje debe ser mayor a la masa * gravedad, para que el cohete pueda despegar")
##    print("Ingrese nuevamente los datos: ")
##    f_empuje = float(input("Ingrese fuerza de empuje: "))
##    m = float(input("Ingrese la masa del cohete: "))
##    g = float(input("Ingrese la gravedad: "))

##Fin comentario 2


##Inicio comentario 3

#Aca valida que el paso temporal en el tiempo ingresado por el usuario no sea un valor negativo    
while(dt <= 0):
    print("Debe ingresar un paso temporal mayor que cero")
    print("Ingrese nuevamente el paso temporal: ")
    dt = float(input("Ingrese el paso temporal: "))
##Fin comentario 3

graphs = PhysGraph(radius = 0.01,numPlots=1)#indica el radio de cada grafica, y numPlots indica el numero de graficas que van a ser mostradas, en este caso una por que
                                           
timerDisplay = PhysTimer(1,1)




rocket = cone(pos = (0,-2000,0),radius = 50, axis = (0,800,0))#Crea el cohete
rocket.velocity =  vector(0,velocidadCohete,0)#Velocidad del cohete
rocket.momentum=m0*rocket.velocity






c=curve(pos=(0,rocket.pos.y,0),color = color.red)#Linea roja que deja marcado el recorrido vertical del cohete
t = 0
##const = 0.5*d_aire*coef_arrastre*area #Hacer parte de la formula de densidad del aire, se utiliza para que la aceleracion varie.
while t<0.5*(m0/tasa_perdida_masa):
    rate(100)
    m=m0-tasa_perdida_masa*t
    f_propulsion = (vel_escape_combustible* tasa_perdida_masa)
    ##rocket.aceleracion = vector(0,fuerza_neta,0)# Aca la aceleracion son componentes ( X, Y, Z) donde en Y se le esta pasado la formula de densidad del aire
    d_aire = exp(-mag(rocket.pos*0.00011856))
    fuerza_friccion = 0.5*d_aire*coef_friccion*area*mag(rocket.velocity)*mag(rocket.velocity)#f_drag
    fuerzaVariable = (f_propulsion - m*g - fuerza_friccion)
    rocket.fuerza = vector(0,fuerzaVariable,0)
                                                                                                               
    ##rocket.velocity = rocket.velocity + rocket.aceleracion*dt
    rocket.momentum = rocket.momentum + rocket.fuerza*dt
    ##print("Velocidad: " + str(rocket.velocity))
    #print("Magnitud: " + str(mag(rocket.velocity)))
    rocket.velocity=rocket.momentum/m
    rocket.pos = rocket.pos + rocket.velocity*dt
    c.append(pos = rocket.pos + rocket.velocity*dt)#Para que la linea roja que va dejando el cohete, siga eal cohete
    timerDisplay.update(t)
    graphs.plot(t,rocket.velocity.y)#Dibuja grafico de aceleracion

    ##graphs.plot(t,fuerza_y.y)   
    #graphs.plot(t,rocket.pos.y,rocket.velocity.y,rocket.aceleracion.y)
    t=t+dt


