'''
###FER###
Añade en la llaves el contenido de la variable puesta
'''

from icecream import ic

A = '1.e4,e5 {}'
B = '2.Cf3,Cf6'

C = A.format(B)
print(f'{C}')
print(f'{C=}')
ic(f'{C=}')
print(A.format(B))
