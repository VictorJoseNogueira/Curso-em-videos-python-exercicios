lista = []
pergunta = 'S'
contador = 0
while True:
    pergunta = str(input('deseja digitar algum numero [S/N] ?')).strip().upper()[0]
    if pergunta in 'Ss':
        n = lista.append(int(input('digite um valor: ')))
        contador += 1
    elif pergunta in 'nN':
        print('isso é tudo por hoje ')
        break
    else:
        print('vc é burro né:')
print(lista)
print(f'vc digitou {contador} numeros ')
lista.reverse()
print(f' lista invertida fica {lista}')
lista.reverse()
print(f'o numero 5 esta na lista na posição {lista.index(5)}' if 5 in lista else ' numero 5 nao esta na lista')
