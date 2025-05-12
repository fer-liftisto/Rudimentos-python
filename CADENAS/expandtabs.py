'''
###FER###
Sintaxis: cadena.expandtabs(int)
parametros: 1 => int
¿Que hace?: todos los '\t' caracteres son reemplazados con espacios en blanco
hasta el siguiente múltiplo del parámetro(por defecto es 8)
¿Que devuelve?: 1 => str
'''
from icecream import ic

CADENA = 'e4,e5\tCf3,Cf6'

print(CADENA.expandtabs(10))
print(type(CADENA.expandtabs(9)))
ic(type(CADENA.expandtabs(9)))
