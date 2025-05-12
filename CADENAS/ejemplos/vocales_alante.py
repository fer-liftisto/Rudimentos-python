''' https: // www.youtube.com/watch?v = FlUAfGArQe0 & t = 17s'''
from icecream import ic

def vocal_alante(cadena):
    '''Deja las vocales alante y las consonantes atras'''
    vocales=[c for c in cadena if c in 'aeiouAEIOU']
    consonantes = [c for c in cadena if c not in 'aeiouAEIOU']
    return ''.join(vocales) + ''.join(consonantes)

def vocales_alante(cadena):
    '''Deja las vocales alante y las consonantes atras'''
    vocales = list()
    consonantes = list()

    for i in cadena:
        if i in 'aeiouAEIOU':
            vocales.append(i)

    for i in cadena:
        if i not in 'aeiouAEIOU':
            consonantes.append(i)
    
    return ''.join(vocales) + ''.join(consonantes)


if __name__ == '__main__':
    ic(vocal_alante('cadena'))
    ic(vocal_alante('vocales'))
    ic(vocal_alante('Fernando'))
    print()
    print(vocales_alante('cadena'))
    print(vocales_alante('vocales'))
    print(vocales_alante('Fernando'))
