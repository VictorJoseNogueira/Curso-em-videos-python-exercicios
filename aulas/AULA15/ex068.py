from random import randint
cont = 0
while True:
    parimpar = str(input('par ou impar [P/I]?')).strip().upper()[0]
    computador = randint(0, 10)
    if parimpar in 'PpiI':
        jogador = int(input('digite seu numero: '))
        soma = jogador + computador
        somapar = soma % 2
        print(f'{computador}+{jogador} é ', end='')
        if somapar == 0:
            print('par')
        else:
            print('impar',)
        if parimpar in 'Pp':
            if somapar == 0:
                print('\033[34mvc escolheu par\033[m')
                print('\033[34mjogador venceu\033[m')
                cont += 1
            else:
                print('\033[34mvc escolheu par\033[m')
                print('\033[31mperdeu playboy\033[m')
                break
        if parimpar in 'Ii':
            if somapar == 1:
                print('\033[34mvc escolheu impar\033[m')
                print('\033[34mjogador venceu\033[m')
                cont += 1
            else:
                print('\033[34mvc escolheu impar\033[m')
                print('\033[31mperdeu playboy\033[m')
                break
    else:
        print('resposta errada tente novamente')
#print('deu par' if somapar == 0 else 'deu impar')
print(f'vc venceu {cont} partidas consecutivas')
