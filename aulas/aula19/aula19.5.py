'''pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
pessoas['nome'] = 'Leandro'
pessoas['Peso'] = 100
print(pessoas['nome'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
brasil = []
estado = {'UF': 'rio de janeiro', 'Sigla': 'RJ'}
estado2 = {'Uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil[0]['UF'])
'''
estado = {}
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
