'''
###FER###
sintaxis: cadena.endswith(str)
Parametros: 1 => str
¿Que hace?: devuelve True si el final coincide
¿latino: cadena.termina_con(cadena,'caracteres')?
¿Que devuelve?: 1 => bool
'''
from icecream import ic

CADENA='Cf6#'
CARACTER = '#'
print(CADENA.endswith(CARACTER))
ic(CADENA.endswith(CARACTER))
print(type(CADENA.endswith(CARACTER)))
