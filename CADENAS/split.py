'''
Combierte a lista separando en los caracter especificados

Como parte de la manipulación de strings y listas, <<< split y join >>> en Python. La función join convierte una lista en una cadena formada por los elementos de la lista separados por comas. Por otro lado, split convierte una cadena de texto en una lista. Por defecto, los elementos de dicha lista serán las palabras de la cadena.
''' 
a='''1.Cf3,Cf6 
2.e4,e5
'''
b=a.split(' ')
print(b)
print(''.join(b))