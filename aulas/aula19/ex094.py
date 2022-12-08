pessoa = {}
galera = []
soma = media = cont = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('NOME: '))
    while True:
        pessoa['sexo'] = str(input('SEXO [M/F] :  ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!, por favor digite apenas M ou F')
    pessoa['idade'] = int(input('IDADE: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar ? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! por favor digite S ou N')
    if resp in 'Nn':
        break
print('-=-'*30)
print(galera)
for k, v in enumerate(galera):
    print(f'{k}: {v}')
#quantas
print('-=-'*30)
print(f'ao todos temos {len(galera)} pessoas cadastradas')
media = soma/len(galera)
print(f' a media das idades sao {media:5.2f}')
print('as mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
    print()
print(f' as pessoas acima da media de idade sao: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
print('encerrando...')