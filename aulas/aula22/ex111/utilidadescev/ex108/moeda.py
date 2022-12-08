def moeda(mod):
    return f'R${mod:.2f}'.replace('.', ',')


def metade(n=0):
    met = n/2
    return met


def dobro(n=0):
    dob = n*2
    return dob


def aumentar(n=0, cento=0):
    vn = (1+(cento/100))*n
    return vn


def diminuir(n=0, cento=0):
    vn = (1-(cento/100))*n
    return vn

