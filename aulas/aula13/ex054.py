#leia 7 pessoas e fale quem é maior e quem é menor
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pss in range(1, 8):
    nascmento = int(input(f'em que ano a {pss}º pessoa nasceu ? '))
    idade = ano - nascmento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'temos {maior} pessoas maiores de idade\ne {menor} menores de idade')
