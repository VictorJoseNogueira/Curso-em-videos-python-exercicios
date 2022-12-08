'''def contador(i, f, p):
    """faz uma contagem e mostra na tela
:param i: inicio da contagem
:param f: fim da contagem
:param p: passo da contagem
:return: sem retorno"""
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('fim')


contador(1, 41, 5)
help(contador)
def somar(a=0, b=0, c=0):#a=0, b=0, c=0 chamasse parametro opcional
    s = a+b+c
    print(f' a soma vale {s}')

somar(2, 54, 6)

somar(4, 7)
somar()


def teste():
    x = 8
    print(f'na função teste n vale {n}')
    print(f' na função teste x = {x}')


# programa principal
n = 2
print(f'no programa principal n = {n}')

teste()
#print(f'{x}') escopo local

def testes(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f' a, b e c  dentro vale {a},{b},{c}')


a = 5
testes(a)
print(f'a fora vale {a}')

def função():
    n1 = 2
    print(n1)

n1 = 5

print(n1)
função()'''


def somar(a=0,b=0, c=0):
    s = a+b+c
    return s

r1 = somar(3, 5, 7)
r2 = somar(3, 6, 1)
r3 = somar(1, 2, 3)
print(f'{r1},{r2},{r3}')
print(somar(3, 5, 7))