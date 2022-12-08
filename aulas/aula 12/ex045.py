pr = float(input('digite o valor do produto? '))
print('''\033[35m1 = dinheiro,
2= cheque, 
3= cartao a vista, 
4= 2x no cartao, 5 = 
3x ou mais no cartao\033[m''')
pg = int(input('por favor digite a opção de pagamento desejada: '))

if pg == 1 or pg == 2:
    pgmt = pr - (pr * 0.10)
    print(f' o valor a ser pago é de {pgmt} reais')
elif pg == 3:
    pgmt = pr - (pr * 0.05)
    print(f' o valor a ser pago é de {pgmt} reais')
elif pg == 4:
    print(f' o valor a ser pago é de {pr} reais')
    print(f'valor a ser pago por parcela é de: R$ {pr/2}')
elif pg == 5:
    pgmt = pr + (pr * 0.2)
    print(f' o valor a ser pago é de {pgmt} reais')
    prce = int(input('digite a quantidade de parcelas:'))
    print(f'o valor da parcela é de R$ {pgmt/prce}')
else:
    print('\033[31m opção invalida de pagamento tente novamente')
