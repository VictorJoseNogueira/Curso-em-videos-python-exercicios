'''def lin():
    print('-' * 50)


def mensagem(msg):
    lin()
    print(msg)
    lin()



mensagem('sistema de alunos')

def conta():
    a = int(input('digite um valor: '))
    b = int(input('digite outro valor: '))
    s = a + b
    print(s)




def soma(a, b):
    s = a + b
    print(s)

soma(4, 6)


def contador(* núm):
    for valor in núm:
        print(valor, end=' ')
    print('fim')



contador(4, 5, 6, 7, 8)
contador(1, 1, 2, 4, 6)
contador(1, 2, 3, 4, 54)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 3, 4, 5, 6, 7, 22]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'para os valores {valores} temos o seguinte resultado {s}')


soma(1, 2, 3, 5, 1, 2, 3, 22)
