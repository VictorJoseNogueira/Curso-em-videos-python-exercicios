#from aula23.ex113 import leiaint
limpa = '\033[m'
vermelho = '\033[31m'
azul = '\033[34m'
verde = '\033[32m'
preto = '\033[30m'
branco = '\033[47m'


def blz(msg):
    tam = 50
    print('-'*tam)
    print(f"{msg:^{tam}}")
    print('-'*tam)


def sistema(lista):
    blz(f'{verde}MENU PRINCIPAL{limpa}')
    c = 1
    for item in lista:
        print(f'{azul}{c} - {item}{limpa}')
        c +=1
    print('-'*50)
    #opc = leiaint('Sua opção: ')
    #return opc
