from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terc = 0
big = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(0, 99)
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        terc += matriz[l][2]
        if matriz[1][c] > big:
            big = matriz[1][c]
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f' os valores pares da matriz somados sao iguais a: {pares}')
print(f' os valores da terceira coluna somados sao {terc}')
print(f' o maior valor da segunda linha é: {big}')
print(len(matriz))