from aula23.ex115.lib.interface import *
from aula23.ex115.lib.arquivo import *
from time import sleep

arc = 'cursoemvideo.txt'
if not arquivoexiste(arc):
    criararquivo(arc)
while True:

    resposta = sistema(['ver pessoas cadastradas: ', 'Cadastrar nova pessoa: ', 'Sair do programa'])
    if resposta == 1:
        #leraquivo
        blz('opção 1')
        lerarquivo(arc)
    elif resposta == 2:
        blz('Novo Cadastro')
        nome = str(input('nome: '))
        idade = leiaint('idade: ')
        cadastrar(arc, nome, idade)
        #cadastro
    elif resposta == 3:
        blz(f'{vermelho}saindo do sistema...ate logo{limpa}')
        break
    else:
        blz(f'{vermelho}ERRO! opção invalida{limpa}')
        sleep(1)