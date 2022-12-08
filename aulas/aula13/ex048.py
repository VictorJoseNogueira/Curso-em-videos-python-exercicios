#calcule a soma dos numeros multiplos de 3 entre 0 e 500
soma = 0
cont = 0
n = int(input('digite um valor: '))
for c in range(1, n, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f' a soma de todos os valores ({cont}) é : {soma}')
