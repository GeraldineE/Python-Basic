#Determinar si un numero es primo

def Esprimo(num):
	if num==2:
		return True
	if num<2 or num%2==0	
		return False
	for n in xrange(3,int(num**0.5)+2,2):
		if num%n==0:
			return False
	return True


