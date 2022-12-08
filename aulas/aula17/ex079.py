n = []
j = 0
pergunta = 'S'
while True:
    pergunta = str(input('vc quer digitar mais algum numero [S/N]? ')).strip().upper()[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('vc quer digitar mais algum numero ? SIM OU NAO: ')).strip().upper()[0]
    if pergunta in 'Ss':
        j = int(input('digite um valor: '))

        if n.count(j) == 0:
            n.append(int(j))


    elif pergunta in 'Nn':
        print('certo isso é tudo')
        break
print(f'os numeros em ordem crescente na lista sao {sorted(n)}')
