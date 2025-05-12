
'''
 ###FER###
 Pone la cadena en minusculas
'''
from icecream import ic

A= 'SALIR'

print(A)
print(A.lower())
B = A.lower()
ic(B)
# inmutable
print(f' A => {A}')

lista= ['PEDRO','JUAN','LuCAS']
ic(lista)
nombres_propios = map(lambda x : x.lower(), lista)
nombres= list(nombres_propios)
ic(nombres)

minusculas = [x.lower() for x in lista]
ic(minusculas)
