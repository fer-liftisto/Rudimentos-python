# quita los caracteres desde alante y # # desde el final
# las coleciones
cadena=' 1.e4, e5    '
cadena1='up quitado detras'
print(cadena.strip())
print(cadena1.strip('up'))
print(cadena1.strip('detras'))
print(type(cadena))