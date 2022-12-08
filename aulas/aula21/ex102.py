def fator(fac=1, show=0):
    '''-> calcula o fatorial de um numero
    :param fac: numero a ser fatorado  
    :param show: se True ele mostra o processo de fatoramento se False nao mostra
    :return: ele retorna o valor do numero fatorado'''
    f = 1
    for c in range(fac, 0, -1):
        f *= c
        if show == True:
            print(f'{c}x' if c > 1 else f'{c}=', end='')
    return f

f1 = fator(6,True)

print(f1)
help(fator)
