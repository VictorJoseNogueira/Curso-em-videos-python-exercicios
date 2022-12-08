'''dados = []
pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
print(pessoas[1])
test = []
test.append('gustavo')
test.append(40)
print(test)
galera = list()
galera.append(test[:])
test[0] = 'maria'
test[1] = 22
galera.append(test[:])
print(galera)'''
galera = list()
dados = list()
totalm = totalmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
        totalm += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmen += 1
print(f' temos {totalm} maiores e {totalmen} menores')