from time import sleep
saque = 0
print('BEM VINDO AO BANCO TIR OBAN O ')
sleep(1)
print('nesse caixa temos notas de:')

print('R$50,00')

print('R$20,00')

print('R$10,00')

print('R$1,00')

saque = int(input('quanto deseja sacar ?'))
total = saque
ced = 50
totalced = 0
while True:
    if total >= ced:
        total-= ced
        totalced += 1
    else:
        if totalced >0:
            print(f'total de {totalced} de R${ced} ')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('volte sempre')
