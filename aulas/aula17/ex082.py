lista = []
listapar = []
listaimpar = []
while True:
    print('=-=' * 30)
    pergunta = str(input('deseja digitar algum numero ? [S/N]')).strip().upper()[0]
    if pergunta in 'Ss':

        n = int(input('digite o valor desejado: '))
        lista.append(n)
        if n % 2 == 0:
            listapar.append(n)
        else:
            listaimpar.append(n)
    elif pergunta in 'Nn':
        print('certo isso é tudo entao.')
        break
    else:
        print('sim ou nao cara nao seja burro.')

print('=-=' * 30)
print(lista)
print(f'numeros pares da lista sao {listapar}')
print(f'os numeros impares da lista sao {listaimpar}')
