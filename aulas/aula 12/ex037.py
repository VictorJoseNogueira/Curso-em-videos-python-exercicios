casa = float(input('digite o valor da casa: R$:'))
salario = float(input('digite o seu salario por favor: R$: '))
parcelas = int(input('digite quantos anos : '))

parcelamento = casa / (parcelas * 12)
if parcelamento > salario * 0.30:
    print(f'nao foi possivel fazer o emprestimo de {casa} reais')
    print(f'pois a parcela({parcelamento:.2f}) excede 30% do seu salario({salario})')
else:
    print(f'emprestimo aprovado parcelas de {parcelamento:.2f}')
