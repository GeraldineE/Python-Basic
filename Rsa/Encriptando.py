
def Encriptar(kp,t):

	e,n=kp
	#Generar el texto en claro basado en el
	#cifrado y la clave utilizando el algortimo rsa:
	# mod ** e

	#Castea el texto a numeros
	#Uso del algoritmo RSA:
	#mod ** e
	#a**b mod m

	cifrar=[(ord(char)**e) % n for char in t]
	return cifrar


	def Decifrar(pk,tc):
		d,n=pk
		des=[chr((char**d)%n)for char in tc]
		return ''.join(des)

		