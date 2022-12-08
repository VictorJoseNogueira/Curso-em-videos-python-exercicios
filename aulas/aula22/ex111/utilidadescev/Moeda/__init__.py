def moeda(mod=0, moeda='R$'):
    return f'{moeda}{mod:.2f}'.replace('.', ',')


def metade(n=0, formt=False):
    met = n/2
    if formt == True:
        return moeda(met)
    else:
        return met


def dobro(n=0, formt=False):
    dob = n*2
    if formt == True:
        return moeda(dob)
    else:
        return dob


def aumentar(n=0, cento=0, formt=False):
    vn = (1+(cento/100))*n
    if formt == True:
        return moeda(vn)
    else:
        return vn


def diminuir(n=0, cento=0, formt=False):
    vn = (1-(cento/100))*n
    if formt == True:
        return moeda(vn)
    else:
        return vn


def resumo(preço=0, aumento=0, diminuto=0):

    resumido = dict()
    resumido['preço analizado'] = f'R${preço}'
    resumido['metade'] = metade(preço, True)
    resumido['dobro'] = dobro(preço, True)
    resumido[f'{aumento}% acrescimo'] = aumentar(preço, aumento, True)
    resumido[f'{diminuto}% desconto'] = diminuir(preço, diminuto, True)
    msg = 'VALOR ANALIZADO'
    print('-' * 50)
    print(f'{msg:^50}')
    print('-' * 50)
    for k, v in resumido.items():
            print(f'{k:.<30}{v:>6}')
    print('-' * 50)
