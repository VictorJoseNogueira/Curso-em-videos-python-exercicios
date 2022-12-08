c = 's'
cont = 0
homem = mulher = maior = mulhernova = 0
while True:
    print('-' * 20)
    c = str(input('vc gostaria de cadastrar alguem [S/N]? ')).strip().upper()[0]
    if c in 'Nn':
        break
    while c not in 'nNsS':
       print('-'*20)
       print('opção invalida ')
       print('-' * 20)
       c = str(input('vc gostaria de cadastrar alguem [S/N]? ')).strip().upper()[0]
    print('-' * 20)
    sexo = str(input('qual seu sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'FfMm':
        print('opção nao aceita ')
        sexo = str(input('qual seu sexo [M/F]: ')).strip().upper()[0]

    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff':
        mulher += 1
    idade = int(input('quantos anos vc tem ?'))
    if idade >= 18:
        maior += 1
    elif sexo in 'Ff' and idade < 18:
            mulhernova += 1

print(f' {homem} homens foram cadastrados')
print(f' {mulher} mulheres foram cadastrados')
print(f'{maior} sao maiores de idade')
print(f'temos {mulhernova} mulheres  menores de idade')