from lib.interface import *

from lib.interface import blz


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro na criação do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ler ao ler arquivo')
    else:
        blz('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq,  nome='<desconhecido>', telefone=0, email='', txto=''):
    try:
        a = open(arq, 'at')
    except:
        print(f'houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{telefone};{email};{txto}\n')
        except:
            print(f'houve um erro na gravação dos dados')
        else:
            print(f'novo registro de {nome} adicionado')
            a.close()
