
'''
    uso f"string"
'''
###  https: // youtu.be/EoNOWVYKyo0?si = zfsxZ5xVk_J4uTTx  ###
from datetime import datetime
fecha: datetime =datetime.now()
print(f'{fecha:%d.%m.%y (%H:%M:%S)}')
print(f'{fecha:%c}')
print(f'{fecha:%I%p}')

num :int = 100000000000000000000000000000000000000
print(f'{num:_}')
print(f'{num:,}')

pi :float = 3.141516
print(f'{pi:.2f}')
print(f'{pi:.0f}')
num: float = 100000000000000000000.455678901234556
print(f'{num:,.6f}')
print(f'{num:_.2f}')

nom :str = 'Fre'
print(f'veinte espacios => {nom:>20}')
print(f'veinte espacios => {nom:<20}')
print(f'veinte espacios => {nom:^20}')
print(f'veinte espacios => {nom:_>20}')
print(f'veinte espacios => {nom:#<20}')
print(f'veinte espacios => {nom:|^20}')
print(f'veinte espacios => {nom:k^20}')

a:int = 5
b:int = 2
print(f'{a + b = }')
print(f'{bool(a) = }')

nombre:str = 'Fer'
print(f'{nombre =}')
