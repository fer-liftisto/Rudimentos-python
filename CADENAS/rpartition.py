'''
sintaxis: cadena.rpartition(str)
parametros: 1 - str 
¿Que hace?: divide la cadena en tres cadenas (supcaden,str,poscadena)
¿Que devuelve?: 1 - pupla ,de tres cadenas
'''

a='1.e4,e5 2.Cf3,Cc6 3.Ab5,Cf6'
print(a.rpartition('Ab5'))
print(type(a.rpartition('Ab5')))