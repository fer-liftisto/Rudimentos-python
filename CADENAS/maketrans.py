
'''
###FER### 
sustituye la aparicion del caracter de  cadenaEntrada por el caracter de cadenaSalida
###########################
sintaxis: cadena.maketrans(cadenaEntrada,cadenaSalida)

parametros: 2 => str (iguales de longitud)

¿que hace?: un diccionario con el valor ascii de los caracteres de cadenaEntrada como clave
 y cadenaSalida como valor

¿que devuelve?: 1 => dict
############################
sintaxis: cadena.translate(diccionario)

parametros: 1 => dict

¿que hace?: sustituye los valores de la clave del diccionario por el valor
 y borra los componentes de la cadena

¿que devuelve?: 1 => str
'''
from icecream import ic

INTAB = "aeiou"
OUTTAB = "12345"
CADENA = "esto es la cadena de ejemplo....guau!!!"
# CADENA = "this is string example....wow!!!"

trantab = CADENA.maketrans(INTAB, OUTTAB)

print(trantab)
ic(trantab)
print(CADENA)
ic(CADENA)
print (CADENA.translate(trantab))
ic(CADENA.translate(trantab))
