#algoritmo de euclides para determinar:
#el minimo comun divisor 

def mcd(a,b):
	while b!=0:
		a,b=b,a%b
	return a


#Algortimo de euclides extendido para determinar:
# El inverso multiplicativo de dos numeros 

def inversoMultiplicativo(e,phi):
	d=0
	x1=0
	x2=1
	y1=1
	temp=phi
	while e>0:
		aux=temp/e
		temp1=temp/aux * e
		e=temp1

		x=x2-aux*x1
		y=d-temp*y1

		x2=x1
		x1=x
		d=y1
		y1=y

		if tem==1:
			return d+phi


			