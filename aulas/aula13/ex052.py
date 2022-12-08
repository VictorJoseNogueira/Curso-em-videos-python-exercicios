#diga se é ou nao um numero primo
n = int(input('digite um numero: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m',end='')
        cont += 1
    else:
        print('\033[31m',end='')
    print(c, end=' ')
if cont == 2:
    print(f'\n\033[mo numero {n} é primo')
else:
    print(f'\n\033[mo numero {n} nao é primo')
print(f'\n\033[mo numero {n} foi dividido {cont} vezes.')
