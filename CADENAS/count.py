'''
###FER###
sintaxis:cadena.count(str)
Parametros: 1 => str
¿Que hace?: Cuenta y devuelve las apariciones de str en cadena
¿Que devuelve?: 1 => int
'''
from icecream import ic

CADENA = '1.e4,e5 2.Cf3,Cc6 3.Ab5,O-O'
CARACTER = '.'

print(type(CADENA.count(CARACTER)))
print(f'En la cadena:{CADENA} tiene {CADENA.count(CARACTER)} veces {CARACTER}')
ic(CADENA.count(CARACTER))
