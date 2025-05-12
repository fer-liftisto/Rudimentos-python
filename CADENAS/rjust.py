'''
sintaxis:cadena.rjust(entero)
paretros:1- int
¿Que hace?: Genera un espacio para escribir y lo alinea a la derecha
¿Que devuelve?: 1 - str
'''	
cadena='1.e4,e5 2.Cf3,Cc6 3.Ab5,Cf6'
print(len(cadena))
print(len(cadena.rjust(29)))
print(type(cadena.rjust(29)))
print(cadena.rjust(29))
