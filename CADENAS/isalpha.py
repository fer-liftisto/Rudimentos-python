
'''
###FER###
Comprueva si es alfabetico sin numeros ni caracteres de puntuacion
'''
from icecream import ic

A= 'e4,e5'
B= 'e4e5'
C= 'e4 e5'
N= 'edf'

print(N.isalpha())
ic(N.isalpha())
print(A.isalpha())
ic(A.isalpha())
print(B.isalpha())
ic(B.isalpha())
print(C.isalpha())
ic(C.isalpha())
