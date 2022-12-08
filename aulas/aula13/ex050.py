#leia 6 numeros e some apenas os pares
soma = 0
cont = 0
for c in range(1, 7):
    c = int(input('digite um numero: '))
    if c % 2 == 0:
        soma += c
        cont += 1
print(f'entre esses 6 numeros temos {cont} numeros pares')
print(f' e a soma entre eles é de {soma}')
