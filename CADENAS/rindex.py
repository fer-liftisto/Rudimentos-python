'''
sintaxis: cadena.rindex(str)
parametros: 1 - str
¿Que hace?:  Busca el str en la cadena desde el final al principio y nos da la posicion , si no esta devuelve un error (ValueError)
¿Que devuelve?: 1 - int , si no esta - ValueError
'''
cadena = '1.e4,e5 2.Cf3,Cc6 3.Ab5,Cf6'
str = 'Ab5'
if str in cadena:
	# para asegurarnos de que esta lo que vuscamos
	print(type(cadena.rindex(str)),cadena.rindex(str))