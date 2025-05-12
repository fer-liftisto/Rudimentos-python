
''' 
###FER###
sintaxis: str.index(cadena,posicion)
parametros: 2 - str , int
¿que hace?:Busca la primera aparicion de la cadena despues de la posicion
¿que devuelve?: 1- int
 '''
from icecream import ic

A='1.e4,e5 2.Cf3,Cc6 3.Ab5'
# Comprueba si esta en a
if ',' in A:
    print(A.index('.'),A.index(','))
    print(A.index(',',5))
    ic(A.index(',', 5))
	# Busca la primera aparicion despues de  aparecer la cadena
    print(A.index(',',A.index(',')+1))
    ic(A.index(',', A.index(',')+1))
