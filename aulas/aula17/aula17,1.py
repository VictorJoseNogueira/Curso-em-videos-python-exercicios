lanche = ['burg', 'pizza', 'suco', 'pudim']
print(lanche)
lanche.append('cookie')
print(lanche)
lanche.insert(0, 'dog')
print(lanche)
lanche[2] = 'picole'
print(lanche)
lanche.insert(3, 'sanduiche')
print(lanche)
del lanche[3]
print(lanche)
lanche.pop(1)
print(lanche)
lanche.remove('dog')
print(lanche)
lanche.pop()
print(lanche)
if 'burg' in lanche:
    lanche.remove('burg')
print(lanche)
valor = list(range(4, 11))
print(valor)
