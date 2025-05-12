'''
###FER###
sintaxis: cadena.center(int)
parametros: 1 => int
¿Que hace?: centra el texto en los caracteres especificados
¿Que devuelve?: 1 => str
'''
from icecream import ic

CADENA='e4'
CENTRADO_EN = 25
print(CADENA.center(CENTRADO_EN))
print(len(CADENA.center(CENTRADO_EN)))
ic(len(CADENA.center(CENTRADO_EN)))
print(type(CADENA.center(CENTRADO_EN)))
