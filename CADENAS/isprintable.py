
'''
###FER###
Es imprimible
'''
from icecream import ic

A='1.e4,e5 2.d4,exd'
B= '\n'

print(A.isprintable())
print(B.isprintable())

ic(A, A.isprintable())
ic(B, B.isprintable())
