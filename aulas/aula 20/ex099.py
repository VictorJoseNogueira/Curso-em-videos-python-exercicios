from  random import randint
from  time import sleep
def maior(* num):
    ok = []
    x = int(input('digite quantos numeros na função: '))
    maior = 0
    for c in range(0, x):
        n = randint(0, 100)
        ok.append(n)
        if n > maior:
            maior = n
    print(f' entre os numeros')
    for i in ok:
        print(i, end=' ')
        sleep(0.5)
    print(f'o maior numero é {maior}\ne foram informados {len(ok)} numeros')
    print('-'* 40)
    sleep(1)


maior()
maior()


def trespontinho():
    for c in range(0, 10):
        print('.', end='')
        sleep(0.3)
    print()


trespontinho()
