'''
sintaxis: cadena.splitline(boleano)
parametros:1- boleano
¿Que hace?: mete lo  separado por \n o \r en un elemento de una lista .
si boleano es igual a True lo incluye 
¿Que devuelve?: 1- list
'''
cadena='''1.e4,e5 
2.Cf3,Cc6 
3.Ab5,Cf6\n4.O-O,d6'''

print(cadena.splitlines())
print(type(cadena.splitlines()))
print()
############################
cadena = "Hola ha todos \rel mundo de\nyupiii"
print(cadena) 
print (cadena.splitlines( )) 
  
print (cadena.splitlines(0))
  
print (cadena.splitlines(True)) 
print()
############################
string = "Cat\nBat\nSat\nMat\nXat\nEat"
  
print (string.splitlines( )) 
  
print('India\nJapan\nUSA\nUK\nCanada\n'.splitlines())
print()
############################
def Cal_longitud(cadena): 
    lista= cadena.splitlines() 
    print (lista) 
    numero_letras = [len(elemento) for elemento in lista] 
    return numero_letras
#### #### ####
cadena = "1.e4,e5\n2.Cf3,Cf6\r3.Ab5,O-O"
print(Cal_longitud(cadena)) 