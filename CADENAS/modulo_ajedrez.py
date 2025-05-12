
'''
SUPRIME LAS LLAVES
'''
from icecream import ic

def quitar_llave(partida):
    '''quita llaves
    mal
    '''
    pri= 0
    fin= 0
    while True:
        try:
            pri= partida.index('{', pri)
        except ValueError:
            break
        fin= partida.index('}', fin)
        trozo= partida[pri: fin + 1]
        partida= partida.replace(trozo, '')
    return partida
############################
def quitar_puntos(partida):
    '''quita puntos
    
    mal si decenas jugada ejemplo 12...Cd5 '''
    prin= 0
    while True:
        try:
            prin= partida.index('...', prin)
            cacho = partida[prin -2 : prin + 3]
            partida = partida.replace(cacho, ',')
            ic(prin)
        except ValueError:
            break
    return partida
############################
def traducir_sp(partida):
    '''Traduce'''
    princ= 0
    while True:
        try:
            princ= partida.index('N', princ)
        except ValueError:
            break
        trozo= partida[princ : princ+1]
        partida=partida.replace(trozo,'C')
    princ=0
    while True:
        try:
            princ= partida.index('R',princ)
        except ValueError:
            break
        trozo= partida[princ : princ+1]
        partida= partida.replace(trozo,'T')
    princ= 0
    while True:
        try:
            princ= partida.index('B',princ)
        except ValueError:
            break
        trozo= partida[princ : princ+1]
        partida= partida.replace(trozo,'A')
    princ= 0
    while True:
        try:
            princ= partida.index('Q',princ)
        except ValueError:
            break
        trozo= partida[princ : princ+1]
        partida= partida.replace(trozo,'D')
    princ=0
    while True:
        try:
            princ= partida.index('K',princ)
        except ValueError:
            break
        trozo= partida[princ  : princ+1]
        partida= partida.replace(trozo,'R')
    return partida
############################
def main():
    '''Principal'''
    partida= '1.Nf3 1...Nf6 2.Nc3 2...Nc6'
    partida= quitar_puntos(partida)
    ic(partida)
    partida= traducir_sp(partida)
    ic(partida)
    print('pattida',partida)

if __name__ == '__main__':
    main()
