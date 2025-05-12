'''
sintaxis:cadena.zfill(int)
parametros:1- int
¿Que hace?: reserva un espacio y rellena con cero por la izquierda
¿Que devuelve?:1- str
'''
cadena ='1.e4,e5 '
print(cadena,len(cadena))
print(cadena.zfill(15),len(cadena.zfill(15)))