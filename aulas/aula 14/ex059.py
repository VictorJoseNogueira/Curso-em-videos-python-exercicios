#programacommenu
from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
m = 0
while m != 5:
    print('=-' * 20)
    m = int(input('oque vc gostaria de fazer com esses numeros\n[1]somar\n[2]multiplicar\n[3]mostrar o maior\n[4]alterar numeros\n[5]sair do menu. '))
    if m == 1:
        r = n1 + n2
        print(f'\033[34m{n1} + {n2} = {r}\033[m')
    elif m == 2:
        r = n1 * n2
        print(f'\033[34m{n1} x {n2} = {r}\033[m')
    elif m == 3:
        if n1 > n2:
            print(f'\033[34mo maior é {n1}\033[m')
        elif n2 > n1:
            print(f'\033[34m o maior é {n2}\033[m')
        else:
            print('\033[34mambos sao iguais\033[m')
    elif m == 4:
        n1 = int(input('digite o primeiro valor:'))
        n2 = int(input('digite o segundo valor '))
    elif m == 5:
        print('\033[34mfinalizando...\033[m')
        sleep(1)
    else:
        print('\033[31moperação nao aceita tente novamente\033[m')
print('muito obrigado por usar meu menu!!!')
