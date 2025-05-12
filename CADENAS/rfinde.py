'''
sintaxis: cadena.rfind(cadena)
parametros:1 - str
¿Que hace?: Busca la cadena en otra cadena desde la derecha si no encuentra nada devuelve (-1)
¿Que devuelve?: 1- int de la posicion desde la izquierda
'''

a='1.e4,e5 2.Cf3,Cc6 3.Ab5,Cf6'

posicion = 'chocolate'.rfind('i')
print(type(posicion),posicion)
print(a.rfind('Cc6'))