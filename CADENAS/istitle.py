
'''
###FER###
Si tiene la primera letra en mayusculas
devuelve: bool
'''
from icecream import ic

A= 'Titulo'
B='titulo Titu'

print(A.istitle())
ic(A, A.istitle())

print(B.istitle())
ic(B, B.istitle(), type(B.istitle()))
