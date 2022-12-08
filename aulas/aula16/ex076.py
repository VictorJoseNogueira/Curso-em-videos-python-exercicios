lista = ('caderno', 40, 'estojo', 10, 'lapis', 3, 'borracha', 1.50, 'caneta', 2.75, 'pincel', 7, 'tinta', 5)
o = (lista[::2])
p = (lista[1::2])
h = 0
for c in range(0, 7):#foi gambiarra
    print(f'{o[h]:.<30} R$ {p[h]:>5.2f}')
    h += 1
'''print('=-'*36)
print(f'{"LISTAGEM DE PREÇOS ":^36}')
print('=-'*36)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>6.2f}')'''