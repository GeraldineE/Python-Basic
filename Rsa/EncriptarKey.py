import random

def GenerarKeyPrivate(p,q):
	if not(Esprimo(p) and Esprimo(q)):
		raise ValueError('Debe ser primo')
	elif p==q:
		raise ValueError('p y q no pueden ser iguales')
	n=p*q

	phi =(p-1)*(q-1)
	#Evaluando que e y phi sean coprimos
	e=random.randrange(1,phi)
	g=mcdr(e,phi)

	#Evaluando que e y n sean coprimos 
	e=random.randrange(1,n)
	g=mcdr(e,n)

	#Usando el algortimo extendido de euclides 
	#Generando clave privada

	d=inversoMultiplicativo(e,phi)
	return((e,n),(d,n))

	
