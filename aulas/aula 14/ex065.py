n = maior = menor = cont = 0
resp = 'S'
total = n
while resp in "sS":
    n = int(input('digite um valor '))
    resp = str(input('quer continuar ? S/N '))
    total += n
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = total / cont
print('fim')
print(f'vc digitou {cont} e a media é {media}')
print(f'o maior numero foi {maior} e o menor foi {menor}')