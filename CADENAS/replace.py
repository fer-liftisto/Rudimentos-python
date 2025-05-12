'''
Reemplaza o sustituye el valor por otro
'''
a='1.e4,e5 2.Cf3'
print(a)
a=(a.replace('e','d'))
print(a)

instruccion='escribir(a)'
instruccion=instruccion.replace('escribir','print')
print(instruccion)