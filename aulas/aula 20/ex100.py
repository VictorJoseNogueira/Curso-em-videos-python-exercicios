from random import randint
from time import  sleep
numeros = []
def sorteio(lista):
    for c in range(1, 6):
        g = randint(0, 99)
        lista.append(g)
    print('sorteando os valores ', end='')
    for c, t in enumerate(lista):
        print(t, end=' ')
        sleep(0.5)
    sleep(0.5)
    print('\npronto')
def somapar(lista):
    somarei = 0
    pares = []
    x = 0
    for c, g in enumerate(lista):
        if g % 2 == 0:
            somarei += g
            pares.append(g)
            x += 1
    print(f'somando os valores', end=' ')
    for c, j in enumerate(pares):
        print(j, end=' ')
        sleep(0.5)
    print(f'temos o resultado de {somarei}')


sorteio(numeros)
sleep(0.5)
somapar(numeros)