def moeda(mod):
    return f'R${mod:.2f}'


def metade(n, formt=0):
    met = n/2
    if formt == True:
        return moeda(met)
    else:
        return met


def dobro(n, formt=0):
    dob = n*2
    if formt == True:
        return moeda(dob)
    else:
        return dob


def aumentar(n, cento, formt = 0):
    vn = (1+(cento/100))*n
    if formt == True:
        return moeda(vn)
    else:
        return vn


def diminuir(n, cento, formt = 0):
    vn = (1-(cento/100))*n
    if formt == True:
        return moeda(vn)
    else:
        return vn

