
'''
###FER###

Pone un guion delante y detras de cada caracteres
'''
from icecream import ic
A= ' 1 . e4  2 . e5'
print('-'.join(map(str,A)))
print('.'.join(A))
B= ['a','b']
HABER = ''.join(B)
ic(HABER, type(HABER))
print(f'{type(HABER)} {HABER}')
