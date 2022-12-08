maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'digite o peso da {p}º pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso lido foi de {maior} kilos e \n o menor peso é {menor} kgs')
