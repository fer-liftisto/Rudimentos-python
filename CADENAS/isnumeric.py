
'''
###FER###
Sintaxis: cadena.isnumeric()
argumentos: no
¿ que hace?: Da true si es int sin signo
¿retorna un tipo de dato?: Boleano

'''
from icecream import ic

A= str(1235)
B= '12.6'
C= '-67'
print(A.isnumeric())
ic(A,A.isnumeric())

ic(B,B.isnumeric())
ic(C,C.isnumeric())

print('1'.isnumeric())
