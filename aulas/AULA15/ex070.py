linha = '-='*25
titulo = 'LOJAS BARATIN'
caro = ''

gasto = maisdemil = preço = 0
carovalor = 0
coisabarata = ''
pergunta = ''
print(linha)
print(titulo.center(50))
print(linha)
while True:
    pergunta = str(input('deseja comprar algo ? [S/N]')).strip()
    while pergunta in 'Ss':
        barato = preço
        produto = str(input('qual produto deseja comprar ?'))
        preço = float(input('quanto ele custa? R$ '))
        gasto += preço
        if carovalor < preço:
            carovalor = preço
            caro = produto
        if preço >= 1000:
            maisdemil += 1
        if preço < barato:
            barato = preço
            coisabarata = produto

        pergunta = str(input('deseja comprar algo ? [S/N]')).strip()
    if pergunta in 'nN':
        break
print(f'vc gastou R$ {gasto:.2f} , {maisdemil} produtos foram mais de R$1000.00 reais e o mais caro foi {caro} ')
print(f'a coisa mais barata que comprou foi {coisabarata} e ela custou {barato}')
