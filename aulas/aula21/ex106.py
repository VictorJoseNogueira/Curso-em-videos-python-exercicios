cores = (
    '\033[40m',#0 branco
    '\033[41m',#1 vermelho
    '\033[m',#2 limpa
    '\033[42m',#3verde
    '\033[44m',#4 azul
    '\033[40:7m'# 5 invertido
);


def pyhelps():
    from time import  sleep
    while True:
        msg = 'Sistema de ajuda pyhelsp'
        print('\033[43m~' * len(msg))
        print(msg)
        print('~' * len(msg))
        arg = str(input('\033[mFunção ou Biblioteca:')).strip()
        if arg == 'sair':
            print('\033[41m')
            msg = 'saindo..'
            print('~'* len(msg))
            print(msg)
            print('~' * len(msg))
            sleep(1)
            msg = 'fim do programa'
            print('~' * len(msg))
            print(msg)
            print('~' * len(msg))
            break
        msg = f'acessando manual do comando {arg}...'
        print('\033[42m~'* len(msg))
        print(msg)
        print('~' * len(msg))
        sleep(0.5)
        print('\033[40:7m')
        print(help(arg))
        print('\033[m')


pyhelps()

print(f'{cores[4]}teste do comando ')
