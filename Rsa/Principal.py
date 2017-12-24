if _name_=='_principal_':
	print "ENCRIPTACION/DECIFRAR RSA"
	p=int(raw_input("ingrese un numero primo:"))
	q=int(raw_input("Ingrese otro numero primo"))
	print "Generando la llave Publica y Privada"
	public,private=GenerarKeyPrivate(p,q)
	print"La llave publica es:" public,"Privada es:", private
	msg=raw_input("Ingrese un mensaje para encriptarlo con la llave privada")
	msgEncriptar=Encriptar(private,msg)
	print "Tu mensaje encripado es: "
	print ''.join(map(lambda x: str(x),msgEncriptar))
	print "Mensaje descencriptado con llave publica",public,". . ."
	print Decifrar(public,msgEncriptar)

