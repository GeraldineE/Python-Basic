import sys

def cuantasEstrellasEnLasConstelaciones(nombreArchivo):
    file = open(nombreArchivo)
    catal = dict() #crear un diccionario para guardar el conteo de estrellas


    for i in range(1,7):
        file.readline()


    #lee cada uno de los registros del archivo
    for line in file:
        siglaConstel = line[7:10]   #extraer la sigla de la constelacion
        if siglaConstel == "":
            continue
        else:
            if siglaConstel in catal:   #pregunta si la sigla ya esta en el diccionario
                catal [ siglaConstel ] += 1
            else:
                catal [ siglaConstel ] = 1 #si no esta la sigla se crea y se inicializa en 1

    file.close()  
    return catal

def imprimirCatalogo(catalog):
    for constel, total in catalog.items() :
        print (constel, total)

if __name__ == '__main__':
     catalConst = cuantasEstrellasEnLasConstelaciones("starlist.txt")
     imprimirCatalogo(catalConst)
