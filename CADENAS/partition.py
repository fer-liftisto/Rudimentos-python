''' 
sintaxis: str.partition(str)
parametros: 1 - str
¿que hace?: divide la cadena por la primera vez que aparecca el caracter pasado 
¿que devuelve?: tuple 
 - una tupla con tres cadenas
 '''
a='1.e4,e5 2.Cf3,Cc6 3.Ab5,Cf6'

print(a.partition('3'))