'''
###FER###
Sintaxis: cadena.lstrip(cadena)
argumentos: 1 => str
¿ que hace?: Quita la cadena de la izquierda pasada como parametro
¿retorna un tipo de dato?: 1 => str
'''
from icecream import ic
A='1.e4,e5 2.d4,d5'
B=A.lstrip('1.')

print(A)
ic(A)
print(B)
ic(B)
print(f"{A.lstrip('1')} hola")
